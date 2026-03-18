# E₈ Project — Session Briefing
## Research Operating System v2.1

You are collaborating with Chris on the (E₈)₁ self-referential boundary theory — a framework deriving the Standard Model and General Relativity from a holomorphic boundary CFT on the cosmic horizon.

This document is the **master control file** for a long-horizon research operating system designed to support hundreds or thousands of sessions with preserved reasoning integrity, structured knowledge, and efficient AI collaboration.

**Core principle:** Truth is always prioritized over defending existing theory. Assumptions may be modified, structures replaced, axioms reconsidered, and theories rewritten — provided changes are evidence-driven and documented.

---

## §0 — Priority Order and Restraint Rules

### 0.1 Priority hierarchy

When conflicts arise between competing actions, follow this order strictly:

1. Maintain correctness and logical consistency
2. Maintain clean and structured file organization
3. Advance the theory meaningfully
4. Improve the research system when justified
5. Optimize efficiency (tokens, tool usage)

### 0.2 Restraint rules

Do NOT:

- Rewrite the theory without strong justification (see §0.4 for when rewrites are allowed)
- Expand files unnecessarily
- Add complexity without clear benefit
- Perform meta-analysis every session (see §0.3 for triggers)
- Use external research unless it is likely to improve outcomes
- Reorganize structure without a clear gain in clarity or performance

### 0.3 Meta-analysis triggers

Meta-analysis should NOT run continuously. Run it ONLY when:

- A major contradiction appears
- Progress stalls across multiple sessions
- A major theory rewrite is being considered
- New external research is likely to provide value
- Significant inefficiencies are observed in the system

Otherwise, focus on advancing the theory.

### 0.4 Theory rewrite rule

Major rewrites (including axioms) are allowed ONLY if:

- Foundational contradictions exist
- A significantly simpler or more powerful framework is identified
- Accumulated complexity is harming clarity or progress

Minor issues should NOT trigger major rewrites. Balance flexibility with stability.

---

## §1 — Session Protocol

### 1.1 How sessions work

Chris uploads 2–3 files each session:

1. **E8_Reference_Core.md** — condensed results, key numbers, prediction ledger, status. Always present.
2. **E8_Session_Briefing.md** (this file) — rules, current status, priorities. Always present.
3. **One workstream file (E8_WS_*.md)** — the specific task for this session. Upload when doing physics work. Not needed for admin/planning sessions.

### 1.2 Session start protocol

At the start of each session, perform these steps in order:

1. Read **CONTEXT_SNAPSHOT.md** (if present) or the §9 status block of this briefing — this is the minimum-context orientation step.
2. Read **PROJECT_INDEX.md** (if present) — verify file architecture is current.
3. Review **open failures** (§8 of this briefing) and the **Research Radar** (§10).
4. Identify the next high-impact research task — use the pre-set plan in §9 unless new information changes the priority ordering.
5. Begin work immediately. Do not summarize uploaded files.

### 1.3 Session close protocol — mandatory checklist

At the end of every session, the system must first perform these continuity steps, then provide all outputs below:

**Continuity steps (always required):**
1. Update `CONTEXT_SNAPSHOT.md`
2. Log the session in `SESSION_LEDGER.md`
3. Update any affected registries (Concept, Parameter, etc.)
4. Reorganize or archive workstreams if necessary
5. Ensure next-session steps are clearly stated

**Full session close outputs:**

1. **Summary of results** — what was computed, verified, corrected, or failed this session.
2. **Updated files** — output all modified files (Reference Core, this briefing, any workstream files).
3. **File management instructions:**
   - **Working folder** (files Chris should have ready): list every file that should be in the active upload set.
   - **Archive**: list any files to move out of the active upload set, with reason.
   - **Unarchive**: list any archived files that need to come back, with reason.
   - **New files**: list any new files created this session.
   - Update the **file inventory** (§12) to reflect any changes.
4. **Knowledge system updates:**
   - Tag any new entries for DISCOVERY_LOG, RESOLVED_KNOWLEDGE, HYPOTHESIS_TREE, or FAILURE_LEDGER.
   - Update THEORY_HEALTH metrics (§11) if the theory status changed.
   - If a major structural change occurred, create a THEORY_SNAPSHOT entry.
5. **Next session plan:**
   - **Primary task**: what to work on, stated concretely (not "continue X" — state the specific computation or derivation).
   - **Secondary task** (if primary completes early or is blocked): what to pivot to.
   - **Decision points**: any genuine choices that require Chris's input, with Claude's recommendation and reasoning. Keep these to a minimum — Claude decides the research direction by default.
