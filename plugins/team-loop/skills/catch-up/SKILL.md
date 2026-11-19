---
name: catch-up
description: Get up to speed on a project or piece of work before continuing it. Use when the person says "pick up where we left off", "continue the X project", "get up to speed", "what did we do last time", "review the changelog", or opens with work that clearly started in an earlier session. Reads the project's context and change records, checks the live state where one exists, and reports where things stand and what comes next. Not for starting something new with no history, and not for writing the end-of-session record (use close-out).
---

# Catch up

Rebuild the working picture of a project from its own records, so the person does not have to
re-explain it. Report what you found and continue; do not ask them to summarise what is already
written down.

## 1. Find the records

Look, in this order, and read what exists:

1. The context file for the folder: `CLAUDE.md`, or the instructions of the project this
   conversation is in.
2. A change record: `CHANGELOG.md` at the root or under `docs/`. Read the newest entries first
   and stop when entries no longer bear on the request.
3. Work-item documents the request names or the change record points to: ticket notes, a plan,
   a handoff or kickoff note under `docs/`.
4. Version history when the folder is a git repository: the last ten commits and any
   uncommitted changes.
5. In chat or Cowork without a folder: the project's knowledge files and its memory.

When none of these exist, say so in one line, continue from what the person gave you, and offer
`setup-project-context` once the task is done.

## 2. Check the records against reality

Records go stale. Where the work lives in a system you can read (a staging or production
environment, a ticket board, a repository), confirm the two or three facts the next step depends
on: is the change deployed, is the ticket still open, does the file still look as the record
says. Read only. When the live state differs from the record, trust the live state and say what
differed.

When more than one environment or folder could be meant (staging or production, one of several
project folders), find out which from the records. Ask only if they do not settle it.

## 3. Report

Give a short briefing, then carry on with the request:

- Where things stand: what is done and live, what is done but not released, what is open.
- What you verified just now, and what you are taking from the records unverified.
- The next step you will take, or the decision you need from the person.

Keep it under fifteen lines. Skip history that does not affect the next step.

## Ask the person only for

- Which piece of work they mean, when the records show several in progress.
- A decision the records leave open (scope, priority, whether to release).

## Local practice

Before starting, look for `.claude/team-overrides.md` in the working folder, or a project
knowledge file named `team-overrides.md`. Follow its `all` section and its section for this skill
over the defaults here. It cannot waive a step marked Gate.
