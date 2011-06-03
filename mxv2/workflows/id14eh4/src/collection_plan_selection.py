from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataMXv1")


from XSDataMXv1 import XSDataResultStrategy
xsDataResultStrategy = XSDataResultStrategy.parseString(suggestedStrategy)

for xsDataCollectionPlan in xsDataResultStrategy:
    if xsDataCollectionPlan.getCollectionPlanNumber().getValue() == collectionPlanIndex:
        break
