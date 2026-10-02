# Suggested graduate reading and discussion plan

[Course home](README.md) · [Chapters](docs/README.md)

This is an original teaching sequence, not a claim of accreditation or a schedule attached to an institution. Sessions may be combined for self-study. No paid software or calculation is required to work through the conceptual assignments.

| Session | Readings | Assignment | Evidence of understanding |
|---|---|---|---|
| 1 · The corrosion question | README 1–3; docs 07 and 09 | Write a one-paragraph model card for an inhibitor claim | Distinguish atomistic mechanism from macroscopic efficiency |
| 2 · DFT foundations | docs 01–05 | Explain each term in the energy and KS equations | Do not confuse eigenvalue sums and total energy |
| 3 · Molecule versus metal | docs 02, 06, 11 | Compare molecular IP/EA and metallic work function | State species, reference and descriptor convention |
| 4 · Surfaces and convergence | docs 03, 06, 07, 22 | Design observable-specific convergence tests | Separate numerical refinement, model changes and sampling |
| 5 · Adsorption thermodynamics | docs 08, 13, 14 | Build a balanced adsorption/displacement cycle | State surface/molecule/solvent/ion reservoirs |
| 6 · Electronic evidence | docs 10–12, 24 | Critique a hypothetical PDOS/CDD/Bader claim | State which independent evidence is missing |
| 7 · Electrochemical ensembles | docs 15–16 | Derive the SHE/RHE relation for a matched-pair reduction | Avoid sign mistakes and pH double counting |
| 8 · Films and environment | docs 17, 25 | Explain why one Fe oxide slab is not all passivation | Account for defects, transport and surface preparation |
| 9 · Case-study design | case-study files | Complete model card and choose essential analyses | No fabricated results; clear decision gates |
| 10 · Scientific communication | docs 19–21; CHECKLIST | Write a bounded abstract and methods record | Separate observation, mechanism and performance |

## Discussion questions with answer sketches
**Why can two fully converged calculations disagree?** They can use different physical models, geometries, magnetic/electronic branches, surface states or reference conventions. Numerical convergence is not identity of Hamiltonians or states.

**Why can CDD integrate to zero while Bader assigns charge transfer?** Electron-conserving redistribution has zero global integral. A partition can still assign gain to the adsorbate and equal loss to the remainder.

**Why is an imidazolium calculation not directly comparable with neutral imidazole?** Composition/charge and proton/electron reservoirs differ. Balance the reaction and solution/electrode references first.

**Can lower vacancy energy prove faster corrosion?** Not alone. Site availability, transition states, ion hydration, potential and transport must be addressed.

**Can a normal-termination message validate a transition state?** No. Check forces, electronic state, mode character and relevant pathway connectivity.

**Does larger work function imply greater corrosion resistance?** Not generally. Work function describes vacuum electron removal; corrosion performance depends on coupled interfacial reactions and environment.

**Why are Fe(100) papers included in an Fe(110) tutorial?** They provide useful contrasting mechanisms and controls. Their facet-specific findings must not become numerical claims for the proposed case.

## Capstone deliverable
Produce a 3–5 page study proposal (length suggestion only): question, assumptions, workflow, essential analyses, balanced reference equations, uncertainty strategy, experimental connection and explicitly untested claims. Attach the blank worksheets as the planned data schema. Do not submit invented simulation results.
