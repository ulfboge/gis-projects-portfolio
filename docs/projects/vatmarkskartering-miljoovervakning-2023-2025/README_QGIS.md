### Körning i QGIS (Våtmarkskartering – Miljöövervakning)

1) Öppna QGIS och gå till Processing‑verktygslådan.
2) Scripts → Tools → Add script from file…
3) Välj `2_Scripts/process_wetlands.py` (den dyker upp under gruppen "Wetlands").
4) Kör "Wetlands: Build status/trend (scaffold)" med:
   - Startår/Slutår: t.ex. 2019–2025
   - Utdata‑mapp: peka på `3_Outputs/`
   - AOI eller Extent: valfritt (placeholder använder projektets extent)
5) Efter körning: 
   - `3_Outputs/status/wetlands_status_{år}.tif`
   - `3_Outputs/trend/wetlands_trend_{start}_{end}.tif`
   - `3_Outputs/summary.csv`

Byt ut placeholder‑stegen i `process_wetlands.py` mot din riktiga S1/S2‑preprocess.

