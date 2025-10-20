# Våtmarkskartering – Miljöövervakning

**Beställare:** Länsstyrelse  
**Plats:** Sverige  
**År:** 2023–2025  
**Taggar:** GIS, Våtmark, Miljöövervakning, Fjärranalys, Sverige

!!! abstract "Sammanfattning"
    Långsiktig våtmarkskartering och miljöövervakning med satellitdata och fältverifiering för att följa våtmarksförändringar över tid. Projektet använder tidsserieanalys av Sentinel-1/2 och Landsat-data för att identifiera trender och förändringar i våtmarksområden.

## Metodik (svenska dataset)
- Lantmäteriet: Ortofoto, Laserdata NH (DEM), GSD-Hydrografi
- SLU: Nationella Marktäckedata (NMD)
- Skogsstyrelsen: Skogliga grunddata
- SMHI: Vattenföring, nederbörd
- Sentinel-1/2 satellitdata (ESA)
- Landsat time series

## Struktur
- `0_Admin/` – avtal, uppdragsbeskrivning, kontakt
- `1_Data/` – rådata/externa källor (lägg inte tunga filer i git)
- `2_Scripts/` – QGIS-stilar, Python/GDAL, GEE-länkar
- `3_Outputs/` – kartor, miniatyrer, symbolik (små filer)
- `4_Documentation/` – rapportutkast, figurer

## Reproducerbarhet
1. Lista steg/skript (i ordning)  
2. Ev. beroenden (Python-paket, QGIS-version)  
3. Hur man kör om analysen från grunden

## Licenser & källor
- Ange villkor för Lantmäteriet/SLU/Skogsstyrelsen – särskilt vid publicering.
