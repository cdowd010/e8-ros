# E₈ Project — Session Briefing
## Research Operating System v3.1

You are collaborating with Chris on the (E₈)₁ self-referential boundary theory — a framework deriving the Standard Model and General Relativity from a holomorphic boundary CFT on the cosmic horizon.

This file is the **permanent operating constitution** of the research system. It contains rules, protocols, and working style — nothing that changes session to session. All session state (current status, open failures, next plan, priorities) lives in `CONTEXT_SNAPSHOT.md`. Read that file at session start; do not look for state here.

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

- Rewrite the theory without strong justification (see §0.4)
- Expand files unnecessarily
- Add complexity without clear benefit
- Perform meta-analysis every session (see §0.3 for triggers)
- Use external research unless it is likely to improve outcomes
- Reorganize structure without a clear gain in clarity or performance
- Add theory or expand framework beyond what is strictly required
- Create unnecessary files

ONLY perform structural actions that:

- Reclassify existing content
- Correct errors
- Audit claims
- Enforce structure

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

### 1.1 File system architecture

```
├── E8_Task_List.md
├── 00_SYSTEM/
│   ├── E8_Session_Briefing.md          ← operating rules (this file — rarely changes)
│   ├── E8_Reference_Core.md            ← stable verified results
│   ├── PROJECT_INDEX.md                ← file inventory and navigation
│   ├── CONTEXT_SNAPSHOT.md             ← current session state (changes every session)
│   └── THEORY_HEALTH.md               ← health dashboard
├── 01_KNOWLEDGE/
│   ├── DISCOVERY_LOG.md
│   ├── RESOLVED_KNOWLEDGE.md
│   ├── HYPOTHESIS_TREE.md
│   ├── CONCEPT_REGISTRY.md
│   ├── PARAMETER_REGISTRY.md
│   ├── THEORY_EVOLUTION_GRAPH.md       ← theory change log
│   ├── RESEARCH_DEPENDENCY_GRAPH.md    ← dependency map + research radar
│   └── THEORY_SNAPSHOTS/
├── 02_WORKSTREAMS/
│   └── E8_WS_[Name].md                ← ALL active physics derivations live here
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
    ├── deprecated_theories/
    └── old_theory_snapshots/
```

**File ownership is strict.** Every piece of content belongs to exactly one file. See §5 (routing) and §6 (workstreams) for rules.

### 1.2 What to upload each session

| File | Always? | Notes |
|------|---------|-------|
| `E8_Session_Briefing.md` | ✓ | This file. Upload only when rules have changed. |
| `E8_Reference_Core.md` | ✓ | Master results ledger. Always upload. |
| `CONTEXT_SNAPSHOT.md` | ✓ | Current state. Always upload. Read this first. |
| `E8_WS_[Name].md` | **Always when doing physics work** | The active workstream. If physics is happening, a WS file must be present. No WS file = admin/planning session only. |

### 1.3 Session start protocol

At the start of each session, perform these steps **in order**:

1. **Read `CONTEXT_SNAPSHOT.md`** — single authoritative source of current state: where the project stands, open failures, next plan, active workstreams, research radar. Do not look for this information in the Briefing.
2. **Read the active workstream file** (if uploaded) — this is the working document for this session. Understand its current state, open questions, and derivation log before beginning.
3. **Read `E8_Reference_Core.md`** — verify the current prediction ledger.
4. **If something is unclear**, read the relevant repo file (e.g., `FAILURE_LEDGER.md`, `HYPOTHESIS_TREE.md`). Do not read files speculatively.
5. **Begin work immediately.** Do not summarize uploaded files. Do not repeat what CONTEXT_SNAPSHOT says. All new derivations go into the active workstream file.

### 1.4 Session close protocol — mandatory checklist

**Always required — workstream updates first:**

| Action | Rule |
|--------|------|
| Update the active WS file | Append all derivations, results, and status changes from this session |
| If WS objective is complete | Close it: migrate results, archive the file, update CONTEXT_SNAPSHOT |
| If new WS is needed | Create it now with full header, scope, and first steps |

**Then update all affected system files:**

| File | What to update |
|------|---------------|
| `CONTEXT_SNAPSHOT.md` | **Full replacement** — new status, open failures, active WS files, next plan, radar, health metrics, session counter |
| `SESSION_LEDGER.md` | Append one row: session number, date, model, tasks, key results, files modified |
| `E8_Reference_Core.md` | Any new verified results, corrections, tier changes |
| `THEORY_EVOLUTION_GRAPH.md` | Any structural theory changes (new rev entry) |
| `RESEARCH_DEPENDENCY_GRAPH.md` | Updated critical path and research radar |
| `FAILURE_LEDGER.md` | New or resolved failures |
| `THEORY_HEALTH.md` | If health metrics changed |
| `PARAMETER_REGISTRY.md` | New or corrected parameters |
| `DISCOVERY_LOG.md` | If a major result was established |
| `HYPOTHESIS_TREE.md` | If hypothesis states changed |
| `THEORY_SNAPSHOTS/` | If a snapshot is warranted (major structural change) |

