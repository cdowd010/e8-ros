# PROTOCOL_TheoryAudit.md
## Theory Audit — Full Procedure
*Research Operating System v3.3 | Upload only for theory audit sessions*

---

A theory audit is a structured attempt to **stress-test and potentially falsify** the theory — not to advance it. The mindset is that of a hostile referee who has been given access to all working files. The goal is to find what is weak, wrong, or overstated before a journal reviewer or experimentalist does.

**Always use Opus for a theory audit.** This is the highest-stakes reasoning in the project. A wrong derivation in a theory audit that gets written into THEORY_HEALTH and RESOLVED_KNOWLEDGE could silently corrupt the research direction for many sessions.

**Duration:** Plan for a full session. A rushed theory audit is worse than no audit — it creates false confidence.

---

## §A — Pre-Audit Preparation

Before beginning the audit, read and have in context:

- `E8_Reference_Core.md` — the full prediction ledger and logical chain
- `THEORY_HEALTH.md` — current dashboard (the baseline to compare against)
- `RESOLVED_KNOWLEDGE.md` — all settled results
- `RESEARCH_DEPENDENCY_GRAPH.md` — the full dependency map
- `FAILURE_LEDGER.md` — all open and resolved failures
- `HYPOTHESIS_TREE.md` — all active and rejected hypotheses
- `CONTRADICTION_TRACKER.md` — all open and resolved contradictions
- `THEORY_AUDIT_CHECKLIST.md` — the current theory-specific audit targets (highest-risk claims, KC proximity, PDG benchmarks, literature topics)

Do not begin any audit step without these files in context. An audit performed from memory is not an audit.

**Before reading any of these files**, write a one-paragraph cold-start answer to:

> *"If a hostile referee were handed this project today with no prior context, what would their first three objections be?"*

Write the answer before reviewing any files. Context contaminates adversarial perspective. This paragraph anchors the audit's critical posture. Log it in `META_RESEARCH_LOG.md` as the opening entry for this audit.

---

## §B — Step 1: Logical Chain Integrity

The logical chain in Reference Core §1 is the spine of the entire theory. This step audits each link and checks that the chain is complete and correctly classified.

### B.1 — Full chain reconstruction (mandatory)

Do not rely on the stored logical chain as authoritative. Reconstruct it independently:

1. Start from the axioms. List them explicitly — if an axiom is not named as such somewhere, it is a hidden axiom and must be surfaced.
2. For each subsequent claim, identify which prior claims it directly depends on. Build the dependency graph from scratch.
3. Compare the reconstructed graph to the stored one in `RESEARCH_DEPENDENCY_GRAPH.md`. Any discrepancy is a finding — either the stored graph is wrong, or an implicit dependency has been missed.
4. Every logical step in the reconstructed chain must carry a tag. Any step that is not tagged `[P]`, `[D]`, or `[T]` is an **untagged hidden assumption** — flag it `[⚠ UNTAGGED ASSUMPTION]` and require resolution before the audit closes.

The goal is to find steps that were treated as obvious transitions but are actually assumptions. These are the most dangerous elements of the logical chain because they are invisible to routine checking.

### B.2 — Per-claim audit

**For every `[P]` claim:**
- State precisely what would have to be true for this claim to be false.
- Is there a published result or computation that could confirm or refute it?
- Has anything been derived since this claim was made that bears on it?
- Is there a stronger alternative justification that hasn't been pursued?
- If it has not been revisited in 10+ sessions, treat it as unreviewed and flag it `[⚠ UNREVIEWED P-CLAIM]`.
- Is this claim **load-bearing** (downstream predictions depend on it) or **decorative** (present in the framework but nothing downstream uses it)? Decorative `[P]` claims should be pruned or promoted to load-bearing status. See the theory shrinkage test (§H.2).
- Consult `THEORY_AUDIT_CHECKLIST.md` for the current highest-priority `[P]` claims to scrutinize.

**For every `[D]` claim:**
- Are the stated assumptions still the minimal set, or have later results allowed some to be strengthened?
- Are all dependencies explicitly listed? Check for hidden inputs that have accumulated since the derivation was first written.
- Is there a boundary case where this `[D]` should actually be `[P]` — i.e., does the derivation contain an unjustified step that is effectively an assumption?
- Consult `THEORY_AUDIT_CHECKLIST.md` for the current highest-priority `[D]` claims to scrutinize.

