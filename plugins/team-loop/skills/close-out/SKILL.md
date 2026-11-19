---
name: close-out
description: Finish a working session by bringing the project's records up to date - change record, work-item notes, context file - and leaving a handoff for the next session. Use when the person says "wrap up", "close out", "update the docs", "update the changelog", "document our progress", "give me a kickoff prompt for next time", "log this as a win", or when a piece of work that changed a project's state is done. Not for writing a message to someone else (use write-update).
---

# Close out

Leave the project so that the next session, by anyone, can continue from the records alone. The
person should not have to say what to write or where.

## 1. Establish what changed

From this conversation, and from `git status` and `git diff --stat` when the folder is a
repository, list:

- What was changed, and where each change now lives: local only, test environment, production;
  drafted or sent.
- Decisions taken, with the reason in a few words.
- What is still open, and what blocks it.

Record only what happened. Where you did not verify an outcome, write "not verified".

## 2. Update the records

Use the records the project already has; create one only when it is missing.

1. Change record: `CHANGELOG.md` at the root, or under `docs/` when the project keeps it there.
   Add a dated entry at the top: a one-line heading, then the three lists from step 1 in a few
   lines each. Leave earlier entries as they are.
2. Work-item notes: when the project keeps a document per ticket or workstream and this session
   advanced one, update its status and next step.
3. Context file (`CLAUDE.md`, or the project's instructions): add only what every future session
   needs, such as a new environment, a convention, or a trap that cost time today. It holds
   pointers and standing facts; history belongs in the change record. When it has grown past
   about 60 lines, move detail into a document under `docs/` and leave a pointer.
4. Corrections: when the person corrected how a team skill works for this project and wants it
   to stick, or made the same correction twice, run `adapt-skill` so it is kept. A fact about
   the project itself goes in the context file instead.

In chat or Cowork without write access to project knowledge, produce the updated text of each
record and tell the person which knowledge file to replace.

Keep credentials, personal data of customers or users, and anything the person marked
confidential out of all records.

Win line: when the person says the work saved time, or asks to log a win, add one line to the
change-record entry: `Win: <what Claude was used for> - <the saving or result, in their words> -
reusable: yes, no or maybe`. Never ask for it, estimate hours yourself, or raise it unprompted.
These lines are collected from project records later.

## 3. Leave a handoff

End the change-record entry with a `Next:` line, and give the person a kickoff sentence they can
paste into a new session. It names the piece of work and the record to read, for example:
"Continue the export job work; start from the 12 March entry in CHANGELOG.md."

## 4. Report

Tell the person in a few lines: which records you updated, what remains unrecorded and why, and
the kickoff sentence.

## Gates and limits

- Gate: commit or push only when the project's instructions or the person ask for it.
- Gate: when the folder is a repository other people use, ask before adding new record files to
  it; offer to keep them out of version control instead.

## Local practice

Before starting, look for `.claude/team-overrides.md` in the working folder, or a project
knowledge file named `team-overrides.md`. Follow its `all` section and its section for this skill
over the defaults here. It cannot waive a step marked Gate.
