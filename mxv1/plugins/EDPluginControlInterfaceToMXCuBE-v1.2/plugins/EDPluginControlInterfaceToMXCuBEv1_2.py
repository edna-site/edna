#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

import os
import shutil
import smtplib

from EDVerbose import EDVerbose
from EDMessage import EDMessage
from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsImage import EDUtilsImage
from EDConfiguration import EDConfiguration
from EDUtilsPath import EDUtilsPath

from XSDataMXCuBEv1_2 import XSDataInputMXCuBE
from XSDataMXCuBEv1_2 import XSDataResultMXCuBE
from XSDataMXCuBEv1_2 import XSDataResultCharacterisation
from XSDataMXCuBEv1_2 import XSDataDictionary
from XSDataMXCuBEv1_2 import XSDataKeyValuePair
from XSDataMXCuBEv1_2 import XSDataString
from XSDataMXv1 import XSDataInputControlISPyB


class EDPluginControlInterfaceToMXCuBEv1_2(EDPluginControl):
    """
    This is the plugin interface to launch the MXv1 characterisation from an MXCuBE gui.
    It is for the moment a wrapper for the EDPluginControlCCP4iv1_1 plugin, which also
    runs the ISPyB control plugin if a data collection id is available.
    """

    __EDNA_CONTACT_EMAIL = "contactEmail"
    __EDNA_EMAIL_SENDER = "emailSender"

    def __init__ (self):
        """
        Initialisation of EDPluginControlInterfaceToMXCuBEv1_2:
        - Input data type class : XSDataInputMXCuBE
        - Name of default characterisation plugin : EDPluginControlCharacterisationv1_1
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMXCuBE)
        self.__strPluginControlCCP4i = "EDPluginControlCCP4iv1_1"
        self.__edPluginControlCCP4i = None
        self.__strPluginControlISPyB = "EDPluginControlISPyBv1_0"
        self.__edPluginControlISPyB = None
        self.__xsDataResultMXCuBE = None
        self.__xsDataIntegerDataCollectionId = None
        self.__strPluginExecOutputHTMLName = "EDPluginExecOutputHTMLv1_0"
        self.__edPluginExecOutputHTML = None
        self.__strEDNAContactEmail = None
        self.__strEDNAEmailSender = "edna-support@esrf.fr"


    def checkParameters(self):
        """
        Checks the mandatory input parameters :
        - dataSet
        - outputFileDirectory
        """
        self.verboseDebug("EDPluginControlInterfaceToMXCuBEv1_2.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataSet(), "dataSet")
        #self.checkMandatoryParameters( self.getDataInput().getOutputFileDirectory(), "outputFileDirectory" )


    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.configure")
        xsPluginItem = self.getConfiguration()
        if xsPluginItem == None:
            EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.configure: No plugin item defined.")
        else:
            self.__strEDNAContactEmail = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginControlInterfaceToMXCuBEv1_2.__EDNA_CONTACT_EMAIL)
            EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.configure: EDNAContactEmail = %s" % self.__strEDNAContactEmail)
            strEDNAEmailSender = EDConfiguration.getStringParamValue(xsPluginItem, self.__EDNA_EMAIL_SENDER)
            if strEDNAEmailSender:
                self.__strEDNAEmailSender = strEDNAEmailSender


    def preProcess(self, _edPlugin=None):
        """
        This method prepares the input for the CCP4i plugin and loads it.
        """
        EDPluginControl.preProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.preProcess...")

        EDFactoryPluginStatic.loadModule("XSDataCCP4iv1_1")
        from XSDataCCP4iv1_1 import XSDataInputCCP4i
        xsDataInputCCP4i = XSDataInputCCP4i()
        xsDataInputMXCuBE = self.getDataInput()
        xsDataInputCCP4i.setDataSet(xsDataInputMXCuBE.getDataSet())
        #xsDataInputCCP4i.setDataFile( xsDataInputMXCuBE.getDataFile() )
        xsDataInputCCP4i.setExperimentalCondition(xsDataInputMXCuBE.getExperimentalCondition())
        xsDataInputCCP4i.setDiffractionPlan(xsDataInputMXCuBE.getDiffractionPlan())
        xsDataInputCCP4i.setSample(xsDataInputMXCuBE.getSample())

        self.__edPluginControlCCP4i = self.loadPlugin(self.__strPluginControlCCP4i, "CCP4i")
        self.__edPluginControlCCP4i.setDataInput(xsDataInputCCP4i)

        self.__xsDataIntegerDataCollectionId = xsDataInputMXCuBE.getDataCollectionId()
        if (self.__xsDataIntegerDataCollectionId is not None):
            self.__edPluginControlISPyB = self.loadPlugin(self.__strPluginControlISPyB, "ISPyB")

        self.__edPluginExecOutputHTML = self.loadPlugin(self.__strPluginExecOutputHTMLName, "OutputHTML")


    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.process...")

        if self.__edPluginControlCCP4i is not None:
            self.connectProcess(self.__edPluginControlCCP4i.executeSynchronous)
            self.__edPluginControlCCP4i.connectSUCCESS(self.doSuccessActionCCP4i)
            self.__edPluginControlCCP4i.connectFAILURE(self.doFailureActionCCP4i)
            if self.__edPluginControlISPyB is not None:
                self.__edPluginControlISPyB.connectSUCCESS(self.doSuccessActionISPyB)
                self.__edPluginControlISPyB.connectFAILURE(self.doFailureActionISPyB)


    def postProcess(self, _edPlugin=None):
        EDPluginControl.postProcess(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.postProcess...")
        self.setDataOutput(self.__xsDataResultMXCuBE)


    def doSuccessActionCCP4i(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.doSuccessActionCCP4i...")
        self.retrieveSuccessMessages(self.__edPluginControlCCP4i, "EDPluginControlInterfaceToMXCuBEv1_2.doSuccessActionCCP4i")
        # Retrieve the results from the CCP4 plugin execution
        xsDataResultCCP4i = self.__edPluginControlCCP4i.getDataOutput()
        self.__xsDataResultMXCuBE = XSDataResultMXCuBE()
        xsDataStringListOfOutputFiles = xsDataResultCCP4i.getListOfOutputFiles()
        self.__xsDataResultMXCuBE.setListOfOutputFiles(xsDataStringListOfOutputFiles)
        # Retrieve the characterisation output object
        xsDataResultCharacterisation = self.getXSDataResultCharacterisation(xsDataStringListOfOutputFiles.getValue())
        # For the moment, create "DNA" style output directory
        strPathToDNAFileDirectory = self.createDNAFileDirectoryPath(xsDataResultCharacterisation)
        xsDataDictionaryLogFile = None
        if (self.createDNAFileDirectory(strPathToDNAFileDirectory)):
            xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataStringListOfOutputFiles, xsDataResultCharacterisation, strPathToDNAFileDirectory)
        strPyArchPathToDNAFileDirectory = self.createPyArchDNAFilePath(strPathToDNAFileDirectory)
        if (self.createDNAFileDirectory(strPyArchPathToDNAFileDirectory)):
            xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataStringListOfOutputFiles, xsDataResultCharacterisation, strPyArchPathToDNAFileDirectory)
        self.__xsDataResultMXCuBE.setOutputFileDictionary(xsDataDictionaryLogFile)
        # Send success email message (MXSUP-183):
        strSubject = "%s : SUCCESS!" % EDUtilsPath.getEdnaSite()
        strMessage = "Success!"
        if xsDataDictionaryLogFile != None:
            for xsDataKeyValuePair in xsDataDictionaryLogFile.getKeyValuePair():
                strKey = xsDataKeyValuePair.getKey().getValue()
                if strKey == "executiveSummary":
                    strPathToExecutiveSummary = xsDataKeyValuePair.getValue().getValue()
                    strMessage = EDUtilsFile.readFile(strPathToExecutiveSummary)
        self.sendEmail(strSubject, strMessage)
        # Fix for bug EDNA-55 : If burning strategy EDNA2html shouldn't be run
        bRunExecOutputHTML = True
        xsDataInputMXCuBE = self.getDataInput()
        xsDataDiffractionPlan = xsDataInputMXCuBE.getDiffractionPlan()
        if xsDataDiffractionPlan.getStrategyOption() is not None:
            strStrategyOption = xsDataDiffractionPlan.getStrategyOption().getValue()
            if strStrategyOption.find("-DamPar") != -1:
                bRunExecOutputHTML = False
        if (self.__edPluginExecOutputHTML is not None) and bRunExecOutputHTML:
            self.__edPluginExecOutputHTML.executeSynchronous()
            if not self.__edPluginExecOutputHTML.isFailure() and self.__edPluginExecOutputHTML.hasDataOutput("htmlFile"):
                strPathToHTMLFile = self.__edPluginExecOutputHTML.getDataOutput("htmlFile")[0].getPath().getValue()
                strPathToHTMLDir = self.__edPluginExecOutputHTML.getDataOutput("htmlDir")[0].getPath().getValue()
                strPathToDNAIndexDirectory = os.path.join(strPathToDNAFileDirectory, "index")
                if os.path.exists(strPathToHTMLFile):
                    try:
                        os.mkdir(strPathToDNAIndexDirectory)
                        shutil.copy(strPathToHTMLFile, os.path.join(strPathToDNAIndexDirectory, "index.html"))
                        shutil.copytree(strPathToHTMLDir, os.path.join(strPathToDNAIndexDirectory, os.path.basename(strPathToHTMLDir)))
                        if strPyArchPathToDNAFileDirectory is not None:
                            strPathToPyArchIndexDirectory = os.path.join(strPyArchPathToDNAFileDirectory, "index")
                            os.mkdir(strPathToPyArchIndexDirectory)
                            shutil.copy(strPathToHTMLFile, os.path.join(strPathToPyArchIndexDirectory, "index.html"))
                            shutil.copytree(strPathToHTMLDir, os.path.join(strPathToPyArchIndexDirectory, os.path.basename(strPathToHTMLDir)))
                    except Exception, e:
                        EDVerbose.DEBUG("Exception caught: %r" % e)
        if (self.__edPluginControlISPyB is not None):
            # Execute the ISPyB control plugin
            xsDataInputControlISPyB = XSDataInputControlISPyB()
            xsDataInputControlISPyB.setCharacterisationResult(xsDataResultCharacterisation)
            xsDataInputControlISPyB.setDataCollectionId(self.__xsDataIntegerDataCollectionId)
            self.__edPluginControlISPyB.setDataInput(xsDataInputControlISPyB)
            self.__edPluginControlISPyB.executeSynchronous()


    def getXSDataResultCharacterisation(self, _strListOfOutputFiles):
        listResult = _strListOfOutputFiles.split()
        # Search for the outputfile
        xsDataResultCharacterisation = None
        strPathToXSDataResultCharacteristion = None
        for strLine in listResult:
            if (strLine.find("dataOutput.xml") != -1):
                strPathToXSDataResultCharacteristion = strLine
        if (strPathToXSDataResultCharacteristion is not None):
            xsDataResultCharacterisation = XSDataResultCharacterisation.parseFile(strPathToXSDataResultCharacteristion)
        else:
            errorMessage = EDMessage.ERROR_DATA_HANDLER_02 % ("EDPluginControlInterfaceToMXCuBEv1_2.getXSDataResultCharacterisation", "Cannot find dataOutput.xml file in %s" % _strListOfOutputFiles)
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage
        return xsDataResultCharacterisation





    def doFailureActionCCP4i(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.doFailureActionCCP4i...")
        self.setFailure()
        xsDataResultMXCuBE = XSDataResultMXCuBE()
        self.setDataOutput(xsDataResultMXCuBE)
        self.writeDataOutput()
        # Send failure email message (MXSUP-183):
        strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        strMessage = "CCP4I FAILURE!"
        self.sendEmail(strSubject, strMessage)


    def doSuccessActionISPyB(self, _edPlugin):
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.__edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_2.doSuccessActionISPyB")


    def doFailureActionISPyB(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.doFailureActionISpyB...")
        self.retrieveFailureMessages(self.__edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_2.doFailureActionISpyB")
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
            EDVerbose.WARNING("EDPluginControlInterfaceToMXCuBEv1_2.createPyArchDNAFilePath: path not converted for pyarch: %s " % _strDNAFileDirectoryPath)
        return strPyarchDNAFilePath



    def createDNAFileDirectory(self, _strDNAFileDirectoryPath):
        """
        Create a "DNA-files" directory - if possible.
        """
        bSuccess = False
        if (_strDNAFileDirectoryPath is not None):
            if (os.path.exists(_strDNAFileDirectoryPath)):
                EDVerbose.warning("Removing existing DNA files directory: %s" % _strDNAFileDirectoryPath)
                if (os.access(_strDNAFileDirectoryPath, os.W_OK)):
                    shutil.rmtree(_strDNAFileDirectoryPath)
                else:
                    EDVerbose.warning("Cannot remove existing DNA files directory!")
            if (_strDNAFileDirectoryPath is not None):
                # Check if directory one level up is writeable
                strDNAFileBaseDirectory = os.path.split(_strDNAFileDirectoryPath)[0]
                if (os.access(strDNAFileBaseDirectory, os.W_OK)):
                    EDVerbose.DEBUG("Creating DNA files directory: %s" % _strDNAFileDirectoryPath)
                    os.mkdir(_strDNAFileDirectoryPath)
                    bSuccess = True
                else:
                    EDVerbose.warning("Cannot create DNA files directory: %s" % _strDNAFileDirectoryPath)
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


    def createOutputFileDictionary(self, _xsDataStringListOfOutputFiles, _xsDataResultCharacterisation, _strPathToLogFileDirectory=None):
        """
        This method creates an XSDataDictionary containing the name and locations of the 
        characterisation output files.
        """
        xsDataDictionaryLogFile = XSDataDictionary()
        # Start with the prediction images
        xsDataIndexingResult = _xsDataResultCharacterisation.getIndexingResult()
        xsDataGeneratePredictionResult = xsDataIndexingResult.getPredictionResult()
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
        listResult = _xsDataStringListOfOutputFiles.getValue().split()
        for strLine in listResult:
            if ((strLine.find("EDPluginBestv1_1.log") != -1) or (strLine.find("best.log") != -1)):
                strPathToBESTLogFile = strLine
            if (strLine.find("ExecutiveSummary") != -1):
                strPathToExecutiveSummary = strLine
        if (strPathToBESTLogFile is not None):
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



#        edStringListOfOutputFiles = '\n'
#        edStringListOfOutputFiles = edStringListOfOutputFiles + self.getBaseDirectory() + '\n'
#        xsDataOutput = self.__edPluginCharacterisation.getDataOutput()
#        edListPredictionImages = xsDataOutput.getIndexingResult().getPredictionResult().getPredictionImage()
#        for xsDataImagePrediction in edListPredictionImages:
#            strImagePath = xsDataImagePrediction.getPath().getValue()
#            edStringListOfOutputFiles = edStringListOfOutputFiles + strImagePath + '\n'
#
#        edStringCharacterisationDirectory = os.path.join( self.getWorkingDirectory(), "Characterisation" )
#        edStringBestWorkingDirectory = os.path.join( edStringCharacterisationDirectory, "Strategy" )
#        edStringBestWorkingDirectory = os.path.join( edStringBestWorkingDirectory, "EDPluginBestv1_2" )
#        edStringBestPlotFilePath = os.path.join( edStringBestWorkingDirectory, "EDPluginBestv1_2_plots.mtv" )
#        edStringCharacterisationOutput = os.path.join( edStringCharacterisationDirectory, "EDPluginControlCharacterisationv1_2_dataOutput.xml" )
#
#        edStringListOfOutputFiles = edStringListOfOutputFiles + edStringCharacterisationOutput + '\n'
#        edStringListOfOutputFiles = edStringListOfOutputFiles + edStringBestPlotFilePath + '\n'
#        
#        xsDataStringListOfOutputFiles = XSDataString( edStringListOfOutputFiles )
#        xsDataResultMXCuBE.setListOfOutputFiles( xsDataStringListOfOutputFiles )
#        
#        self.setDataOutput( xsDataResultMXCuBE )


    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.doFailureActionCharacterisation")
        # Send failure email message (MXSUP-183):
        strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        strMessage = "Characterisation FAILURE!"
        self.sendEmail(strSubject, strMessage)


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
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.createDataInputCharacterisationFromDataSets")
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

        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.sendEmail: Subject = %s" % _strSubject)
        EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.sendEmail: Message:")
        EDVerbose.DEBUG(_strMessage)
        if self.__strEDNAContactEmail == None:
            EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.sendEmail: No email address configured!")
        elif not EDUtilsPath.getEdnaSite().startswith("ESRF"):
            EDVerbose.DEBUG("EDPluginControlInterfaceToMXCuBEv1_2.sendEmail: Not executed at the ESRF! EDNA_SITE=%s" % EDUtilsPath.getEdnaSite())
        else:
            try:
                EDVerbose.DEBUG("Sending message to %s." % self.__strEDNAContactEmail)
                EDVerbose.DEBUG("Message: %s" % _strMessage)
                strMessage = """
EDNA_HOME = %s
EDNA_SITE = %s
PLUGIN_NAME = %s
working_dir = %s
%s

""" % (EDUtilsPath.getEdnaHome(), EDUtilsPath.getEdnaSite(), self.getPluginName(), self.getWorkingDirectory(), _strMessage)
                strEmailMsg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (self.__strEDNAEmailSender, \
                                                                                self.__strEDNAContactEmail, \
                                                                                _strSubject, strMessage))
                server = smtplib.SMTP("localhost")
                server.sendmail(self.__strEDNAEmailSender, self.__strEDNAContactEmail, strEmailMsg)
                server.quit()
            except:
                EDVerbose.DEBUG("Error when sending email message!")
                EDVerbose.writeErrorTrace()