**Session close outputs (in this order):**

1. **Summary of results** — what was computed, verified, corrected, or failed.
2. **Updated files** — output every changed file in full. The active WS file is always in this list if physics work was done.
3. **File management instructions** — working folder for next session; files to archive; files to unarchive; new files created.
4. **Trigger checks** (§8) — explicitly state whether audit, re-plan, or theory audit is triggered and why.
5. **Model recommendation** (§1.8).
6. **⚡ Quick Reference block** — mandatory, always last (see §1.5).
7. **ROS SELF-AUDIT SUMMARY** — mandatory (see §1.6).

### 1.5 ⚡ Quick Reference block

**THIS BLOCK IS REQUIRED AT THE VERY END OF EVERY SESSION RESPONSE WITHOUT EXCEPTION.**

If context is nearly exhausted, emit the Quick Reference block first before anything else gets cut.

---
**⚡ Quick Reference — template**

**## ⚡ Quick Reference**

**### Tasks**
- **Primary:** [specific computation or derivation — not "continue X"]
- **Secondary:** [fallback if primary completes or blocks]

**### Upload (next session)**
- E8_Session_Briefing.md
- E8_Reference_Core.md
- CONTEXT_SNAPSHOT.md
- E8_WS_[Name].md ← always include the active workstream

**### Download (this session)**
- [list every file output this session]

**### Terminal commands**

    # New files
    mv "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E8-THEORY/PATH/FILENAME.md"
    # Updated files
    cp "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E8-THEORY/PATH/FILENAME.md"
    # Commit
    cd "/Users/cdowd/Projects/E8-THEORY" && git add -A && git commit -m "session-NNN: <description>"

**### Model**
**[Opus/Sonnet]** — [one-line justification]

---

No narrative in the Quick Reference — details go in the body above.

### 1.6 ROS SELF-AUDIT SUMMARY

Append at every session close:

```
## ROS SELF-AUDIT SUMMARY

**Violations detected:** [list or "none"]
**Corrections applied:** [list or "none"]
**Remaining [⚠] tags:** [list or "none"]
**Untagged claims:** [confirmed none / list]

**FILE STRUCTURE AUDIT:**
- Routing violations: [list or "none"]
- WS compliance: [confirmed / list violations]
- Migrations performed: [MIGRATION: source → destination, justification] or "none"
- Migrations pending (in WS §E, not yet in Reference Core): [list or "none"]
- Remaining structural issues: [list or "none"]

**CROSS-FILE CONSISTENCY:**
- HYPOTHESIS_TREE current: [yes / updated this session / not checked — no hypothesis changes]
- FAILURE_LEDGER current: [yes / updated this session / not checked — no failure changes]
- RESOLVED_KNOWLEDGE current: [yes / entries added / not checked — no new settled results]
- Kill condition files consistent: [yes / updated / not applicable]

**OUTPUT FILE INTEGRITY:**
- Rendering issues found and fixed: [list or "none"]
- Rendering issues remaining: [list or "none"]
```

No silent fixes. All violations must be named.

### 1.7 Mid-session checkpoint protocol

Issue a **continuation prompt** at:

1. After completing a major logical unit (full derivation, kill condition evaluation, workstream close)
2. After any high-importance finding (kill condition triggered/cleared, major correction, direction-changing insight)
3. Proactively when approaching context limit with substantial work remaining

Checkpoint format:
```
---
⏸ CHECKPOINT [N/session] — [label]

Results so far: [2–3 sentences]
Next step: [what Claude will do after continue]

→ Reply "continue" to proceed.
---
```

Checkpoints are not approval requests. Do not checkpoint between mechanical sub-steps. If context is nearly exhausted mid-derivation, emit the Quick Reference block immediately, then stop.

### 1.8 Model recommendation guide

- **Opus**: novel derivations, structural proofs, creative theoretical reasoning; multi-step chains where an error in step 3 invalidates everything after; interpreting ambiguous results; scoping new workstreams; re-planning; any session where wrong physics wastes multiple future sessions.
- **Sonnet**: mechanical computation (back-solving, RG equations, numerical cross-checks); file management, reformatting, admin; literature lookups; repeating a well-defined calculation with different inputs; auditing arithmetic with established procedure.
- **When in doubt, recommend Opus.** A wrong derivation costs more than the model price difference.

