# 07 · From a clean surface to a corrosion interface

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
State what a simplified interface leaves out before assigning a corrosion mechanism to it.

Corrosion is a coupled process. Metal atoms can oxidize and dissolve while reduction consumes electrons elsewhere on the same electrically connected material. Water, hydroxyl groups, oxygen, aggressive ions and inhibitors may occupy the interface simultaneously. Atomic-scale corrosion reviews motivate models of this evolving interface rather than treating corrosion as one adsorption event. [36](../README.md#ref-36) [37](../README.md#ref-37)

## Build a hierarchy of explicit questions

| Level | Model | Question answered | Important omission |
|---|---|---|---|
| A | Clean neutral Fe + intact molecule in vacuum | Is this binding geometry locally favorable? | Water, ions, potential, film formation |
| B | Hydroxylated or oxidized termination | Does surface chemistry alter coordination? | Full passive-film disorder and transport |
| C | Water-covered surface + molecule | Can the molecule compete with selected water structures? | Entropy and extended sampling |
| D | Explicit water + an ion + chosen charge | What local solvent/ion arrangements are possible? | Reservoir and potential calibration |
| E | Potential-controlled solvated interface | How does a reaction free energy depend on electron chemical potential? | Time scales, transport and finite-size limits |

Moving down the table is not automatically “better”: a complicated unsampled model may be less informative than a carefully bounded simple one. Modern interface methodologies explicitly trade detail, sampling and control of thermodynamic variables. [38](../README.md#ref-38) [39](../README.md#ref-39)

## Define chemistry before geometry
Specify substrate/alloy composition, phase, facet, termination, temperature, pH range, dissolved species and intended electrode-potential scale. Identify which quantities are imposed, equilibrated with reservoirs or excluded. Decide whether the surface is bare, hydroxylated, oxide-covered or reconstructed under the scenario.

For a neutral imidazole baseline, describe it as an intentional teaching state. Do not call it the dominant acidic-solution form without a speciation calculation or appropriate experimental evidence.

## Balance atoms and electrons
A molecule adsorbing on a dry surface and replacing three water molecules are different reactions. An isolated Cl atom and aqueous chloride have different electron counts and chemical potentials. A hydrogen atom placed next to a protonated inhibitor does not by itself define a valid electrochemical proton-transfer step.

Write balanced reactions first, with reservoirs and charge accounting. Then construct the required structures. This prevents appealing images from hiding a chemically inconsistent energy subtraction.

## Anodic and cathodic pathways
Anodic dissolution includes changes of oxidation state and stabilization of the outgoing ion by solution. Cathodic oxygen reduction or hydrogen evolution supplies a complementary electron sink. A neutral surface vacancy energy describes neither complete sequence automatically. Select the elementary step to model, not a vague “corrosion energy.”

**Exercise:** Compare an inhibitor on pristine Fe with one on Fe oxide. What must change in the interpretation? The substrate identity, available coordination sites, electronic reference, protonation and surface thermodynamics—not merely the adsorption-energy label.
