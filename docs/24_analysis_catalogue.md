# 24 · Analysis catalogue: what to calculate and what it means

[Course home](../README.md) · [Interpretation table](20_interpreting_results.md) · [Case study](../case-study/analyses.md)

This is a decision guide, not a mandate to calculate every observable. Start from the corrosion question and add an analysis only when it can test a hypothesis. The equations use electron-number density unless explicitly stated otherwise. Numerical implementation and units must still be checked in the chosen package.

Each of the **26 cards** contains the requested eight components: calculation, equation/definition, physical meaning, corrosion question, valid conclusion, invalid conclusion, common mistakes and output. Equations without a separate source-specific citation are standard definitions or explicit algebraic bookkeeping; linked papers establish the method or application context.

## Contents

- [01 · Geometry optimization](#geometry)

- [02 · Adsorption energy](#adsorption)

- [03 · Interaction and deformation energies](#deformation)

- [04 · Adsorption distances and molecular tilt](#distance)

- [05 · Multiple adsorption sites and orientations](#sites)

- [06 · Coverage and lateral interactions](#coverage)

- [07 · Surface energy and surface thermodynamics](#surface-energy)

- [08 · Vacancy and defect formation](#vacancies)

- [09 · Total density of states](#dos)

- [10 · Projected density of states](#pdos)

- [11 · Spin-resolved DOS](#spin-dos)

- [12 · Charge-density difference (electron-number convention)](#cdd)

- [13 · Bader charge](#bader)

- [14 · Electron localization function](#elf)

- [15 · COHP, projected COHP and ICOHP](#cohp)

- [16 · Work function and adsorption-induced shift](#work-function)

- [17 · Electrostatic potential profile](#potential)

- [18 · Total and local magnetic moments](#magnetism)

- [19 · d-band center](#d-band)

- [20 · Vibrational frequencies and stationary-point tests](#frequencies)

- [21 · Zero-point energy](#zpe)

- [22 · Entropy and thermal contributions](#entropy)

- [23 · Adsorption/reaction free energy](#free-energy)

- [24 · NEB and activation barriers](#neb)

- [25 · Ab initio molecular dynamics](#aimd)

- [26 · Radial distribution and interfacial coordination](#rdf)

<a id="geometry"></a>
## 01 · Geometry optimization

**1. What is calculated.** Minimize the Born–Oppenheimer energy with respect to the allowed coordinates while solving the electronic problem at each step.

**2. Equation or definition.**

```math
\mathbf F_I=-\frac{\partial E_{\mathrm{BO}}}{\partial\mathbf R_I};\qquad \mathbf F_I\rightarrow\mathbf 0\ \text{for relaxed degrees of freedom}.
```

**3. Physical meaning.** A local stationary structure within the chosen electronic, boundary and constraint model.

**4. Corrosion question.** Can a proposed inhibitor attachment motif persist after relaxation?

**5. Justified conclusion.** This structure is a converged local candidate; a frequency check can test curvature in the examined subspace.

**6. Conclusion not established.** It is the global minimum, the aqueous equilibrium structure or the protective film.

**7. Common mistakes.** Confusing electronic convergence with force convergence; ignoring fixed coordinates, symmetry trapping and magnetic alternatives.

**8. Typical output.** Final coordinates, force/displacement history, constraints and top/side structural views.

**Method/application references:** [2](../README.md#ref-2) [4](../README.md#ref-4)

---

<a id="adsorption"></a>
## 02 · Adsorption energy

**1. What is calculated.** Evaluate combined and separated relaxed reference systems with compatible Hamiltonians and numerical settings.

**2. Equation or definition.**

```math
E_{\mathrm{ads}}=E_{SM}^{\mathrm{rel}}-E_S^{\mathrm{rel}}-E_M^{\mathrm{rel}}.
```

**3. Physical meaning.** Electronic energy change relative to the specified surface S and molecule M reference states; negative means exothermic under this convention.

**4. Corrosion question.** Which comparable tested configuration binds more favorably?

**5. Justified conclusion.** A configuration is more favorable relative to those references if the difference exceeds practical numerical/model uncertainty.

**6. Conclusion not established.** The same ordering must hold for adsorption from solution or for inhibition efficiency.

**7. Common mistakes.** Mixing charged and neutral references, gas/solution states, energy conventions, spin states or incompatible settings; omitting dispersion/basis sensitivity.

**8. Typical output.** Energy ledger and adsorption-energy table with chemical state, geometry ID, reference IDs and uncertainty.

**Method/application references:** [33](../README.md#ref-33) [44](../README.md#ref-44)

---

<a id="deformation"></a>
## 03 · Interaction and deformation energies

**1. What is calculated.** Compute isolated fragments frozen at their positions in the combined relaxed structure, in addition to the individually relaxed fragments.

**2. Equation or definition.**

```math
E_{\mathrm{int}}=E_{SM}^{\mathrm{rel}}-E_S^{\mathrm{frz}}-E_M^{\mathrm{frz}},\qquad E_{\mathrm{def}}=(E_S^{\mathrm{frz}}-E_S^{\mathrm{rel}})+(E_M^{\mathrm{frz}}-E_M^{\mathrm{rel}}),\qquad E_{\mathrm{ads}}=E_{\mathrm{int}}+E_{\mathrm{def}}.
```

**3. Physical meaning.** An exact bookkeeping decomposition for the selected fragment definitions; it separates contact stabilization from structural distortion costs.

**4. Corrosion question.** Does a strongly interacting adsorption motif pay a large distortion penalty?

**5. Justified conclusion.** Net binding differences can be decomposed into these chosen contributions.

**6. Conclusion not established.** The decomposition is a unique observable or proves an elementary bonding mechanism.

**7. Common mistakes.** Using different frozen geometries or fragment electron counts; changing the basis environment without considering BSSE.

**8. Typical output.** Component table and labeled energy-level schematic without fictitious values.

**Method/application references:** [33](../README.md#ref-33)

---

<a id="distance"></a>
## 04 · Adsorption distances and molecular tilt

**1. What is calculated.** Measure nearest contacts and a defined molecular-plane angle relative to the surface normal/plane after relaxation.

**2. Equation or definition.**

```math
d_{AB}=|\mathbf R_A-\mathbf R_B|\quad\text{with the correct periodic minimum image}.
```

**3. Physical meaning.** Geometric proximity and orientation, not an independent bond-energy measurement.

**4. Corrosion question.** Which donor atoms approach Fe, and what footprint might the molecule occupy?

**5. Justified conclusion.** A particular contact motif is geometrically supported.

**6. Conclusion not established.** Shorter distance alone proves stronger inhibition or a covalent bond.

**7. Common mistakes.** Using an arbitrary drawn bond, comparing distances to different atom types, or neglecting tilted/rough surface references.

**8. Typical output.** Contact table, tilt definition, annotated top/side views and atom IDs.

**Method/application references:** [44](../README.md#ref-44)

---

<a id="sites"></a>
## 05 · Multiple adsorption sites and orientations

**1. What is calculated.** Relax several top/short-bridge/long-bridge/hollow starts and flat/tilted/upright orientations; cluster duplicates by final geometry.

**2. Equation or definition.**

Not a universal scalar equation: compare final distinct states, not labels assigned to starting structures.

**3. Physical meaning.** A search over a finite set of local configurations.

**4. Corrosion question.** Is the reported adsorption motif robust to reasonable starting choices?

**5. Justified conclusion.** The lowest of the tested distinct minima is identified under the selected model.

**6. Conclusion not established.** The global minimum has been proven by testing only a few starts.

**7. Common mistakes.** Counting many starts that collapse to one minimum as independent evidence; transferring fcc hollow-site terminology to bcc without geometry.

**8. Typical output.** Search matrix, final-minimum IDs, failed starts and duplicate map.

**Method/application references:** [44](../README.md#ref-44) [47](../README.md#ref-47)

---

<a id="coverage"></a>
## 06 · Coverage and lateral interactions

**1. What is calculated.** Compare specified molecule counts and surface areas, including more than one arrangement at a given density.

**2. Equation or definition.**

```math
\Gamma=\frac{N_M}{A},\qquad \theta=\frac{N_M}{N_{\mathrm{sites}}}\quad\text{only for a stated site convention}.
```

**3. Physical meaning.** Adsorbate surface density and a model-dependent site occupancy.

**4. Corrosion question.** Do cooperative hydrogen bonding or crowding alter adsorption/film motifs?

**5. Justified conclusion.** The tested periodic overlayer responds to coverage and arrangement.

**6. Conclusion not established.** A solution concentration or Langmuir isotherm follows automatically.

**7. Common mistakes.** Using inconsistent area per face, ignoring multidentate footprints or identifying current-based efficiency with coverage.

**8. Typical output.** Energy per molecule versus specified density, overlayer geometries and incremental adsorption energies.

**Method/application references:** [46](../README.md#ref-46) [51](../README.md#ref-51)

---

<a id="surface-energy"></a>
## 07 · Surface energy and surface thermodynamics

**1. What is calculated.** Compare a slab to a consistent bulk reference; include species chemical potentials for nonstoichiometric/environment-dependent surfaces.

**2. Equation or definition.**

```math
\gamma=\frac{E_{\mathrm{slab}}-N e_{\mathrm{bulk}}}{2A}\quad\text{for two equivalent stoichiometric surfaces}.
```

**3. Physical meaning.** Excess energy per surface area under a restricted model, or a reservoir-dependent surface free energy.

**4. Corrosion question.** Which facets/terminations are candidate stable surfaces under specified conditions?

**5. Justified conclusion.** Comparable candidate surfaces can be ranked thermodynamically within the reservoir window.

**6. Conclusion not established.** One gamma value predicts pitting potential, morphology or passivation kinetics.

**7. Common mistakes.** Applying the symmetric formula to inequivalent slab faces; inconsistent bulk reference; omitting atom reservoirs.

**8. Typical output.** Surface-energy convergence and, when justified, a chemical-potential phase diagram.

**Method/application references:** [22](../README.md#ref-22) [47](../README.md#ref-47)

---

<a id="vacancies"></a>
## 08 · Vacancy and defect formation

**1. What is calculated.** Compare defective and intact systems with explicit removed/added species reservoirs and charge treatment.

**2. Equation or definition.**

```math
E_{\mathrm{vac}}^{0}=E_{\mathrm{def}}-E_{\mathrm{perfect}}+\mu_X.
```

**3. Physical meaning.** Thermodynamic cost of a neutral vacancy relative to that reservoir; charged defects need additional electronic/electrostatic terms.

**4. Corrosion question.** Which defects could affect adsorption or transport in a candidate surface/film?

**5. Justified conclusion.** A specified defect is more or less favorable under the selected chemical-potential model.

**6. Conclusion not established.** This is the electrochemical dissolution barrier or the experimental defect concentration without entropy/kinetics.

**7. Common mistakes.** Using an isolated atom as an unstated aqueous ion reservoir; omitting charge corrections; testing only oxygen vacancies in an oxide.

**8. Typical output.** Defect geometries, formation-energy ledger, chemical-potential bounds and spin/charge localization.

**Method/application references:** [22](../README.md#ref-22) [52](../README.md#ref-52)

---

<a id="dos"></a>
## 09 · Total density of states

**1. What is calculated.** Sum electronic eigenstates over k-points, bands and spin with a documented broadening/integration procedure.

**2. Equation or definition.**

```math
D(E)=\sum_{j\mathbf k s}w_{\mathbf k}\delta(E-\varepsilon_{j\mathbf k s}).
```

**3. Physical meaning.** Available one-electron states per energy under the approximate electronic model.

**4. Corrosion question.** Does adsorption/oxidation change states near the Fermi level?

**5. Justified conclusion.** Spectral structure changes under a controlled energy alignment.

**6. Conclusion not established.** DOS at the Fermi level is an inhibition efficiency or a full charge-transfer rate.

**7. Common mistakes.** Inadequate k meshes, excessive smoothing, inconsistent normalization or confusing an isolated molecular gap with a metal gap.

**8. Typical output.** Aligned DOS with units, broadening, normalization, Fermi reference and spin convention.

**Method/application references:** [2](../README.md#ref-2) [4](../README.md#ref-4)

---

<a id="pdos"></a>
## 10 · Projected density of states

**1. What is calculated.** Project states onto a defined atom/orbital set and compare surface, adsorbate and combined systems.

**2. Equation or definition.**

```math
D_{\alpha}(E)=\sum_{j\mathbf k s}w_{\mathbf k}|\langle\phi_\alpha|\psi_{j\mathbf k s}\rangle|^2\delta(E-\varepsilon_{j\mathbf k s})\quad\text{for a simple orthonormal-projector picture}.
```

**3. Physical meaning.** Approximate orbital/atomic character; actual PAW/LCAO projection and overlap conventions vary.

**4. Corrosion question.** Are N p and Fe d features consistent with molecule–surface hybridization?

**5. Justified conclusion.** Broadening, shifts and mixed character support a hybridization hypothesis alongside other evidence.

**6. Conclusion not established.** Overlapping peaks alone prove a chemical bond or its strength.

**7. Common mistakes.** Treating projections as complete basis-independent populations, comparing independently zeroed energy axes, or ignoring spin.

**8. Typical output.** Fe d and adsorbate p projections with aligned references, projector definition and compatible clean/frozen-fragment controls.

**Method/application references:** [26](../README.md#ref-26) [44](../README.md#ref-44)

---

<a id="spin-dos"></a>
## 11 · Spin-resolved DOS

**1. What is calculated.** Compute/project both collinear spin channels using the same energy reference.

**2. Equation or definition.**

```math
D(E)=D_\uparrow(E)+D_\downarrow(E).
```

**3. Physical meaning.** Spin-dependent distribution of electronic states in the selected magnetic branch.

**4. Corrosion question.** Does inhibitor coordination alter surface spin asymmetry?

**5. Justified conclusion.** The chosen magnetic state’s spectrum changes locally or globally.

**6. Conclusion not established.** A plotted negative spin channel means negative DOS, or one state is the magnetic ground state without comparison.

**7. Common mistakes.** Forgetting that the down-spin curve is often reflected only for visualization; summing inconsistent projections.

**8. Typical output.** Spin-resolved DOS and final total/site moment records.

**Method/application references:** [47](../README.md#ref-47) [54](../README.md#ref-54)

---

<a id="cdd"></a>
## 12 · Charge-density difference (electron-number convention)

**1. What is calculated.** Subtract isolated fragments frozen in the combined geometry, with identical cell, grid and compatible electron counts.

**2. Equation or definition.**

```math
\Delta n(\mathbf r)=n_{SM}(\mathbf r)-n_S^{\mathrm{frz}}(\mathbf r)-n_M^{\mathrm{frz}}(\mathbf r).
```

**3. Physical meaning.** Positive values show electron accumulation relative to the chosen noninteracting fragments; negative values show depletion.

**4. Corrosion question.** Where does adsorption redistribute electrons around contacts and in the interface?

**5. Justified conclusion.** Spatial polarization/redistribution is resolved relative to the stated reference.

**6. Conclusion not established.** A colored lobe uniquely measures net electron transfer or proves protection.

**7. Common mistakes.** Confusing electron density with physical charge density (opposite sign); independently relaxing fragments; misaligned grids; unequal isovalues.

**8. Typical output.** Equal-magnitude accumulation/depletion isosurfaces plus a planar-average profile and electron-conservation check.

**Method/application references:** [18](../README.md#ref-18) [33](../README.md#ref-33)

---

<a id="bader"></a>
## 13 · Bader charge

**1. What is calculated.** Integrate the chosen electron density in zero-flux basins and subtract populations from the appropriate core/valence reference.

**2. Equation or definition.**

```math
\nabla n\cdot\hat{\mathbf n}=0\ \text{on a basin boundary},\qquad q_A/e=Z_A^{\mathrm{val}}-\int_{\Omega_A}n_{\mathrm{val}}(\mathbf r)d\mathbf r.
```

**3. Physical meaning.** Partition-specific atomic charge; the formula shown is the valence-density convention.

**4. Corrosion question.** Which basins gain or lose population upon adsorption relative to compatible references?

**5. Justified conclusion.** A consistent partition assigns a stated change in electron population.

**6. Conclusion not established.** The assigned charge is an integer oxidation state or an experimental electron-transfer current.

**7. Common mistakes.** Mixing valence density with full nuclear charges, poor grid convergence, or failing to sum basin charges.

**8. Typical output.** Atom-resolved populations/charges, total-charge sum, grid test and reference definition.

**Method/application references:** [18](../README.md#ref-18)

---

<a id="elf"></a>
## 14 · Electron localization function

**1. What is calculated.** Evaluate a spin-appropriate localization indicator based on local kinetic-energy/Pauli behavior.

**2. Equation or definition.**

```math
\mathrm{ELF}=\frac{1}{1+(D/D_h)^2}.
```

**3. Physical meaning.** A dimensionless indicator of localization relative to a homogeneous reference; define the spin/current implementation used.

**4. Corrosion question.** Are localized lone-pair or bonding-region features consistent with a proposed attachment motif?

**5. Justified conclusion.** Electron localization patterns differ in the examined regions.

**6. Conclusion not established.** ELF quantitatively measures transferred charge, adsorption energy or inhibition.

**7. Common mistakes.** Interpreting every high-ELF region as a surface bond; ignoring core/lone-pair regions and comparison isovalues.

**8. Typical output.** Plane cuts/isosurfaces at stated levels, with geometry and density context.

**Method/application references:** [19](../README.md#ref-19)

---

<a id="cohp"></a>
## 15 · COHP, projected COHP and ICOHP

**1. What is calculated.** Analyze Hamiltonian-weighted local-orbital contributions and their occupied integral in a compatible projection.

**2. Equation or definition.**

```math
\mathrm{ICOHP}_{AB}=\int^{E_F}\mathrm{COHP}_{AB}(E)\,dE.
```

**3. Physical meaning.** Energy-resolved projected bonding/antibonding contributions; negative COHP is conventionally bonding, while plots of minus-COHP reverse the sign.

**4. Corrosion question.** Which Fe–N/Fe–C contacts show occupied bonding versus antibonding character?

**5. Justified conclusion.** Within an adequately validated projection, specific interactions have distinguishable bonding contributions.

**6. Conclusion not established.** ICOHP is a unique dissociation energy or directly ranks inhibitor performance.

**7. Common mistakes.** Ignoring charge spilling/projector completeness, spin and occupancy, sign convention, basis changes or pair multiplicity.

**8. Typical output.** Pair- and spin-resolved curves, integrated values, basis/projection settings and quality metrics.

**Method/application references:** [20](../README.md#ref-20) [26](../README.md#ref-26)

---

<a id="work-function"></a>
## 16 · Work function and adsorption-induced shift

**1. What is calculated.** Extract a converged vacuum electron potential-energy plateau and subtract the Fermi energy of the same slab.

**2. Equation or definition.**

```math
\Phi=V_{\mathrm{vac}}^{(e)}-E_F,\qquad\Delta\Phi=\Phi_{\mathrm{ads}}-\Phi_{\mathrm{clean}}.
```

**3. Physical meaning.** Electron-removal energy relative to the chosen vacuum side.

**4. Corrosion question.** Does adsorption alter the surface dipole/electronic environment?

**5. Justified conclusion.** The chosen vacuum work function changes under controlled slab and reference conditions.

**6. Conclusion not established.** The sign determines experimental corrosion resistance or directly equals a corrosion-potential shift.

**7. Common mistakes.** No plateau, wrong potential component/sign, mixing faces of an asymmetric slab, or comparing incompatible electrostatic treatments.

**8. Typical output.** Planar-averaged potential, marked plateau/Fermi level, face label and convergence table.

**Method/application references:** [21](../README.md#ref-21) [38](../README.md#ref-38)

---

<a id="potential"></a>
## 17 · Electrostatic potential profile

**1. What is calculated.** Average a specified potential component in planes parallel to the surface.

**2. Equation or definition.**

```math
\overline V(z)=\frac1A\int_A V(x,y,z)\,dx\,dy.
```

**3. Physical meaning.** Spatial variation under a chosen gauge and electrostatic boundary condition.

**4. Corrosion question.** Is the interfacial field/plateau consistent with the intended slab model?

**5. Justified conclusion.** A field or potential-step feature is present in the defined model.

**6. Conclusion not established.** An arbitrary potential zero is an absolute electrode potential.

**7. Common mistakes.** Combining electrostatic voltage and electron potential-energy signs; omitting dipole/charged-cell artifacts.

**8. Typical output.** Planar and, where useful, macroscopic averages with units and gauge declaration.

**Method/application references:** [21](../README.md#ref-21) [38](../README.md#ref-38)

---

<a id="magnetism"></a>
## 18 · Total and local magnetic moments

**1. What is calculated.** Integrate spin density globally or within declared atomic/projector regions.

**2. Equation or definition.**

```math
m=\mu_B\int(n_\uparrow-n_\downarrow)\,d\mathbf r.
```

**3. Physical meaning.** Spin imbalance for a collinear description; atom-resolved values depend on partition.

**4. Corrosion question.** Do surface coordination, oxidation or adsorption change the Fe magnetic state?

**5. Justified conclusion.** Magnetic solutions and their energies can be compared consistently.

**6. Conclusion not established.** A single converged initial magnetization proves the relevant state or magnetic changes directly measure corrosion.

**7. Common mistakes.** Failing to test alternatives, confusing total and local moments, applying metallic Fe settings indiscriminately to oxides.

**8. Typical output.** Initial/final spin patterns, state energies, layer moments and spin-density views.

**Method/application references:** [47](../README.md#ref-47) [40](../README.md#ref-40) [14](../README.md#ref-14)

---

<a id="d-band"></a>
## 19 · d-band center

**1. What is calculated.** Take a first moment of a named d-projected DOS over a specified energy interval, relative to a stated energy reference.

**2. Equation or definition.**

```math
\varepsilon_d=\frac{\int_{E_1}^{E_2}(E-E_F)D_d(E)\,dE}{\int_{E_1}^{E_2}D_d(E)\,dE}.
```

**3. Physical meaning.** A compressed spectral descriptor, dependent on projector, window, spin and occupied-only/all-state convention.

**4. Corrosion question.** Can a consistent family of surface sites be compared using a compact electronic feature?

**5. Justified conclusion.** The selected spectral first moment shifts within the defined protocol.

**6. Conclusion not established.** Its shift alone predicts adsorption, passivity or inhibitor efficiency across unrelated metals and oxides.

**7. Common mistakes.** Comparing different windows/projectors or ignoring spin and covalency; treating correlation as causation.

**8. Typical output.** DOS plus integration window, normalization, spin treatment and descriptor sensitivity.

**Method/application references:** [33](../README.md#ref-33) [47](../README.md#ref-47)

---

<a id="frequencies"></a>
## 20 · Vibrational frequencies and stationary-point tests

**1. What is calculated.** Diagonalize the mass-weighted Hessian in the stated full or partial coordinate subspace.

**2. Equation or definition.**

```math
\sum_{J\beta}\frac{H_{I\alpha,J\beta}}{\sqrt{M_I M_J}}e_{J\beta}=\omega^2 e_{I\alpha}.
```

**3. Physical meaning.** Local curvature and normal modes around the chosen structure; negative eigenvalues correspond to unstable directions.

**4. Corrosion question.** Is an adsorption structure locally stable, or is a candidate TS consistent with the intended reaction?

**5. Justified conclusion.** The examined subspace has the reported stable/unstable modes.

**6. Conclusion not established.** An adsorbate-only Hessian proves full-slab stability; every tiny negative mode is physically meaningful.

**7. Common mistakes.** Poor force precision, unsuitable displacements, fixed atoms not reported or ignoring mode character.

**8. Typical output.** Frequencies, displacement amplitudes, active atom list and mode animations/assignments.

**Method/application references:** [17](../README.md#ref-17)

---

<a id="zpe"></a>
## 21 · Zero-point energy

**1. What is calculated.** Sum the ground-state harmonic vibrational contributions for consistently defined stable modes.

**2. Equation or definition.**

```math
E_{\mathrm{ZPE}}=\frac12\sum_i\hbar\omega_i.
```

**3. Physical meaning.** Nuclear quantum ground-state correction within the harmonic approximation.

**4. Corrosion question.** Does a vibrational correction change an adsorption/reaction energy ordering?

**5. Justified conclusion.** The harmonic correction changes the electronic difference by the computed amount.

**6. Conclusion not established.** ZPE alone supplies a finite-temperature aqueous adsorption free energy.

**7. Common mistakes.** Double counting ZPE already included in a vibrational free energy; treating an imaginary TS mode as a stable oscillator.

**8. Typical output.** Mode list and state-by-state ZPE ledger with consistent mode counting.

**Definition reference:** harmonic-oscillator statistical mechanics, explained in [Chapter 16](16_reaction_pathways_neb.md); see the [ASE thermochemistry documentation](https://ase-lib.org/ase/thermochemistry/thermochemistry.html) for a practical implementation.

---

<a id="entropy"></a>
## 22 · Entropy and thermal contributions

**1. What is calculated.** Use an appropriate partition-function model for each phase; harmonic vibrations for selected modes and suitable gas/solution treatments.

**2. Equation or definition.**

```math
F_{\mathrm{vib}}(T)=\sum_i\left[\frac{\hbar\omega_i}{2}+k_BT\ln(1-e^{-\hbar\omega_i/k_BT})\right],\qquad S_{\mathrm{vib}}=-\left(\frac{\partial F_{\mathrm{vib}}}{\partial T}\right)_V.
```

**3. Physical meaning.** Temperature-dependent state counting, with substantial model sensitivity for low-frequency adsorbate motion.

**4. Corrosion question.** Can entropic costs oppose apparently favorable electronic binding?

**5. Justified conclusion.** The stated statistical-mechanical model produces the reported thermal corrections.

**6. Conclusion not established.** A gas-phase ideal-rotor/translator entropy applies unchanged to an adsorbate or dissolved inhibitor.

**7. Common mistakes.** Mixing standard states, overinterpreting very soft harmonic modes, ignoring hindered motion and configurational entropy.

**8. Typical output.** Correction table by mode/phase and sensitivity to low-mode treatment.

**Method/application references:** [38](../README.md#ref-38) [34](../README.md#ref-34)

---

<a id="free-energy"></a>
## 23 · Adsorption/reaction free energy

**1. What is calculated.** Assemble balanced state and reservoir free energies with consistent thermal, solvation and standard-state conventions.

**2. Equation or definition.**

```math
\Delta G=\sum_i\nu_iG_i;\qquad G_i\simeq E_i^{\mathrm{DFT}}+E_i^{\mathrm{ZPE}}+\Delta H_{i,T}-TS_i+\Delta G_{i,\mathrm{solv}}+\Delta G_{i,\mathrm{std}}.
```

**3. Physical meaning.** A thermodynamic state preference in the named ensemble; the displayed decomposition is approximate.

**4. Corrosion question.** Which adsorption/chemical-state alternatives are thermodynamically plausible under specified conditions?

**5. Justified conclusion.** An ordering follows within the documented reservoir/correction model.

**6. Conclusion not established.** Thermodynamic favorability determines rate, morphology or protection by itself.

**7. Common mistakes.** Unbalanced proton/electron/ion counts, inconsistent references, duplicated corrections or unsupported uncertainty precision.

**8. Typical output.** Balanced reaction ledger and free-energy diagram labeled with temperature, standard states, pH and potential reference.

**Method/application references:** [22](../README.md#ref-22) [23](../README.md#ref-23) [24](../README.md#ref-24)

---

<a id="neb"></a>
## 24 · NEB and activation barriers

**1. What is calculated.** Optimize a path between verified endpoints; refine the saddle-point candidate and examine its unstable mode.

**2. Equation or definition.**

```math
E_a=E_{\mathrm{TS}}-E_{\mathrm{IS}},\qquad\Delta G^\ddagger=G_{\mathrm{TS}}-G_{\mathrm{IS}}.
```

**3. Physical meaning.** Path-specific activation cost, not simply the reaction energy.

**4. Corrosion question.** Does adsorption change a candidate elementary event, such as bond cleavage or site migration?

**5. Justified conclusion.** The tested path has an identified barrier within the model and refinement.

**6. Conclusion not established.** It is the only path, the solution activation free energy or the overall corrosion rate.

**7. Common mistakes.** Unoptimized endpoints, wrong atom mapping, too few images, insufficient image-force convergence, no potential/solvent treatment.

**8. Typical output.** Images, force convergence, refined TS, mode verification and energy/free-energy profile with reference states.

**Method/application references:** [17](../README.md#ref-17) [25](../README.md#ref-25)

---

<a id="aimd"></a>
## 25 · Ab initio molecular dynamics

**1. What is calculated.** Propagate nuclei on a DFT energy surface under a defined ensemble, timestep and electronic precision; analyze equilibrated segments.

**2. Equation or definition.**

```math
M_I\ddot{\mathbf R}_I=-\nabla_I E_{\mathrm{BO}}\quad\text{for the unthermostatted classical-nuclear equations}.
```

**3. Physical meaning.** A finite-time trajectory, typically with classical nuclei, generated by the chosen approximate interactions.

**4. Corrosion question.** Which hydration/coordination motifs persist or interconvert on accessible timescales?

**5. Justified conclusion.** Specified structures or events occur during the sampled trajectory.

**6. Conclusion not established.** Absence of dissolution/desorption during a short run proves long-term stability or inhibition.

**7. Common mistakes.** Short unthermalized runs, single initial solvent arrangement, timestep/SCF drift, no independent blocks or event statistics.

**8. Typical output.** Trajectory provenance, temperature/energy diagnostics, independent sampling windows and structural statistics.

**Method/application references:** [53](../README.md#ref-53) [35](../README.md#ref-35)

---

<a id="rdf"></a>
## 26 · Radial distribution and interfacial coordination

**1. What is calculated.** Count pair separations with a normalization appropriate to the geometry; use layer-resolved/directional alternatives for inhomogeneous interfaces.

**2. Equation or definition.**

```math
g_{AB}(r)=\frac{1}{4\pi r^2\rho_B N_A}\left\langle\sum_{i\in A}\sum_{j\in B,j\ne i}\delta(r-r_{ij})\right\rangle\quad\text{for a homogeneous bulk reference}.
```

**3. Physical meaning.** Pair-structure statistics relative to a stated reference density and accessible volume.

**4. Corrosion question.** Does inhibitor adsorption alter local hydration or coordination?

**5. Justified conclusion.** The sampled pair distribution/coordination differs with uncertainty under the chosen normalization.

**6. Conclusion not established.** A bulk-normalized RDF next to a slab automatically gives unbiased interfacial coordination or a reaction mechanism.

**7. Common mistakes.** Using full cell volume including vacuum as liquid density, ignoring excluded volumes/layers, correlating frames as independent.

**8. Typical output.** Layer-resolved distributions, coordination integrals, density definition, uncertainty and sampling information.

**Method/application references:** [48](../README.md#ref-48) [53](../README.md#ref-53)

---
