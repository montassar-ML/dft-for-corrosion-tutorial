# 01 · DFT foundations

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Explain what is minimized in a DFT calculation, what an orbital eigenvalue is, and why none of those quantities is itself a corrosion rate. This chapter uses nonrelativistic, collinear-spin notation; spin–orbit coupling and generalized Kohn–Sham operators require extensions.

## From the many-electron problem to a density
With the nuclei fixed at positions R, the electronic Hamiltonian contains kinetic energy, electron–nucleus interaction, and electron–electron repulsion. The Born–Oppenheimer approximation separates the fast electronic problem from nuclear motion. The electronic energy must be supplemented by the nucleus–nucleus interaction to form the energy surface used for geometry optimization.

The Hohenberg–Kohn framework establishes a ground-state density description for a fixed external potential and electron number, subject to the theorem's conditions. It is not a statement that an arbitrary approximate functional is exact, or that a particular SCF solver will find the physically desired state. Degeneracy, representability, spin and finite-temperature ensembles require care beyond the elementary theorem. [1](../README.md#ref-1)

In atomic units, an instructive Kohn–Sham energy decomposition is:

```math
E_{\mathrm{BO}}[n;\mathbf R]
=T_s[n]+\int v_{\mathrm{ext}}(\mathbf r;\mathbf R)n(\mathbf r)\,d\mathbf r
+E_H[n]+E_{xc}[n]+E_{\mathrm{II}}(\mathbf R).
```

Here `Ts` is the auxiliary noninteracting kinetic energy, `EH` the classical Hartree energy, and `Exc` includes exchange, correlation and the difference between interacting and noninteracting kinetic energies. `EII` is the ion–ion term. In periodic implementations, the electrostatic terms are evaluated under consistent lattice-sum and neutrality conventions; they are not independent divergent sums to be added manually.

The auxiliary orbitals solve a self-consistent eigenproblem. For a local spin-dependent effective potential:

```math
\left[-\frac12\nabla^2+v_{\mathrm{ext}}(\mathbf r)
+v_H[n](\mathbf r)+v_{xc,s}[n_\uparrow,n_\downarrow](\mathbf r)\right]
\psi_{j\mathbf k s}=\varepsilon_{j\mathbf k s}\psi_{j\mathbf k s}.
```

The band index is `j`, the spin channel is `s`, and the electron density is `n`. With Brillouin-zone weights normalized consistently with cell-normalized orbitals:

```math
n_s(\mathbf r)=\sum_{\mathbf k}w_{\mathbf k}\sum_j
f_{j\mathbf k s}|\psi_{j\mathbf k s}(\mathbf r)|^2,
\qquad \int_{\rm cell}n(\mathbf r)\,d\mathbf r=N_e.
```

PAW, nonlocal pseudopotentials and hybrid functionals introduce nonlocal operators or generalized eigenproblems. The compact equation above is a teaching model, not literal source code for every package. [2](../README.md#ref-2) [5](../README.md#ref-5) [6](../README.md#ref-6)

## What self-consistency establishes
A trial density defines a potential, which produces orbitals and a new density. Mixing or minimization continues until residuals meet chosen tolerances. Geometry optimization then changes nuclear coordinates using forces from the converged electronic problem. These are two separate convergence loops.

An SCF-converged ferromagnetic state and another SCF-converged magnetic arrangement may have different energies. Similarly, two geometries can both be local minima. Test physically motivated alternatives instead of interpreting the first successful run as the global minimum.

## What eigenvalues do not establish
The DFT total energy is not simply the sum of occupied eigenvalues: double-counting corrections and ion terms matter. Nor is the ordinary Kohn–Sham gap generally identical to the fundamental or optical gap. The exact energy has a derivative discontinuity as electron number crosses an integer; approximate functionals need not reproduce it. [13](../README.md#ref-13)

For a metal surface, an isolated inhibitor's molecular gap is therefore not a gap of the combined interface and cannot be converted into an inhibition efficiency.

## Self-check
**Question:** A calculation prints a small SCF residual but large forces. Is the surface relaxed?

**Answer:** No. Electronic convergence concerns the density at the current geometry. Nuclear relaxation requires its own force/displacement checks. Neither condition verifies the correct surface termination, magnetic state or electrolyte model.
