
# Skoglig förändringsanalys 2015–2025

**Beställare:** Länsstyrelsen X  
**Plats:** Småland  
**År:** 2015–2025  
**Taggar:** Skog, Förändringsanalys, Sverige

!!! abstract "Sammanfattning"
    Jämförelse av skogsmark 2015–2025 med NMD (2015, 2023) och Laserdata NH för strukturindikatorer.
    Arealstatistik per klass (behållen, förlorad, nytillkommen skog) samt kartbilagor och metodik.

## Metodik (svenska dataset)
- Lantmäteriet: Ortofoto, Laserdata NH (DEM), GSD-Hydrografi
- SLU: Nationella Marktäckedata (NMD) 2015–2023
- Skogsstyrelsen: Skogliga grunddata

## Struktur
- `0_Admin/` – avtal, uppdragsbeskrivning, kontakt
- `1_Data/` – rådata/externa källor (lägg inte tunga filer i git)
- `2_Scripts/` – QGIS-stilar, Python/GDAL, GEE-länkar
- `3_Outputs/` – kartor, miniatyrer, symbolik (små filer)
- `4_Documentation/` – rapportutkast, figurer

## Reproducerbarhet
1. Förbered NMD 2015/2023, Laserdata NH.  
2. Kör analys enligt script i `2_Scripts/` (beskriv i README eller notebook).  
3. Exportera resultat (GPKG, PDF-karta, CSV-statistik).

## Licenser & källor
- Följ publiceringsvillkoren för Lantmäteriet, SLU och Skogsstyrelsen.