**For every `[T]` claim:**
- Is the cited source correct and accessible?
- Is the specific result from that source the one being used, or a looser paraphrase?
- Has the cited result been superseded or qualified in the literature since citation?

### B.3 — Internal consistency test

The logical chain must not only be derivationally valid — the axioms must be **mutually consistent** under all the constraints the theory places on them. This is a separate check from whether individual predictions match experiment.

For each axiom, identify every constraint the theory places on it (directly or downstream). Ask: can all constraints be simultaneously satisfied? If two constraints from different parts of the theory jointly overconstrain the same axiom, flag `[⚠ INTERNAL TENSION: axiom X overconstrained by constraints Y and Z]`.

This check is most important when the theory has been extended since the last audit — new mechanisms can introduce constraints that conflict with old ones silently.

---

## §C — Step 2: Prediction Accuracy Review

PDG values drift. Experimental bounds tighten. A prediction that was 2% off two years ago may be 4% off now, or may now be excluded.

### C.1 — Re-benchmark against current PDG

For every prediction in the ledger:

- Look up the current PDG value for every experimental input used in predictions. Note any that have changed since the last audit date.
- Recompute every match percentage using current PDG values, not stored ones.
- If any Tier A or Tier B prediction has degraded past 5%, flag for investigation.
- If any Tier C prediction has degraded to excluded territory (>3σ from current PDG), escalate to active failure.
- Note any experimental inputs that carry active measurement controversy — these may shift significantly between audits.

Consult `THEORY_AUDIT_CHECKLIST.md` for the specific predictions to re-benchmark and any known measurement controversies relevant to the current theory state.

### C.2 — Retrodiction vs. prediction separation

Predictions made before the relevant experimental value was known are fundamentally different from predictions fitted or tuned after the value was known. These must be tracked separately and never conflated in the scorecard.

For every prediction in the ledger:
- Was this prediction made before or after the relevant PDG value was in scope? Tag each as `[PRED: pre-data]` or `[RETRO: post-data]`.
- If `[RETRO]`: was any parameter tuned (even partially) to improve this match? If so, it is not a genuine retrodiction — it is a fit. Tag `[FIT]` and downgrade tier accordingly.
- The honest scorecard in §H.1 must count only `[PRED: pre-data]` results as genuine predictions.

### C.3 — Correlation audit

Two predictions are not independent if they share a common parameter or intermediate result. Overcounting independent successes is a form of implicit p-hacking.

- List every pair of predictions that share a common fitted parameter, `[P]` claim, or derived intermediate.
- For each such pair, count them as a single independent test, not two.
- Update the "number of independent predictions" figure in `THEORY_HEALTH.md` to reflect the correlation-corrected count.

---

## §D — Step 3: Tier Inflation Audit

Over many sessions, claims tend to silently drift upward in confidence. This step actively pushes back.

### D.1 — Current tier assignments

**For every Tier A claim:**
- List every input that enters the prediction. Is each input strictly derived from the axioms, or does any rely on an external input, a fitted parameter, or a `[P]` assumption?
- If ANY input is not strictly derived → the claim does not qualify for Tier A. Downgrade.
- Apply the zero-parameter test: could this prediction have been made before any experimental data was seen? If not, it is not Tier A.

**For every Tier B claim:**
- Identify the specific `[D]` or `[T]` dependency that keeps it out of Tier A. Is that dependency still the binding constraint, or has something changed?
- Is there a path to derive that dependency that hasn't been explored yet?

**For every Tier C claim:**
- Count the free parameters explicitly. Is the stated parameter count accurate?
- Is this prediction actually predictive (makes a testable claim given the fitted parameters), or is it just a fit?

### D.2 — Tier A graveyard audit

The `THEORY_AUDIT_CHECKLIST.md` maintains a **Tier A graveyard**: a log of every claim that was ever Tier A and was subsequently downgraded, with the reason. This graveyard must be reviewed at every theory audit.

- Are there patterns in the graveyard? (E.g., claims consistently downgraded because of hidden `[P]` dependencies — this suggests the zero-parameter test is not being applied rigorously enough at promotion time.)
- Has any claim been re-promoted to Tier A after being in the graveyard? If so, is the re-promotion justified by a genuine new derivation, or by a softening of standards?

If no graveyard exists yet in `THEORY_AUDIT_CHECKLIST.md`, create it now. Populate it from the audit history.

### D.3 — Grandfathering check

