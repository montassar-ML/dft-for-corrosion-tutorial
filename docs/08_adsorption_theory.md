# 08 · Adsorption, deformation and free-energy references

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Write an energy difference whose reference reaction can be explained in words.

For neutral molecular adsorption from the chosen isolated-molecule reference, let S be the clean surface and M the molecule:

```math
E_{\rm ads}=E_{SM}^{\rm relaxed}-E_S^{\rm relaxed}-E_M^{\rm relaxed}.
```

Negative energy means exothermic adsorption **relative to those references**. It does not directly mean favorable adsorption from water at a stated concentration, and does not establish inhibition efficiency. Test several starting sites and orientations before discussing a preferred structure. The molecular–surface interaction can involve multiple bonding contributions. [50](../README.md#ref-50)

## Separate distortion from interaction
Extract S and M in the geometry they have in the adsorbed complex, without relaxing them. With the same cell, basis conventions and electronic-state choices:

```math
E_{\rm int}=E_{SM}^{\rm relaxed}-E_S^{\rm frozen}-E_M^{\rm frozen},
```

```math
E_{\rm def}=(E_S^{\rm frozen}-E_S^{\rm relaxed})
+(E_M^{\rm frozen}-E_M^{\rm relaxed}),\qquad
E_{\rm ads}=E_{\rm int}+E_{\rm def}.
```

This bookkeeping distinguishes a strongly interacting but highly distorted configuration from one that binds with little deformation. The decomposition is reference-dependent, not a unique observable. The fragment electronic states must remain defined, especially for broken bonds or radicals; counterpoise conventions for localized bases need separate explanation.

## An aqueous displacement reaction
A more relevant inhibition question may be displacement of surface water:

```math
M_{\rm aq}+S(\mathrm{H_2O})_n
\rightleftharpoons SM(\mathrm{H_2O})_{n-m}+m\,\mathrm{H_2O}_{\rm aq}.
```

Its free energy includes the inhibitor's solution chemical potential, surface configurations and released water. Gas-phase translational entropy cannot simply be assigned to a condensed-phase reservoir. A vacuum adsorption energy and a solution adsorption free energy should have different column names in a data table.

For a species with activity a, the reservoir term is:

```math
\mu(T,a)=\mu^\circ(T)+k_BT\ln a.
```

Choose and report the standard state. Standard-state conversion, protonation equilibria and electrode potential can alter the preferred adsorption pathway. Continuum solvation is one approximation to these environmental effects, not a complete electrolyte description. [24](../README.md#ref-24)

## Coverage and competition
Report areal density `Nads/A` and, when using monolayers, the explicit site-density convention. Increasing adsorbate number changes lateral interactions, available adsorption sites and sometimes molecular connectivity. Keeping one molecule while changing cell area also changes its periodic separation. These are physical changes as well as finite-size tests.

Do not automatically equate an experimentally measured inhibition efficiency with fractional coverage or infer a standard adsorption free energy from that assumption. That specific practice has been critically examined. [51](../README.md#ref-51)

**Self-check:** A more negative interaction energy but a less negative adsorption energy is possible. Explain it using the deformation term without claiming an arithmetic contradiction.
