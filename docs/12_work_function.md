# 12 · Work function is not corrosion potential

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Calculate and interpret a vacuum-referenced electronic quantity without confusing it with a measured mixed potential.

For a neutral metallic slab with a well-defined vacuum plateau:

```math
\Phi=V_{\rm vac}^{(e)}-E_F.
```

`Vvac(e)` denotes the **electron potential-energy reference**, usually reported in energy units. It is not an unlabeled electric potential in volts; electron charge and sign matter when converting conventions. A work function is the energy cost of taking an electron from the metal's Fermi level to the vacuum reference.

## Procedure and controls
Average a suitable electrostatic potential parallel to the surface. Locate a genuinely flat vacuum region, choose the exposed side consistently, and test the vacuum width, slab thickness, grid and dipole treatment. When a field persists through the nominal vacuum, a single plateau value may not exist. Do not extract the last grid point merely because it is farthest from the atoms.

Asymmetric slabs create electrostatic artifacts under repeated boundary conditions unless treated appropriately. A dipole correction addresses a specific periodic-image effect; it does not simulate an electrolyte double layer. [21](../README.md#ref-21)

## Adsorption-induced shifts

```math
\Delta\Phi=\Phi_{SM}-\Phi_S.
```

A shift can arise from molecular dipoles, rearrangement of metal electron density, charge transfer, structural relaxation and changed coverage. Its sign alone does not distinguish all contributions. Examine CDD and geometry, and preserve the same potential definition across compared calculations.

## Where the electrochemical comparison changes
An electrode in solution has an electron chemical potential referenced to an electrochemical scale, solvent polarization and countercharge. A vacuum work function cannot simply be declared equal to an experimental corrosion potential. Model-specific alignment to a reference electrode may be possible with additional calibration and interface physics. [38](../README.md#ref-38) [39](../README.md#ref-39)

Corrosion potential is the open-circuit mixed potential at which the net anodic and cathodic currents balance under the experimental conditions. Work-function shifts can motivate a question about interfacial electronic change, but do not supply those current–potential curves.

## Minimum reporting packet
Report the potential type, averaging direction, plateau selection, slab side, dipole treatment, Fermi-energy definition, cell and coverage. Include the planar-average curve rather than only one scalar number. A good curve can expose a bad model that a rounded scalar conceals.

**Self-check:** “Higher work function means lower corrosion rate.” Is this universal? No. Without a validated model for competing reactions, potential, surface chemistry and transport, the work function alone does not determine corrosion kinetics.
