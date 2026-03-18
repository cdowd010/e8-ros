# THEORY_EVOLUTION_GRAPH.md
## History of Major Theory Revisions

**Last updated:** 2026-03-18 (Session 6)

Records structural changes to the theory in reverse chronological order.

---

## Revision Log

### REV-010: α₂ [⚠] flags RESOLVED — b₂^WZW, +2.75, M_GUT all classified (2026-03-18)
**Change:** All three α₂ [⚠] flags resolved. b₂^WZW = +38/3 classified FITTED (36 Weyl doublets give 50/3; 30 doublets needed but unjustified; not derivable from E₈ field content). +2.75 corrections classified FITTED (no source identified). M_GUT = 5.7×10¹⁶ classified EXTERNAL INPUT (self-consistent WZW crossing gives 2.2×10¹⁶). Rows 3 (α₂) and 5 (sin²θ_W) downgraded Tier A → Tier C. Self-consistent prediction: 1/α₂ = 29.10 (1.6% off, 1 free param).
**Trigger:** Session 6 field content analysis, back-solving, scenario comparison.
**Impact:** The "showcase" 0.4% α₂ match revealed as partially fitted (2 free params). Genuine Tier A predictions are α_em (0.2%), α₁ (3.9%), α₃ (4.7%). Theory claims are now more honest and more credible. Self-consistent crossing version (1.6%, 1 param) is the new reported prediction.
**Downstream:** b₂^WZW derivation from first principles becomes a future optional upgrade (Priority 5). No kill conditions triggered.

### REV-009: WS-3875 mechanism SPECIFIED — CKM from (27̄,6) symmetric Yukawa (2026-03-18)
**Change:** CKM mechanism fully specified. KZ equation solved exactly. Cabibbo angle V_us ~ 0.2–0.3 predicted from (27̄,6) symmetric Yukawa component of 3875. (351,3) channel shown to preserve V_CKM = I (antisymmetric coupling, cannot generate mixing). KC-g upgraded from "mechanism unspecified" to "mechanism specified."
**Trigger:** Session 5 — OPE analysis, KZ equation, vacuum block decomposition, (351,3) channel analysis.
**Impact:** KC-g partial kill unchanged (248 sector fully killed), but 3875 path now has a concrete, testable mechanism. Suppression corrected from 1/31 to geometric √(162/4124).
**Downstream:** WS-3875 exact CG coefficient computation is now the #1 priority — mechanism is known, coefficient needs to be computed.

### REV-008: WS-3875 branching CONFIRMED — h(3875) corrected (2026-03-17)
**Change:** 3875 branching rule confirmed via SageMath. h(3875) corrected from h=1 (stored error) to h=48/31. Suppression mechanism clarified: ~1/31 geometric factor is √(dim(27̄,6)/dim(3875)) = √(162/4124). Dimension-uniqueness proof completed.
**Trigger:** Session 4 — SageMath output verified; dimension-uniqueness proof; E₈ rep theory.
**Impact:** KC-g partial kill unchanged. Suppression mechanism on firm footing. h(3875)=1 was a stored error now corrected in Reference Core.
**Downstream:** Mechanism specification (REV-009) could proceed on correct foundation.

### REV-007: WS-3875 scoped VIABLE — F7 exact back-solve complete (2026-03-17)
**Change:** WS-3875 (3875 of E₈ as CKM source) assessed as VIABLE — not ruled out by any known argument. F7 (parameter inconsistency) resolved via exact back-solve: P×L, Q×L parameters corrected to Tier-C-consistent values.
**Trigger:** Session 3 — 3875 decomposition analysis; PDG back-solve.
**Impact:** KC-g remains at partial kill. F7 moved to RESOLVED. Priority shifted to α₂ flags after CG work.
**Downstream:** WS-3875 became active workstream; α₂ flag resolution elevated to #3 priority.

### REV-006: Phase 2 re-evaluation complete — full theory audit (2026-03-17)
**Change:** Fresh-eyes assessment of all claims in Reference Core. Full dependency analysis. All §2–§7 entries re-derived and audited; every entry carries an audit tag. WS-3875 elevated to #1 priority. α₂ [⚠] flags elevated to #3. M_GUT flagged as hidden parameter. THEORY_SNAPSHOT_001 created.
**Trigger:** Session 2 — Phase 2 re-evaluation.
**Impact:** Priority reordering across the board. Exposed three ⚠ flags (b₂^WZW, +2.75, M_GUT) that had been implicit. KC-g partial kill confirmed with four independent proofs of V_CKM = I in 248.
**Downstream:** Sessions 3–6 all follow from the re-prioritization established here.

### REV-005: KC-g partial kill — 248 sector killed for CKM (2026-03-17)
**Change:** V_CKM = I proved exact in the 248 at renormalizable order. Four independent proofs. CKM mixing now requires the 3875 extension.
**Trigger:** WS-CKM2 closure; WS-CGC result.
**Impact:** CKM physics no longer obtainable from minimal (E₈)₁ field content. 3875 extension is the only surviving path. KC-g at partial kill.
**Downstream:** WS-3875 created. Theory viability now depends on 3875 evaluation.

### REV-004: α₃ demoted to Tier C (pre-ROS v2)
**Change:** α₃(M_Z) prediction requires M_T/M_GUT = 1.586 from doublet-triplet splitting. Three approaches to derive this ratio dynamically all failed. Value fitted.
**Trigger:** WS-α₃ Session 4 — all dynamical derivation approaches exhausted.
**Impact:** α₃ no longer a zero-parameter prediction. Tier A → Tier C.
**Downstream:** GUT-breaking sector model needed for future upgrade.

### REV-003: Paper 2 (G₂)₆ condensate framework introduced (pre-ROS v2)
**Change:** Mass degeneracy (F1) resolved by introducing (G₂)₆ condensates (symmetric S + adjoint A) that break SU(3)_fam and generate RS bulk mass profiles.
**Trigger:** F1 — degenerate heavy families in Paper 1.
**Impact:** Created Tier C mass predictions. Introduced P×L, Q×L parameters. Opened F7 (parameter inconsistency).
**Downstream:** F7 eventually resolved in Session 3.

### REV-002: n = 15 accepted as algebraic identity, not derived (pre-ROS v2)
**Change:** Multiple attempts to derive n=15 from the self-modeling map failed. Accepted as [D] status: algebraic identity with three independent coincidences but no dynamical derivation.
**Trigger:** WS-N15 stalled at foundational gap.
**Impact:** Tier B predictions remain [D]-tagged. M_W not promotable to Tier A.
**Downstream:** F3 remains archived/parked.

### REV-001: Original (E₈)₁ framework established (pre-ROS v2)
**Change:** Core framework: (E₈)₁ holomorphic CFT → self-referential boundary → subfactor → Fibonacci → conformal embedding → SM. Gauge couplings derived.
**Trigger:** Initial theoretical construction.
**Impact:** Foundation of all subsequent work.

---

*Add entries when the theory undergoes a structural change (new mechanism, killed pathway, reclassification, major correction). Minor numerical corrections do not qualify.*
