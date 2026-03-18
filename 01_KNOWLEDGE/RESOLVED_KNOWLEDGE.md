# RESOLVED_KNOWLEDGE.md
## Stable Conclusions — Do Not Re-derive

**Last updated:** 2026-03-18 (Session 6 — RK-008 through RK-012 added)

Contains results considered settled. Re-derivation is unnecessary unless a dependency is invalidated.

---

## RK-001: Central charge arithmetic of the embedding cascade
**Verified:** 2026-03-17 (code-verified, exact rational arithmetic)
**Result:** All central charges in the E₈ → SU(3)_fam × E₆ → ... → SM chain are exact at level 1. Total c = 8.
**Key values:** c(E₈)=8, c(E₆)=6, c(SO(10))=5, c(SU(5))=4, c(SU(3))=2, c(SU(2))=1, c(G₂)=14/5, c(F₄)=26/5.
**Dependencies:** WZW formula c = dim(G)/(1+h∨) at k=1.
**Would invalidate if:** Error found in dual Coxeter numbers or WZW formula.

## RK-002: j(i)^{1/3} = 12 exactly
**Verified:** 2026-03-17 (code-verified)
**Result:** j(i) = 1728 = 12³. Z = j(τ)^{1/3} at τ = i gives Z = 12 exactly. Z'(i) = 0 proved (saddle point).
**Dependencies:** Modular j-invariant theory.
**Would invalidate if:** Mathematical error in j-invariant evaluation.

## RK-003: Jones index discrete series selects φ²
**Verified:** Standard reference (Jones 1983)
**Result:** The discrete series of Jones indices is {4cos²(π/n) : n ≥ 3}. Computational faithfulness argument selects n=5, giving index φ² = (3+√5)/2.
**Dependencies:** [P] Computational faithfulness selection criterion.
**Would invalidate if:** Alternative selection criterion is better justified.

## RK-004: Fibonacci τ anyon uniqueness at index φ²
**Verified:** Jones-Ocneanu classification; RSW 2009
**Result:** The unique non-trivial MTC at Jones index φ² is Fibonacci. d_τ = φ. Realized by (G₂)₁.
**Dependencies:** MTC classification theorems.
**Would invalidate if:** Rank-3+ MTC with d=φ found (KC-a).

## RK-005: SM one-loop beta coefficients
**Verified:** 2026-03-17 (code-verified from SM field content)
**Result:** b₃ = −7, b₂ = −19/6, b₁ = +41/6.
**Dependencies:** SM field content (n_g=3, one Higgs doublet).
**Would invalidate if:** BSM fields below M_Z.

## RK-006: V_CKM = I in the 248 framework (renormalizable order)
**Verified:** 2026-03-17 (four independent proofs, code-verified)
**Result:** The 248 of E₈ admits exactly one Yukawa operator. All mass matrices are proportional. V_CKM = I exact. All five escape routes within 248 exhausted (see F8 in Reference Core §8).
**Dependencies:** E₈ representation theory, SU(3)_fam invariance.
**Would invalidate if:** Error in 3×3×3̄ decomposition or E₆ Clebsch-Gordan analysis.

## RK-007: 4cos²(π/5) = φ²
**Verified:** 2026-03-17 (code-verified, algebraic identity)
**Result:** Exact algebraic identity. 4cos²(π/5) = (3+√5)/2 = φ².
**Dependencies:** None (pure mathematics).
**Would invalidate if:** Never — exact identity.

## RK-008: Level-2 vacuum module structure of (E₈)₁
**Verified:** 2026-03-17 (code-verified, SageMath)
**Result:** Sym²(248) = 1 + 248 + 3875 + 27000. The 27000 has a null state at level 2 and decouples entirely. The physical level-2 space has dimension 4124 = 1 + 248 + 3875.
**Dependencies:** E₈ representation theory; (E₈)₁ WZW null state structure.
**Would invalidate if:** Error in Sym²(248) decomposition or null state argument.

## RK-009: Conformal weight h(3875) = 48/31
**Verified:** 2026-03-17 (code-verified; corrected from stored error h=1)
**Result:** h(3875) = C₂(3875)/(2K) = 96/62 = 48/31 ≈ 1.548 via Weyl formula ⟨ω₇, ω₇+2ρ⟩/(2(k+h∨)) = 96/62. The 3875 is NOT integrable at k=1 (Kac mark a₇=2); it appears as a composite operator :JᵃJᵇ: at level 2 of the vacuum module.
**Dependencies:** Weyl character formula; E₈ Kac marks.
**Would invalidate if:** Error in C₂(3875) or Weyl formula application.

## RK-010: (351,3) component of 3875 cannot generate CKM mixing
**Verified:** 2026-03-18 (code-verified, Session 5)
**Result:** The (351,3) component of the 3875 under E₆×SU(3)_fam gives an ANTISYMMETRIC Yukawa coupling (3×3×3 → ε_{ijk} singlet). An antisymmetric Yukawa matrix gives V_CKM = I upon diagonalization. The (351,3) does not contribute to CKM mixing. CKM mixing comes exclusively from the (27̄,6) symmetric component.
**Dependencies:** E₆ representation theory; SU(3)_fam tensor products.
**Would invalidate if:** Error in antisymmetry argument or 3×3×3 decomposition.

## RK-011: α₂ fitted parameter classification (Session 6)
**Verified:** 2026-03-18 (Session 6 field content analysis)
**Result:** Three quantities previously carrying [⚠] flags are now classified:
- b₂^WZW = +38/3: FITTED. Not derivable from E₈ field content. Naive counting gives 36 Weyl doublets (b₂=50/3) or 24f+12s (b₂=28/3); neither gives 38/3. The value requires exactly 30 Weyl doublets with no physical justification.
- +2.75 corrections: FITTED. No identified source among threshold, two-loop, or WZW non-perturbative contributions.
- M_GUT = 5.7×10¹⁶ GeV: EXTERNAL INPUT. The self-consistent WZW α₃=α₂ crossing gives M_GUT = 2.20×10¹⁶ GeV, 1/α₂ = 29.10 (1.6% off observed). The 5.7×10¹⁶ value was taken as an external input.
**Consequence:** α₂ prediction (Row 3) and sin²θ_W (Row 5) downgraded Tier A → Tier C. The self-consistent prediction (1.6%, 1 free param) is the honest reported value.
**Would invalidate if:** A physical derivation of b₂^WZW = +38/3 is found, which would upgrade α₂ back toward Tier B.

## RK-012: KZ equation solution for (E₈)₁ adjoint 4-point function
**Verified:** 2026-03-18 (code-verified, exact, Session 5)
**Result:** The KZ equation 31·dF/dz = −60·[1/z + 1/(z−1)]·F has exact solution F(z) = [z(z−1)]^{−60/31}. Level-2 vacuum block coefficient c₂ = 2730/961 ≈ 2.841 (exact rational arithmetic).
**Dependencies:** (E₈)₁ WZW OPE structure; KZ equation at level k=1.
**Would invalidate if:** Error in KZ equation setup or boundary conditions.

---

*Add entries when a result is confirmed stable and no longer needs re-derivation. Remove if a dependency is invalidated.*
