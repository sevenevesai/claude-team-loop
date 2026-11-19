# Context template

One template, two shapes. In a folder it becomes `CLAUDE.md`. For a shared Claude Project the
first three sections become the project instructions and the rest becomes `context.md`.

Write facts you saw. Delete a section that would be empty. Angle brackets mark what to replace;
none may remain in the result. For a shared Project, rewrite the Records bullets to name its
knowledge files (`changelog.md`, `context.md`, `team-overrides.md`) in place of the folder paths.

```markdown
# <Project> - <what it is in a few words>

## What this is
<Two or three lines: what the team delivers here and for whom.>

## Environments
| Name or alias | What it is | Rule |
|---|---|---|
| <alias> | <production / staging / test / board / repository> | <read and write / read only / never write without the person naming it> |

Production is <alias>. <Any environment that must never be written to, and why.>

## Working here
- Check the live system before trusting a local copy: <the read-only command or tool that does it>.
- <A convention the team or its customer expects: ticket format, naming, branch flow, language.>
- <A trap that has cost time, with its symptom and its remedy.>

## Readers
<Who reads the output: roles, and what each needs from it.>

## Records
- `CHANGELOG.md`: what changed and what is open, newest first. Updated at the end of each
  working session by the team-loop close-out skill.
- `docs/`: one note per ticket or workstream.
- `.claude/team-overrides.md`: how team skills are adjusted for this project, when present.
- <The shared Claude Project or the repository this context is paired with, when there is one.>
```

## First change-record entry

```markdown
# Changelog

## <YYYY-MM-DD> - Context set up
- Starting point: <what exists and works today, in two or three lines>.
- Open: <what the team is about to do>.
- Next: <the first step>.
```

## What stays out

- Credentials, tokens, connection strings.
- Personal data of customers or users.
- History: it belongs in the change record, not the context file.
- Anything the person marked confidential.
