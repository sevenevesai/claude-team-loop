# team-loop

How the team works with Claude on any project, whatever your role: developer, analyst,
consultant, designer, project lead. Works in Claude chat, Cowork and Claude Code.

You do not need to learn the skills. Ask for what you need in your own words and Claude picks
the matching one.

| When you say something like | Claude will |
|---|---|
| "Pick up where we left off on the X project" | read the project's records, check them against the live system, and brief you (`catch-up`) |
| "Wrap up" or "update the docs" | bring the change record and context up to date and give you a kickoff line for next time (`close-out`) |
| "Write an update for the customer" or "summarise this for X" | draft a short, plain message from checked facts and show it before anything is sent (`write-update`) |
| "Set up Claude for this project" | create the context file and change record, or a shared Project for the people on it (`setup-project-context`) |
| "On this project we do it differently" | record the adjustment with the project so it sticks (`adapt-skill`) |
| "Find skill ideas in my sessions" | look through your own Claude history for work you repeat and corrections you keep making, and write a short report for the maintainers that you check and send (`ideas`) |

In Claude Code and Cowork the plugin also adds a short set of working agreements to every
session: check before claiming, ask before changing a production or shared system, keep records
current.

## Install

From your organisation's plugin library once the maintainers have published it there. In Claude
Code, from the kit's public repository:

```
/plugin install team-loop --marketplace sevenevesai/claude-team-loop
```

## Where your project's records live

On your own computer, in the project folder (`CLAUDE.md`, `CHANGELOG.md`, `docs/`), or in a
Claude Project you share with the people on the project. Claude keeps them current when you wrap
up. Files kept elsewhere stay as they are.

Mention that something saved you time, or say "log this as a win", and Claude adds a one-line
`Win:` note to the project's change record. It never asks.

## Adjusting it for a project

Tell Claude what is different ("ticket comments go in Dutch here"). It records the adjustment
in `.claude/team-overrides.md` in the project folder, or gives you a `team-overrides.md` file to
add to the shared Project. Plugin updates do not touch that file. Steps that protect production
and shared systems cannot be switched off.

## Updates, ideas and problems

New versions are published to the organisation's plugin library. Ideas and problems for every
team plugin (`team-loop` and any later `team-<platform>` one) go through this one:

- Tell Claude "the skill got this wrong" and it drafts a short note (`adapt-skill`).
- Every few months, or when the maintainers ask, type `/ideas` or say "find skill ideas".
  Claude reads your own history on your computer or account, compares it with all team plugins,
  including ones you have not installed, and drafts a report of counts and task descriptions
  with no project details. It also tells you which team plugins would suit your work.

Nothing leaves until you have read it. Then Claude adds it to the team's findings sheet when you
agree, or you send it to the maintainer named below. The sheet lists every team plugin and shows
what became of each idea.

## Maintainers

Maintainer: not set. Before publishing, replace "not set" with the person or channel that
receives findings reports and feedback notes.

Source and release rules: the `plugins/team-loop` folder of the kit's repository and its
`.claude/rules/plugin-authoring.md`. Setup is in `docs/setup.md`, the design in
`docs/how-it-works.md`. Changes are listed in `CHANGELOG.md`.
