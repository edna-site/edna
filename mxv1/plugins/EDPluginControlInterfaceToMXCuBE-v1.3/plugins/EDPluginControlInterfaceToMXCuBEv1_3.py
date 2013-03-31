#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import shutil
import smtplib
import time

from EDMessage import EDMessage
from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsImage import EDUtilsImage
from EDConfiguration import EDConfiguration
from EDUtilsPath import EDUtilsPath

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFlux
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataKeyValuePair

from XSDataMXv1 import XSDataInputControlISPyB
from XSDataMXv1 import XSDataResultCharacterisation

from XSDataMXCuBEv1_3 import XSDataInputMXCuBE
from XSDataMXCuBEv1_3 import XSDataResultMXCuBE

EDFactoryPluginStatic.loadModule("XSDataSimpleHTMLPagev1_0")
from XSDataSimpleHTMLPagev1_0 import XSDataInputSimpleHTMLPage

EDFactoryPluginStatic.loadModule("XSDataInterfacev1_2")
from XSDataInterfacev1_2 import XSDataInputInterface

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection

class EDPluginControlInterfaceToMXCuBEv1_3(EDPluginControl):
    """
    This is the plugin interface to launch the MXv1 characterisation from an MXCuBE gui.
    It is for the moment a wrapper for the EDPluginControlCCP4iv1_1 plugin, which also
    runs the ISPyB control plugin if a data collection id is available.
    """

    EDNA_CONTACT_EMAIL = "contactEmail"
    EDNA_EMAIL_SENDER = "emailSender"


    def __init__ (self):
        """
        Initialisation of EDPluginControlInterfaceToMXCuBEv1_3:
        - Input data type class : XSDataInputMXCuBE
        - Name of default characterisation plugin : EDPluginControlCharacterisationv1_1
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMXCuBE)
        self.strPluginControlInterface = "EDPluginControlInterfacev1_2"
        self.edPluginControlInterface = None
        self.strPluginControlISPyB = "EDPluginControlISPyBv1_4"
        self.edPluginControlISPyB = None
        self.xsDataResultMXCuBE = None
        self.xsDataIntegerDataCollectionId = None
        self.strPluginExecOutputHTMLName = "EDPluginExecOutputHTMLv1_0"
        self.edPluginExecOutputHTML = None
        self.strPluginExecSimpleHTMLName = "EDPluginExecSimpleHTMLPagev1_0"
        self.edPluginExecSimpleHTML = None
        self.strPluginISPyBRetrieveDataCollection = "EDPluginISPyBRetrieveDataCollectionv1_4"
        self.edPluginISPyBRetrieveDataCollection= None
        self.strEDNAContactEmail = None
        self.strEDNAEmailSender = "edna-support@esrf.fr"
        self.tStart = None
        self.tStop = None
        self.fFluxThreshold = 1e3


    def checkParameters(self):
        """
        Checks the mandatory input parameters :
        - dataSet
        - outputFileDirectory
        """
        self.verboseDebug("EDPluginControlInterfaceToMXCuBEv1_3.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataSet(), "dataSet")


    def configure(self):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.configure")
        self.strEDNAEmailSender = self.config.get(self.EDNA_EMAIL_SENDER, self.strEDNAEmailSender)
        self.strEDNAContactEmail = self.config.get(self.EDNA_CONTACT_EMAIL, self.strEDNAContactEmail)



    def preProcess(self, _edPlugin=None):
        """
        This method prepares the input for the CCP4i plugin and loads it.
        """
        EDPluginControl.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.preProcess...")

        self.tStart = time.time()

        #self.edPluginExecOutputHTML = self.loadPlugin(self.strPluginExecOutputHTMLName, "OutputHTML")
        self.edPluginExecSimpleHTML = self.loadPlugin(self.strPluginExecSimpleHTMLName, "SimpleHTML")
        self.edPluginISPyBRetrieveDataCollection = self.loadPlugin(self.strPluginISPyBRetrieveDataCollection, \
                                                                   "ISPyBRetrieveDataCollection")
        self.xsDataResultMXCuBE = XSDataResultMXCuBE()



    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.process...")

        xsDataInputMXCuBE = self.getDataInput()
        xsDataInputInterface = XSDataInputInterface()
        self.edPluginControlInterface = self.loadPlugin(self.strPluginControlInterface)
        xsDataFirstImage = None
        for xsDataSetMXCuBE in xsDataInputMXCuBE.getDataSet():
            for xsDataFile in xsDataSetMXCuBE.getImageFile():
                xsDataInputInterface.addImagePath(xsDataFile)
                if xsDataFirstImage is None:
                    xsDataFirstImage = xsDataFile
        
        xsDataExperimentalCondition = self.getFluxFromISPyB(xsDataFirstImage, \
                                                            xsDataInputMXCuBE.getExperimentalCondition())
        
        xsDataInputInterface.setExperimentalCondition(xsDataExperimentalCondition)
        xsDataInputInterface.setDiffractionPlan(xsDataInputMXCuBE.getDiffractionPlan())
        xsDataInputInterface.setSample(xsDataInputMXCuBE.getSample())
        xsDataInputInterface.setDataCollectionId(xsDataInputMXCuBE.getDataCollectionId())
        self.edPluginControlInterface.setDataInput(xsDataInputInterface)

        if self.edPluginControlInterface is not None:
            self.connectProcess(self.edPluginControlInterface.executeSynchronous)
            self.edPluginControlInterface.connectSUCCESS(self.doSuccessActionInterface)
            self.edPluginControlInterface.connectFAILURE(self.doFailureActionInterface)


    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.postProcess...")
        self.setDataOutput(self.xsDataResultMXCuBE)


    def doSuccessActionInterface(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doSuccessActionInterface...")
        self.retrieveSuccessMessages(self.edPluginControlInterface, "EDPluginControlInterfaceToMXCuBEv1_3.doSuccessActionInterface")
        # Send success email message (MXSUP-183):
        self.tStop = time.time()
        strSubject = "%s : SUCCESS! (%.1f s)" % (EDUtilsPath.getEdnaSite(), self.tStop-self.tStart)
        strMessage = "Characterisation success!"
        self.storeResultsInISPyB(strSubject, strMessage)
        
    def doFailureActionInterface(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doFailureActionInterface...")
        # Send failure email message (MXSUP-183):
        strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        strMessage = "Characterisation FAILURE!"
        self.storeResultsInISPyB(strSubject, strMessage)
        #self.setFailure()
#        xsDataResultCharacterisation = None
#        if self.edPluginControlInterface.hasDataOutput("characterisation"):
#            xsDataResultCharacterisation = self.edPluginControlInterface.getDataOutput("characterisation")[0]
#        # Execute plugin which creates a simple HTML page
#        self.executeSimpleHTML(xsDataResultCharacterisation)            
#        xsDataResultCharacterisation = self.edPluginControlInterface.dataOutput.resultCharacterisation
#        if xsDataResultCharacterisation is not None:
#            self.xsDataResultMXCuBE.characterisationResult = xsDataResultCharacterisation
#            if xsDataResultCharacterisation.getStatusMessage():
#                strMessage += "\n\n"
#                strMessage += xsDataResultCharacterisation.getStatusMessage().getValue()
#            if xsDataResultCharacterisation.getShortSummary():
#                strMessage += "\n\n"
#                strMessage += xsDataResultCharacterisation.getShortSummary().getValue()
#        self.sendEmail(strSubject, strMessage)
        
        
    def storeResultsInISPyB(self, _strSubject, _strMessage):
        strSubject = _strSubject
        strMessage = _strMessage
        xsDataResultCharacterisation = self.edPluginControlInterface.getDataOutput().getResultCharacterisation()
        self.xsDataResultMXCuBE.setCharacterisationResult(xsDataResultCharacterisation)
        xsDataResultControlISPyB = self.edPluginControlInterface.getDataOutput().getResultControlISPyB()
        if xsDataResultControlISPyB != None:
            self.xsDataResultMXCuBE.setScreeningId(xsDataResultControlISPyB.getScreeningId())
        if xsDataResultCharacterisation != None:
            self.xsDataResultMXCuBE.characterisationResult = xsDataResultCharacterisation
            strPathCharacterisationResult = os.path.join(self.getWorkingDirectory(), "CharacterisationResult.xml")
            xsDataResultCharacterisation.exportToFile(strPathCharacterisationResult)
            self.xsDataResultMXCuBE.setListOfOutputFiles(XSDataString(strPathCharacterisationResult))
            # For the moment, create "DNA" style output directory
            strPathToDNAFileDirectory = self.createDNAFileDirectoryPath(xsDataResultCharacterisation)
            xsDataDictionaryLogFile = None
            if (self.createDNAFileDirectory(strPathToDNAFileDirectory)):
                xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataResultCharacterisation, strPathToDNAFileDirectory)
            strPyArchPathToDNAFileDirectory = self.createPyArchDNAFilePath(strPathToDNAFileDirectory)
            if (self.createDNAFileDirectory(strPyArchPathToDNAFileDirectory)):
                xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataResultCharacterisation, strPyArchPathToDNAFileDirectory)
            self.xsDataResultMXCuBE.setOutputFileDictionary(xsDataDictionaryLogFile)
            if xsDataResultCharacterisation.getStatusMessage():
                strMessage += "\n\n"
                strMessage += xsDataResultCharacterisation.getStatusMessage().getValue()
            if xsDataResultCharacterisation.getShortSummary():
                strMessage += "\n\n"
                strMessage += xsDataResultCharacterisation.getShortSummary().getValue()
            self.sendEmail(strSubject, strMessage)
            # Fix for bug EDNA-55 : If burning strategy EDNA2html shouldn't be run
            bRunExecOutputHTML = False
            xsDataInputMXCuBE = self.getDataInput()
            xsDataDiffractionPlan = xsDataInputMXCuBE.getDiffractionPlan()
            if xsDataDiffractionPlan.getStrategyOption() is not None:
                strStrategyOption = xsDataDiffractionPlan.getStrategyOption().getValue()
                if strStrategyOption.find("-DamPar") != -1:
                    bRunExecOutputHTML = False
            if (self.edPluginExecOutputHTML is not None) and bRunExecOutputHTML:
                self.edPluginExecOutputHTML.setDataInput(XSDataFile(XSDataString(strPathToDNAFileDirectory)), "dnaFileDirectory")
                self.edPluginExecOutputHTML.execute()
            # Fix for bug MXSUP-251: Put the BEST .par file in the EDNA characterisation root directory
            xsDataIntegrationResult = xsDataResultCharacterisation.getIntegrationResult()
            if xsDataIntegrationResult:
                listXSDataIntegrationSubWedgeResult = xsDataIntegrationResult.getIntegrationSubWedgeResult()
                if listXSDataIntegrationSubWedgeResult:
                    if listXSDataIntegrationSubWedgeResult != []:
                        strBestfilePar = listXSDataIntegrationSubWedgeResult[0].getBestfilePar().getValue()
                        # Put the file one directory above the mxCuBE v1.3 plugin working directory:
                        strDir = os.path.dirname(self.getWorkingDirectory())
                        strPath = os.path.join(strDir, "bestfile.par")
                        EDUtilsFile.writeFile(strPath, strBestfilePar)
            # Execute plugin which creates a simple HTML page
            self.executeSimpleHTML(xsDataResultCharacterisation)    
                    





    def doSuccessActionISPyB(self, _edPlugin):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_3.doSuccessActionISPyB")


    def doFailureActionISPyB(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doFailureActionISpyB...")
        self.retrieveFailureMessages(self.edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_3.doFailureActionISpyB")
        # Send failure email message (MXSUP-183):
        strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        strMessage = "ISPyB FAILURE!"
        self.sendEmail(strSubject, strMessage)


    def createDNAFileDirectoryPath(self, _xsDataResultCharacterisation):
        """
        This method creates a "DNA" style directory path, i.e. in the same directory were the 
        images are located a new directory is created with the following convention:
        
          dnafiles_prefix_runNumber
        
        The path to this directory is returned if the directory was successfully created.
        """
        # First extract all reference image directory paths and names
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        listImageDirectoryPath = []
        listImagePrefix = []
        for xsDataSubWedge in xsDataCollection.getSubWedge():
            for xsDataImage in xsDataSubWedge.getImage():
                strImagePath = xsDataImage.getPath().getValue()
                listImageDirectoryPath.append(os.path.dirname(strImagePath))
                listImagePrefix.append(EDUtilsImage.getPrefix(strImagePath))
        # TODO: Check that all paths and prefixes are the same
        strImageDirectory = listImageDirectoryPath[0]
        strPrefix = listImagePrefix[0]
        # Remove any "ref-" or "postref-" from the prefix in order to make it fully
        # compatitble with DNA standards:
        if (strPrefix is not None):
            if (strPrefix.startswith("ref-")):
                strPrefix = strPrefix[4:]
            elif (strPrefix.startswith("postref-")):
                strPrefix = strPrefix[8:]
        strDNAFileDirectoryPath = os.path.join(strImageDirectory, "%s_dnafiles" % strPrefix)
        return strDNAFileDirectoryPath



    def createPyArchDNAFilePath(self, _strDNAFileDirectoryPath):
        """
        This method translates from a "visitor" path to a "pyarch" path:
        /data/visitor/mx415/id14eh1/20100209 -> /data/pyarch/id14eh1/mx415/20100209
        """
        strPyarchDNAFilePath = None
        listOfDirectories = _strDNAFileDirectoryPath.split(os.sep)
        listBeamlines = ["bm14", "id14eh1", "id14eh2", "id14eh3", "id14eh4", "id23eh1", "id23eh2", "id29"]
        # Check that we have at least four levels of directories:
        if (len(listOfDirectories) > 4):
            strDataDirectory = listOfDirectories[ 1 ]
            strSecondDirectory = listOfDirectories[ 2 ]
            strProposal = None
            strBeamline = None
            if ((strDataDirectory == "data") and (strSecondDirectory == "visitor")):
                strProposal = listOfDirectories[ 3 ]
                strBeamline = listOfDirectories[ 4 ]
            elif ((strDataDirectory == "data") and (strSecondDirectory in listBeamlines)):
                strBeamline = strSecondDirectory
                strProposal = listOfDirectories[ 4 ]
            if (strProposal != None) and (strBeamline != None):
                strPyarchDNAFilePath = os.path.join(os.sep, "data")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, "pyarch")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strBeamline)
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strProposal)
                for strDirectory in listOfDirectories[ 5: ]:
                    strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strDirectory)
        if (strPyarchDNAFilePath is None):
            self.WARNING("EDPluginControlInterfaceToMXCuBEv1_3.createPyArchDNAFilePath: path not converted for pyarch: %s " % _strDNAFileDirectoryPath)
        return strPyarchDNAFilePath



    def createDNAFileDirectory(self, _strDNAFileDirectoryPath):
        """
        Create a "DNA-files" directory - if possible.
        """
        bSuccess = False
        if (_strDNAFileDirectoryPath is not None):
            if (os.path.exists(_strDNAFileDirectoryPath)):
                self.warning("Removing existing DNA files directory: %s" % _strDNAFileDirectoryPath)
                if (os.access(_strDNAFileDirectoryPath, os.W_OK)):
                    shutil.rmtree(_strDNAFileDirectoryPath)
                else:
                    self.warning("Cannot remove existing DNA files directory!")
            if (_strDNAFileDirectoryPath is not None):
                # Check if directory one level up is writeable
                strDNAFileBaseDirectory = os.path.split(_strDNAFileDirectoryPath)[0]
                if (os.access(strDNAFileBaseDirectory, os.W_OK)):
                    self.DEBUG("Creating DNA files directory: %s" % _strDNAFileDirectoryPath)
                    os.mkdir(_strDNAFileDirectoryPath)
                    bSuccess = True
                else:
                    self.warning("Cannot create DNA files directory: %s" % _strDNAFileDirectoryPath)
        return bSuccess



    def splitHeadDirectory(self, _strPath):
        """
        This method works like os.path.split except that it splits the head directory
        from the rest of the path. Example:
        "/" -> [ None, None]
        "/data" -> ["data", None]
        "/data/visitor" -> ["data", "visitor"]
        "/data/visitor/mx415/id14eh2/20100212" -> ["data", "visitor/mx415/id14eh2/20100212"]
        """
        listOfDirectories = _strPath.split(os.sep)
        strTail = None
        strHead = None
        if (len(listOfDirectories) > 1):
            strHead = listOfDirectories[1]
            if (strHead == ""):
                strHead = None
            if (len(listOfDirectories) > 1):
                for strEntry in listOfDirectories[2:]:
                    if (strTail is None):
                        strTail = strEntry
                    else:
                        strTail = os.path.join(strTail, strEntry)
        return [ strHead, strTail ]


    def createOutputFileDictionary(self, _xsDataResultCharacterisation, _strPathToLogFileDirectory=None):
        """
        This method creates an XSDataDictionary containing the name and locations of the 
        characterisation output files.
        """
        xsDataDictionaryLogFile = XSDataDictionary()
        # Start with the prediction images
        xsDataIndexingResult = _xsDataResultCharacterisation.getIndexingResult()
        if xsDataIndexingResult is not None:
            xsDataGeneratePredictionResult = xsDataIndexingResult.getPredictionResult()
            if xsDataGeneratePredictionResult is not None:
                listXSDataImagePrediction = xsDataGeneratePredictionResult.getPredictionImage()
                for xsDataImagePrediction in listXSDataImagePrediction:
                    xsDataKeyValuePair = XSDataKeyValuePair()
                    iPredictionImageNumber = xsDataImagePrediction.getNumber().getValue()
                    xsDataStringKey = XSDataString("predictionImage_%d" % iPredictionImageNumber)
                    xsDataStringValue = None
                    strPredictionImagePath = xsDataImagePrediction.getPath().getValue()
                    if (_strPathToLogFileDirectory is not None):
                        strPredictionImageFileName = EDUtilsFile.getBaseName(strPredictionImagePath)
                        strNewPredictionImagePath = os.path.join(_strPathToLogFileDirectory, strPredictionImageFileName)
                        EDUtilsFile.copyFile(strPredictionImagePath, strNewPredictionImagePath)
                        xsDataStringValue = XSDataString(strNewPredictionImagePath)
                    else:
                        xsDataStringValue = XSDataString(strPredictionImageFileName)
                    xsDataKeyValuePair.setKey(xsDataStringKey)
                    xsDataKeyValuePair.setValue(xsDataStringValue)
                    xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)
        # Best log file
        strPathToBESTLogFile = None
        strPathToExecutiveSummary = None
        if _xsDataResultCharacterisation.getStrategyResult() is not None:
            if _xsDataResultCharacterisation.getStrategyResult().getBestLogFile() != None:
                strPathToBESTLogFile = _xsDataResultCharacterisation.getStrategyResult().getBestLogFile().getPath().getValue()
            if strPathToBESTLogFile is not None:
                xsDataStringKey = XSDataString("logFileBest")
                xsDataStringValue = None
                if (_strPathToLogFileDirectory is not None):
                    strNewBestLogPath = os.path.join(_strPathToLogFileDirectory, "best.log")
                    EDUtilsFile.copyFile(strPathToBESTLogFile, strNewBestLogPath)
                    xsDataStringValue = XSDataString(strNewBestLogPath)
                else:
                    xsDataStringValue = XSDataString(strPathToBESTLogFile)
                xsDataKeyValuePair = XSDataKeyValuePair()
                xsDataKeyValuePair.setKey(xsDataStringKey)
                xsDataKeyValuePair.setValue(xsDataStringValue)
                xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)
            if (strPathToExecutiveSummary is not None):
                xsDataStringKey = XSDataString("executiveSummary")
                xsDataStringValue = None
                if (_strPathToLogFileDirectory is not None):
                    strExecutiveSummaryFileName = EDUtilsFile.getBaseName(strPathToExecutiveSummary)
                    strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, strExecutiveSummaryFileName)
                    EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)
                    xsDataStringValue = XSDataString(strNewExecutiveSummaryPath)
                    # Copy also the executive summary file to "dna_log.txt"...
                    strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, "dna_log.txt")
                    EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)
                else:
                    xsDataStringValue = XSDataString(strPathToExecutiveSummary)
                xsDataKeyValuePair = XSDataKeyValuePair()
                xsDataKeyValuePair.setKey(xsDataStringKey)
                xsDataKeyValuePair.setValue(xsDataStringValue)
                xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)

        return xsDataDictionaryLogFile





    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        self.DEBUG("EDPluginControlInterfacev1_3.doFailureActionCharacterisation")
        self.setFailure()
        # Send failure email message (MXSUP-183):
        strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        strMessage = "Characterisation FAILURE!"
        self.sendEmail(strSubject, strMessage)


    def getFluxFromISPyB(self, _xsDataFirstImage, _xsDataExperimentalCondition):
        """
        This method retrieves the flux from ISPyB
        """
        xsDataExperimentalCondition = None
        if (_xsDataExperimentalCondition is not None):
            xsDataExperimentalCondition = _xsDataExperimentalCondition.copy()
            bFoundValidFlux = False
            xsDataBeam = xsDataExperimentalCondition.getBeam()
            if xsDataBeam is None:
                xsDataBeam = XSDataBeam()    
                xsDataExperimentalCondition.setBeam(xsDataBeam)
            xsDataBeamFlux = xsDataBeam.getFlux()
            if xsDataBeamFlux is not None:
                fFluxMXCuBE = xsDataBeamFlux.getValue()
                self.screen("MXCuBE reports flux to be: %g photons/sec" % fFluxMXCuBE)
                if fFluxMXCuBE > self.fFluxThreshold:
                    bFoundValidFlux = True
                else:
                    self.screen("MXCuBE flux invalid! Trying to obtain flux from ISPyB.")
            if not bFoundValidFlux:
                # Here we try to retrieve the flux from ISPyB
                xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
                xsDataInputRetrieveDataCollection.setImage(XSDataImage(_xsDataFirstImage.getPath()))
                self.edPluginISPyBRetrieveDataCollection.setDataInput(xsDataInputRetrieveDataCollection)
                self.edPluginISPyBRetrieveDataCollection.executeSynchronous()
                xsDataResultRetrieveDataCollection = self.edPluginISPyBRetrieveDataCollection.getDataOutput()
                if xsDataResultRetrieveDataCollection is not None:
                    xsDataISPyBDataCollection = xsDataResultRetrieveDataCollection.getDataCollection()
                    if xsDataISPyBDataCollection is not None:
                        fFlux = xsDataISPyBDataCollection.getFlux()
                        if fFlux is not None:
                            self.screen("ISPyB reports flux to be: %g photons/sec" % fFlux)
                            xsDataExperimentalCondition.getBeam().setFlux(XSDataFlux(fFlux))
                            bFoundValidFlux = True
                if not bFoundValidFlux:
                    self.screen("No valid flux could be retrieved from ISPyB!")
        return xsDataExperimentalCondition
                            
                            




    def updateDataInputCharacterisation(self, _xsDataInputCharacterisation):
        """
        This method updates the xsDataInputCharacterisation object given as argument with the following
        parameters (if available) goven as input:
        - Diffraction plan
        - Beam size
        - Beam flux
        - Min exposure time per image
        - Max oscillation speed
        - Min oscillation width
        - Sample information
        """
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.createDataInputCharacterisationFromDataSets")
        xsDataCollection = _xsDataInputCharacterisation.getDataCollection()
        if (_xsDataInputCharacterisation is not None):
            xsDataInputCCP4i = self.getDataInput()
            # Update with diffraction plan
            xsDiffactionPlan = xsDataInputCCP4i.getDiffractionPlan()
            if(xsDiffactionPlan is not None):
                xsDataCollection.setDiffractionPlan(xsDiffactionPlan)
            # Update the data collection subwedges with additional experimental conditions
            for xsDataSubWedge in xsDataCollection.getSubWedge():
                xsDataExperimentalCondition = xsDataInputCCP4i.getExperimentalCondition()
                if(xsDataExperimentalCondition is not None):
                    xsDataBeam = xsDataExperimentalCondition.getBeam()
                    if(xsDataBeam is not None):
                        xsDataBeamSize = xsDataBeam.getSize()
                        if(xsDataBeamSize is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataBeamSize)
                        xsDataBeamFlux = xsDataBeam.getFlux()
                        if(xsDataBeamFlux is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(xsDataBeamFlux)
                        xsDataMinExposureTime = xsDataBeam.getMinExposureTimePerImage()
                        if(xsDataMinExposureTime is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(xsDataMinExposureTime)
                    xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()
                    if(xsDataGoniostat is not None):
                        xsDataMaxOscSpeed = xsDataGoniostat.getMaxOscillationSpeed()
                        if(xsDataMaxOscSpeed is not None):
                            xsDataSubWedge.getExperimentalCondition().getGoniostat().setMaxOscillationSpeed(xsDataMaxOscSpeed)
                        xsDataMinOscWidth = xsDataGoniostat.getMinOscillationWidth()
                        if(xsDataMinOscWidth is not None):
                            xsDataSubWedge.getExperimentalCondition().getGoniostat().setMinOscillationWidth(xsDataMinOscWidth)
            # Update with the sample
            xsDataSample = xsDataInputCCP4i.getSample()
            if(xsDataSample is not None):
                xsDataCollection.setSample(xsDataSample)


    def sendEmail(self, _strSubject, _strMessage):
        """Sends an email to the EDNA contact person (if configured)."""

        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.sendEmail: Subject = %s" % _strSubject)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.sendEmail: Message:")
        self.DEBUG(_strMessage)
        if self.strEDNAContactEmail == None:
            self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.sendEmail: No email address configured!")
        elif not EDUtilsPath.getEdnaSite().startswith("ESRF"):
            self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.sendEmail: Not executed at the ESRF! EDNA_SITE=%s" % EDUtilsPath.getEdnaSite())
        else:
            try:
                self.DEBUG("Sending message to %s." % self.strEDNAContactEmail)
                self.DEBUG("Message: %s" % _strMessage)
                strMessage = """
