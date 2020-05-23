layer = iface.activeLayer()
renderer = layer.renderer()
provider = layer.dataProvider()

bands = renderer.usesBands()

min = [provider.bandStatistics(band, QgsRasterBandStats.All).minimumValue 
            for band in bands]

max = [provider.bandStatistics(band, QgsRasterBandStats.All).maximumValue 
            for band in bands]

print(min)
print(max)

ContrastEnhancement = QgsContrastEnhancement.StretchToMinimumMaximum

myRedBand = layer.renderer().redBand()
myRedType = layer.renderer().dataType(myRedBand)
myRedEnhancement = QgsContrastEnhancement(myRedType)
myRedEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement,True)
myRedEnhancement.setMinimumValue(70)
myRedEnhancement.setMaximumValue(255)
layer.renderer().setRedContrastEnhancement(myRedEnhancement)

myGreenBand = layer.renderer().greenBand()
myGreenType = layer.renderer().dataType(myGreenBand)
myGreenEnhancement = QgsContrastEnhancement(myGreenType)
myGreenEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement,True)
myGreenEnhancement.setMinimumValue(89)
myGreenEnhancement.setMaximumValue(255)
layer.renderer().setGreenContrastEnhancement(myGreenEnhancement)

myBlueBand = layer.renderer().blueBand()
myBlueType = layer.renderer().dataType(myBlueBand)
myBlueEnhancement = QgsContrastEnhancement(myBlueType)
myBlueEnhancement.setContrastEnhancementAlgorithm(ContrastEnhancement,True)
myBlueEnhancement.setMinimumValue(90)
myBlueEnhancement.setMaximumValue(255)
layer.renderer().setBlueContrastEnhancement(myBlueEnhancement)

layer.triggerRepaint()