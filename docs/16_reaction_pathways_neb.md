# 16 · Reaction barriers, thermochemistry and sampling

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Distinguish a favorable endpoint, an activation barrier and an experimentally relevant rate.

For a defined minimum-energy path:

```math
\Delta E^\ddagger=E_{\rm TS}-E_{\rm IS},\qquad
\Delta E_{\rm rxn}=E_{\rm FS}-E_{\rm IS}.
```

A negative reaction energy does not establish a low barrier. Geometry optimization tends to remain in its local basin; lack of reaction during relaxation is not proof of thermodynamic stability.

## NEB logic
The nudged elastic band method connects optimized endpoints using intermediate images. The climbing-image modification refines a high-energy image toward a saddle. Endpoints need compatible atom identities, cell, charge/electronic ensemble and constraints; interpolation must not drive atoms through the slab or create artificial bond crossings. Test image number and residual forces rather than taking the highest unrelaxed image as a transition state. [17](../README.md#ref-17)

For Fe–imidazole, possible elementary questions include reorientation, migration, proton transfer or specific bond cleavage. Choose one balanced pathway. A paper's Fe(100) dissociation mechanism is a hypothesis source for Fe(110), not its already known barrier. [46](../README.md#ref-46)

## Frequency validation
A first-order saddle has one unstable mode in the relevant unconstrained subspace, aligned with the proposed reaction coordinate. A minimum has no unstable modes within the approximation. Partial Hessians that move only the adsorbate test only that subspace; they cannot certify the entire surface. Tiny negative modes need convergence and mode-shape inspection rather than automatic deletion.

For stable harmonic modes:

```math
E_{\rm ZPE}=\frac12\sum_i\hbar\omega_i,
\qquad F_{\rm vib}(T)=\sum_i\left[\frac12\hbar\omega_i
+k_BT\ln\left(1-e^{-\hbar\omega_i/k_BT}\right)\right].
```

Do not put negative/imaginary frequencies into this real harmonic expression. At a transition state the unstable reaction-coordinate mode is treated through transition-state theory, not included as an ordinary bound vibration. Acoustic zeros and low-frequency hindered motion require appropriate treatment. Gas translation/rotation, solution standard states and adsorbate vibration are different contributions.

## Rates require more than a static saddle
A simple transition-state estimate is:

```math
k\approx\kappa\frac{k_BT}{h}\exp[-\Delta G^\ddagger/(k_BT)].
```

The transmission factor κ, solvent dynamics, potential dependence, coverage and mechanism assumptions matter. This expression does not turn a single DFT barrier into a complete corrosion current.

## AIMD and interfacial structure
AIMD samples trajectories with forces from electronic calculations; it can reveal local solvent rearrangement or a possible reaction. Verify equilibration, time-step behavior, thermostat choices, SCF stability and independent samples. An event seen once is not a converged rate; an event not seen in a short trajectory is not impossible.

Bulk radial-distribution normalization assumes a homogeneous isotropic reference. At a slab/liquid interface, use layer-conditioned distributions, accessible-volume corrections or density profiles instead of blindly applying a bulk `4πr²ρ` denominator. State the sampled region and statistical uncertainty.

**Self-check:** An inhibitor remains adsorbed during a short AIMD trajectory. The supported conclusion is persistence during that observation window and conditions, not guaranteed protective-film lifetime.
