
#!/usr/bin/env python3
import os, sys, shutil, re, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "project_template"
PROJECTS = ROOT / "docs" / "projects"

def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/new_project.py 'Projektnamn' [Beställare] [Plats] [År]")
        sys.exit(1)

    title = sys.argv[1]
    client = sys.argv[2] if len(sys.argv) > 2 else ""
    location = sys.argv[3] if len(sys.argv) > 3 else ""
    years = sys.argv[4] if len(sys.argv) > 4 else ""

    slug = slugify(title)
    dest = PROJECTS / slug
    if dest.exists():
        print(f"ERROR: {dest} exists.")
        sys.exit(2)

    shutil.copytree(TEMPLATE, dest)

    # metadata.yaml
    meta_path = dest / "metadata.yaml"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f)

    meta["title"] = title
    meta["slug"] = slug
    if client:   meta["client"] = client
    if location: meta["location"] = location
    if years:    meta["years"] = years

    with open(meta_path, "w", encoding="utf-8") as f:
        yaml.dump(meta, f, allow_unicode=True, sort_keys=False)

    # index.md placeholders
    md_path = dest / "index.md"
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    repl = {
        "[[Projektnamn]]": title,
        "[[Beställare]]": client or "",
        "[[Plats]]": location or "",
        "[[År]]": years or "",
    }
    for k, v in repl.items():
        text = text.replace(k, v)

    # infoga tags placeholder
    tags = ", ".join(meta.get("tags", []))
    text = text.replace("{{ tags }}", tags)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Created project at {dest}")

if __name__ == "__main__":
    main()