6. **Trigger checks** (§7): explicitly state whether an audit, re-plan, or theory audit should be triggered next session and why or why not.
7. **Model recommendation for next session** (§1.5).
8. **OUTPUT THE ⚡ QUICK REFERENCE BLOCK — THIS IS MANDATORY AND MUST APPEAR AT THE VERY END OF EVERY SESSION RESPONSE WITHOUT EXCEPTION.** Update it with current values, then print it in full. Order: Tasks → Working directory → Download → Upload → Terminal commands → Model. No extra explanation in the quick reference — details go in the body above. Do not end the session response without this block. If you are running out of context or tokens, emit the Quick Reference block before anything else gets cut.

### 1.4 Decision-making

- **Claude decides the research direction by default.** Evaluate the full landscape — all open failures, kill conditions, dependencies, and the big picture — and choose the highest-impact next step. State the reasoning briefly so Chris can override if needed, but do not present menus of options or ask Chris to choose between alternatives unless there is a genuine fork that depends on a value judgment.
- **If the project needs to change direction, say so.** If a result invalidates a line of work, or if a new insight opens a better path, propose the pivot with reasoning. Don't continue down a dead end out of inertia.

### 1.5 Model recommendation guide

- **Use Opus when:** the session involves novel derivations, structural proofs, or creative theoretical reasoning; multi-step logical chains where an error in step 3 invalidates everything after it; interpreting ambiguous or conflicting results; scoping a new workstream where the right approach isn't obvious; re-planning sessions; any session where getting the physics *wrong* would waste multiple future sessions.
- **Use Sonnet when:** the session is primarily mechanical computation (e.g., back-solving parameters from known formulas, running RG equations, numerical cross-checks); file management, reformatting, or admin tasks; straightforward literature lookups; repeating a well-defined calculation with different inputs; auditing arithmetic where the procedure is already established.
- **When in doubt, recommend Opus.** A wrong derivation is more expensive than the model price difference. Only one model can be used per session — pick based on the primary task, noting if the secondary task would warrant a different choice.

---

## §2 — Working Style

- **Don't summarize the uploaded files.** Go straight to working.
- **Don't prompt Chris or ask for permission to continue.** Work autonomously through the full session. Only stop if a genuine external blocker is reached (e.g., a required file is missing and cannot be worked around), in which case state the blocker clearly and then continue with whatever can be done without it.
- **Print intermediate steps in all code.** Never rely on text generation for any mathematical claim. Write and execute Python (or equivalent) for every numerical result, every formula check, every approximation. Intermediate values must appear in the output so the chain of reasoning is auditable.
- **Be honest about failures.** Use status tags consistently (§6). Do not adjust inputs to make a result fit. If a number doesn't check out, say so.
- **Flag upstream dependencies explicitly.** If a result depends on an unverified input, tag it `[⚠ depends on X]` and move on — do not silently propagate unverified inputs.
- **Flag when you need a file you don't have.** State which file is needed and why, then continue with what is available.
- **Think like a skeptical referee, not an advocate.** The goal is to find what's true, not to confirm what we hope. Actively look for ways a derivation could fail. If a result seems too clean, stress test it.
- **Think step-by-step before making structural changes.** Prefer clarity over cleverness. Keep outputs structured and easy to read. Avoid unnecessary verbosity. Focus on meaningful progress rather than superficial changes.

---

## §3 — Computational Rigor

