# THEORY_HEALTH.md
## Theory Status Dashboard

**Last updated:** 2026-03-18 (Session 6)

---

## Overall Verdict

**VIABLE — pending WS-3875 outcome.** The core structure (E₈ → SM via conformal embedding, gauge couplings, EW scale) is robust. The honest predictive scorecard is now clearer after Session 6 tier reclassifications. The existential risk remains CKM: the mechanism is now specified (27̄,6 Yukawa from 3875), but exact CG coefficients and the full CKM matrix are not yet computed.

---

## Scorecard

| Metric | Value | Trend | Notes |
|--------|-------|-------|-------|
| Tier A predictions verified | α_em (0.2%), α₁ (3.9%), α₃ (4.7%), 3 generations, SM gauge group, coupling ordering | ↑ clarified | α₂ and sin²θ_W removed from Tier A this session |
| Tier B predictions | EW scale, Higgs mass ratio | Stable | Both depend on n=15 (F3, not derived) |
| Tier C predictions | α₂ (1.6%, 1 param), sin²θ_W, mass ratios | ↓ α₂ and sin²θ_W newly demoted | α₂ 0.4% match was partially fitted — now correctly reported as Tier C |
| Active hypotheses | 2 | → stable | 3875 CKM path [mechanism specified]; RS mass mechanism |
| Stable results | ~10 | → stable | Gauge couplings, EW scale, Higgs ratio, 3 generations, SM gauge group, 3875 branching, KZ solution, (351,3) antisymmetry, CKM mechanism |
| Open failures | 2 active + 1 parked + 2 resolved | ↓ improved | F4 active; KC-g partial; F3 parked; F7 and α₂ flags resolved |
| Active contradictions | 0 | — | |
| Kill conditions | 1 partial (KC-g) | → stable | 248 sector fully killed; 3875 mechanism specified but CG not yet computed |
| Unverified flags (⚠) | 0 active | ↓ improved | All three α₂ flags resolved in Session 6 (classified as FITTED or EXTERNAL) |
| Hidden parameters identified | 1 confirmed | → stable | M_GUT as external input |
| Tier downgrades this session | 2 | NEW | Row 3 (α₂): Tier A→C; Row 5 (sin²θ_W): Tier A→C |

---

## Structural Integrity

| Component | Status | Confidence |
|-----------|--------|------------|
| E₈ → SM embedding chain | Verified | High |
| Central charge arithmetic | Code-verified exact | High |
| Gauge couplings — α_em, α₁, α₃ | Verified; zero-parameter Tier A | High |
| Gauge couplings — α₂, sin²θ_W | Verified; 1–2 fitted params; Tier C | Medium |
| EW scale from Z=12, n=15 | Verified numerically; n=15 not derived | Medium |
| Higgs mass ratio m_H/M_W = φ | By construction | High (structural) |
| 3 generations from SU(3)_fam | Structural | High |
| Mass hierarchy from (G₂)₆ | Framework established; F7 resolved | Medium |
| CKM mixing — 248 sector | **Proven impossible (V_CKM = I exact)** | High (negative result) |
| CKM mixing — 3875 sector | **Mechanism specified; CG coefficients not yet computed** | Medium — existential risk |

---

## Risk Assessment

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| WS-3875 CG gives wrong V_us | Fatal | Unknown | CG computation is next session's primary task |
| Full CKM matrix not reproducible from 3875 | Fatal | Unknown | RS profile differences must give correct hierarchy |
| F7 back-solve unstable | Major | Low | Resolved — exact values computed Session 3 |
| n=15 never derived → Tier B stays [D] | Moderate | High | Theory functional without derivation; parked |
| b₂^WZW not derivable → α₂ stays Tier C | Moderate | Medium | Future optional upgrade; not blocking |
| Top mass 11% persists after QCD corrections | Minor-Moderate | Medium | Bounded computation; Session 7 secondary task |

---

*Updated at session close when health metrics change. Detailed failure descriptions in FAILURE_LEDGER.md and Reference Core §8.*
