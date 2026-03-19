# PROTOCOL_ROSHealth.md
## ROS Health Check — Full Procedure
*Research Operating System v3.3 | Upload only for ROS health check sessions*

---

A ROS health check evaluates whether the research operating system itself is working — not the physics. It runs on the schedule and triggers defined in `E8_Session_Briefing.md §11`. Always run the cross-file consistency audit (§D) alongside any meta-analysis.

---

## §A — ROS Health Check (~every 10 sessions)

Evaluate whether the research operating system is working. Go through each question and log findings:

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
- **Root cause check:** For any file found to be stale, is there a documented rule in the Briefing that requires it to be updated when the relevant event occurs? If no such rule exists, that is the root cause — add the rule, don't just fix the instance.

**File routing:**
- Is any state accumulating in the Briefing (§§ that should be in CONTEXT_SNAPSHOT)?
- Is any derivation content appearing in the Reference Core?
- Is CONTEXT_SNAPSHOT being fully replaced each session, or just appended?
- **Universality check:** Has any theory-specific content crept back into the Briefing (specific claim names, formula references, current workstream names, named failures)? The Briefing contains universal rules only — any theory-specific content belongs in CONTEXT_SNAPSHOT, THEORY_AUDIT_CHECKLIST, or the relevant knowledge file.

**Efficiency:**
- Is the upload set minimal, or has it grown?
- Are sessions reading files they don't need?
- Is the Briefing growing with one-off rules that should be generalized or removed?

---

## §B — File System Audit (~every 10 sessions)

A structural check of the repository:

**Content integrity:**
- Do any files contain orphaned references (links to files that no longer exist or have been renamed)?
- Do any files contain open work items (e.g., `(not yet computed)`, `TBD`, `to be created`) that should be in a workstream instead?
- Do any files contain content that belongs in a different file per §5.1 routing rules?
- Are there any dead `[⚠]` flags that have been resolved in workstreams but not updated in the Reference Core?

**Markdown and formatting:**
- Do all files render correctly? Check specifically for: nested fenced code blocks (renders as raw text), unclosed bold/italic markers, broken table formatting, headers at wrong depth.
- Are tagging conventions consistent across files (§7 of the Briefing)?
- Are all status tags from the known set (`[✓]`, `[⚠]`, `[D]`, `[P]`, `[T]`, `[F]`, `[✗]`)?

**Structural health:**
- Are any folders consistently empty or unused? Consider removing or consolidating.
- Have files accumulated outside the defined structure?
- Are naming conventions consistent? Fix drift.
- Is the archive growing in a way that needs subcategorization?
- Is ARCHIVE_MANIFEST current with all archived workstreams?

**Cross-file staleness** — run the §D checklist below.

---

## §C — System Design Audit — Level 2/3 (runs with every ROS health check)

The checks in §A–§B are Level 1: they verify compliance with existing rules. They cannot detect rules that are wrong, rules that are missing, or failure modes the system was never designed to catch. This section addresses Level 2 (is the design right?) and Level 3 (what are we not seeing?).

Run this section **after** completing §A–§B, not before. The compliance results are the raw material for the design audit.

**Run these five techniques in order:**

---

**Technique 1 — Fresh-eyes simulation**

Before reviewing any session outputs or compliance results, write a one-paragraph answer to this question from a cold start:

> *"If a researcher joined this project today with no prior context, what would confuse them, seem poorly organized, or prompt immediate questions about how the system works?"*

This must be written before re-reading any project files — context contaminates the perspective. The goal is to surface what is invisible to someone inside the system.

Then check: is any item raised by this simulation currently unaddressed? If yes, it is a gap.

---

**Technique 2 — Failure mode enumeration (inversion)**

For each major component of the ROS, ask: *"How could this fail silently, without anyone noticing until significant damage is done?"* Do not ask whether it is working — ask how it could break invisibly.

Components to invert:

| Component | Key inversion question |
|-----------|----------------------|
| Workstream protocol | How could physics work happen outside workstreams without triggering a violation flag? |
| Knowledge file tracking | How could verified results fail to reach RESOLVED_KNOWLEDGE, HYPOTHESIS_TREE, or FAILURE_LEDGER without detection? |
| File routing | How could the wrong content accumulate in the wrong file across many sessions without being caught? |
| Reference Core | How could the prediction ledger silently drift out of sync with actual current theory state? |
| Meta-analysis itself | How could a meta-analysis run and appear to pass while missing a major systemic problem? |
| Theory audit | How could the THEORY_AUDIT_CHECKLIST become stale and misdirect a theory audit without anyone noticing? |
| Session close protocol | How could a session close appear complete while leaving a significant gap in the file system? |

For each component: enumerate the top 1–2 silent failure modes. Then check: does the current system have a detection mechanism for each one? If not, that is a gap. Add the rule or check that would catch it.

---

**Technique 3 — Adversarial audit of the audit**

After completing §A–§B and Techniques 1–2, ask:

