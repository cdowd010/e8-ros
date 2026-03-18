# FAILURE_LEDGER.md
## Unresolved Problems and Theoretical Failures

**Last updated:** 2026-03-17 (ROS v2 Session 1 — initial population from Reference Core §8)

---

## Active Failures

### F2 — M_R (right-handed neutrino mass) not derived
**Status:** [ACTIVE — low priority]
**Description:** The seesaw mass M_R is fitted, not derived from the framework. m_ν prediction (Tier C #17) depends on this fitted parameter.
**Impact:** m_ν prediction is not a genuine prediction until M_R is derived.
**Blocking:** Nothing critical.
**Approach:** Requires understanding of Majorana mass origin in the E₈ framework. Deferred.

### F4 — Top mass 11% discrepancy
**Status:** [ACTIVE]
**Description:** Tree-level prediction m_top = v/√φ ≈ 193 GeV vs observed 173 GeV (11% off). Source unknown. Possible causes: QCD corrections, threshold effects, running vs pole mass distinction, or genuine theoretical issue.
**Impact:** Largest single discrepancy in a zero-parameter prediction.
**Blocking:** Confidence in the Yukawa = 1/√φ claim.
**Approach:** Compute QCD and EW corrections to tree-level mass. Check running mass vs pole mass. Bounded computation.

### F5 — α₃ dynamical origin of M_T/M_GUT
**Status:** [ACTIVE — deprioritized]
**Description:** α₃(M_Z) prediction requires M_T/M_GUT = 1.586 from doublet-triplet splitting. Three dynamical approaches all failed (perturbative shift insufficient; RS bulk profiles wrong direction; Paper 2 condensate governs fermions not GUT-Higgs). Value is fitted.
**Impact:** α₃ demoted from Tier A to Tier C.
**Blocking:** α₃ Tier A restoration.
**Approach:** GUT-breaking sector model needed. Deferred.

### F7 — §6 parameter inconsistency
**Status:** [ACTIVE — high priority]
**Description:** Stored P×L, Q×L values (from Paper 2 notebook) give mass ratios wildly inconsistent with Tier C targets: m_t/m_u = 291.5 (target: 84,455, factor ~274× off) and m_b/m_d = 6.6 (target: 836, factor ~136× off). Tier-C-consistent values exist (PuL=5.401, QuL=3.188, PdL=3.533, QdL=1.498) but are ~5–7% off exact targets.
**Impact:** All Tier C mass predictions unreliable until resolved. Paper 2 notebook audit blocked.
**Blocking:** Tier C predictions; Paper 2 notebook; downstream CKM work.
**Approach:** Back-solve exact P×L, Q×L for up and down sectors to reproduce m_t/m_u = 84,455 and m_b/m_d = 836 exactly. Then audit Paper 2 notebook with corrected values.

## Confirmed / Resolved Failures

### F1 — Mass degeneracy (Paper 1)
**Status:** [RESOLVED]
**Resolution:** Paper 2 (G₂)₆ condensates break the degeneracy.

### F3 — n = 15 not derived
**Status:** [ARCHIVED — stalled]
**Description:** Three independent [T] coincidences at n=15 documented. Fundamental blockage: self-modeling map S not defined precisely enough to derive termination. M_W stays Tier B.
**Impact:** Tier B predictions cannot be promoted to Tier A.
**Blocking:** Tier B → Tier A upgrade only.
**Approach:** Needs new mathematical ideas. Parked.

### F8 — V_CKM = I structural result
**Status:** [CONFIRMED — 2026-03-17]
**Description:** Fully confirmed within 248 framework at renormalizable order. Four independent proofs. This is not a failure to fix — it is a structural feature of the 248 that requires the 3875 extension.
**Impact:** Triggered KC-g partial kill.

---

## Kill Condition Tracker

### KC-g — CKM mixing
**Status:** [PARTIAL KILL]
**248 sector:** FULLY KILLED. V_CKM = I exact at renormalizable order.
**3875 sector:** UNTESTED. Path A ((351,3_fam) from 3875) is the only surviving viable mechanism.
**Upgrade to full kill if:** WS-3875 shows Path A is also insufficient.
**Verdict date:** Pending WS-3875.

---

*Update at session close. Move resolved failures to the resolved section with resolution noted.*
