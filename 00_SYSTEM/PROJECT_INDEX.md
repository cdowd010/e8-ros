# PROJECT_INDEX.md
## Research Project Navigation Map

**Last updated:** 2026-03-18 (Session 7 — ROS v3.3)

---

## Purpose

High-level map of the research project structure. Allows both the researcher and AI systems to quickly understand where information is stored, which files are important for each session, and how the research operating system is organized.

This file should remain **short, stable, and easy to scan**. Detailed workflow rules are in `E8_Session_Briefing.md`. Current project state is in `CONTEXT_SNAPSHOT.md`.

---

## Session Startup — What to Read and Upload

### Upload set (every session)
| File | Location | Purpose |
|------|----------|---------|
| `E8_Session_Briefing.md` | `00_SYSTEM/` | Operating rules — rarely changes |
| `E8_Reference_Core.md` | `00_SYSTEM/` | Master results ledger |
| `CONTEXT_SNAPSHOT.md` | `00_SYSTEM/` | **Current session state — read this first** |
| `E8_WS_[Name].md` | `02_WORKSTREAMS/` | **Active workstream — always upload when doing physics** |

**Rule:** If physics work is happening, a workstream file must be in the upload set. No workstream = admin/planning session only.

### Session start reading order
1. `CONTEXT_SNAPSHOT.md` — orientation, active WS files, open failures, next plan
2. Active workstream file — current derivation state and next steps
3. `E8_Reference_Core.md` — prediction ledger
4. Other files from repo only if specifically needed

---

## File System Architecture

### `00_SYSTEM/` — Research Operating System

| File | Role | Changes |
|------|------|---------|
| `E8_Session_Briefing.md` | Operating rules and protocols (ROS v3.3) | Rarely — only when rules change |
| `E8_Reference_Core.md` | Stable verified results and predictions | Every session (new results) |
| `CONTEXT_SNAPSHOT.md` | Current session state + active WS list | Every session (full replacement) |
| `THEORY_HEALTH.md` | Theory health dashboard | When health metrics change |
| `PROJECT_INDEX.md` | This navigation document | When structure changes |

### `01_KNOWLEDGE/` — Structured Knowledge

| File | Role | Changes |
|------|------|---------|
| `DISCOVERY_LOG.md` | Final major results only | When a major result is established |
| `RESOLVED_KNOWLEDGE.md` | Settled facts no longer needing re-derivation | When knowledge is settled |
| `HYPOTHESIS_TREE.md` | Competing theoretical paths and their status | When hypothesis states change |
| `CONCEPT_REGISTRY.md` | Canonical definitions of theoretical objects | When new concepts are defined |
| `PARAMETER_REGISTRY.md` | Constants, couplings, parameters and provenance | When parameters are updated |
| `THEORY_AUDIT_CHECKLIST.md` | Theory-specific audit targets — highest-risk claims, KC proximity, PDG benchmarks, literature topics. Updated after each theory audit. | When a theory audit runs |
| `RESEARCH_DEPENDENCY_GRAPH.md` | Dependency map + research radar | When dependencies or priorities change |
| `THEORY_SNAPSHOTS/` | Theory snapshots at major milestones | At major structural changes |

### `02_WORKSTREAMS/` — Active Physics Work

**Every active line of investigation has a workstream file. All derivations live here.**

| File | Title | Status | Priority |
|------|-------|--------|----------|
| `E8_WS_3875.md` | CKM Mixing from the 3875 Representation | **ACTIVE** | 1 — critical path |
| `E8_WS_F4_TopMass.md` | Top Mass 11% Discrepancy — QCD Correction | OPEN | 3 |

See `CONTEXT_SNAPSHOT.md §B` for current workstream status and upload instructions.

Workstream lifecycle: OPEN → ACTIVE → (BLOCKED) → CLOSED → `05_ARCHIVE/completed_workstreams/`

Full workstream protocol in `E8_Session_Briefing.md §6`.

### `03_REFERENCE/` — External References

| File | Role |
|------|------|
| `PAPER_INDEX.md` | Citation index with arXiv/DOI links — **no copyrighted content** |
| `NOTES/` | Original research notes only |

### `04_META/` — Research Process Tracking

| File | Role | Changes |
|------|------|---------|
| `SESSION_LEDGER.md` | Log of research sessions (one row per session) | Every session |
| `FAILURE_LEDGER.md` | Unresolved problems and theoretical failures | When failures open or close |
| `CONTRADICTION_TRACKER.md` | Conflicts between theoretical results | When contradictions found/resolved |
| `META_RESEARCH_LOG.md` | Improvements to the research operating system | When ROS changes made |

### `05_ARCHIVE/` — Historical Material

| Folder | Contents |
|--------|----------|
| `completed_workstreams/` | E8_WS_Alpha3.md, E8_WS_CGC.md, E8_WS_CKM.md, E8_WS_N15.md, E8_WS_CKM2.md |
| `deprecated_theories/` | Future use |
| `old_theory_snapshots/` | Future use |

---

## File Ownership Rules (Summary)

Every piece of content belongs to exactly one file:

| Content type | Belongs in |
|-------------|-----------|
| Active derivations, reasoning, intermediate results | `E8_WS_*.md` (workstream) |
| Stable, verified, finalized results | `E8_Reference_Core.md` |
| Current project state, open failures, next plan | `CONTEXT_SNAPSHOT.md` |
| Theory structural changes | `THEORY_EVOLUTION_GRAPH.md` |
| Research priorities and dependency map | `RESEARCH_DEPENDENCY_GRAPH.md` |
| Operating rules | `E8_Session_Briefing.md` |

Full routing rules and violation tags: `E8_Session_Briefing.md §5`.
Full workstream protocol: `E8_Session_Briefing.md §6`.

---

## Repository Policy

- **No copyrighted material** — no PDFs, paper text, book excerpts.
- **No secrets or credentials.**
- **No large binary files** — text-only repo.
- **Commit messages reference session numbers:** `session-007: WS-3875 CG coefficient computed`
- Python scripts go in `scripts/` for version control alongside research files.

---

*Keep this document concise and accurate. It is a navigation map, not a research log.*
