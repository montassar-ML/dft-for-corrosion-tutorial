# 05 · Exchange–correlation, dispersion and magnetic states

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Treat functional choice as a model to benchmark, not a list of universally improving corrections.

PBE is a widely used semilocal reference functional. Its practical usefulness does not imply accurate electron localization, molecular affinities, oxide band gaps or adsorption energies for every material. SCAN adds kinetic-energy-density dependence; screened hybrids mix short-range exact exchange. All require appropriate datasets and convergence settings. [3](../README.md#ref-3) [16](../README.md#ref-16) [55](../README.md#ref-55)

## Iron metal and iron oxides are different problems
A spin-polarized metallic Fe surface has partially filled bands and competing magnetic configurations. Many iron oxides require an explicit treatment of localized d states and ordered spin arrangements. A setup that reproduces metallic Fe is not automatically adequate for FeO, magnetite or hematite.

The local spin-density difference gives a magnetization density. For a collinear spin-only description:

```math
M_{\rm spin}=\mu_B\int[n_\uparrow(\mathbf r)-n_\downarrow(\mathbf r)]\,d\mathbf r.
```

A code's atom-resolved moments depend on its projection or spatial integration. Compare the same definition across structures, and do not interpret a surface-projected moment as a unique oxidation state.

## DFT+U: sensitivity, not cutoff convergence
The effective interaction depends on the correlated subspace and screening environment. Linear-response constructions provide one way to determine an effective interaction instead of tuning it to a desired adsorption ranking. [14](../README.md#ref-14)

Increasing U until a trend “converges” is not analogous to increasing a basis cutoff. Changing U changes the Hamiltonian. Separate a numerical convergence study at fixed U from a model-sensitivity/benchmark study across justified U choices. When comparing phases and defects, preserve reference consistency and explain the treatment of differently coordinated Fe atoms.

## Dispersion and inhibitor geometry
Large organic adsorbates may combine covalent/coordinate bonding with dispersion. A dispersion correction may alter orientation, contact area and energetics. It is not proof that adsorption is solely physical rather than chemical. Record the functional, correction and damping variant; do not double count dispersion with an already compatible nonlocal model. [15](../README.md#ref-15)

## A useful model-selection report
For each candidate level of theory, ask whether bulk geometry, magnetism, surface structure and relevant adsorption chemistry are credible. Comparison to experiment should account for temperature, facet and surface preparation. Agreement with a single number is not a broad validation.

Two independent uncertainties remain even after a good functional choice: the experimental interface might not be the simulated termination, and the experiment may probe a kinetic mixture rather than an equilibrium structure.

**Exercise:** A DFT+U calculation reproduces one oxide band gap but reverses adsorption ordering. What must be reported? Both results, the correlated subspace and U choice, numerical convergence, and the sensitivity of the mechanistic conclusion—not only the favorable band-gap benchmark.
