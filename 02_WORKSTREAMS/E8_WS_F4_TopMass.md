# E8_WS_F4_TopMass.md
## Workstream: Top Mass 11% Discrepancy — QCD Correction Analysis

**Status:** OPEN
**Opened:** 2026-03-18 (Session 6, scoped at close)
**Closed:** —
**Priority:** 3 (after WS-3875 CG computation — see RESEARCH_DEPENDENCY_GRAPH)
**Objective:** Determine whether QCD corrections (RG running + threshold effects) can account for the 11% discrepancy between the tree-level prediction m_top = v/√φ and the observed pole mass of 172.57 GeV.
**Kill condition relevance:** None directly. If the discrepancy persists after all corrections, it becomes a new active failure (F4 escalated), but does not trigger an existing kill condition.

---

## §A — Problem Statement

The tree-level theory predicts m_top = v/√φ. Using v = 246.22 GeV (PDG) and φ = (1+√5)/2 = 1.61803...:

m_top^{tree} = v/√φ = 246.22 / √1.61803 = 246.22 / 1.27202 ≈ 193.6 GeV

The observed top quark pole mass is m_top^{pole} = 172.57 ± 0.29 GeV (PDG 2024).

Discrepancy: (193.6 - 172.57) / 172.57 ≈ 12.2% — call it ~11–12%.

This is large enough to require explanation. The most natural resolution is that the tree-level prediction is the MS-bar mass at some high renormalization scale μ_0, not the pole mass. Converting between MS-bar and pole mass requires:
1. QCD RG running: m_top^{MS}(μ) runs with the QCD beta function from μ_0 down to μ ~ m_top
2. QCD threshold correction: the pole mass differs from the MS-bar mass at μ = m_top by a QCD loop correction of order α_s/π

**Success condition:** After applying RG running and threshold corrections, the corrected prediction agrees with the pole mass to within ~2–3% (consistent with remaining theoretical uncertainties in the RS mass framework).

**Failure condition:** After all corrections, the discrepancy persists at >5%. This would escalate F4 and require identifying a new source of the discrepancy in the theory.

---

## §B — Known Inputs

| Input | Value | Status | Source |
|-------|-------|--------|--------|
| Higgs VEV | v = 246.22 GeV | `[✓]` | PDG 2024 |
| Golden ratio | φ = (1+√5)/2 = 1.618034... | `[✓ exact]` | Mathematical identity |
| Tree-level prediction | m_top^{tree} = v/√φ ≈ 193.6 GeV | `[D]` | Theory framework |
| Observed pole mass | m_top^{pole} = 172.57 ± 0.29 GeV | `[✓]` | PDG 2024 |
| Raw discrepancy | ~11–12% | `[✓ code-verified]` | Direct computation |
| α_s(M_Z) | 0.1180 ± 0.0009 | `[✓]` | PDG 2024 |
| QCD beta function b0 | b0 = (33 - 2n_f) / (12π), n_f=6 above m_top | `[T]` | Standard QCD |
| 1-loop pole-mass relation | m_pole = m_MS(μ) × [1 + (4/3)(α_s(μ)/π) + O(α_s²)] | `[T]` | Standard QCD |
| RS bulk mass parameters (quark sector) | P_q×L, Q_q×L (from F7 back-solve, Session 3) | `[D]` | Reference Core |
| Scale μ_0 at which tree-level formula applies | Unknown — this is the key question | `[⚠]` | To be determined |

---

## §C — Open Questions

1. **[OPEN] At what scale μ_0 does the tree-level prediction m_top = v/√φ apply?**
   The RS/AdS₅ framework sets mass parameters at the KK scale or the GUT scale. The tree-level formula gives the MS-bar mass at that scale. Identifying μ_0 requires understanding where in the RS geometry the top Yukawa coupling is generated.

2. **[OPEN] What is the RG-corrected prediction at μ = m_top?**
   Once μ_0 is identified, run m_top^{MS}(μ_0) down to μ = m_top using the 3-loop QCD beta function. This is a bounded, well-defined computation.

3. **[OPEN] What is the pole mass correction?**
   Apply the 1-loop (or 2-loop) QCD threshold correction to convert m_top^{MS}(m_top) to the pole mass. Compare to PDG.

4. **[OPEN] Is the residual discrepancy within theoretical uncertainty?**
   If residual <2–3%, F4 is resolved. If residual is 3–8%, flag for further investigation. If >8%, escalate F4.

---

## §D — Derivation Log

*(No derivations yet — workstream opened at Session 6 close. First derivations in Session 7 if primary task (WS-3875 CG) completes or is blocked.)*

---

## §E — Results

*(Empty — no results yet.)*

---

## §F — Status and Next Steps

**Overall status:** OPEN. Scoped and ready. Waiting on WS-3875 CG as primary task.

**First session steps (when this workstream becomes active):**

1. **Identify μ_0:** Determine the natural scale at which the RS framework generates the top Yukawa. Candidates: M_KK (KK scale), M_GUT (2.2×10¹⁶ GeV from self-consistent WZW crossing), M_Pl. Argue from the RS geometry which is most natural.

2. **Compute RG running:** Use 3-loop QCD beta function to run m_top^{MS}(μ_0) → m_top^{MS}(m_top). Print intermediate values at each decade of energy.

3. **Apply pole mass correction:** m_top^{pole} = m_top^{MS}(m_top) × [1 + (4α_s(m_top))/(3π) + ...]. Use α_s(m_top) from RG evolution of α_s(M_Z).

4. **Compare and classify:** Compute residual discrepancy. If resolved → log F4 as RESOLVED, migrate result to Reference Core. If not → escalate and document the failure.

**Estimated session cost:** One session (bounded computation — no novel derivations needed, primarily QCD standard results).
