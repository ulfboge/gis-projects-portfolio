
#!/usr/bin/env python3
import yaml, pathlib, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "docs" / "projects"
INDEX = ROOT / "docs" / "index.md"

def load_meta(p: pathlib.Path):
    m = p / "metadata.yaml"
    if not m.exists():
        return None
    with open(m, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def card_block(title, url, client, years, summary, tags):
    chips = "".join([f'<span class="mdx-chip">{t}</span>' for t in tags]) if tags else ""
    meta_line = " — ".join([x for x in [client, years] if x])
    return textwrap.dedent(f"""
    <div class="grid cards" markdown>
    -   :material-folder-open: **[{title}]({url})**  
        *{meta_line}*  
        {summary if summary else ""}
        
        {chips}
    </div>
    """)

def main():
    items = []
    for proj in sorted(PROJECTS_DIR.glob("*")):
        if proj.is_dir():
            meta = load_meta(proj) or {}
            title = meta.get("title", proj.name)
            slug = meta.get("slug", proj.name)
            client = meta.get("client","")
            years  = meta.get("years","")
            summary = (meta.get("summary","") or "").strip()
            tags = meta.get("tags", [])
            url = f"projects/{slug}/"
            items.append((title, url, client, years, summary, tags))

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write("# Projektportfölj – GIS & Fjärranalys (Sverige)\n\n")
        f.write("Nedan listas publika exempelprojekt. Klicka för detaljer, metodik och material.\n\n")
        for it in items:
            f.write(card_block(*it))
            f.write("\n")

    print(f"Wrote {INDEX}")

if __name__ == "__main__":
    main()
