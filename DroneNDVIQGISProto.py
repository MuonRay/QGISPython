from PyQt5.QtGui import *

from PyQt5.QtCore import *

from qgis.analysis import *

rasterName = "field"

raster = QgsRasterLayer("/qgis_data/rasters/field.tif", rasterName)
ir = QgsRasterCalculatorEntry()}

r = QgsRasterCalculatorEntry()

ir.raster = raster

r.raster = raster

ir-bandNumber = 2

r.bandNumber = 1

ir.ref = rasterName + "@2"

r.ref = rasterName + "@1"

references = (ir.ref, r.ref, ir.ref, r.ref)

exp = "1.0 * (%s - %s) / 1.0 + (%S + %s)" % references
output = "/qgis_data/rasters/ndvi.tif"

e = raster.extent()}

w = raster.width()

h = raster.height()

entries = [ir,r]

ndvi = QgsRasterCalculator(exp, output, "GTiff", e, w, h, entries)
ndvi.processCalculation()

lyr = QgsRasterLayer(output, "NDVI")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax
lyr.setContrastEnhancement(algorithm, limits) :

Ss = QgsRasterShader()

c = QgsColorRampShader()
c.setColorRampType(QgsColorRampShader. INTERPOLATED)
i=[]

qri = QgsColorRampShader.ColorRampltem

iappend(qri(0, QColor(0,0,0,0), ‘NODATA'))

iappend(qri(214, QColor(120,69,25,255), ‘Lowest Biomass'))
iappend(qri(236, QColor(255,178,74,255), ‘Lower Biomass'))
iappend(qri(258, QColor(255,237, 166,255), ‘Low Biomass'))
iappend(qri(280, QColor(173,232,94,255), ‘Moderate Biomass'))
iappend(qri(303, QColor(135,181,64,255), ‘High Biomass’))
iappend(qri(325, QColor(3,156,0,255), ‘Higher Biomass'))
iappend(qri(400, QColor(1,100,0,255), ‘Highest Biomass'))
c.setColorRampltemList(i)

s.setRasterShaderFunction(c)

ps = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1, s)
lyr.setRenderer(ps)
QgsMapLayerRegistry.instance().addMapLayer(lyr)
