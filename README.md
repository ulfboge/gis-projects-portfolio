
# GIS & Fjärranalys – Projektportfölj (MkDocs)

Publika exempelprojekt med svensk inriktning (Lantmäteriet, SLU, Skogsstyrelsen m.fl.).  
Varje projekt ligger i `docs/projects/<slug>/` med metadata och en projektsida (`index.md`).

## Snabbstart

1) Skapa nytt projekt:
```bash
python tools/new_project.py "Skoglig förändringsanalys 2015–2025" "Länsstyrelsen X" "Småland" "2015–2025"
```

2) Bygg startsidan och kör lokalt:
```bash
python tools/build_index.py
mkdocs serve
```

3) Commit & push (sajten byggs och publiceras automatiskt via GitHub Actions).