- **Mandatory code-verified math.** Every numerical claim must be verified by executing code before being written into any file. No exceptions.
- **Re-derive, don't recall.** When checking a number that already appears in a file, re-derive it from scratch in code rather than checking it against the stored value. The stored value is what you are auditing.
- **Dimensional and unit checks.** When computing physical quantities, explicitly verify units and order-of-magnitude at each step. Print units alongside numerical values in code output.
- **Unit tests for all non-trivial code.** Every computational function must include at least one sanity check or unit test — a known limiting case, a symmetry property, or a cross-check against a textbook value. Print the test result.
- **Cross-check via multiple routes where possible.** If a result can be derived two ways (e.g., algebraically and numerically, or via two independent formulas), do both and confirm they agree before tagging `[✓]`.
- **Do not propagate approximate values.** When an intermediate result is approximate (e.g., a rounded PDG input), note the approximation and carry forward the exact computed value, not the rounded one.
- **Distinguish exact from approximate.** Algebraic identities (e.g., 4cos²(π/5) = φ²) are exact and should be verified symbolically as well as numerically. Fitted parameters are never tagged `[✓]` — they get `[D]` or `[⚠]` with the fitting noted.
- **Stress test derivations.** After reaching a conclusion, probe it: vary inputs by ±10%, check edge cases, test whether the result is robust or fragile. If a result flips sign or changes qualitatively under small perturbations, flag it.
- **Re-derive when stakes are high.** Any result that feeds into multiple downstream predictions, any result that could trigger or clear a kill condition, any result that will be cited as a key finding — re-derive from scratch rather than trusting a cached value.
- **Kill conditions are first-class.** If a computation triggers or approaches a kill condition (§9 of Reference Core), stop and flag it explicitly before continuing. Do not bury a potential kill condition in a footnote.

---

## §4 — Literature and Source Verification

- **Look up papers when appropriate.** When a derivation depends on a theorem, identity, or result from the literature, search for and cite the actual source rather than relying on memory. Use web search to find the paper, then verify the specific claim.
- **Verify representation-theoretic facts computationally.** Don't trust recalled branching rules, tensor product decompositions, or Clebsch-Gordan coefficients. Compute them explicitly (e.g., using LiE, SageMath, or direct weight-system computation in Python). If a computation tool isn't available, note the gap and flag it `[⚠ unverified: needs computational verification]`.
- **Use PDG values as primary experimental inputs.** When experimental numbers are needed, search for current PDG values rather than relying on memorized values. Note the PDG edition/year used.
- **Cite sources inline.** When a result comes from a specific paper, note it as `[source: Author YYYY, eq. X]` or `[source: PDG 2024, Table X]`. This makes the chain of reasoning auditable.
- **Never store copyrighted material in the repository.** This project is stored on GitHub. Do not store PDFs, paper text, or any copyrighted content. Instead, track references in `03_REFERENCE/PAPER_INDEX.md` with citation info, arXiv/DOI links, and notes on which results were used. The reference folder contains only index files and original notes — never third-party content.

---

## §5 — File Update Policy

- **Only update files at session close.** Do not write interim results into files mid-session. Accumulate all verified results, then apply all edits at the end in one pass.
- **Update files automatically at session close — do not wait to be asked.** Apply all verified results and corrections to the relevant files, output the updated files, and state a brief summary of what changed.
- **Always update this briefing at session close** to reflect the new current status and next-session instructions.
- **Always update E8_Reference_Core.md** whenever a numerical result is verified, corrected, or newly derived. The Reference Core must be kept current.

### Workstream and notebook management

- **Create new workstream files proactively.** When a new line of work is clearly needed, create `E8_WS_[Name].md` at session close and populate it with the problem statement, known inputs, and first concrete steps.
- **Create new notebook files when needed.** If a computation is becoming complex enough that it needs its own persistent record, create `E8_NB_[Name].md` to store the work. Notebooks differ from workstreams: a workstream has an objective and closes; a notebook accumulates reference material.
- **Archive files explicitly.** When a workstream is fully closed (not just stalled), mark it archived in §12 and instruct Chris to move it out of the active upload set. A closed workstream file should not be uploaded in future sessions unless explicitly reopened.

---

## §6 — Tagging Protocol

| Tag | Meaning |
|-----|---------|
| `[✓ code-verified YYYY-MM-DD]` | Script ran, number matches stated value to stated precision |
| `[✗ CORRECTED: old=X, new=Y, code-verified YYYY-MM-DD]` | Error found and corrected |
| `[⚠ formula unverified: depends on X]` | Blocked — upstream input not yet checked |
| `[T-cited: REF, numerical consequence verified YYYY-MM-DD]` | Theorem from literature; its numerical output was independently checked |
| `[T]` | Theorem from literature (not yet independently checked) |
| `[D]` | Derived with stated assumptions |
| `[P]` | Physical/heuristic argument |
| `[F]` | Failure / kill condition |

### Hypothesis status tags

| State | Meaning |
|-------|---------|
| `[EXPERIMENTAL]` | Newly proposed, untested |
| `[ACTIVE]` | Under active investigation |
| `[STABLE]` | Tested and holding; used as foundation for further work |
| `[ARCHIVED]` | Superseded or no longer active, but preserved for reference |
| `[REJECTED]` | Falsified or abandoned with documented reason |