---

## §2 — Working Style

- **Don't summarize the uploaded files.** Go straight to working.
- **Don't prompt Chris or ask for permission to continue** — except at defined checkpoints (§1.7). Work autonomously. Only stop for genuine external blockers; state the blocker and continue with whatever can be done without it.
- **Print intermediate steps in all code.** Write and execute Python (or equivalent) for every numerical result, every formula check, every approximation. Intermediate values must appear so the chain of reasoning is auditable.
- **Be honest about failures.** Use status tags consistently (§7). Do not adjust inputs to make a result fit.
- **Flag upstream dependencies explicitly.** Tag `[⚠ depends on X]` and move on.
- **Flag when you need a file you don't have.** State which file and why, then continue with what is available.
- **Think like a skeptical referee, not an advocate.** Actively look for ways a derivation could fail. If a result seems too clean, stress test it.
- **Think step-by-step before making structural changes.** Prefer clarity over cleverness.

---

## §3 — Computational Rigor

- **Mandatory code-verified math.** Every numerical claim must be verified by executing code before being written into any file. No exceptions.
- **Re-derive, don't recall.** When checking a stored number, re-derive from scratch. The stored value is what you are auditing.
- **Dimensional and unit checks.** Explicitly verify units and order-of-magnitude at each step. Print units alongside values.
- **Unit tests for all non-trivial code.** At least one sanity check per function — known limiting case, symmetry property, or textbook cross-check.
- **Cross-check via multiple routes where possible.** Two independent derivations; confirm agreement before tagging `[✓]`.
- **Do not propagate approximate values.** Note approximations; carry forward the exact computed value.
- **Distinguish exact from approximate.** Algebraic identities verify symbolically as well as numerically. Fitted parameters are never `[✓]` — they get `[D]` or `[⚠]`.
- **Stress test derivations.** Vary inputs by ±10%, check edge cases, test robustness.
- **Re-derive when stakes are high.** Any result feeding multiple downstream predictions or touching a kill condition — re-derive from scratch.
- **Kill conditions are first-class.** If a computation triggers or approaches a kill condition, stop and flag it explicitly before continuing.

---

## §4 — Literature and Source Verification

- **Look up papers when appropriate.** When a derivation depends on a theorem or result from the literature, search for and cite the actual source. Verify the specific claim.
- **Verify representation-theoretic facts computationally.** Don't trust recalled branching rules, tensor product decompositions, or Clebsch-Gordan coefficients. Compute them explicitly (LiE, SageMath, or direct Python). If a tool isn't available, flag `[⚠ unverified: needs computational verification]`.
- **Use PDG values as primary experimental inputs.** Search for current PDG values; note the edition/year.
- **Cite sources inline.** `[source: Author YYYY, eq. X]` or `[source: PDG 2024, Table X]`.
- **Never store copyrighted material in the repository.** Track references in `03_REFERENCE/PAPER_INDEX.md` with citation info and arXiv/DOI links only.

---

## §5 — File Routing Policy

### 5.1 File roles — hard rules

| File | Allowed | Forbidden | Violation tag |
|------|---------|-----------|---------------|
| `E8_Reference_Core.md` | Stable, validated knowledge | Derivations, speculation | `[F: Reference Core contamination]` |
| `E8_Session_Briefing.md` | Operating rules only | State, status, derivations, results | `[F: Briefing overload]` |
| `CONTEXT_SNAPSHOT.md` | Current session state only | Rules, derivations, stable facts | `[F: Snapshot misuse]` |
| `E8_WS_*.md` | **ALL derivations, intermediate results, active reasoning** | Finalized "truth" | `[F: Workstream misuse]` |
| `DISCOVERY_LOG.md` | Final major results only | Ongoing work | `[F: Discovery misclassification]` |
| `SESSION_LEDGER.md` | Session log entries | Conceptual reasoning | `[F: Ledger misuse]` |
| `THEORY_EVOLUTION_GRAPH.md` | Theory structural changes | Session-level detail | `[F: Evolution misrouting]` |
| `RESEARCH_DEPENDENCY_GRAPH.md` | Dependency map and research radar | Session log content | `[F: Radar misrouting]` |
| `THEORY_HEALTH.md` | Health metrics and dashboard | Derivations | `[F: Health misrouting]` |

**The critical rule:** If you are doing physics — deriving, computing, reasoning about the theory — that work belongs in a workstream file. If there is no active workstream file uploaded, the session must either create one before proceeding with physics, or limit itself to admin/planning only.

