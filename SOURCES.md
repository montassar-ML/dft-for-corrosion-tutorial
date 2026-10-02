# Literature framework and source-access record

[Main bibliography](README.md#references) · [BibTeX](references.bib) · [Per-reference verification ledger](reference-verification.csv)

## Scope and selection
This is a curated educational reading set, not a systematic review or exhaustive ranking. Search themes included DFT/corrosion reviews; inhibitor descriptor limitations; imidazole/Fe surfaces; iron/water and oxide interfaces; adsorption, charge, bonding and reaction-path methods; and electrochemical ensemble/solvation theory. Official project documentation supports current software notes.

The set contains **55 unique DOI-bearing references** spanning foundations, methods, reviews, software and representative applications. Prefer primary methodological papers for definitions and primary application papers for surface-specific conclusions. Reviews establish context and point to competing models; they are not a license to make stronger claims than their underlying evidence.

## Reading order and what each review contributes
| Reading | How used in this course | Caution |
|---|---|---|
| Kokalj (2021), molecular modeling/pitfalls [33](README.md#ref-33) | Organizes the distinction between isolated descriptors, molecule–surface interaction and mechanism | Do not turn its critical discussion into a universal alternative ranking |
| Chen et al. (2025), applications review [34](README.md#ref-34) | Contemporary map of corrosion/prevention applications and analysis choices | Broad applicability does not make every descriptor causal |
| Li et al. (2024), computational experiments review [35](README.md#ref-35) | Locates DFT alongside dynamics and larger-scale methods | We do not adopt broad predictive statements as guarantees for one static slab |
| Maurice and Marcus (2018) [36](README.md#ref-36) | Connects atomic/nanometric structures with corrosion/passivation context | Surface-preparation and environmental differences remain central |
| Taylor and Ke (2021) [37](README.md#ref-37) | Connects surface reactions, environment, chloride/hydrogen and alloy questions | A specific electrochemical model is not every material/environment |
| Schwarz and Sundararaman (2020) [38](README.md#ref-38) | Separates first-principles electrochemical interface formulations | Choice of ensemble, charge compensation and solvent is not interchangeable |
| Todorova et al. (2026) [39](README.md#ref-39) | Updates the conceptual landscape of electrochemical interface modeling | Date of DOI registration is not necessarily publication year |
| Parkinson (2016) [40](README.md#ref-40) | Distinguishes iron-oxide phases, surfaces, defects and reconstructions | Vacuum/single-crystal findings are not automatically aqueous passive-film structures |
| Obot et al. (2015) [41](README.md#ref-41) | Background on molecular inhibitor-modeling practice | Read with the critical descriptor literature, not as proof of universality |
| Geerlings et al. (2003) [12](README.md#ref-12) | Conceptual-DFT terminology and response framework | Publish prefactor conventions and finite-difference assumptions |

## Representative applications and their transfer limits
- **Fe(110):** Camacho-Mendoza et al. provide an imidazole-derivative molecular/surface precedent. The present case is a new teaching design, not a reproduced set of their calculations. [44](README.md#ref-44)
- **Fe(100):** Kokalj and Zhao et al. motivate film, hydrogen-bond and dissociation controls. Their facet-specific numbers are not supplied as Fe(110) results. [45](README.md#ref-45) [46](README.md#ref-46)
- **Clean iron:** Spencer et al. motivate consistent slab/electronic surface checks. [47](README.md#ref-47)
- **Water/iron:** the 2025 iron–water study motivates facet/oxidation/environment sensitivity. [48](README.md#ref-48)
- **Oxidized copper/azoles:** these studies illustrate that substrate and oxidation state alter the adsorption question; they are not iron benchmarks. [49](README.md#ref-49) [50](README.md#ref-50)
- **Cu/Zr descriptors:** limited one-parameter correlations motivate caution, without establishing the behavior of iron. [43](README.md#ref-43)
- **Magnetite(001):** subsurface cation vacancies illustrate why an oxide model should not consider only oxygen vacancies by default. [52](README.md#ref-52)
- **Efficiency versus coverage:** Walczak et al. motivate keeping measured rate reductions separate from assumed adsorption-site occupancy. [51](README.md#ref-51)

## What “verified” means here
Each DOI/title pair was cross-checked using an accessible publisher, author/project, bibliographic record or publisher reference-list record. The CSV provides the evidence URL and an access description. This is **metadata verification**, not a certification that every study is correct or that its complete text and supporting information were read.

Some originals were blocked or unavailable. For example, the original NEB, ELF and HSE pages were not all accessible directly; alternative bibliographic/author evidence is recorded rather than claiming full-text access. Not all optional volume/page fields were available; those fields are omitted instead of guessed. Some long author lists use the legitimate BibTeX `and others` abbreviation.

Bibliographic metadata can use online publication dates differing from issue years. The Reuter–Scheffler surface-thermodynamics entry notes that distinction in the ledger; consult the original article and its correction when using its specific numerical results. The 2026 electrochemical review has a DOI containing 2025 but was published in 2026.

No all-sites HTTP link-check guarantee is claimed. Publisher redirects and access controls can vary by network, and metadata availability is not equivalent to licensed full-text access. No papers or publisher figures are redistributed.

## Explicit layers of content
1. **Literature-derived statements:** narrowly attributed methods, review scope or case-specific observations with citations.
2. **Standard theoretical definitions:** mathematical definitions and textbook-level quantum/statistical mechanics, with conventions stated.
3. **Original synthesis:** the decision gates, analysis cards, comparison tables, exercises and worksheets.
4. **Proposed work:** the Fe(110) case and figure designs, with no reported simulation results.

## Official documentation
The [software chapter](docs/23_software_and_analysis_tools.md) links the official VASP, Quantum ESPRESSO/Environ, CP2K, GPAW, CASTEP and ABINIT documentation plus analysis-tool sources. Software access and feature claims were checked as available on 1 October 2026; no unsupported benchmark ranking is made.

For equation rendering, GitHub documents [fenced mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). This repository validates the local markup, not every user's browser rendering.
