# get the raster layer
layer = iface.activeLayer()

# define the filter
contrastFilter = QgsBrightnessContrastFilter()
contrastFilter.setContrast(50)

# assign filter to raster pipe
layer.pipe().set(contrastFilter)

# apply changes
layer.triggerRepaint()

# to set contrast back, change properties of assigned filter.
# DO NOT ASSIGN THIS OR ANOTHER QgsBrightnessContrastFilter AGAIN, QGIS WILL CRASH
contrastFilter.setContrast(0)
layer.triggerRepaint()