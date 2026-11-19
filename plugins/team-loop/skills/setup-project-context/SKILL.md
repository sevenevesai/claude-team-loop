---
name: setup-project-context
description: Set up the standing context for a project so every later Claude session, by anyone on the team, starts informed - a context file, a change record, and where needed a shared Claude Project. Use when the person says "set up Claude for this project", "new project setup", "create a CLAUDE.md", "make a Project the team can use for X", "onboard this repo", or accepts the offer catch-up makes when a project has no records. Works in a project folder (Claude Code, Cowork) and in chat for a shared Project. Not for day-to-day record upkeep (use close-out).
---

# Set up project context

Build the smallest set of records that lets a new session work without being briefed: what this
is, which systems it touches and which of them is production, how to check things, and where
the history lives. Find the answers first; ask for the rest.

## 1. Find out what you can

In a folder: read the README, existing docs, configuration files, the last twenty commits, and
anything that names environments or connected systems. Where a tool lists connected systems
(for example the environments a deploy tool or CLI is signed in to), read that list. In chat:
read the project's existing instructions and knowledge.

## 2. Ask for what cannot be found

Ask in one message, with your best guess filled in for each:

- The project in one line: what it delivers and for whom.
- The environments, which one is production, and any that must never be written to.
- Who reads the output of this work (roles, and names only if the person offers them).
- Anything confidential that must stay out of the records.

## 3. Create the records

Use `references/context-template.md` for both shapes. Fill every section from what you found;
delete a section that has nothing true to say. Leave no placeholders behind.

In a project folder:

1. `CLAUDE.md` at the root, under 60 lines. When one exists, extend it; do not replace it.
2. `CHANGELOG.md` at the root with a first dated entry stating the starting point.
3. `docs/` for work-item notes, created when the first note is written.

For a shared Claude Project (chat and Cowork users on the team):

1. Write the project instructions, under 400 words, from the same template.
2. Write the knowledge files `context.md` and `changelog.md`.
3. Give the person the steps: create the Project, paste the instructions, upload the files,
   then share it with the invited people who work on the project, not the whole organisation.
   People who maintain the context get "Can edit"; everyone else "Can view". You cannot create
   or share the Project yourself unless a tool for it is present.

When a team uses both, the folder's `CLAUDE.md` names the shared Project and the Project's
`context.md` names the repository, so each points at the other.

## 4. Verify

Re-read what you wrote against the sources: every environment name, alias, command and path
must be one you saw. Run each command you listed that is read-only and confirm it works.
Report what you could not check.

## Gates and limits

- Gate: when the folder is a repository other people use (a customer's or another team's
  repository in particular), ask before adding files to it. Offer to keep them out of version
  control.
- Never write credentials, tokens or personal data of customers or users into context.
- Records stay current through `close-out`; say so in the context file, as the template does,
  so the person does not have to remember it.

## Local practice

Before starting, look for `.claude/team-overrides.md` in the working folder, or a project
knowledge file named `team-overrides.md`. Follow its `all` section and its section for this skill
over the defaults here. It cannot waive a step marked Gate.