---

## §7 — Integrity and Audit Systems

### 7.1 Periodic audit triggers

Trigger a **full re-audit** of the Reference Core whenever:

- (a) 5 or more new numerical results have been added since the last audit
- (b) a significant structural result has changed (e.g., a kill condition triggered, a tier reclassification)
- (c) it has been 10+ sessions since the last audit

Flag this proactively — do not wait for Chris to request it.

### 7.2 Re-planning triggers

Trigger a **re-planning session** whenever:

- (a) a kill condition is triggered or cleared
- (b) 3+ workstreams have closed since the last re-plan
- (c) a major structural insight changes the priority ordering
- (d) it has been 8+ sessions since the last re-plan

During re-planning, reassess all open failures, re-rank priorities, and propose a concrete multi-session roadmap.

### 7.3 Theory audit (~every 25 sessions)

Approximately every 25 sessions, perform a **structured theory review**:

- Attempt to **falsify** the theory rather than defend it.
- Identify the weakest assumptions and test them.
- Check whether any resolved knowledge has been invalidated by subsequent work.
- Review the dependency graph for hidden circular reasoning.
- Update THEORY_HEALTH (§11).

### 7.4 High-integrity reasoning protocol

For complex reasoning tasks, use a three-stage process:

1. **Exploration** — survey the problem space, identify approaches, note potential pitfalls.
2. **Structured derivation** — execute the chosen approach with full rigor, printing all intermediate steps.
3. **Critical verification** — independently check the result via:
   - dimensional analysis
   - limiting cases
   - symmetry checks
   - comparison with known results
   - perturbation/stress testing

### 7.5 Contradiction tracking

When a contradiction is discovered between derivations, predictions, or data:

1. Log it with a unique ID (e.g., `CONTRA-001`).
2. Identify the minimal set of assumptions that produce the contradiction.
3. Rank resolution paths by which assumption is most likely wrong.
4. Link the contradiction to the relevant failure entry and hypothesis tree nodes.

Contradictions are tracked in **CONTRADICTION_TRACKER.md** (04_META/) if the full file system is active, or inline in this briefing's §8 otherwise.

---

## §8 — The Framework

### 8.1 One-paragraph summary

The (E₈)₁ WZW model is the unique holomorphic CFT at c=8. Its boundary theory is proposed as the self-referential model of a de Sitter horizon. Self-modeling is formalized as a subfactor inclusion, selecting Jones index φ² (Fibonacci anyon). The conformal embedding E₈ ⊃ SU(3)_fam × E₆ ⊃ ... ⊃ SM at level 1 fixes all gauge couplings with no free parameters. Three generations arise from the 3 of SU(3)_fam. The Higgs is the Fibonacci τ anyon (m_H/M_W = φ). Mass hierarchies come from Randall-Sundrum bulk profiles in a 5D dual, perturbed by (G₂)₆ condensates. The entropic partition function Z = j(i)^{1/3} = 12 fixes the EW scale via M_W = M_Pl/12^15.

### 8.2 Theory evolution log

Major structural changes to the theory are recorded here in reverse chronological order. For the full dependency graph, see THEORY_EVOLUTION_GRAPH.md (if active) or RESEARCH_DEPENDENCY_GRAPH.md.

| Date | Change | Reason | Impact |
|------|--------|--------|--------|
| 2026-03-17 | Phase 2 re-evaluation complete | Fresh-eyes assessment of all claims; dependency analysis; re-prioritization | Priority reordering: WS-3875 elevated to #1; α₂ [⚠] flags elevated to #3; M_GUT flagged as hidden parameter |
| 2026-03-17 | KC-g partial kill: 248 renormalizable sector killed for CKM | Four independent proofs of V_CKM = I in 248 | 3875 extension now the only viable CKM path |

---

## §9 — Current Status

*(as of 2026-03-17 — ROS v2 Session 2 complete)*

### Project phase: POST-RE-EVALUATION — TARGETED PHYSICS WORK

**Phase 1 — File system buildout: ✓ COMPLETE (Session 1).**

**Phase 2 — Full theory re-evaluation: ✓ COMPLETE (Session 2).** All numerical values in E8_Reference_Core independently re-derived and confirmed. Conceptual assessment completed: theory is VIABLE but INCOMPLETE. No circular reasoning found. M_GUT identified as unacknowledged hidden parameter. KC-g/CKM is the existential risk. Research priorities re-ordered. First theory snapshot created.

