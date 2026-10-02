# Case study · Neutral imidazole on ferromagnetic bcc Fe(110)

[Course home](../README.md) · [Workflow](workflow.md) · [Analysis plan](analyses.md) · [Expected outputs](expected_outputs.md)

> **Status: proposed teaching investigation, not a completed DFT study.** No numerical energies, charges, lattice constants, rankings or corrosion efficiencies are supplied. Worksheets are intentionally blank where calculations are required.

## 1. State the question before selecting analyses
**Primary question:** Among a declared set of adsorption sites and molecular orientations, which neutral-imidazole geometries are locally stable on a chosen bare Fe(110) surface, and what electronic evidence explains their reference-specific binding?

**Secondary question:** Which parts of that interpretation are sensitive to coverage, solvent and chemical state?

**Question not answered by the baseline:** What is the experimental inhibition efficiency of imidazole on a real steel in an acid or chloride electrolyte?

The study isolates molecule–metal interaction. The baseline is a neutral fixed-electron-number vacuum slab. It does not represent an electrode held at a named electrochemical potential, and it omits water, ions, oxide films, roughness, alloying and solution speciation.

## 2. Literature map and facet discipline
| Reading | Relevant contribution | Transfer boundary |
|---|---|---|
| Camacho-Mendoza et al. (2015) | Molecular/surface treatment of imidazole derivatives with an Fe(110) model | Does not supply results for our unspecified cell/settings or justify all experimental conditions |
| Kokalj (2013) | Adsorption/film questions for imidazole on Fe(100) | Different facet; use to motivate film/dissociation controls, not Fe(110) numerical rankings |
| Zhao et al. (2025) | Hydrogen bonding and imidazole adsorption/dissociation on Fe(100) | Different facet and coverage/environment assumptions |
| Spencer et al. (2002) | DFT examination of low-index Fe surface structure/electronics | Clean surfaces are a baseline, not electrolyte-covered steel |
| Recent water/iron study (2025) | Facet- and oxidation-dependent water interactions | Motivates an environment extension; does not substitute for sampling our interface |

