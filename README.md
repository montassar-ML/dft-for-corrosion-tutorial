# Density Functional Theory for Corrosion Science

**Theory · Surfaces · Adsorption · Electronic Structure · Corrosion Mechanisms**

**Maintained by Montassar Bouzidi** · Theory-led open educational resource · Version 0.1.0

A graduate-level tutorial on molecular and periodic DFT for corrosion, with an explicitly bounded Fe(110)/imidazole case study. Learn what to calculate, what each observable means, and which conclusions require additional evidence.

> **Study status:** educational theory and proposed investigation; not an executed corrosion simulation or a prediction of inhibition efficiency. [Validation scope](VALIDATION_REPORT.md).

## Table of contents
- [How to use this course](#how-to-use)
- [1 · Corrosion as a coupled interfacial process](#corrosion)
- [2 · What DFT can and cannot establish](#capabilities)
- [3 · Molecular versus periodic DFT](#molecular-periodic)
- [4 · Hohenberg–Kohn and Kohn–Sham foundations](#hk-ks)
- [5 · Exchange–correlation, dispersion and model sensitivity](#xc)
- [6 · Periodic boundaries and Bloch states](#periodicity)
- [7 · Plane waves, pseudopotentials and PAW](#basis)
- [8 · k-points, smearing and spin in metals](#metals-spin)
- [9 · From bulk to a defensible corrosion surface](#slabs)
- [10 · Converge observables, separate model uncertainty](#convergence)
- [11 · Adsorption, interaction and deformation](#adsorption)
- [12 · Sites, orientation and coverage](#search-coverage)
- [13 · Molecular inhibitor descriptors without overclaiming](#inhibitor-descriptors)
- [14 · Water, oxygen, hydroxyl and aggressive ions](#water-ions)
- [15 · Surface stability, vacancies and dissolution](#surface-defects)
- [16 · Oxides and passive films](#passivation)
- [17 · What each DFT analysis tells us](#analysis-table)
- [18 · DOS, PDOS, bands and magnetic interpretation](#spectral-analysis)
- [19 · Charge transfer, localization and bonding](#charge-bonding)
- [20 · Work function and electrostatic potential](#work-function)
- [21 · Vibrations, ZPE, entropy and free energy](#thermochemistry)
- [22 · Solvation and the electrochemical interface hierarchy](#electrolyte)
- [23 · Constant charge, constant potential and CHE](#potential-che)
- [24 · NEB, kinetics, AIMD and RDF](#kinetics-dynamics)
- [25 · A staged Fe(110)/imidazole investigation](#case-study)
- [26 · Solvers versus analysis tools](#software)
- [27 · Connecting to experiment](#experiment)
- [28 · Reporting and preventing overinterpretation](#reporting)
- [29 · Figures, teaching materials and reuse](#figures)
- [30 · References and source verification](#references)

---

<a id="how-to-use"></a>
## How to use this course

This repository teaches **theory → model choice → analysis → defensible interpretation**. It is intended for MSc/PhD researchers, experimental corrosion scientists and computational chemists moving from isolated molecules to metal/electrolyte interfaces. It is not a job-submission or software-installation course.

Start with this lecture, then use the [25 detailed chapters](docs/README.md), [26 analysis cards](docs/24_analysis_catalogue.md), [case study](case-study/README.md) and [teaching plan](TEACHING_PLAN.md). Readers mainly interested in interpreting a corrosion paper should begin with the analysis table and the chapters on molecular descriptors, electrochemical interfaces and experimental comparison.

**Evidence convention:** references identify literature or official methods; the course organization, study design, decision gates and worksheets are original pedagogical synthesis. The case study is **proposed, not executed**. There are no invented Fe lattice constants, adsorption rankings, charge values, work-function shifts or inhibition efficiencies.

**Two distinctions recur throughout:** a finished/converged calculation is not necessarily a physically valid model; an isolated inhibitor calculation is not a calculation of an electrochemical interface.

---

<a id="corrosion"></a>
## 1 · Corrosion as a coupled interfacial process

Corrosion involves material degradation through chemical/electrochemical interaction with the environment. For metallic corrosion, oxidation at anodic sites supplies electrons consumed by cathodic reactions. Which reactions dominate depends on the material, electrolyte, potential, oxygen availability and temperature; there is no single universal corrosion reaction.

Illustrative balanced half-reactions are:

```math
\mathrm{Fe}\rightarrow\mathrm{Fe}^{2+}(aq)+2e^-;
\qquad 2\mathrm H^++2e^-\rightarrow\mathrm H_2;
\qquad\mathrm O_2+2\mathrm H_2O+4e^-\rightarrow4\mathrm{OH}^-.
```

These are reservoir-level equations, not proof of single-step atomistic mechanisms. At a mixed corrosion potential, signed anodic and cathodic currents balance; metal can still dissolve while net external current is zero. Atomic-scale structures and macroscopic degradation must therefore be linked, not identified with each other. [36](#ref-36) [37](#ref-37)

DFT can examine water/O/OH adsorption, surface bonding, defects, oxide interfaces and selected reaction steps. Predicting a corrosion current additionally requires appropriate kinetics, populations, transport and environmental information.

---

<a id="capabilities"></a>
## 2 · What DFT can and cannot establish

At a specified composition, electronic state and boundary condition, DFT supplies an approximate ground-state electronic energy, forces, density and electronic states. Differences and response calculations can address adsorption, defects, vibrations and reaction pathways.

DFT does not output “inhibition efficiency” merely because an adsorption calculation converged. Solubility, concentration, protonation, surface oxidation, competitive adsorption, temperature, desorption, film formation and elementary kinetics can all affect performance. Broad corrosion-modeling reviews provide useful context, while critical analyses show why apparently simple molecular-descriptor correlations must be examined carefully. [41](#ref-41) [42](#ref-42) [33](#ref-33)

A defensible question is “how does this specified adsorbate change a particular surface interaction?” A much stronger question—“how well will this molecule inhibit corrosion of an alloy in acid?”—requires several additional modeling and experimental layers.

---

<a id="molecular-periodic"></a>
## 3 · Molecular versus periodic DFT

| Molecular model | Periodic surface/interface model |
|---|---|
| Isolated or continuum-solvated finite species | Repeated crystal/slab with specified environment |
| Discrete molecular orbitals | Bands/k-point states, often metallic occupations |
| Useful for geometry, conformers, protonation candidates, local reactivity | Useful for attachment sites, reconstruction, surface charge/electronics and reactions |
| Does not contain the metal surface unless an explicit cluster is included | Does not contain an electrolyte or potential control unless explicitly modeled |

A cluster calculation can include local metal chemistry, but finite size, charge, spin and boundary effects require justification. Periodicity does not automatically make a model realistic either: a clean vacuum slab is still not oxidized steel in solution.

The molecular descriptors in [Chapter 02](docs/02_molecular_vs_periodic_dft.md) are used to generate hypotheses, not to prove inhibition. An analysis of imidazole compounds tested on Cu/Zr-based materials is an instructive warning about universal descriptor correlations, not evidence specific to Fe(110). [43](#ref-43)

---

<a id="hk-ks"></a>
## 4 · Hohenberg–Kohn and Kohn–Sham foundations

For fixed nuclei, ground-state DFT uses electron density rather than the many-electron wavefunction as its central variable. The Hohenberg–Kohn statements are exact foundations under their conditions; they do not make a chosen approximate functional exact. [1](#ref-1)

In atomic units, an instructive Born–Oppenheimer energy decomposition is:

```math
E_{\mathrm{BO}}[n;\mathbf R]=T_s[n]
+\int v_{\mathrm{ext}}(\mathbf r;\mathbf R)n(\mathbf r)d\mathbf r
+E_H[n]+E_{xc}[n]+E_{\mathrm{II}}(\mathbf R).
```

The final term is the ion–ion interaction; it cannot be forgotten in the total energy used for nuclear relaxation. The Kohn–Sham construction introduces auxiliary orbitals reproducing the density. For a local collinear-spin potential:

```math
\left[-\frac12\nabla^2+v_{\mathrm{ext}}+v_H[n]+v_{xc,s}\right]
\psi_{j\mathbf k s}=\varepsilon_{j\mathbf k s}\psi_{j\mathbf k s}.
```

`j` labels the band, `k` reciprocal space and `s` spin. PAW, nonlocal pseudopotentials and hybrids require generalized/nonlocal operator forms; this compact equation is a teaching form, not the exact input implementation of every code. [2](#ref-2) [5](#ref-5)

An SCF loop makes the potential and density self-consistent. Nuclear optimization is a second loop driven by forces. Neither loop chooses the correct surface phase or proves the global lowest-energy magnetic state.

---

<a id="xc"></a>
## 5 · Exchange–correlation, dispersion and model sensitivity

PBE is a widely used GGA baseline, not a universal reference truth. Adsorption, localization and oxide energetics can be sensitive to functional choice. SCAN and screened hybrids illustrate other approximations, each with different numerical/cost requirements. [3](#ref-3) [16](#ref-16) [55](#ref-55)

Dispersion can matter for molecular approach, orientation and packing; document the specific correction and avoid double counting. DFT+U can change localized d/f states, but its correlated subspace and determination/benchmark must be reported. Changing U is a model sensitivity test, not the equivalent of increasing a plane-wave cutoff. [15](#ref-15) [14](#ref-14)

For Fe oxides, inspect alternative magnetic/occupation solutions and reference-state consistency. Tight SCF convergence cannot remove a wrong chemical state or unsuitable functional.

---

<a id="periodicity"></a>
## 6 · Periodic boundaries and Bloch states

A periodic potential obeys a lattice translation symmetry. Bloch states separate a phase from a lattice-periodic component:

```math
V(\mathbf r+\mathbf R)=V(\mathbf r),\qquad
\psi_{j\mathbf k s}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{j\mathbf k s}(\mathbf r).
```

Bulk cells repeat in three dimensions. A conventional slab calculation usually also repeats in three dimensions but inserts vacuum in one direction to approximate a surface. One k-point along the empty direction is not a switch that turns electrostatic interactions between repeated slabs off. Choose the Coulomb boundary treatment, slab symmetry/dipole correction and vacuum consistently.

A larger supercell changes the reciprocal-space sampling needs and the distances between repeated adsorbates/defects. [Chapter 03](docs/03_periodic_boundary_conditions.md) separates this numerical effect from the physical coverage change.

---

<a id="basis"></a>
## 7 · Plane waves, pseudopotentials and PAW

For a plane-wave representation:

```math
\psi_{j\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{j,\mathbf k+\mathbf G}
 e^{i(\mathbf k+\mathbf G)\cdot\mathbf r},\qquad
\frac{\hbar^2|\mathbf k+\mathbf G|^2}{2m_e}\le E_{\mathrm{cut}}.
```

Pseudopotentials replace selected core degrees of freedom; PAW reconstructs all-electron-like information through its transformation. Dataset valence configuration and compatibility are part of the Hamiltonian, not incidental filenames. [4](#ref-4) [5](#ref-5) [6](#ref-6)

CP2K's GPW representation uses Gaussian orbital functions plus an auxiliary grid/plane-wave density representation. Increasing its grid cutoff does not replace testing the Gaussian basis. A plane-wave cutoff in one code is not numerically transferable to a different representation. [53](#ref-53)

---

<a id="metals-spin"></a>
## 8 · k-points, smearing and spin in metals

Brillouin-zone integration is approximated by weighted k-point sums. Metals have states crossing the Fermi level, making meshes and occupation treatment especially important. Monkhorst–Pack sampling, smearing methods and tetrahedron integration are alternative numerical components whose use must be documented. [7](#ref-7) [8](#ref-8) [9](#ref-9)

Do not interchange a code's electronic free energy, internal energy and extrapolated zero-smearing energy without checking definitions. Converge the quantity used in the actual energy difference. Empty bands and broadening suitable for relaxation may be inadequate for a detailed unoccupied-state analysis.

Use a justified spin-polarized baseline for ferromagnetic bcc Fe, examine surface moments, and record magnetic alternatives. Atom-resolved moments depend on the integration/projector convention. A singlet isolated inhibitor does not make the metal–inhibitor system a singlet. [47](#ref-47)

---

<a id="slabs"></a>
## 9 · From bulk to a defensible corrosion surface

Define bulk lattice provenance, facet, termination, stoichiometry, slab thickness, lateral area, fixed atoms and vacuum before adsorbate placement. Converge a bulk reference, then verify the slab's interior, surface relaxation and electronic behavior.

An asymmetric slab can carry a dipole that interacts with its periodic images. Use appropriate electrostatic treatment and verify a vacuum plateau before work-function analysis. More vacuum is not a universal remedy for a charged repeated slab. [21](#ref-21)

Distinguish bare Fe, hydroxylated Fe, oxide surfaces and metal/oxide interfaces. Fe(110) is a useful controlled teaching surface, not a substitute for every alloy grain, defect or passive film. [47](#ref-47) [36](#ref-36)

---

<a id="convergence"></a>
## 10 · Converge observables, separate model uncertainty

| Check | Main observable to monitor | Why a total-energy plateau is insufficient |
|---|---|---|
| Cutoffs/basis/density grid | Binding differences, forces, basin charges | These may demand different precision |
| k-points/smearing/bands | Adsorption, Fe moments, DOS, work function | Metallic occupations and projections matter |
| Slab thickness/vacuum | Surface energy, work function, binding | Central layers and potential plateau must be valid |
| Lateral area/coverage | Binding, packing, image interactions | The physical adsorbate density changes |
| SCF/force/Hessian settings | Geometry and vibrational corrections | A finished job may not be a minimum |

Define acceptance tolerances appropriate to the scientific comparison. Revisit close competitors with tighter common settings. Test fixed-geometry numerical effects separately from relaxation where useful.

XC, dispersion, U, magnetic state, protonation and surface phase belong in a **model sensitivity** table. Solvent configurations and adsorption starts belong in a **sampling** table. Neither is eliminated by increasing numerical precision. [Full convergence chapter](docs/22_convergence.md).

---

<a id="adsorption"></a>
## 11 · Adsorption, interaction and deformation

For a surface S and molecule M, define the electronic adsorption energy explicitly:

```math
E_{\mathrm{ads}}=E_{SM}^{\mathrm{rel}}-E_S^{\mathrm{rel}}-E_M^{\mathrm{rel}}.
```

Negative means exothermic relative to those references. It does not by itself mean adsorption from water is favorable. Charge, protonation, solvent and standard states belong in a balanced thermodynamic cycle.

Frozen-fragment calculations distinguish contact interaction from distortion:

```math
\begin{aligned}
E_{\mathrm{int}}&=E_{SM}^{\mathrm{rel}}-E_S^{\mathrm{frz}}-E_M^{\mathrm{frz}},\\
E_{\mathrm{def}}&=(E_S^{\mathrm{frz}}-E_S^{\mathrm{rel}})+(E_M^{\mathrm{frz}}-E_M^{\mathrm{rel}}),\\
E_{\mathrm{ads}}&=E_{\mathrm{int}}+E_{\mathrm{def}}.
\end{aligned}
```

This is reference-dependent bookkeeping, not a unique experimental energy decomposition. Localized basis sets may require BSSE/basis sensitivity assessment. The [adsorption chapter](docs/08_adsorption_theory.md) explains solution displacement and competing adsorbates. [33](#ref-33)

---

<a id="search-coverage"></a>
## 12 · Sites, orientation and coverage

Test several geometrically sensible starts rather than one optimized image. Flat, tilted and upright molecules can reach different contacts or the same final minimum. Keep the duplicate map and failed attempts. Define top/bridge/hollow sites according to the actual lattice; bcc(110) geometry should not be labeled by analogy to fcc(111) without inspection.

Molecular surface density is number per area. Fractional site coverage additionally needs a site/footprint convention. A periodic overlayer does not define a solution concentration. Intermolecular hydrogen bonding can motivate a cooperative adsorption hypothesis, but its behavior must be tested on the chosen facet and chemical state. [46](#ref-46)

Do not equate an experimental efficiency inferred from corrosion current with the occupied-site fraction. That requires an additional kinetic/blocking model. [51](#ref-51)

---

<a id="inhibitor-descriptors"></a>
## 13 · Molecular inhibitor descriptors without overclaiming

Vertical ionization/electron-attachment energies use the same reference nuclear geometry:

```math
I_v=E(N-1,\mathbf R_0)-E(N,\mathbf R_0),\qquad
A_v=E(N,\mathbf R_0)-E(N+1,\mathbf R_0).
```

HOMO/LUMO eigenvalues are not automatically these energy differences. The exact integer-electron behavior and approximate-functional errors make unqualified Koopmans-style interpretations unreliable. [13](#ref-13)

This course uses the curvature convention consistently:

```math
\mu=-\frac{I+A}{2},\quad \chi=-\mu,\quad
\eta_c=I-A,\quad S_c=\eta_c^{-1},\quad \omega_c=\frac{\mu^2}{2\eta_c}.
```

Other literature uses half-gap hardness, `eta_h=(I−A)/2`, and sometimes different softness/electrophilicity prefactors. Always publish the equation, not just the symbol. The [molecular chapter](docs/02_molecular_vs_periodic_dft.md) gives the conversion and the approximate quadratic-response derivation. [10](#ref-10) [11](#ref-11) [12](#ref-12)

Dipole, electrostatic potential and Fukui functions can suggest local reactivity or orientation. They do not include the real surface, adsorbed coverage, electrolyte or reaction kinetics. Empirical correlations should be tested for chemical-state consistency, domain of applicability and independent validation. [42](#ref-42)

---

<a id="water-ions"></a>
## 14 · Water, oxygen, hydroxyl and aggressive ions

Water can compete for sites, orient in interfacial fields and mediate proton transfer. Oxygen/hydroxyl can change surface composition rather than merely decorate the same metal model. Facet and pre-oxidation affect which comparisons are meaningful; a recent study of water on iron surfaces provides a specific illustration, not universal rules for every steel. [48](#ref-48)

A chloride study must specify whether it models neutral Cl, a charged adsorbed species or exchange with aqueous Cl−. These are not interchangeable reference reactions. Charge compensation, ion chemical potentials and potential control are central to a realistic comparison.

An inhibitor may displace interfacial water, coadsorb with aggressive species or bind to hydroxylated oxides. A vacuum molecular adsorption energy cannot establish which competition wins in solution. [34](#ref-34) [35](#ref-35)

---

<a id="surface-defects"></a>
## 15 · Surface stability, vacancies and dissolution

For two equivalent stoichiometric faces:

```math
\gamma=\frac{E_{\mathrm{slab}}-N e_{\mathrm{bulk}}}{2A}.
```

For nonstoichiometric or environment-dependent surfaces, include the appropriate chemical potentials. For inequivalent faces, the simple expression gives an aggregate excess, not either individual surface energy. [22](#ref-22)

A neutral vacancy expression is:

```math
E_{\mathrm{vac}}^0=E_{\mathrm{def}}-E_{\mathrm{perfect}}+\mu_X.
```

It is not automatically an electrochemical dissolution free energy or barrier. Dissolution can involve hydrated ions, electron exchange, solvent reorganization and path-dependent activation. Defect populations also depend on chemical potentials, entropy and kinetics. [37](#ref-37)

---

<a id="passivation"></a>
## 16 · Oxides and passive films

| Teaching phase | Important distinctions |
|---|---|
| Fe | Metallic magnetic reference; bare surface not necessarily experiment |
| FeO / Fe1−xO | Ideal stoichiometric crystal versus nonstoichiometry and defect chemistry |
| Fe3O4 | Magnetite; mixed Fe environments, magnetic ordering and cation defects |
| Fe2O3 | Specify polymorph: hematite and maghemite are not interchangeable |

A stable oxide is not necessarily a protective film. Continuity, adhesion, transport, dissolution and environmental stability matter. Real steel/passive interfaces can be multicomponent, hydroxylated, amorphous and spatially graded. [40](#ref-40) [36](#ref-36)

Do not only test oxygen vacancies by convenience: magnetite(001)'s subsurface-cation-vacancy reconstruction is a specific reason to consider cation rearrangements where relevant. It is not a universal aqueous-film structure. [52](#ref-52)

---

<a id="analysis-table"></a>
## 17 · What each DFT analysis tells us

| Analysis | Physical meaning | Corrosion use | Inference limit |
|---|---|---|---|
| Geometry / contacts | Local structural stationary state | Attachment motif and footprint | Not global minimum or actual film |
| Adsorption / deformation | Reference-specific energy change | Binding comparison / distortion cost | Not efficiency or solution free energy |
| Coverage | Periodic surface density / arrangement | Cooperative or crowded motifs | Not directly concentration or isotherm |
| Surface / defect energies | Excess/formation energies with reservoirs | Candidate phases and defect sites | Not transport/dissolution kinetics |
| DOS / PDOS / spin DOS | Electronic states and projected character | Candidate hybridization and magnetic effects | Peak overlap does not prove a bond |
| CDD | Spatial electron redistribution | Polarization and accumulation/depletion | Not unique net transfer |
| Bader | Basin electron populations | Partitioned charge changes | Not oxidation state or current |
| ELF | Localization indicator | Lone-pair/bonding-region patterns | Not transferred charge or binding strength |
| COHP / ICOHP | Hamiltonian-weighted projected bonding | Bonding/antibonding contributions | Not dissociation energy |
| Work function / potential | Vacuum electron-removal energy / spatial potential | Dipole and referencing checks | Not corrosion potential |
| Magnetic moments / d center | Spin populations / projected spectral moment | Electronic descriptors within a defined family | Not universal activity descriptors |
| Frequencies / ZPE / entropy | Curvature and nuclear thermal contributions | Stationary states and free energies | Partial Hessians and low modes need care |
| NEB | Path-specific barrier | Elementary-event kinetics | Not overall corrosion rate |
| AIMD / RDF | Finite-time dynamics and pair structure | Hydration and sampled configurations | Not long-term stability |

The [26-card catalogue](docs/24_analysis_catalogue.md) supplies the equation/definition, question, justified conclusion, invalid conclusion, common mistakes and deliverable for **every analysis**, not just its name. Sources include the original Bader, ELF, COHP and NEB methods. [18](#ref-18) [19](#ref-19) [20](#ref-20) [17](#ref-17)

---

<a id="spectral-analysis"></a>
## 18 · DOS, PDOS, bands and magnetic interpretation

Total DOS distributes one-electron states in energy; PDOS assigns approximate atomic/orbital character through a declared projector. Band structures show dispersion and may help with semiconducting oxides, but a molecular “gap” discussion does not describe a metal surface.

Use consistent references when comparing separate calculations, specify spin and broadening, and check that enough bands and k-points represent the target spectrum. Fe d / inhibitor p mixing is a hypothesis supported by appropriate projections and geometry—not proven by any two coincident peaks.

A d-band center is a first moment over a chosen projected spectrum and window. Its value depends on the reference, integration range, spin and projection. It should not be used as a universal corrosion ranking across metals, oxides and unrelated inhibitor species. [Detailed spectral chapter](docs/11_dos_pdos_bands.md).

---

<a id="charge-bonding"></a>
## 19 · Charge transfer, localization and bonding

Use **electron-number density** in the following CDD:

```math
\Delta n(\mathbf r)=n_{SM}(\mathbf r)-n_S^{\mathrm{frz}}(\mathbf r)-n_M^{\mathrm{frz}}(\mathbf r).
```

Positive values mean electron accumulation; physical electron charge density has the opposite sign. Match frozen fragment geometry, cell and grid. For matched electron counts the total integral is zero, but spatial redistribution can be large.

Bader analysis integrates zero-flux basins. Match valence density with valence reference charges, or consistently use an appropriate all-electron convention. Its charge is partition-specific, not a formal oxidation state. [18](#ref-18)

ELF identifies localization features, while COHP/ICOHP evaluates projected bonding/antibonding contributions. Check the `COHP` versus `−COHP` sign convention and projection quality. Do not interpret either as a direct corrosion-resistance measurement. [19](#ref-19) [20](#ref-20) [26](#ref-26)

---

<a id="work-function"></a>
## 20 · Work function and electrostatic potential

For a slab with an appropriate vacuum reference:

```math
\Phi=V_{\mathrm{vac}}^{(e)}-E_F.
```

`Vvac(e)` denotes **electron potential energy**, not an unqualified voltage. Extract a plateau on the specified slab face and document electrostatic correction, smoothing and units. An adsorbed asymmetric slab can have different face-specific values.

An adsorption-induced shift probes electronic/dipole changes. It is not an uncalibrated absolute electrode potential and does not equal the mixed corrosion potential. Either sign can occur; do not assign a universal “protective” direction. [21](#ref-21) [38](#ref-38)

---

<a id="thermochemistry"></a>
## 21 · Vibrations, ZPE, entropy and free energy

Frequencies probe local curvature in the Hessian subspace actually calculated. A full unconstrained minimum has no genuine unstable vibrational direction; a transition-state candidate normally has one relevant unstable direction. Adsorbate-only Hessians do not verify the entire slab.

In a harmonic treatment:

```math
F_{\mathrm{vib}}(T)=\sum_i\left[\frac{\hbar\omega_i}{2}
+k_BT\ln(1-e^{-\hbar\omega_i/k_BT})\right].
```

This already contains ZPE; do not add it a second time. Soft adsorbate translations/rotations can require hindered-motion or configurational models. Gas, adsorbed and solution species must use compatible but physically appropriate standard states.

An approximate free-energy ledger can combine electronic, nuclear thermal, solvation and standard-state contributions. Every proton/electron/ion must be balanced. A favorable free energy establishes thermodynamic preference in that model, not a kinetic rate. [Thermochemistry and pathway chapter](docs/16_reaction_pathways_neb.md).

---

<a id="electrolyte"></a>
## 22 · Solvation and the electrochemical interface hierarchy

A vacuum slab isolates bonding. Implicit solvent adds a continuum response with a specified cavity and parameters. Explicit solvent resolves local molecular structure but requires sampling. Combining explicit interfacial molecules with an outer continuum can be useful, provided reference and cavity choices remain consistent. [24](#ref-24)

A realistic electrochemical model may also need ions, surface charge, potential control and a double layer. A neutral cell with a few water molecules does not automatically meet these requirements. A charged periodically repeated cell with compensating background can carry severe electrostatic artifacts. Modern reviews distinguish the available ensemble and environment approximations rather than treating them as one interchangeable “electrochemical DFT” method. [38](#ref-38) [39](#ref-39)

---

<a id="potential-che"></a>
## 23 · Constant charge, constant potential and CHE

Ordinary canonical calculations specify electron number. An electrode at fixed potential can exchange electrons, motivating a grand-potential description:

```math
\Omega(\mu_e,T)=\min_{N_e}\{F(N_e,T)-\mu_eN_e\}.
```

Nuclear species reservoirs must be added where reactions exchange atoms/ions. A constant-charge energy difference is not automatically a constant-potential free-energy difference. [25](#ref-25)

For the computational hydrogen electrode, with positive elementary charge e and potential versus SHE:

```math
\mu_{\mathrm H^++e^-}=\tfrac12G_{\mathrm H_2}
-eU_{\mathrm{SHE}}-k_BT\ln(10)\,\mathrm{pH}.
```

A reduction step **consuming n matched proton–electron pairs** therefore has:

```math
\Delta G(U,\mathrm{pH})=\Delta G(0,0)
+neU_{\mathrm{SHE}}+nk_BT\ln(10)\,\mathrm{pH}.
```

With `U_RHE = U_SHE + (kBT ln10/e)pH`, the explicit pH term is absorbed for such matched-pair bookkeeping. Do not double count pH or apply this shortcut to unmatched ion/proton/electron stoichiometries. CHE is not a model of double-layer structure or activation barriers. [23](#ref-23)

---

<a id="kinetics-dynamics"></a>
## 24 · NEB, kinetics, AIMD and RDF

NEB approximates a minimum-energy path between endpoints; climbing-image refinement targets a saddle-point candidate. Optimize endpoints, preserve atom mapping, converge image forces and check the unstable mode. A reaction energy is not an activation barrier. [17](#ref-17)

```math
\Delta G^\ddagger=G_{\mathrm{TS}}-G_{\mathrm{IS}},\qquad
k\simeq\kappa\frac{k_BT}{h}\exp[-\Delta G^\ddagger/(k_BT)].
```

The rate expression is an elementary transition-state-theory approximation, not a full corrosion law. Solvent and potential can alter the barrier and competing pathways.

AIMD supplies finite-time trajectories on an approximate DFT surface, generally with classical nuclei. Check temperature/energy behavior, SCF precision, timestep, equilibration and independent sampling. No desorption in a short trajectory does not establish a film lifetime. For interfacial RDF/coordination, avoid normalizing a liquid by a cell volume that includes vacuum or inaccessible slab volume. [53](#ref-53) [35](#ref-35)

---

<a id="case-study"></a>
## 25 · A staged Fe(110)/imidazole investigation

The [case-study protocol](case-study/README.md) progresses through **ten phases**: bulk Fe, clean slab, isolated neutral molecule, adsorption search, energies, spin-resolved electronic structure, charge redistribution, work function, coverage and environment.

It supplies a decision gate and deliverable for each phase. The [six CSV worksheets](case-study/worksheets/README.md) contain **headers, not calculated data**. The [model card](case-study/worksheets/model-card.md) records assumptions before any calculation.

Camacho-Mendoza et al. provide a relevant Fe(110) imidazole-derivative precedent. Other prominent imidazole film/dissociation studies concern **Fe(100)**; they motivate controls but cannot be presented as Fe(110) numerical results. [44](#ref-44) [45](#ref-45) [46](#ref-46)

The proposed study may establish which **tested** neutral vacuum configurations are more favorable and why. It cannot establish experimental inhibition efficiency, aqueous protonation populations or long-term film durability without additional evidence.

---

<a id="software"></a>
## 26 · Solvers versus analysis tools

| Electronic-structure engine | Representation | Relevant teaching scope |
|---|---|---|
| VASP | Plane waves / PAW | Magnetic slabs, adsorption, oxide states, pathways |
| Quantum ESPRESSO | Plane waves / pseudopotentials and PAW | Periodic surfaces, response and paths |
| CP2K | Gaussian orbitals + density grids/plane waves | Large interfaces, solvent and dynamics |
| GPAW | PAW with grid/PW/LCAO choices | Python-oriented surface/electrochemical models |
| CASTEP | Plane waves / pseudopotentials | Solid/surface/vibrational calculations |
| ABINIT | Plane waves / pseudopotentials and PAW | Bulk, defects, response and surfaces |

The [software chapter](docs/23_software_and_analysis_tools.md) contains official-source links, licensing distinctions, NEB/AIMD capability notes, solvent/electrode routes and the limits of those claims. Features and allowed combinations are release dependent.

VESTA and OVITO primarily visualize/inspect structures and fields. ASE and pymatgen manage atomistic/materials data and workflows. VASPKIT and py4vasp provide VASP-oriented analysis. Bader tools, LOBSTER, Multiwfn and Critic2 answer different density/wavefunction/bonding questions; compatibility and definitions must be checked. They are not interchangeable DFT solvers. [27](#ref-27) [28](#ref-28) [29](#ref-29) [30](#ref-30) [31](#ref-31) [32](#ref-32)

---

<a id="experiment"></a>
## 27 · Connecting to experiment

DFT can test structural assignments consistent with XPS, vibrational changes in FTIR/Raman, or candidate surface/film arrangements seen in microscopy. A proper simulated spectrum requires more than displaying DOS. Bader charges are not XPS binding energies.

Polarization and EIS probe current/kinetic/interfacial response under particular protocols. An adsorption energy does not directly give corrosion current or charge-transfer resistance. SEM/TEM/AFM access structures at scales and conditions that one ideal slab does not reproduce. A single water adsorption energy is not a contact angle.

Match surface preparation, alloy, electrolyte, oxygen, pH, temperature, concentration and time before comparing. The [experimental chapter](docs/25_connection_with_experiment.md) provides a measurement-by-measurement map and limitations. [36](#ref-36) [37](#ref-37) [51](#ref-51)

---

<a id="reporting"></a>
## 28 · Reporting and preventing overinterpretation

A complete report preserves structures and state IDs, code/version, functional/corrections, basis/data provenance, magnetic treatment, numerical tests, surface model, reference equations, density conventions and environmental assumptions. Keep failed searches and ambiguous rankings visible.

Use a layered conclusion: **observation → robustness → mechanism → environmental relevance → performance connection**. Do not skip from the first to the last. A claim should name its reference and uncertainty and explicitly state what remains untested.

Use the [reporting chapter](docs/21_reporting_and_reproducibility.md), [common-mistake table](docs/19_common_mistakes.md), [interpretation chapter](docs/20_interpreting_results.md) and [study checklist](CHECKLIST.md). Numerical precision, model error and sampling uncertainty are separate categories.

---

<a id="figures"></a>
## 29 · Figures, teaching materials and reuse

This edition supplies **ten original figure-design briefs**, with intended panels, annotations, reference-linked captions and safeguards against presenting schematics as computed results. They cover the workflow, molecular/periodic distinction, Fe slab, adsorption-energy bookkeeping, CDD, PDOS, work function, case study, electrochemical hierarchy and analysis-to-evidence map.

The briefs are proposals, not image files or simulated plots. No publisher figure is reproduced. [Figure briefs](figures/README.md).

Original educational text and original repository code use the [MIT license](LICENSE). Third-party papers, software, data and trademarks retain their own rights. See [reuse notes](THIRD_PARTY.md). Public contact placeholders remain in [CONTACT.md](CONTACT.md); no institutional or unpublished project information is included.

---

<a id="references"></a>
## 30 · References and source verification

The bibliography below contains **55 unique DOI-bearing references**, matching every entry in [references.bib](references.bib). The [source map](SOURCES.md) identifies what each reading contributes and the evidence-access limitations. The [verification ledger](reference-verification.csv) records a bibliographic evidence URL, access description and any caveat for each DOI.

Most metadata were checked on publisher or author/official records. Some inaccessible original pages were cross-checked through bibliographic records or publisher reference lists. **A verified title/DOI is not the same as a full-text review.** This repository does not claim all full texts were accessible or that every DOI redirect will resolve in every network environment.

Method definitions and explicit algebraic derivations are distinguished from source-specific empirical findings. Do not treat a bibliographic citation as support for transferring a result to another facet, chemical state or environment.

<a id="ref-1"></a>
**[1]** P. Hohenberg; W. Kohn (1964). **Inhomogeneous Electron Gas.** *Physical Review* **136**, B864–B871. [DOI: 10.1103/PhysRev.136.B864](https://doi.org/10.1103/PhysRev.136.B864).

<a id="ref-2"></a>
**[2]** W. Kohn; L. J. Sham (1965). **Self-Consistent Equations Including Exchange and Correlation Effects.** *Physical Review* **140**, A1133–A1138. [DOI: 10.1103/PhysRev.140.A1133](https://doi.org/10.1103/PhysRev.140.A1133).

<a id="ref-3"></a>
**[3]** John P. Perdew; Kieron Burke; Matthias Ernzerhof (1996). **Generalized Gradient Approximation Made Simple.** *Physical Review Letters* **77**, 3865–3868. [DOI: 10.1103/PhysRevLett.77.3865](https://doi.org/10.1103/PhysRevLett.77.3865).

<a id="ref-4"></a>
**[4]** G. Kresse; J. Furthmüller (1996). **Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set.** *Physical Review B* **54**, 11169–11186. [DOI: 10.1103/PhysRevB.54.11169](https://doi.org/10.1103/PhysRevB.54.11169).

<a id="ref-5"></a>
**[5]** Peter E. Blöchl (1994). **Projector augmented-wave method.** *Physical Review B* **50**, 17953–17979. [DOI: 10.1103/PhysRevB.50.17953](https://doi.org/10.1103/PhysRevB.50.17953).

<a id="ref-6"></a>
**[6]** G. Kresse; D. Joubert (1999). **From ultrasoft pseudopotentials to the projector augmented-wave method.** *Physical Review B* **59**, 1758–1775. [DOI: 10.1103/PhysRevB.59.1758](https://doi.org/10.1103/PhysRevB.59.1758).

<a id="ref-7"></a>
**[7]** Hendrik J. Monkhorst; James D. Pack (1976). **Special points for Brillouin-zone integrations.** *Physical Review B* **13**, 5188–5192. [DOI: 10.1103/PhysRevB.13.5188](https://doi.org/10.1103/PhysRevB.13.5188).

<a id="ref-8"></a>
**[8]** M. Methfessel; A. T. Paxton (1989). **High-precision sampling for Brillouin-zone integration in metals.** *Physical Review B* **40**, 3616–3621. [DOI: 10.1103/PhysRevB.40.3616](https://doi.org/10.1103/PhysRevB.40.3616).

<a id="ref-9"></a>
**[9]** Peter E. Blöchl; O. Jepsen; O. K. Andersen (1994). **Improved tetrahedron method for Brillouin-zone integrations.** *Physical Review B* **49**, 16223–16233. [DOI: 10.1103/PhysRevB.49.16223](https://doi.org/10.1103/PhysRevB.49.16223).

<a id="ref-10"></a>
**[10]** Robert G. Parr; Ralph G. Pearson (1983). **Absolute hardness: companion parameter to absolute electronegativity.** *Journal of the American Chemical Society* **105**, 7512–7516. [DOI: 10.1021/ja00364a005](https://doi.org/10.1021/ja00364a005).

<a id="ref-11"></a>
**[11]** Robert G. Parr; László von Szentpály; Shubin Liu (1999). **Electrophilicity Index.** *Journal of the American Chemical Society* **121**, 1922–1924. [DOI: 10.1021/ja983494x](https://doi.org/10.1021/ja983494x).

<a id="ref-12"></a>
**[12]** P. Geerlings; F. De Proft; W. Langenaeker (2003). **Conceptual Density Functional Theory.** *Chemical Reviews* **103**, 1793–1874. [DOI: 10.1021/cr990029p](https://doi.org/10.1021/cr990029p).

<a id="ref-13"></a>
**[13]** John P. Perdew; Robert G. Parr; Mel Levy; John L. Balduz, Jr. (1982). **Density-Functional Theory for Fractional Particle Number: Derivative Discontinuities of the Energy.** *Physical Review Letters* **49**, 1691–1694. [DOI: 10.1103/PhysRevLett.49.1691](https://doi.org/10.1103/PhysRevLett.49.1691).

<a id="ref-14"></a>
**[14]** Matteo Cococcioni; Stefano de Gironcoli (2005). **Linear response approach to the calculation of the effective interaction parameters in the LDA+U method.** *Physical Review B* **71**, 035105. [DOI: 10.1103/PhysRevB.71.035105](https://doi.org/10.1103/PhysRevB.71.035105).

<a id="ref-15"></a>
**[15]** Stefan Grimme; Stephan Ehrlich; Lars Goerigk (2011). **Effect of the damping function in dispersion corrected density functional theory.** *Journal of Computational Chemistry* **32**, 1456–1465. [DOI: 10.1002/jcc.21759](https://doi.org/10.1002/jcc.21759).

<a id="ref-16"></a>
**[16]** Jianwei Sun; Adrienn Ruzsinszky; John P. Perdew (2015). **Strongly Constrained and Appropriately Normed Semilocal Density Functional.** *Physical Review Letters* **115**, 036402. [DOI: 10.1103/PhysRevLett.115.036402](https://doi.org/10.1103/PhysRevLett.115.036402).

<a id="ref-17"></a>
**[17]** Graeme Henkelman; Blas P. Uberuaga; Hannes Jónsson (2000). **A climbing image nudged elastic band method for finding saddle points and minimum energy paths.** *The Journal of Chemical Physics* **113**, 9901–9904. [DOI: 10.1063/1.1329672](https://doi.org/10.1063/1.1329672).

<a id="ref-18"></a>
**[18]** Graeme Henkelman; Andri Arnaldsson; Hannes Jónsson (2006). **A fast and robust algorithm for Bader decomposition of charge density.** *Computational Materials Science* **36**, 354–360. [DOI: 10.1016/j.commatsci.2005.04.010](https://doi.org/10.1016/j.commatsci.2005.04.010).

<a id="ref-19"></a>
**[19]** Axel D. Becke; Kenneth E. Edgecombe (1990). **A simple measure of electron localization in atomic and molecular systems.** *The Journal of Chemical Physics* **92**, 5397–5403. [DOI: 10.1063/1.458517](https://doi.org/10.1063/1.458517).

<a id="ref-20"></a>
**[20]** Richard Dronskowski; Peter E. Blöchl (1993). **Crystal orbital Hamilton populations (COHP): energy-resolved visualization of chemical bonding in solids based on density-functional calculations.** *The Journal of Physical Chemistry* **97**, 8617–8624. [DOI: 10.1021/j100135a014](https://doi.org/10.1021/j100135a014).

<a id="ref-21"></a>
**[21]** Lennart Bengtsson (1999). **Dipole correction for surface supercell calculations.** *Physical Review B* **59**, 12301–12304. [DOI: 10.1103/PhysRevB.59.12301](https://doi.org/10.1103/PhysRevB.59.12301).

<a id="ref-22"></a>
**[22]** Karsten Reuter; Matthias Scheffler (2001). **Composition, structure, and stability of RuO2(110) as a function of oxygen pressure.** *Physical Review B* **65**, 035406. [DOI: 10.1103/PhysRevB.65.035406](https://doi.org/10.1103/PhysRevB.65.035406).

<a id="ref-23"></a>
**[23]** J. K. Nørskov et al. (2004). **Origin of the Overpotential for Oxygen Reduction at a Fuel-Cell Cathode.** *The Journal of Physical Chemistry B* **108**, 17886–17892. [DOI: 10.1021/jp047349j](https://doi.org/10.1021/jp047349j).

<a id="ref-24"></a>
**[24]** Kiran Mathew et al. (2014). **Implicit solvation model for density-functional study of nanocrystal surfaces and reaction pathways.** *The Journal of Chemical Physics* **140**, 084106. [DOI: 10.1063/1.4865107](https://doi.org/10.1063/1.4865107).

<a id="ref-25"></a>
**[25]** Ravishankar Sundararaman; William A. Goddard, III; Tomas A. Arias (2017). **Grand canonical electronic density-functional theory: Algorithms and applications to electrochemistry.** *The Journal of Chemical Physics* **146**, 114104. [DOI: 10.1063/1.4978411](https://doi.org/10.1063/1.4978411).

<a id="ref-26"></a>
**[26]** Stefan Maintz; Volker L. Deringer; Andrei L. Tchougréeff; Richard Dronskowski (2016). **LOBSTER: A tool to extract chemical bonding from plane-wave based DFT.** *Journal of Computational Chemistry* **37**, 1030–1035. [DOI: 10.1002/jcc.24300](https://doi.org/10.1002/jcc.24300).

<a id="ref-27"></a>
**[27]** Koichi Momma; Fujio Izumi (2011). **VESTA 3 for three-dimensional visualization of crystal, volumetric and morphology data.** *Journal of Applied Crystallography* **44**, 1272–1276. [DOI: 10.1107/S0021889811038970](https://doi.org/10.1107/S0021889811038970).

<a id="ref-28"></a>
**[28]** Ask Hjorth Larsen et al. (2017). **The atomic simulation environment—a Python library for working with atoms.** *Journal of Physics: Condensed Matter* **29**, 273002. [DOI: 10.1088/1361-648X/aa680e](https://doi.org/10.1088/1361-648X/aa680e).

<a id="ref-29"></a>
**[29]** Shyue Ping Ong et al. (2013). **Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis.** *Computational Materials Science* **68**, 314–319. [DOI: 10.1016/j.commatsci.2012.10.028](https://doi.org/10.1016/j.commatsci.2012.10.028).

<a id="ref-30"></a>
**[30]** Vei Wang et al. (2021). **VASPKIT: A user-friendly interface facilitating high-throughput computing and analysis using VASP code.** *Computer Physics Communications* **267**, 108033. [DOI: 10.1016/j.cpc.2021.108033](https://doi.org/10.1016/j.cpc.2021.108033).

<a id="ref-31"></a>
**[31]** Alberto Otero-de-la-Roza; Erin R. Johnson; Víctor Luaña (2014). **Critic2: A program for real-space analysis of quantum chemical interactions in solids.** *Computer Physics Communications* **185**, 1007–1018. [DOI: 10.1016/j.cpc.2013.10.026](https://doi.org/10.1016/j.cpc.2013.10.026).

<a id="ref-32"></a>
**[32]** Tian Lu; Feiwu Chen (2012). **Multiwfn: A multifunctional wavefunction analyzer.** *Journal of Computational Chemistry* **33**, 580–592. [DOI: 10.1002/jcc.22885](https://doi.org/10.1002/jcc.22885).

<a id="ref-33"></a>
**[33]** Anton Kokalj (2021). **Molecular modeling of organic corrosion inhibitors: Calculations, pitfalls, and conceptualization of molecule–surface bonding.** *Corrosion Science* **193**, 109650. [DOI: 10.1016/j.corsci.2021.109650](https://doi.org/10.1016/j.corsci.2021.109650).

<a id="ref-34"></a>
**[34]** Dihao Chen; Wenjie Zhou; Yucheng Ji; Chaofang Dong (2025). **Applications of density functional theory to corrosion and corrosion prevention of metals: A review.** *Materials Genome Engineering Advances* **3**, e83. [DOI: 10.1002/mgea.83](https://doi.org/10.1002/mgea.83).

<a id="ref-35"></a>
**[35]** Shuhao Li; Chunqing Li; Feng Wang (2024). **Computational experiments of metal corrosion studies: A review.** *Materials Today Chemistry*, 101986. [DOI: 10.1016/j.mtchem.2024.101986](https://doi.org/10.1016/j.mtchem.2024.101986).

<a id="ref-36"></a>
**[36]** Vincent Maurice; Philippe Marcus (2018). **Progress in corrosion science at atomic and nanometric scales.** *Progress in Materials Science* **95**, 132–171. [DOI: 10.1016/j.pmatsci.2018.03.001](https://doi.org/10.1016/j.pmatsci.2018.03.001).

<a id="ref-37"></a>
**[37]** Christopher D. Taylor; Huibin Ke (2021). **Investigations of the intrinsic corrosion and hydrogen susceptibility of metals and alloys using density functional theory.** *Corrosion Reviews* **39**, 177–209. [DOI: 10.1515/corrrev-2020-0094](https://doi.org/10.1515/corrrev-2020-0094).

<a id="ref-38"></a>
**[38]** Kathleen Schwarz; Ravishankar Sundararaman (2020). **The electrochemical interface in first-principles calculations.** *Surface Science Reports* **75**, 100492. [DOI: 10.1016/j.surfrep.2020.100492](https://doi.org/10.1016/j.surfrep.2020.100492).

<a id="ref-39"></a>
**[39]** Mira Todorova; Stefan Wippermann; Jörg Neugebauer (2026). **First-principles approaches and concepts to simulate electrochemical interfaces.** *Nature Reviews Chemistry* **10**, 133–146. [DOI: 10.1038/s41570-025-00792-6](https://doi.org/10.1038/s41570-025-00792-6).

<a id="ref-40"></a>
**[40]** Gareth S. Parkinson (2016). **Iron oxide surfaces.** *Surface Science Reports* **71**, 272–365. [DOI: 10.1016/j.surfrep.2016.02.001](https://doi.org/10.1016/j.surfrep.2016.02.001).

<a id="ref-41"></a>
**[41]** I. B. Obot; D. D. Macdonald; Z. M. Gasem (2015). **Density functional theory (DFT) as a powerful tool for designing new organic corrosion inhibitors. Part 1: An overview.** *Corrosion Science* **99**, 1–30. [DOI: 10.1016/j.corsci.2015.01.037](https://doi.org/10.1016/j.corsci.2015.01.037).

<a id="ref-42"></a>
**[42]** Anton Kokalj (2010). **Is the analysis of molecular electronic structure of corrosion inhibitors sufficient to predict the trend of their inhibition performance.** *Electrochimica Acta* **56**, 745–755. [DOI: 10.1016/j.electacta.2010.09.065](https://doi.org/10.1016/j.electacta.2010.09.065).

<a id="ref-43"></a>
**[43]** Anton Kokalj; Chenyang Xie; Ingrid Milošev; Daniel Crespo (2021). **How relevant are molecular electronic parameters for predicting corrosion inhibition efficiency: imidazoles as corrosion inhibitors of Cu/Zr materials in NaCl solution.** *Corrosion Science* **193**, 109900. [DOI: 10.1016/j.corsci.2021.109900](https://doi.org/10.1016/j.corsci.2021.109900).

<a id="ref-44"></a>
**[44]** Rosa L. Camacho-Mendoza et al. (2015). **Density Functional Theory and Electrochemical Studies: Structure–Efficiency Relationship on Corrosion Inhibition.** *Journal of Chemical Information and Modeling* **55**, 2391–2402. [DOI: 10.1021/acs.jcim.5b00385](https://doi.org/10.1021/acs.jcim.5b00385).

<a id="ref-45"></a>
**[45]** Anton Kokalj (2013). **Formation and structure of inhibitive molecular film of imidazole on iron surface.** *Corrosion Science* **68**, 195–203. [DOI: 10.1016/j.corsci.2012.11.015](https://doi.org/10.1016/j.corsci.2012.11.015).

<a id="ref-46"></a>
**[46]** Weina Zhao; Chang Shen; Anil Kumar Tummanapelli; Ming Wah Wong (2025). **Computational Insights Into Corrosion Inhibition Mechanism: Dissociation of Imidazole on Iron Surface.** *Journal of Computational Chemistry* **46**, e70047. [DOI: 10.1002/jcc.70047](https://doi.org/10.1002/jcc.70047).

<a id="ref-47"></a>
**[47]** Michelle J. S. Spencer; Andrew Hung; Ian K. Snook; Irene Yarovsky (2002). **Density functional theory study of the relaxation and energy of iron surfaces.** *Surface Science* **513**, 389–398. [DOI: 10.1016/S0039-6028(02)01809-5](https://doi.org/10.1016/S0039-6028(02)01809-5).

<a id="ref-48"></a>
**[48]** Adenilson Felipe Sousa-Silva et al. (2025). **Iron–Water Interface at Different Electrochemical Conditions.** *The Journal of Physical Chemistry C* **129**, 18666–18675. [DOI: 10.1021/acs.jpcc.5c04170](https://doi.org/10.1021/acs.jpcc.5c04170).

<a id="ref-49"></a>
**[49]** Dunja Gustinčič; Anton Kokalj (2015). **A DFT study of adsorption of imidazole, triazole, and tetrazole on oxidized copper surfaces: Cu2O(111) and Cu2O(111)-w/o-CuCUS.** *Physical Chemistry Chemical Physics* **17**, 28602–28615. [DOI: 10.1039/C5CP03647J](https://doi.org/10.1039/C5CP03647J).

<a id="ref-50"></a>
**[50]** Nataša Kovačević; Anton Kokalj (2012). **Chemistry of the interaction between azole type corrosion inhibitor molecules and metal surfaces.** *Materials Chemistry and Physics* **137**, 331–339. [DOI: 10.1016/j.matchemphys.2012.09.030](https://doi.org/10.1016/j.matchemphys.2012.09.030).

<a id="ref-51"></a>
**[51]** Monika S. Walczak; Perla Morales-Gil; Robert Lindsay (2019). **Determining Gibbs energies of adsorption from corrosion inhibition efficiencies: Is it a reliable approach?.** *Corrosion Science* **155**, 182–185. [DOI: 10.1016/j.corsci.2019.04.040](https://doi.org/10.1016/j.corsci.2019.04.040).

<a id="ref-52"></a>
**[52]** R. Bliem et al. (2014). **Subsurface cation vacancy stabilization of the magnetite (001) surface.** *Science* **346**, 1215–1218. [DOI: 10.1126/science.1260556](https://doi.org/10.1126/science.1260556).

<a id="ref-53"></a>
**[53]** Thomas D. Kühne et al. (2020). **CP2K: An electronic structure and molecular dynamics software package - Quickstep: Efficient and accurate electronic structure calculations.** *The Journal of Chemical Physics* **152**, 194103. [DOI: 10.1063/5.0007045](https://doi.org/10.1063/5.0007045).

<a id="ref-54"></a>
**[54]** J. Enkovaara et al. (2010). **Electronic structure calculations with GPAW: a real-space implementation of the projector augmented-wave method.** *Journal of Physics: Condensed Matter* **22**, 253202. [DOI: 10.1088/0953-8984/22/25/253202](https://doi.org/10.1088/0953-8984/22/25/253202).

<a id="ref-55"></a>
**[55]** Jochen Heyd; Gustavo E. Scuseria; Matthias Ernzerhof (2003). **Hybrid functionals based on a screened Coulomb potential.** *The Journal of Chemical Physics* **118**, 8207–8215. [DOI: 10.1063/1.1564060](https://doi.org/10.1063/1.1564060).

---

## Maintainer and contact

**Montassar Bouzidi**  
GitHub: [montassar-ML](https://github.com/montassar-ML)  
Personal email: `<ADD_EMAIL>`  
LinkedIn: `<ADD_LINKEDIN>`

This is an independent educational resource, not an endorsement by a software vendor or institution. Contributions should improve evidence, clarity or reproducibility; see [CONTRIBUTING.md](CONTRIBUTING.md).
