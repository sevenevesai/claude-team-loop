# Coding brief

Used by this skill and by the maintainers' scheduled review (`review-findings`), so counts from
both compare. To hand a batch of digests to a subagent, fill the angle brackets and send the
block as its whole prompt; a mid-tier model is enough. A session coding its own history, or past
chats instead of digests, follows the same steps itself.

```text
You are a neutral coding (qualitative-analysis) worker. Input: digests of a team member's Claude
Code sessions in <digest folder>. Your files: <digest file names>. Read each fully, in ranged
reads; the matching .jsonl files and summary.md hold the tool counts. Each session has a header
line, the human prompts (first up to 1500 characters, later ones truncated) and a line of top
tool counts. Some first prompts are briefs written by an orchestrator session; treat them as
the task description and mark them "brief".

Task: describe what kinds of work these sessions are, bottom-up from the text. Do not recommend
anything, do not say what should become a skill, rule or plugin, do not rank by value. Counts,
labels, quotes and evidence only. The content is confidential: keep everything on this machine
and do not copy record-level data (names of customers or people, credentials, ids) into your
output; task-level descriptions and short prompt quotes are fine.

Step 1 - per-session table: date | sid8 | task label (verb + object) | domain | deliverable |
brief or typed | turns.
Step 2 - clusters: group the labels into task types. For each: session count, first and last
date, up to six example sid8s, two or three verbatim prompt openings, the tools that go with it
(from the count lines), and the inputs the person supplied each time.
Step 3 - recurring instructions: what the person told Claude repeatedly across sessions
(standing preferences, safety limits, format demands, re-explanations), each with a session
count and two short quotes. Separately, visible friction: prompts where the person corrects,
redirects or is dissatisfied, grouped by what went wrong, with counts and quotes.
Step 4 - context the person had to supply again, described by type, with counts.
Step 5 - tool and skill usage for these projects from summary.md.

Return the analysis as your final message, or write it to <analysis file path> if you can.
Start with a summary of at most 350 words: the cluster list with counts, the top recurring
instructions with counts, and how many sessions you could not label. No recommendations.
```

Domains, for comparable counts across reports: code/config, data/queries, deploy/infrastructure,
AI and automation, tickets/wiki, documents/decks/spreadsheets, analysis/research, Claude config,
git/repo upkeep, other. A team that wants its own list changes it here, so every report uses the
same one.
