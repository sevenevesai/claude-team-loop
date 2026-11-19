# Team loop kit

A starter kit for a team plugin that improves from its own use: the plugin members work with,
the owner's review skill, and the docs to set both up. When someone asks you to set this up for
their team, follow `docs/setup.md` and ask them its five opening questions first.

## Layout

| Path | Holds |
|---|---|
| `plugins/team-loop/` | the plugin for everyone: six skills, working agreements, session-start hook |
| `.claude/skills/review-findings/` | the owner's review of what the team sent in; not published |
| `.claude/rules/plugin-authoring.md` | the standard every plugin skill meets; loads when editing `plugins/` |
| `.claude-plugin/marketplace.json` | lists the plugins, for validation, local use and GitHub sync |
| `tools/` | `package-plugins.py` builds upload zips into `dist/`; `plugin-catalogue.py` prints the sheet's Plugins tab |
| `docs/` | `how-it-works.md` (design and reasons), `setup.md`, `backlog.md` |
| `writeup/` | the article and visuals that explain the loop |

## Commands

- `claude plugin validate . --strict` and `claude plugin validate plugins/<name> --strict`:
  both print "Validation passed" and exit 0.
- `python tools/package-plugins.py <name>`: prints the zip path, file count and size. Exits 1
  when that version already has a zip; bump the version first.
- `python tools/plugin-catalogue.py --published <name>`: prints the Plugins tab rows as JSON.
- `claude -p "<request>" --plugin-dir plugins/<name>` from a scratch folder: a headless trial
  of a skill.

## Invariants

- Plugin content names no client, customer, person, product or system, and works in chat,
  Cowork and Claude Code. Specifics come from a project's context file and overrides.
- Findings reports, sheet exports and session digests stay outside this repository. The backlog
  carries counts and task-level descriptions only.
- Every change to a plugin bumps its `version` and adds a line to its `CHANGELOG.md`. Without a
  version bump, installed copies do not update.
- `review-findings` never merges, publishes or pushes. Releasing is the owner's decision.
- The extractor and coding brief exist once, in `plugins/team-loop/skills/ideas/`. Change them
  there so everyone's counts stay comparable.

## Conventions

- A decision or a release gets a dated entry in the root `CHANGELOG.md`.
- A skill idea goes into `docs/backlog.md` with its evidence before it is built.
- Facts about Claude's features cite the table in `docs/how-it-works.md`. Check a fact against
  its source again before relying on it.