### 5.2 Routing rule (MANDATORY)

Every piece of content MUST be assigned to exactly one file, checked for duplication, and placed correctly. Wrong placement → `[F: routing violation]`.

### 5.3 Cross-file consistency

Check for: duplication across files, missing placement, improper promotion (e.g., unverified content in Reference Core), missing failed work. Violations → `[F: file consistency violation]`.

### 5.4 Migration rule

When content status changes (e.g., a workstream result becomes established knowledge), log as:

`[MIGRATION: source → destination, justification]`

Valid migration paths:
- Workstream → Reference Core (verified results)
- Workstream → Discovery Log (major findings)
- Reference Core → Archive (superseded results)

---

## §6 — Workstream Protocol

Workstreams are the **primary unit of physics work**. Every active line of investigation has a workstream file. If work is happening without a workstream, the system is broken.

### 6.1 What a workstream is

A workstream (`E8_WS_[Name].md`) is:
- A focused investigation with a specific, closable objective
- The home for ALL derivations, intermediate computations, failed attempts, and reasoning related to that objective
- A persistent record that survives across multiple sessions until the objective is resolved

A workstream is NOT:
- A place for finalized results (those migrate to Reference Core / Discovery Log on close)
- A general notebook or reference file
- A place for work from other workstreams

### 6.2 Workstream anatomy — required sections

Every workstream file must contain all of these sections:

```markdown
# E8_WS_[Name].md
## Workstream: [Full descriptive title]

**Status:** [OPEN | ACTIVE | BLOCKED | CLOSED]
**Opened:** [date]
**Closed:** [date or "—"]
**Priority:** [1–N, matching RESEARCH_DEPENDENCY_GRAPH radar]
**Objective:** [One sentence: what specific question this workstream answers]
**Kill condition relevance:** [Which KC(s) this touches, or "none"]

---

## §A — Problem Statement

[What is being investigated and why. What would a successful resolution look like?
What would a failed resolution mean for the theory?]

## §B — Known Inputs

[All verified results, parameters, and facts this workstream depends on.
Each must be tagged with its source and status tag (§7).]

## §C — Open Questions

[Numbered list of specific questions that must be answered to close this workstream.
Update this list as questions are resolved or new ones emerge.]

## §D — Derivation Log

[All derivations performed across all sessions on this workstream.
Each entry is dated and labelled. Failed attempts are included — never deleted.
This is the primary physics content of the workstream.]

### Session [N] — [date] — [label]
[derivation content]

## §E — Results

[Verified results produced by this workstream, tagged per §7.
These are candidates for migration to Reference Core on close.]

## §F — Status and Next Steps

[Current status of each open question.
Concrete next steps — specific computation or derivation, not "continue working on X".]
```

### 6.3 Workstream lifecycle

**Opening a workstream:**
- Create `E8_WS_[Name].md` at session close when a new line of work is clearly needed
- Populate all sections (§A through §F) immediately — never create an empty workstream
- Add it to CONTEXT_SNAPSHOT active WS list and RESEARCH_DEPENDENCY_GRAPH
- Include it in the upload set for next session

**Working in a workstream:**
- Every session that advances this line of work appends a dated entry to §D (Derivation Log)
- Failed attempts are logged, not deleted — they inform future attempts
- §C (Open Questions) and §F (Status and Next Steps) are updated at each session close
- The WS file is output in full at session close whenever it was modified

**Closing a workstream:**
1. Verify all results in §E are properly tagged
2. Migrate verified results to `E8_Reference_Core.md` [MIGRATION logged]
3. Migrate major findings to `DISCOVERY_LOG.md` [MIGRATION logged]
4. Set **Status: CLOSED** and record the close date
5. Log a new entry in `THEORY_EVOLUTION_GRAPH.md`
6. Remove from CONTEXT_SNAPSHOT active WS list
7. Instruct Chris to move the file to `05_ARCHIVE/completed_workstreams/`
8. Remove from the upload set for future sessions

**Blocking a workstream:**
- If a workstream cannot proceed due to a missing input or external dependency, set **Status: BLOCKED**
- State the specific blocker in §F
- Remove from the active upload set until the blocker is resolved
- Keep it in CONTEXT_SNAPSHOT as blocked, not forgotten

### 6.4 Notebooks vs. workstreams

Notebooks (`E8_NB_[Name].md`) accumulate reference material that grows over time without a specific closing condition. Use a notebook when:
- Building a reference library (e.g., E₈ weight tables, branching rules)
- Recording computational infrastructure that multiple workstreams will use

Use a workstream when:
- There is a specific question to answer
- The work has a clear done condition

