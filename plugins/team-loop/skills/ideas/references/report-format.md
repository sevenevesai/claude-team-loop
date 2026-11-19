# Findings report format

The maintainers merge reports from many colleagues, by hand or with Claude, and their counts go
into the plugins' backlog. Keep the headings and field names exactly as below. This is format
`team-findings 1`. The same content goes into the shared intake as rows; that layout is in
`intake.md`.

## Privacy rules

The report is shared inside the team. Check every line before the person sees it.

- No names of clients, customers, colleagues, products, systems or projects. Call projects
  "project A", "project B", consistently within one report.
- No record ids, URLs, file paths, email addresses, credentials, or figures from customer or
  project data.
- No text copied from prompts, transcripts or project documents. Describe each task in your own
  words, at the level of "turn meeting notes into ticket updates".
- The person's standing instructions may be paraphrased. Quote one only when the quote holds no
  project detail, for example "check the live environment before answering".

## Template

```markdown
# Team plugin findings

- Format: team-findings 1
- Date: <YYYY-MM-DD>
- Role: <the person's own description, for example "backend developer" or "business analyst">
- Scanned: <Claude Code | chat>, <n> sessions or chats, <first date> to <last date>, <n> projects
- Not scanned: <Cowork, chats in Projects, deleted history, sessions left out for size; or "nothing">
- Plugins: <each team plugin installed, with its version or "version not readable"; then "missing:" and the available team plugins not installed>
- Notes: <"extractor failed", "catalogue not read", a path or setting that differed; or "none">

## Work seen

<Up to eight task types, largest first, one line each: "<task type>: <n> sessions, <n> projects".>

## Team skills used

| Skill | Sessions | Corrected or worked around in |
|---|---|---|
| <plugin:skill> | <n> | <n> |

<Write "none" when no team skill ran in the window.>

## Wins

<"<n> Win lines in project change records", then the ones marked reusable, rewritten without
project detail. Write "none found" when there are none.>

## Findings

### F1. <title: verb and object>

- Kind: new skill | skill change | not installed | working agreement | gate | hook | integration | shared resource | other
- Target: <plugin:skill>, or "new in <plugin>", or "new plugin for <audience or platform>", or "not sure"
- Evidence: <n> sessions, <n> projects, <first month> to <last month>; <what recurs>
- Today: <what the person or Claude does now, including any local skill, rule or override>
- Proposal: <the behaviour to add or change; for a change, the wording you would use>
- Confidence: high | medium | low - <one reason>
```

Number findings F1, F2 and so on, strongest evidence first. A finding that rests on an override
names the skill and the gist of the override line, without project detail. A not installed
finding names, as Target, the skill that would have covered the work; its Proposal is what
would have made the person find that plugin, or "none".
