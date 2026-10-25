# Coordination and research log

Updated: 25 October 2026  
Project entry point: [README.md](README.md)

## Current handoff

**Active handoff: IND-004 — five-record pilot curation and v0.2 schema corrections.**  
Status: **IN REVIEW — Codex**, 25 October 2026.  
Review [PR #4](https://github.com/flysamc/game/pull/4), stacked on [PR #2](https://github.com/flysamc/game/pull/2). [Curation note and exact source checklist](https://github.com/flysamc/game/blob/indus/IND-004-pilot-curation/indus-script/notes/IND-004-pilot-curation.md); [current data guide](https://github.com/flysamc/game/blob/indus/IND-004-pilot-curation/indus-script/data/README.md).  
Completed: all 12 normalized faces; [Claude accepted the source addendum, crosswalks and five pilot identities](https://github.com/flysamc/game/pull/4#pullrequestreview-5645307407). His three corrections are applied: H-322 A and H-977 B normalization outcomes are now qualified; H-977 C retains both its M77 sign encoding and an explicitly inferred CISI motif assessment. Photo outcomes total 9 confirms / 8 consistent; both source-doubt marks remain. Thirty-five tests pass. Record-level transcription/content review and a frozen release remain pending.  
Acceptance is scoped: Claude did not independently check Vats I pp. 348/351 item-to-find links. No corpus-wide duplicate or production-group independence is claimed. [Review response and remaining checks](https://github.com/flysamc/game/blob/indus/IND-004-pilot-curation/indus-script/notes/IND-004-review-response.md). IND-002 is DONE and [PR #1](https://github.com/flysamc/game/pull/1) is merged. IND-003/004 remain IN REVIEW.  
The broader strokes-plus-cup family remains the subsequent search target; these five are a workflow pilot. [H001 proposal #3](https://github.com/flysamc/game/pull/3) is at Claude's revision 3 and remains unlocked. No expanded label-by-count tabulation or H001 test was run. The pinned public third-party copy was used only to cross-check the 12 exposed pilot sequences; no raw corpus or scans are committed.

Sam asked us to use `flysamc/game` as a shared workspace and proceed one step at a time. The summary is now the starting reference. Actual coordination happens through committed notes, task status, and reviews when a contributor's session is active; this file does not automatically invoke or synchronize assistants.

At setup, the repository's default branch was `claude/inspiring-meitner-7i6ujk`. Check the current default before branching or opening a PR; do not assume `main`.

## Task board

| ID | Task | Status | Owner | Dependency / completion evidence |
|---|---|---|---|---|
| IND-001 | Initial project summary, references, hypothesis, and coordination protocol | DONE | Codex | This initial documentation commit; no corpus analysis claimed |
| IND-002 | Verify source availability and H-351 identification/transcription | DONE | Codex; reviewed by Claude | [PR #1](https://github.com/flysamc/game/pull/1); [Claude review](notes/IND-002-review-claude.md) accepted with additions (2026-10-25) |
| IND-003 | Choose the pilot source, schema, and deduplication rules | IN REVIEW | Codex; reviewed by Claude | [PR #2](https://github.com/flysamc/game/pull/2); requested changes implemented in v0.2 [PR #4](https://github.com/flysamc/game/pull/4), awaiting review |
| IND-004 | Curate and independently review stroke-plus-cup parallels | IN REVIEW | Codex; crosswalks reviewed by Claude | [PR #4](https://github.com/flysamc/game/pull/4): source addendum and five pilot identities accepted; three corrections applied; record-level transcription/content review and broader family curation pending |
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
- Keep one implementation workstream active at a time. Sam's 2026-10-25 instruction to continue authorizes IND-004 pilot curation and its prerequisite schema corrections. Keep source approval, design review, transcription review and an analytical release distinct; do not treat a sequencing change as an independent review.
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

### 2026-10-25 — Claude — H001 pre-registration draft

- No Codex reply on PR #1 or PR #2 since the reviews (checked 21:26).
- Opened [PR #3](https://github.com/flysamc/game/pull/3) on branch `indus/H001-prereg-draft`: a **draft, unlocked** pre-registration for testing H001, written before any label × stroke-count tabulation. It covers the strokes-plus-cup search set, object-level unit, declared exclusions, models A/B/C, a permutation test of within-label agreement, decision rules, a power check, five sensitivity analyses and an unseen-subset check for contributors' prior exposure.
- Task board not changed. Proposal: lock this (Codex + Sam) before IND-004 data are tabulated, as a new task or as an IND-004 acceptance criterion; Codex to decide in the next board update.
- Next action: Codex reviews PR #3 and answers the open questions in PRs #1–#3.

### 2026-10-25 — Codex — IND-004 claim and review response

- Read Claude's accepted IND-002 review, requested IND-003 changes, and new H001 proposal. Preserved all review notes and merged PR #1 after resolving coordination-only history conflicts.
- Accepted the broader strokes-plus-cup family as the subsequent search target, while retaining the five exposed Figure 4 entries as a workflow pilot. Replied on PRs #2 and #3 before expanded tabulation.
- Requested corrections to the H001 proposal: non-significance is not evidence for a free quantity; model verdict thresholds need justification; permutation units must be exchangeable; illegible labels cannot form wildcard equivalence groups; curation exposure is not blindness.
- Claimed `indus/IND-004-pilot-curation`: add photo-check conclusions and surface content; locate the four outstanding pilot objects and transcribe nine faces from primary images; keep unresolved identity and ambiguity explicit.
- Exposure: Codex has read Claude's aggregate counts, M77 5498 sequences and prior-exposure list, and has already seen the H-351 plate and neighbouring H-352–354. This is not blind replication. No H001 test or family-wide association table is authorized by this claim.
- Source registration decision: public third-party M77 metadata/cross-checks are within the requested source research; raw data and restricted plates will not be committed. Unknown reuse terms remain documented.

### 2026-10-25 — Codex — IND-004 curation handoff

- [PR #4](https://github.com/flysamc/game/pull/4), branch `indus/IND-004-pilot-curation`, content commit [e0308a2](https://github.com/flysamc/game/commit/e0308a2b1146ed7ddc995089d5cf5212ce3505ab); stacked on PR #2. Retarget #4 to the current default after #2 is merged.
- Located primary identifier chains and photographs: M77 5498 → CISI-I H-322; 4444 → H-303; 4456 → CISI-II H-916; 4591 → H-977. Rechecked the prior H-351 match. These proposed mappings await independent review.
- Transcribed the nine missing faces; v0.2 now has 12 normalized faces across five catalogue records. Kept both source-doubt marks. Recorded 17 field-level photo outcomes (11 confirms, 6 consistent); these are not independent sample counts. H-351's four strokes remain photographically qualified.
- Addressed Claude's schema requests: photo outcomes with checker/evidence, explicit surface content, non-script face anchors, separate third-party evidence kind, and a conservative unknown-span policy. No invented motif faces or sign-zero tokens were added.
- Retrieved full M77, Vats text tables, and CISI-II scans; expanded CISI-I checks. Corrected retrieval traps: FC is not M77; ASI 49.255.200 is on H-322's continuation line, not H-323's row. M77 scan offsets vary: p. 360 is PDF 371, but pp. 821/824 are PDF 830/833.
- Pinned joyboseroy/indus_decipher at cd600349f6d3193a241c3eb87ff80a2a65377efc. After a primary-source checkpoint, all 12 pilot base-sign sequences agreed with the CSV. Exact doubt positions, direction and damage are not validated by its defaults. Its MIT software license does not establish underlying portal-data rights; no raw corpus was committed.
- Validation: Python 3.12.14; all 31 tests pass; draft validator exit 0, readiness exit 1 as intended; legacy v0.1 data/schema preserved unchanged and still validate. Source additions, v0.2 transcription/crosswalk review, physical-object grouping and frozen status remain pending.
- Exposure: full M77 p. 360 context, Vats and CISI index rows, adjacent CISI plates, Claude's aggregate report, and the 12 cross-check rows were seen. No family-wide label/count table, hypothesis test, phonetic assignment or translation was made.
- Claude has revised proposal #3 following the six review points. It remains unlocked; method details still need resolution before inference. Next action: independent review of #4 using its source checklist, then identity adjudication and a separately specified family search.

### 2026-10-25 — Codex — Claude's IND-004 review applied

- Read [Claude's actual review](https://github.com/flysamc/game/pull/4#pullrequestreview-5645307407) and H001 revision 3 at `23fa6579cc702608aafae15c0c96132e69b951e8`. Branch: `indus/IND-004-pilot-curation`; PR #4 stays open and stacked on #2.
- Re-inspected CISI-I p. 226 and CISI-II p. 343. Changed H-322 A and H-977 B normalization outcomes to `consistent`; kept the independently visible stroke counts at `confirms`. Now 17 outcomes: 9 confirms, 8 consistent.
- Preserved M77 59 on H-977 C while adding evidence-linked `content_disputed`/`content_assessments`. CISI's plate heading supports a motif interpretation by inference, not an explicit per-face ruling. Checked CISI-I p. 230's heading too; no equivalent source conflict is established for H-351 C's X. Its function remains an open question.
- Recorded Claude's explicitly authorized source-addendum and crosswalk acceptance plus five distinct physical-object groups within the pilot. H-322's excavation number remains unreported. Vats I pp. 348/351 were not independently checked by Claude; that limitation is explicit, and Vats alias statuses are not upgraded. All record-level transcription reviews remain pending.
- Validation: all 35 tests pass; draft validator exit 0; `--require-ready` exit 1 as intended. Historical v0.1 data/schema unchanged. No corpus scans or raw third-party data committed.
- New family leads (H-917/M77 4472 and H-354/M77 5499) remain Claude-reported, not new pilot records. Read his reported direction/alternative-face example; no additional family search or statistical test performed.
- Next: review corrected record transcriptions and source-classification representation; inspect outstanding Vats links if accessible; settle H001's analysis rules before broader tabulation. IND-003 and IND-004 remain IN REVIEW; H001 remains unlocked. Full response is in `notes/IND-004-review-response.md` on the curation branch.

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


