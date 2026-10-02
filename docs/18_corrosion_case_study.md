# 18 · Case study: imidazole on Fe(110)

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Turn a chemical hypothesis into a staged investigation, with a decision gate before each new analysis.

**Teaching hypothesis:** a neutral imidazole molecule can form a site-dependent interaction with a specified bare, ferromagnetic bcc Fe(110) surface. The initial question is which geometries are locally stable and how their binding is expressed in density and electronic structure. This is deliberately narrower than claiming inhibition of steel corrosion in an acidic electrolyte.

## Literature boundary
Camacho-Mendoza and co-workers investigated imidazole derivatives using isolated-molecule and iron-surface calculations; the Fe(110) model makes this a relevant methodological precedent. It does not validate our as-yet uncomputed geometry or adsorption ordering. [44](../README.md#ref-44)

Other instructive papers describe imidazole film formation or hydrogen-bond networks on **Fe(100)**. Facet, chemical state and coverage affect what those calculations mean. Here those studies motivate questions about dissociation and cooperative adsorption; they are not numerical benchmarks for Fe(110). [45](../README.md#ref-45) [46](../README.md#ref-46)

## Sequence and deliverables
| Phase | Question | Minimum deliverable | Do not proceed until |
|---|---|---|---|
| Bulk Fe | Is the chosen lattice/magnetic state internally consistent? | Energy–volume and moment records | Numerical and magnetic checks are documented |
| Fe(110) slab | Are the two surfaces and finite-size effects controlled? | Cell, layers, terminations, area, work-function profile | Slab/vacuum/lateral convergence is adequate |
| Isolated molecule | What species is being adsorbed? | Neutral tautomer/conformer, electron count and reference energy | Charge, multiplicity and geometry are justified |
| Configuration search | Which sites/orientations survive relaxation? | Final structures and duplicate map | Several physically plausible starts are tested |
| Energetics | Which tested configurations bind more favorably? | Consistent adsorption/deformation energies | States and energy references are comparable |
| Electronic response | Where does the interface change? | Spin PDOS, CDD, Bader and work function | Densities/projections/reference alignment are valid |
| Environment | Does the vacuum inference persist? | Water/protonation/coverage sensitivity plan | Reservoirs and electrostatic treatment are explicit |

## Study design, not a completed calculation
This repository supplies a protocol, interpretation criteria and empty worksheets. No lattice constant, adsorption energy, charge transfer, work-function shift, ranking or inhibition efficiency is asserted as a result of this tutorial.

The full protocol is in [case-study/README.md](../case-study/README.md). Its [analysis plan](../case-study/analyses.md) explains which calculations are essential and which are conditional extensions. Its [expected outputs](../case-study/expected_outputs.md) describe deliverables without fabricating values.

**Checkpoint:** Before constructing a slab, write one sentence stating surface composition, facet, charge model, environment and question. If any is undefined, “DFT for corrosion” is not yet a reproducible study design.
