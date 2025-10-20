
# [[Projektnamn]]

**Beställare:** [[Beställare]]  
**Plats:** [[Plats]]  
**År:** [[År]]  
**Taggar:** {{ tags }}

!!! abstract "Sammanfattning"
    [[Sammanfattning (2–3 stycken om syfte, metodik och resultat).]]

## Metodik (svenska dataset)
- Lantmäteriet: Ortofoto, Laserdata NH (DEM), GSD-Hydrografi
- SLU: Nationella Marktäckedata (NMD)
- Skogsstyrelsen: Skogliga grunddata
- SMHI (vid behov): nederbörd/avrinning/markfukt

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