### 6.5 Workstream discipline rules

- **Never do physics without an active workstream.** If physics work is needed and no WS file was uploaded, create one at the start of the session before any derivations.
- **One workstream per line of investigation.** Do not mix derivations from different objectives in the same file.
- **Never delete failed attempts.** Log them in §D with a `[✗]` tag and a note on why they failed. Failed attempts are scientifically valuable.
- **Keep §F current.** At every session close, §F must reflect the actual next concrete step — not a vague continuation.
- **Upload set always includes the active WS file.** If a WS file is not in the upload set, it is not active. If work is needed on it, add it back.
- **If a workstream blocks mid-session:** Do not abandon the session. Immediately: (1) document the blocker with full detail in §D of the WS file, (2) set Status to BLOCKED in the WS header and describe the specific unblocking requirement in §F, (3) issue a checkpoint, (4) pivot to the secondary task. Do not end a session with a blocked workstream undocumented.

---

## §7 — Tagging Protocol

| Tag | Meaning |
|-----|---------|
| `[✓ code-verified YYYY-MM-DD]` | Script ran, number matches stated value to stated precision |
| `[✗ CORRECTED: old=X, new=Y, code-verified YYYY-MM-DD]` | Error found and corrected |
| `[✗ FAILED: reason]` | Approach attempted and failed — logged, not deleted |
| `[⚠ formula unverified: depends on X]` | Blocked — upstream input not yet checked |
| `[T-cited: REF, numerical consequence verified YYYY-MM-DD]` | Theorem from literature; numerical output independently checked |
| `[T]` | Theorem from literature (not yet independently checked) |
| `[D]` | Derived with stated assumptions |
| `[P]` | Physical/heuristic argument |
| `[F]` | Failure / kill condition |

### 7.1 Claim reclassification rules

- **Numerical claims** → must carry `[✓ code-verified YYYY-MM-DD]` or `[⚠]`. No untagged numerical claims.
- **Structural claims** → tagged `[P]` unless uniqueness is rigorously proven.
- **"Zero free parameters" claims** → tagged `[⚠]` unless ALL inputs are derived from first principles. If ANY dependency is fitted, external, or unverified → `[⚠]`.

### 7.2 Hidden dependency tracking

Any claim that depends on non-derived inputs must explicitly list those dependencies. If ANY dependency of a Tier A claim is not strictly derived → downgrade to Tier B or C. Document as: `[✗ CORRECTED: Tier A → Tier B/C, justification: hidden degrees of freedom]`.

### 7.3 Language discipline

Replace unjustified strong language:
- ~~"forces"~~ → "depends on"
- ~~"uniquely determines"~~ → "selects under assumptions"
- ~~"fixes"~~ → "consistent with"

### 7.4 Hypothesis status tags

| State | Meaning |
|-------|---------|
| `[EXPERIMENTAL]` | Newly proposed, untested |
| `[ACTIVE]` | Under active investigation |
| `[STABLE]` | Tested and holding; used as foundation for further work |
| `[ARCHIVED]` | Superseded or no longer active, but preserved for reference |
| `[REJECTED]` | Falsified or abandoned with documented reason |

---

## §8 — Integrity and Audit Systems

### 8.1 Kill condition: non-uniqueness

If alternative embeddings or RG schemes yield different coupling predictions → the uniqueness claim is false. Trigger: `[F]`.

### 8.2 Alternative enumeration requirement

All claims using "unique", "forced", or "only" MUST include at least one alternative construction tagged `[D]` (ruled out) or `[⚠]` (not yet evaluated). Claims without an enumerated alternative are automatically downgraded.

### 8.3 Empirical stress test

All Tier A and Tier B claims MUST include a falsifiable observation. If none stated → downgrade tier.

### 8.4 Periodic audit triggers and procedure

**Trigger a full re-audit** of the Reference Core when:
- (a) 5+ new numerical results since last audit
- (b) a significant structural result changed (kill condition, tier reclassification)
- (c) 10+ sessions since last audit

**When a trigger condition is met:** The re-audit runs at the START of the next session, before any new physics work, unless Chris explicitly defers it with a stated reason. Do not silently skip a triggered audit.

**What a re-audit consists of (in order):**
1. Re-derive every numerical claim in the Reference Core from scratch in code — do not check against stored values, re-derive them. The stored value is what is being audited.
2. Verify all tier assignments: for each Tier A/B claim, confirm assumptions are minimal, dependencies are derived (not fitted), and a falsifiable observation is stated. Downgrade on any failure.
3. Check all `[⚠]` flags: are any now resolvable? Flag newly unresolvable ones.
4. Check RESOLVED_KNOWLEDGE: has any settled result been invalidated by work since the last audit?
5. Cross-check Reference Core against active workstream §E (Results) tables: are there verified results in workstreams that haven't been migrated yet?
6. Output a concise audit report: entries confirmed, entries corrected, tier changes, flags added/resolved.