References: [44](../README.md#ref-44) [45](../README.md#ref-45) [46](../README.md#ref-46) [47](../README.md#ref-47) [48](../README.md#ref-48). These are literature precedents. The following workflow and worksheets are an original pedagogical design.

## 3. Phase 1 — Bulk Fe and magnetic reference
Construct bcc Fe from a traceable structure and inspect its cell convention. Use spin-polarized calculations and compare physically motivated initial magnetic states. For a lattice search, sample volumes or relax a suitable bulk cell, while preserving a clearly identified magnetic branch. Record energy per atom, cell volume, stress and the definition of magnetic moments.

Converge wavefunction/density representation, k-points, electronic precision and metallic occupation treatment. Compare candidate lattice and moment trends with appropriate literature or experiment while recognizing temperature and model differences; do not force agreement by arbitrary parameter tuning.

**Deliverables:** lattice vectors and provenance, energy–volume dataset, final spin-state records, numerical convergence ledger.

**Gate:** Are energy per atom and stress obtained consistently enough to serve as a surface reference? If spin collapses or changes with numerical settings, diagnose that before building the slab.

## 4. Phase 2 — Define the Fe(110) slab
Use the selected bulk lattice. Identify the (110) normal and the in-plane periodic vectors explicitly. Choose the surface area, number of atomic layers, vacuum and fixed-layer policy. Distinguish a symmetric clean slab used for surface-energy tests from an asymmetric adsorbed slab used for binding/work-function calculations.

Examine layer relaxations and layer-resolved moments. Converge thickness and vacuum using the target quantities, not only total energy. For work function verify a plateau on the analyzed face and treat the slab dipole appropriately. Keep the lateral lattice tied to the chosen bulk unless intentional strain is a study variable.

**Deliverables:** clean-slab coordinates, facet/area/layer metadata, boundary conditions, thickness and vacuum tests, clean-surface energy and work-function protocol.

**Gate:** Does the slab have a bulk-like interior, controlled periodic-image electrostatics and a reproducible surface reference? If not, do not interpret small adsorption-energy differences.

## 5. Phase 3 — Define imidazole and its reference
For neutral imidazole, the formula C3H4N2 gives 36 all-electron electrons by atomic-number bookkeeping, compatible with a closed-shell singlet molecular reference. This does **not** make the combined Fe slab a singlet. Effective valence electron counts depend on pseudopotentials.

Specify tautomer and atom numbering, particularly the pyridine-like versus pyrrole-like N environments. Optimize the isolated molecule under a compatible Hamiltonian and converge cell isolation when using a periodic molecular calculation. A separate molecular calculation may explore MEP/Fukui descriptors, but such descriptors are not used to assign an inhibition efficiency.

Neutral imidazole is a starting teaching choice, not an assertion about the predominant species at a particular pH. Protonated or deprotonated alternatives require an explicitly balanced proton/electron and solvation treatment before energy comparison.

**Deliverables:** labeled molecular structure, charge/multiplicity, reference energy, isolation/basis checks.

**Gate:** Can another reader reconstruct the exact chemical species and reference state?

## 6. Phase 4 — Search adsorption configurations
Construct several nonoverlapping initial geometries. Test flat, tilted and upright orientations, alternative azimuthal alignments and accessible donor contacts. Include top, short-bridge, long-bridge and an explicitly defined hollow region of the bcc(110) net. Site nomenclature must follow this lattice; do not simply import fcc(111) labels.

A starting height is a search parameter, not a predicted bond distance. Relax the allowed degrees of freedom and track both geometry and magnetic state. Do not constrain the molecule to remain atop its initial site unless a constrained study is intended. Cluster final structures: two differently named starts may become the same minimum.

**Deliverables:** initial/final coordinates, optimization status, final contact/tilt metrics, magnetic state, unique-minimum ID and reason for excluded failures.

**Gate:** Have enough distinct physical starts been tested to make “lowest among tested configurations” meaningful? No finite small search proves a global minimum.

## 7. Phase 5 — Compare energy components
For each retained state use:

```math
E_{\mathrm{ads}}=E_{SM}^{\mathrm{rel}}-E_S^{\mathrm{rel}}-E_M^{\mathrm{rel}}.
```

Check a single consistent convention, units, surface area, pseudopotential/basis choices, spin treatment and energy-like output field. If localized bases are used, assess basis sensitivity and possible basis-set superposition error. A molecular Gamma-only reference and metallic slab mesh need individually converged treatment; “consistency” does not require a physically inappropriate identical k-point mesh for every kind of system.

Optionally calculate frozen-fragment interaction and deformation contributions. Re-evaluate close competitors with tighter settings, and report ambiguous orderings rather than printing unjustified precision. Compare the same stoichiometry/chemical state, or use an explicit reservoir equation.

**Deliverables:** total/reference/adsorption energies and uncertainty; optional interaction/deformation ledger.

**Gate:** Is the ranking larger than practical uncertainty and robust to reasonable methodological checks? If not, retain more than one candidate for interpretation.

## 8. Phase 6 — Electronic structure
Generate spin-resolved total and projected spectra for selected candidates and references. Inspect Fe d and molecule N/C p character, with projections, normalization, energy alignment and broadening specified. Label the projection method and the relevant atoms/layers.

Ask whether new mixed character, shifts or broadened molecular features are consistent with the attachment motif. A mere overlap of two separately plotted peaks is not proof of bonding. The combined metal interface does not inherit the isolated molecule's HOMO–LUMO gap as a corrosion descriptor.

**Deliverables:** aligned spin DOS/PDOS, projections and controlled reference comparisons.

## 9. Phase 7 — Charge redistribution and bonding
For each chosen adsorbed geometry calculate the combined density and frozen-fragment densities in the same cell/grid. Use the electron-number-density CDD convention and check the integral. For electron-conserving fragments, the total CDD integral is zero even when spatial transfer/polarization is substantial.

Report Bader populations with valence/all-electron convention and a total-charge check. An adsorbate's assigned electron gain must be balanced by the rest of the system for a neutral fixed-electron-count decomposition. ELF or COHP/ICOHP may test a specific bonding hypothesis, but they are optional—not decorative requirements.

**Deliverables:** CDD reference record, grid test, partitioned charge table; optional validated localization/bonding analysis.

## 10. Phase 8 — Work function
Calculate the clean and covered surface work functions using the same exposed side, converged electrostatics and Fermi/potential conventions. Inspect the planar potential before recording a number.

```math
\Delta\Phi=\Phi_{\mathrm{covered}}-\Phi_{\mathrm{clean}}.
```

A shift is evidence of a changed vacuum electron-removal energy and surface dipole/electronics. Do not label it a corrosion-potential shift or assign a universal favorable sign.

## 11. Phase 9 — Coverage
Increase area at fixed molecule count to probe the dilute limit; separately compare finite-density arrangements with more than one molecule. Report number per area and any site-coverage convention. Examine hydrogen bonding, molecular packing and altered attachment, but do not assume the Fe(100) film findings reproduce on Fe(110).

A concentration-to-coverage connection additionally needs solution chemical potential and an adsorption/kinetic model. Coverage and an efficiency inferred from current are different quantities. [51](../README.md#ref-51)

## 12. Phase 10 — Extend the environment deliberately
| Extension | New question | Additional requirement |
|---|---|---|
| Implicit solvent | How does continuum screening change a motif/order? | Cavity/dielectric specification and compatible reference states |
| Explicit water | Does water compete, orient or mediate bonding? | Multiple configurations, sufficient water region, sampling |
| Protonation / deprotonation | Which inhibitor state is populated/bound? | Solution speciation and balanced proton/electron reservoirs |
| Chloride | Does it compete at a chosen site or alter a pathway? | Distinguish aqueous anion from neutral atom; countercharge/reference treatment |
| Oxidized/hydroxylated surface | Is the bare-metal mechanism still relevant? | New phase/termination/defect/magnetic model |
| Constant potential | How does electron exchange affect adsorption? | Grand-canonical formulation and electrolyte/reference calibration |
| AIMD / free-energy sampling | Which motifs interconvert at temperature? | Independent sampling, thermalization, collective variables if rare events matter |

Changing several axes simultaneously makes causality hard to identify. Expand the model hierarchy one justified step at a time. Modern electrochemical DFT reviews discuss why potential control and realistic environments remain modeling choices rather than automatic properties of a neutral slab. [38](../README.md#ref-38) [39](../README.md#ref-39)

## 13. What a completed report could conclude
A defensible conclusion would identify the lowest **tested** configurations, describe reference-specific binding and electronic evidence, and list which trends survived the environment/coverage controls actually performed. It would explicitly leave experimental efficiency, long-term film durability and corrosion current unresolved unless an appropriate larger model or experiment supplied that evidence.
