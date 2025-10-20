# Våtmarkskartering – Miljöövervakning

**Beställare:** Länsstyrelsen Z  
**Plats:** Sverige  
**År:** 2023–2025  
**Taggar:** Våtmark, SAR, Sverige

!!! abstract "Sammanfattning"
    Övervakning av våtmarker med tidsserier från SAR (Sentinel‑1) och optiska sensorer (Sentinel‑2/Landsat) för att kvantifiera förändringar i vattennivå, utbredning och vegetationens fuktighet. Metodiken kombinerar radarbaserade våtmarksindikatorer med optiska index samt hydrologiska referensdata.

## Syfte och mål
- Kartlägga och följa förändringar i våtmarkers utbredning (areal, klass) 2019–2025.
- Ta fram indikatorer: permanent/temporärt vatten, fuktiga ytor, vegetationsdynamik.
- Leverera årsvisa lager, sammanställd trend och rapport med metodik och osäkerhet.

## Avgränsning
- AOI: enligt `metadata.yaml` (bbox och koordinatsystem).  
- Tidsperiod: 2019–2025 (med baslinje 2019/2020 beroende på datatäckning).

## Data och förbehandling
- Lantmäteriet: Ortofoto (referens/validering), Laserdata NH (DEM för avrinning), GSD‑Hydrografi (vattennät).  
- SLU: NMD (masker/klassfilter).  
- Skogsstyrelsen: Skogliga grunddata (komplement till maskning).  
- SMHI: Vattenföring/nederbörd (för händelsekontekst och säsongsnormaler).  
- ESA Copernicus: Sentinel‑1 GRD (VV/VH, backscatter, speckle‑filter), Sentinel‑2 L2A (molnmaskerad reflektans).  
- USGS/NASA: Landsat 5/7/8/9 (ytvatten-/vegetationsindex i historik).  

## Metodik (översikt)
1) Sentinel‑1: kalibrering → speckle‑reducering → backscatter‑statistik per säsong → indikator för våta ytor.  
2) Sentinel‑2/Landsat: molnmask → index (NDWI/MNDWI, NDVI) → säsongsmedel och percentiler.  
3) DEM‑derivat (flödesackumulation, sänkor) för att stödja sannolik våtmark.  
4) Sammanvägning (rule‑based/klassificering) till klasser: vatten, fuktig mark, torr mark.  
5) Årsvisa mosaiker och trendanalys (ökning/minskning, stabil).  
6) Validering mot ortofoto/SMHI‑serier och manuella tolkningspunkter.

## Arbetsflöde (reproducerbart)
1. Skapa och aktivera miljö  
   ```bash
   pip install rasterio geopandas numpy pandas scikit-image scipy earthengine-api
   ```
2. Ladda ner/åtkomst till tidsserier (GEE‑script eller Copernicus Hub API).  
3. Kör förbehandling och index‑beräkning (skript i `2_Scripts/`).  
4. Generera lager i `3_Outputs/`:
   - `wetlands_status_{year}.tif` (klass)
   - `wetness_index_{year}.tif` (kontinuerlig)
   - `wetlands_trend_2019_2025.tif`  
5. Exportera sammanfattning (areal per klass och år) till `3_Outputs/summary.csv`.  
6. Uppdatera kartor/figurer och rapportutdrag i `4_Documentation/`.

## Leverabler
- GeoPackage med klassade lager (status/trend) och metadata (HMK).  
- Raster: våtmarksstatus/indikatorer per år samt trendlager.  
- PDF‑kartor (A3/A4) med layout och teckenförklaring.  
- Sammanfattande rapport (PDF) med metod, resultat, kvalitet och osäkerhet.

## Figurer (platshållare)
- Figur 1: Översiktskarta AOI.  
- Figur 2: Exempel på S1‑baserad våthetsindikator.  
- Figur 3: Trend 2019–2025 (ökning/minskning).

## Struktur
- `0_Admin/` – avtal, uppdragsbeskrivning, kontakt  
- `1_Data/` – rådata/externa källor (lägg inte tunga filer i git)  
- `2_Scripts/` – QGIS‑stilar, Python/GDAL, GEE‑länkar  
- `3_Outputs/` – kartor, miniatyrer, symbolik (små filer)  
- `4_Documentation/` – rapportutkast, figurer  

## Kvalitet & begränsningar
- SAR reagerar starkt på vegetation/struktur; kombination med optik minskar feltolkning.  
- Moln i optik täcks via molnmask och tidsmedel men kan minska täckning.  
- DEM‑produkter påverkar hydrologiska derivat (kvalitet varierar regionalt).  
- Rekommenderat: regional kalibrering och punktvalidering per delområde.

## Licenser & källor
- Följ publiceringsvillkor för Lantmäteriet, SLU, Skogsstyrelsen, SMHI och Copernicus.  
- Ange källa i figurer/kartor och i metadata.
