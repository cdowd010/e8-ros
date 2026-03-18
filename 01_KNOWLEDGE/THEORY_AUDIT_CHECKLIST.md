# THEORY_AUDIT_CHECKLIST.md
## Theory-Specific Audit Targets

**Location:** `01_KNOWLEDGE/`
**Last updated:** 2026-03-18 (created at ROS v3.2 — populated from sessions 1–6 analysis)
**Next audit due:** Session 15

This file contains the **theory-specific targets** for each step of the Theory Audit (§12 of the Session Briefing). The Briefing contains the universal *procedure*; this file contains the current *content* — which specific claims, predictions, kill conditions, and literature areas to focus on.

**Update this file at the close of every theory audit.** The targets should reflect the theory's current most exposed vulnerabilities, not its state at the time the checklist was last written. A checklist that isn't updated after each audit is worse than no checklist — it directs attention to problems that have already been resolved while letting new ones accumulate.

---

## §A — Highest-Priority [P] Claims to Scrutinize (Step 1)

These are the `[P]` (physical/heuristic argument) claims in the logical chain that carry the most downstream weight and have received the least scrutiny. Ordered by risk.

### P-1: Computational faithfulness → selects φ² [FKLW 2002]
**Risk level:** CRITICAL — the entire φ chain descends from this single claim
**What depends on it:** φ² Jones index → Fibonacci MTC → Higgs = τ anyon → m_H/M_W = φ → Yukawa = 1/√φ → mass hierarchy suppression
**Audit questions:**
- What is the strongest alternative selection criterion, and does it give a different Jones index?
- Has FKLW 2002 been read carefully and critically, or just cited? Is the specific "computational faithfulness" argument present in that paper, or is this an interpretation?
- Is there a competing argument in the literature for a different selection principle?
- Could the framework work with a different Jones index? What would break?

### P-2: Self-model = subfactor (Route 3 is corollary only)
**Risk level:** HIGH — foundational to the whole self-referential construction
**What depends on it:** Everything downstream of the subfactor identification
**Audit questions:**
- Routes 1 (QECC) and 2 (Wiesbrock) are independent — audit whether they are genuinely independent or share a hidden common step
- Route 3 being a corollary means only two truly independent justifications exist. Is that sufficient?
- Is there a published critique of using subfactors to formalize self-reference?

---

## §B — Highest-Priority [D] Claims to Scrutinize (Step 1)

These `[D]` (derived) claims may contain steps that are actually assumptions in disguise.

### D-1: Einstein's equations via Jacobson with G = ℓ²_Pl/ln 12
**Risk level:** HIGH
**Audit question:** Is G = ℓ²_Pl/ln 12 derived from the framework, or is it an identification/assumption? If the latter, this `[D]` should be reclassified as `[P]`.

### D-2: Forced symmetry breaking from tachyonic τ (h = 2/5 → m² < 0)
**Risk level:** HIGH — this is KC-d
**Audit question:** Has h = 2/5 actually been verified to give m² < 0 in the dS context? This is a computable check that has not been done. Until it is, this `[D]` is carrying weight it hasn't earned.

### D-3: Gauge couplings at M_Pl from WZW levels
**Risk level:** MEDIUM
**Audit question:** Is this a derivation (the couplings follow necessarily from the WZW structure) or an identification (we identify the WZW coupling with the gauge coupling by assumption)? The boundary between `[D]` and `[P]` here needs to be made explicit.

### D-4: Seesaw and doublet-triplet splitting from Casimir ordering
**Risk level:** MEDIUM
**Audit question:** What exactly is the Casimir ordering argument? Is the ordering of mass scales a genuine derivation from first principles, or a consistency check against a desired outcome?

---

## §C — Predictions to Re-benchmark (Step 2)

All predictions in the Reference Core should be re-benchmarked at each audit. The following are flagged for extra attention due to fast-moving experimental inputs or known measurement issues.

| Prediction | Formula | Why flagged | PDG quantity to re-look up |
|-----------|---------|-------------|---------------------------|
| m_top (tree level) | v/√φ | PDG top mass updated frequently; QCD corrections pending (WS-F4) | m_top pole mass |
| m_H/M_W ratio | φ | Both measured precisely; ratio has changed slightly over time | m_H, M_W |
| 1/α_em(M_Pl) | 4π × K_em | Depends on α_em(M_Z) RG running | α_em(M_Z) |
| 1/α₁(M_Z) | 20π/3 + Δ | Depends on hypercharge normalization convention | α₁(M_Z) |
| 1/α₃(M_Z) (Tier C) | 16π − Δ + threshold | M_T/M_GUT fitted; sensitive to αs(M_Z) precision | α_s(M_Z) |
| M_W (Tier B) | M_Pl/12¹⁵ | Subject to ongoing experimental controversy (CDF vs LEP vs LHC) | M_W current PDG consensus |
| m_t/m_u, m_b/m_d (Tier C) | RS profiles | Light quark masses (m_u, m_d) carry large uncertainties | m_u, m_d, m_s current PDG |
| τ(proton) | M_GUT⁴/(...) | M_GUT is not self-consistently derived; experimental bound tightening | Current proton lifetime bound |

---

