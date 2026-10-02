# 09 · Inhibitors: molecular descriptors are hypotheses

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Explain why selecting the molecule with the smallest gap is not a defensible general inhibitor-screening protocol.

An inhibitor can change corrosion through adsorption, site blocking, complex formation, surface-film organization, changes in cathodic chemistry or interactions with an existing passive layer. A single isolated-molecule descriptor contains no explicit information about many of these processes. The computational question should specify which proposed mechanism is under examination. [33](../README.md#ref-33)

## What molecular descriptors can contribute
A calculated electrostatic potential or Fukui function can suggest atoms to test as coordination centers. A conformer search can reveal whether the proposed donor group is exposed. Protonation calculations can suggest which molecular species should enter an adsorption model. These are useful *model-building* contributions rather than stand-alone predictions of performance.

A statistical correlation between an orbital descriptor and measured efficiency may hold in a restricted dataset. It requires uncertainty estimates, independent validation and comparable measurement conditions. Small datasets, chemically redundant descriptors and many tried regressions can produce apparent relationships with little predictive value. Material-specific imidazole results on Cu/Zr illustrate why a correlation must not be promoted to a substrate-independent rule. [43](../README.md#ref-43)

## A mechanism-based screening chain

| Gate | Evidence needed | Reason to stop or revise |
|---|---|---|
| Chemical identity | Tautomer, protonation, purity, solubility | Wrong dominant solution species |
| Interface access | Delivery and competition with water/ions | Favorable dry binding but inaccessible sites |
| Bound state | Multiple geometries and dissociation alternatives | Only one guessed minimum tested |
| Layer formation | Coverage, lateral interactions and connectivity | Strong single-molecule binding but no coherent layer |
| Electrochemical effect | Which anodic/cathodic steps change? | Binding evidence does not establish rate suppression |
| Experiment | Same material, electrolyte and conditions | Model/measurement refer to different interfaces |

These gates are a proposed teaching framework. They are not a published universal scoring formula.

## Molecular integrity is an assumption to test
An intact adsorbate may not be the species that forms a film. Imidazole/Fe(100) studies consider dehydrogenated surface species and dissociation pathways. Such results motivate testing chemical transformations; they do not establish a Fe(110) structure or barrier without new calculations. [45](../README.md#ref-45) [46](../README.md#ref-46)

Similarly, inhibitor bonding on an oxidized surface can differ from bonding on bare metal. Oxidized-copper azole studies demonstrate the relevance of explicitly defined surface sites, but are not numerical predictions for iron oxides. [49](../README.md#ref-49)

## Avoid classification by one energy threshold
“Physisorption” and “chemisorption” are limiting descriptions of interaction mechanisms, not labels reliably assigned by a universal adsorption-energy cutoff. Orbital mixing, polarization, dispersion and structural change can coexist. Use geometry, density and bonding analyses together, with a defined energy reference.

**Exercise:** The flat configuration has the strongest vacuum binding. State three tests before calling it the best inhibitor. Suggested answers: assess water displacement/protonation; inspect feasible layer coverage and adsorption/desorption kinetics; determine whether the relevant anodic or cathodic reaction is suppressed under matching electrochemical conditions.
