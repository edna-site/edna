from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataMXv1")


from XSDataMXv1 import XSDataResultStrategy
xsDataResultStrategy = XSDataResultStrategy.parseString(mxv1StrategyResult)
xsDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()[0]
xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
xsDataSubWedge = xsDataCollectionStrategy.getSubWedge()[0]
xsDataExperimentalCondition = xsDataSubWedge.getExperimentalCondition()
exposureTime = xsDataExperimentalCondition.getBeam().getExposureTime().getValue()
detectorDistance = xsDataExperimentalCondition.getDetector().getDistance().getValue()
oscillationWidth = xsDataExperimentalCondition.getGoniostat().getOscillationWidth().getValue()
rotationAxisStart = xsDataExperimentalCondition.getGoniostat().getRotationAxisStart().getValue()
rotationAxisEnd = xsDataExperimentalCondition.getGoniostat().getRotationAxisEnd().getValue()
noImages = int( (rotationAxisEnd - rotationAxisStart) / oscillationWidth)
runNumberDataCollection = run_number

print "Suggested strategy:"
print "Oscillation start: %.2f" % rotationAxisStart
print "Oscillation width: %.2f" % oscillationWidth
print "No images: %d" % noImages
print "Exposure time: %.2f" % exposureTime
print "Detector distance: %.2f" % detectorDistance
print "Run number: %d " % runNumberDataCollection