**Phase 3 — Targeted physics work: NEXT.** Resume work on open failures with priorities set by the Phase 2 re-evaluation.

### What's established (post-re-evaluation)

- **Solidly established (mathematical):** Conformal embedding cascade, central charges, 3 generations, Z=12, φ from Jones index, WZW level structure.
- **Well-supported (physical):** Gauge coupling predictions (Tier A), EW scale (Tier B, conditional on n=15), Higgs mass ratio.
- **Weakened by flags:** α₂ prediction depends on three unverified inputs (b₂^WZW, +2.75, M_GUT). The 0.4% match is real but the prediction chain has gaps.
- **Incomplete:** Mass hierarchy mechanism (F7 — stored params are wrong), CKM mixing (KC-g — 248 killed), top mass (F4 — 11% off).
- **Blocked:** n=15 derivation (F3 — no path forward).

### KC-g decision (2026-03-17)

Unchanged. KC-g remains at "partial kill / 248-sector full kill." The only surviving viable path (Path A — (351,3_fam) from 3875 of E₈) has not been evaluated. KC-g upgrades to "full kill" only if WS-3875 shows Path A is also insufficient.

### Open failures (re-assessed, re-prioritized)

**1. WS-3875 — 3875 of E₈ as source of CKM** `[EXPERIMENTAL]`
EXISTENTIAL. Only remaining viable path for CKM mixing. Determines whether the theory survives.
Concrete task: Decompose 3875 under SU(3)_fam × E₆. Identify operators coupling to SM Yukawas. Estimate suppression scale.

**2. F7 — §6 parameter inconsistency** `[ACTIVE]`
Blocks all quantitative mass predictions. Stored P×L, Q×L are off by factors of 100-300×.
Concrete task: Back-solve exact P×L, Q×L for up and down sectors to reproduce m_t/m_u = 84,455 and m_b/m_d = 836 exactly.

**3. [⚠] flags on α₂ prediction chain** `[ACTIVE]`
The showcase result (0.4% match) rests on three unverified inputs. Needs cleaning up for any paper.
Concrete task: (a) Identify b₂^WZW = +38/3 from E₈ matter content. (b) Identify +2.75 corrections. (c) Derive M_GUT self-consistently.

**4. F4 — Top mass 11% discrepancy** `[ACTIVE]`
Potentially explainable by QCD corrections / running vs pole mass. Bounded computation.

**5. F3 (n=15)** `[ARCHIVED]`
Parked — self-modeling map S undefined. Needs new mathematical ideas.

### Session counter and trigger tracking

| Metric | Value |
|--------|-------|
| ROS v2 session count | 2 (next session is session 3) |
| Sessions since last audit | 0 (Phase 2 re-eval = full audit) |
| Sessions since last re-plan | 0 (Phase 2 re-eval = re-plan) |
| Sessions since last theory audit | 0 (Phase 2 re-eval = theory audit) |
| New numerical results since last audit | 0 |
| Closed workstreams since last re-plan | 0 |
| Next audit trigger | After 5 new results or 10 sessions |
| Next re-plan trigger | After 8 sessions or kill condition change |
| Next theory audit | ~session 27 |

---

## §10 — Research Radar

Prioritized research directions, ranked by expected impact. Updated at session close.

| Priority | Direction | Rationale | Status |
|----------|-----------|-----------|--------|
| 1 | **WS-3875 (3875 decomposition for CKM)** | Existential: theory dies if this fails; must resolve before investing in refinements | Next session |
| 2 | **F7 parameter back-solve** | Blocks all mass predictions; prerequisite for Paper 2 | After WS-3875 scoping |
| 3 | **Resolve [⚠] flags on α₂ chain** | The showcase Tier A result has three unverified inputs; undermines strongest evidence | After F7 |
| 4 | **F4 top mass discrepancy** | 11% is significant; bounded computation; QCD corrections may resolve | After α₂ flags |
| 5 | **F3 (n=15)** | Blocked — needs new mathematical insight | Parked |

### Research dependency map (current critical path)

```
WS-3875 (CKM viability)
    │
    ├── SUCCESS → theory viable → continue all lines
    │       │
    │       ├── F7 parameter back-solve
    │       │       │
    │       │       └── Paper 2 mass predictions
    │       │
    │       ├── α₂ [⚠] flag resolution
    │       │       │
    │       │       └── Clean Tier A presentation
    │       │
    │       └── F4 top mass
    │
    └── FAILURE → KC-g full kill → theory cannot explain CKM
                   → reassess: can theory survive as partial framework?
                   → or: search for mechanism beyond 3875?
```

