# Mathematical and reference conventions

[Course home](README.md)

| Topic | Convention in this repository | Consequence |
|---|---|---|
| Fundamental electronic equations | Atomic units where stated; electron-number density `n` | Include ion–ion energy in Born–Oppenheimer total energy |
| Orbitals | `j` band, `k` wavevector, `s` spin | Avoid using `n` for both density and band index in the same expression |
| Density | Positive electron-number density; physical electron charge density is `−e n` | Positive CDD means electron accumulation, not positive physical charge |
| Adsorption | Combined minus relaxed separated references | Negative electronic adsorption energy is exothermic relative to those references |
| Deformation | Frozen isolated fragments minus relaxed isolated fragments | Adsorption = interaction + deformation by bookkeeping |
| Hardness | Curvature `eta_c=I−A`; `S_c=1/eta_c`; `omega_c=mu²/(2eta_c)` | Convert half-gap conventions by explicit equations; do not mix prefactors |
| Surface energy | `(Eslab−N ebulk)/(2A)` for two equivalent faces | Not either individual gamma of an asymmetric slab |
| Work function | Vacuum **electron potential energy** minus Fermi energy | Do not mix voltage and electron-energy signs |
| Electrode potential | SHE explicitly named; e is positive elementary charge | Reduction consuming matched pairs gains `+neU_SHE` in deltaG |
| pH reference | Pair chemical potential includes `−kBT ln10 pH` | Matched-pair deltaG gains positive pH term vs SHE; absorb it vs RHE |
| Grand ensemble | `Omega=F−mu_e N_e` at fixed electron chemical potential | Include nuclear reservoirs separately where relevant |
| COHP | Conventional negative bonding; plotting minus-COHP reverses sign | Report the plotting convention and projection quality |
| Vibrations | Angular frequencies; harmonic stable modes | ZPE already included in harmonic Fvib; unstable TS mode handled separately |
| RDF | Bulk formula only for homogeneous reference | Interface/vacuum requires corrected normalization or layer-resolved measures |

Equations use GitHub fenced `math` blocks. Local tests check fences, braces and selected algebraic identities. They are **not** a mathematical proof of every approximation, a browser-render test or a substitute for scientific review.
