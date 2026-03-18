# FAILURE_LEDGER.md
## Unresolved Problems and Theoretical Failures

**Last updated:** 2026-03-18 (Session 6 — F7 moved to resolved, KC-g updated, F4 linked to WS)

---

## Active Failures

### F2 — M_R (right-handed neutrino mass) not derived
**Status:** [ACTIVE — low priority]
**Description:** The seesaw mass M_R is fitted, not derived from the framework. m_ν prediction (Tier C #17) depends on this fitted parameter.
**Impact:** m_ν prediction is not a genuine prediction until M_R is derived.
**Blocking:** Nothing critical.
**Approach:** Requires understanding of Majorana mass origin in the E₈ framework. Deferred.

### F4 — Top mass 11% discrepancy
**Status:** [ACTIVE — workstream open]
**Workstream:** `E8_WS_F4_TopMass.md` [OPEN, Priority 3]
**Description:** Tree-level prediction m_top = v/√φ ≈ 193.6 GeV (using observed v=246.22 GeV) vs observed pole mass 172.57 GeV — 12% discrepancy. Most likely explanation: tree-level formula gives MS-bar mass at some high scale μ_0, not the pole mass. QCD RG running + threshold corrections need to be computed.
**Impact:** Largest single discrepancy in a zero-parameter prediction. Undermines confidence in Yukawa = 1/√φ if not resolved.
**Blocking:** Confidence in the Yukawa structure at tree level.
**Approach:** Identify μ_0 (KK scale, M_GUT, or M_Pl); run m_top^{MS}(μ_0) → m_top^{MS}(m_top) via 3-loop QCD beta function; apply pole mass correction. Bounded computation. See `E8_WS_F4_TopMass.md §F` for full steps.

### F5 — α₃ dynamical origin of M_T/M_GUT
**Status:** [ACTIVE — deprioritized]
**Description:** α₃(M_Z) prediction requires M_T/M_GUT = 1.586 from doublet-triplet splitting. Three dynamical approaches all failed (perturbative shift insufficient; RS bulk profiles wrong direction; Paper 2 condensate governs fermions not GUT-Higgs). Value is fitted.
**Impact:** α₃ remains Tier C.
**Blocking:** α₃ Tier A restoration only.
**Approach:** GUT-breaking sector model needed. Deferred.

### F6 — DM abundance
**Status:** [ACTIVE — low priority]
**Description:** Dark matter abundance not predicted. Requires condensation dynamics.
**Impact:** Cosmological predictions incomplete.
**Blocking:** Nothing critical for particle physics predictions.
**Approach:** Deferred.

### F7-lepton — Lepton sector RS parameters not computed
**Status:** [ACTIVE — medium priority]
**Description:** The exact PDG back-solve for the quark sector (P_u×L, Q_u×L, P_d×L, Q_d×L) was completed in Session 3. The lepton sector parameters (P_l×L, Q_l×L) have not yet been computed from m_τ/m_μ and m_μ/m_e. This is the remaining open part of what was F7.
**Impact:** Lepton mass predictions (Tier C) remain unaudited. Paper 2 notebook audit for leptons blocked.
**Blocking:** Lepton sector Tier C predictions; Paper 2 notebook completion.
**Approach:** Same method as quark sector: ln(m_τ/m_μ) = 2Y_l, ln(m_μ/m_e) — solve for P_l×L and Q_l×L exactly. Bounded computation. Should be scoped into a workstream or added to WS-F4_TopMass as a secondary task.

---

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

### F7 — Quark sector P×L, Q×L inconsistency
**Status:** [RESOLVED — Session 3, 2026-03-17]
**Resolution:** Exact PDG back-solve complete. Up sector: P_u×L = 5.9405, Q_u×L = 2.4571 (reproduces m_t/m_u = 86,500, m_t/m_c = 136.2, m_c/m_u = 635 exactly). Down sector: P_d×L = 3.2173, Q_d×L = 1.9027 (reproduces m_b/m_d = 836, m_b/m_s = 44.9, m_s/m_d = 18.6 exactly). All `[✓ code-verified 2026-03-17]`. Stored values in §6 remain present as legacy but are flagged as incorrect — use exact back-solved values only. Lepton sector is open as F7-lepton above.

### F8 — V_CKM = I structural result
**Status:** [CONFIRMED — 2026-03-17]
**Description:** Fully confirmed within 248 framework at renormalizable order. Four independent proofs. This is not a failure to fix — it is a structural feature of the 248 that requires the 3875 extension (see KC-g and WS-3875).
**Impact:** Triggered KC-g partial kill.

### F-α₂ — Three [⚠] flags on α₂ prediction chain
**Status:** [RESOLVED — Session 6, 2026-03-18]
**Resolution:** All three flags classified. b₂^WZW = +38/3: FITTED (not derivable from E₈ field content). +2.75 corrections: FITTED (no identified source). M_GUT = 5.7×10¹⁶: EXTERNAL INPUT (self-consistent crossing gives 2.20×10¹⁶). Rows 3 and 5 downgraded Tier A → Tier C. Self-consistent WZW crossing prediction: 1/α₂ = 29.10 (1.6% off, 1 free param). See RK-011 in RESOLVED_KNOWLEDGE.md.

---

## Kill Condition Tracker

### KC-g — CKM mixing
**Status:** [PARTIAL KILL — mechanism specified, CG pending]
**248 sector:** FULLY KILLED. V_CKM = I exact at renormalizable order (RK-006).
**3875 sector — mechanism specified (Session 5):** The (27̄,6) symmetric component of the 3875 generates V_CKM ≠ I via a SYMMETRIC Yukawa coupling (6 = Sym²(3)_fam). The (351,3) was ruled out — antisymmetric coupling preserves V_CKM = I (RK-010). KZ equation solved exactly (RK-012). Semi-quantitative V_us ~ 0.2–0.3 (observed 0.226).
**Remaining work:** Exact CG coefficient for (27̄,6) Yukawa vertex; full CKM matrix from RS profile differences. See `E8_WS_3875.md`.
**Upgrade to full kill if:** Exact CG coefficient gives V_us far outside observed range (≪0.1 or ≫0.5).
**Clear if:** Exact CG + RS profiles reproduce V_us, V_cb, V_ub to within ~20%.
**Verdict date:** Pending Session 7 (WS-3875 exact CG computation).

---

*Update at session close. Move resolved failures to the resolved section with resolution noted. Link active failures to their workstream files.*
