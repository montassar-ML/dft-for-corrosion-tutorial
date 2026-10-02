# 10 · Density redistribution and partitioned charge

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Separate spatial electron redistribution from an assigned atomic charge and from an oxidation state.

This course defines `n(r)` as **positive electron-number density**. For neutral adsorption, evaluate complex and fragment densities at the *same frozen coordinates*, cell, grid and electronic method:

```math
\Delta n(\mathbf r)=n_{SM}(\mathbf r)-n_S^{\rm frozen}(\mathbf r)-n_M^{\rm frozen}(\mathbf r).
```

Positive values mean electron accumulation. If a plotting program uses physical charge density `ρcharge=−en` instead, the sign reverses. Always label which density is plotted.

## Why frozen fragments matter
Relaxing the isolated fragments before subtraction mixes adsorption-induced redistribution with atomic displacement. A positive region could then reflect a shifted atom rather than electronic rearrangement at fixed geometry. Align grids and do not interpolate one density casually onto another without quantifying numerical error.

For matched electron numbers:

```math
\int_{\rm cell}\Delta n(\mathbf r)\,d\mathbf r
=N_{SM}-N_S-N_M=0.
```

A nonzero integral can reveal inconsistent reference charge, grids or density type. It is not automatically the number of electrons transferred from metal to molecule. At constant potential, the complex and fragments can contain different numbers of electrons, so the reservoir bookkeeping changes this test.

## Planar averages and cumulative transfer
A planar average along the surface normal is:

```math
\overline{\Delta n}(z)=\frac{1}{A}\int_A\Delta n(x,y,z)\,dx\,dy,
\qquad \Delta N(z)=A\int_{z_0}^{z}\overline{\Delta n}(z')\,dz'.
```

The cumulative curve depends on the chosen spatial dividing plane. It complements but does not replace atom-based partitioning. Adsorbate-induced polarization can be large even when a net molecular charge is small.

## Bader charges
Bader basins are bounded by zero-flux surfaces of the density gradient. A practical grid algorithm assigns density to atomic basins. [18](../README.md#ref-18)

For a valence-density convention:

```math
N_A=\int_{\Omega_A}n_{\rm val}(\mathbf r)\,d\mathbf r,
\qquad q_A/e=Z_{A,\rm val}-N_A.
```

Positive `qA` means an electron deficit relative to the chosen reference. Sum charges over all atoms of the molecule, state how basins were constructed, and check conservation. Reconstructed core/all-electron reference densities and integrated valence populations must be used according to the implementation; do not mix nuclear Z with a valence-only population.

Bader charge is not a directly measured oxidation state. Different reasonable partitions can yield different magnitudes. Report grid sensitivity and use charge analysis to support a defined mechanistic interpretation rather than to “prove” a bond by its sign alone.

## What a defensible conclusion looks like
“At the tested geometry and partition convention, electron redistribution and the summed molecular basin population are consistent with electron gain by the adsorbate.” This is more precise than “the molecule donates electrons, therefore it inhibits corrosion.” The latter requires a kinetic and environmental bridge absent from a charge table.

**Self-check:** A CDD map contains both large accumulation and depletion lobes, but Bader finds small net transfer. This is not a contradiction: polarization and covalent redistribution need not produce a large net basin charge.
