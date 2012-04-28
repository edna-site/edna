# coding: utf8
#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginExecSimpleHTMLPagev1_0.py.py 2100 2010-09-27 09:17:13Z svensson $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os, shutil, time, cgi

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath

EDFactoryPluginStatic.loadModule("markupv1_7")
import markupv1_7

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataSimpleHTMLPagev1_0 import XSDataInputSimpleHTMLPage
from XSDataSimpleHTMLPagev1_0 import XSDataResultSimpleHTMLPage

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan


class EDPluginExecSimpleHTMLPagev1_0(EDPluginExec):
    """
    This plugin launches the EDPluginExecOutputHTMLv1_0 for creating web pages for ISPyB
    """

    def __init__ (self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputSimpleHTMLPage)
        self.strPluginExecOutputHTMLName = "EDPluginExecOutputHTMLv1_0"
        self.edPluginExecOutputHTML = None
        self.strHTML = None
        self.xsDataResultCharacterisation = None
        self.page = None
        self.strPath = None
        self.strTableColourTitle1 = "#F5F5FF"
        self.strTableColourTitle2 = "#F0F0FF" 
        self.strTableColourRows   = "#FFFFA0"
        self.strPageEDNALog = None


    def preProcess(self, _edPlugin=None):
        EDPluginExec.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.preProcess...")
        self.xsDataResultCharacterisation = self.getDataInput().getCharacterisationResult()
        self.strHtmlFileName = "index.html"
        self.strPath = os.path.join(self.getWorkingDirectory(), self.strHtmlFileName)


    def process(self, _edPlugin=None):
        EDPluginExec.process(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.process...")
        if self.xsDataResultCharacterisation is not None:
            # Create the simple characterisation result page
            self.page = markupv1_7.page(mode='loose_html')
            self.page.init( title="Characterisation Results", 
                       footer="Generated on %s" % time.asctime())
            self.page.div( align_="CENTER")
            self.page.h1()
            if self.xsDataResultCharacterisation is not None:
                self.page.strong( "Characterisation Results " )
            else:
                self.page.strong( "No Characterisation Results! " )
            # Link to the EDNA log file
            strPathToLogFile = self.findEDNALogFile()
            if strPathToLogFile is not None:
                self.page.strong("(")
                self.strPageEDNALog = os.path.join(self.getWorkingDirectory(), "edna_log.html")
                pageEDNALog = markupv1_7.page()
                pageEDNALog.h1("EDNA Log")
                pageEDNALog.a("Back to previous page", href_=self.strHtmlFileName)
                pageEDNALog.pre(cgi.escape(EDUtilsFile.readFile(strPathToLogFile)))
                pageEDNALog.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(self.strPageEDNALog, str(pageEDNALog))
                self.page.a("EDNA log file", href_="edna_log.html")
                self.page.strong(")")
            self.page.h1.close()
            self.page.div.close()
            self.diffractionPlan()
            self.page.hr()
            self.strategyResults()
            self.graphs()
            self.page.hr()
            self.indexingResults()
            self.imageQualityIndicatorResults()
        


    def finallyProcess(self, _edPlugin=None):
        EDPluginExec.finallyProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.finallyProcess...")
        # Render the page
        strHTML = str(self.page)
        EDUtilsFile.writeFile(self.strPath, strHTML)
        xsDataResultSimpleHTMLPage = XSDataResultSimpleHTMLPage()
        xsDataResultSimpleHTMLPage.setPathToHTMLFile(XSDataFile(XSDataString(self.strPath)))
        xsDataResultSimpleHTMLPage.setPathToHTMLDirectory(XSDataFile(XSDataString(os.path.dirname(self.strPath))))
        self.setDataOutput(xsDataResultSimpleHTMLPage)
        # Store in Pyarch
        strPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchHtmlDirectoryPath(self.xsDataResultCharacterisation.getDataCollection())
        if strPyarchPath is None:
            # For debugging purposes
            strPyarchPath = EDUtilsPath.getEdnaUserTempFolder()
        EDHandlerESRFPyarchv1_0.copyHTMLDir(_strPathToHTMLDir=os.path.dirname(self.strPath), _strPathToPyarchDirectory=strPyarchPath)


    def indexingResults(self):
        # Was the indexing successful?
        xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
        strForcedSpaceGroup = None
        # Check for forced space group!
        if self.xsDataResultCharacterisation.dataCollection.diffractionPlan is not None:
            if self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup is not None:
                strForcedSpaceGroup = self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup.value
        if xsDataResultIndexing:
            self.page.hr()
            # Table containg indexing results and thumbnail images
            self.page.table( class_='indexResultsAndThumbnails', border_="0", cellpadding_="0")
            self.page.tr( align_="CENTER" )
            self.page.td()
            # Table with indexing results
            self.createTableWithIndexResults(xsDataResultIndexing, strForcedSpaceGroup)
            self.page.td.close()
            # Thumbnail images
            self.page.td()
            self.createThumbnailRowOfImages(xsDataResultIndexing)
            self.page.td.close()
            self.page.tr.close()
            self.page.table.close()

    
    def strategyResults(self):
        # Was the strategy successful?
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()
        self.page.hr()
        if xsDataResultStrategy is None:
            # Check if indexing and integration results
            xsDataResultIntegration = self.xsDataResultCharacterisation.getIntegrationResult()
            xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
            if xsDataResultIndexing is None:
                self.page.h2()
                self.page.strong("Strategy calculation not performed due to indexing failure, see the " )  
                self.page.a("EDNA log file", href=self.strPageEDNALog)
                self.page.strong(" for more details" )  
                self.page.h2.close()
            elif xsDataResultIntegration is None:
                self.page.h2()
                self.page.strong("Strategy calculation not performed due to integration failure, see the " )  
                self.page.a("EDNA log file", href=self.strPageEDNALog)
                self.page.strong(" for more details" )  
                self.page.h2.close()
            else:
                self.page.h2()
                self.page.strong( "Strategy calculation failed, see the " )
                self.page.a("EDNA log file", href=self.strPageEDNALog)
                self.page.strong(" for more details" )  
                self.page.h2.close()
        else:
            # Add link to BEST log file:
            if xsDataResultStrategy.getBestLogFile():
                strPathToBestLogFile = xsDataResultStrategy.getBestLogFile().getPath().getValue()
                strPageBestLog = os.path.join(self.getWorkingDirectory(), "best_log.html")
                pageBestLog = markupv1_7.page()
                pageBestLog.h1("BEST Log")
                pageBestLog.a("Back to previous page", href_=self.strHtmlFileName)
                pageBestLog.pre(cgi.escape(EDUtilsFile.readFile(strPathToBestLogFile)))
                pageBestLog.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(strPageBestLog, str(pageBestLog))
            # Add link to RADDOSE log file:
            strPageRaddoseLog = None
            if xsDataResultStrategy.getRaddoseLogFile():
                strPathToRaddoseLogFile = xsDataResultStrategy.getRaddoseLogFile().getPath().getValue()
                strPageRaddoseLog = os.path.join(self.getWorkingDirectory(), "raddose_log.html")
                pageRaddoseLog = markupv1_7.page()
                pageRaddoseLog.h1("RADDOSE Log")
                pageRaddoseLog.a("Back to previous page", href_=self.strHtmlFileName)
                pageRaddoseLog.pre(cgi.escape(EDUtilsFile.readFile(strPathToRaddoseLogFile)))
                pageRaddoseLog.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(strPageRaddoseLog, str(pageRaddoseLog))
            listXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            iNoSubWedges = len(listXSDataCollectionPlan)
            self.page.h2()
            if iNoSubWedges != 1:
                self.page.strong("Multi-wedge collection plan strategy (")
            else:
                self.page.strong( "Collection plan strategy (" )
            if strPageRaddoseLog is not None:
                self.page.a("RADDOSE log file", href="raddose_log.html")
                self.page.strong(", ")
            self.page.a("BEST log file", href="best_log.html")
            self.page.strong(")")
            self.page.h2.close()
            # Check if ranking resolution is higher than the suggested strategy resolution(s)
            bHigherResolutionDetected = False
            fRankingResolution = None
            fResolutionMax = None
            fDistanceMin = None
            for xsDataCollectionPlan in listXSDataCollectionPlan:
                xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                if xsDataSummaryStrategy.getRankingResolution():
                    # Retrieve the resolution...
                    fResolution = xsDataSummaryStrategy.getResolution().getValue()
                    # Retrieve the detector distance...
                    fDistance = xsDataCollectionStrategy.getSubWedge()[0].getExperimentalCondition().getDetector().getDistance().getValue()
                    if fResolutionMax is None:
                        fResolutionMax = fResolution
                        fDistanceMin = fDistance
                    elif (fResolution < fResolutionMax) and (abs(fResolution-fResolutionMax) > 0.1):
                        fResolutionMax = fResolution                        
                        fDistanceMin = fDistance
                    fRankingResolution = xsDataSummaryStrategy.getRankingResolution().getValue()
            
            if fRankingResolution != None and fResolutionMax != None:
                if fRankingResolution < fResolutionMax:
                    if not bHigherResolutionDetected:
                        self.page.font(_color="red", size="+2")
                        self.page.i()
                        self.page.h2("Best has detected that the sample can diffract to %.2f &Aring;!" % fRankingResolution)
                        self.page.i.close()
                        self.page.font.close()
                        self.page.font(_color="red", size="+1")
                        self.page.strong("The current strategy is calculated to %.2f &Aring;." % fResolutionMax)
                        #self.page.strong("In order to calculate a strategy to %.2f &Aring; set the detector distance to %.2f mm (%.2f &Aring;) and re-launch the EDNA characterisation." % (fRankingResolution,fDistanceMin,fRankingResolution))
                        self.page.strong("In order to calculate a strategy to %.2f &Aring; move the detector to collect %.2f &Aring; data and re-launch the EDNA characterisation." % (fRankingResolution,fRankingResolution))
                        self.page.font.close()
                    bHigherResolutionDetected = True
                
                
            for xsDataCollectionPlan in listXSDataCollectionPlan:
                xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                fResolutionMax = xsDataSummaryStrategy.getResolution().getValue()
                strResolutionReasoning = ""
                if xsDataSummaryStrategy.getResolutionReasoning():
                    strResolutionReasoning = xsDataSummaryStrategy.getResolutionReasoning().getValue()
                self.page.table( class_='indexResults', border_="1", cellpadding_="0")
                self.page.tr( align_="CENTER" )
                self.page.th(strResolutionReasoning, colspan_="9", bgcolor_=self.strTableColourTitle1)
                self.page.tr.close()
                self.page.tr( align_="CENTER", bgcolor_=self.strTableColourTitle2)
                self.page.th("Wedge")
                self.page.th("Subwedge")
                self.page.th("Start (&deg;)")
                self.page.th("Width (&deg;)")
                self.page.th("No images")
                self.page.th("Exp time (s)")
                self.page.th("Max res (&Aring;)")
                self.page.th("Rel trans (%)")
                self.page.th("Distance (mm)")
                self.page.tr.close()
                xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                for xsDataSubWegde in xsDataCollectionStrategy.getSubWedge():
                    xsDataExperimentalCondition = xsDataSubWegde.getExperimentalCondition()
                    iWedge = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
                    iRunNumber = xsDataSubWegde.getSubWedgeNumber().getValue()
                    fRotationAxisStart = xsDataExperimentalCondition.getGoniostat().getRotationAxisStart().getValue()
                    fRotationAxisEnd = xsDataExperimentalCondition.getGoniostat().getRotationAxisEnd().getValue()
                    fOscillationWidth = xsDataExperimentalCondition.getGoniostat().getOscillationWidth().getValue()
                    iNumberOfImages = int((fRotationAxisEnd-fRotationAxisStart)/fOscillationWidth)
                    fExposureTime = xsDataExperimentalCondition.getBeam().getExposureTime().getValue()
                    fTransmission = xsDataExperimentalCondition.getBeam().getTransmission().getValue()
                    fDistance = xsDataExperimentalCondition.getDetector().getDistance().getValue()
                    self.page.tr( align_="CENTER", bgcolor_=self.strTableColourRows)
                    self.page.th(iWedge)
                    self.page.th(iRunNumber)
                    self.page.th("%.2f" % fRotationAxisStart)
                    self.page.th("%.2f" % fOscillationWidth)
                    self.page.th(iNumberOfImages)
                    self.page.th("%.2f" % fExposureTime)
                    self.page.th("%.2f" % fResolutionMax)
                    self.page.th("%.2f" % fTransmission)
                    self.page.th("%.2f" % fDistance)
                    self.page.tr.close()
                self.page.table.close()


    def diffractionPlan(self):
        # Do we have a diffracionPlan?
        xsDataDiffractionPlan = self.xsDataResultCharacterisation.getDataCollection().getDiffractionPlan()
        if xsDataDiffractionPlan is None:
            xsDataDiffractionPlan = XSDataDiffractionPlan()
        self.page.h2( "Diffraction Plan" )
        self.page.table( class_='diffractionPlan', border_="1", cellpadding_="0")
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourTitle2)
        self.page.th("Forced<br>space group")
        self.page.th("Anomalous<br>data")
        self.page.th("Aimed<br>multiplicity")
        self.page.th("Aimed<br>completeness")
        self.page.th("Aimed I/sigma<br>at highest res.")
        self.page.th("Aimed<br>resolution (&Aring;)")
        self.page.tr.close()
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourRows)
        # Forced space group               
        if xsDataDiffractionPlan.getForcedSpaceGroup() is None:
            strForcedSpaceGroup = "None"
        else:
            strForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
        self.page.th(strForcedSpaceGroup)
        # Anomalous data
        if xsDataDiffractionPlan.getAnomalousData() is None or xsDataDiffractionPlan.getAnomalousData().getValue() == False:
            strAnomalousData = "False"
        else:
            strAnomalousData = "True"
        self.page.th(strAnomalousData)
        # Aimed multiplicity
        if xsDataDiffractionPlan.getAimedMultiplicity() is None:
            strAimedMultiplicity = "Default<br>(optimized)"
        else:
            strAimedMultiplicity = "%.2f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue()
        self.page.th(strAimedMultiplicity)
        # Aimed completeness
        if xsDataDiffractionPlan.getAimedCompleteness() is None:
            strAimedCompleteness = "Default<br>(>= 0.99)"
        else:
            strAimedCompleteness = "%.2f" % xsDataDiffractionPlan.getAimedCompleteness().getValue()
        self.page.th(strAimedCompleteness)
        # Aimed aimedIOverSigmaAtHighestResolution
        if xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is None:
            strAimedIOverSigmaAtHighestResolution = "BEST Default"
        else:
            strAimedIOverSigmaAtHighestResolution = "%.2f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue()
        self.page.th(strAimedIOverSigmaAtHighestResolution)
        # Aimed resolution              
        if xsDataDiffractionPlan.getAimedResolution() is None:
            strAimedResolution = "Default<br>(highest possible)"
        else:
            strAimedResolution = "%0.2f" % xsDataDiffractionPlan.getAimedResolution().getValue()
        self.page.th(strAimedResolution)
        # Close the table
        self.page.tr.close()
        self.page.table.close()     


    def createLinkToBestLogFile(self):
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()
        

    def createThumbnailRowOfImages(self, _xsDataResultIndexing):
        # Thumbnail images of the predictions
        xsDataResultPrediction = _xsDataResultIndexing.getPredictionResult()
        listPaths = []
        self.page.div(align_="left")
        self.page.table( class_='imageRow' )
        self.page.tr( align_="CENTER" )
        listXSDataReferenceImage = _xsDataResultIndexing.getImage()
        for xsDataImagePrediction in xsDataResultPrediction.getPredictionImage():
            self.page.td()
            strPathToPredictionImage = xsDataImagePrediction.getPath().getValue()
            strFileName = os.path.basename(strPathToPredictionImage)
            strReferenceFileName = None
            for xsDataReferenceImage in listXSDataReferenceImage:
                if xsDataReferenceImage.getNumber().getValue() == xsDataImagePrediction.getNumber().getValue():
                    strReferenceFileName = os.path.basename(xsDataReferenceImage.getPath().getValue())
            if strReferenceFileName is None:
                strReferenceFileName = strFileName
            strLocalPath = os.path.join(self.getWorkingDirectory(), strFileName)
            shutil.copyfile(strPathToPredictionImage, strLocalPath)
            listPaths.append(strLocalPath)
            self.page.table( class_='image' )
            self.page.tr( align_="CENTER" )
            self.page.td()
            strPageReferenceImage = os.path.splitext(strFileName)[0]+".html"
            pageReferenceImage = markupv1_7.page()
            pageReferenceImage.init( title=strReferenceFileName, 
                   footer="Generated on %s" % time.asctime())
            pageReferenceImage.h1(strReferenceFileName)
            pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
            pageReferenceImage.img(src=strFileName, title=strReferenceFileName)
            pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
            EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(),strPageReferenceImage), str(pageReferenceImage))
            self.page.a( href=strPageReferenceImage)
            self.page.img( src=strFileName, width=128, height=128, title=strFileName )
            self.page.a.close()
            self.page.td.close()
            self.page.tr.close()
            self.page.tr( align_="CENTER" )
            self.page.td( strReferenceFileName, class_="caption")
            self.page.td.close()
            self.page.tr.close()
            self.page.table.close()
            self.page.td.close()
        self.page.table.close()
        self.page.div.close()


    def createTableWithIndexResults(self, _xsDataResultIndexing, _strForcedSpaceGroup):
        xsDataSolutionSelected = _xsDataResultIndexing.getSelectedSolution()
        xsDataCrystal = xsDataSolutionSelected.getCrystal()
        xsDataCell = xsDataCrystal.getCell()
        strSpaceGroup = xsDataCrystal.spaceGroup.name.value
        if _strForcedSpaceGroup is None:
            self.page.h3("Indexing summary: Selected spacegroup: %s" % strSpaceGroup)
        else:
            if strSpaceGroup.upper() == _strForcedSpaceGroup.upper():
                self.page.h3("Indexing summary: Forced spacegroup: %s" % strSpaceGroup)
            else:
                self.page.h3("Indexing summary: Selected spacegroup: %s, forced space group: %s" % strSpaceGroup, _strForcedSpaceGroup)
        self.page.table( class_='indexResults', border_="1", cellpadding_="0" )
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourTitle1 )
        self.page.th("Refined unit cell parameters (&Aring;/degrees)", colspan_="6")
        self.page.tr.close()
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourTitle2 )
        self.page.th("a (&Aring;)")
        self.page.th("b (&Aring;)")
        self.page.th("c (&Aring;)")
        self.page.th("alpha (&deg;)")
        self.page.th("beta (&deg;)")
        self.page.th("gamma (&deg;)")
        self.page.tr.close()
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourRows )
        self.page.td("%.3f" % xsDataCell.getLength_a().getValue())
        self.page.td("%.3f" % xsDataCell.getLength_b().getValue())
        self.page.td("%.3f" % xsDataCell.getLength_c().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_alpha().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_beta().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_gamma().getValue())
        self.page.td.close()
        self.page.tr.close()
        self.page.table.close()
        

        
    def imageQualityIndicatorResults(self):
        listXSDataResultImageQualityIndicators = self.xsDataResultCharacterisation.imageQualityIndicators
        self.page.h3("Image quality indicators")
        self.page.table( class_='imageQualityIndicatorResults', border_="1", cellpadding_="0")
        self.page.tr( align_="CENTER", bgcolor_=self.strTableColourTitle2  )
        self.page.th("File")
        self.page.th("Tot integr signal")
        self.page.th("Spot total")
        self.page.th("In-Res Total")
        self.page.th("Good Bragg")
        self.page.th("Ice Rings")
        self.page.th("Meth 1 Res")
        self.page.th("Meth 2 Res")
        self.page.th("Max unit cell")
        self.page.tr.close()
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            self.page.tr( align_="CENTER", bgcolor_=self.strTableColourRows )
            self.page.td("%s" % os.path.basename(xsDataResultImageQualityIndicators.image.path.value))
            if xsDataResultImageQualityIndicators.totalIntegratedSignal:
                self.page.td("%.0f" % xsDataResultImageQualityIndicators.totalIntegratedSignal.value)
            else:
                self.page.td("NA")
            self.page.td("%d" % xsDataResultImageQualityIndicators.spotTotal.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.inResTotal.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.goodBraggCandidates.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.iceRings.value)
            self.page.td("%.2f" % xsDataResultImageQualityIndicators.method1Res.value)
            if xsDataResultImageQualityIndicators.method2Res:
                self.page.td("%.2f" % xsDataResultImageQualityIndicators.method2Res.value)
            else:
                self.page.td("NA")
            if xsDataResultImageQualityIndicators.maxUnitCell:
                self.page.td("%.1f" % xsDataResultImageQualityIndicators.maxUnitCell.value)
            else:
                self.page.td("NA")
            self.page.td.close()
            self.page.tr.close()
        self.page.table.close()
        


    def findEDNALogFile(self):
        """Trying to locate the EDNA plugin launcher log file..."""
        strBaseDir = self.getWorkingDirectory()
        strPathToLogFile = None
        for iLevels in range(4):
            strBaseDir = os.path.dirname(strBaseDir)
            self.DEBUG("Searching in strBaseDir: " + strBaseDir)
            # Now search for a ED*.log file...
            for strFileName in os.listdir(strBaseDir):
                if strFileName.startswith("ED") and strFileName.endswith(".log"):
                    # Check that the corresponding direcory exists...
                    strDirectoryName = strFileName[:-4]
                    if os.path.isdir(os.path.join(strBaseDir, strDirectoryName)):
                        # Final check - is the directory name in the working dir
                        if self.getWorkingDirectory().find(strDirectoryName) != -1:
                            # Ok, we found it!
                            strPathToLogFile = os.path.join(strBaseDir, strFileName)
        return strPathToLogFile


    def graphs(self):
        self.page.table( class_='bestGraphs', border_="0", cellpadding_="0")
        if self.getDataInput().characterisationResult.strategyResult is None:
            return
        if self.getDataInput().characterisationResult.strategyResult.bestGraphFile == []:
            return
        listXSDataFile = self.getDataInput().characterisationResult.strategyResult.bestGraphFile
        if listXSDataFile != []:
            self.page.tr( align_="CENTER" )
            iIndex = 1
            # If -damPar is used only three plots are available:
            if len(listXSDataFile) > 4:
                listPlotsToDisplay = [0, 1, 3, 6]
            else:
                listPlotsToDisplay = range(len(listXSDataFile))
            for iIndexPlot in listPlotsToDisplay:
                xsDataFile = listXSDataFile[iIndexPlot]
                strFileName = os.path.basename(xsDataFile.path.value)
                #print strFileName
                shutil.copy(xsDataFile.path.value, os.path.join(self.getWorkingDirectory(), strFileName))
                self.page.td()
                strPageGraphFileName = os.path.splitext(strFileName)[0]+".html"
                strPageGraphPath = os.path.join(self.getWorkingDirectory(), strPageGraphFileName)
                pageGraph = markupv1_7.page()
                pageGraph.init( title=strFileName, 
                       footer="Generated on %s" % time.asctime())
                pageGraph.h1(strFileName)
                pageGraph.a("Back to previous page", href_=self.strHtmlFileName)
                pageGraph.br()
                pageGraph.img(src=strFileName, title=strFileName)
                pageGraph.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(strPageGraphPath, str(pageGraph))
                self.page.a( href=strPageGraphFileName)
                self.page.img( src=strFileName, width=175, height=175, title=strFileName )
                self.page.a.close()
                self.page.td.close()
                iIndex += 1
                if iIndex > 4:
                    iIndex = 1
                    self.page.tr.close()
                    self.page.tr( align_="CENTER" )
            self.page.tr.close()
            self.page.table.close()
            
