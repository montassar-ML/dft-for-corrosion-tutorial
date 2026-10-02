# Workflow and decision log

[Case overview](README.md) · [Analysis plan](analyses.md) · [Expected outputs](expected_outputs.md)

## A gated investigation
```text
Question and experimental context
    |
    v
Define bare Fe(110) + neutral imidazole baseline
    |
    v
Bulk Fe: numerical convergence + magnetic branch
    |
    v
Slab: thickness + electrostatics + surface reference
    |
    v
Molecule: species + geometry + isolation
    |
    v
Multiple sites / orientations / magnetic starts
    |
    v
Distinct relaxed candidates + failed-start log
    |
    v
Consistent adsorption energies + uncertainty
    |
    +--> ordering unresolved? --> tighten controls / retain alternatives
    |
    v
Targeted PDOS + CDD/Bader + work-function analysis
    |
    v
Coverage / solvent / chemical-state sensitivity
    |
    v
Limited mechanistic conclusion + next evidence
```

## Before calculation
Write a model card describing what is intentionally absent. Assign immutable IDs to structures and references. Define how duplicate minima and convergence failures will be identified. Set numerical tolerances based on the intended comparison rather than reusing values from an unrelated system.

The worksheets in `worksheets/` are ordinary CSV files. They have headers only, except the model-card text file. Blank means **not calculated or not specified**, never zero. Do not fill cells with guessed example energies merely to create attractive plots.

## Decision-log entries
For each change record `date`, `model_id`, `question`, `change`, `reason`, `observable_checked`, `decision`, and `remaining_uncertainty`. Distinguish a numerical refinement from a new chemical/electrochemical model. A new protonation state is not merely another optimization setting.

## Recovery when a gate fails
A failed SCF or optimization is evidence that the state was not obtained, not an unfavorable adsorption energy. Preserve the attempted structure and failure reason. Re-examine geometry, magnetic state, occupations and numerical settings before interpreting. This course does not prescribe automatic keyword changes or job resubmission.

## Literature comparison record
For each comparison list paper DOI, facet, species/tautomer, charge treatment, coverage, functional, solvent, energy reference and what was actually accessible in the source. If these differ, compare the methodological idea or qualitative limitation instead of presenting a numerical reproduction.

## Final decision branches
- If several candidates are near-degenerate, analyze the plausible set and consider thermal/configurational populations rather than a single winner.
- If solvent reverses a vacuum ordering, report the reversal as model sensitivity; do not delete the vacuum result.
- If a final structure dissociates, redefine the products and balanced energy comparison. Do not compare it to intact adsorption without identifying the reaction.
- If the relevant experiment involves an oxide, the bare Fe model remains a controlled baseline; construct an appropriate oxide/interface model before claiming realism.
