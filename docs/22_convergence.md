# 22 · Convergence and model sensitivity

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Design a convergence study around a corrosion-relevant observable rather than a universal input recipe.

## Define a decision tolerance first
Choose a justified tolerance `epsilon_Q` for each quantity Q before screening configurations. Different applications may require different tolerances. A nearly degenerate ordering requires tighter controls than identifying an unmistakably different structural motif. Do not assume an error per atom is an adequate bound for the adsorption-energy difference.

```math
\delta Q(x)=|Q(x)-Q(x_{\mathrm{ref}})|.
```

Here `x_ref` is a sufficiently demanding comparison setting, not a declaration that its result is exact. Test neighboring refinements to ensure an apparent plateau is not accidental.

## Numerical test matrix
| Parameter | What changes | Watch especially | Common confounder |
|---|---|---|---|
| Orbital basis / plane-wave cutoff | Variational representation of wavefunctions | Binding differences and forces | Grid convergence mistaken for Gaussian basis completeness |
| Density/augmentation grid | Representation of products/density | Bader charge, forces, CDD | Coarse partition grid despite converged total energy |
| k-points | Brillouin-zone integration | Fe energy, moments, work function | Mesh changes entangled with smearing |
| Smearing width/type | Occupations and electronic entropy | Metal forces, energy reference, magnetic state | Comparing different energy-like output fields |
| Slab layers | Recovery of bulk-like interior | Surface energy, moment, binding, work function | Fixed-layer policy changed simultaneously |
| Vacuum / Coulomb treatment | Repeated-slab electrostatics | Vacuum plateau and dipole | One empty-region k-point mistaken for electrostatic isolation |
| Lateral cell | Adsorbate/defect periodic separation | Coverage dependence and image interactions | A physical coverage change mislabeled only a numerical error |
| SCF thresholds | Electronic solution accuracy | Force noise and energy differences | Unconverged electronic steps inside otherwise finished run |
| Force threshold | Nuclear stationarity | Geometry ordering, frequencies | Small residual forces in wrong local minimum |
| Empty bands | Unoccupied-state completeness | Smearing, PDOS, response | Sufficient ground-state energy but truncated analysis |
| Hessian displacement | Finite-difference curvature | Frequencies, low modes, TS | SCF noise competing with small displacement forces |

Reciprocal-space and metallic integration choices have established methodological foundations, but numerical meshes cannot be copied from a paper without considering cell shape, size and observable. [7](../README.md#ref-7) [8](../README.md#ref-8) [9](../README.md#ref-9)

## A practical sequence
First converge a plausible bulk magnetic branch; determine a consistent lattice and bulk reference. Then converge clean-surface thickness/electrostatics. Test an adsorbed geometry as well: the combined interface can demand greater accuracy than the clean slab. After initial search, re-evaluate close competitors with tighter shared settings.

Use a fixed-geometry series to isolate electronic numerical effects, followed by checks that tighter settings do not materially change relaxation. Otherwise changing geometry and quadrature simultaneously can obscure the origin of a trend.

## CP2K versus pure plane waves
In GPW, Gaussian basis completeness and auxiliary-grid cutoffs are separate. Converge both orbital basis and the `CUTOFF`/`REL_CUTOFF` pair. In plane-wave/PAW approaches, wavefunction and density/augmentation representations also require their own checks. None of these cutoffs has a universally transferable numerical value. [53](../README.md#ref-53) [4](../README.md#ref-4) [6](../README.md#ref-6)

## Magnetic states, U and XC are not convergence dials
Increasing a k mesh normally refines the same numerical approximation. Changing a functional, U, spin state or solvation cavity changes the physical model or state being compared. Keep a separate sensitivity table rather than calling the lowest result “most converged.” Test alternative Fe moments and oxide occupation patterns; the first stationary electronic solution may not be the relevant branch. [14](../README.md#ref-14)

## Coverage is partly physics
Enlarging the lateral cell at fixed molecule count approaches dilute coverage. That removes some periodic-image interaction but also changes the physical adsorbate density. Report both the dilute-limit test and intended finite coverage. An experimental concentration cannot be assigned from one periodic coverage without an adsorption/speciation model.

## Exercise
Suppose work function changes little with cutoff but its vacuum plateau remains sloped. Which test should come next? Check slab dipole/electrostatic treatment and vacuum, not simply increase cutoff again. A stable number extracted from an inappropriate reference region is not a validated work function.
