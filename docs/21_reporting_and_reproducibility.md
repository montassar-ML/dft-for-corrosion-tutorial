# 21 · Reporting, reproducibility and uncertainty

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Write a methods record that allows another researcher to reproduce both the numerical calculation and the interpretation.

## Minimum metadata
Record the code version, functional, dispersion model, pseudopotential/PAW identifiers and valence configurations, basis representation, relativistic treatment, spin settings, magnetic initial states and convergence thresholds. Name the actual U definition/subspace if used, not just a number. A code name plus “PBE” is not a reproducible method.

For surfaces include lattice provenance, Miller indices, lattice vectors, layer count, thickness, vacuum, termination, stoichiometry, constraints, lateral area, coverage, symmetry and electrostatic boundary treatment. Deposit the **final coordinates**, not only a picture. Preserve atom ordering when comparing densities or NEB images.

For every energy expression identify all reference systems, units, chemical states and thermal/solvation corrections. For electrochemistry name the electron/proton/ion reservoirs, potential reference, pH, standard states and constant-charge/potential treatment.

## Reproducibility is not only numerical settings
Document how initial adsorption geometries were chosen, which searches failed, which minima were duplicates and which magnetic states were retained. Reporting only the winning geometry hides search bias. Retain the decision log in the [case-study workflow](../case-study/workflow.md).

## Three uncertainty classes
| Class | Examples | Sensible test |
|---|---|---|
| Numerical | k-points, grid, force threshold, slab finite size | Tighten parameters and monitor the actual observable |
| Model | XC, dispersion, U, charge state, surface phase | Physically motivated alternatives and benchmarks |
| Sampling | adsorption starts, solvent arrangements, trajectories | More configurations / independent runs / statistical analysis |

These classes are not interchangeable. A tiny SCF tolerance cannot remove a wrong surface termination or insufficient solvent sampling. A difference smaller than its combined practical uncertainty should not be advertised as a strong ranking.

## An original reporting paragraph template
> Calculations used [version] with [functional and model corrections]. The [facet] surface was built from [bulk reference] using [cell and layers]. [Layers] were fixed; [vacuum/electrostatics] controlled periodic-image effects. Numerical parameters were tested against [adsorption energy/work function/etc.] to [declared criterion]. [Species and orientations] were relaxed from [search design]. Energies use [reference equation], with [thermal/solvation treatment]. Electronic analyses use [projection/density definitions]. The model omits [potential/solvent/film features], limiting conclusions to [scope].

## Public data discipline
Only release structures, results and scripts you own or have permission to redistribute. This tutorial includes no production results or proprietary software data. Citing a paper does not grant permission to copy its figures, inputs or raw results. An open software license does not automatically license every auxiliary dataset.

## What this repository has validated
Document links, citation consistency and selected algebraic identities are checked locally. No Fe adsorption calculation, experimental efficiency, DFT-code benchmark or scientific peer review is claimed. See [VALIDATION_REPORT.md](../VALIDATION_REPORT.md) for the actual checks and limitations.