Claims that achieved Tier A in early sessions (before the current zero-parameter standard was fully established) may have been promoted under a less strict criterion. Do not accept early Tier A status as valid by default.

- Identify every Tier A claim that was promoted before session 10 (or before the last major standards revision — check `META_RESEARCH_LOG.md` for ROS version history).
- Re-audit each against the current zero-parameter standard from scratch. Prior Tier A status is not evidence of current Tier A status.
- Downgrade any that do not pass the current standard. Log as `[✗ CORRECTED: Tier A → Tier B, reason: grandfathering audit, session N]`.

### D.4 — Tier inflation red flags

- A claim upgraded to Tier A in a previous session without a full zero-parameter audit
- A `[D]` claim where the derivation is in an archived workstream that hasn't been re-examined in 10+ sessions
- Any claim where the match is suspiciously good (< 0.5%) — this is more likely to indicate hidden fitting than genuine prediction
- A claim that has survived multiple audits without ever having its dependencies explicitly re-verified

---

## §E — Step 4: Kill Condition Stress Test

For each kill condition, answer two questions: (1) is it well-defined enough to actually trigger? (2) how close is the theory to triggering it?

### E.1 — Per-KC stress test

**For each non-triggered KC:**
- Identify the specific computation or observation that would trigger it.
- If no such computation can be named, the kill condition is not well-defined — rewrite it with a concrete trigger.
- Estimate how far the theory currently is from the trigger threshold. "Not close" is not an acceptable answer — quantify.

**For each partially-triggered KC:**
- What exact result would convert it to a full kill?
- What exact result would clear it entirely?
- Are the success/failure thresholds in the relevant workstream still the right ones?

### E.2 — KC completeness check (new at each audit)

The existing kill conditions catch only the failure modes that were anticipated when they were written. This step asks whether there are failure modes with no KC coverage.

For each major mechanism in the theory:
1. What is the single result that would most directly falsify it?
2. Is there a kill condition that covers that result?
3. If not — should there be? Propose a new KC with a concrete trigger condition and bring it to Chris for approval. Do not add KCs unilaterally.

### E.3 — Near-miss log

The `THEORY_AUDIT_CHECKLIST.md` maintains a **near-miss log**: results that came within 2× of triggering a kill condition, even if they didn't trigger it. Review and update this log:

- Have any new results come close to a kill condition since the last audit?
- Has any near-miss been followed up with a workstream to understand the proximity?
- A near-miss that appears in two consecutive audit logs without resolution should be escalated to a formal workstream.

---

## §F — Step 5: Parameter Budget

A theory with no free parameters is a claim. Verify it explicitly.

### F.1 — Full parameter inventory

List every external input the theory uses:
- Fundamental constants taken as given (e.g., ℏ, c, G)
- Parameters fitted to data (e.g., M_GUT tuned to match α₂)
- Parameters derived from first principles within the theory
- Parameters assumed without derivation (`[P]` claims with numerical content)

For each: state its value, its provenance, and its tag.

### F.2 — Zero-parameter claim audit

The theory's central claim is that it has zero free parameters. Test this explicitly:

- Count parameters in category (b) above — fitted to data. Each one is a free parameter.
- Count parameters in category (d) above — assumed. Each one is a hidden free parameter.
- The true parameter count is (b) + (d). State this number explicitly.
- If the count is nonzero, the "zero free parameters" claim must be qualified. Downgrade any predictions that depend on fitted parameters.

### F.3 — Parameter budget statement

The audit report must contain an explicit parameter budget:

```
True free parameter count: N
  Fitted to data: [list]
  Assumed [P]: [list]
  External inputs: [list]
Predictions dependent on fitted parameters: [list]
Predictions with fully derived inputs: [list]
```

---

## §G — Step 6: Literature and Experimental Exposure

### G.1 — Literature scan

Consult `THEORY_AUDIT_CHECKLIST.md` for the current list of literature topics that are most relevant to the theory's exposed foundations. For each:

- Has there been new work in this area since the last audit?
- Does any new result strengthen or weaken a key assumption?
- Are there papers that directly address the mechanisms the theory relies on?

Do not do a comprehensive literature review — focus on the specific topics flagged in the checklist as highest exposure.

### G.2 — Experimental pipeline check

For each active Tier A and Tier B prediction:
- Is there a running or planned experiment that will test this prediction within the next 5 years?
- If yes: what precision will it reach? Will it be sufficient to confirm or exclude the prediction?
- Update `THEORY_AUDIT_CHECKLIST.md` with any upcoming experiments identified.

