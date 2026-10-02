# Analysis plan and minimum evidence

[Case overview](README.md) · [Full analysis catalogue](../docs/24_analysis_catalogue.md)

## Core baseline analyses
| Analysis | Required inputs | Control | Conclusion available |
|---|---|---|---|
| Geometry/contact search | Multiple starts; allowed surface/molecule relaxation | Duplicate and magnetic-state checks | Distinct tested attachment motifs |
| Adsorption energy | Combined and separate references | Shared Hamiltonian; converged numerical strategy | Reference-specific binding preference |
| Spin PDOS | Adequate final electronic calculation | Projection and energy-reference consistency | Candidate Fe–molecule hybridization features |
| CDD | Combined and frozen-fragment grids | Alignment and integrated-electron conservation | Spatial redistribution |
| Bader populations | Suitable converged density | Charge sum; density convention | Partition-specific charge changes |
| Work function | Potential and Fermi level | Vacuum plateau, exposed face, dipole correction | Vacuum work-function response |
| Coverage sensitivity | Larger area / alternative overlayers | Consistent per-molecule and per-area accounting | Finite-cell versus overlayer effects |

These are the recommended core for the question we selected; they are not a universal checklist for every corrosion paper. Their meanings and caveats follow the methods and critical inhibitor literature. [18](../README.md#ref-18) [21](../README.md#ref-21) [33](../README.md#ref-33)

## Conditional analyses
**Deformation energy:** add when two motifs have different geometric distortion, or when stronger apparent contact does not lead to stronger net binding.

**ELF/COHP:** add to test a specific bonding hypothesis, and report projection/localization conventions. Do not add only to multiply figures.

**Vibrations:** add when verifying local stability or applying ZPE/entropy corrections. State whether the Hessian is full or restricted. A flat molecule's low modes can require more than a naive harmonic treatment.

**NEB:** add only after specifying a relevant elementary event, such as adsorption reorientation, dissociation or a surface reaction. A path without a corrosion-related mechanistic question is not automatically useful.

**AIMD/RDF:** add for questions involving explicit water and finite-temperature structure. Sampling, density normalization and accessible-volume definitions become part of the analysis.

**Surface/defect thermodynamics:** add when arguing about surface-phase or defect populations. A defect's attractive binding site must also be available under relevant conditions.

## Proposed analysis file schema
Use `worksheets/energies.csv` for raw/reference energies, `geometry.csv` for contacts and final states, `electronic_analysis.csv` for charge/work-function metadata, and `convergence.csv` for numerical tests. Every derived value should point to the source geometry and calculation/reference IDs.

Do not insert numbers from Fe(100) publications into these Fe(110) worksheets. Related studies justify questions and controls, not a substitute dataset. [45](../README.md#ref-45) [46](../README.md#ref-46)

## Minimum publication inference
A completed baseline could say “configuration A was lowest among the tested neutral vacuum Fe(110) states, with these electronic changes.” It could not say “A gives a particular inhibition efficiency in acid” without additional chemistry, kinetics and/or experimental evidence.
