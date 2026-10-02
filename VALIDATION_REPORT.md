# Validation report · Version 0.1.0

Prepared: **1 October 2026**

## What this release is
A theory-led educational repository, an original proposed Fe(110)/imidazole investigation, and ten figure-design briefs. It contains **no DFT result dataset, numerical inhibition ranking, executed case-study calculation or rendered scientific-result image**.

## Automated local checks performed
The distributed checker is [tools/check_repository.py](tools/check_repository.py). It uses the Python standard library, reads local files and does not execute calculations, contact a network, submit jobs or modify files.

| Check | Result / scope |
|---|---|
| Markdown structure | All 52 Markdown files checked for balanced fences |
| Local navigation | Relative file links and target anchors checked; rerunnable checker prints the exact current count |
| Equations | 82 nonempty fenced `math` blocks; balanced braces/environments and no legacy math delimiters in Markdown |
| Citation references | No unresolved draft citation tokens; all numbered reference anchors present |
| Bibliography consistency | 55 unique DOI records match JSON, BibTeX and verification ledger |
| Analysis catalogue | 26 entries each contain all eight required pedagogical components |
| Case-study worksheets | Six CSV files contain headers only; no invented result rows |
| Encoding | Markdown checked as UTF-8 with LF line endings |
| Exact arithmetic | Seven bookkeeping/convention checks passed |

An independent CommonMark parser also parsed all Markdown and recognized the 82 math fences. `CITATION.cff` was loaded as YAML, with maintainer and version fields inspected. These checks are not a live preview on GitHub.

## Independent symbolic checks performed
Four SymPy identity checks passed during preparation:

1. Adsorption energy equals interaction plus deformation for the declared references.
2. The matched-pair SHE expression transforms to the RHE expression without a second pH term.
3. The minimum of the stated smooth quadratic electron-response approximation occurs at `deltaN=−mu/eta_c`.
4. Its stabilization magnitude is `mu²/(2 eta_c)`.

These symbolic checks are an editorial supplement, not a proof of physical applicability of the approximations. SymPy is not required to read the repository or run its distributed standard-library checker.

## Scientific convention review
The review specifically checked the ion–ion term in the total-energy expression; band versus density notation; electron-number CDD sign; frozen-fragment reference requirements; hardness prefactors; surface-energy symmetry assumptions; work-function electron-energy convention; SHE/RHE signs; ZPE accounting; and distinction between program completion, stationary states, and experimental corrosion performance. See [MATH_CONVENTIONS.md](MATH_CONVENTIONS.md).

The case study distinguishes Fe(110) from Fe(100) literature, isolated neutral imidazole from other protonation states, and bare metal from realistic passive films. The worksheets deliberately do not assume adsorption ordering or a favorable sign of charge/work-function change.

## Reference verification scope
The [verification ledger](reference-verification.csv) records a bibliographic evidence URL and access description for all 55 DOI entries. Most were cross-checked on publisher or author/official records; some inaccessible originals were checked against bibliographic records or publisher reference lists. Optional unverified fields were not fabricated.

This is **DOI/title metadata verification**, not a claim that every full text and supporting information file was accessible or fully reviewed. Publisher redirects and access controls are not covered by an all-sites HTTP guarantee. See [SOURCES.md](SOURCES.md) for limitations and the separation between source findings and original course design.

## Not performed / not claimed
- No VASP, Quantum ESPRESSO, CP2K, GPAW, CASTEP or ABINIT run.
- No optimized Fe/imidazole structure, adsorption-energy result, PDOS, charge map, barrier or AIMD trajectory.
- No experimental corrosion measurement or predicted inhibition efficiency.
- No formal independent scientific peer review.
- No live GitHub publication, browser-render check or automatic upload.
- No journal-figure reproduction or generation of realistic-looking fake numerical plots.

A maintainer should still review the scientific narrative and source-specific statements before treating the course as a publication or an experimental design authority.

## Rerun
From the extracted repository root:

```bash
python3 tools/check_repository.py
```

On a Windows Python installation the equivalent command may be `python tools/check_repository.py`. This is documentation QA, not a DFT execution command.
