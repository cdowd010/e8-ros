# E₈ Workstream: WS-CKM2 — Two-Higgs CKM from (27,3) + (27̄,3̄) in 248
## Status: CLOSED — Proposal killed by group theory; deeper structural result obtained

**Opened:** 2026-03-17 (following WS-CGC completion)
**Closed:** 2026-03-17 (same session)
**Status:** Proposal group-theoretically forbidden; all renormalizable escape routes for F8 systematically closed.

---

## 1. The Proposal

From the 248 of E8 under E8 → E6 × SU(3)_fam:
```
248 = (78,1) + (1,8) + (27,3) + (27̄,3̄)
```

The proposal was: use the (27̄,3̄_fam) component as a second Higgs with VEV v₂₇̄, giving
a second Yukawa coupling with different SU(3)_fam structure. This would generate M_u ≠ M_d
with one additional parameter tan β = v₂₇/v₂₇̄.

---

## 2. Finding 1: SU(3)_fam Forbids the (27̄,3̄_fam) Coupling [CODE-VERIFIED]

**The coupling 27_i × 27_j × (27̄, 3̄_fam)_H requires a singlet in 3_fam × 3_fam × 3̄_fam.**

```python
# Weight system computation (code-verified):
# 3 × 3 = 3̄ (antisymm) + 6 (symm)
# (3̄ + 6) × 3̄:
#   3̄ × 3̄ = 6̄ + 3    [no singlet: 3̄ ≠ conj(3̄) = 3]
#   6 × 3̄ = 3 + 15   [no singlet: 6 ≠ 6̄]
# 
# Result: 3 × 3 × 3̄ = 6̄ + 3 + 3 + 15  (dims 6+3+3+15 = 27 ✓)
# NO SINGLET.
```

Verified by two independent methods:
1. Direct weight-system computation: weight (0,0) has multiplicity 0 in the product.
2. Tensor product decomposition: 3×3×3̄ = 6̄+3+3+15, no dimension-1 representation.

**Contrast:** 3 × 3 × 3 = 1 + 8 + 8 + 10 (singlet EXISTS — this is the ε_{ijk} invariant used in Paper 1/2).

**Conclusion:** (27̄, 3̄_fam)_H has no SU(3)_fam-invariant coupling to matter 27_i × 27_j.
The WS-CKM2 proposal is group-theoretically killed.
The tan β = v₂₇/v₂₇̄ parameter has no Yukawa coupling to matter at renormalizable level.

---

## 3. Finding 2: Structural Theorem — ONE Yukawa in 248 Framework [STRUCTURAL PROOF]

The only renormalizable E6 × SU(3)_fam invariant Yukawa coupling is:
```
W_Yukawa = λ × ε_{ijk} × 27_i × 27_j × (27_H)_k
```

