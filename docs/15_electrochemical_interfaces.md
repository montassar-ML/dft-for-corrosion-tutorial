# 15 · Charge, potential, CHE and mixed corrosion kinetics

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Keep fixed-electron calculations, potential-controlled calculations and corrosion current in separate conceptual boxes.

Most ordinary periodic DFT calculations hold electron number fixed. A potentiostated experimental electrode exchanges electrons with an external circuit. The appropriate electronic thermodynamic potential at fixed electron chemical potential is a Legendre transform:

```math
\Omega(T,\mu_e;\mathbf R)=\min_{N_e}\{F(T,N_e;\mathbf R)-\mu_eN_e\}.
```

At fixed nuclear composition this expression concerns the electronic reservoir. Reactions exchanging atoms, protons or ions require their reservoir terms too. In a constant-potential calculation, energies and forces must follow a consistent grand-potential formulation, including how electrostatic countercharge is represented. [25](../README.md#ref-25)

## Fixed charge does not imply fixed potential
Two adsorbate states at the same electron number can have different work functions. Comparing them at fixed number is not necessarily comparing them at the same experimental potential. Conversely, at fixed potential their equilibrium electron numbers can differ. Additional electrons and a homogeneous background do not by themselves define a physical double layer. [39](../README.md#ref-39)

## Computational hydrogen electrode: define the sign
Let e be the positive elementary charge. At the standard hydrogen reference, for ideal proton activity and potential U versus SHE:

```math
\mu(\mathrm H^++e^-)
=\tfrac12G_{\mathrm H_2}-eU_{\rm SHE}-k_BT\ln(10)\,\mathrm{pH}.
```

For a reaction written to **consume n matched proton–electron pairs**, with other terms consistently referenced:

```math
\Delta G(U,\mathrm{pH})=\Delta G(0,0)+neU_{\rm SHE}
+n k_BT\ln(10)\,\mathrm{pH}.
```

The plus sign follows because the pair chemical potential is subtracted from product minus reactant free energy. Reverse the reaction and reverse the sign. The conversion is:

```math
U_{\rm RHE}=U_{\rm SHE}+\frac{k_BT\ln(10)}{e}\,\mathrm{pH}.
```

On the RHE scale, matched-pair pH contributions are already incorporated in the potential reference; do not add them again. Unequal proton/electron stoichiometries and other acid–base steps require separate accounting. The CHE paper established a thermodynamic strategy for electrochemical intermediates; CHE is not itself a constant-potential electronic solver. [23](../README.md#ref-23)

## What CHE omits
Neutral-slab CHE comparisons do not automatically capture explicit solvent rearrangement, potential-dependent adsorption dipoles/capacitance, double-layer structure or charge-dependent barriers. More explicit interface approaches trade computational cost against these missing effects. [38](../README.md#ref-38)

## Corrosion potential requires two reaction families
Anodic dissolution and cathodic reduction contribute currents. With anodic current positive:

```math
j_{\rm a}(U_{\rm corr})+j_{\rm c}(U_{\rm corr})=0.
```

At open circuit, zero *net* current does not mean zero metal dissolution. DFT can constrain elementary-state energies, barriers and electronic structure. Predicting `Ucorr` and corrosion rate additionally requires kinetic models, coverages and often transport. Work function, inhibitor gap and equilibrium adsorption energy do not directly give this current balance.

**Exercise:** A water-assisted reaction consumes one proton but releases one electron. Can the matched-pair formula be copied? No. Write the full balanced reaction and collect proton and electron chemical-potential terms with their own stoichiometric signs.
