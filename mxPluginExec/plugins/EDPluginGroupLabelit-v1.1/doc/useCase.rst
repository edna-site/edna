The EDPluginLabelitDistlv1_1 plugin:
  - Input : "referenceImage" of type XSDataImage (only the first image is taken into account)
  - Output : "imageQualityIndicators" of type XSDataLabelitv1_1.XSDataQualityIndicators

The EDPluginLabelitIndexingv1_1 plugin:
  - Input : "referenceImage" of type XSDataImage (only the first two images are taken into account)
  - Output : "labelitScreenOutput" of type XSDataLabelitv1_1.XSDataLabelitScreenOutput
             "mosflmScriptsOutput" of type XSDataLabelitv1_1.XSDataLabelitMosflmScriptsOutput

The EDPluginLabelitIndexingv1_1 plugin has for the moment the following limitations:
  - No possibility for forcing the space group
  - Only one or two reference images are taken into account
  
