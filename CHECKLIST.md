# DFT corrosion study checklist

[Course home](README.md) · [Case-study model card](case-study/worksheets/model-card.md)

## Question and model
- [ ] State the physical question and the stronger performance claim not yet being made.
- [ ] Define composition, facet, termination, defects, oxide/hydroxylation and relevant alloying.
- [ ] State charge, protonation/tautomer, electron count and magnetic model.
- [ ] Identify vacuum/solvent/electrolyte and fixed-charge or fixed-potential ensemble.
- [ ] List omitted physics and the consequences for comparison to experiment.

## Numerical and sampling controls
- [ ] Test basis/cutoffs/density grids, k-points and smearing against the actual observable.
- [ ] Converge slab thickness, vacuum and electrostatic treatment.
- [ ] Declare lateral area, molecule count, coverage and fixed-atom policy.
- [ ] Verify both SCF and force convergence; inspect final structures.
- [ ] Examine alternative magnetic/electronic states where appropriate.
- [ ] Explore adsorption orientations/sites and record failed/duplicate minima.
- [ ] Treat XC/U/dispersion as model sensitivity, not merely convergence.
- [ ] Report uncertainty and near-degeneracies rather than unsupported rankings.

## Analysis
- [ ] State adsorption-energy sign, units, chemical state and reference calculations.
- [ ] Separate deformation and interaction definitions if used.
- [ ] Freeze fragment geometry and align cells/grids for CDD.
- [ ] State electron-density versus physical-charge sign convention.
- [ ] Check Bader density/core convention and charge sums.
- [ ] Specify DOS reference, spin, projectors, normalization and broadening.
- [ ] Verify a work-function plateau on the specified surface face.
- [ ] Check COHP/ICOHP sign and projection quality before bonding claims.
- [ ] State Hessian subspace; validate minima/TS mode character.
- [ ] Avoid double-counting ZPE and thermal/solvation corrections.
- [ ] Balance proton/electron/ion reservoirs and specify SHE/RHE or other reference.
- [ ] Verify NEB endpoints/mapping/path convergence when making kinetic claims.
- [ ] State AIMD sampling/time limitations and interfacial RDF normalization.

## Interpretation and publication
- [ ] Do not equate HOMO/LUMO, adsorption energy, Bader charge or work function with inhibition efficiency.
- [ ] Separate experimental current-derived efficiency from surface coverage.
- [ ] Distinguish vacuum Fe(110) from electrolyte-covered steel or passive films.
- [ ] Keep Fe(100) literature findings separate from Fe(110) case-study results.
- [ ] Connect to experiment only at the level the calculated observable supports.
- [ ] Deposit permission-cleared structures, metadata and source/derived-data relationships.
- [ ] Cite original methods and the actual papers underlying specific claims.
