# a prototype script that rns in the QGIS Python Console and Generates and NDVI and Key for TIF file orthomosaic drone images
# Coding developed by MuonRay Enterprises Ireland For Drone-based Mapping and Geomatics Projects (2018-2020)
# This work is Creative Commons and is Open to use for educational, non-commercial and NGO use.
from PyQt5.QtGui import *

from PyQt5.QtCore import *

from qgis.analysis import *

rasterName = "farm"
layer = iface.activeLayer()


raster = layer

ir = QgsRasterCalculatorEntry()

r = QgsRasterCalculatorEntry()

ir.raster = raster

r.raster = raster

ir.bandNumber = 2

r.bandNumber = 1

ir.ref = rasterName + "@2"

r.ref = rasterName + "@1"

references = (ir.ref, r.ref, ir.ref, r.ref)

exp = "1.0 * (%s - %s) / 1.0 + (%s + %s)" % references
output = "/qgis_data/rasters/ndvi.tif"

e = raster.extent()

w = raster.width()

h = raster.height()

entries = [ir,r]

ndvi = QgsRasterCalculator(exp, output, "GTiff", e, w, h, entries)
ndvi.processCalculation()

lyr = QgsRasterLayer(output, "NDVI")

ContrastEnhancement = QgsContrastEnhancement.StretchToMinimumMaximum
#
lyr.setContrastEnhancement(ContrastEnhancement,True)

#lyr.setMinimumValue(70)
#lyr.setMaximumValue(255)

renderer = lyr.renderer()
provider = lyr.dataProvider()
extent = lyr.extent()

ver = provider.hasStatistics(1, QgsRasterBandStats.All)

stats = provider.bandStatistics(1, QgsRasterBandStats.All,extent, 0)

if ver is not False:
    print("minimumValue = ", stats.minimumValue)

    print("maximumValue = ", stats.maximumValue)

if (stats.minimumValue < 0):
    min = 0  

else: 
    min= stats.minimumValue

max = stats.maximumValue
range = max - min
add = range//2
interval = min + add

colDic = {'blue':'#ff0000', 'yellow':'#ffff00','red':'#0000ff'}

valueList =[min, interval, max]


qri = QgsColorRampShader.ColorRampItem

myRasterShader = QgsRasterShader() #s

myColorRamp = QgsColorRampShader() #c

i=[]


i.append(qri(0, QColor(0,0,0,0), 'NODATA'))

i.append(qri(214, QColor(120,69,25,255), 'Lowest Biomass'))
i.append(qri(236, QColor(255,178,74,255), 'Lower Biomass'))
i.append(qri(258, QColor(255,237, 166,255), 'Low Biomass'))
i.append(qri(280, QColor(173,232,94,255), 'Moderate Biomass'))
i.append(qri(303, QColor(135,181,64,255), 'High Biomass'))
i.append(qri(325, QColor(3,156,0,255), 'Higher Biomass'))
i.append(qri(400, QColor(1,100,0,255), 'Highest Biomass'))

myColorRamp.setColorRampItemList(i) #c
myColorRamp.setClassificationMode(1) # this line doesn't work #c

myRasterShader.setRasterShaderFunction(myColorRamp) #s


myRasterShader.setRasterShaderFunction(myColorRamp) #s

myPseudoRenderer = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 
                                                    lyr.type(),  
                                                    myRasterShader)

layer.setRenderer(myPseudoRenderer)

layer.triggerRepaint()
