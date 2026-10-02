# 25 · Connecting DFT with corrosion experiments

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Connect microscopic hypotheses to measured signals without presenting a computed descriptor as a direct instrument reading.

## Match the experimental conditions first
Record alloy composition, surface preparation, oxide history, electrolyte, pH, oxygen availability, temperature, inhibitor concentration, immersion time and applied/open-circuit potential. A clean single-crystal vacuum model may be useful precisely because it isolates a mechanism, but it should not be described as reproducing a rough, oxidized alloy/electrolyte interface.

| Measurement | What is measured/inferred experimentally | DFT contribution | Important boundary |
|---|---|---|---|
| Potentiodynamic polarization | Current–potential response; kinetic fits under assumptions | Relative elementary barriers and adsorption/coverage hypotheses | Adsorption energy alone cannot reproduce a polarization curve or `i_corr` |
| EIS | Frequency-dependent interfacial response fitted with a model | Candidate film structures, dielectric/bonding changes or transport steps | A Bader charge cannot be converted directly to charge-transfer resistance |
| XPS | Binding-energy/chemical-state and composition information | Carefully referenced core-level shifts and candidate environments | Bader charges are not XPS binding energies; final-state effects matter |
| FTIR / Raman | Vibrational frequencies and intensities | Adsorption motifs, bond changes, computed modes | Solvent, selection rules, coverage and anharmonicity affect comparison |
| SEM | Morphology over larger scales | Hypotheses for preferential attack or film persistence | A flat atomic slab cannot predict a micrograph directly |
| TEM | Local structure, lattice/film observations | Candidate crystalline phases, interfaces and defects | Real films may be amorphous or beam altered |
| AFM | Topography/forces at accessible scales | Possible step/adsorbate arrangements | Finite probe, roughness and dynamic effects are outside one DFT cell |
| Contact angle | Macroscopic wetting response | Surface-water interactions and candidate film polarity | One water adsorption energy is not a contact angle |
| Surface-sensitive spectroscopy | Occupied/unoccupied or local environments | DOS/PDOS, simulated spectra with proper matrix elements | Bare DOS is not an experimental intensity spectrum |

Reviews of atomically resolved corrosion/passivation and multiscale modeling motivate connecting structural information to measurable degradation rather than replacing one with the other. [36](../README.md#ref-36) [37](../README.md#ref-37)

## Efficiency is not automatically coverage
An inhibition efficiency derived from corrosion currents compares rates under stated protocols. A coverage fraction describes occupied sites under an adsorption model. Equating them requires a kinetic/blocking model; it is not an identity. The critical analysis by Walczak, Morales Gil and Lindsay explains why that shortcut can undermine adsorption-isotherm deductions. [51](../README.md#ref-51)

```math
\mathrm{IE}_{j}=100\left(1-\frac{j_{\mathrm{corr,inh}}}
{j_{\mathrm{corr,blank}}}\right)\%.
```

The expression defines a current-based experimental efficiency when both inferred currents are comparable. It is **not** supplied by a static DFT adsorption-energy calculation.

## A triangulation example without invented results
A measured vibrational band change may suggest adsorption through an N-containing group. Compute competing attachment motifs and their modes; inspect spin PDOS/CDD for consistency; then test whether solvent/protonation changes the predicted motif. Agreement narrows plausible structures but does not prove a unique mechanism unless competing models are excluded.

## Stronger study design
Use matched controls: blank versus inhibitor at the same conditions, a structurally related inactive compound if available, multiple surface chemical states, and time-dependent measurements. When comparing a series, separate experimental variation from computational model variation. Report negative or ambiguous evidence rather than selecting only quantities that support the preferred conclusion.

**Exercise:** An inhibitor lowers the measured corrosion current but increases the calculated vacuum work function. Does the work-function change explain the full current reduction? Not by itself. A causal account requires which anodic/cathodic steps or coverage changes are affected and under which electrode conditions.
