from PyQt5.QtCore import *
from PyQt5.QtGui import *

layer = iface.activeLayer()

renderer = layer.renderer()
provider = layer.dataProvider()
extent = layer.extent()

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

colDic = {'red':'#ff0000', 'yellow':'#ffff00','blue':'#0000ff'}

valueList =[min, interval, max]

lst = [ QgsColorRampShader.ColorRampItem(valueList[0], QColor(colDic['red'])), 
        QgsColorRampShader.ColorRampItem(valueList[1], QColor(colDic['yellow'])), 
        QgsColorRampShader.ColorRampItem(valueList[2], QColor(colDic['blue']))]

myRasterShader = QgsRasterShader()
myColorRamp = QgsColorRampShader()

myColorRamp.setColorRampItemList(lst)
myColorRamp.setClassificationMode(1) # this line doesn't work
myRasterShader.setRasterShaderFunction(myColorRamp)

myPseudoRenderer = QgsSingleBandPseudoColorRenderer(layer.dataProvider(), 
                                                    layer.type(),  
                                                    myRasterShader)

layer.setRenderer(myPseudoRenderer)

layer.triggerRepaint()