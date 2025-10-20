"""
QGIS Processing algorithm: Wetlands status/trend scaffold (Sentinel-1/2 placeholders)

This script provides a runnable scaffold inside QGIS Processing. It prepares
project folders, validates inputs, and writes placeholder rasters/vectors
that downstream cartography can style. Replace the placeholder computations
with your actual S1/S2 preprocessing steps.

Usage (in QGIS): Processing Toolbox -> Scripts -> Tools -> Add script from file...
Select this file, then run "Wetlands: Build status/trend (scaffold)".
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterExtent,
    QgsProcessingParameterNumber,
    QgsProcessingParameterFileDestination,
    QgsProcessingParameterFolderDestination,
    QgsProcessingParameterBoolean,
    QgsCoordinateReferenceSystem,
    QgsProject,
    QgsRasterFileWriter,
)
from qgis import processing
import os


class WetlandsBuildAlgorithm(QgsProcessingAlgorithm):
    """Scaffold algorithm for wetlands status/trend outputs."""

    INPUT_AOI = "INPUT_AOI"
    EXTENT = "EXTENT"
    START_YEAR = "START_YEAR"
    END_YEAR = "END_YEAR"
    OUTPUT_FOLDER = "OUTPUT_FOLDER"
    CREATE_PLACEHOLDERS = "CREATE_PLACEHOLDERS"

    def tr(self, string: str) -> str:
        return QCoreApplication.translate("WetlandsBuildAlgorithm", string)

    def createInstance(self):
        return WetlandsBuildAlgorithm()

    def name(self) -> str:
        return "wetlands_build_status_trend_scaffold"

    def displayName(self) -> str:
        return self.tr("Wetlands: Build status/trend (scaffold)")

    def group(self) -> str:
        return self.tr("Wetlands")

    def groupId(self) -> str:
        return "wetlands_group"

    def shortHelpString(self) -> str:
        return self.tr(
            "Förbereder utskriftsmappar och skriver platshållare för status/trend.\n"
            "Byt ut placeholder-stegen mot din S1/S2-preprocess."
        )

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT_AOI,
                self.tr("AOI (polygon)"),
                [QgsProcessing.TypeVectorPolygon],
                optional=True,
            )
        )
        self.addParameter(
            QgsProcessingParameterExtent(
                self.EXTENT,
                self.tr("AOI-utbredning (om AOI inte anges)"),
                optional=True,
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.START_YEAR,
                self.tr("Startår"),
                type=QgsProcessingParameterNumber.Integer,
                defaultValue=2019,
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.END_YEAR,
                self.tr("Slutår"),
                type=QgsProcessingParameterNumber.Integer,
                defaultValue=2025,
            )
        )
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUT_FOLDER,
                self.tr("Utdata-mapp (3_Outputs)"),
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.CREATE_PLACEHOLDERS,
                self.tr("Skriv platshållare (enkla GeoTIFF + CSV)"),
                defaultValue=True,
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        start_year = int(self.parameterAsInt(parameters, self.START_YEAR, context))
        end_year = int(self.parameterAsInt(parameters, self.END_YEAR, context))
        out_dir = self.parameterAsFile(parameters, self.OUTPUT_FOLDER, context)
        make_ph = self.parameterAsBool(parameters, self.CREATE_PLACEHOLDERS, context)

        if end_year < start_year:
            raise QgsProcessingException(self.tr("Slutår måste vara >= startår"))

        # Ensure subfolders
        status_dir = os.path.join(out_dir, "status")
        trend_dir = os.path.join(out_dir, "trend")
        os.makedirs(status_dir, exist_ok=True)
        os.makedirs(trend_dir, exist_ok=True)

        # Placeholder generation
        if make_ph:
            # Create trivial CSV summary placeholder
            csv_path = os.path.join(out_dir, "summary.csv")
            with open(csv_path, "w", encoding="utf-8") as f:
                f.write("year,water,wet,other\n")
                for y in range(start_year, end_year + 1):
                    f.write(f"{y},0,0,0\n")

            # Create small dummy rasters as placeholders (1x1 pixel GeoTIFF)
            # Use processing "Create constant raster layer" to avoid complex GDAL code
            for y in range(start_year, end_year + 1):
                out_tif = os.path.join(status_dir, f"wetlands_status_{y}.tif")
                processing.run(
                    "gdal:rasterize",
                    {
                        # Use extent from project or fallback
                        "INPUT": None,
                        "FIELD": None,
                        "BURN": 1,
                        "UNITS": 1,
                        "WIDTH": 1,
                        "HEIGHT": 1,
                        "EXTENT": context.project().extent() if QgsProject.instance() else None,
                        "NODATA": 0,
                        "DATA_TYPE": 5,  # Float32
                        "INIT": 0,
                        "INVERT": False,
                        "EXTRA": "",
                        "OUTPUT": out_tif,
                    },
                    context=context,
                    feedback=feedback,
                )

            # Trend placeholder
            trend_tif = os.path.join(trend_dir, f"wetlands_trend_{start_year}_{end_year}.tif")
            processing.run(
                "gdal:rasterize",
                {
                    "INPUT": None,
                    "FIELD": None,
                    "BURN": 0,
                    "UNITS": 1,
                    "WIDTH": 1,
                    "HEIGHT": 1,
                    "EXTENT": context.project().extent() if QgsProject.instance() else None,
                    "NODATA": 0,
                    "DATA_TYPE": 5,
                    "INIT": 0,
                    "INVERT": False,
                    "EXTRA": "",
                    "OUTPUT": trend_tif,
                },
                context=context,
                feedback=feedback,
            )

        feedback.pushInfo(self.tr("Platshållare skapade. Ersätt med verklig preprocess i detta skript."))
        return {self.OUTPUT_FOLDER: out_dir}


def classFactory(iface):  # Required for QGIS Script loader
    return WetlandsBuildAlgorithm()


