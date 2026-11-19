# Where the history is, per surface

Checked against Claude's documentation on 2026-11-19. Paths and settings can change between
releases. When what you find differs from this file, say so under Notes in the report header.

## Claude Code

- Configuration folder: the `CLAUDE_CONFIG_DIR` environment variable when set, otherwise `.claude`
  in the person's home folder.
- Transcripts: `projects/<folder>/<session id>.jsonl` inside it, one file per session. `<folder>`
  is the working directory with every non-alphanumeric character replaced by `-`, so it shows
  which project folder the session ran in. Subfolders hold subagent transcripts; skip them.
- Retention: at startup Claude Code deletes transcripts older than `cleanupPeriodDays`. The
  default is 30 days and the minimum is 1. The setting is a top-level key in `settings.json` in
  the configuration folder; when the file is missing, create it as `{"cleanupPeriodDays": 180}`,
  and when it exists, keep its other keys. Sessions started or last continued in Claude Desktop
  or Cowork are kept at any age.
- An `/insights` report: when `usage-data/report.html` exists in the configuration folder, its
  friction and suggestion sections are extra evidence. Do not ask the person to run `/insights`
  for this skill; it uses plan usage of its own.

### With Python: the extractor

`scripts/extract.py` in this skill's folder needs Python 3.7 or later (`python`, `python3` or
`py -3`) and nothing else. It only reads the transcripts.

```
python -I <this skill's folder>/scripts/extract.py --out <new folder in the system temp folder> --since <YYYY-MM-DD>
```

Success: one line per project folder, then a total of projects, sessions and prompts; exit 0.
The output folder holds `summary.md` (counts per project folder, including skill invocations)
and `digest-<project>.md` files (each session's first prompts, truncated, and its tool counts).
`--match <text>` keeps only project folders whose name contains the text; `--projects-dir`
points at another transcripts folder. The output holds project and customer text: keep it
outside every repository and delete it when the report is final.

The transcript format is internal to Claude Code and can change with any release. When the
script fails, or reports no prompts while transcripts exist, use the route below and write
"extractor failed" under Notes in the report header, so the maintainers fix it.

### Without Python

Read each transcript in the window one line at a time as JSON (PowerShell `ConvertFrom-Json`,
or `jq`) and keep only:

- the person's prompts: lines with `"type": "user"` whose `message.content` is text rather than
  a tool result, skipping lines marked `isMeta` and text inside `<system-reminder>` tags. Keep
  the first 1,500 characters of the first prompt and 400 of later ones, at most twelve per
  session;
- skills used: items of type `tool_use` named `Skill` in lines with `"type": "assistant"`, and
  their `skill` input.

Never load a whole transcript into the conversation; they run to megabytes.

## Chat

- Past chats are reachable only with "Search and reference chats" on. The person switches it on
  under Settings > Your Claude (Settings > Memory in older layouts). It is available on Team
  plans. When an Owner has switched memory off for the organisation, it may be unavailable.
- From a chat outside a Project, search reaches chats outside Projects. Chats inside a Project
  are reached only from within that Project: offer to run the skill there as well, or count them
  as not scanned.
- How many chats one search returns, and how far back it reaches, is not documented. Page back
  through recent chats until the window is covered or 60 chats are read.

## Cowork

Where Cowork keeps session history, and whether a Cowork session can read it, is not documented.
Cowork does not read the Claude Code configuration folder. Do not search the computer for it;
suggest running the skill in Claude Code or in chat.
