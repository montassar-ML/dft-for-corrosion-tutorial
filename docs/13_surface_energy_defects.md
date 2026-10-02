# 13 · Surface stability, vacancies and dissolution

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Distinguish an equilibrium formation energy from a dissolution barrier or passivity-breakdown criterion.

For a stoichiometric slab with **two equivalent faces** and a matching bulk energy per atom or formula unit:

```math
\gamma=\frac{E_{\rm slab}-N e_{\rm bulk}}{2A}.
```

`N` must count the same unit used in `ebulk`. For inequivalent faces, the expression yields an aggregate contribution under additional assumptions; it is not automatically either face's individual surface energy. Nonstoichiometric or adsorbate-covered surfaces require reservoir terms. [22](../README.md#ref-22)

At the schematic thermodynamic level:

```math
\gamma(T,\{\mu_i\})=\frac{G_{\rm slab}-\sum_iN_i\mu_i}{A_{\rm exposed}}.
```

The denominator and reference subtraction depend on the construction, paired faces and bulk constraints. Bulk phase stability restricts accessible chemical potentials. Chemical potentials cannot be selected independently to make every chosen termination stable.

## Vacancy bookkeeping
For removal of neutral species X into a specified reservoir:

```math
E_{\rm vac}=E_{\rm defective}-E_{\rm perfect}+\mu_X.
```

Check vacancy position, depth, concentration, relaxation and spin state. A surface vacancy and a bulk vacancy are different defects. Removing an oxygen from an oxide requires an oxygen reference and possibly correction/uncertainty for that reference; it is not the same reaction as removing Fe into hydrated Fe ions.

For charged *bulk* defects, electron-reservoir and finite-size correction terms enter. A schematic expression includes `q(EF+Ev+ΔV)+Ecorr` when q is positive for removed electrons and the energy reference is specified. Charged slabs are a different electrostatic problem: do not transfer a bulk correction scheme without justification.

## Anodic dissolution needs a solution product
A corrosion-relevant event may be:

```math
\mathrm{Fe}_{\rm surface}\rightarrow\mathrm{Fe}^{z+}_{\rm aq}+z e^-+\mathrm{vacancy}.
```

This symbolic reaction requires consistent solvent stabilization, ion chemical potential and electron reservoir. Its barrier depends on the pathway of detachment and hydration. A neutral vacancy energy supplies only a partial term, not a corrosion potential or dissolution rate. [37](../README.md#ref-37)

## Oxide defects and passivity
Do not assume oxygen vacancies dominate all iron-oxide behavior. Magnetite surface work explicitly identifies cation rearrangements, vacancies and interstitials as important structural possibilities. This is a reason to include alternative defect models rather than build every passive-film narrative around one missing oxygen. [52](../README.md#ref-52)

**Exercise:** A lower Fe vacancy energy suggests easier removal under a particular reference. State two missing ingredients before predicting faster corrosion: a solution/electrode thermodynamic cycle and the kinetic/transport constraints governing the actual dissolution route.
