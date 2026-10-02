# 02 · Molecular versus periodic DFT

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Choose a model from the question rather than from the descriptor that is easiest to compute.

| Question | Natural starting model | Missing information |
|---|---|---|
| Where is a molecule electron-rich? | Isolated or solvated molecular DFT | Specific metal coordination and interface screening |
| Which inhibitor orientation binds on Fe? | Explicit periodic metal–molecule interface | Electrolyte, potential and film kinetics unless added |
| Which protonation state adsorbs? | Aqueous speciation plus interface free energies | Concentration and reservoir conventions must be specified |
| Does an inhibitor reduce corrosion current? | Mechanistic interface model plus kinetics and experiment | Cannot be answered from one orbital or adsorption energy |

Molecular DFT is useful for conformers, protonation alternatives, charge distributions and testable bonding hypotheses. It is not made irrelevant by periodic DFT. The two models answer different questions. The optimistic descriptor-oriented overview by Obot and co-workers and the critical analyses by Kokalj should be read together rather than used as interchangeable endorsements of a universal ranking rule. [41](../README.md#ref-41) [42](../README.md#ref-42)

## Ionization energy and electron affinity
At the fixed neutral geometry R0, define vertical energy differences:

```math
I_v=E_{N-1}(\mathbf R_0)-E_N(\mathbf R_0),\qquad
A_v=E_N(\mathbf R_0)-E_{N+1}(\mathbf R_0).
```

Relaxing each charge state's geometry instead gives adiabatic quantities. Specify the relevant spin states, solvent treatment and whether the anion is bound. A basis incapable of representing diffuse density can give misleading affinities. Approximate relations such as `I ≈ −εHOMO` and `A ≈ −εLUMO` are orbital estimates, not replacements for measured ionization and electron-addition energies. [13](../README.md#ref-13)

## Explicit convention for conceptual descriptors
This tutorial uses the **curvature convention** for hardness:

```math
\mu\approx-\frac{I+A}{2},\qquad
\chi=-\mu,\qquad
\eta_c\approx I-A,\qquad
S_c=\eta_c^{-1},\qquad
\omega_c=\frac{\mu^2}{2\eta_c}.
```

These are descriptors of a specified electronic model. In a smooth quadratic approximation, `ΔE ≈ μΔN + ηc(ΔN)²/2`. Minimizing this parabola yields the stabilization magnitude used in `ωc`. The exact integer-electron theory is not a smooth parabola; the approximation must remain visible.

The **half-gap hardness** convention `ηh=(I−A)/2` is also common. Because `ηc=2ηh`, the same curvature-derived index would be `μ²/(4ηh)` and the same response softness would be `1/(2ηh)`. Some papers define different named indices using other prefactors. Record the actual formula, not only the word “hardness,” “softness” or “electrophilicity,” before comparing values. No convention produces a universal corrosion-efficiency law. [10](../README.md#ref-10) [11](../README.md#ref-11) [12](../README.md#ref-12)

## Local reactivity and electrostatic maps
At fixed nuclei and external potential, finite-difference Fukui functions are:

```math
f^+(\mathbf r)\approx n_{N+1}(\mathbf r)-n_N(\mathbf r),\qquad
f^-(\mathbf r)\approx n_N(\mathbf r)-n_{N-1}(\mathbf r).
```

Condensed functions depend on the partitioning scheme. Using net atomic charges instead of electron populations reverses the sign of population differences. An electrostatic-potential map describes interaction with a test charge under its stated reference; it is not a measured adsorption-energy map.

## Why the interface can change the inference
Adsorption broadens molecular states, polarizes density, screens charges and may change molecular geometry or connectivity. Water and ions compete for sites; protonation changes donor availability. An Fe oxide and metallic Fe need not bind the same molecule in the same way. A favorable isolated descriptor is a hypothesis about reactivity, not evidence of a protective film.

**Checkpoint:** Rewrite “the smallest HOMO–LUMO gap proves the best inhibitor.” A defensible replacement is: “the molecular calculation suggests a different electronic response; surface binding, speciation and inhibition measurements are needed to establish relevance.”
