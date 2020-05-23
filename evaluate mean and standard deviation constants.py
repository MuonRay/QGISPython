from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

layer = iface.activeLayer()
entries = []

# Define band1
band1 = QgsRasterCalculatorEntry()
band1.ref = 'band@1'
band1.raster = layer
band1.bandNumber = 1
entries.append( band1 )

renderer = layer.renderer()
provider = layer.dataProvider()
extent = layer.extent()

stats = provider.bandStatistics(1, QgsRasterBandStats.All,extent, 0)

myMean = stats.mean
myStdDev = stats.stdDev

myFormula = '(band@1 -' + str(myMean) +')/' + str(myStdDev)

print("mean = ", myMean)

print("stdev = ", myStdDev)

# Process calculation with input extent and resolution
calc = QgsRasterCalculator( myFormula, 
                            '/home/zeito/pyqgis_data/outputfile.tif', 
                            'GTiff',
                            layer.extent(), 
                            layer.width(), 
                            layer.height(), 
                            entries )

calc.processCalculation()