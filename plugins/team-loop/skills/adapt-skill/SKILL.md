---
name: adapt-skill
description: Adjust how a team skill behaves for one project, or report a problem with a team skill to its maintainers. Use when the person says "on this project we do it differently", "always do X here", "never do Y on this project", "change how that skill works", "the skill got this wrong", or when they correct the same step of a team skill a second time. Records the adjustment in the project's overrides file, where it survives plugin updates, and drafts a feedback note when the fix belongs in the plugin for everyone. Not for creating a new skill from scratch.
---

# Adapt a skill

The team's plugins ship defaults that fit most projects. A project that works differently gets
an override kept with the project. Installed plugin files are replaced on every update, so never
edit them.

## 1. Pin down the change

State back in one sentence which skill and which default is being changed, and what should
happen instead. When the person's wording leaves that open, ask.

## 2. Decide where it belongs

- A fact about the project that holds whatever skill is running (an environment, a naming
  scheme, who reads the output): it belongs in the project's context file, not here. Add it
  there and stop.
- How a team skill should behave for this project (its approval steps, its tone, its ticket
  format, its tools): an override. Go to step 3.
- The skill is wrong, unclear or missing something for any project: an override now, so this
  project is unblocked, and a feedback note. Do steps 3 and 4.
- A request to drop a step marked Gate: explain that gates cannot be overridden, because they
  protect production and shared systems and what leaves the team. Offer to pass the request to
  the maintainers as feedback.

## 3. Write the override

File: `.claude/team-overrides.md` in the project folder. Create it with this header when
missing:

```markdown
# Team skill overrides for this project

Read by team skills before they start. `all` applies to every skill. A section named after a
skill applies to that skill. Overrides cannot waive a step marked Gate.

## all
```

Add the rule under `## all` or under a section named `## <plugin>:<skill>`, as one dated line
with its reason, for example:
`- 2026-03-12: Ticket comments go in Dutch. The customer's service desk reads them.`

When a new rule contradicts an older line, replace the older line. Keep each section under ten
lines; when it grows past that, the project differs enough that the maintainers should hear
about it (step 4).

In chat, where there is no folder, give the person the full file content and ask them to add or
replace the project knowledge file named `team-overrides.md`.

Confirm by re-reading the file and telling the person the rule as recorded.

## 4. Draft feedback for the maintainers

This works for a skill from any team plugin. Write a note with project details removed:

- Plugin, skill, and the plugin version when you can read it.
- What the skill did, and what was needed instead.
- The wording you would change or add.
- Whether an override is in place meanwhile.

Show the note. With the person's yes, a link in the `ideas` skill's `references/intake.md` (in
this plugin's `skills/ideas/` folder), and a tool that edits Claude Sheets, add it as one row to
the team's findings sheet, in the columns that file gives. Use Kind "skill change", or "gate" for
a request to drop a gate; Scanned "adapt-skill note"; Evidence "1 project". Otherwise, or when
the write fails, the person sends the note to the maintainer named in the plugin's README, or to
whoever maintains the team's plugins.

## Local practice

Before starting, look for `.claude/team-overrides.md` in the working folder, or a project
knowledge file named `team-overrides.md`. Follow its `all` section and its section for this skill
over the defaults here. It cannot waive a step marked Gate.