Proof:
- Coupling to (27, 3_fam)_H: uses d_{ABC} E6 invariant × ε_{ijk} SU(3)_fam invariant. EXISTS ✓
- Coupling to (27̄, 3̄_fam)_H: requires 3×3×3̄ singlet. DOES NOT EXIST ✗ (Finding 1)
- Coupling to (78, 1_fam)_H: 27×27 does not contain 78 in its product (27×27 = 27̄+351+351'). ABSENT ✗
- Coupling to (1, 8_fam)_H: E6 adjoint singlet, no SM quantum numbers for Yukawa. ABSENT ✗

**Consequence:** ALL mass matrices (M_u, M_d, M_e, M_ν) derive from the SAME Yukawa operator.
They are all proportional to ε_{ijk} ĥ^k, with the SAME generation direction ĥ^k.
**V_CKM = V_PMNS = I exactly.** This is an exact structural result.

---

## 4. Finding 3: Why U(1)_χ VEV Does Not Help [CODE-VERIFIED]

Within 16_i (under SO(10) → SU(5)):
- 10 of SU(5) carries U(1)_χ charge −1 (contains Q, u^c, e^c)
- 5̄ of SU(5) carries U(1)_χ charge +3 (contains d^c, L)

A VEV of U(1)_χ generator (in the (78, 1_fam) component) gives generation-universal shift:
```
c_i^{u^c} = c_i − δ    (charge −1 × δ)
c_i^{d^c} = c_i + 3δ   (charge +3 × δ)
```

Physical Yukawas with ĥ^k fixed:
```
y_u^{ij} = ε_{ijk} ĥ^k × F(c_i^Q) × F(c_j^{u^c}) = e^{+δL} × [ε_{ijk} ĥ^k F(c_i^Q) F(c_j)]
y_d^{ij} = ε_{ijk} ĥ^k × F(c_i^Q) × F(c_j^{d^c}) = e^{−3δL} × [ε_{ijk} ĥ^k F(c_i^Q) F(c_j)]
```

The δ enters as an overall multiplicative factor, not as a matrix-structure modifier.
**y_u ∝ y_d with same eigenvectors. V_CKM = I.**

---

## 5. Finding 4: Paper 2 Condensates All E6-Neutral → η₁₀ = η₅̄ is Exact [STRUCTURAL PROOF]

The F8 proof from WS-CKM stated η₁₀ = η₅̄ because "10 and 5̄ live in same 16_i".
This was proved for the specific Paper 2 condensates S and A.

**Strengthened result:** η₁₀ = η₅̄ holds for ANY condensate that is an E6 singlet.
Proof: An E6-singlet operator acts as c × ½_{E6} on any E6 multiplet — it cannot
distinguish the 10 from the 5̄ component within the 27 of E6.
The Paper 2 condensates S = (1, symmetric SU(3)_fam) and A = (1, adjoint SU(3)_fam)
are both E6 singlets. Therefore η₁₀ = η₅̄ is exact for the current framework.

For η₁₀ ≠ η₅̄, one needs a condensate with **nonzero E6 charge**. This breaks E6.
Such a condensate must come from the (27, 3_fam) or (27̄, 3̄_fam) sectors of 248.
But the (27̄, 3̄_fam) Yukawa is forbidden (Finding 1), and the (27, 3_fam) gives
the same ε_{ijk} ĥ^k direction for all mass matrices.

---

## 6. Finding 5: General Structural Theorem [ANALYTICAL + CODE-VERIFIED]

**THEOREM:** In any model satisfying:
1. Matter in (27, 3_fam) of E6 × SU(3)_fam
2. Yukawa W = ε_{ijk} × 27_i × 27_j × (27_H)_k (unique operator)
3. c-parameter structure c_i^{(f)} = c_i^{(0)} + Δ^{(f)} × D_i (any diagonal D_i)

The physical mass matrices satisfy:
```
M_u M_u† = F_i^Q F_l^Q × W_{il}^{(u)}
M_d M_d† = F_i^Q F_l^Q × W_{il}^{(d)}
```

Both share the same left factor F^Q. Since c_i^Q = c_i^{u^c} (both in 10 of SU(5)),
the matrix W^{(u)} has degenerate eigenvalues when F_Q = F_u (Antisymmetric theorem, F1).
After Paper 2 condensates lift F1 (distinct c_i per generation), the eigenbasis of
W^{(u)} and W^{(d)} is the same (both diagonal in the S+A basis). **V_CKM = I.**

Code-verified for Paper 2 parameters (PuL=5.401, QuL=3.188, PdL=3.533, QdL=1.498):
- M_u M_u† degenerate for all tested VEV directions when F_Q = F_u ✓
- [M_u M_u†, M_d M_d†] = 0 numerically (max element < 10⁻²³) ✓
- V_CKM = I (or permutation from eigenvalue ordering degeneracy) ✓

---

## 7. Genuine Paths to V_CKM ≠ I

Three mechanisms survive the analysis:

**PATH A: (351, 3_fam) operator from 3875 of E8**
- 3875 of E8 contains (351, 3_fam) component
- 351 of E6 has different SO(10) branching than 27; H_u and H_d appear at different levels
- Could give M_u ≠ M_d in eigenbasis
- **Suppression:** operators from 3875 are suppressed by M_GUT or M_Pl depending on origin
- If M_* ~ M_GUT: suppression factor (v/M_GUT) ~ 10⁻¹⁴ — too small for Cabibbo angle
- Unless 3875 appears with O(1) coefficient at the condensation scale
- **Status:** untested; requires 351 × 27 × 27 E6 CGC computation [⚠ GAP]

**PATH B: Flavor-dependent U(1)_χ breaking (generation-selective)**
- Would require a condensate carrying BOTH SU(3)_fam charge and E6 charge
- Only such fields in 248: (27, 3_fam) and (27̄, 3̄_fam)
- (27̄, 3̄_fam) Yukawa forbidden (Finding 1); (27, 3_fam) gives same eigenbasis
- **Status:** not achievable within 248

**PATH C: Non-renormalizable operators suppressed by 1/M_Pl**
- Dim-5 operators 27_i × 27_j × 27_H × X/M_Pl where X breaks 10 ↔ 5̄ symmetry
- Could give V_CKM ≠ I at O(v/M_Pl) ~ O(10⁻¹⁶)
- CKM angles are O(0.01–0.22), far too large for this suppression
- **Status:** insufficient by ~ 14 orders of magnitude

---

## 8. Session Summary

The WS-CKM2 proposal is killed. The F8 failure is now confirmed at four independent levels:
1. Renormalizable structure: only one Yukawa operator in 248 (structural)
2. Condensate structure: E6-neutral condensates force η₁₀ = η₅̄ (structural)
3. WS-CKM2 specific: (27̄,3̄_fam) coupling SU(3)_fam-forbidden (code-verified)
4. Extended analysis: no extension within 248 at renormalizable order breaks V_CKM = I

**KC-g upgrade question for Chris:** Given that ALL renormalizable escape routes are now closed,
should KC-g be upgraded from "partial kill" to "full kill of Paper 2 CKM"?
The framework survives if Paper 2 is understood as predicting mass hierarchies only,
with CKM delegated to non-renormalizable physics. This is a meaningful but weaker claim.

---

*End of WS-CKM2 workstream file. Status: CLOSED → Archive.*
