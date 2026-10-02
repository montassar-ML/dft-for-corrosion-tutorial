# 23 · Electronic-structure and analysis software

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Select software by the physical model and observable, and distinguish the solver from post-processing tools. Capability notes were checked against official project documentation on **1 October 2026**; they are not speed or accuracy rankings. Feature combinations and licensing must be checked for the installed release.

## Electronic-structure engines
| Engine | Representation / core treatment | Access model | Corrosion teaching use | Paths and dynamics | Solvent/electrode route | Analysis ecosystem |
|---|---|---|---|---|---|---|
| VASP | Plane waves, PAW | Proprietary licensed | Magnetic Fe slabs, oxide defects, adsorption | NEB; AIMD | VASPsol-family extension; check implementation/release | py4vasp, VASPKIT, ASE/pymatgen, compatible Bader/LOBSTER workflows |
| Quantum ESPRESSO | Plane waves; NC/US/PAW datasets | Open-source GPL | Slabs, bulk, response and adsorption | PWneb; PW/CP dynamics | Environ extension; not a universal automatic constant-potential mode | Native post-processing, ASE/pymatgen and compatible density tools |
| CP2K | Gaussian orbital + grid/plane-wave density (GPW/GAPW); commonly GTH | Open-source GPL | Large water/interface cells and adsorption | BAND/NEB; AIMD | Documented SCCS continuum; other choices version dependent | Native cube/PDOS outputs, ASE, compatible real-space analysis |
| GPAW | PAW; grid, plane-wave or LCAO modes | Open-source GPL | Python-based surface and electrochemical workflows | ASE-coupled NEB and MD | Solvation/SJM for specified constant-potential models | ASE, native density/projection utilities |
| CASTEP | Plane waves and pseudopotentials | Licensed; eligible academic routes and commercial distribution | Solids, surfaces and vibrational studies | Documented NEB/LST/QST and MD | Check exact release/extension; no universal option asserted here | Native analysis, compatible structure/density exporters |
| ABINIT | Plane waves; pseudopotentials/PAW | Open-source GPL | Bulk/defect/response and surface studies | `imgmov` NEB/string; MD | Check exact implementation; no default electrolyte treatment asserted | AbiPy, native post-processing, density exporters |

**NC/US:** norm-conserving/ultrasoft. Having a feature in a package does not mean every XC/spin/boundary-condition combination supports it. A free academic license is not the same as an unrestricted open-source license.

## Official capability references
- [VASP project](https://www.vasp.at/), [NEB documentation](https://www.vasp.at/wiki/index.php/Nudged_elastic_bands), and the original periodic-solvation paper. [24](../README.md#ref-24)
- [Quantum ESPRESSO project](https://www.quantum-espresso.org/), [package documentation](https://www.quantum-espresso.org/documentation/), [PWneb guide](https://www.quantum-espresso.org/Doc/neb_user_guide/node4.html), [Environ documentation](https://environ.readthedocs.io/en/latest/).
- [CP2K features](https://www.cp2k.org/features), [SCCS input reference](https://manual.cp2k.org/cp2k-2026_2-branch/CP2K_INPUT/FORCE_EVAL/DFT/SCCS.html). [53](../README.md#ref-53)
- [GPAW project](https://gpaw.readthedocs.io/), [SJM documentation](https://gpaw.readthedocs.io/documentation/sjm/sjm.html). [54](../README.md#ref-54)
- [CASTEP capabilities](https://www.castep.org/features/capabilities), [access/licensing](https://www.castep.org/get_castep).
- [ABINIT presentation](https://www.abinit.org/presentation.html), [license](https://docs.abinit.org/about/license/), [relaxation/NEB variables](https://docs.abinit.org/variables/rlx/).

## Analysis and visualization tools
| Tool | Actual role | Useful corrosion output | What it does not establish |
|---|---|---|---|
| VESTA | Structure and volumetric visualization | Slab contacts, CDD/ELF isosurfaces | Bond strength from a drawn bond |
| OVITO | Atomistic trajectory/structure visualization and analysis | Reconstruction, coordination, trajectory inspection | Electronic bonding from positions alone |
| ASE | Atomistic data structures, calculators and workflows | Build/test surfaces; organize paths | Correct surface chemistry automatically |
| pymatgen | Materials structures, parsing and analysis | Slab provenance, crystallography, electronic-output analysis | Experimental surface populations |
| VASPKIT | VASP-oriented pre/post-processing | DOS, potentials, geometries | Correctness of the original DFT run |
| py4vasp | VASP's Python analysis interface | Structured VASP output exploration | Universal parsing of every historic output |
| p4vasp | Legacy VASP analysis/visualization option | Older workflows where compatibility is established | Current compatibility by assumption |
| Bader tools | Numerical zero-flux density partitioning | Atomic/basin electron populations | Oxidation states or corrosion currents |
| LOBSTER | Local-orbital projection of compatible wavefunctions | COHP/ICOHP and bonding analysis | Basis-independent dissociation energies |
| Multiwfn | Wavefunction/density analyses for supported formats | MEP, molecular descriptors and selected real-space analyses | Automatic support for every periodic projection |
| Critic2 | Real-space critical points, topology and density analysis | Periodic density partitioning/topology | Unique experimental charge transfer |

Method references: VESTA [27](../README.md#ref-27), ASE [28](../README.md#ref-28), pymatgen [29](../README.md#ref-29), VASPKIT [30](../README.md#ref-30), Bader [18](../README.md#ref-18), LOBSTER [26](../README.md#ref-26), Multiwfn [32](../README.md#ref-32), Critic2 [31](../README.md#ref-31). Official additional resources: [OVITO](https://www.ovito.org/), [py4vasp](https://www.vasp.at/py4vasp/latest/), [p4vasp](http://www.p4vasp.at/), [Bader](https://theory.cm.utexas.edu/henkelman/code/bader/), [LOBSTER](http://www.cohp.de/), [Critic2](https://aoterodelaroza.github.io/critic2/).

## Interoperability checklist
Before choosing a post-processor, check whether the export contains the density or potential you actually need, whether it is valence/all-electron/reconstructed, its units and grid, spin channels, and whether the energy reference is preserved. Distinguish a total-density cube from an orbital-density cube. Validate at least one small reference and charge/electron-count sum rule.

**Exercise:** Why is changing the visualization isovalue not an electronic convergence test? The density is unchanged; only the displayed level set changes. The visual impression can change strongly without new physical evidence.
