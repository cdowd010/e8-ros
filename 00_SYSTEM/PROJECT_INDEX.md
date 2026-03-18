# PROJECT_INDEX.md
Research Project Navigation Map

---

# Purpose

This document provides a **high-level map of the research project structure**.

It allows both the researcher and AI systems to quickly understand:

- where information is stored
- which files are important for each session
- how the research operating system is organized

This file should remain **short, stable, and easy to scan**.

Detailed workflow rules are defined in:

`E8_Session_Briefing.md`

---

# Core System Files

Location: `00_SYSTEM/`

These files define the **research operating system**.

- `E8_Session_Briefing.md`  
  Main research workflow and session instructions.

- `E8_Reference_Core.md`  
  Condensed results, key numbers, prediction ledger, status. Always upload.

- `CONTEXT_SNAPSHOT.md`  
  Short summary of the current state of the project.  
  This file should be read at the **start of every session**.

- `THEORY_HEALTH.md`  
  Overview of the current status of the theory.

- `PROJECT_INDEX.md`  
  This navigation document.

---

# Knowledge Layer

Location: `01_KNOWLEDGE/`

These files contain **structured knowledge generated during research**.

- `DISCOVERY_LOG.md`  
  Records major discoveries made during the research process.

- `RESOLVED_KNOWLEDGE.md`  
  Contains results considered stable and no longer needing re-derivation.

- `HYPOTHESIS_TREE.md`  
  Tracks competing theoretical paths and their current status.

- `CONCEPT_REGISTRY.md`  
  Canonical definitions of important theoretical objects.

- `PARAMETER_REGISTRY.md`  
  Registry of constants, couplings, and parameters used in the theory.

- `THEORY_EVOLUTION_GRAPH.md`  
  Tracks major revisions and structural changes in the theory.

- `RESEARCH_DEPENDENCY_GRAPH.md`  
  Maps dependencies between axioms, assumptions, derivations, predictions, and tests.

- `THEORY_SNAPSHOTS/`  
  Contains snapshots of the theory at major milestones. First snapshot to be created during Phase 2 re-evaluation.

---

# Active Research Workstreams

Location: `02_WORKSTREAMS/`

Each workstream represents a **focused research investigation**.

Currently empty — `E8_WS_CKM2.md` pending move to archive. New workstreams (e.g., `E8_WS_3875.md`) will be created after Phase 2 re-evaluation.

---

# Reference Materials

Location: `03_REFERENCE/`

Contains external reference tracking and original research notes.

- `PAPER_INDEX.md`  
  Citation index with arXiv/DOI links. **No copyrighted content stored.**

- `NOTES/`  
  Original research notes only — no third-party content.

---

# Meta Research Layer

Location: `04_META/`

Tracks the **research process itself**.

- `SESSION_LEDGER.md`  
  Log of research sessions.

- `FAILURE_LEDGER.md`  
  Records unresolved problems or theoretical failures.

- `CONTRADICTION_TRACKER.md`  
  Tracks conflicts between theoretical results.

- `META_RESEARCH_LOG.md`  
  Records improvements to the research operating system or workflow.

---

# Archive

Location: `05_ARCHIVE/`

Stores historical material to keep the active workspace clean.

- `completed_workstreams/`  
  Archived workstream files (E8_WS_Alpha3.md, E8_WS_CGC.md, E8_WS_CKM.md, E8_WS_N15.md, E8_WS_CKM2.md).

- `deprecated_theories/`  
  Future use.

- `old_theory_snapshots/`  
  Future use.

---

# Session Startup Priority

At the beginning of each research session review:

1. `CONTEXT_SNAPSHOT.md`
2. `PROJECT_INDEX.md`
3. `SESSION_LEDGER.md`
4. `FAILURE_LEDGER.md`

This provides orientation for continuing the research.

---

# Research Philosophy

The research system is designed to support:

- long-horizon theoretical exploration
- structured hypothesis development
- high-integrity reasoning
- efficient AI-assisted collaboration

The theory is allowed to evolve significantly if evidence justifies it.

Major structural changes should always be:

- documented
- justified
- tracked in the theory evolution systems

---

# Maintenance Rules

Keep this document:

- concise
- accurate
- aligned with the current folder structure

Avoid adding detailed research notes here.

This file should remain a **navigation map**, not a research log.