> *"What did this meta-analysis not check? What questions did it not ask? What would a critic of this meta-analysis say was missed?"*

Write the answer explicitly — do not just think it. If the answer is "nothing," the audit has not been adversarial enough. A well-functioning meta-analysis should reliably surface at least one gap in itself.

Then ask: is the gap a one-time miss, or evidence of a structural blind spot in how the meta-analysis is designed? If structural, add it to the known blind spots register (§C output below).

---

**Technique 4 — Historical pattern scan**

Review `SESSION_LEDGER.md` and `META_RESEARCH_LOG.md` for the last 10 sessions. Look for:

- The same routing violation appearing more than once
- The same file going stale repeatedly
- Problems that were fixed in a previous meta-analysis but have reappeared
- Friction points mentioned across multiple sessions
- Rules that are consistently not being followed despite being documented

A single violation is an individual failure. The same violation appearing twice is a pattern. A pattern means the rule that was supposed to prevent it is either unclear, missing, or insufficient. Identify the pattern, diagnose the rule gap, fix the rule.

---

**Technique 5 — The researcher question test**

Ask:

> *"Are there questions about how this system is working that a thoughtful researcher stepping back would ask — questions that the current meta-analysis has no mechanism to surface or answer?"*

This is the most open-ended technique and the most important. It directly asks whether the system is examining itself from the right angles. The most valuable improvements to this ROS have come from questions asked from outside it, not from compliance checks run inside it.

If yes — add a check, a question, or a technique that would surface those questions in future meta-analyses. The goal is to gradually transfer the researcher's perspective-shifting ability into the system itself.

---

**§C Output (required at every ROS health check):**

Log the following in `META_RESEARCH_LOG.md` under the current session entry:

1. **Fresh-eyes paragraph** — the one-paragraph simulation output, verbatim
2. **Silent failure modes found** — any failure modes from Technique 2 that lack a detection mechanism, with the gap and the fix
3. **Adversarial audit findings** — what the meta-analysis missed, and whether it is a one-time miss or a structural blind spot
4. **Patterns identified** — any recurring problems from Technique 4, with root cause and rule change
5. **New researcher questions** — any questions from Technique 5 that the system couldn't previously answer, with the mechanism added to surface them in future

If all five outputs are "none found," log that explicitly with brief reasoning. Do not skip the output step — an undocumented finding is a lost finding.

**Known blind spots register:**

`META_RESEARCH_LOG.md` maintains a running section called `## Known Blind Spots` at the top of the file. When Technique 3 reveals a structural blind spot — a category of problem the system was not designed to see — log it here:

```
### BS-NNN: [Short label]
**Discovered:** Session N, [date]
**Description:** What the blind spot was — what category of problem was invisible
**Root cause:** Why the system couldn't see it
**Detection mechanism added:** What rule, check, or technique was added
**Status:** [OPEN — no fix yet | ADDRESSED — fix added session N]
```

This register is the institutional memory of the system's self-improvement. It answers the question "have we been here before?" when a new meta-analysis finds something unexpected.

---

## §D — Cross-File Consistency Audit (runs with every meta-analysis)

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

**When a theory audit completes:**
- [ ] Have all files listed in `PROTOCOL_TheoryAudit.md §J` been updated before closing the audit session?

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
- [ ] Is `THEORY_AUDIT_CHECKLIST.md` current? Specifically: does its KC proximity table reflect current KC statuses? Do its [P]/[D] priority targets reflect the current logical chain? Were its literature topics updated after the last theory audit? If a theory audit has run since the checklist was last updated, the checklist is stale.

---

## §E — ROS Improvement Policy

When a meta-analysis identifies a problem with the research operating system itself:

1. **Diagnose the root cause**, not just the symptom. A stale HYPOTHESIS_TREE is a symptom — the root cause is that there is no rule requiring it to be updated when a WS session produces hypothesis-relevant results.
2. **Fix the rule, not just the instance.** Update the Briefing to prevent recurrence. A one-off fix that doesn't change the system will produce the same error again.
3. **Choose the right home for the fix.** Not every fix belongs in the Briefing:
   - If the fix is a universal procedural rule → add it to the Briefing.
   - If the fix is theory-specific content that will need updating over time → create or update a dedicated file (e.g., `THEORY_AUDIT_CHECKLIST.md`), not the Briefing. Embedding theory-specific content in rule documents is the root cause of content drift.
   - If the fix is current project state → it belongs in `CONTEXT_SNAPSHOT.md`.
4. **Log the change in `META_RESEARCH_LOG.md`**: what was broken, what the root cause was, what rule or file was added or changed, and the session number.
5. **Bump the ROS version** in the Briefing header (e.g., v3.2 → v3.3) when a substantive rule change is made. Minor clarifications do not require a version bump.

The ROS version history should be traceable via `META_RESEARCH_LOG.md` and git commit messages.

---

*This file contains the ROS health check procedure only. Schedule, triggers, and upload instructions are in `E8_Session_Briefing.md §11`.*