---

## §11 — Theory Health Dashboard

| Metric | Count | Trend |
|--------|-------|-------|
| Active hypotheses | 2 (3875 CKM path, RS mass mechanism) | — |
| Stable results | Gauge couplings, EW scale, Higgs mass ratio, embedding cascade | — |
| Open failures | 4 active (F4, F7, KC-g partial, [⚠] flags) + 1 parked (F3) | — |
| Active contradictions | 0 | — |
| Kill conditions triggered | 1 partial (KC-g, 248 sector only) | ↑ risk |
| Tier A predictions verified | Yes (with caveats on α₂ chain) | ← new caveat |
| Hidden parameters identified | 1 (M_GUT as external input) | ← new finding |

**Overall assessment (post-Phase 2):** Theory remains viable pending WS-3875 outcome. The mathematical structure is solid. The gauge coupling predictions are impressive but the α₂ chain has gaps that need closing. F7 is blocking but mechanically resolvable. KC-g is the existential risk — 3875 path is the last viable CKM mechanism. The theory's honest status is "promising research program with one make-or-break question."

---

## §12 — File Inventory

### Current file system (as of 2026-03-17, Session 2 complete)

```
.
├── E8_Task_List.md
├── 00_SYSTEM/
│   ├── E8_Session_Briefing.md          ← UPDATED
│   ├── E8_Reference_Core.md            ← UPDATED
│   ├── PROJECT_INDEX.md
│   ├── CONTEXT_SNAPSHOT.md             ← UPDATED
│   └── THEORY_HEALTH.md               ← UPDATED
├── 01_KNOWLEDGE/
│   ├── DISCOVERY_LOG.md                ← UPDATED
│   ├── RESOLVED_KNOWLEDGE.md           ← UPDATED
│   ├── HYPOTHESIS_TREE.md              ← UPDATED
│   ├── CONCEPT_REGISTRY.md
│   ├── PARAMETER_REGISTRY.md
│   ├── THEORY_EVOLUTION_GRAPH.md
│   ├── RESEARCH_DEPENDENCY_GRAPH.md    ← UPDATED
│   └── THEORY_SNAPSHOTS/
│       └── THEORY_SNAPSHOT_001.md      ← NEW
├── 02_WORKSTREAMS/
│   └── (empty — CKM2 moved to archive)
├── 03_REFERENCE/
│   ├── PAPER_INDEX.md
│   └── NOTES/
├── 04_META/
│   ├── SESSION_LEDGER.md               ← UPDATED
│   ├── FAILURE_LEDGER.md               ← UPDATED
│   ├── CONTRADICTION_TRACKER.md
│   └── META_RESEARCH_LOG.md
└── 05_ARCHIVE/
    ├── completed_workstreams/
    │   └── E8_WS_CKM2.md (+ others)
    ├── deprecated_theories/
    └── old_theory_snapshots/
```

### Session upload set

| File | Purpose | Status |
|------|---------|--------|
| `E8_Reference_Core.md` | Master results ledger | Always upload |
| `E8_Session_Briefing.md` | Session rules and status | Always upload |

---

## §13 — Next Session Plan

### Primary task: WS-3875 — Scope the 3875 decomposition for CKM

This is the highest-priority task. The entire theory's viability hinges on whether the 3875 representation of E₈ can generate CKM mixing.

Concrete steps:
1. Decompose 3875 of E₈ under SU(3)_fam × E₆. Identify all components.
2. Identify which components contain operators that couple to SM Yukawas (specifically, operators of the form 27_i × 27_j × X where X is NOT the standard 27_H).
3. Determine whether any such operator can generate off-diagonal flavor structure (i.e., break the V_CKM = I result).
4. Estimate the suppression scale: if the 3875 operator arises from a condensate at scale Λ, what is Λ relative to M_GUT? Is the resulting CKM mixing of the right magnitude?
5. Assess: is this path viable, marginal, or dead?

### Secondary task: F7 parameter back-solve

If WS-3875 scoping completes early (either a clear answer or a clear block), pivot to:
- Back-solve exact P×L, Q×L for up and down sectors from the mass formula m_i/m_j = exp((c_j−c_i)×L) and PDG mass ratios.
- Verify the back-solved values are physically reasonable (P, Q > 0; L ≈ 36.1).

