Use case for the EDPluginControlImageQualityIndicators plugin:

This plugin is designed for working with the EDPluginLabelitDistlv1_1 execute plugin.

  - Input : "referenceImage" of type XSDataImage (one or many)
  - Output : "imageQualityIndicators" of type XSDataMXv1.XSDataQualityIndicators (one per referenceImage)
  
If many images are given as input, the EDPluginLabelitDistlv1_1 plugin is launched in
parallel for each image.