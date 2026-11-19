# Set the loop up for your team

Written for a person and their Claude Code session working through it together. Each step says
what success looks like. The design and its reasons are in `how-it-works.md`.

## Before you start

- A Claude Team or Enterprise plan. The steps assume ordinary member rights.
- Claude Code and Python 3 on the owner's computer. Members need neither.
- A private repository for your copy. It will hold your backlog and your team's practice, and
  organisation-run GitHub sync accepts only private or internal repositories.

Decide these first; a Claude session setting this up asks the person and does not guess:

1. Who is the owner, and who else may release?
2. What is the team's prefix? The kit uses `team`; a company or team name works better.
3. Which actions need a gate: which systems are shared or production, and what counts as
   sending something outside the team?
4. What counts as confidential in your work? The privacy rules in
   `plugins/team-loop/skills/ideas/references/report-format.md` list names, ids, URLs, paths,
   figures and copied text.
5. Which audiences or platforms need a plugin of their own later?

## 1. Copy the kit

Create a private repository from this one (on GitHub: "Use this template", or clone and push to
a new private remote). Success: `claude plugin validate . --strict` prints "Validation passed".

## 2. Make it yours

Rename the prefix everywhere it appears. With the prefix `acme`:

| Kit name | Becomes | Where |
|---|---|---|
| `team-loop` | `acme-loop`, or any `acme-<name>` | the folder under `plugins/`, `plugin.json`, `marketplace.json`, every `team-loop:` reference |
| `team-loop-kit` | `acme-plugins` | `marketplace.json` `name` |
| `.claude/team-overrides.md`, `team-overrides.md` | `.claude/acme-overrides.md`, `acme-overrides.md` | every skill's "Local practice" section, `adapt-skill` |
| `team-findings` | `acme-findings` | report file name, folder, format id and title in `ideas` and its references |
| names starting `team-` | names starting `acme-` | `ideas`, the authoring rule |

A plugin name must not start with `claude-`, `anthropic-`, `anthropics-` or `cc-plugin-`;
validation rejects those.

Then edit the content that carries your practice:

- `plugins/<plugin>/context/working-agreements.md`: the agreements every session starts with.
  Keep it short and ASCII.
- The `Gate:` lines in each skill, to match your answer to question 3.
- `plugins/<plugin>/README.md`: name the owner, so a session knows where a report file goes.
- `plugin.json` and `marketplace.json`: author, owner and descriptions.

Success: both validate commands pass, and a search for the old prefix finds nothing outside
`docs/` and `writeup/`.

## 3. Create the intake sheet

The intake is one place every member's Claude can append to and the owner's Claude can read. The
kit assumes a Claude Sheet. Another shared spreadsheet works when sessions can reach it through
a connector, and with no sheet at all members send the report file.

1. Create a sheet with two tabs, `Findings` and `Plugins`.
2. On `Findings`, put the columns of `plugins/<plugin>/skills/ideas/references/intake.md` in
   the first row, in that order. Make Kind and Status dropdowns. Kind takes the labels listed
   there. Status takes `new`, `reviewed`, `accepted`, `shipped`, `declined`.
3. On `Plugins`, write the rows this prints, header first:
   `python tools/plugin-catalogue.py --published <plugin>`
4. Share the sheet with the team with edit access.
5. Replace the first line of `intake.md` with `Link: <the sheet's link>`.

Success: asked "read the Plugins tab of the sheet in intake.md", your session lists your plugin
and its skills.

## 4. Trial

From an empty scratch folder, so the session has no other context:

```
claude -p "the close-out skill got something wrong, I want to report it" --plugin-dir <path to repo>/plugins/<plugin>
```

Success: the reply follows `adapt-skill`: it asks which default is wrong and offers an override
and a note for the owner. Give each skill you changed one such trial before releasing it.

## 5. Publish

1. Bump `version` in `plugin.json` when anything changed since the last release, and add a line
   to the plugin's `CHANGELOG.md`.
2. `python tools/package-plugins.py <plugin>` prints the zip's path, file count and size. It
   exits 1 when that version already has a zip.
3. In Claude, under Customize > Plugins, upload the zip and publish it to the organisation.
   Menu names move; the current steps are at <https://claude.com/docs/plugins/share>.
4. Refresh the sheet's `Plugins` tab (step 3.3).

An organisation Owner can sync this repository to the organisation instead:
<https://claude.com/docs/plugins/org-sync>.

Success: a colleague finds the plugin in the organisation's library, and a new session of theirs
lists its skills.

## 6. Tell the team

Three sentences are enough:

- Install the plugin from the organisation's library.
- When a skill gets something wrong, say so in the session: "the skill got this wrong".
- After a few weeks of use, ask Claude to "find skill ideas", read the report and approve it.

Claude Code deletes transcripts after 30 days by default. `ideas` offers to raise that and leaves
the choice to the person, because transcripts hold confidential text in plain files.

## 7. Schedule the review

Run it by hand first, in the repository: ask Claude Code to "review the findings". Success: a
summary of what arrived, a changed `docs/backlog.md`, statuses set on the sheet, and a branch
`review/<date>` when a change was drafted.

Then let a scheduler start it each night. Any scheduler that can run a command works:

```
cd <path to repo> && claude -p "Run the review-findings skill, unattended."
```

On Linux or macOS that is a cron line; on Windows a Task Scheduler task. Claude Code and Cowork
also offer scheduled tasks of their own. An unattended run needs the permissions it will use
allowed in advance, and may not reach the sheet: check the first scheduled run's summary. When it
cannot, export the Findings tab as CSV into the inbox folder (`~/team-findings-inbox`) before the
run.

## 8. The owner's morning

1. Read the summary and the diff of `review/<date>`.
2. Merge what should ship, or change it first. Decline the rest on the sheet with a reason.
3. Publish (step 5) and set the shipped rows to `shipped` with the version.

That closes the loop: the person who reported the problem sees the status, and their next
session has the fix.
