# 04 · Basis sets, pseudopotentials and PAW

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Identify which mathematical representation is being converged and which physical approximation is being changed.

For a plane-wave representation:

```math
\psi_{j\mathbf k}(\mathbf r)
=\sum_{\mathbf G}c_{j,\mathbf k+\mathbf G}
 e^{i(\mathbf k+\mathbf G)\cdot\mathbf r},\qquad
\frac{\hbar^2|\mathbf k+\mathbf G|^2}{2m_e}\le E_{\rm cut}.
```

A cutoff enlarges the basis systematically at fixed cell and dataset. Hard pseudopotentials need more basis resolution than softer ones; an arbitrary identical cutoff across unrelated datasets is not a proof of equivalent accuracy. Density and augmentation grids may need separate settings. [4](../README.md#ref-4)

## Core treatment is part of the method
Pseudopotentials replace chemically inactive core behavior by an effective operator. Norm-conserving and ultrasoft constructions make different numerical choices. PAW combines smooth auxiliary functions with atom-centered reconstruction; it should not be described as identical to a bare pseudopotential or as an unrestricted all-electron basis. Frozen-core and dataset choices still matter. [5](../README.md#ref-5) [6](../README.md#ref-6)

For Fe, choosing whether semicore states are explicitly included affects the reference electron count and numerical requirements. Use internally consistent datasets in bulk, surface and adsorbate calculations. Never compare raw total energies from different core treatments as though their arbitrary core references cancel.

## CP2K is not a plane-wave orbital cutoff in disguise
In the GPW approach, localized Gaussian functions describe orbitals while auxiliary grids represent density-related quantities. Improving the grid does not complete a small Gaussian orbital basis. Basis-family and cardinality tests belong beside grid tests. Different packages can be compared through converged observables and matched physical approximations, not equal numerical values of a cutoff keyword. [53](../README.md#ref-53)

## Basis-set superposition error
With localized bases, a fragment in the complex can borrow basis functions from its partner. Part of apparent binding can therefore be basis-set superposition error (BSSE). A frozen-fragment/ghost-basis comparison may diagnose it; its implementation and applicability must be checked for the code and periodic model. Do not apply a molecular counterpoise recipe blindly to every periodic metal calculation. State the convention and test the basis.

Plane waves at a common cell and cutoff do not have the same atom-centered basis-borrowing mechanism, but still have finite-basis, grid and dataset errors. “No conventional BSSE” does not mean “exact adsorption energy.”

## Forces and geometry
When a basis depends on nuclear positions, derivative contributions beyond a naive Hellmann–Feynman expression must be handled consistently. Variable-cell calculations introduce further basis changes. Converge stress for lattice optimization separately from adsorption energy at fixed cell.

**Self-check:** A new Fe dataset shifts every absolute energy by a large value. Is the chemistry necessarily different? Not from the shift alone. Compare balanced energy differences computed entirely within each dataset and examine convergence and physical observables.
