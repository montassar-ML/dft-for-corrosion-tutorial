#!/usr/bin/env python3
"""Offline documentation QA; no DFT, network access, submission or file writes.

Run from any directory: python3 /path/to/repository/tools/check_repository.py
Checks links to local files/fragments, fences, math brace balance, bibliography
consistency, worksheet emptiness and selected algebraic conventions.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def outside_fences(text: str) -> tuple[str, list[str]]:
    """Return Markdown outside code fences and contained fenced math bodies."""
    out: list[str] = []
    maths: list[str] = []
    fence: str | None = None
    lang = ""
    block: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence is None and match:
            fence, lang = match.group(1), match.group(2).strip()
            block = []
        elif fence is not None and match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
            if lang == "math":
                maths.append("\n".join(block))
            fence = None
        elif fence is not None:
            block.append(line)
        else:
            out.append(line)
    if fence is not None:
        raise ValueError("Unclosed code fence")
    return "\n".join(out), maths


def anchors(text: str) -> set[str]:
    """Approximate GitHub heading slugs and include explicit HTML anchors."""
    clean, _ = outside_fences(text)
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', clean))
    seen: Counter[str] = Counter()
    for title in re.findall(r"^#{1,6}\s+(.+)$", clean, re.M):
        title = re.sub(r"<[^>]*>", "", title).strip().lower()
        title = re.sub(r"[^\w\-\s]", "", title)
        slug = re.sub(r"\s", "-", title)
        occurrence = seen[slug]
        seen[slug] += 1
        result.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return result


def main() -> int:
    errors: list[str] = []
    mds = sorted(ROOT.rglob("*.md"))
    texts = {p: p.read_text(encoding="utf-8") for p in mds}
    anchor_sets: dict[Path, set[str]] = {}
    maths: list[tuple[Path, str]] = []
    for p, text in texts.items():
        if b"\r\n" in p.read_bytes():
            errors.append(f"CRLF line endings: {p.relative_to(ROOT)}")
        if re.search(r"\[@[A-Za-z0-9_]+\]", text):
            errors.append(f"Unresolved citation token: {p.relative_to(ROOT)}")
        if any(old in text for old in ("\\[", "\\]", "\\(", "\\)", "$$")):
            errors.append(f"Legacy math delimiter: {p.relative_to(ROOT)}")
        try:
            anchor_sets[p.resolve()] = anchors(text)
            _, blocks = outside_fences(text)
            maths.extend((p, b) for b in blocks)
        except ValueError as exc:
            errors.append(f"{p.relative_to(ROOT)}: {exc}")

    link_count = 0
    for p, text in texts.items():
        try:
            clean, _ = outside_fences(text)
        except ValueError:
            continue
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", clean):
            if urlsplit(target).scheme or target.startswith("//"):
                continue
            link_count += 1
            target = unquote(target)
            filename, _, fragment = target.partition("#")
            dest = (p.parent / filename).resolve() if filename else p.resolve()
            if not dest.is_relative_to(ROOT.resolve()):
                errors.append(f"Escaping local link: {p.relative_to(ROOT)} -> {target}")
            elif not dest.exists():
                errors.append(f"Missing local link: {p.relative_to(ROOT)} -> {target}")
            elif fragment and fragment not in anchor_sets.get(dest, set()):
                errors.append(f"Missing anchor: {p.relative_to(ROOT)} -> {target}")

    for p, block in maths:
        depth = 0
        # Ignore escaped literal braces, but retain ordinary grouping braces.
        value = re.sub(r"\\[{}]", "", block)
        for c in value:
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth < 0:
                    break
        if depth != 0:
            errors.append(f"Math brace imbalance: {p.relative_to(ROOT)}")
        starts = re.findall(r"\\begin\{([^}]+)\}", block)
        ends = re.findall(r"\\end\{([^}]+)\}", block)
        if starts != list(reversed(ends)) and starts != ends:
            errors.append(f"Math environment imbalance: {p.relative_to(ROOT)}")

    refs = json.loads((ROOT / "references.json").read_text(encoding="utf-8"))
    keys = [r["key"] for r in refs]
    dois = [r["doi"].lower() for r in refs]
    bib = (ROOT / "references.bib").read_text(encoding="utf-8")
    bib_keys = re.findall(r"@article\{([^,]+),", bib)
    bib_dois = [d.lower() for d in re.findall(r"\bdoi\s*=\s*\{([^}]+)\}", bib)]
    if len(set(keys)) != len(keys) or len(set(dois)) != len(dois):
        errors.append("Duplicate bibliographic keys or DOIs")
    if bib_keys != keys or bib_dois != dois:
        errors.append("BibTeX and reference JSON disagree")
    if any(not re.match(r"^10\.\d{4,9}/\S+$", d, re.I) for d in dois):
        errors.append("Malformed DOI")
    with (ROOT / "reference-verification.csv").open(encoding="utf-8", newline="") as f:
        ledger = list(csv.DictReader(f))
    if [r["doi"].lower() for r in ledger] != dois:
        errors.append("Verification ledger does not match bibliography")
    for i in range(1, len(refs)+1):
        if f"ref-{i}" not in anchor_sets.get((ROOT / "README.md").resolve(), set()):
            errors.append(f"Missing numbered reference anchor {i}")

    cardtext = texts[ROOT / "docs/24_analysis_catalogue.md"]
    for label in ("1. What is calculated", "2. Equation or definition", "3. Physical meaning", "4. Corrosion question", "5. Justified conclusion", "6. Conclusion not established", "7. Common mistakes", "8. Typical output"):
        if cardtext.count(label) != 26:
            errors.append(f"Analysis card coverage: {label}")

    worksheets = sorted((ROOT / "case-study/worksheets").glob("*.csv"))
    for p in worksheets:
        with p.open(encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        if len(rows) != 1 or not rows[0]:
            errors.append(f"Worksheet should be header-only: {p.name}")

    # Exact arithmetic checks of identities, with arbitrary numbers used ONLY
    # as software test inputs. They are not scientific data or example results.
    algebra_checks = 0
    for combined, surface, molecule, sfrozen, mfrozen in [(F(-10),F(-7),F(-2),F(-6),F(-1)), (F(3,2),F(-9,7),F(1,3),F(-2,5),F(4,9))]:
        adsorption = combined-surface-molecule
        interaction = combined-sfrozen-mfrozen
        deformation = sfrozen-surface+mfrozen-molecule
        assert adsorption == interaction+deformation
        algebra_checks += 1
    for n,e,u,tph in [(2,F(1),F(-1,2),F(1,4)),(1,F(3,2),F(2,3),F(5,7))]:
        u_rhe=u+tph/e
        assert n*e*u+n*tph == n*e*u_rhe
        algebra_checks += 1
    mu,eta=F(-3),F(4)
    dn=-mu/eta
    assert -(mu*dn+eta*dn*dn/2) == mu*mu/(2*eta)
    assert 1/eta == 1/(2*(eta/2))
    algebra_checks += 2
    assert (F(12)-F(5)-F(7)) == 0  # Electron-number CDD integral bookkeeping.
    algebra_checks += 1

    print(f"Markdown files checked: {len(mds)}")
    print(f"Relative file/anchor links checked: {link_count}")
    print(f"Fenced math blocks checked: {len(maths)}")
    print(f"Unique bibliography/ledger DOI records: {len(refs)}")
    print("Analysis cards checked: 26, with all eight pedagogical fields")
    print(f"Blank CSV worksheets checked: {len(worksheets)}")
    print(f"Exact-arithmetic identity checks: {algebra_checks}")
    if errors:
        print("FAILED:", file=sys.stderr)
        for e in errors:
            print("- "+e, file=sys.stderr)
        return 1
    print("PASS: offline documentation checks. Not DFT or external-link validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
