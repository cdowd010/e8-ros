# RESEARCH_DEPENDENCY_GRAPH.md
## Axiom → Derivation → Prediction → Test Dependency Map

**Last updated:** 2026-03-17 (ROS v2 Session 1 — initial population)

Maps what depends on what. Used to assess the impact of changing any single assumption.

---

## Core Axioms / Assumptions

| ID | Axiom | Status | If invalidated... |
|----|-------|--------|-------------------|
| A1 | (E₈)₁ is the correct holomorphic CFT for the dS boundary | [P] | Everything collapses |
| A2 | Self-modeling formalized as subfactor inclusion | [D] | Jones index selection fails |
| A3 | Computational faithfulness selects φ² | [P] | Different Jones index → different MTC |
| A4 | Conformal embedding at level 1 gives SM | [T] verified | Gauge group wrong |
| A5 | Z = j(i)^{1/3} = 12 fixes entropy | [T] verified | EW scale prediction lost |
| A6 | n = 15 tower height | [D] algebraic identity | Tier B predictions fail |
| A7 | Higgs = Fibonacci τ anyon | [D] | m_H/M_W = φ lost |
| A8 | (G₂)₆ condensates for mass hierarchy | [D] | Tier C predictions fail |
| A9 | RS/AdS₅ dual geometry | [D] | Bulk mass formula lost |

---

## Dependency Chains

```
A1 → A2 → A3 → Jones index φ²
                  ↓
              Fibonacci MTC → A7 → m_H/M_W = φ (Tier B, #15)
                  ↓
              (G₂)₁ realization (RK-004)

A1 → A4 → SM gauge group (Tier A, #8)
           ↓
       WZW levels K_i → Planck-scale couplings
           ↓
       + SM beta coefficients (RK-005) → M_Z-scale couplings (Tier A, #1–6)
           ↓
       + [⚠ b₂^WZW] → α₂ two-stage RG
       + [⚠ M_GUT] → all RG running
       + [⚠ +2.75] → α₂ final value

A1 → A5 → s₀ = ln(12) → Bekenstein bound
           ↓
       + A6 → M_W = M_Pl/12¹⁵ (Tier B, #13)
                ↓
            v = 2M_W/g₂ (Tier A, #10)
            m_H = φ × M_W (Tier B, #14)
            m_top = v/√φ (Tier C, #16)

A4 → SU(3)_fam → 3 generations (Tier A, #7)
      ↓
  + A8 → (G₂)₆ condensates → c-parameters
          ↓
      + A9 → RS bulk profiles → mass formula m_i = v×exp(−c_i×L)
              ↓
          Mass ratios (Tier C, #18, #19) [⚠ F7: params inconsistent]
              ↓
          CKM mixing → BLOCKED (V_CKM = I in 248)
              ↓
          Requires 3875 extension (H-001) → KC-g verdict
```

---

## Unverified Dependencies (⚠ flags)

| Flag | What depends on it | Risk if wrong |
|------|-------------------|---------------|
| b₂^WZW = +38/3 | α₂ two-stage RG → sin²θ_W | Tier A #3, #5 shift |
| +2.75 corrections | α₂ final value | Tier A #3 shifts by ~9% |
| M_GUT = 5.7×10¹⁶ | All RG running; proton lifetime | Tier A #2–4 shift; #12 changes |

## Kill Condition Dependencies

| KC | Triggered by | Would kill |
|----|-------------|------------|
| KC-a | Rank-3+ MTC with d=φ | Fibonacci uniqueness → all φ predictions |
| KC-b | Jones index argument circular | Self-modeling foundation |
| KC-c | Wrong EM charges from embedding | SM identification |
| KC-d | h=2/5 non-tachyonic | Forced symmetry breaking |
| KC-e | dS/CFT inconsistency | Jacobson gravity derivation |
| KC-f | Embedding arithmetic error | Central charge cascade |
| KC-g | No CKM from E₈ (any rep) | Flavor physics entirely |

---

*Update when dependencies change. Use this to assess blast radius of any new result.*
