# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (Kieffer@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, tempfile, stat, types

from EDSlot                import EDSlot
from EDUtilsPath           import EDUtilsPath
from EDConfiguration       import EDConfiguration
from EDConfigurationStatic import EDConfigurationStatic
from EDUtilsFile           import EDUtilsFile
from EDStatus              import EDStatus
from EDAction              import EDAction
from EDDecorator           import deprecated
from XSDataCommon          import XSDataResult


class EDPlugin(EDAction):
    """
    This is the EDNA plugin main class
    An EDNA plugin class:
        - is a configurable entity
        - has a base name (<date>-<random number>-<base name>)
        - handles input/output data (setter, getter, checker)
        - has warning and error messages
        - has a base and a working directory (both are configurable)
        The working directory is the folder from which the plugin is launched
        and should contain all associated files with the plugin execution (edna xml input/output, 3rd party output files)
        The base directory is the parent directory of the working directory. 
        Example: the working directory of a control plugin is the base directory of the plugins that it invokes,
        i.e. the plugins working directories has the control plugin working directory as parent.
    - defines the method that generates an executive summary (user-related output summary) that sub-classes should implement
    """
    CONF_BASE_DIR_LABEL = "baseDirectory"
    CONF_WORKING_DIR_LABEL = "workingDirectory"
    CONF_TIME_OUT = "timeOut"
    CONF_WRITE_XML_INPUT_OUTPUT = "writeXMLInputOutput"
    CONF_WRITE_XML_OUTPUT = "writeXMLOutput"
    CONF_WRITE_XML_INPUT = "writeXMLInput"

    def __init__ (self):
        """
        Initializes plugin related attributes described above
        """
        EDAction.__init__(self)
        self.__xsPluginItem = None
        self.__dictXSDataInputClass = {}
        self.__dictXSDataInput = {}
        self.__dictXSDataOutput = {}
        self.__strDefaultInputDataKey = "defaultInputData"
        self.__strDefaultOutputDataKey = "defaultOutputData"
        self.__edSlotExportDataOutput = EDSlot()
        self.__strBaseDirectory = None
        self.__strWorkingDirectory = None
        self.__strBaseName = None
        self.__listExecutiveSummaryLines = []
        self.__strExecutiveSummarySeparator = "-" * 80
        self.__listErrorMessages = []
        self.__listWarningMessages = []
        self.__isRequiredToHaveConfiguration = False
        self.__bWriteDataXMLInputOutput = True
        self.__bWriteDataXMLOutput = True
        self.__bWriteDataXMLInput = True
        self.__strPluginId = "%s-%08i" % (self.getClassName(), self.getId())
        self.strPathDataInput = None
        self.strPathDataOutput = None
        self.__bUseWarningInsteadOfError = False
        self.__edConfiguration = EDConfigurationStatic()


    def preProcess(self, _edObject=None):
        """
        Writes xml data input in the working dir (if required)
        Connects a slot for generating the executive summary after the plugin execution
        Connects a slot for checking output data to the finally process
        Initialize the base directory
        Configures the plugin
        Checks the input data
        """
        EDAction.preProcess(self, _edObject)
        self.DEBUG("EDPlugin.preProcess")
        self.connectPostProcess(self.exportDataOutput)
        if self.__bWriteDataXMLInputOutput:
            if self.__bWriteDataXMLInput:
                self.connectPreProcess(self.writeDataInput)
        self.connectPostProcess(self.generateExecutiveSummary)
        self.connectFinallyProcess(self.checkDataOutput)
        if (self.__strBaseName is None):
            self.setBaseName(self.createBaseName())
        EDStatus.tellRunning(self.__strPluginId)
        self.connectFinallyProcess(self.tellFinished)
        self.checkParameters()


    def tellFinished(self, _edObject=None):
        """
        Tell EDStatus that the plugin has finished, either in success either in error 
        """
        if self.isFailure():
            EDStatus.tellFailure(self.__strPluginId)
        else:
            EDStatus.tellSuccess(self.__strPluginId)

    def checkDataOutput(self, _edObject=None):
        """
        Checks if output data is available, if not issues a warning and sets an empty XSDataResult as output data
        Writes xml data output in the working dir (if required)
        """
        EDAction.finallyProcess(self, _edObject)
        if self.__dictXSDataOutput == {}:
            strWarningMessage = "Output data for plugin %s not set, using XSDataResult as output" % self.getPluginName()
            self.WARNING(strWarningMessage)
            self.addWarningMessage(strWarningMessage)
            self.setDataOutput(XSDataResult())
        if self.__bWriteDataXMLInputOutput:
            if self.__bWriteDataXMLOutput:
                self.writeDataOutput()


    def synchronize(self):
        """
        This method calls EDAction.synchronize and if a time-out occurs an error message
        is added to the list of error messages.
        """
        EDAction.synchronize(self)
        if self.isTimeOut():
            strErrorMessage = "Timeout when waiting for %s to terminate." % self.getClassName()
            self.addErrorMessage(strErrorMessage)

    @deprecated
    def setConfiguration(self, _xsPluginItem):
        """
        Receives a Plugin Configuration as XSPluginItem or python dict from the application.
        """
        self.DEBUG("EDPlugin.setConfiguration")
        self.__edConfiguration = EDConfiguration()
        if isinstance(_xsPluginItem, dict):
            self.__edConfiguration[self.getPluginName()] = _xsPluginItem
        else:
            self.__edConfiguration.setXSConfigurationItem(_xsPluginItem)


    @deprecated
    def getConfiguration(self):
        """
        Gets the Plugin Configuration as an XSPluginItem
        """
        self.DEBUG("EDPlugin.getConfiguration")
        return self.__edConfiguration.getXSConfigurationItem(self.getPluginName())
    configuration = property(getConfiguration, setConfiguration)


    def getConfig(self):
        """
        Gets the Plugin Configuration as a dictionary
        """
        self.DEBUG("EDPlugin.getConfig")
        return self.__edConfiguration.get(self.getPluginName(), {})

    def setConfig(self, _dict, _bLocal = False):
        """
        Receives a dictionary (Plugin Configuration) from the application.
        """
        self.DEBUG("EDPlugin.setConfiguration")
        if _bLocal:
            self.__edConfiguration = EDConfiguration()
        if _dict is not None:
            self.__edConfiguration[self.getPluginName()] = _dict
        else:
            self.__edConfiguration[self.getPluginName()] = {}
    config = property(getConfig, setConfig)


    @deprecated
    def getStringConfigurationParameterValue(self, _strConfigurationParameterName):
        """
        This method returns a configuration parameter value if a corresponding configuration
        parameter name can be found in the configuration file.
        
        If an application wide configuration file is provided via EDApplication it will
        override the product configuration file.
        
        The configuration parameter is then searched in the configration file in following order:
          - If a plugin configuration item exists and the configration parameter name is present it will be used.
          - Otherwise if a product-wide (e.g. "mxPluginExec") configuration value exists it will be used.         
        """
        strParameterValue = self.__edConfiguration.getStringValue(self.getPluginName(), _strConfigurationParameterName)
        self.DEBUG("EDPlugin.getConfigurationParameterValue: %s, %s = %s" % (self.getPluginName(),
                                                                             _strConfigurationParameterName,
                                                                             strParameterValue))
        return strParameterValue

    @deprecated
    def getDoubleConfigurationParameterValue(self, _strConfigurationParameterName):
        fParameterValue = None
        strParameterValue = self.getStringConfigurationParameterValue(_strConfigurationParameterName)
        try:
            return float(strParameterValue)
        except TypeError:
            return
        except ValueError:
            self.ERROR("float() argument must be a string or a number, got %s" % strParameterValue)


    @deprecated
    def getIntegerConfigurationParameterValue(self, _strConfigurationParameterName):
        iParameterValue = None
        strParameterValue = self.getStringConfigurationParameterValue(_strConfigurationParameterName)
        try:
            return int(strParameterValue)
        except TypeError:
            return
        except ValueError:
            self.ERROR("int() argument must be a string or a number, got %s" % strParameterValue)


    def configure(self):
        """
        Should be overridden by the Final Plugin If needed
        This method should set its proper members attributes from a Plugin configuration Object
        """
        self.DEBUG("EDPlugin.configure : plugin name = %s, EDNA_SITE = %s" % (self.getPluginName(), EDUtilsPath.EDNA_SITE))

        # set Timeout if different from default one
        if self.getTimeOut() == self.getDefaultTimeOut():
            # Try to get time out from plugin configuration
            iTimeOut = self.config.get(EDPlugin.CONF_TIME_OUT, None)
            if iTimeOut is not None:
                self.DEBUG("EDPlugin.configure: Setting time out to %d s from plugin configuration." % iTimeOut)
                self.setTimeOut(iTimeOut)
        else:
            self.DEBUG("EDPlugin.configure: timeout already set before plugin is configured.")
        # Base directory
        strBaseDirectory = self.getBaseDirectory()
        if (strBaseDirectory is None):
            # Try to get base directory from plugin configuration
            strBaseDirectory = self.config.get(EDPlugin.CONF_BASE_DIR_LABEL, None)
            if(strBaseDirectory is None):
                # Try to get working directory from environment variable
                strBaseDirectory = os.environ.get("EDNA_BASE_DIRECTORY")
                if (strBaseDirectory is None):
                    self.DEBUG("EDPlugin.configure: Using current base directory as working directory.")
                    strBaseDirectory = os.getcwd()
                else:
                    self.DEBUG("EDPlugin.configure: Setting base directory from $EDNA_WORKING_DIRECTORY.")
            else:
                if (strBaseDirectory == "."):
                    self.DEBUG("EDPlugin.configure: Using current base directory as working directory.")
                    strBaseDirectory = os.getcwd()
                else:
                    strBaseDirectory = os.path.abspath(strBaseDirectory)
                    self.DEBUG("EDPlugin.configure: Setting base directory from plugin configuration.")
            self.setBaseDirectory(strBaseDirectory)
        else:
            self.DEBUG("EDPlugin.configure: Base directory already set before plugin is configured.")
        # Working directory
        strWorkingDirectory = self.getWorkingDirectory()
        if (strWorkingDirectory is None):
            # Try to get working directory from plugin configuration
            strWorkingDirectory = self.config.get(EDPlugin.CONF_WORKING_DIR_LABEL, None)
            if(strWorkingDirectory is not None):
                self.DEBUG("EDPlugin.configure: Setting working directory from plugin configuration.")
            else:
                self.DEBUG("EDPlugin.configure: Setting working directory as base directory + base name.")
                strWorkingDirectory = os.path.join(self.getBaseDirectory(), self.getBaseName())
            self.setWorkingDirectory(strWorkingDirectory)
        else:
            self.DEBUG("EDPlugin.configure: Working directory already set before plugin is configured.")
        #
        self.__bWriteDataXMLInputOutput = bool(self.config.get(self.CONF_WRITE_XML_INPUT_OUTPUT, True))
        self.__bWriteDataXMLOutput = bool(self.config.get(self.CONF_WRITE_XML_OUTPUT, True))
        self.__bWriteDataXMLInput = bool(self.config.get(self.CONF_WRITE_XML_INPUT, True))


    def execute(self, _edObject=None):
        # Configure the plugin before starting it's thread
        self.configure()
        EDAction.execute(self, _edObject)


    def checkParameters(self):
        """
        Should be overridden by the Final Plugin If needed
        This method should check that the data input are consistent
        """
        self.DEBUG("EDPlugin.checkParameters")


    def setXSDataInputClass(self, _xsDataInputClass, _strDataInputKey=None):
        """
        This method should be called in the constructor of the derived plugins
        in order to set the XSData type of the input data, e.g. XSDataInputXXX
        """
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        if (strDataInputKey in self.__dictXSDataInputClass.keys()):
            strErrorMessage = "ERROR: " + self.getPluginName() + ".setXSDataInputClass, Data Input Class already defined for key: " + strDataInputKey
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        self.__dictXSDataInputClass[ strDataInputKey ] = _xsDataInputClass


    def getXSDataInputClass(self, _strDataInputKey=None):
        """
        Returns the XSData type of the input data.
        """
        pyXSDataInputClass = None
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        if (strDataInputKey in self.__dictXSDataInputClass.keys()):
            pyXSDataInputClass = self.__dictXSDataInputClass[ strDataInputKey ]
        return pyXSDataInputClass


    def setDataInput(self, _oDataInput, _strDataInputKey=None):
        """
        Sets the plugin input data.
        _oDataInput could be either an String XML or an XSData object.

        The input data is stored in a dictionary with the key _strDataInputKey.
        If the key is not provided a default key is used.

        If not data input class is defined for the key an exception is raised.
        
        If the key is not the default key, the data object is added to a list which 
        might contain already stored object(s).
        
        If _oDataInput is None the list corresponding to a keyword is deleted.
        """
        self.DEBUG("EDPlugin.setDataInput")
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        # Allow for None input
        if (_oDataInput is None):
            self.DEBUG("EDPlugin.setDataInput: Data input is None")
            self.__dictXSDataInput[ strDataInputKey ] = []
        elif (self.getXSDataInputClass(strDataInputKey) is None):
            strErrorMessage = "ERROR: " + self.getPluginName() + ".setDataInput, Data Input Class not defined for key: " + strDataInputKey
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        else:
            # Check the type
            xsDataInput = None
            if isinstance(_oDataInput, (str, unicode)):
                self.DEBUG("EDPlugin.setDataInput: Input Data is string ")
                xsDataInput = self.getXSDataInputClass(strDataInputKey).parseString(_oDataInput)
            elif (isinstance(_oDataInput, self.getXSDataInputClass(strDataInputKey))):
                self.DEBUG("EDPlugin.setDataInput: Input Data is of type " + str(_oDataInput.__class__))
                xsDataInput = _oDataInput
            else:
                strErrorMessage = "ERROR: %s.setDataInput, wrong data type %r for data input key: %s, expected XML string or %r" % \
                                  (self.getPluginName(), _oDataInput.__class__, strDataInputKey, self.getXSDataInputClass(strDataInputKey))
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            # Add the object to a list if its key is not the default key
            if (strDataInputKey != self.__strDefaultInputDataKey) :
                # Check if there's already a list stored
                if (not strDataInputKey in self.__dictXSDataInput.keys()):
                    self.__dictXSDataInput[ strDataInputKey ] = []
                self.__dictXSDataInput[ strDataInputKey ].append(xsDataInput)
            else:
                self.__dictXSDataInput[ strDataInputKey ] = xsDataInput


    def hasDataInput(self, _strDataInputKey=None):
        """
        Returns True if the plugin has Input Data for a particular key.
        If the key is not provided a default key is used.
        """
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        if (strDataInputKey in self.__dictXSDataInput.keys()):
            return True
        else:
            return False


    def getDataInput(self, _strDataInputKey=None):
        """
        Returns the Plugin Input Data for a particular key.
        If the key is not provided a default key is used.
        """
        oValue = None
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        if (strDataInputKey in self.__dictXSDataInput.keys()):
            oValue = self.__dictXSDataInput[ strDataInputKey ]
        else:
            strErrorMessage = self.getPluginName() + ".getDataInput, no input data defined for key: " + strDataInputKey
            self.warning(strErrorMessage)
            self.addWarningMessage(strErrorMessage)
        return oValue


    def delDataInput(self, _strDataInputKey=None):
        """
        Deletes the data input for a particular key.
        If the key is not provided a default key is used.
        """
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.__strDefaultInputDataKey
        if (strDataInputKey in self.__dictXSDataInput.keys()):
            self.__dictXSDataInput[ strDataInputKey ] = None
        else:
            strErrorMessage = self.getPluginName() + ".delDataInput, no input data defined for key: " + strDataInputKey
            self.warning(strErrorMessage)
            self.addWarningMessage(strErrorMessage)

    # Property for dataInput
    dataInput = property(getDataInput, setDataInput, delDataInput, "Property for dataInput")


    def setDataOutput(self, _xsDataOutput, _strDataOutputKey=None):
        """
        Sets the plugin output data for a particular key.
        If the key is not provided a default key is used.

        If the key is already defined in the dictionary, the corresponding
        data object is added to a list which contains the already stored object(s).
        """
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.__strDefaultOutputDataKey
        # Add the object to a list if its key not the default key 
        if (strDataOutputKey == self.__strDefaultOutputDataKey):
            self.__dictXSDataOutput[ strDataOutputKey ] = _xsDataOutput
        else:
            # Check if the _xsDataoutput object is already a list
            if (type(_xsDataOutput) == types.ListType):
                self.__dictXSDataOutput[ strDataOutputKey ] = _xsDataOutput
            else:
                # Check if the stored object contains already a list
                if (not strDataOutputKey in self.__dictXSDataOutput.keys()):
                    self.__dictXSDataOutput[ strDataOutputKey ] = []
                self.__dictXSDataOutput[ strDataOutputKey ].append(_xsDataOutput)


    def getDataOutput(self, _strDataOutputKey=None):
        """
        Returns the Plugin Output Data
        """
        oValue = None
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.__strDefaultOutputDataKey
        if (strDataOutputKey in self.__dictXSDataOutput.keys()):
            oValue = self.__dictXSDataOutput[ strDataOutputKey ]
        return oValue


    def hasDataOutput(self, _strDataOutputKey=None):
        """
        Returns True if the plugin has the specified Output Data
        """
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.__strDefaultOutputDataKey
        if (strDataOutputKey in self.__dictXSDataOutput.keys()):
            return True
        else:
            return False


    def delDataOutput(self, _strDataOutputKey=None):
        """
        Deletes the data output for a particular key.
        If the key is not provided a default key is used.
        """
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.__strDefaultOutputDataKey
        if (strDataOutputKey in self.__dictXSDataOutput.keys()):
            self.__dictXSDataOutput[ strDataOutputKey ] = None
        else:
            strErrorMessage = self.getPluginName() + ".delDataOutput, no output data defined for key: " + _strDataOutputKey
            self.warning(strErrorMessage)
            self.addWarningMessage(strErrorMessage)

    # Property for dataOutput
    dataOutput = property(getDataOutput, setDataOutput, delDataOutput, "Property for dataOutput")


    def exportDataOutput(self, _edPlugin=None):
        """
        Deprecated
        Exports the Plugin Output Data to slot
        """
        self.DEBUG("EDPlugin.exportDataOutput")
        self.__edSlotExportDataOutput.call(self.__dictXSDataOutput)


    def connectExportDataOutput(self, _oMethod):
        """
        Deprecated
        """
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotExportDataOutput.connect(_oMethod)
        self.synchronizeOff()


    def generateExecutiveSummary(self, _edPlugin):
        """
        This method, which should be implemented by sub-classes, generates an executive summary (user-related output summary).
        """
        self.DEBUG("EDPlugin.generateExecutiveSummary")


    def addErrorMessage(self, _strErrorMessage):
        """
        Adds an error message to the error messages list
        """
        self.__listErrorMessages.append(_strErrorMessage)


    def getErrorMessages(self):
        """
        Returns the error messages list
        OBS! This method is deprecated, please use getListOfErrorMessages instead.
        """
        self.warning("Deprecation by Monday 7th June 2010 of EDPlugin, called getErrorMessages")
        from EDImportLib import EDList
        return EDList(self.__listErrorMessages)


    def getListOfErrorMessages(self):
        """
        Returns the error messages list
        """
        return self.__listErrorMessages


    def addWarningMessage(self, _strWarningMessage):
        """
        Adds a warning message to the warning messages list
        """
        self.DEBUG("EDPlugin.addWarningMessage : " + _strWarningMessage)
        self.__listWarningMessages.append(_strWarningMessage)


    def getWarningMessages(self):
        """
        Returns the warning messages list
        OBS! This method is deprecated, please use getListOfWarningMessages instead.
        """
        self.warning("Deprecation by Monday 7th June 2010 of EDPlugin, called getWarningMessages")
        from EDImportLib import EDList
        return EDList(self.__listWarningMessages)


    def getListOfWarningMessages(self):
        """
        Returns the warning messages list
        """
        return self.__listWarningMessages


    def writeDataInput(self, _edObject=None):
        """
        Writes the input data object(s) into a working dir xml file 
        """
        self.DEBUG("EDPlugin.writeDataInput")
        strBasename = os.path.join(self.getWorkingDirectory(), self.compactPluginName(self.getPluginName()))
        for strKey in self.__dictXSDataInput.keys():
            if (strKey == self.__strDefaultInputDataKey):                # "Old" style
                xsDataInput = self.__dictXSDataInput[ self.__strDefaultInputDataKey ]
                self.strPathDataInput = strBasename + "_dataInput.xml"
                EDUtilsFile.writeFile(self.strPathDataInput, xsDataInput.marshal())
            else:                                                       # We have a list of objects
                listXSDataInput = self.__dictXSDataInput[ strKey ]
                for iIndex, xsDataInput in enumerate(listXSDataInput):
                    strPathDataInput = "%s_%s_%d_dataInput.xml" % (strBasename, strKey, iIndex)
                    EDUtilsFile.writeFile(strPathDataInput, xsDataInput.marshal())


    def writeDataOutput(self, _edObject=None):
        """
        Writes the output data object(s) into a working dir xml file 
        """
        self.DEBUG("EDPlugin.writeDataOutput")
        for strKey in self.__dictXSDataOutput.keys():
            if (strKey == self.__strDefaultOutputDataKey):                # "Old" style
                xsDataOutput = self.__dictXSDataOutput[ self.__strDefaultOutputDataKey ]
                if (xsDataOutput is not None):
                    self.strPathDataOutput = os.path.join(self.getWorkingDirectory(), self.compactPluginName(self.getPluginName()) + "_dataOutput.xml")
                    EDUtilsFile.writeFile(self.strPathDataOutput, xsDataOutput.marshal())
            else:
                listXSDataOutput = self.__dictXSDataOutput[ strKey ]
                for iIndex, xsDataOutput in enumerate(listXSDataOutput):
                    if (xsDataOutput is not None):
                        strPathDataOutput = os.path.join(self.getWorkingDirectory(), self.compactPluginName(self.getPluginName()) + "_" + strKey + "_%d_dataOutput.xml" % iIndex)
                        EDUtilsFile.writeFile(strPathDataOutput, xsDataOutput.marshal())


    def getBaseName(self):
        """
        Returns the plugin base name
        """
        if (self.__strBaseName is None):
            self.__strBaseName = self.createBaseName()
        return self.__strBaseName


    def setBaseName(self, _strBaseName):
        """
        Sets the plugin base name
        """
        self.__strBaseName = self.compactPluginName(_strBaseName)
        self.setName(self.__strBaseName)
        # Create the directory baseDirectory/baseName which will be used as working directory
        strWorkingDirPath = os.path.join(self.getBaseDirectory(), self.__strBaseName)
        if not os.path.isdir(strWorkingDirPath):
            os.mkdir(strWorkingDirPath)
        self.setWorkingDirectory(strWorkingDirPath)


    def createBaseName(self):
        """
        Generates the plugin base name: (<prefix>-<object ID>)
        """
        # First try to use global instance ID from EDObject
        strBaseName = "%s-%08d" % (self.compactPluginName(self.getPluginName()), self.getId())
        strBaseDir = os.path.join(self.getBaseDirectory(), strBaseName)
        # Try to create the directory...
        try:
            os.mkdir(strBaseDir)
        except BaseException, strErrorDetail:
            self.error("EDPlugin.createBaseName: Could not create base directory %s because of %s" % (strBaseDir, strErrorDetail))
            self.warning("EDPlugin.createBaseName: Trying to create alternative base directory...")
            self.writeErrorTrace()
            strTempDir = tempfile.mkdtemp(prefix=strBaseName, dir=self.getBaseDirectory())
            os.chmod(strTempDir, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            strBaseName = os.path.split(strTempDir)[1]
            strBaseDir = os.path.join(self.getBaseDirectory(), strBaseName)
            self.warning("EDPlugin.createBaseName: Alternative base directory created: %s" % strBaseDir)
        self.DEBUG("EDPlugin.createBaseName : Directory created = " + strBaseDir)
        return strBaseName


    def compactPluginName(self, _pluginName):
        """
        The prefix is constructed from the plugin name with the following renaming:
        EDPlugin -> ""
        EDPluginExec -> ""
        EDPluginControl -> "Control"
        """
        strCompactName = _pluginName
        if (strCompactName.startswith("EDPluginExec")):
            strCompactName = strCompactName[12:]
        elif (strCompactName.startswith("EDPluginControl")):
            strCompactName = strCompactName[8:]
        elif (strCompactName.startswith("EDPlugin")):
            strCompactName = strCompactName[8:]
        return strCompactName


    def setBaseDirectory(self, _strBaseDirectory):
        """
        Sets the plugin base directory
        """
        self.DEBUG("EDPlugin.setBaseDirectory : " + _strBaseDirectory)
        if (not os.path.isdir(_strBaseDirectory)):
            self.DEBUG("EDPlugin.setBaseDirectory: base directory %s does dot yet exist! Creating it." % _strBaseDirectory)
            os.mkdir(_strBaseDirectory)
        self.__strBaseDirectory = _strBaseDirectory


    def getBaseDirectory(self):
        """
        Returns the plugin base directory
        """
        self.DEBUG("EDPlugin.getBaseDirectory : %s" % self.__strBaseDirectory)
        if (self.__strBaseDirectory is None):
            self.__strBaseDirectory = os.getcwd()
        return self.__strBaseDirectory


    def setWorkingDirectory(self, _strWorkingDirectory):
        """
        Sets the plugin working directory
        """
        self.DEBUG("EDPlugin.setWorkingDirectory : " + _strWorkingDirectory)
        self.__strWorkingDirectory = _strWorkingDirectory
        if not os.path.isdir(_strWorkingDirectory):
            self.DEBUG("EDPlugin.setWorkingDirectory, creating working directory %s." % _strWorkingDirectory)
            os.mkdir(self.__strWorkingDirectory)


    def getWorkingDirectory(self):
        """
        Returns the plugin base directory
        """
        self.DEBUG("EDPlugin.getWorkingDirectory : %s" % self.__strWorkingDirectory)
        returnValue = None
        if (self.__strWorkingDirectory is not None):
            returnValue = self.__strWorkingDirectory
        return returnValue


    def checkMandatoryParameters(self, _xsData, _strParamName):
        """
        Checks that a mandatory parameter exists in the data
        If not, an error message is added in the list and the plugin fails
        """
        if _xsData is None or (hasattr(_xsData, '__len__') and len(_xsData) == 0):
            strErrorMessage = "%s: input parameter is missing: %s" % (self.getPluginName(), _strParamName)
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage


    def checkImportantParameters(self, _xsData, _strParamName):
        """
        Checks that a specific parameter exists in the data
        If not, a warning message is added in the list
        """
        if(_xsData == None):
            strWarningMessage = "%s: input parameter is missing: %s" % (self.getPluginName(), _strParamName)
            self.warning(strWarningMessage)
            self.addWarningMessage(strWarningMessage)


    def addExecutiveSummaryLine(self, _strExecutiveSummaryLine):
        """
        Add a line to the executive summary string.
        """
        self.DEBUG("EDPlugin.addExecutiveSummaryLine : %r" % _strExecutiveSummaryLine)
        strExecutiveSummaryLine = _strExecutiveSummaryLine
        if (not strExecutiveSummaryLine == ""):
            if (strExecutiveSummaryLine[-1] == "\n"):
                strExecutiveSummaryLine = strExecutiveSummaryLine[:-1]
        self.__listExecutiveSummaryLines.append(strExecutiveSummaryLine)


    def addExecutiveSummarySeparator(self, _strSeparator=None):
        """
        Adds a separator to split the executive summary into different parts
        Default is a dotted line
        """
        strSeparator = _strSeparator
        if (strSeparator is None):
            strSeparator = self.__strExecutiveSummarySeparator
        # Check that the last line doesn't already contain a separator
        if self.__listExecutiveSummaryLines != []:
            if self.__listExecutiveSummaryLines[-1] != strSeparator:
                self.addExecutiveSummaryLine(strSeparator)
        else:
            self.addExecutiveSummaryLine(strSeparator)


    def getListExecutiveSummaryLines(self):
        """
        Returns the executive summary (list of text lines)
        """
        return self.__listExecutiveSummaryLines


    def verboseScreenExecutiveSummary(self):
        """
        Prints the executive summary on the screen
        """
        for line in self.getListExecutiveSummaryLines():
            self.screen(line)

    def verboseDebug(self, _strMessage):
        self.DEBUG(self.getPluginName() + " : " + _strMessage)


    def getPluginName(self):
        return self.getClassName()


    def getListOfDataInputKeys(self):
        return self.__dictXSDataInput.keys()


    def getListOfDataOutputKeys(self):
        return self.__dictXSDataOutput.keys()


    def getDefaultInputDataKey(self):
        return self.__strDefaultInputDataKey


    def getDefaultOutputDataKey(self):
        return self.__strDefaultOutputDataKey


    def getExecutiveSummarySeparator(self):
        return self.__strExecutiveSummarySeparator


    def isRequiredToHaveConfiguration(self):
        """
        If the return value from this method is true, the plugin 
        is required to have a configuration in order to be executed in a
        plugin execution test case.
        @return: RequiredToHaveConfiguration
        @rtype: boolean
        """
        return self.__isRequiredToHaveConfiguration


    def setRequiredToHaveConfiguration(self, _bValue=True):
        """
        Sets or unsets the plugin to be required to have a configuration
        for execution in a plugin execution test case.
        plugin execution test case.
        @param _bValue: RequiredToHaveConfiguration
        @type: boolean
        """
        self.__isRequiredToHaveConfiguration = _bValue


    def setWriteXMLInputOutput(self, _bValue=True):
        """
        Sets or unsets the plugin to write XML input and output files.
        @param _bValue: WriteDataXMLInputOutput
        @type: boolean
        """
        self.__bWriteDataXMLInputOutput = _bValue

    def setWriteXMLInput(self, _bValue=True):
        """
        Sets or unsets the plugin to write XML input  files.
        @param _bValue: WriteDataXMLInput
        @type: boolean
        """
        self.__bWriteDataXMLInput = _bValue

    def setWriteXMLOutput(self, _bValue=True):
        """
        Sets or unsets the plugin to write XML  output files.
        @param _bValue: WriteDataXMLOutput
        @type: boolean
        """
        self.__bWriteDataXMLOutput = _bValue


    def setUseWarningInsteadOfError(self, _bValue=True):
        """
        Sets or unsets the plugin to use warning messages also for error messages.
        @param _bValue: UseWarningInsteadOfError
        @type: boolean
        """
        self.__bUseWarningInsteadOfError = _bValue

    def error(self, _strErrorMessage):
        """
        Overloaded from EDLogging. If self.__bUseWarningInsteadOfError is True
        a warning message is issued instead of an error message.
        """
        if self.__bUseWarningInsteadOfError:
            self.warning(_strErrorMessage)
        else:
            EDAction.error(self, _strErrorMessage)

    def ERROR(self, _strErrorMessage):
        """
        Uses the overloaded self.error method above.
        """
        self.error(_strErrorMessage)
