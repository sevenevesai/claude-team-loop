"""Print the rows of the findings sheet's Plugins tab, which `team-loop:ideas` reads.

Usage: python tools/plugin-catalogue.py --published NAME [--published NAME ...]

Prints a JSON array of rows, header first: one row per plugin, then one per skill. Plugins not
named with --published are listed as "not yet", so `ideas` knows what is coming without telling
colleagues to install it. Claude writes the rows into the tab with the Claude Docs connector.
"""
import argparse
import json
import re
import sys
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.S)


def frontmatter(skill_md: Path) -> dict:
    match = FRONTMATTER.match(skill_md.read_text(encoding="utf-8"))
    if not match:
        raise SystemExit(f"{skill_md}: no frontmatter")
    fields = {key: unquote(value) for key, value in re.findall(r"^(\w[\w-]*):[ \t]*(.*)$", match.group(1), re.M)}
    if not fields.get("name") or not fields.get("description"):
        raise SystemExit(f"{skill_md}: frontmatter needs name and description on one line each")
    return fields


def unquote(value: str) -> str:
    """A YAML scalar as its text: imported skills quote their descriptions."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            return json.loads(value)  # YAML double-quoted escapes used here are JSON's
        except json.JSONDecodeError:
            return value[1:-1]
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--published", action="append", default=[], metavar="NAME",
                        help="a plugin published to the organisation library; repeat for each")
    args = parser.parse_args()

    plugins = [p for p in (root / "plugins").iterdir() if (p / ".claude-plugin" / "plugin.json").is_file()]
    plugins.sort(key=lambda p: (p.name not in args.published, p.name))
    unknown = set(args.published) - {p.name for p in plugins}
    if unknown:
        print(f"no such plugin: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    rows = [["Plugin", "Version", "Available", "Skill", "What it does"]]
    for plugin in plugins:
        manifest = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        available = "yes" if plugin.name in args.published else "not yet"
        rows.append([plugin.name, manifest["version"], available, "(plugin)", manifest.get("description", "")])
        for skill_md in sorted(plugin.glob("skills/*/SKILL.md")):
            fields = frontmatter(skill_md)
            rows.append([plugin.name, manifest["version"], available, fields["name"], fields["description"]])
    sys.stdout.reconfigure(encoding="utf-8")  # descriptions hold non-ASCII; Windows consoles default to cp1252
    json.dump(rows, sys.stdout, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
