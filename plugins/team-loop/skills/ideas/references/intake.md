Link: not set

Maintainers: before publishing, replace "not set" above with the link of the team's shared
findings sheet. While it reads "not set", sessions treat the intake as absent and the person
sends the report file instead.

# Shared findings intake

A Claude Sheet (for example "Plugin Ideas Log") that the maintainers own and share with the team
with edit access. It is the one intake for every team plugin, used by this skill and by
`adapt-skill`. The maintainers' scheduled review (`review-findings`) reads it.

## Plugins tab: the catalogue

Read only. One row per team plugin, then one per skill: Plugin, Version, Available ("yes" when
it is in the organisation's plugin library, "not yet" when it is coming), Skill ("(plugin)" for
the plugin's own row), and What it does (the plugin's or skill's description). The maintainers
refresh it with every release.

## Findings tab: where rows go

A table whose first row holds these columns, in this order:

| Column | Holds |
|---|---|
| A Date | the report's date, YYYY-MM-DD |
| B Role | the report's Role line |
| C Scanned | the report's Scanned line; "adapt-skill note" for a row from `adapt-skill` |
| D Plugins | the report's Plugins line |
| E Kind | one of: new skill, skill change, not installed, working agreement, gate, hook, integration, shared resource, other; for the report's other sections: work seen, skill used, wins |
| F Plugin | the plugin the row is about, such as team-loop; "new plugin" for one that does not exist yet; empty for work seen and wins rows |
| G Target | plugin:skill, "new in <plugin>", "new plugin for <audience or platform>" or "not sure"; the skill for a skill used row; empty otherwise |
| H Title | the finding's title, or the task type for a work seen row |
| I Evidence | the finding's Evidence line; for other rows the counts |
| J Today | the finding's Today line |
| K Proposal | the finding's Proposal line; the reusable wins for a wins row |
| L Confidence | high, medium or low, with its reason |
| M Status | new |
| N Maintainer note | leave empty |

Kind and Status are dropdowns: write the labels exactly as above, or the write is refused.
Status and Maintainer note belong to the maintainers once a row is in.

Write one row per finding, per "Work seen" line and per "Team skills used" row, and one wins row,
all in one write starting on the first empty row under the table. When the write is refused
because someone else wrote meanwhile, read the tab again and write under its new last row.

Never change or delete other rows, or anything on the Plugins tab: the sheet has no protected
ranges, so everyone's rows depend on each session keeping to its own. When the sheet cannot be
opened or written, tell the person why and fall back to the file.