EDNA_HOME = %s
EDNA_SITE = %s
PLUGIN_NAME = %s
working_dir = %s
%s

""" % (EDUtilsPath.getEdnaHome(), EDUtilsPath.getEdnaSite(), self.getPluginName(), self.getWorkingDirectory(), _strMessage)
                strEmailMsg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (self.strEDNAEmailSender, \
                                                                                self.strEDNAContactEmail, \
                                                                                _strSubject, strMessage))
                server = smtplib.SMTP("localhost")
                server.sendmail(self.strEDNAEmailSender, self.strEDNAContactEmail, strEmailMsg)
                server.quit()
            except:
                self.ERROR("Error when sending email message!")
                self.writeErrorTrace()


    def executeSimpleHTML(self, _xsDataResultCharacterisation):
        xsDataInputSimpleHTMLPage = XSDataInputSimpleHTMLPage()
        xsDataInputSimpleHTMLPage.setCharacterisationResult(_xsDataResultCharacterisation)
        self.edPluginExecSimpleHTML.setDataInput(xsDataInputSimpleHTMLPage)
        self.edPluginExecSimpleHTML.connectSUCCESS(self.doSuccessSimpleHTML)
        self.edPluginExecSimpleHTML.connectFAILURE(self.doFailureSimpleHTML)
        self.executePluginSynchronous(self.edPluginExecSimpleHTML)


    def doSuccessSimpleHTML(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doSuccessSimpleHTML...")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlInterfaceToMXCuBEv1_3.doSuccessSimpleHTML")
        self.xsDataResultMXCuBE.setHtmlPage(_edPlugin.getDataOutput().getPathToHTMLFile())

    def doFailureSimpleHTML(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_3.doFailureSimpleHTML...")
