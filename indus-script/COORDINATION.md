# Coordination and research log

Updated: 25 October 2026  
Project entry point: [README.md](README.md)

## Current handoff

**Active task: IND-003 — pilot source, schema and duplicate-handling rules.**  
Status: **IN PROGRESS — Codex**, claimed 25 October 2026 after Sam asked to do the next step.  
Working branch: `indus/IND-003-pilot-schema`, based on the IND-002 source-audit branch. Last completed step: current files, branches and PR #1 checked; no reviews or comments were present.  
IND-002 remains **IN REVIEW** at [PR #1](https://github.com/flysamc/game/pull/1). Sam's instruction authorizes drafting the next stage while that review is pending; it does not establish source approval.  
Suggested independent reviewer: **Claude**. Review and curation gates still apply before freezing data or running H001 tests.

Sam asked us to use `flysamc/game` as a shared workspace and proceed one step at a time. The summary is now the starting reference. Actual coordination happens through committed notes, task status, and reviews when a contributor's session is active; this file does not automatically invoke or synchronize assistants.

At setup, the repository's default branch was `claude/inspiring-meitner-7i6ujk`. Check the current default before branching or opening a PR; do not assume `main`.

## Task board

| ID | Task | Status | Owner | Dependency / completion evidence |
|---|---|---|---|---|
| IND-001 | Initial project summary, references, hypothesis, and coordination protocol | DONE | Codex | This initial documentation commit; no corpus analysis claimed |
| IND-002 | Verify source availability and H-351 identification/transcription | IN REVIEW | Codex | [PR #1](https://github.com/flysamc/game/pull/1); independent review pending |
| IND-003 | Choose the pilot source, schema, and deduplication rules | IN PROGRESS | Codex | Claimed 2026-10-25 on `indus/IND-003-pilot-schema`; draft work authorized while IND-002 review remains pending |
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
- Keep one implementation stage active at a time. Sam's 2026-10-25 instruction to proceed allows IND-003 design and draft examples while IND-002 is in review. Do not treat this sequencing change as an independent review or freeze unreviewed data; later empirical tests still require their evidence dependencies.
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

### 2026-10-25 — Codex — IND-002 audit handoff

- Branch: `indus/IND-002-source-audit`; [PR #1](https://github.com/flysamc/game/pull/1). Audit content commit: [6d6a8cd](https://github.com/flysamc/game/commit/6d6a8cdd8eed2146f39ebd9dba32e9324d7fdba9).
- Files: audit note, source manifest, updated project summary and this handoff.
- Evidence: Mahadevan paper §3/§5 and supplement Figs. 2–4; CISI-I printed p. 230 (IGNCA PDF p. 266); M77 coding excerpt; Yadav et al. Methods/Fig. 12; official RMRL and ICIT pages/manual.
- Checks performed: visually compared H-351 A/B/C photographs and normalized diagrams; read five candidate IDs and stroke counts; retained doubtful initial signs on M77 4581 and 4591; recorded distinct source surface labels and export conventions; hashed downloaded PDFs.
- Findings: a tractable curation target exists, but the five examples are source-selected and cannot establish a numerical interpretation or corpus frequency.
- Gaps: four other object crosswalks and photographs, duplicate checks, complete machine-readable corpus access and reuse terms remain unresolved. These are recorded explicitly for later curation. No statistical analysis or translation was attempted.
- Next action: an independent reviewer follows the four-item checklist in the audit. Record corrections or acceptance here; only then mark IND-002 DONE and IND-003 READY. Do not infer that Claude has been invoked by this handoff.
- Status: IN REVIEW; no independent review yet.

### 2026-10-25 — Codex — IND-003 claim

- Sam instructed Codex to do the next step.
- Checked the default branch, IND-002 branch, repository instructions, PR #1 reviews and comments. No independent review was present; IND-003 was unclaimed.
- Claimed pilot source choice, schema, duplicate-handling rules and draft example records. IND-002 stays IN REVIEW, and analytical release remains gated on review and curation.
- Working branch: `indus/IND-003-pilot-schema`; will open a focused PR against the audit branch so its changes can be reviewed separately.

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

