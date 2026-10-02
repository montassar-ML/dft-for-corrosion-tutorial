# 06 · Metal surfaces and the bcc Fe(110) teaching model

[Course home](../README.md) · [Analysis catalogue](24_analysis_catalogue.md) · [Case study](../case-study/README.md)

## Learning objective
Specify an actual atomic surface rather than writing only “mild steel” in a computational methodology.

A Miller index identifies a crystallographic orientation relative to a particular lattice. bcc Fe(110), Fe(100) and Fe(111) are not interchangeable. They have different surface coordinations and can relax and magnetize differently. A first-principles study of several Fe faces provides a useful methodological precedent, not a license to reuse its parameters without reconvergence. [47](../README.md#ref-47)

## Why Fe(110) is a useful exercise
The relatively dense bcc(110) termination supplies a manageable baseline for learning adsorption. It is not an assertion that an experimental steel sample exposes only this facet. Real samples contain alloys, grain boundaries, steps, oxide/hydroxide films and contaminants.

Use a relaxed ferromagnetic bulk reference calculated with the same method as the slab. Converge its lattice and energy per atom, then cleave a crystallographically defined surface. Choosing an experimental lattice instead is legitimate for a constrained comparison, but state the imposed strain and do not silently mix lattice conventions.

## Surface-site naming
The bcc(110) surface mesh is not the hexagonal mesh of fcc(111). Label top and inequivalent bridge candidates from the actual neighbor geometry; identify short- and long-bridge families where appropriate. Define “hollow” by the surrounding atoms and coordinates. Record lateral lattice vectors and fractional adsorption coordinates. Avoid copying a threefold-site label from an unrelated facet.

An extended molecule spans several atoms. Its relevant descriptor may be the donor-atom coordination and molecular footprint, not just one point designated “the adsorption site.”

## Fixed layers and relaxation
A fixed lower slab region mimics bulk support and reduces cost, but it changes the accessible relaxation space. Increase both total depth and the relaxed portion until the target observable is stable. For magnetic surfaces, inspect central-layer moments as well as interlayer spacing. A flat energy curve alone can conceal a geometry or magnetic artifact.

## Two sides of a slab
A symmetric clean slab can simplify surface-energy analysis. One-sided adsorption usually makes the slab asymmetric; electrostatic treatment and which vacuum side is used for the work function must be recorded. The opposite face is not absent simply because it is not drawn in a picture. [21](../README.md#ref-21)

**Self-check:** You have a well-converged Fe(110) slab. Does that validate a corrosion mechanism in chloride solution? It validates only part of the numerical solid model. Surface speciation, electrolyte and potential still require a physical justification.
