# 17 · Iron oxides and passive films

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Use crystalline oxide models to study selected mechanisms without presenting them as a complete passive film.

| Model | Why it is useful | Essential caution |
|---|---|---|
| Metallic bcc Fe | Reference for exposed metallic regions | Does not contain oxide chemistry |
| Ideal FeO | Simple Fe(II)-oxide limit | Real wüstite is often nonstoichiometric Fe1−xO |
| Fe3O4 | Mixed-valence inverse-spinel model | Cation arrangement, charge localization and magnetism matter |
| α-Fe2O3 | Hematite Fe(III)-oxide model | Distinguish it from γ-Fe2O3 and hydroxylated phases |
| Multicomponent/disordered film | Closer to many real passive layers | More structural possibilities and sampling demands |

Iron-oxide surface chemistry depends on crystal phase, termination, reconstruction, defects and environment. Parkinson's review is a useful map to these distinctions, not evidence that every oxide surface behaves identically. [40](../README.md#ref-40)

## From thermodynamic stability to protection
A stable oxide is not necessarily a protective film. Protection also depends on continuity, adhesion, ionic/electronic transport, defects, dissolution and environmental stability. Film breakdown is a coupled process; one favorable chloride adsorption geometry does not determine a macroscopic pitting potential. Reviews of corrosion at atomic and nanometric scales connect these interfacial structures to experimental observations and their limitations. [36](../README.md#ref-36)

## A targeted DFT study
Define one question: for example, whether chloride prefers a hydroxylated site near a chosen defect relative to a defect-free reference under a specified reservoir model. Compare relevant surface phases and charge states, converge the slab, and inspect relaxation, magnetism and charge localization. If a transport or dissolution mechanism is claimed, calculate or otherwise justify the relevant barriers and solution products.

## Do not restrict the defect menu prematurely
A missing oxygen is an easy model to build, but cation rearrangements can be decisive. The magnetite(001) subsurface-cation-vacancy structure is a specific experimental/DFT example of that point. It is not proof that the same defect occurs in every aqueous passive film. [52](../README.md#ref-52)

## DFT+U and magnetic configurations
Iron oxides often admit metastable occupation and spin solutions. Report initial and final patterns, atom-resolved moment definitions, correlated subspaces and U values. Numerical convergence of one state does not establish the global lowest-energy state. A phase comparison can change if reference states are inconsistent. [14](../README.md#ref-14)

## Boundaries of the teaching model
Stainless-steel passivity can involve alloying elements and composition gradients; pure crystalline Fe oxides cannot stand in for a Cr-containing, hydroxylated, amorphous multilayer without explanation. Real film evolution also spans lengths and times not accessible to one static slab. DFT results should constrain a larger mechanistic model rather than silently replace it.

**Exercise:** A defect binds chloride strongly. List the next questions: Is that defect populated at the relevant potential/pH? Is chloride available at that site? Does it change transport or dissolution barriers? Does water/protonation alter binding? Does the resulting structure persist or reconstruct?