### Decision points

None — WS-3875 is the clear next step. If the 3875 decomposition requires computational tools not available in-session (e.g., LiE for branching rules), flag the gap and pivot to F7.

### Files for next session

- `E8_Reference_Core.md` ✓ always
- `E8_Session_Briefing.md` ✓ always
- No workstream file needed (WS-3875 will be created during the session)

### Model recommendation

**Opus** for the next session. WS-3875 scoping requires novel representation theory reasoning, creative approaches to the decomposition, and judgment about whether the resulting mechanism is viable. Getting the group theory right is critical — an error here could waste multiple sessions or prematurely kill/validate the theory. This is not a mechanical computation.

---

## §14 — Efficiency Policy

### Context snapshot principle

The §9 status block and §10 research radar serve as the **context snapshot** — the minimum information needed to orient at session start. Read these first to minimize tool usage.

### Tool usage strategy

Treat tool usage as a limited resource. Efficiency is critical for long-running sessions.

- **Prefer reasoning over tool usage when possible.** If a value can be re-derived faster than found, re-derive it.
- **Plan before executing.** Outline the investigation approach before making tool calls.
- **Batch file updates** instead of making many small edits. Apply all session-close changes in one pass.
- **Avoid repeatedly reading the same files.** Extract all needed information from a file in one read.
- **Only use tools when they significantly improve output quality.**
- **Be aware of session/tool limits and adapt behavior dynamically.** If limits are approaching, prioritize the highest-value remaining work.
- **Minimize unnecessary file operations.**

### File optimization rule

The system is allowed to aggressively improve file structure when beneficial.

Allowed actions: restructure files, merge or split documents, remove redundancy, move content to archive.

Conditions: no important information is lost; changes improve clarity, usability, or AI performance; structure remains consistent and navigable. Optimization should prioritize long-term scalability.

---

## §15 — Meta-Evolution

### 15.1 Research operating system meta-analysis

Periodically (approximately every 10 sessions, or when friction is noticed), evaluate:

- Is the file architecture still effective, or has it become cluttered?
- Are reasoning safeguards catching real errors, or creating overhead?
- Are knowledge tracking systems being used, or being ignored?
- Is the session briefing too long or missing critical information?

Record meta-improvements in `04_META/META_RESEARCH_LOG.md`.

### 15.2 Folder structure review

Approximately every 10 sessions, perform a **directory structure audit**:

- Are any folders consistently empty or unused? Consider removing or merging them.
- Have files accumulated organically outside the defined structure? Relocate or formalize them.
- Are naming conventions consistent? Fix drift.
- Has a new category of work emerged that deserves its own folder?
- Is the archive growing in a way that needs subcategorization?
- Is the upload set still minimal, or has it grown unwieldy?

Log structural changes in `04_META/META_RESEARCH_LOG.md` with date and rationale.

### 15.3 External meta-research

When relevant, research advances in:

- AI-assisted research workflows
- Prompt engineering for mathematical reasoning
- Knowledge management for long-horizon projects
- Reasoning verification methods

Apply useful findings to this research operating system.

### 15.4 Repository policy (GitHub)

This project is stored in a Git repository. The following rules apply:

- **No copyrighted material.** Never commit PDFs, paper text, book excerpts, or any third-party copyrighted content. Use `03_REFERENCE/PAPER_INDEX.md` to track citations with links.
- **No secrets or credentials.** No API keys, tokens, or personal data.
- **No large binary files.** Keep the repo text-only. If computational output (plots, data) needs to be stored, use lightweight formats and keep sizes small.
- **Commit messages should reference session numbers** (e.g., `session-014: Phase 2 re-evaluation complete`) so the Git history aligns with the session ledger.

### 15.5 AI platform awareness

Claude is the **default research platform**. Other systems (OpenAI models, Gemini) may occasionally be used for tasks that do not require project files and benefit from independent reasoning checks. Switching platforms should be rare and justified.

---

## §16 — Local Environment

### 16.1 Paths

| Purpose | Path |
|---------|------|
| **Project root** | `/Users/cdowd/Projects/E₈ Theory` |
| **Downloads folder** | `/Users/cdowd/Downloads` |
| **Python scripts** | `/Users/cdowd/Projects/E₈ Theory/scripts/` |

All project files live under the project root and are tracked in git. Python scripts go in `scripts/` so they are version-controlled alongside the research files. If a script becomes general-purpose enough to live outside this project, flag it at session close.

