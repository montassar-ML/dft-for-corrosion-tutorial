# 14 · Solvent, aggressive ions and chemical reservoirs

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Understand what is and is not represented when a calculation adds water or chloride.

An implicit solvent supplies an averaged dielectric or related response without resolving individual solvent molecules. Explicit water can represent hydrogen bonds, coordination and molecular rearrangement, but a single water configuration is only one microstate. Hybrid explicit/implicit models can separate a chemically structured first layer from an averaged outer environment. None removes the need for sampling and reference-state consistency. [24](../README.md#ref-24) [38](../README.md#ref-38)

## Water adsorption versus a liquid interface
Placing one water molecule on Fe probes a selected adsorption configuration. A water-covered surface, a finite water film, and a liquid-equilibrated electrode differ in coverage, entropy, screening and allowed chemistry. Iron–water calculations across facets and electrochemical conditions provide a relevant example of why speciation and thermodynamic conditions matter. Their findings do not substitute for a simulation of an inhibitor-containing electrolyte. [48](../README.md#ref-48)

Distinguish lack of spontaneous dissociation during geometry relaxation from unfavorable dissociation thermodynamics. Relaxation can stay behind a barrier. A comparison of final-state energies addresses a different question from a dynamical trajectory or transition-state search.

## Chloride is not a neutral chlorine atom
An isolated chlorine atom, gas-phase Cl2 and hydrated chloride are distinct references. Adding a negative ion to a periodic model demands charge compensation and electrostatic conventions. A uniform background can create cell-size-dependent artifacts; an arbitrary ionic energy subtraction can therefore produce a misleading adsorption number.

Chloride may compete with inhibitors, alter hydration, interact with defects or affect a passive film. Which mechanism is relevant depends on the metal and surface state. A computation on oxidized copper is informative about model design but is not direct evidence for chloride-induced breakdown on an Fe oxide. [49](../README.md#ref-49)

## Speciation and concentration
Protonation changes molecular charge and often the donor atom's chemical availability. The relative amounts of neutral, protonated or deprotonated species depend on acid–base equilibria, solvent and activity. Surface binding can shift those equilibria. Treat neutral imidazole as a controlled baseline and explicitly extend to other states before claiming acidic corrosion relevance.

A realistic adsorption comparison includes exchange with reservoirs. Write all water, protons, electrons and ions in the balanced reaction. Do not infer that a negatively charged adsorbate must bind best to every nominally positive surface without a calibrated interfacial model.

## Sampling and interpretation
Use multiple solvent arrangements, not only the most visually appealing snapshot. Examine energy/structural distributions, equilibration, convergence with water-layer thickness and finite-size effects. A few-picosecond trajectory can illustrate local behavior but cannot establish long-term inhibition or passivity.

**Self-check:** Does adding a continuum dielectric impose experimental pH? No. Dielectric screening and proton chemical potential are different physical ingredients.
