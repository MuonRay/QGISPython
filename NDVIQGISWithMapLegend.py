from PyQt5.QtGui import *

from PyQt5.QtCore import *

from qgis.analysis import *

layer = iface.activeLayer()

raster = layer

ir = QgsRasterCalculatorEntry()

r = QgsRasterCalculatorEntry()

ir.raster = raster

r.raster = raster

ir.bandNumber = 1

r.bandNumber = 3

ir.ref = rasterName + "@1"

r.ref = rasterName + "@3"

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

#ContrastEnhancement = QgsContrastEnhancement.StretchToMinimumMaximum
ContrastEnhancement = QgsContrastEnhancement.StretchAndClipToMinimumMaximum

lyr.setContrastEnhancement(ContrastEnhancement,True)

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

colDic = {'red':'#ff0000', 'green':'#00ff00', 'yellow':'#ffff00','blue':'#0000ff','white':'#ffffff','maroon':'#800000' }

valueList =[min, interval, max]


qri = QgsColorRampShader.ColorRampItem

myRasterShader = QgsRasterShader() #s

myColorRamp = QgsColorRampShader() #c

i=[]

i.append(qri(0, QColor(0,0,0,0), 'NODATA'))
i.append(qri(100, QColor(120,69,25,255), 'Lowest Biomass'))
i.append(qri(130, QColor(255,178,74,255), 'Lower Biomass'))
i.append(qri(160, QColor(255,237, 166,255), 'Low Biomass'))
i.append(qri(190, QColor(173,232,94,255), 'Moderate Biomass'))
i.append(qri(220, QColor(135,181,64,255), 'High Biomass'))
i.append(qri(250, QColor(3,156,0,255), 'Higher Biomass'))
i.append(qri(280, QColor(1,100,0,255), 'Highest Biomass'))

myColorRamp.setColorRampItemList(i) #c
myColorRamp.setClassificationMode(1) # this line doesn't work #c

myRasterShader.setRasterShaderFunction(myColorRamp) #s
myRasterShader.setRasterShaderFunction(myColorRamp) #s

myPseudoRenderer = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 
                                                    lyr.type(),  
                                                    myRasterShader)

layer.setRenderer(myPseudoRenderer)

layer.triggerRepaint()