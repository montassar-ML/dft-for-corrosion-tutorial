# Contributing

[Course home](README.md)

Contributions should improve physical correctness, explanatory clarity, reproducibility or literature attribution. Keep the material in English and theory-focused.

## A scientific correction
State the disputed sentence/equation, explain the problem, provide a primary methodological paper or official documentation, and propose replacement wording. Distinguish a genuine error from an alternative convention. For hardness, charge sign, energy reference or electrode potential, supply the full defining equation.

## A literature addition
Provide a real DOI, title, author/year match and the precise claim it supports. Identify whether you accessed full text, selected sections, abstract or metadata. A review can map a field; a source-specific empirical claim should lead to the actual study.

## A case-study extension
Do not label new results as established tutorial benchmarks until the calculations, settings, reference states and validation are supplied. Keep provenance and permissions explicit. Report unsuccessful/ambiguous outcomes as well as favorable ones.

## Documentation checks
Run `python3 tools/check_repository.py` from the repository root. This validates local documentation structure and selected algebraic bookkeeping tests. It does not execute DFT, establish literature permissions, validate all external redirects or replace scientific review.

Use fenced math blocks, explicit stable anchors for manually maintained navigation, and relative links between local files. Do not add a generated image that resembles a computed PDOS or density map without making its schematic status unmistakable.