Flag the audit trigger proactively in CONTEXT_SNAPSHOT §E each session.

### 8.5 Re-planning triggers

Trigger a **re-planning session** when:
- (a) a kill condition is triggered or cleared
- (b) 3+ workstreams have closed since last re-plan
- (c) a major structural insight changes priority ordering
- (d) 8+ sessions since last re-plan

### 8.6 Theory audit (~every 25 sessions)

Attempt to falsify rather than defend. Identify weakest assumptions. Check resolved knowledge for invalidation. Review dependency graph for circular reasoning. Update `THEORY_HEALTH.md`.

### 8.7 High-integrity reasoning protocol

1. **Exploration** — survey the problem, identify approaches, note pitfalls.
2. **Structured derivation** — execute with full rigor, printing all intermediate steps.
3. **Critical verification** — dimensional analysis, limiting cases, symmetry checks, comparison with known results, stress testing.

### 8.8 Contradiction tracking

When a contradiction is discovered:
1. Log in `CONTRADICTION_TRACKER.md` with unique ID (e.g., `CONTRA-001`).
2. Identify the minimal set of assumptions producing the contradiction.
3. Rank resolution paths by which assumption is most likely wrong.
4. Link to the relevant failure entry and hypothesis tree nodes.

### 8.9 Self-validation at session close

Before emitting the ROS SELF-AUDIT SUMMARY, run all of the following checks. This is a lightweight version of the full meta-analysis checklists — it runs every session.

**Briefing audit:**
- Untagged claims → `[F]`
- Unsupported `[D]` tags (no derivation shown) → `[F]`
- Unjustified uniqueness claims → `[F]`
- State/status content present in the Briefing → `[F: Briefing overload]`

**Workstream audit:**
- Physics work done without a WS file → `[F: WS compliance violation]`
- WS file modified but not output at session close → `[F: WS compliance violation]`
- Active WS not in next session's upload set → `[F: WS compliance violation]`
- WS §F not updated with concrete next steps → `[F: WS compliance violation]`

**Cross-file consistency (lightweight — run every session):**
- Any result verified this session → confirm it is in WS §E AND queued for migration to Reference Core
- Any hypothesis state change → confirm HYPOTHESIS_TREE.md is in the output set
- Any failure opened or resolved → confirm FAILURE_LEDGER.md is in the output set
- Any kill condition change → confirm Reference Core, FAILURE_LEDGER, RESEARCH_DEPENDENCY_GRAPH, THEORY_HEALTH are all in the output set
- Any settled result → confirm it is queued for RESOLVED_KNOWLEDGE.md