---

## §H — Step 7: Failure Ledger Review

### H.1 — Open failure status check

For each open failure in `FAILURE_LEDGER.md`:
- Has the status changed since the last audit (partially resolved, new information, new workstream opened)?
- Is the stated unblocking condition still accurate, or has the situation evolved?
- Is the failure still genuinely open, or has it been de facto resolved without being formally closed?

For parked failures:
- Is there a concrete unblocking condition stated? If not, is this failure genuinely parked or de facto closed?
- Has any work in other areas created a new path to resolution?
- Has the failure been parked long enough that it should either be formally closed or have a workstream opened?

For resolved failures:
- Has the resolution held up under subsequent work? A "resolved" failure whose resolution was later undermined is a silent bug.

### H.2 — Failure clustering analysis

Failures are not always independent. Review the full failure ledger for clusters:

- Do any failures share a common root cause? (E.g., multiple failures all downstream of the same `[P]` claim, or all arising from the same mechanism.)
- If a cluster is identified: is the common root cause itself a kill condition or a hypothesis? It should be.
- A cluster of 3+ failures with the same root cause constitutes a structural vulnerability — it must be addressed as a single problem, not as separate open items.

Log any clusters found in the audit report. A cluster that has appeared in two consecutive audits without resolution should be escalated to a formal kill condition.

---

## §I — Step 8: Theory Scope and Honesty Assessment

This step is deliberately adversarial. The goal is to identify overreach.

### I.1 — Honest scorecard

Construct the most conservative possible version of the theory's predictive record:

- Count only Tier A predictions where every input is strictly derived (no `[P]` dependencies, no fitted parameters upstream)
- Among those, count only `[PRED: pre-data]` predictions (§C.2) — not retrodictions, not fits
- Apply the correlation-corrected independent count (§C.3)
- For those predictions, what is the median match percentage?
- Estimate the probability that this match record occurred by chance. (Order of magnitude estimate — not rigorous, but informative.) Include the look-elsewhere correction: if the theory made N total predictions (before filtering) and k passed after filtering, the k successes are drawn from N attempts.

This scorecard must be stated explicitly in the audit report and in `THEORY_HEALTH.md`. The uncorrected scorecard (all predictions at face value) may also be stated, but the corrected scorecard must appear first.

### I.2 — Theory shrinkage exercise

The goal is to identify which `[P]` claims are genuinely load-bearing vs. which could be removed without collapsing the theory's predictive record.

For each `[P]` claim in the logical chain:
1. Remove it (hypothetically). Which predictions lose their derivation path?
2. If removing it collapses 0 predictions: it is **decorative** — either derive it properly or remove it. A decorative `[P]` claim gives the theory false depth.
3. If removing it collapses multiple predictions via a single dependency: it is **high-leverage**. These are the highest-priority derivation targets. Log them in `THEORY_AUDIT_CHECKLIST.md` as `[HIGH-LEVERAGE P-CLAIM: derive first]`.
4. Prune all decorative `[P]` claims from the framework, with a note on why they were removed. Simpler theories are stronger theories.

### I.3 — Scope creep check

- Count the `[T]` vs `[D]` vs `[P]` tags in the logical chain. Is the ratio of proven to assumed claims moving in the right direction over time?
- Has the framework been extended to explain new phenomena without sufficient justification? New `[P]` claims should be scrutinized.
- Are there claims in the framework that are not in the logical chain but are implicit in predictions?

### I.4 — Alternative model comparison

A theory audit that never asks "is there a simpler theory that makes the same predictions?" is not adversarial enough.

For each cluster of predictions:
1. Is there a model with fewer axioms or fewer parameters that makes the same predictions to the same precision?
2. Even a sketch of the most competitive alternative is valuable. Name it, state its parameter count, and state whether it is excluded or not.
3. If no alternative has ever been formally considered, that is a gap. The audit report must include at least one named alternative for each major prediction cluster.

This is not a request to build a competing theory — it is a request to confirm that the existing theory has been compared against its alternatives, even informally.

### I.5 — Experimental exclusion audit

For each prediction:
1. What future experimental result would specifically exclude it (not just "falsify the theory" in general, but exclude this prediction at this precision)?
2. What experiment or analysis would produce that result? Name the experiment, the observable, and the precision required.
3. If no such experiment can be named, the prediction is not testable at present. It should be tagged `[⚠ NOT CURRENTLY TESTABLE]` and must not be counted in the honest scorecard (§I.1).

