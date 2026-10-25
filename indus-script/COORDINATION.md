# Coordination and research log

Updated: 25 October 2026  
Project entry point: [README.md](README.md)

## Current handoff

**Active task: IND-003 — pilot source, schema and duplicate-handling rules.**  
Status: **IN REVIEW — Codex**, updated 25 October 2026 after completing the requested draft design.  
Working branch: `indus/IND-003-pilot-schema`, based on the IND-002 source-audit branch. Last completed step: source choice, data schema, duplicate rules, five-record draft, validator and 18 passing regression tests.
Review: [PR #2](https://github.com/flysamc/game/pull/2) (depends on PR #1).  
Design: [IND-003](https://github.com/flysamc/game/blob/indus/IND-003-pilot-schema/indus-script/notes/IND-003-pilot-design.md). Draft/run instructions: [data README](https://github.com/flysamc/game/blob/indus/IND-003-pilot-schema/indus-script/data/README.md).  
IND-002 was reviewed by Claude on 25 October 2026 and accepted with additions ([review note](notes/IND-002-review-claude.md)); PR #1 is ready to merge. The additions affect IND-003/IND-004 scope and should be answered in PR #2.  
Suggested independent reviewer: **Claude**. Review and curation gates still apply before freezing data or running H001 tests.

Sam asked us to use `flysamc/game` as a shared workspace and proceed one step at a time. The summary is now the starting reference. Actual coordination happens through committed notes, task status, and reviews when a contributor's session is active; this file does not automatically invoke or synchronize assistants.

At setup, the repository's default branch was `claude/inspiring-meitner-7i6ujk`. Check the current default before branching or opening a PR; do not assume `main`.

## Task board

| ID | Task | Status | Owner | Dependency / completion evidence |
|---|---|---|---|---|
| IND-001 | Initial project summary, references, hypothesis, and coordination protocol | DONE | Codex | This initial documentation commit; no corpus analysis claimed |
| IND-002 | Verify source availability and H-351 identification/transcription | DONE | Codex; reviewed by Claude | [PR #1](https://github.com/flysamc/game/pull/1); [Claude review](notes/IND-002-review-claude.md) accepted with additions (2026-10-25) |
| IND-003 | Choose the pilot source, schema, and deduplication rules | IN REVIEW | Codex | [PR #2](https://github.com/flysamc/game/pull/2); draft, schema and validator; 18 tests pass; source/design review pending |
| IND-004 | Curate and independently review stroke-plus-cup parallels | BLOCKED | Unclaimed | Source/design review; four object crosswalks and nine face transcriptions remain; do not freeze the draft |
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

### 2026-10-25 — Codex — IND-003 design handoff

- Branch: `indus/IND-003-pilot-schema`; [PR #2](https://github.com/flysamc/game/pull/2), based on the source-audit branch. Implementation commit: [62ec337](https://github.com/flysamc/game/commit/62ec337b9bb000c21f73b482bd466d38c6cae270).
- Deliverables: explicit five-entry source choice; data contract and duplicate rules; draft JSON with twelve separate faces; three H-351 sign-number sequences; nine untranscribed faces; preserved doubt on 4581:20 and 4591:20.
- Added a JSON Schema, cross-record validator, pinned Python requirements and regression tests. Unknown metadata stays null, matching strings do not merge objects, and repeated publications do not create new artifact evidence.
- Checks: Python 3.12.14; all 18 tests pass. Normal validation exits 0; `--require-ready` correctly exits 1. Rechecked the Figure 4 inventory visually and verified local links. These are implementation/transcription checks, not independent review.
- Status: IND-003 IN REVIEW. IND-002 still IN REVIEW; neither stage has been signed off on behalf of Claude.
- Review checklist: examine the source-selection limits, H-351 mappings and uncertainty; run both validator modes; scrutinize duplicate and review rules; record actual acceptance or requested changes. Use the current board rather than earlier handoff states: accepting IND-002 alone must not downgrade the already drafted IND-003 to READY.
- Next curation: locate original photographs and crosswalks for 5498, 4444, 4456 and 4591; transcribe their nine faces; resolve physical-object duplicates and review all records before an analytical release.
- The pilot PR is stacked on PR #1. After PR #1 is merged, retarget the pilot PR to the current default branch before merging it. Keep shared coordination updates when reconciling either PR.
### 2026-10-25 — Claude — IND-002 independent review

- Branch: `indus/IND-002-source-audit`; review note [notes/IND-002-review-claude.md](notes/IND-002-review-claude.md); PR #1 review comment.
- Checks performed: paper §3–5 text (crosswalk Vats 581 = IM 77:4581 = CISI-I:H-351); supplement Fig. 4 rendered and read glyph by glyph (IDs, side codes, stroke counts 2/3/3/4/4, asterisks on the first reading-order sign of 4581.20 and 4591.20); CISI-I printed p. 230 photographs H-351 A/B/C; cross-check of all five entries against a third-party machine-readable M77 digitization.
- Findings: audit table confirmed. Qualifications: H-351 A first sign worn (supports the doubtful mark); H-351 B four strokes consistent but not unambiguous in the scan; paper also cites 5296; CISI p. 230 shows H-352–354 in the same three-sided format with different face-A labels and undocumented dotted-circle faces (M77 crosswalk unverified).
- Correction: a machine-readable M77 copy exists (joyboseroy/indus_decipher), provenance documented by its converter, reuse terms unknown; use for cross-checking only, do not commit.
- Selection-effect sizing (not an H001 test): the four-sign group occurs in 11 texts, 5 with a cup line; 255 texts have a two-sign `[X] 328` line. Recommend curating the strokes-plus-cup family and pre-registering the H001 comparison. Reviewer exposure to M77 records 4580–4597 recorded in the note.
- Status: IND-002 DONE (accepted with additions). IND-003 (PR #2, opened by Codex during this review) remains Codex's; Claude's review of PR #2 follows separately.
- Next action: Codex responds to the two open questions in the review note (curation unit; whether to register the third-party M77 copy) and decides which additions to fold into the IND-003 schema.

### 2026-10-25 — Claude — IND-002 sign-off recorded; IND-003 review

- Recorded the IND-002 acceptance in `sources/manifest.json` (`independent_review: accepted`, reviewer, date, reference, scope). With it, the IND-003 validator's source-audit blocker clears; the draft stays valid and all 18 tests still pass (checked against PR #2's code).
- Reviewed [PR #2](https://github.com/flysamc/game/pull/2#pullrequestreview-5645054459): reproduced the validator results (exit 0 / `--require-ready` exit 1) and 18 passing tests; the H-351 record matches the independently checked evidence.
- Requested before IND-004: (1) declare the strokes-plus-cup family as the search set and pre-register the H001 null and unit; (2) a per-field photo-check outcome (`confirms`/`consistent`/`illegible`/`contradicts`); (3) a surface `content` field for non-script faces; (4) optional `third_party_digitization` evidence kind for blind cross-checks; (5) plan the `000` illegible-sign convention.
- Status: IND-003 IN REVIEW with changes requested (Codex decides v0.1 merge vs v0.2). IND-004 should not start until point 1 is agreed.
- Next action: Codex replies on PR #2; Sam decides whether the third-party M77 copy may be registered.

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

