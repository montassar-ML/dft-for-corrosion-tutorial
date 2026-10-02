# 20 · Building an evidence-based interpretation

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Separate a calculated observation, a mechanistic hypothesis and an experimental performance claim.

## An evidence ladder
1. **Observation:** the relaxed structure has a specified contact pattern, or a computed energy difference has a given sign.
2. **Robustness:** the difference survives numerical convergence, alternative initial states and a stated uncertainty test.
3. **Mechanistic interpretation:** several independent observables support a proposed bonding or reaction mechanism.
4. **Environmental relevance:** protonation, solvent, potential, coverage and surface phase do not contradict that interpretation.
5. **Performance connection:** a kinetic/interfacial model or controlled experimental comparison links the mechanism to corrosion behavior.

Do not jump from rung 1 to rung 5. Molecular/surface calculations are complementary to experiment precisely because they resolve selected parts of the interface, not because one scalar descriptor replaces the experiment. [33](../README.md#ref-33) [37](../README.md#ref-37)

## Central interpretation table
| Analysis | Physical meaning | Corrosion-relevant interpretation | Major limitation |
|---|---|---|---|
| Relaxed geometry | Local nuclear stationary configuration | Possible attachment motif / accessible footprint | Search and model dependent |
| Adsorption energy | Reference-specific electronic binding | Preference among comparable tested states | Not aqueous adsorption free energy or efficiency |
| Deformation energy | Cost of distorting separated fragments | Why contact strength and net binding differ | Fragment and reference dependent |
| Coverage study | Interaction between periodic adsorbates | Cooperative or competitive film motifs | Finite cells do not give an isotherm automatically |
| Surface energy | Excess energy per area | Candidate clean facets/terminations | Environment and kinetics can change populations |
| Vacancy energy | Cost relative to a species reservoir | Defect susceptibility in that model | Not a dissolution barrier |
| DOS / spin PDOS | State distribution and projected character | Candidate orbital mixing / magnetic changes | Projection and energy alignment dependent |
| CDD | Spatial electron redistribution | Accumulation/depletion relative to frozen fragments | No unique net transfer or bond type |
| Bader charge | Integrated density in zero-flux basins | Partition-specific electron gain/loss | Not oxidation state or measurable corrosion current |
| ELF | Localization indicator | Regions consistent with localized electron pairs | Not adsorption energy or transferred charge |
| COHP / ICOHP | Hamiltonian-weighted projected bonding | Occupied bonding/antibonding contributions | Basis/projection/sign convention dependent |
| Work function | Vacuum electron-removal energy | Surface dipole / electronic response | Not mixed corrosion potential |
| Potential profile | Spatial electrostatic energy variation | Plateau and interfacial field checks | Boundary conditions and gauge matter |
| Magnetic moments | Spin-density integrals/projections | State changes induced by coordination | Partition and metastability dependent |
| d-band center | Chosen projected spectral first moment | Compact descriptor within a defined family | Not universal for Fe oxides or inhibitor performance |
| Frequencies / ZPE | Local curvature / vibrational ground energy | Minimum or TS checks; corrections | Partial Hessians and low modes require care |
| Free energies | Thermodynamic state preference | Population/competition under named reservoirs | Standard states and sampling matter |
| NEB / TST | Path-specific activation estimate | Candidate elementary kinetic bottleneck | Environment/potential and competing paths matter |
| AIMD / RDF | Finite-time dynamics / pair structure | Hydration motifs and sampled stability | Short trajectories and interface normalization |

Detailed analysis cards with equations, valid/invalid conclusions and deliverable types are in the [analysis catalogue](24_analysis_catalogue.md).

## Combining observables without double counting
Geometry, PDOS, CDD and Bader all derive from the same approximate electronic problem. Agreement is useful internal consistency, but these are not four independent experimental validations. A very attractive isosurface is not stronger evidence than a reproducible reference calculation.

## A claim template
> Within [surface/species/environment model], [observable] changes by [computed value and numerical uncertainty] relative to [reference]. Together with [supporting observations], this is consistent with [limited interpretation]. It does not establish [larger claim], which additionally requires [next evidence].

Leave values blank until calculated. Use this template in the case-study report rather than guessing the sign or magnitude.

**Self-check:** Can two inhibitors have similar adsorption energies and different experimental efficiencies? Yes: accessible concentration, speciation, competitive adsorption, film structure, kinetics and experimental protocol can differ.
