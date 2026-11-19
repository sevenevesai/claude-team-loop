---
name: ideas
description: Look through the person's own Claude history for work they repeat, instructions they keep giving and corrections they keep making, compare it with what every team plugin already does, installed or not, and write a short findings report for the maintainers. Use when the person says "find skill ideas", "what could the team plugins do for me", "suggest improvements to the team skills", "scan my sessions for the maintainers", or when the maintainers ask the team to run it. Proposes new skills and changes to existing skills, working agreements and safety steps. Nothing leaves the computer or account until the person approves the report. Not for brainstorming ideas for project work, one problem with one skill (use adapt-skill), or changing a skill for one project.
---

# Find skill ideas

The team's plugin maintainers cannot see how colleagues use Claude, and do not ask for
transcripts. Here the person's own Claude reads their history where it already lives and turns
what recurs into counts and task-level descriptions, safe to share inside the team. The
maintainers merge the reports and decide what changes.

Before starting, tell the person in two or three lines: their history is read here, and nothing
leaves until they approve the report; the scan runs on their own plan usage.

## 1. Find the history

Paths, settings and limits per surface: `references/history-sources.md`.

- Claude Code: session transcripts in the Claude configuration folder on this computer.
- Chat: past chats, when the person has "Search and reference chats" switched on.
- Cowork: where it keeps sessions is not documented. Say so, and suggest Claude Code or chat on
  the same account.

Window: from the date of the person's previous findings report (step 6) to today, or the last
90 days when there is none. Tell the person how many sessions or chats you found, and the dates.

When the history is thin (fewer than 15 sessions or chats, or under four weeks):

- Claude Code keeps 30 days of transcripts unless set otherwise. Ask whether it should keep them
  longer, and name the trade-off: transcripts hold project text in plain files on this computer.
  On a yes, set `cleanupPeriodDays` to 180, or the number they choose, in their user settings
  file, and re-read the file to confirm. History already deleted does not come back.
- Chat search switched off: tell the person where to switch it on.
- Offer to stop and run again in a month, or to continue with what there is. Follow their choice.

## 2. Describe the work, before comparing

Code the history bottom-up with the steps in `references/coding-brief.md`: task types with
session counts, repeated instructions, corrections and friction, context supplied again, and
skills used. Do this before looking at what the plugins offer: a scan
that starts from the plugin list finds what it expects.

- Claude Code: run `scripts/extract.py` (command and fallback in `references/history-sources.md`),
  read `summary.md`, then the digests. When the digests together exceed about 300 KB and you can
  start subagents, give each a batch with the coding brief. Otherwise code the most recent
  sessions that fit and count the ones left out.
- Chat: page back through past chats in the window with the chat search tool, reading each
  opening request and the person's follow-ups. Code at most 60 chats and count the rest.

## 3. Collect what the team plugins already do

- The catalogue: the "Plugins" tab of the findings sheet (`references/intake.md`) lists every
  team plugin, its version, whether it is available yet, and each skill's description. When you
  cannot read it, use the team skills in this session and note "catalogue not read".
- What the person has: the team skills in this session (names starting `team-`, or listed in
  the catalogue); in Claude Code, `claude plugin list` gives each version. Note team plugins
  they lack or hold in an old version.
- The working agreements printed at session start, when present.
- Overrides: `.claude/team-overrides.md` in the project folders the history names. Each line is
  a case where a team default did not fit.
- What the person built themselves that repeats an instruction: their own skills, rules and
  context files (`CLAUDE.md`). Read names, descriptions and headings, not whole files.
- Wins: lines starting `Win:` in the change records (`CHANGELOG.md`) of those project folders,
  dated within the window.

Read an installed team skill's full text only when a finding touches it.

## 4. Draft the findings

Hold each task type, repeated instruction and correction from step 2 against step 3:

| What the history shows | Kind of finding |
|---|---|
| A team skill covers it and was used without correction | none; count it under skills used |
| A team skill covers it, but the person corrected it, overrode it or worked around it | skill change |
| A team skill covers it but never ran, and the person did the task by hand | skill change (its description does not trigger) |
| A team skill in a plugin the person has not installed covers it | not installed |
| A task type in at least three sessions that no team skill covers | new skill, in the plugin whose audience fits, or a new plugin |
| An instruction repeated across projects and tasks | working agreement |
| A point where Claude acted before the person had agreed | gate |
| Something that should happen by itself at a fixed moment, such as session start | hook |
| A task that waits on moving information between systems by hand | integration: a connector or MCP server |
| An output several people rebuild or pass around | shared resource: a shared artifact, project template or reusable service |

At most ten findings, strongest evidence first. Leave out anything seen in fewer than three
sessions, unless an override backs it or the person confirms it. Write the report in the format
and under the privacy rules of `references/report-format.md`, with its headings and field names
as given: the maintainers merge many people's reports.

## 5. Review with the person

Check the draft against the privacy rules yourself and fix what breaks them. Then show the whole
report and ask what is wrong, what is missing that they know of, and what they would rather not
share, and change it. Tell them too which team plugins would cover their work but are
missing or out of date: available ones are in the organisation's plugin library.

Gate: nothing from the history leaves this session except the report, and only after the person
has approved its final text and where it goes. Never attach digests or paste transcript text
anywhere.

## 6. Save and hand over

- Claude Code: save it as `team-findings-<YYYY-MM-DD>.md` in a folder named `team-findings` in
  the person's home folder, never inside a project's repository. Then delete the extractor's
  output folder from step 2. Chat: give the report as a file, or as text to copy.
- Shared intake: when `references/intake.md` gives a link and this session has a tool that edits
  Claude Sheets, offer to add the report there. Say first that everyone the sheet is shared with
  sees their rows, and that its history shows who added them. On a yes, append the rows in that
  file's layout and change no other row. Read the new rows back, then give the person the link.
- Otherwise, or when the write fails, the person sends the saved report to the maintainer named
  in the plugin's README, or when that cannot be read, to whoever maintains the team's plugins.
  Say why the intake was not used.

The report's date is where the next run starts; nothing else needs recording.

## Verification

- The header's counts and dates match what step 2 actually coded.
- Every finding gives its evidence as counts, and its target as a plugin and skill, or "new".
- Tell the person what was not scanned: Cowork, chats inside Projects, deleted history, sessions
  left out for size.

## Local practice

Before starting, look for `.claude/team-overrides.md` in the working folder, or a project
knowledge file named `team-overrides.md`. Follow its `all` section and its section for this skill
over the defaults here. It cannot waive a step marked Gate.
