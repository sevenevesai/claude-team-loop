---
paths: ["plugins/**", ".claude-plugin/**"]
---

# Authoring the team's plugins

The readers are colleagues' Claude sessions in chat, Cowork and Claude Code, often driven by
someone who does not know what a skill is. The skill carries the expertise; the person brings
the task and the decisions that are theirs. Reasons: `docs/how-it-works.md`.

## Naming
- A plugin is `team-<audience or platform>`: `team-loop` (everyone), `team-<platform>` for one
  platform's work. A new audience or platform starts a new plugin. Skills for a neighbouring area
  start in the closest plugin and move to their own once three exist that its users do not need.

## Portability
- Skills are the core: they load on every surface. Hooks and agents are ignored in chat, so
  nothing a skill depends on lives only in a hook.
- SKILL.md frontmatter holds `name` and `description`, plus `allowed-tools` where needed. Other
  keys may be rejected on claude.ai.
- No top-level `bin/` (claude.ai rejects the plugin), no `$ARGUMENTS`, no `` !`command` ``
  injection (neither works in chat).
- Files a hook prints stay ASCII. Windows PowerShell 5.1 misreads BOM-less UTF-8.
- A script is an optional helper. Name the runtime it needs and give the manual route.

## What every skill contains
- Description: what it does, the phrases that trigger it, what it is not for. Under 1,000
  characters; the listing is cut at 1,536.
- Agnostic defaults: no names of clients, customers, people, products, systems or projects, and
  no absolute paths. Specifics come from the project's context and `.claude/team-overrides.md`.
- Find out, then ask: what the session looks up itself, and which decisions go to the person.
- Gates: a step that changes a production or shared system, or sends something outside the
  team, starts with `Gate:` and waits for the person. Overrides cannot waive a gate.
- Verification: how the session proves the result, and what it reports as unverified.
- Upkeep: what the skill records when done, so the person never manages documents by hand.
- The `## Local practice` section, verbatim from `plugins/team-loop/skills/catch-up/SKILL.md`.
- SKILL.md under 8 KiB and 150 lines; depth in `references/`.

## Releasing
- A release goes to the organisation's plugin library, by Claude Code's publish tool or as the
  zip `python tools/package-plugins.py <name>` builds.
- After a release, write what `python tools/plugin-catalogue.py --published <name> ...` prints
  into the findings sheet's Plugins tab, which `ideas` reads.
- Every change to a plugin bumps `version` in its `plugin.json` and adds a line to its
  `CHANGELOG.md`. Packaging refuses an existing version.
- Gate: `claude plugin validate . --strict` and `claude plugin validate plugins/<name> --strict`
  exit 0 before commit.
- A new or reworked skill gets one headless trial before release, from a scratch folder:
  `claude -p "<a request that should trigger it>" --plugin-dir plugins/<name>`.
