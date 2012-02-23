#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Karl Levik"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose import EDVerbose
from EDMessage import EDMessage
from EDApplication import EDApplication
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataInputCharacterisation

class EDApplicationMXv1Characterisation(EDApplication):

    APPLICATION_NAME = "EDApplicationMXv1Characterisation"
    APPLICATION_VERSION = "1.0.1"
    IMAGE_PARAM_LABEL = "--image"
    DATASET_PARAM_LABEL = "--data"
    FLUX_PARAM_LABEL = "--flux"
    BEAM_SIZE_PARAM_LABEL = "--beamSize"
    BEAM_POS_X_PARAM_LABEL = "--beamPositionX"
    BEAM_POS_Y_PARAM_LABEL = "--beamPositionY"
    MAX_EXPOSURE_TIME_PARAM_LABEL = "--maxExposureTimePerDataCollection"
    MIN_EXPOSURE_TIME_PARAM_LABEL = "--minExposureTimePerImage"
    DEBUG_PARAM_LABEL = "--DEBUG"
    VERSION_PARAM_LABEL = "--version or -v"
    TEMPLATE_PARAM_LABEL = "--generateTemplate"
    COMPLEXITY_PARAM_LABEL = "--complexity"
    RESULTS_FILE_LABEL = "--resultFile"
    FORCED_SPACE_GROUP_LABEL = "--forcedSpaceGroup"
    ANOMALOUS_DATA_LABEL = "--anomalousData"
    STRATEGY_OPTION_LABEL = "--strategyOption"
    COMMENTS_LABEL = "--comments"
    SHORTCOMMENTS_LABEL = "--shortComments"
    TRANSMISSION_LABEL = "--transmission"


    """
    Derives from EDApplication in order to add a Configuration Feature
    """
    def __init__(self, _strPluginName=None, _strConfigurationFileName=None, _xsDataInputCharacterisation=None, _strComments = None, _strShortComments = None):
        """
        @param _strPluginName: name of control plugin to load
        @type  _strPluginName: string
        @param _strConfigurationFileName: the configuration file to use  
        @type _strConfigurationFileName: string
        @param _xsDataInputCharacterisation: the input characterisation object to use  
        @type _xsDataInputCharacterisation: XSDataInputCharacterisation
        """
        EDApplication.__init__(self, _strName=EDApplicationMXv1Characterisation.APPLICATION_NAME, \
                                _strVersion=EDApplicationMXv1Characterisation.APPLICATION_VERSION, \
                                _strPluginName=_strPluginName, \
                                _strConfigurationFileName=_strConfigurationFileName)
        self.__listImagePaths = None
        self.__strDatasetFileName = None
        self.__fFlux = None
        self.__fMaxExposureTimePerDataCollection = 10000 # s, default MXv1 value
        self.__fMinExposureTimePerImage = None
        self.__fBeamSize = None
        self.__bTemplateMode = False
        self.__strGeneratedTemplateFile = None
        self.__strComplexity = "none"
        self.__strResultsFilePath = None
        self.__strForcedSpaceGroup = None
        self.__bAnomalousData = False
        self.__fBeamPosX = None
        self.__fBeamPosY = None
        self.__strStrategyOption = None
        self.__bProcess = True
        self.__iDataCollectionId = None
        self.__xsDataInputCharacterisation = _xsDataInputCharacterisation
        self.__strPluginName = None
        self.__strDataInputFilePath = None
        self.__strShortComments = _strShortComments
        self.__strComments = _strComments
        self.__fTransmission = None
        

    def preProcess(self):
        """
        Processes the command line, creates the plugins
        """
        EDApplication.preProcess(self)
        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.preProcess")

        if self.__xsDataInputCharacterisation == None:
            # Read command line parameters and check if they are ok
            self.__bProcess = self.readAndProcessCommandLine()

            if (self.__bProcess) and not (self.__strDatasetFileName is None):
                # Check if XML data is given as input :
                if (self.__strDatasetFileName is not None):
                    try:
                        self.__xsDataInputCharacterisation = XSDataInputCharacterisation.parseFile(self.__strDatasetFileName)
                    except:
                        errorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ("EDApplicationMXv1Characterisation.process", self.__strDatasetFileName)
                        EDVerbose.error(errorMessage)
                        raise RuntimeError, errorMessage


    def process(self):
        """
        Calls the Plugin to be executed
        """
        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.process")
        if (not self.isFailure()) and (self.__bProcess):
            edPlugin = EDFactoryPluginStatic.loadPlugin(self.getPluginName())
            if(edPlugin is not None):
                edPlugin.setBaseDirectory(self.getFullApplicationWorkingDirectory())
                edPlugin.setBaseName(self.getPluginName())

                self.setPluginInput(edPlugin)

                edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplicationMXv1Characterisation.process: Executing " + self.getPluginName())
                edPlugin.execute()
                edPlugin.synchronize()
            else:
                EDVerbose.error("EDApplicationMXv1Characterisation.process : plugin not loaded : %s" % self.getPluginName())
                self.setFailure(True)


    def setPluginInput(self, _edPlugin):
        xsDataDiffractionPlan = XSDataDiffractionPlan()
        if (not self.__fMaxExposureTimePerDataCollection is None):
            xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(self.__fMaxExposureTimePerDataCollection))
        if (not self.__strForcedSpaceGroup is None):
            xsDataDiffractionPlan.setForcedSpaceGroup(XSDataString(self.__strForcedSpaceGroup))
        if (not self.__bAnomalousData is None):
            xsDataDiffractionPlan.setAnomalousData(XSDataBoolean(self.__bAnomalousData))
        if (not self.__strStrategyOption is None):
            xsDataDiffractionPlan.setStrategyOption(XSDataString(self.__strStrategyOption))
        if (not self.__strComplexity is None):
            xsDataDiffractionPlan.setComplexity(XSDataString(self.__strComplexity))
        _edPlugin.setDataInput(xsDataDiffractionPlan, "diffractionPlan")

        if (not self.__listImagePaths is None):
            for strImagePath in self.__listImagePaths:
                _edPlugin.setDataInput(XSDataString(strImagePath), "imagePaths")

        if (not self.__xsDataInputCharacterisation is None):
            _edPlugin.setDataInput(self.__xsDataInputCharacterisation, "inputCharacterisation")
        if (not self.__fFlux is None):
            _edPlugin.setDataInput(XSDataFloat(self.__fFlux), "flux")
        if (not self.__fMinExposureTimePerImage is None):
            _edPlugin.setDataInput(XSDataFloat(self.__fMinExposureTimePerImage), "minExposureTimePerImage")
        if (not self.__fBeamSize is None):
            _edPlugin.setDataInput(XSDataFloat(self.__fBeamSize), "beamSize")
        if (not self.__bTemplateMode is None):
            _edPlugin.setDataInput(XSDataBoolean(self.__bTemplateMode), "templateMode")
        if (not self.__strGeneratedTemplateFile is None):
            _edPlugin.setDataInput(XSDataString(self.__strGeneratedTemplateFile), "generatedTemplateFile")
        if (not self.__strResultsFilePath is None):
            _edPlugin.setDataInput(XSDataString(self.__strResultsFilePath), "resultsFilePath")
        if (not self.__fBeamPosX is None):
            _edPlugin.setDataInput(XSDataFloat(self.__fBeamPosX), "beamPosX")
        if (not self.__fBeamPosY is None):
            _edPlugin.setDataInput(XSDataFloat(self.__fBeamPosY), "beamPosY")
        if (not self.__iDataCollectionId is None):
            _edPlugin.setDataInput(XSDataInteger(self.__iDataCollectionId), "dataCollectionId")
        if (not self.__strShortComments is None):
            _edPlugin.setDataInput(XSDataString(self.__strShortComments), "shortComments")
        if (not self.__strComments is None):
            _edPlugin.setDataInput(XSDataString(self.__strComments), "comments")
        if (not self.__fTransmission is None):
            _edPlugin.setDataInput(XSDataDouble(self.__fTransmission), "transmission")



    def readAndProcessCommandLine(self):
        """
        Reads and processes the command line
        """
        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.readAndProcessCommandLine")
        bCommandLineIsOk = False
        strResultsFilePath = self.getCommandLineArgument(EDApplicationMXv1Characterisation.RESULTS_FILE_LABEL)
        if (strResultsFilePath is not None):
            self.__strResultsFilePath = strResultsFilePath
            EDVerbose.screen("Results written to file                      : %s" % (self.__strResultsFilePath))
        strShortComments = self.getCommandLineArgument(EDApplicationMXv1Characterisation.SHORTCOMMENTS_LABEL)
        if(strShortComments is not None):
            self.__strShortComments = strShortComments
            EDVerbose.screen("Short comments                               : %s" % (self.__strShortComments))
        strComments = self.getCommandLineArgument(EDApplicationMXv1Characterisation.COMMENTS_LABEL)
        if(strComments is not None):
            self.__strComments = strComments
            EDVerbose.screen("Comments                                     : %s" % (self.__strComments))
        # Check if m_strDATASET_PARAM_LABEL is given:
        self.__strDatasetFileName = self.getCommandLineArgument(EDApplicationMXv1Characterisation.DATASET_PARAM_LABEL)
        if (self.__strDatasetFileName is not None):
            if (not os.path.isabs(self.__strDatasetFileName)):
                self.__strDatasetFileName = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.__strDatasetFileName))
            EDVerbose.screen("Reading input data from : %s" % (self.__strDatasetFileName))
            EDVerbose.screen("(Any other command line arguments are neglected.)")
            bCommandLineIsOk = True
        else:
            # Special processing necessary for image list:
            EDVerbose.DEBUG("EDApplicationMXv1Characterisation.readAndProcessCommandLine: Searching for " + EDApplicationMXv1Characterisation.IMAGE_PARAM_LABEL + " tag.")
            strCommandLine = self.getCommandLine()
            EDVerbose.DEBUG("EDApplicationMXv1Characterisation.readAndProcessCommandLine: Command line: " + strCommandLine)
            listCommandLine = self.getEdCommandLine().getCommandLineArguments()
            # First go through in order to find if there are any images
            bFoundImageToken = False
            for strCommandLineItem in listCommandLine:

                bFoundImageToken = self.processCommandLineItems(strCommandLineItem, bFoundImageToken)

            # Check that we have at least one image...
            if (self.__listImagePaths is not None):
                # Then find any other optional parameters
                strComplexity = self.getCommandLineArgument(EDApplicationMXv1Characterisation.COMPLEXITY_PARAM_LABEL)
                if (strComplexity is not None):
                    self.__strComplexity = strComplexity
                EDVerbose.screen("BEST complexity set to                       : %s" % (self.__strComplexity))
                strFlux = self.getCommandLineArgument(EDApplicationMXv1Characterisation.FLUX_PARAM_LABEL)
                if (strFlux is not None):
                    self.__fFlux = float(strFlux)
                    EDVerbose.screen("Beamline flux set to                         : %7.1f [photons/s]" % (self.__fFlux))
                strMaxExposureTimePerDataCollection = self.getCommandLineArgument(EDApplicationMXv1Characterisation.MAX_EXPOSURE_TIME_PARAM_LABEL)
                if (strMaxExposureTimePerDataCollection is not None):
                    self.__fMaxExposureTimePerDataCollection = float(strMaxExposureTimePerDataCollection)
                    EDVerbose.screen("Max exposure time per data collection set to : %7.1f [s]" % (self.__fMaxExposureTimePerDataCollection))
                else:
                    EDVerbose.screen("Max exposure time per data collection set to : %7.1f [s] (default value for MXv1)" % (self.__fMaxExposureTimePerDataCollection))
                strMinExposureTimePerImage = self.getCommandLineArgument(EDApplicationMXv1Characterisation.MIN_EXPOSURE_TIME_PARAM_LABEL)
                if (strMinExposureTimePerImage is not None):
                    self.__fMinExposureTimePerImage = float(strMinExposureTimePerImage)
                    EDVerbose.screen("Minimum exposure time per image set to       : %7.3f [s]" % (self.__fMinExposureTimePerImage))
                strBeamSize = self.getCommandLineArgument(EDApplicationMXv1Characterisation.BEAM_SIZE_PARAM_LABEL)
                if (strBeamSize is not None):
                    self.__fBeamSize = float(strBeamSize)
                    EDVerbose.screen("Beam size (beam assumed to be square)        : %7.3f [mm]" % (self.__fBeamSize))
                strBeamPosX = self.getCommandLineArgument(EDApplicationMXv1Characterisation.BEAM_POS_X_PARAM_LABEL)
                if (strBeamPosX is not None):
                    self.__fBeamPosX = float(strBeamPosX)
                    EDVerbose.screen("Beam position X (MOSFLM ordering)            : %7.3f [mm]" % (self.__fBeamPosX))
                strBeamPosY = self.getCommandLineArgument(EDApplicationMXv1Characterisation.BEAM_POS_Y_PARAM_LABEL)
                if (strBeamPosY is not None):
                    self.__fBeamPosY = float(strBeamPosY)
                    EDVerbose.screen("Beam position Y (MOSFLM ordering)            : %7.3f [mm]" % (self.__fBeamPosY))
                strForcedSpaceGroup = self.getCommandLineArgument(EDApplicationMXv1Characterisation.FORCED_SPACE_GROUP_LABEL)
                if (strForcedSpaceGroup is not None):
                    self.__strForcedSpaceGroup = strForcedSpaceGroup
                    EDVerbose.screen("Forced space group for indexing              : %s" % (self.__strForcedSpaceGroup))
                strStrategyOption = self.getCommandLineArgument(EDApplicationMXv1Characterisation.STRATEGY_OPTION_LABEL)
                if(strStrategyOption is not None):
                    self.__strStrategyOption = strStrategyOption
                    EDVerbose.screen("Strategy option                              : %s" % (self.__strStrategyOption))
                strTransmission = self.getCommandLineArgument(EDApplicationMXv1Characterisation.TRANSMISSION_LABEL)
                if(strTransmission is not None):
                    self.__fTransmission = float(strTransmission)
                    EDVerbose.screen("Transmission                                 : %.1f [%%]" % (self.__fTransmission))
                bCommandLineIsOk = True
            elif (not self.__strGeneratedTemplateFile is None):
                bCommandLineIsOk = True
            else:
                # Check for -v or --v which has already been processed by EDApplciation
                if not ((EDApplication.VERSION_PARAM_LABEL_1 in listCommandLine) or \
                        (EDApplication.VERSION_PARAM_LABEL_2 in listCommandLine) or \
                        (EDApplication.HELP_LABEL_1 in listCommandLine) or \
                        (EDApplication.HELP_LABEL_2 in listCommandLine)):
                    self.usage()
                    bCommandLineIsOk = False
        return bCommandLineIsOk


    def processCommandLineItems(self, _strCommandLineItem, _bFoundImageToken):
        bFoundImageToken = _bFoundImageToken
        if(_strCommandLineItem == EDApplicationMXv1Characterisation.TEMPLATE_PARAM_LABEL):
            self.__bTemplateMode = True
            self.__strGeneratedTemplateFile = self.getCommandLineArgument(EDApplicationMXv1Characterisation.TEMPLATE_PARAM_LABEL)
            if (self.__strGeneratedTemplateFile == None):
                strErrorMessage = EDMessage.ERROR_MANDATORY_PARAM_MISSING_02 % ("EDApplicationMXv1Characterisation.preProcess", "No argument for command line %s key word found!" % \
                                                                              EDApplicationMXv1Characterisation.TEMPLATE_PARAM_LABEL)
                EDVerbose.error(strErrorMessage)
                return False
            if (not os.path.isabs(self.__strGeneratedTemplateFile)):
                self.__strGeneratedTemplateFile = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.__strGeneratedTemplateFile))

        if(_strCommandLineItem == EDApplicationMXv1Characterisation.ANOMALOUS_DATA_LABEL):
            self.__bAnomalousData = True
            EDVerbose.screen("Anomalous data:                              : True")

        if (bFoundImageToken == False):
            if (_strCommandLineItem == EDApplicationMXv1Characterisation.IMAGE_PARAM_LABEL):
                bFoundImageToken = True
        else:
            if (_strCommandLineItem[0:2] == "--"):
                bFoundImageToken = False
            else:
                if (self.__listImagePaths is None):
                    self.__listImagePaths = []
                if (not os.path.isabs(_strCommandLineItem)):
                    strAbsolutePath = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), _strCommandLineItem))
                else:
                    strAbsolutePath = _strCommandLineItem
                if (not os.path.exists(strAbsolutePath)):
                    strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ("EDApplicationMXv1Characterisation.readAndProcessCommandLine", strAbsolutePath)
                    EDVerbose.error(strErrorMessage)
                    return False
                else:
                    EDVerbose.DEBUG("EDApplicationMXv1Characterisation.readAndProcessCommandLine: Found image path: " + strAbsolutePath)
                self.__listImagePaths.append(strAbsolutePath)
        return bFoundImageToken




    def processCommandLinePluginName(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.processCommandLinePluginName")
        if (not self.getEdCommandLine().existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
        else:
            self.__strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationMXv1Characterisation.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self.__strPluginName))


    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.processCommandLineInputFilePath")
        if (not self.getEdCommandLine().existCommand(EDApplicationMXv1Characterisation.DATASET_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplicationMXv1Characterisation.DATASET_PARAM_LABEL)
        else:
            self.__strDataInputFilePath = self.getCommandLineArgument(EDApplicationMXv1Characterisation.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationMXv1Characterisation.processCommandLineInputFilePath : %s = %s" % (EDApplicationMXv1Characterisation.DATASET_PARAM_LABEL, self.__strDataInputFilePath))


    def usage(self):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("----- ")
        EDVerbose.screen("")
        EDVerbose.screen(" Either use:")
        EDVerbose.screen("")
        EDVerbose.screen(" - the full/advanced XML input:")
        EDVerbose.screen("")
        EDVerbose.screen("   edna-mxv1-characterisation --data path_to_xsDataInputCharacterisation_xml_file")
        EDVerbose.screen("")
        EDVerbose.screen(" - or use the --image keyword (note that all these keywords are ignored if the --data option is used):")
        EDVerbose.screen("")
        EDVerbose.screen("   edna-mxv1-characterisation --image image1 [image2 image3 ...]")
        EDVerbose.screen("")
        EDVerbose.screen(" In the case of using the --image command line keyword the following arguments are optional:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : BEST complexity [none (default), min or full]" % (EDApplicationMXv1Characterisation.COMPLEXITY_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam flux [photon/s]" % (EDApplicationMXv1Characterisation.FLUX_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam size [mm] (beam assumed to be square)" % (EDApplicationMXv1Characterisation.BEAM_SIZE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam position X [mm] (MOSFLM ordering)" % (EDApplicationMXv1Characterisation.BEAM_POS_X_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam position Y [mm] (MOSFLM ordering)" % (EDApplicationMXv1Characterisation.BEAM_POS_Y_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Max exposure time per data collection [s]" % (EDApplicationMXv1Characterisation.MAX_EXPOSURE_TIME_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Min exposure time per image [s]" % (EDApplicationMXv1Characterisation.MIN_EXPOSURE_TIME_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Forced space group for indexing" % (EDApplicationMXv1Characterisation.FORCED_SPACE_GROUP_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Anomalous data" % (EDApplicationMXv1Characterisation.ANOMALOUS_DATA_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Incoming transmission [%%]" % (EDApplicationMXv1Characterisation.TRANSMISSION_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Optional command to BEST, the currently only supported command is: -DamPar" % (EDApplicationMXv1Characterisation.STRATEGY_OPTION_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" Additional options available:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an xml template input file for edna" % (EDApplicationMXv1Characterisation.TEMPLATE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an xml file containing the characterisation results" % (EDApplicationMXv1Characterisation.RESULTS_FILE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (EDApplicationMXv1Characterisation.DEBUG_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (EDApplicationMXv1Characterisation.VERSION_PARAM_LABEL))
        EDVerbose.screen("")


    def doFailureActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDApplication.doFailureActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.doFailureActionPlugin")
        EDVerbose.screen("Execution of " + _edPlugin.getPluginName() + " failed.")
        EDVerbose.screen("Please inspect the log file for further information.")


    def doSuccessActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDApplication.doSuccessActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.doSuccessActionPlugin")

        if (_edPlugin.getListOfErrorMessages() != []):
            self.doFailureActionPlugin(_edPlugin)
        elif (_edPlugin.getListOfWarningMessages() != []):
            EDVerbose.screen("MXv1 characterisation successful with warning messages, please check the log file.")
        else:
            EDVerbose.screen("MXv1 characterisation successful!")
