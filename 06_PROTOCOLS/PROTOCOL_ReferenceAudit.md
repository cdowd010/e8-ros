# PROTOCOL_ReferenceAudit.md
## Reference Core Re-Audit — Full Procedure
*Research Operating System v3.3 | Upload only for Reference Core re-audit sessions*

---

A Reference Core re-audit numerically re-verifies the prediction ledger and checks tier assignments from scratch. It runs at the **start** of the triggered session, before any new physics work.

**Model:** Sonnet is sufficient for mechanical re-derivation and tier checks. Use Opus only if the audit surfaces a structural issue requiring creative reasoning.

---

## §A — Procedure (run in order)

1. **Re-derive every numerical claim** in the Reference Core from scratch in code. Do not check against stored values — re-derive them independently. The stored value is what is being audited.

2. **Verify all tier assignments.** For each Tier A/B claim: confirm assumptions are minimal, dependencies are derived (not fitted), and a falsifiable observation is stated. Downgrade on any failure.

3. **Check all `[⚠]` flags.** Are any now resolvable given work done since they were raised? Flag any that have become newly unresolvable.

4. **Check `RESOLVED_KNOWLEDGE.md`.** Has any settled result been invalidated by work since the last audit?

5. **Cross-check Reference Core against active workstream §E (Results) tables.** Are there verified results in workstreams that haven't been migrated yet? If so, migrate now with `[MIGRATION:]` tags.

6. **Output a concise audit report** in `META_RESEARCH_LOG.md`: entries confirmed, entries corrected, tier changes, flags added/resolved.

---

## §B — Mandatory Output

- `E8_Reference_Core.md` — updated with any corrections, tier changes, new/resolved `[⚠]` flags, and `[✗ CORRECTED:]` tags
- `META_RESEARCH_LOG.md` — audit report entry (session number, date, summary of findings)
- `CONTEXT_SNAPSHOT.md §E` — reset the "results since last audit" counter to 0; record the audit date

---

*This file contains the Reference Core re-audit procedure only. Trigger conditions and scheduling rules are in `E8_Session_Briefing.md §8.4`.*