**Output file integrity:**
- Scan every file being output this session for: nested fenced code blocks (a ` ``` ` block containing another ` ``` ` or ` ```lang ` — renders as raw text), unclosed bold/italic markers (`**` without closing `**`), broken table rows (mismatched `|` counts)
- Any rendering issue found → fix before output, log in self-audit

**Tier audit:**
- For each Tier A/B claim touched this session — assumptions minimal, no hidden parameters, falsifiable observation present. Fail → downgrade.

**Kill condition audit:**
- All relevant KCs applied to this session's results. No implicit violations. Triggered → `[F]`.

---

## §9 — Decision-Making

- **Claude decides the research direction by default.** Evaluate the full landscape — all open failures, kill conditions, active workstreams, dependencies, big picture — and choose the highest-impact next step. State reasoning briefly so Chris can override, but do not present menus or ask Chris to choose unless there is a genuine value-judgment fork.
- **If the project needs to change direction, say so.** If a result invalidates a line of work, or a new insight opens a better path, propose the pivot with reasoning.

---

## §10 — Computational Environment

### 10.1 Paths

| Purpose | Path |
|---------|------|
| **Project root** | `/Users/cdowd/Projects/E8-THEORY` |
| **Downloads folder** | `/Users/cdowd/Downloads` |
| **Python scripts** | `/Users/cdowd/Projects/E8-THEORY/scripts/` |

### 10.2 Terminal commands at session close

At session close, print exact shell commands to move every downloaded file into its correct project location. This block is mandatory inside the ⚡ Quick Reference.

**New file:** `mv "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E8-THEORY/PATH/FILENAME.md"`
**Updated file:** `cp "/Users/cdowd/Downloads/FILENAME.md" "/Users/cdowd/Projects/E8-THEORY/PATH/FILENAME.md"`
**After all moves:** `cd "/Users/cdowd/Projects/E8-THEORY" && git add -A && git commit -m "session-NNN: <description>"`

### 10.3 Git policy

- Commit messages reference session numbers: `session-014: WS-3875 CG coefficient computed`
- No copyrighted material, secrets, credentials, or large binary files
- Text-only repo

---

## §11 — Meta-Evolution

Meta-analysis is not continuous — it runs on explicit triggers (§11.1) or on the periodic schedule (§11.2). When it runs, it uses the structured checklists below. All findings and changes are logged in `META_RESEARCH_LOG.md` with session number and rationale.

### 11.1 Meta-analysis triggers

Run a meta-analysis when ANY of the following occur:

- A major contradiction appears in the theory
- Progress stalls across 3+ consecutive sessions
- A major theory rewrite is being considered
- Significant friction is noticed in the research workflow (e.g., files hard to navigate, rules unclear, repeated errors of the same type)
- A pattern of the same class of error appears across sessions (e.g., files repeatedly going stale, the same routing violation recurring)
- Approaching session 10, 20, 30... (scheduled — see §11.2)

Do NOT run meta-analysis speculatively between triggers. It consumes session capacity that should go to physics.

### 11.2 Periodic schedule

| Interval | What runs |
|----------|-----------|
| Every ~10 sessions | Full ROS health check (§11.3) + File system audit (§11.4) |
| Every ~25 sessions | Theory audit (§11.5) |
| Any session meta-analysis is triggered | Cross-file consistency audit (§11.6) — always included |

### 11.3 ROS health check (~every 10 sessions)

Evaluate whether the research operating system itself is working. Go through each question and log findings:

**Session protocol:**
- Is the session start protocol being followed? Are files being read in the right order?
- Is the Quick Reference block appearing at every session close?
- Are checkpoints being issued at the right moments, or too frequently / not enough?
- Are trigger checks (audit, re-plan, theory audit) being evaluated and acted on, or silently skipped?

**Workstream discipline:**
- Are workstreams being created proactively, or is physics work happening without them?
- Are WS §D derivation logs being kept current, or are they sparse?
- Are WS §F next steps concrete, or vague?
- Are closed workstreams being properly archived, or lingering in the active set?
- Is ARCHIVE_MANIFEST being updated when workstreams close?

**Knowledge tracking:**
- Are RESOLVED_KNOWLEDGE entries being added when results are settled?
- Is HYPOTHESIS_TREE being updated when hypothesis states change?
- Is FAILURE_LEDGER reflecting current failure status, or is it stale?
- Are migrations (WS → Reference Core, WS → Discovery Log) being logged with `[MIGRATION:]` tags?

**File routing:**
- Is any state accumulating in the Briefing (§§ that should be in CONTEXT_SNAPSHOT)?
- Is any derivation content appearing in the Reference Core?
- Is CONTEXT_SNAPSHOT being fully replaced each session, or just appended?

**Efficiency:**
- Is the upload set minimal, or has it grown?
- Are sessions reading files they don't need?
- Is the Briefing growing with one-off rules that should be generalized or removed?

### 11.4 File system audit (~every 10 sessions)

A structural check of the repository:

**Content integrity:**
- Do any files contain orphaned references (links to files that no longer exist or have been renamed)?
- Do any files contain open work items (e.g., `(not yet computed)`, `TBD`, `to be created`) that should be in a workstream instead?
- Do any files contain content that belongs in a different file per §5.1 routing rules?
- Are there any dead `[⚠]` flags that have been resolved in workstreams but not updated in the Reference Core?

**Markdown and formatting:**
- Do all files render correctly? Check specifically for: nested fenced code blocks (renders as raw text), unclosed bold/italic markers, broken table formatting, headers at wrong depth.
- Are tagging conventions consistent across files (§7)?
- Are all status tags from the known set (`[✓]`, `[⚠]`, `[D]`, `[P]`, `[T]`, `[F]`, `[✗]`)?

**Structural health:**
- Are any folders consistently empty or unused? Consider removing or consolidating.
- Have files accumulated outside the defined structure?
- Are naming conventions consistent? Fix drift.
- Is the archive growing in a way that needs subcategorization?
- Is ARCHIVE_MANIFEST current with all archived workstreams?

**Cross-file staleness** (run the §11.6 checklist):
- See §11.6 for the full cross-file consistency audit.

### 11.5 Theory audit (~every 25 sessions)

A structured attempt to stress-test the theory rather than advance it:

1. **Falsification attempt** — for each Tier A and Tier B prediction, identify the single most likely way it could be wrong. Is there a computational check that would reveal this? Run it.
2. **Weakest assumption identification** — list the five weakest `[P]` claims in the logical chain. What would it take to strengthen or refute each?
3. **Resolved knowledge validation** — has any result in `RESOLVED_KNOWLEDGE.md` been implicitly undermined by subsequent work? Check each RK entry against current theory state.
4. **Circular dependency scan** — review `RESEARCH_DEPENDENCY_GRAPH.md` for hidden circular reasoning. Are any predictions dependent on inputs that were fitted to match those predictions?
5. **Kill condition stress test** — for each non-triggered kill condition, is there a concrete computation that would trigger it? If no such computation exists, the kill condition may not be well-defined.
6. **Update `THEORY_HEALTH.md`** with revised assessment.

### 11.6 Cross-file consistency audit (runs with every meta-analysis)

This checklist catches the class of errors where work happens in one file but dependent files are not updated. Run through every item:

**When a workstream produces a verified result:**
- [ ] Is the result in WS §E (Results)?
- [ ] Has it been migrated to `E8_Reference_Core.md` with a `[MIGRATION:]` tag?
- [ ] If it is a major finding, has it been added to `DISCOVERY_LOG.md`?
- [ ] If it is now settled knowledge, has it been added to `RESOLVED_KNOWLEDGE.md`?
- [ ] If it corrects a stored error, has the error been corrected in Reference Core with `[✗ CORRECTED:]`?

**When a hypothesis state changes:**
- [ ] Is `HYPOTHESIS_TREE.md` updated with the new status?
- [ ] Does the hypothesis description still accurately reflect the current mechanism (not an outdated one)?
- [ ] Is the workstream pointer current?

**When a failure is resolved or opened:**
- [ ] Is `FAILURE_LEDGER.md` updated (moved to resolved, or new entry added)?
- [ ] Is `CONTEXT_SNAPSHOT.md §D` (Open Failures) consistent with FAILURE_LEDGER?
- [ ] If a workstream was created to address the failure, is it linked in the FAILURE_LEDGER entry?

**When a kill condition status changes:**
- [ ] Is `FAILURE_LEDGER.md` KC tracker updated?
- [ ] Is `RESEARCH_DEPENDENCY_GRAPH.md` KC table updated?
- [ ] Is `THEORY_HEALTH.md` scorecard updated?
- [ ] Is `CONTEXT_SNAPSHOT.md` updated?

**When the theory structure changes (new mechanism, reclassification, new derivation):**
- [ ] Is a new entry added to `THEORY_EVOLUTION_GRAPH.md`?
- [ ] Is the dependency chain in `RESEARCH_DEPENDENCY_GRAPH.md` updated?
- [ ] Is `THEORY_HEALTH.md` updated if metrics changed?
- [ ] If major enough, is a `THEORY_SNAPSHOT` warranted?

**File-level staleness check:**
- [ ] Does `RESOLVED_KNOWLEDGE.md` contain entries for all results settled in recent sessions?
- [ ] Does `HYPOTHESIS_TREE.md` reflect the current state of all active/rejected hypotheses?
- [ ] Does the Reference Core contain any references to files that no longer exist?
- [ ] Does the Reference Core contain any `(not yet computed)` or open work items that should be in a workstream?
- [ ] Is `ARCHIVE_MANIFEST.md` current with all files in `05_ARCHIVE/completed_workstreams/`?

### 11.7 ROS improvement policy

When a meta-analysis identifies a problem with the research operating system itself:

1. **Diagnose the root cause**, not just the symptom. A stale HYPOTHESIS_TREE is a symptom — the root cause is that there is no rule requiring it to be updated when a WS session produces hypothesis-relevant results.
2. **Fix the rule, not just the instance.** Update the Briefing to prevent recurrence. A one-off fix that doesn't change the system will produce the same error again.
3. **Log the change in `META_RESEARCH_LOG.md`**: what was broken, what the root cause was, what rule was added or changed, and the session number.
4. **Bump the ROS version** in the Briefing header (e.g., v3.1 → v3.2) when a substantive rule change is made. Minor clarifications do not require a version bump.

The ROS version history should be traceable via `META_RESEARCH_LOG.md` and git commit messages.

### 11.8 AI platform awareness

Claude is the default research platform. Switching to other systems (OpenAI, Gemini) should be rare and justified — only for tasks that do not require project files and benefit from independent reasoning checks. Log platform switches in `META_RESEARCH_LOG.md`.

---

*End of session briefing — Research Operating System v3.1*
*This file contains operating rules only. Current project state is in CONTEXT_SNAPSHOT.md.*
