# RESOLVED_KNOWLEDGE.md
## Stable Conclusions — Do Not Re-derive

**Last updated:** 2026-03-17 (ROS v2 Session 1 — initial population)

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
**Result:** The 248 of E₈ admits exactly one Yukawa operator. All mass matrices are proportional. V_CKM = I exact.
**Dependencies:** E₈ representation theory, SU(3)_fam invariance.
**Would invalidate if:** Error in 3×3×3̄ decomposition or E₆ Clebsch-Gordan analysis.

## RK-007: 4cos²(π/5) = φ²
**Verified:** 2026-03-17 (code-verified, algebraic identity)
**Result:** Exact algebraic identity. 4cos²(π/5) = (3+√5)/2 = φ².
**Dependencies:** None (pure mathematics).
**Would invalidate if:** Never — exact identity.

---

*Add entries when a result is confirmed stable and no longer needs re-derivation. Remove if a dependency is invalidated.*
