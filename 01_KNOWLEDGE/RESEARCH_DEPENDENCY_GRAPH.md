# RESEARCH_DEPENDENCY_GRAPH.md
## Axiom → Derivation → Prediction → Test Dependency Map

**Last updated:** 2026-03-18 (Session 6)

Maps what depends on what. Used to assess the impact of changing any single assumption.
Also serves as the **Research Radar** — prioritized active directions at bottom of file.

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
       + SM beta coefficients (RK-005) → M_Z-scale couplings
           ↓
       α_em (Tier A, 0.2%) ✓
       α₁   (Tier A, 3.9%) ✓
       α₃   (Tier A, 4.7%) ✓
           ↓
       + [FITTED: b₂^WZW = +38/3] → α₂ two-stage RG   } Tier C (Session 6)
       + [EXTERNAL: M_GUT = 5.7×10¹⁶]                  }
       + [FITTED: +2.75 corrections] → α₂ final value   }
       Self-consistent WZW crossing: 1/α₂ = 29.10 (1.6%, 1 param) [Tier C]
       sin²θ_W [Tier C, inherits α₂ flags]

A1 → A5 → s₀ = ln(12) → Bekenstein bound
           ↓
       + A6 → M_W = M_Pl/12¹⁵ (Tier B, #13)
                ↓
            v = 2M_W/g₂ (Tier A, #10)
            m_H = φ × M_W (Tier B, #14)
            m_top = v/√φ (Tier C, #16) [F4: 11% off — QCD corrections pending]

A4 → SU(3)_fam → 3 generations (Tier A, #7)
      ↓
  + A8 → (G₂)₆ condensates → c-parameters
          ↓
      + A9 → RS bulk profiles → mass formula m_i = v×exp(−c_i×L)
              ↓
          Mass ratios (Tier C, #18, #19) [F7: RESOLVED Session 3]
              ↓
          CKM mixing → BLOCKED in 248 (V_CKM = I exact — 4 proofs)
              ↓
          3875 extension (REV-009) → mechanism SPECIFIED
              ↓
          (27̄,6) Yukawa CG coefficient ← NEXT COMPUTATION (WS-3875)
              ↓
          V_us prediction → full CKM matrix (RS profiles) → KC-g verdict
```

---

## Dependency Flag Status (Updated Session 6)

| Flag | Previous Status | Current Status | What depends on it |
|------|----------------|----------------|-------------------|
| b₂^WZW = +38/3 | [⚠ unverified] | [FITTED — classified Session 6] | α₂ two-stage RG → sin²θ_W |
| +2.75 corrections | [⚠ unverified] | [FITTED — classified Session 6] | α₂ final value |
| M_GUT = 5.7×10¹⁶ | [⚠ unverified] | [EXTERNAL INPUT — Session 6; self-consistent value = 2.2×10¹⁶] | All RG running; proton lifetime |

**No active ⚠ flags remaining.** All three resolved in Session 6.

---

## Kill Condition Dependencies

| KC | Triggered by | Would kill | Status |
|----|-------------|------------|--------|
| KC-a | Rank-3+ MTC with d=φ | Fibonacci uniqueness → all φ predictions | Not triggered |
| KC-b | Jones index argument circular | Self-modeling foundation | Not triggered |
| KC-c | Wrong EM charges from embedding | SM identification | Not triggered |
| KC-d | h=2/5 non-tachyonic | Forced symmetry breaking | Not triggered |
| KC-e | dS/CFT inconsistency | Jacobson gravity derivation | Not triggered |
| KC-f | Embedding arithmetic error | Central charge cascade | Not triggered |
| KC-g | No CKM from E₈ (any rep) | Flavor physics entirely | **PARTIAL KILL** — 248 sector killed; 3875 mechanism specified; CG pending |
| KC-NEW | Alternative embeddings yield different couplings | Uniqueness claim false | Not triggered |

---

## Research Radar — Active Directions (Prioritized)

*This section is the single source for research priority ordering. Updated each session.*

| Priority | Direction | Rationale | Depends on | Status |
|----------|-----------|-----------|------------|--------|
| **1** | **WS-3875 exact CG coefficient for (27̄,6) Yukawa** | Existential CKM question; mechanism specified but coefficient not computed; V_us precision depends on this | E₈ weight system in E₆×SU(3)_fam basis | **CRITICAL PATH — next session primary** |
| **2** | **WS-3875 full CKM matrix** | RS profile differences → V_cb, V_ub; Wolfenstein parametrization; closes KC-g | Exact CG (Priority 1) | After Priority 1 |
| **3** | **F4 top mass QCD correction** | m_top 11% off; tree-level vs pole mass requires RG running + threshold corrections; bounded computation | Standard QCD RG | Next session secondary; parallel to CKM |
| **4** | **F7 lepton sector back-solve** | Complete the parameter set; derive P_l×L, Q_l×L from m_τ/m_μ, m_μ/m_e | F4 resolution | After F4 |
| **5** | **Derive b₂^WZW from first principles** | Would upgrade α₂ Tier C → Tier B (0 free params); requires WZW-to-4D correspondence above M_GUT | New theoretical insight | Low priority until CKM resolved |
| **6** | **F3 (n=15)** | Blocked — self-modeling map S undefined; needs new mathematical ideas | None available | Parked indefinitely |

### Critical path (current)
```
WS-3875 exact CG ← SESSION 7 PRIMARY
    └── Precise V_us
            └── Full CKM matrix (RS profiles) → Paper 3
                    └── KC-g final verdict

F4 top mass ← SESSION 7 SECONDARY (parallel)
    └── QCD correction → resolved or escalated
```

---

*Update when dependencies change or priorities shift. Use the dependency chains to assess blast radius of any new result.*
