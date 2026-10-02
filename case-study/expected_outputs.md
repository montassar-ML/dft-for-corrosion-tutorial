# Expected output types — no numerical results supplied

[Case overview](README.md) · [Workflow](workflow.md)

## How to read this page
“Expected” means the **kind of deliverable to produce**, not an expected value, sign or ordering. The study is not executed in this repository. No attractive illustrative curve should be mistaken for calculated data.

| Output | Must contain | A useful interpretation question |
|---|---|---|
| Bulk record | Lattice, volume/energy, magnetic branch, stress/convergence | Is the surface reference self-consistent? |
| Slab views | Cell vectors, area, layer/fixed-atom labels and vacuum | Is this really the intended facet and termination? |
| Search table | Starts, outcomes, unique-minimum IDs and failures | Did the search explore physically different states? |
| Energy ledger | Total/reference energies, units, state IDs and uncertainties | Is a ranking meaningful and reference consistent? |
| PDOS plots | Spin, selected orbitals, normalization and energy zero | Is mixed orbital character supported rather than visually assumed? |
| CDD plots | Frozen references, grid, density convention and matched isovalue magnitudes | Where are electrons redistributed? |
| Bader table | Populations, charge definition, sum and grid test | Are assigned changes charge consistent? |
| Potential/work-function plot | Electron potential energy versus normal distance, plateau and Fermi level | Is vacuum referencing valid on the chosen face? |
| Coverage comparison | Molecule count, area, arrangement and chemical state | Does lateral interaction alter the interpretation? |
| Environment sensitivity | Solvent/ion/proton/electron references and sampling | Does the vacuum mechanism survive the added physics? |

## Interpretation branches instead of predetermined outcomes
**Binding:** if the strongest contact requires large deformation, net adsorption may be less favorable than expected. The energy decomposition tests that explanation.

**Charge:** strong spatial polarization can coexist with a small adsorbate Bader change. This is not a contradiction: CDD and basin integration answer different questions.

**PDOS:** a new feature can have mixed Fe and molecule character without being uniquely attributable to one bond. A validated bonding projection can help, but does not become a measured bond energy.

**Work function:** either sign of shift may occur; interpret the dipole/electronic redistribution actually calculated. Do not prelabel an increasing or decreasing work function as protective.

**Environment:** an aqueous, protonated or oxidized model may change adsorption motifs. Report model dependence rather than treating it as a failed attempt to confirm the vacuum result.

## End-of-case written assignment
Write an abstract with four clearly separated sentences: (1) physical question and model; (2) numerical and sampling controls; (3) observations and limited mechanism; (4) unresolved environment/kinetic connection. Keep all placeholders until actual calculations supply evidence.

## Worksheet conventions
CSV columns ending `_eV`, `_A`, `_A2`, `_muB`, or `_electrons` declare units. Preserve more digits in raw machine output than in reported results, but do not imply corresponding physical accuracy. The model card should define all nonstandard fields. Missing values are left empty, not assigned zero or a guessed uncertainty.
