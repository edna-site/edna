"""complex type XSDataInputBioSaxsHPLCv1_0 extends XSDataInputBioSaxsProcessOneFilev1_0{
    "Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"
//    rawImage : XSDataImage
//    sample: XSDataBioSaxsSample
//    experimentSetup: XSDataBioSaxsExperimentSetup
//    rawImageSize : XSDataInteger optional
//    logFile : XSDataFile optional
//    normalizedImage : XSDataImage optional
//    integratedCurve : XSDataFile optional
//    runId: XSDataString optional
//    frameId: XSDataInteger optional
    bufferCurve : XSDataFile optional
    subtractedCurve: XSDataFile optional
    gnomFile: XSDataFile optional
}

complex type XSDataResultBioSaxsHPLCv1_0 extends XSDataResultBioSaxsSubtractv1_0{
    "Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"
    integratedCurve: XSDataFile
    bufferCurve: XSDataFile optional
//    subtractedCurve : XSDataFile
//    autorg: XSDataAutoRg
//  gnom: XSDataGnom
//    volume: XSDataDoubleWithUnit
}"""
