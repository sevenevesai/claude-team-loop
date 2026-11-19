"""Build upload zips for the plugins under plugins/.

Usage: python tools/package-plugins.py [plugin-name ...] [--out DIR] [--force]

Writes <out>/<name>-<version>.zip with .claude-plugin/ at the top level of the archive, the
layout Claude's Upload plugin accepts. With no names, packages every plugin.
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_DIRS = {"__pycache__", "results"}


def package(plugin_dir: Path, out_dir: Path, force: bool) -> Path:
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    if name != plugin_dir.name:
        raise SystemExit(f"{plugin_dir.name}: plugin.json name is '{name}'; folder and name must match")
    if (plugin_dir / "bin").exists():
        raise SystemExit(f"{name}: has a top-level bin/, which claude.ai rejects")
    target = out_dir / f"{name}-{version}.zip"
    if target.exists() and not force:
        # A changed plugin under an unchanged version would not be seen as an update.
        raise SystemExit(f"{target} exists: bump the version in plugin.json, or pass --force")
    files = [
        p for p in sorted(plugin_dir.rglob("*"))
        if p.is_file() and p.name not in SKIP_NAMES and not SKIP_DIRS.intersection(p.relative_to(plugin_dir).parts)
    ]
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            archive.write(p, p.relative_to(plugin_dir).as_posix())
    print(f"{target}  {len(files)} files  {target.stat().st_size // 1024} KB")
    return target


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("names", nargs="*", help="plugin folder names; default is all")
    parser.add_argument("--out", default=str(root / "dist"))
    parser.add_argument("--force", action="store_true", help="overwrite a zip of the same version")
    args = parser.parse_args()

    plugins_dir = root / "plugins"
    names = args.names or sorted(p.name for p in plugins_dir.iterdir() if (p / ".claude-plugin" / "plugin.json").is_file())
    missing = [n for n in names if not (plugins_dir / n / ".claude-plugin" / "plugin.json").is_file()]
    if missing:
        print(f"no such plugin: {', '.join(missing)}", file=sys.stderr)
        return 2
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in names:
        package(plugins_dir / name, out_dir, args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())