## §D — Kill Condition Proximity Assessment (Step 4)

Current status and proximity estimate for each kill condition. Update after each audit.

| KC | Description | Current status | Proximity | How to trigger | How to clear |
|----|-------------|---------------|-----------|---------------|-------------|
| KC-a | Rank-3+ MTC with d=φ found | Not triggered | Low — Jones-Ocneanu classification is mature, but literature should be checked | Find a rank-3+ MTC with a simple object of quantum dimension φ | N/A (would be fatal) |
| KC-b | Jones index argument circular | Not triggered | Unknown — never explicitly walked through | Demonstrate that any step in the self-model → subfactor → Jones index chain assumes its conclusion | Demonstrate full independence of each step |
| KC-c | Wrong EM charges from embedding | Not triggered | Very low — embedding arithmetic verified | Find an error in the conformal embedding central charge computation | N/A |
| KC-d | h=2/5 maps to non-tachyonic field | Not triggered | **UNKNOWN — never computed** | Verify h=2/5 in the dS context; if m²≥0, trigger | Compute explicitly: confirm m²<0 |
| KC-e | dS/CFT inconsistency with Jacobson | Not triggered | Unknown — depends on dS/CFT status | Demonstrate that a c=8 holomorphic CFT on a dS horizon is inconsistent with Jacobson thermodynamics | Literature review + explicit check |
| KC-f | Embedding arithmetic error | Not triggered | Very low — verified by code | Find a computational error in central charge arithmetic | N/A |
| KC-g | No CKM from E₈ at any rep order | **PARTIAL KILL** | HIGH — the only surviving path is (27̄,6) in 3875 | Exact CG coefficient gives V_us far outside [0.1, 0.5] | Exact CG gives V_us consistent with 0.225 + RS profiles reproduce V_cb, V_ub |
| KC-NEW | Alternative embeddings yield different couplings | Not triggered | Low — embedding is unique by level-1 classification | Find an alternative level-1 conformal embedding that gives SM gauge group with different coupling predictions | N/A |

**Flagged for explicit computation at next audit:** KC-d (h=2/5 tachyonic check — computable, never done).

---

## §E — Literature Search Topics (Step 6)

Topics to run targeted web searches on at each theory audit. Update this list after each audit to reflect the theory's current most exposed foundations.

### High priority (check at every audit)
- **Modular tensor categories at Jones index φ²** — any new classification results beyond Jones-Ocneanu? Any rank-3+ MTC with d=φ found?
- **(E₈)₁ WZW model uniqueness** — any new results on the uniqueness or structure of the (E₈)₁ holomorphic CFT? Any challenge to the c=8 lattice classification?
- **dS/CFT correspondence** — current theoretical status. Is the Jacobson thermodynamic derivation of Einstein's equations still considered valid in dS? Any new consistency results or failures?

### Medium priority (check every other audit)
- **Holographic derivation of gauge couplings** — are there competing frameworks that make similar predictions from different principles? How does this theory's approach compare?
- **Computational complexity and physical law** — any new work on "computational faithfulness" or similar selection principles for physical laws?
- **Subfactor theory and self-reference** — any new mathematical results on using subfactors to formalize self-modeling or self-reference?

### Lower priority (check when relevant)
- **E₈ phenomenology and GUT models** — any competing models that make predictions from E₈ structure? Any predictions that conflict with or corroborate this theory's?
- **Randall-Sundrum mass hierarchy models** — updates to RS phenomenology; new constraints on bulk mass parameters from LHC data

---

## §F — Parked Failure Review Targets (Step 7)

Parked failures that require explicit re-evaluation at each theory audit to determine whether they remain correctly classified.

### F3 — n = 15 not derived
**Parked since:** Pre-ROS v2
**Parked because:** Self-modeling map S not defined precisely enough to derive tower termination
**Re-evaluate:** Is there any new mathematical work on self-referential maps, fixed-point theorems, or termination conditions that could unblock this? Has any work in other areas (e.g., n=15 appearing in a new context) provided a new derivation route?
**Close condition:** If no path forward identified after 3 consecutive theory audits, formally close as "will not resolve within current framework."

### F5 — α₃ dynamical origin of M_T/M_GUT
**Parked since:** WS-α₃ closure (pre-ROS v2)
**Parked because:** Three dynamical approaches all failed; GUT-breaking sector model required
**Re-evaluate:** Has any new insight into the GUT-breaking sector emerged from other workstreams? Is M_T/M_GUT derivable from the 3875 mechanism or RS geometry once WS-3875 closes?
**Close condition:** If WS-3875 completes and provides no new leverage on this, and no other path is identified, formally close.

### F6 — DM abundance
**Parked since:** Pre-ROS v2
**Parked because:** Requires condensation dynamics not yet developed
**Re-evaluate:** Is this genuinely within reach of the current framework, or is it fundamentally outside its scope? The (G₂)₆ condensate framework (Paper 2) may be the natural home for DM predictions — has this connection been explored?

---

## §G — Audit History

| Audit # | Session | Date | Overall verdict | Key findings | Next audit scheduled |
|---------|---------|------|----------------|-------------|---------------------|
| — | — | — | — | No audits yet | Session 15 |

*Add one row per completed theory audit.*
