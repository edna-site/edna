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

EDFactoryPluginStatic.loadModule("markupv1_7")
import markupv1_7

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataSimpleHTMLPagev1_0 import XSDataInputSimpleHTMLPage
from XSDataSimpleHTMLPagev1_0 import XSDataResultSimpleHTMLPage

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


    def preProcess(self, _edPlugin=None):
        EDPluginExec.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.preProcess...")
        self.xsDataResultCharacterisation = self.getDataInput().getCharacterisationResult()
        self.strPath = os.path.join(self.getWorkingDirectory(), "simple.html")
        # Create the simple characterisation result page
        self.page = markupv1_7.page( )
        self.page.init( title="Characterisation Results", 
                   footer="Generated on %s" % time.asctime())
        self.page.div( align_="CENTER")
        if self.xsDataResultCharacterisation is not None:
            self.page.h1( "Characterisation Results" )
        else:
            self.page.h1( "No Characterisation Results!" )
        self.page.div.close()
        self.page.br()


    def process(self, _edPlugin=None):
        EDPluginExec.process(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.process...")
        if self.xsDataResultCharacterisation is not None:
            self.page.hr()
            self.strategyResults()
            self.page.hr()
            self.indexingResults()
            self.page.hr()
            self.imageQualityIndicatorResults()
        self.page.hr()
        self.addLinkToEDNALogFile()
        self.page.hr()
        


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


    def indexingResults(self):
        # Was the indexing successful?
        xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
        strForcedSpaceGroup = None
        # Check for forced space group!
        if self.xsDataResultCharacterisation.dataCollection.diffractionPlan is not None:
            if self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup is not None:
                strForcedSpaceGroup = self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup.value
        if xsDataResultIndexing:
            self.page.h2( "Indexing summary" )
            # Table with indexing results
            self.createTableWithIndexResults(xsDataResultIndexing, strForcedSpaceGroup)
            # Thumbnail images
            self.createThumbnailRowOfImages(xsDataResultIndexing)
            
        else:
            self.page.h2( "Indexing failed" )

    
    def strategyResults(self):
        # Was the strategy successful?
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()
        if xsDataResultStrategy:
            listXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            iNoSubWedges = len(listXSDataCollectionPlan)
            if iNoSubWedges != 1:
                self.page.h2( "Multi-wedge collection plan strategy")
            else:
                self.page.h2( "Collection plan strategy" )
            # Check if ranking resolution is higher than the suggested strategy resolution(s)
            bHigherResolutionDetected = False
            fRankingResolution = None
            fResolutionMax = None
            for xsDataCollectionPlan in listXSDataCollectionPlan:
                xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                if xsDataSummaryStrategy.getRankingResolution():
                    fResolution = xsDataSummaryStrategy.getResolution().getValue()
                    if fResolutionMax is None:
                        fResolutionMax = fResolution
                    elif (fResolution < fResolutionMax) and (abs(fResolution-fResolutionMax) > 0.1):
                        fResolutionMax = fResolution                        
                    fRankingResolution = xsDataSummaryStrategy.getRankingResolution().getValue()
            
            if fRankingResolution != None and fResolutionMax != None:
                if fRankingResolution < fResolutionMax:
                    if not bHigherResolutionDetected:
                        self.page.i()
                        self.page.h3("Best has detected that the sample can diffract to %.2f &Aring;!" % fRankingResolution)
                        self.page.br()
                        self.page.strong("The current strategy is calculated to %.2f &Aring;." % fResolutionMax)
                        self.page.br()
                        self.page.strong("In order to calculate a strategy to %.2f &Aring; move the detector to %.2f &Aring; and re-launch the EDNA characterisation." % (fRankingResolution,fRankingResolution))
                        self.page.i.close()
                    bHigherResolutionDetected = True
                
                
            for xsDataCollectionPlan in listXSDataCollectionPlan:
                xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                fResolutionMax = xsDataSummaryStrategy.getResolution().getValue()
                strResolutionReasoning = ""
                if xsDataSummaryStrategy.getResolutionReasoning():
                    strResolutionReasoning = xsDataSummaryStrategy.getResolutionReasoning().getValue()
                self.page.table( class_='indexResults', border_="1", cellpadding_="1", style_="font-size:12px" )
                self.page.tr( align_="CENTER" )
                self.page.th(strResolutionReasoning, colspan_="8", style_="font-size:20px")
                self.page.tr.close()
                self.page.tr( align_="CENTER" )
                self.page.th("Subwedge")
                self.page.th("Rotation axis start(&deg;)")
                self.page.th("Rotation width(&deg;)")
                self.page.th("Number of images")
                self.page.th("Exposure time (s)")
                self.page.th("Maximum resolution (&Aring;)")
                self.page.th("Relative transmission (%)")
                self.page.th("Distance (mm)")
                self.page.tr.close()
                xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                for xsDataSubWegde in xsDataCollectionStrategy.getSubWedge():
                    xsDataExperimentalCondition = xsDataSubWegde.getExperimentalCondition()
                    iRunNumber = xsDataSubWegde.getSubWedgeNumber().getValue()
                    fRotationAxisStart = xsDataExperimentalCondition.getGoniostat().getRotationAxisStart().getValue()
                    fRotationAxisEnd = xsDataExperimentalCondition.getGoniostat().getRotationAxisEnd().getValue()
                    fOscillationWidth = xsDataExperimentalCondition.getGoniostat().getOscillationWidth().getValue()
                    iNumberOfImages = int((fRotationAxisEnd-fRotationAxisStart)/fOscillationWidth)
                    fExposureTime = xsDataExperimentalCondition.getBeam().getExposureTime().getValue()
                    fTransmission = xsDataExperimentalCondition.getBeam().getTransmission().getValue()
                    fDistance = xsDataExperimentalCondition.getDetector().getDistance().getValue()
                    self.page.tr( align_="CENTER" )
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
            # Add link to BEST log file:
            if xsDataResultStrategy.getBestLogFile():
                strPathToBestLogFile = xsDataResultStrategy.getBestLogFile().getPath().getValue()
                strPageBestLog = os.path.join(self.getWorkingDirectory(), "best_log.html")
                pageBestLog = markupv1_7.page()
                pageBestLog.h1("Best Log")
                pageBestLog.a("Back to previous page", href_=self.strPath)
                pageBestLog.pre(cgi.escape(EDUtilsFile.readFile(strPathToBestLogFile)))
                pageBestLog.a("Back to previous page", href_=self.strPath)
                EDUtilsFile.writeFile(strPageBestLog, str(pageBestLog))
                self.page.h3()
                self.page.a("Best log file", href=strPageBestLog)
                self.page.h3.close()
                    
        else:
            self.page.h2( "Strategy calculation failed" )



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
            strPageReferenceImage = os.path.join(self.getWorkingDirectory(), os.path.splitext(strFileName)[0]+".html")
            pageReferenceImage = markupv1_7.page()
            pageReferenceImage.init( title=strReferenceFileName, 
                   footer="Generated on %s" % time.asctime())
            pageReferenceImage.h1(strReferenceFileName)
            pageReferenceImage.a("Back to previous page", href_=self.strPath)
            pageReferenceImage.img(src=strLocalPath, title=strReferenceFileName)
            pageReferenceImage.a("Back to previous page", href_=self.strPath)
            EDUtilsFile.writeFile(strPageReferenceImage, str(pageReferenceImage))
            self.page.a( href=strPageReferenceImage)
            self.page.img( src=strLocalPath,width=256, height=256, title=strFileName )
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
            self.page.p("<H3>Selected spacegroup: %s</H3>" % strSpaceGroup)
        else:
            if strSpaceGroup.upper() == _strForcedSpaceGroup.upper():
                self.page.p("<H3>Forced spacegroup: %s</H3>" % strSpaceGroup)
            else:
                self.page.p("<H3>Selected spacegroup: %s, forced space group: %s</H3>" % strSpaceGroup, _strForcedSpaceGroup)
        self.page.table( class_='indexResults', border_="1", cellpadding_="1", style_="font-size:12px" )
        self.page.tr( align_="CENTER" )
        self.page.th("Refined unit cell parameters (&Aring;/degrees)", colspan_="6", style_="font-size:15px")
        self.page.tr.close()
        self.page.tr( align_="CENTER" )
        self.page.th("a")
        self.page.th("b")
        self.page.th("c")
        self.page.th("alpha")
        self.page.th("beta")
        self.page.th("gamma")
        self.page.tr.close()
        self.page.tr( align_="CENTER" )
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
        self.page.p("<H3>Image quality indicators</H3>")
        self.page.table( class_='imageQualityIndicatorResults', border_="1", cellpadding_="1", style_="font-size:12px")
        self.page.tr( align_="CENTER" )
        self.page.th("File")
        self.page.th("Total integrated signal")
        self.page.th("Spot total")
        self.page.th("In-Resolution Total")
        self.page.th("Good Bragg Candidates")
        self.page.th("Ice Rings")
        self.page.th("Method 1 Resolution")
        self.page.th("Method 2 Resolution")
        self.page.th("Max unit cell")
        self.page.tr.close()
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            self.page.tr( align_="CENTER" )
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


    def addLinkToEDNALogFile(self):
        strPathToLogFile = self.findEDNALogFile()
        if strPathToLogFile is not None:
            strPageEDNALog = os.path.join(self.getWorkingDirectory(), "edna_log.html")
            pageEDNALog = markupv1_7.page(mode='loose_html')
            pageEDNALog.h1("EDNA Log")
            pageEDNALog.a("Back to previous page", href_=self.strPath)
            pageEDNALog.font(_size="-1")
            pageEDNALog.pre(cgi.escape(EDUtilsFile.readFile(strPathToLogFile)), style_="font-size:8px")
            pageEDNALog.font.close()
            pageEDNALog.a("Back to previous page", href_=self.strPath)
            EDUtilsFile.writeFile(strPageEDNALog, str(pageEDNALog))
            self.page.h3()
            self.page.a("EDNA log file", href=strPageEDNALog)
            self.page.h3.close()

