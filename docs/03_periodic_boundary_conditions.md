# 03 · Periodicity, k-points and metallic occupations

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Separate real crystallographic periodicity from artificial periodic images of a model surface.

A lattice translation R leaves a crystal potential unchanged. Bloch orbitals contain a plane-wave phase and a cell-periodic factor:

```math
v(\mathbf r+\mathbf R)=v(\mathbf r),\qquad
\psi_{j\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{j\mathbf k}(\mathbf r).
```

The cell fixes the reciprocal lattice. A finite weighted set of k-points approximates Brillouin-zone integrals. The quality needed depends on the real-space cell, symmetry, metallicity, occupied states and target observable—not just atom count. Monkhorst–Pack sampling gives a systematic family of meshes. [7](../README.md#ref-7)

## What a slab repeats
A conventional plane-wave slab repeats the solid laterally and repeats a slab-plus-vacuum cell normal to the surface. Its two exposed faces may be equivalent, inequivalent or differently covered. Increasing vacuum addresses interaction normal to the slab; increasing lateral area addresses adsorbate-image interaction. Increasing slab thickness addresses the finite depth of the solid. None substitutes for another.

For a sufficiently separated slab with its normal along a cell direction, a mesh with one point along that direction is usual. This does **not** remove the need for lateral k-point convergence. A large metallic cell is not automatically converged at Gamma.

## Why metals are demanding
At zero temperature the occupancy changes discontinuously at the Fermi energy. Smearing smooths numerical integration and can help iterative stability. Common numerical treatments include Gaussian, Methfessel–Paxton and Fermi–Dirac occupations; tetrahedron methods provide another integration strategy. [8](../README.md#ref-8) [9](../README.md#ref-9)

In Fermi–Dirac form:

```math
f(\varepsilon)=\frac{1}{1+\exp[(\varepsilon-\mu_e)/(k_BT_e)]}.
```

`Te` is an electronic occupation temperature. Choosing it to improve numerical behavior is not a way to impose aqueous temperature or obtain molecular entropy. Compare consistent energy definitions: a smeared electronic free energy, an internal energy and an extrapolated zero-smearing energy are not interchangeable labels.

## Practical thought experiment
Repeat a primitive surface cell twice in each lateral direction, keeping equivalent physical sampling density. Fewer k-points may then be needed, but four times the area changes the coverage if the number of adsorbates stays fixed. You have changed both a numerical representation and, potentially, the physical model. Document which question the comparison is intended to answer.

## Electrostatic warning
A three-dimensionally repeated charged cell with a neutralizing background is not automatically a charged electrode screened by solution. Slab electrostatics, compensation and potential reference need an explicit model; see the electrochemistry chapter.

**Self-check:** Doubling vacuum changes adsorption energy significantly. What follows? The original normal-image electrostatics or density tails were not adequately controlled; investigate rather than simply adopting a familiar vacuum number.
