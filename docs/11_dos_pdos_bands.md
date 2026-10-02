# 11 · DOS, spin-resolved PDOS and bonding evidence

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Use spectral projections to test an interaction hypothesis without confusing graphical overlap with proof of a corrosion mechanism.

The density of states counts electronic states per energy interval. In a spin-resolved representation:

```math
D_s(E)=\sum_{j\mathbf k}w_{\mathbf k}\delta(E-\varepsilon_{j\mathbf k s}).
```

A practical plot replaces delta functions with a stated broadening and uses a sufficiently sampled k mesh. The integral of a total DOS is a count of included states under the program's normalization, whereas an occupied integral also requires occupations.

## Projected DOS is a representation
A PDOS resolves contributions on selected atoms or orbitals using a particular projector, sphere or localized basis. It is not generally a unique decomposition of total density. Compare identical definitions, broadening, energy windows and spin conventions. A fine-looking curve from poorly converged k sampling is still inaccurate.

For Fe–imidazole, test whether donor-N p-like contributions change in the same energy regions as relevant Fe d-like components, whether molecular levels broaden, and whether adsorption alters near-Fermi spectral weight. Inspect actual geometry and density before assigning a particular sigma or pi interaction. [50](../README.md#ref-50) [26](../README.md#ref-26)

## Energy alignment must follow the question
For occupied/unoccupied character within one metal calculation, EF is a convenient zero. Separately setting EF=0 in two different systems can conceal an adsorption-induced absolute shift. To compare work functions or vacuum-level shifts, use a common vacuum reference from a suitable electrostatic calculation. A molecular spectrum calculated in a different cell also needs a compatible reference; visually sliding curves until peaks match is not analysis.

## Spin and magnetic response
Plot both spin channels with a legend. Plotting spin-down as a negative curve is a display convention, not negative DOS. Compare total and atom-projected moments and check whether adsorption induced a different magnetic solution. A surface's metallic density of states must not be relabeled a molecular HOMO–LUMO gap.

## d-band center as a controlled summary
Define the spin/orbital projection, energy reference and integration window:

```math
\varepsilon_d=\frac{\int_{E_1}^{E_2}(E-E_F)D_d(E)\,dE}
{\int_{E_1}^{E_2}D_d(E)\,dE}.
```

This moment can describe a spectral change within a comparable material family. It loses information about orbital symmetry, filling, bandwidth and adsorbate-specific coupling. It is especially unsafe as a universal descriptor across metallic Fe, localized oxides and molecular inhibitors. Use it alongside explicitly calculated adsorption and electronic structure, not as a replacement.

## COHP and pCOHP
Energy-resolved Hamilton populations examine pair-resolved bonding/antibonding contributions. Conventional COHP uses negative values for bonding; plots of **−COHP** reverse that appearance. ICOHP integrates over a specified occupied range. Projection quality and charge spilling must be checked. Neither ICOHP nor an arbitrary peak overlap is a gas-phase bond dissociation energy. [20](../README.md#ref-20) [26](../README.md#ref-26)

**Exercise:** Two PDOS peaks overlap after adsorption. Name additional evidence needed for a bonding argument: altered geometry/coordination, CDD, state character, an energy-resolved bonding analysis when available, and convergence of projections and energy alignment.
