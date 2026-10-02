# 19 · Common mistakes and how to repair the inference

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Identify not just a suspicious result but the missing evidence required to repair the argument.

| Tempting statement | Why it is not established | Better next step |
|---|---|---|
| “The highest HOMO gives the best inhibitor.” | An isolated species is not the interface, coverage or rate model. | Check chemical state and test comparable surface/environment models. |
| “The gap decreased, so corrosion resistance increased.” | The gap is not an inhibition-efficiency observable; metallic interfaces have bands. | State which electronic feature changed and which mechanism it could influence. |
| “Bader proves a covalent bond.” | A partitioned charge is not a bond classification. | Combine geometry, density and appropriately projected bonding analysis. |
| “The molecule adsorbed most strongly, therefore it protects best.” | Dissolution, accessibility, film coverage and cathodic kinetics remain unspecified. | Compare competing adsorption/reaction processes and connect to experiment. |
| “Negative adsorption energy means spontaneous adsorption from water.” | The reference may be an isolated vacuum molecule, not solution. | Build a solvent/standard-state consistent free-energy cycle. |
| “The work function is the corrosion potential.” | Vacuum electron removal differs from a mixed electrode potential. | Define a calibrated electrode reference and reaction-current model. |
| “A vacancy energy is the dissolution barrier.” | Energy of a product defect is not the saddle-point or solution-ion free energy. | Define dissolution products/reservoirs and a pathway. |
| “No reaction in short AIMD proves a durable coating.” | Rare events may not occur on the sampled timescale. | Assess sampling and relevant barriers, and avoid lifetime claims. |
| “The same numerical U works for every Fe species.” | U depends on the correlated-subspace definition and environment. | Document the determination/benchmark and test model sensitivity. |
| “A normally ended run is a converged minimum.” | SCF, ionic, vibrational and physical-state checks differ. | Check each level explicitly. |

These cautions are consistent with critical corrosion-modeling literature, but the repairs in this table are this tutorial's methodological synthesis, not universal prescriptions from one review. [42](../README.md#ref-42) [33](../README.md#ref-33) [43](../README.md#ref-43)

## Model substitution without disclosure
Examples include calling pure Fe “steel,” a crystalline oxide “the passive film,” an adsorbed neutral Cl atom “aqueous chloride,” or an isolated imidazole tautomer “the inhibitor at every pH.” Each substitution changes the question. Make it visible in the methods and conclusions.

## Numerical mistakes that mimic chemistry
Inconsistent pseudopotentials, grids or smearing can shift small adsorption-energy differences. Unmatched fragment geometries can turn a charge-density difference into a structural deformation map. Different DOS references can create apparent peak shifts. A drifting vacuum potential can invalidate a work-function extraction. Repair numerical comparability before constructing a chemical story.

## Statistical mistakes in descriptor correlations
A fitted correlation from a small chemically related series may depend on the selected compounds, solvent and experimental conditions. Reusing related scaffolds across training and test sets can overestimate generalization. Report uncertainty, out-of-domain limits, controls and independent validation; do not call correlation proof of the proposed electron-transfer mechanism.

**Exercise:** Rewrite “larger electron transfer causes higher inhibition efficiency.” A defensible version is: “The chosen charge partition assigns a larger interfacial redistribution in configuration A than B; whether this promotes protective coverage or changes dissolution/cathodic rates requires additional evidence.”
