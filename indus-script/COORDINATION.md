# Coordination and research log

Updated: 25 October 2026  
Project entry point: [README.md](README.md)

## Current handoff

**Active task: IND-002 — verify sources and the H-351 case.**  
Status: **IN PROGRESS — Codex**, claimed 25 October 2026 following Sam's instruction to start.  
Working branch: `indus/IND-002-source-audit`. Last completed step: current repository and task state checked; starting source verification.  
Suggested independent reviewer: **Claude**; review not yet requested or acknowledged.

Sam asked us to use `flysamc/game` as a shared workspace and proceed one step at a time. The summary is now the starting reference. Actual coordination happens through committed notes, task status, and reviews when a contributor's session is active; this file does not automatically invoke or synchronize assistants.

At setup, the repository's default branch was `claude/inspiring-meitner-7i6ujk`. Check the current default before branching or opening a PR; do not assume `main`.

## Task board

| ID | Task | Status | Owner | Dependency / completion evidence |
|---|---|---|---|---|
| IND-001 | Initial project summary, references, hypothesis, and coordination protocol | DONE | Codex | This initial documentation commit; no corpus analysis claimed |
| IND-002 | Verify source availability and H-351 identification/transcription | IN PROGRESS | Codex | Claimed 2026-10-25; working branch `indus/IND-002-source-audit`; source verification underway |
| IND-003 | Choose the pilot source, schema, and deduplication rules | BLOCKED | Unclaimed | IND-002 reviewed; documented choice and example records |
| IND-004 | Curate and independently review stroke-plus-cup parallels | BLOCKED | Unclaimed | IND-003; versioned pilot with per-record provenance and review status |
| IND-005 | Test H001 descriptively and reproduce basic positional statistics where data support it | BLOCKED | Unclaimed | IND-004; rerunnable code, inputs, output, and limitations |
| IND-006 | Compare structural models with matched controls and held-out records | BLOCKED | Unclaimed | Adequate audited corpus and locked evaluation design |
| IND-007 | Evaluate specific semantic/phonetic readings | DEFERRED | Unclaimed | Independent anchors and predeclared rules; not dependent merely on a high model score |

## IND-002: concrete brief for the next contributor

1. Read the project summary and its primary references. Distinguish author claims from findings independently checked by this project.
2. Recheck Mahadevan's tablet paper, especially section 3 (PDF pp. 2–3) and section 5 (pp. 3–4). Verify the identity cross-reference **Vats 581 / IM 77:4581 / CISI-I:H-351**.
3. Find an accessible original photograph, plate, or reliably reproduced figure for H-351. Compare signs, side assignments, and orientation where possible. If only the author's normalized text is accessible, explicitly retain **transcription-only / image verification pending**.
4. Locate the specific parallel tablet records; do not create object IDs or infer unreported counts from the prose.
5. Check what M77/EBUDS/CISI/ICIT data are actually accessible. Distinguish sequence data from derived statistics, scans, and third-party digitizations. Record provenance, version, access terms, and whether image checks are possible. Do not send access-request emails without Sam's instruction.
6. Propose one defensible pilot source and list the remaining gaps. Preserve alternative transcriptions or interpretations.
7. Commit a compact audit at `indus-script/notes/IND-002-source-audit.md`, then update this board and the log. If materials are unavailable, document a partial result and block only the affected checks.

**Acceptance:** another contributor can follow the references and see exactly which claims were verified, which remain source-reported, and which are unresolved. Retrieval alone is not image verification. Do not mark all of IND-002 complete if a required check remains missing; use IN REVIEW or BLOCKED with the specific reason.

## Shared working protocol

- Before working, fetch the current default branch and read these two documents plus any applicable repository instructions. Claim the task by committing an owner/status update. Do not assume ownership from the suggested-contributor field.
- Use explicit states: READY, IN PROGRESS, IN REVIEW, DONE, BLOCKED, DEFERRED. Record a date, branch, and last completed step for an active task.
- Keep one active research stage at a time. A reviewer can examine its evidence, but later stages stay blocked until dependencies are met.
- Keep research files under `indus-script/`. Avoid unrelated game changes.
- For substantive tasks, use a focused branch such as `indus/IND-002-source-audit` and a small PR to the current default branch. Recheck the branch head before updating shared files. Reconcile concurrent edits without overwriting another contributor's work or force-pushing shared history.
- Use GitHub diffs and an independent review when feasible. Mark a review as pending until it has actually occurred. Do not sign off on behalf of another contributor.
- Cite the specific publication, object, page/figure, and corpus version behind each empirical statement. Use labels such as **source-reported**, **independently checked**, **hypothesis**, and **contradicted**.
- Keep raw transcriptions separate from normalization and interpretation. Record every sign merger, repair, orientation change, and exclusion.
- Record proposed tests before inspecting their decisive outcomes. Report negative results and disagreement. Do not tune an interpretation separately for each inscription.
- Commit code, compact permitted data, and reproducible result summaries together when analysis begins. Link to copyrighted plates or restricted data rather than assuming redistribution is allowed.
- End each work session with a handoff: what changed, evidence, checks performed, unresolved issues, next action, and commit/PR reference.

## Research log

### 2026-10-25 — Codex — IND-001

- Sam authorized using the existing `game` repository for this research and coordination with Claude and other contributors.
- Added the project summary, primary-source links, the provisional H001 hypothesis, the ordered approach, and this task board.
- Added a link from the repository README to the research folder.
- Evidence available: published literature and Mahadevan's normalized H-351 transcription.
- Not yet done: original image checking, a source-audited sequence corpus, pilot extraction, independent replication, statistical analysis, or translation.
- Next action: a contributor claims IND-002 and records a source audit; Claude is the suggested first reviewer/contributor.
- Review status: independent review pending.

### 2026-10-25 — Codex — IND-002 claim

- Sam instructed Codex to start the next stage.
- Confirmed IND-002 was unclaimed and no open PR duplicated it.
- Claimed source verification; independent review remains pending.
- Working branch: `indus/IND-002-source-audit`.
- Last completed step: repository and task-state inspection.

## Handoff entry template

- Date / contributor / task:
- Branch / commit / PR:
- Files changed:
- Evidence and source locations:
- Checks actually performed:
- Findings and alternative explanations:
- Unresolved gaps or disagreements:
- Task status:
- Next action:
