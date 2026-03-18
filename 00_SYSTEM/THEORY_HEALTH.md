# THEORY_HEALTH.md
## Theory Status Dashboard

**Last updated:** 2026-03-17 (ROS v2 Session 1)

---

## Overall Verdict

**VIABLE — pending WS-3875 outcome.** The core structure (E₈ → SM via conformal embedding, gauge couplings, EW scale) is robust. The existential risk is CKM: if the 3875 extension cannot generate mixing, the theory fails to reproduce a fundamental observed feature.

---

## Scorecard

| Metric | Value | Trend | Notes |
|--------|-------|-------|-------|
| Tier A predictions verified | 6 of 12 testable | Stable | α_em, α₂, sin²θ_W excellent; α₁, α₃ at 4–5% |
| Tier B predictions | 3 | Stable | All depend on n=15 (F3, not derived) |
| Tier C predictions | 5 | Uncertain | Parameters need back-solving (F7) |
| Active hypotheses | 2 | — | 3875 CKM path; RS mass mechanism |
| Stable results | ~8 | — | Gauge couplings, EW scale, Higgs ratio, 3 generations, SM gauge group |
| Open failures | 5 | — | F2, F3, F4, F5, F7 (F1 resolved, F8 confirmed) |
| Active contradictions | 0 | — | |
| Kill conditions | 1 partial (KC-g) | ↑ risk | 248 sector fully killed; 3875 untested |
| Unverified flags | 3 | — | b₂^WZW, +2.75, M_GUT |

---

## Structural Integrity

| Component | Status | Confidence |
|-----------|--------|------------|
| E₈ → SM embedding chain | Verified | High |
| Central charge arithmetic | Code-verified exact | High |
| Gauge couplings from WZW levels | Verified (3 ⚠ flags) | Medium-High |
| EW scale from Z=12, n=15 | Verified numerically; n=15 not derived | Medium |
| Higgs mass ratio m_H/M_W = φ | By construction | High (structural) |
| 3 generations from SU(3)_fam | Structural | High |
| Mass hierarchy from (G₂)₆ | Framework established; params inconsistent (F7) | Low-Medium |
| CKM mixing | **Failed in 248; untested in 3875** | **Low — existential risk** |

---

## Risk Assessment

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| WS-3875 fails → no CKM | Fatal | Unknown | Only path left; must be tested |
| F7 unresolvable → mass predictions fail | Major | Low | Back-solve expected to work |
| n=15 never derived → Tier B stays [D] | Moderate | Medium | Theory functional without derivation |
| M_GUT inconsistency propagates | Moderate | Medium | Self-consistent derivation needed |
| Top mass 11% persists after corrections | Minor-Moderate | Medium | QCD/threshold corrections may resolve |

---

*Updated at session close per §1.3 checklist. Detailed failure descriptions in FAILURE_LEDGER.md and Reference Core §8.*