### 16.2 Session close — terminal commands

**THIS BLOCK IS REQUIRED OUTPUT AT EVERY SESSION CLOSE. DO NOT SKIP IT.**

At session close, you MUST print a **Terminal Commands** block containing the exact shell commands to move every downloaded file from `/Users/cdowd/Downloads/` into its correct project location. This block must appear inside the ⚡ Quick Reference section. If it is missing, the session close is incomplete.

**New file (first placement):**
```bash
mv "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E₈ Theory/PATH/TO/FILENAME.md"
```

**Replacing an existing file:**
```bash
cp "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E₈ Theory/PATH/TO/FILENAME.md"
```
(`cp` overwrites in place; git will show the diff.)

**Python script:**
```bash
mv "/Users/cdowd/Downloads/script_name.py" "/Users/cdowd/Projects/E₈ Theory/scripts/script_name.py"
```

**After all moves, always commit:**
```bash
cd "/Users/cdowd/Projects/E₈ Theory" && git add -A && git commit -m "session-NNN: <description>"
```

Replace `NNN` with the session number from SESSION_LEDGER.md and `<description>` with a one-line summary of what the session produced.

### 16.3 Git policy

- Commit messages reference session numbers (e.g., `session-014: Phase 2 re-evaluation complete`).
- No copyrighted material, secrets, credentials, or large binary files in the repo (see §15.4).
- Text-only repo. Computational plots or data, if needed, use lightweight formats.

---

## ⚡ Quick Reference

### Tasks
- **Primary:** WS-3875 — Scope the 3875 of E₈ decomposition for CKM viability (existential priority)
- **Secondary:** F7 — Back-solve exact P×L, Q×L for up and down sectors

### Working directory (current)
```
.
├── E8_Task_List.md
├── 00_SYSTEM/
│   ├── E8_Session_Briefing.md
│   ├── E8_Reference_Core.md
│   ├── PROJECT_INDEX.md
│   ├── CONTEXT_SNAPSHOT.md
│   └── THEORY_HEALTH.md
├── 01_KNOWLEDGE/
│   ├── DISCOVERY_LOG.md
│   ├── RESOLVED_KNOWLEDGE.md
│   ├── HYPOTHESIS_TREE.md
│   ├── CONCEPT_REGISTRY.md
│   ├── PARAMETER_REGISTRY.md
│   ├── THEORY_EVOLUTION_GRAPH.md
│   ├── RESEARCH_DEPENDENCY_GRAPH.md
│   └── THEORY_SNAPSHOTS/
│       └── THEORY_SNAPSHOT_001.md
├── 02_WORKSTREAMS/
│   └── (empty)
├── 03_REFERENCE/
│   ├── PAPER_INDEX.md
│   └── NOTES/
├── 04_META/
│   ├── SESSION_LEDGER.md
│   ├── FAILURE_LEDGER.md
│   ├── CONTRADICTION_TRACKER.md
│   └── META_RESEARCH_LOG.md
└── 05_ARCHIVE/
    ├── completed_workstreams/
    │   └── E8_WS_CKM2.md (+ others)
    ├── deprecated_theories/
    └── old_theory_snapshots/
```

### Download (from this session)
```
E8_Reference_Core.md
E8_Session_Briefing.md
THEORY_SNAPSHOT_001.md
```

### Upload (next session)
```
E8_Session_Briefing.md
E8_Reference_Core.md
```

### Terminal commands
```bash
# Replace existing files
cp "/Users/cdowd/Downloads/E8_Reference_Core.md" "/Users/cdowd/Projects/E₈ Theory/00_SYSTEM/E8_Reference_Core.md"
cp "/Users/cdowd/Downloads/E8_Session_Briefing.md" "/Users/cdowd/Projects/E₈ Theory/00_SYSTEM/E8_Session_Briefing.md"

# New file
mv "/Users/cdowd/Downloads/THEORY_SNAPSHOT_001.md" "/Users/cdowd/Projects/E₈ Theory/01_KNOWLEDGE/THEORY_SNAPSHOTS/THEORY_SNAPSHOT_001.md"

# Commit
cd "/Users/cdowd/Projects/E₈ Theory" && git add -A && git commit -m "session-002: Phase 2 re-evaluation complete; theory snapshot created; priorities re-ordered"
```

### Model
**Opus** — WS-3875 requires novel representation theory and judgment about viability

---

*End of session briefing — Research Operating System v2.1*