Predictions that are untestable are not worthless — they may become testable — but they must be clearly labelled and not inflating the apparent predictive power of the theory.

### I.6 — Fine-tuning assessment

For each fitted parameter:
1. What is its value?
2. Is this value natural — i.e., does dimensional analysis suggest it should be roughly this size, or is it many orders of magnitude away from the naive estimate?
3. If fine-tuned: is there a theoretical explanation for the tuning, or is it unexplained?

Fine-tuning is not a kill condition, but unexplained fine-tuning is a flag `[⚠ FINE-TUNING: parameter X, expected O(N), actual O(M)]`. Multiple fine-tuning flags without explanations are a structural weakness.

### I.7 — The adversarial paragraph

Write a one-paragraph summary of the theory's weaknesses as a hostile referee would. This paragraph should be uncomfortable to write. If it isn't, the audit has not been adversarial enough. Log this paragraph in `META_RESEARCH_LOG.md`. It must appear verbatim in the audit report.

The paragraph must address at minimum:
- The weakest `[P]` claim in the logical chain, and why it is weak
- The most questionable tier assignment, and what a skeptic would say about it
- The most important prediction that has not yet been made but should be
- The most plausible way the entire framework could be wrong at a structural level

---

## §J — Mandatory Audit Output

Every theory audit session must produce all of the following before closing:

1. **Updated `THEORY_HEALTH.md`** — full replacement with post-audit metrics. Every metric must change or be explicitly confirmed unchanged with reasoning. The honest scorecard (§I.1) and parameter budget (§F.3) must appear explicitly.
2. **New `THEORY_SNAPSHOT`** — even if the theory hasn't changed structurally. The snapshot records the theory's state at the audit date as an independent baseline.
3. **Audit report in `META_RESEARCH_LOG.md`** — structured entry containing:
   - Session number and date
   - Pre-audit cold-start adversarial paragraph (§A)
   - Summary of what was checked and what was found
   - Logical chain reconstruction findings (§B.1): discrepancies, untagged steps
   - Internal consistency findings (§B.3): any overconstrained axioms
   - Prediction accuracy summary: any degradations, exclusions (§C)
   - Retrodiction/prediction separation results (§C.2)
   - Correlation-corrected independent prediction count (§C.3)
   - All tier changes, with justification
   - Grandfathering check results (§D.3)
   - Tier A graveyard update (§D.2)
   - All new `[⚠]` flags raised
   - All `[⚠]` flags resolved
   - Parameter budget (§F.3)
   - Near-miss KC log update (§E.3)
   - New KCs proposed (§E.2), pending Chris's approval
   - Any KCs proposed for removal or retirement (with reasoning)
   - Failure clustering findings (§H.2)
   - Theory shrinkage results: decorative `[P]` claims pruned, high-leverage targets identified (§I.2)
   - Alternative model comparison (§I.4)
   - Experimental exclusion audit (§I.5): any predictions tagged `[⚠ NOT CURRENTLY TESTABLE]`
   - Fine-tuning flags (§I.6)
   - The adversarial one-paragraph weakness summary (§I.7)
   - Honest scorecard (§I.1): corrected and uncorrected versions
   - Recommendation: is the theory stronger or weaker than at the last audit? Why?
4. **Updated `FAILURE_LEDGER.md`** — any status changes from Step 7 (§H), including any newly identified failure clusters
5. **Updated `E8_Reference_Core.md`** — any tier changes, corrections, or new flags; any `[⚠ NOT CURRENTLY TESTABLE]` tags added; `[RETRO]` / `[PRED]` / `[FIT]` tags added or corrected
6. **Updated `THEORY_AUDIT_CHECKLIST.md`** — refreshed with:
   - New highest-risk `[P]` and `[D]` targets
   - Current KC proximity estimates and near-miss log
   - Updated PDG benchmark list (which predictions are now most at risk)
   - Updated literature topics (theory's current most exposed foundations)
   - Updated Tier A graveyard
   - Updated high-leverage `[P]` claim list from theory shrinkage exercise
   - Updated parameter budget figures
   - Audit history table updated with this audit's findings
   The checklist must reflect the theory's state *after* this audit, not before it.
7. **Next audit date** — stated explicitly in `CONTEXT_SNAPSHOT.md §E`

---

*This file contains the theory audit procedure only. Schedule, triggers, and upload instructions are in `E8_Session_Briefing.md §12`.*
