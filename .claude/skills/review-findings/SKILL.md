---
name: review-findings
description: Review the findings the team's Claude sessions sent in, merge them into the backlog, draft the plugin changes they justify and answer every row with a status. Use when the owner says "review the findings", "process the intake sheet", "what did the team send in", "merge the findings reports", or when a schedule runs it overnight. Owner's skill for this repository; it is not part of the published plugin.
---

# Review findings

Colleagues send findings with the plugin's `ideas` skill (a report from their own history) and
`adapt-skill` (a note about one skill). Both arrive as rows on the Findings tab of the shared
sheet linked in `plugins/team-loop/skills/ideas/references/intake.md`, or as report files in
the format of `references/report-format.md` next to it. This skill turns them into backlog
evidence and drafted changes. The owner decides what ships.

The owner's own history enters the same way: run `ideas` like everyone else.

## 1. Collect what is new

- Sheet: read the Findings tab and take the rows whose Status is `new`. When this session cannot
  open the sheet, use a CSV export in the inbox folder instead.
- Files: reports in the inbox folder that the log in `docs/backlog.md` does not list yet.
- The inbox folder is outside this repository (default `~/team-findings-inbox`). A report can
  still carry a slip of confidential text, so no report, export or copy of a row is committed.

When nothing is new, say so and stop. Do not write a changelog line for an empty run.

## 2. Check each row against the privacy rules

The rules are in `report-format.md`: no names of clients, customers, colleagues, products,
systems or projects; no ids, URLs, paths or figures; no copied text. Leave out of the backlog
whatever breaks them, and note in the row's Maintainer note that it needs rewording. When the
`ideas` skill produced the slip, add a skill change for `ideas` to the backlog.

## 3. Merge into the backlog

Edit `docs/backlog.md`. Count people and sessions; never name anyone.

| Kind | Where it goes |
|---|---|
| new skill | add or update a candidate, with evidence such as "3 people, 41 sessions" |
| skill change, working agreement, gate, hook | one row per target and proposal under "Changes proposed for shipped content", merged across reports |
| integration, shared resource | one row under "Beyond the plugin", with the systems or output as a task-level description |
| not installed | a count per plugin: where people miss a plugin that would serve them |
| skill used | add up per skill. A skill nobody ran while its task shows under work seen has a description that does not trigger |
| work seen, wins | add to the evidence tables |

Two rows are the same finding when they have the same target and ask for the same behaviour,
whatever their wording.

## 4. Draft what the evidence justifies

Draft a change when a finding has at least two people behind it, or one person and a recorded
override, or the owner marked its row `accepted`. Leave the rest in the backlog.

- Work on a branch named `review/<YYYY-MM-DD>`, never on the default branch.
- Follow `.claude/rules/plugin-authoring.md`: bump the plugin's `version`, add a line to its
  `CHANGELOG.md` that cites "colleague reports", and keep SKILL.md within its size limit.
- A new skill is drafted only when the owner asked for it; otherwise write its outline into the
  backlog candidate. An integration or shared resource is never built here: describe it in the
  backlog for the owner to take up.
- Run `claude plugin validate . --strict` and `claude plugin validate plugins/<name> --strict`.
  Both print "Validation passed" and exit 0. Commit the draft on the branch only when they pass.

Gate: do not merge the branch, publish a plugin or push. Releasing changes what every
colleague's session does, so it waits for the owner.

## 5. Answer every row

Set Status and Maintainer note on each row read in step 1, and change nothing else on the sheet.

| Status | Meaning | Set by |
|---|---|---|
| new | just arrived | the sender's session |
| reviewed | merged into the backlog, waiting for a decision | this skill |
| accepted | will be built; a draft may exist | the owner, or this skill when it drafted the change |
| shipped | released, with the plugin version in Maintainer note | the owner at release |
| declined | not taken up, with the reason in Maintainer note | the owner |

When the sheet cannot be written, list the status changes in the summary for the owner to enter.

## 6. Record and report

- Add a dated line to the root `CHANGELOG.md`: rows and reports merged, people, sessions, date
  range, and the branch when one was made.
- Add the merged report files' dates to the log in `docs/backlog.md`.
- End with a summary for the owner: what arrived, what changed in the backlog, what was drafted
  and where, which rows wait for a decision, and anything that could not be read or written.

## Running unattended

On a schedule nobody is there to answer. Do steps 1 to 6 without asking, keep every draft on its
branch, and put each open question into the summary instead of guessing. `docs/setup.md` shows
how to schedule the run.

## Check before finishing

- `git status` shows no report, export or digest inside the repository.
- A search of the changed files finds no name, id, URL or copied sentence from a report.
- Every row read in step 1 has a status other than `new`, or is listed as not written.
