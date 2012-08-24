#
#    Project: EDNA Dimplev0
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2011 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Pipeline authors:   Ronan Keegan (ronan.keegan@stfc.ac.uk)  
#                        Graeme Winter (graeme.winter@diamond.ac.uk)
#
#    This file:          Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Karl Levik"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

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
from XSDataCommon import XSDataFile

from XSDataCCP4DIMPLE import CCP4DataInputControlPipelineCalcDiffMap
from XSDataCCP4DIMPLE import CCP4MTZColLabels

class EDApplicationDimplev0(EDApplication):

    APPLICATION_NAME = "EDApplicationDimplev0"
    APPLICATION_VERSION = "1.0.0"
    DEBUG_PARAM_LABEL = "--DEBUG"
    VERSION_PARAM_LABEL = "--version or -v"
    TEMPLATE_PARAM_LABEL = "--generateTemplate"
    RESULTS_FILE_LABEL = "--resultFile"
    DATASET_PARAM_LABEL = "--data"
    PDBIN_LABEL = "--xyzIn"
    PDBOUT_LABEL = "--xyzOut"
    MTZIN_LABEL = "--hklIn"
    MTZOUT_LABEL = "--hklOut"
    I_LABEL = "--i"
    SIGI_LABEL = "--sigI"

    """
    Derives from EDApplication in order to add a Configuration Feature
    """
    def __init__(self, _strPluginName=None, _strConfigurationFileName=None, _ccp4DataInputControlPipelineCalcDiffMap=None):
        """
        @param _strPluginName: name of control plugin to load
        @type  _strPluginName: string
        @param _strConfigurationFileName: the configuration file to use  
        @type _strConfigurationFileName: string
        @param _ccp4DataInputControlPipelineCalcDiffMap: the input object to use  
        @type _ccp4DataInputControlPipelineCalcDiffMap: CCP4DataInputControlPipelineCalcDiffMap
        """
        EDApplication.__init__(self, _strName=EDApplicationDimplev0.APPLICATION_NAME, \
                                _strVersion=EDApplicationDimplev0.APPLICATION_VERSION, \
                                _strPluginName=_strPluginName, \
                                _strConfigurationFileName=_strConfigurationFileName)
        
        self.colLabelI = None
        self.colLabelSIGI = None

        self.strPDBIn = None
        self.strPDBOut = None
        self.strMTZIn = None
        self.strMTZOut = None

        self.inputXMLFile = None
        self.inputXMLFileName = None

        self.ccp4DataInputControlPipelineCalcDiffMap = _ccp4DataInputControlPipelineCalcDiffMap
        self.strPluginName = _strPluginName
        self.strDatasetFileName = None

        self.xsDataOutput = None


    def preProcess(self):
        """
        Processes the command line, creates the plugins
        """
        EDApplication.preProcess(self)
        EDVerbose.DEBUG("EDApplicationDimplev0.preProcess")

        if self.ccp4DataInputControlPipelineCalcDiffMap == None:
            # Read command line parameters and check if they are ok
            self.__bProcess = self.readAndProcessCommandLine()

            if (self.__bProcess) and not (self.strDatasetFileName is None):
                # Check if XML data is given as input :
                if (self.strDatasetFileName is not None):
                    try:
                        self.ccp4DataInputControlPipelineCalcDiffMap = CCP4DataInputControlPipelineCalcDiffMap.parseFile(self.strDatasetFileName)
                    except Exception:
                        errorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ("EDApplicationDimplev0.process", self.strDatasetFileName)
                        EDVerbose.error(errorMessage)
                        raise RuntimeError, errorMessage


    def process(self):
        """
        Calls the Plugin to be executed
        """
        EDVerbose.DEBUG("EDApplicationDimplev0.process")
        if (not self.isFailure()):
            edPlugin = EDFactoryPluginStatic.loadPlugin(self.getPluginName())
            if(edPlugin is not None):
                edPlugin.setBaseDirectory(self.getFullApplicationWorkingDirectory())
                edPlugin.setBaseName(self.getPluginName())
                
                if self.ccp4DataInputControlPipelineCalcDiffMap is None:
                    self.ccp4DataInputControlPipelineCalcDiffMap = self.createInput()
                edPlugin.setDataInput(self.ccp4DataInputControlPipelineCalcDiffMap)
                edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplicationDimplev0.process: Executing " + self.getPluginName())
                edPlugin.execute()
                edPlugin.synchronize()
            else:
                EDVerbose.error("EDApplicationDimplev0.process : plugin not loaded : %s" % self.getPluginName())
                self.setFailure(True)


    def createInput(self):
        ccp4DataInputControlPipelineCalcDiffMap = CCP4DataInputControlPipelineCalcDiffMap()
        
        xsDataStringPDBIn = XSDataString(self.strPDBIn)
        xsDataStringPDBOut = XSDataString(self.strPDBOut)
        xsDataStringMTZIn = XSDataString(self.strMTZIn)
        xsDataStringMTZOut = XSDataString(self.strMTZOut)

        xsDataFilePDBIn = XSDataFile()
        xsDataFilePDBIn.setPath(xsDataStringPDBIn)
        xsDataFilePDBOut = XSDataFile()
        xsDataFilePDBOut.setPath(xsDataStringPDBOut)
        xsDataFileMTZIn = XSDataFile()
        xsDataFileMTZIn.setPath(xsDataStringMTZIn)
        xsDataFileMTZOut = XSDataFile()
        xsDataFileMTZOut.setPath(xsDataStringMTZOut)
        
        ccp4DataInputControlPipelineCalcDiffMap.setXYZIN(xsDataFilePDBIn)
        ccp4DataInputControlPipelineCalcDiffMap.setXYZOUT(xsDataFilePDBOut)
        ccp4DataInputControlPipelineCalcDiffMap.setHKLIN(xsDataFileMTZIn)
        ccp4DataInputControlPipelineCalcDiffMap.setHKLOUT(xsDataFileMTZOut)
        
        ccp4MTZColLabels = CCP4MTZColLabels()
        ccp4MTZColLabels.setIMEAN(XSDataString(self.colLabelI))
        ccp4MTZColLabels.setSIGIMEAN(XSDataString(self.colLabelSIGI))
        
        ccp4DataInputControlPipelineCalcDiffMap.setColLabels(ccp4MTZColLabels)

        return ccp4DataInputControlPipelineCalcDiffMap

    def getDataOutput(self):
        return self.xsDataOutput

    def getPathToLogFile(self):
        return self._EDApplication__strPathToLogFile

    def readAndProcessCommandLine(self):
        """
        Reads and processes the command line
        """
        EDVerbose.DEBUG("EDApplicationDimplev0.readAndProcessCommandLine")
        bCommandLineIsOk = False
        strResultsFilePath = self.getCommandLineArgument(EDApplicationDimplev0.RESULTS_FILE_LABEL)
        if (strResultsFilePath is not None):
            self.__strResultsFilePath = strResultsFilePath
            EDVerbose.screen("Results written to file                      : %s" % (self.__strResultsFilePath))
        # Check if m_strDATASET_PARAM_LABEL is given:
        self.strDatasetFileName = self.getCommandLineArgument(EDApplicationDimplev0.DATASET_PARAM_LABEL)
        if (self.strDatasetFileName is not None):
            if (not os.path.isabs(self.strDatasetFileName)):
                self.strDatasetFileName = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.strDatasetFileName))
            EDVerbose.screen("Reading input data from : %s" % (self.strDatasetFileName))
            EDVerbose.screen("(Any other command line arguments are neglected.)")
            bCommandLineIsOk = True
        else:
            strPDBIn = self.getCommandLineArgument(EDApplicationDimplev0.PDBIN_LABEL)
            if (strPDBIn is not None):
                self.strPDBIn = str(strPDBIn)
                EDVerbose.screen("XYZ In set to                         : %s" % (self.strPDBIn))
            
            strPDBOut = self.getCommandLineArgument(EDApplicationDimplev0.PDBOUT_LABEL)
            if (strPDBOut is not None):
                self.strPDBOut = str(strPDBOut)
                EDVerbose.screen("XYZ Out set to                         : %s" % (self.strPDBOut))

            strMTZIn = self.getCommandLineArgument(EDApplicationDimplev0.MTZIN_LABEL)
            if (strMTZIn is not None):
                self.strMTZIn = str(strMTZIn)
                EDVerbose.screen("HKL In set to                         : %s" % (self.strMTZIn))
            
            strMTZOut = self.getCommandLineArgument(EDApplicationDimplev0.MTZOUT_LABEL)
            if (strMTZOut is not None):
                self.strMTZOut = str(strMTZOut)
                EDVerbose.screen("HKL Out set to                         : %s" % (self.strMTZOut))

            strI = self.getCommandLineArgument(EDApplicationDimplev0.I_LABEL)
            if (strI is not None):
                self.colLabelI = str(strI)
                EDVerbose.screen("I set to                         : %s" % (self.colLabelI))

            strSIGI = self.getCommandLineArgument(EDApplicationDimplev0.SIGI_LABEL)
            if (strSIGI is not None):
                self.colLabelSIGI = str(strSIGI)
                EDVerbose.screen("SIGI set to                         : %s" % (self.colLabelSIGI))

            strCommandLine = self.getCommandLine()
            EDVerbose.DEBUG("EDApplicationDimplev0.readAndProcessCommandLine: Command line: " + strCommandLine)
            listCommandLine = self.getEdCommandLine().getCommandLineArguments()
            for strCommandLineItem in listCommandLine:
                self.processCommandLineItems(strCommandLineItem)

            if (None not in (strPDBIn, strPDBOut, strMTZIn, strMTZOut)):
                bCommandLineIsOk = True
            elif (not self.strGeneratedTemplateFile is None):
                bCommandLineIsOk = True
            else:
                self.usage()
                bCommandLineIsOk = False
        return bCommandLineIsOk


    def processCommandLineItems(self, _strCommandLineItem):
        if(_strCommandLineItem == EDApplicationDimplev0.TEMPLATE_PARAM_LABEL):
            self.bTemplateMode = True
            self.strGeneratedTemplateFile = self.getCommandLineArgument(EDApplicationDimplev0.TEMPLATE_PARAM_LABEL)
            if (self.strGeneratedTemplateFile == None):
                strErrorMessage = EDMessage.ERROR_MANDATORY_PARAM_MISSING_02 % ("EDApplicationDimplev0.processCommandLineItems", "No argument for command line %s key word found!" % \
                                                                              EDApplicationDimplev0.TEMPLATE_PARAM_LABEL)
                EDVerbose.error(strErrorMessage)
                return False
            if (not os.path.isabs(self.strGeneratedTemplateFile)):
                self.strGeneratedTemplateFile = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.strGeneratedTemplateFile))



    def processCommandLinePluginName(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationDimplev0.processCommandLinePluginName")
        if (not self.getEdCommandLine().existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
        else:
            self.strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationDimplev0.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self.strPluginName))


    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationDimplev0.processCommandLineInputFilePath")
        if (not self.getEdCommandLine().existCommand(EDApplicationDimplev0.DATASET_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplicationDimplev0.DATASET_PARAM_LABEL)
        else:
            self.strDataInputFilePath = self.getCommandLineArgument(EDApplicationDimplev0.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationDimplev0.processCommandLineInputFilePath : %s = %s" % (EDApplicationDimplev0.DATASET_PARAM_LABEL, self.strDataInputFilePath))


    def usage(self):
        """
        Print usage...
        """
        
        EDVerbose.screen("Usage: dimple [-D] HKLIN <input mtz> XYZIN <input pdb> " + \
                   "HKLOUT <output mtz> XYZOUT <output pdb>\n" + \
                   "\n" + \
                   "Options:\n" + \
                   "\n" + \
                   "    -D   Input LABIN keyword defaults to 'IMEAN=IMEAN' and 'SIGIMEAN=SIGIMEAN'.\n" + \
                   "         Also causes input XML file lines to be written in temporary file in the local directory.'\n" + \
                   "\n")
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" Additional options available:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an xml template input file " % (EDApplicationDimplev0.TEMPLATE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an xml file containing the characterisation results" % (EDApplicationDimplev0.RESULTS_FILE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (EDApplicationDimplev0.DEBUG_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (EDApplicationDimplev0.VERSION_PARAM_LABEL))
        EDVerbose.screen("")


    def doFailureActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDApplication.doFailureActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationDimplev0.doFailureActionPlugin")
        EDVerbose.screen("Execution of " + _edPlugin.getPluginName() + " failed.")
        EDVerbose.screen("Please inspect the log file for further information.")


    def doSuccessActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages and set the output
        """
        EDApplication.doSuccessActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationDimplev0.doSuccessActionPlugin")

        xsDataOutput = _edPlugin.getDataOutput()

        if (_edPlugin.getListOfErrorMessages() != []):
            self.doFailureActionPlugin(_edPlugin)
        elif (_edPlugin.getListOfWarningMessages() != []):
            EDVerbose.screen("Dimplev0 successful with warning messages, please check the log file.")
        else:
            EDVerbose.screen("Dimplev0 successful!")
