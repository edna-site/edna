# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (jerome.kieffer@esrf.fr)
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"

import types

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDUtilsPath                         import EDUtilsPath
from EDTestCasePlugin                    import EDTestCasePlugin
from EDFactoryPluginStatic               import EDFactoryPluginStatic
from EDUtilsFile                         import EDUtilsFile
from EDUtilsParallel                     import EDUtilsParallel

class EDTestCasePluginExecute(EDTestCasePlugin):
    """
    This is the main class for all Plugin Execution tests
    """

    def __init__(self, _strPluginName, _strPluginDir=None, _strTestName=None):
        """ 
        Initialise the Plugin Execution test
            - Edna site
            - Configuration files
            - Data input file
            - Plugin launcher
        """
        EDTestCasePlugin.__init__(self, _strPluginName, _strPluginDir, _strTestName)
        self._strRefConfigFile = None
        self._dictStrDataInputFiles = {}
        self._strDefaultInputDataKey = "defaultInputData"
        self._dictStrReferenceDataOutputFiles = {}
        self._strDefaultOutputDataKey = "defaultOutputData"
        self._iNoExpectedErrorMessages = 0
        self._iNoExpectedWarningMessages = 0
        self._bAcceptPluginFailure = False
        # Deprecated!
        self.m_edObtainedOutputDataFile = None
        EDUtilsParallel.uninitializeNbThread()


    def preProcess(self):
        """
        Initialize the plugin to be launched
        """
        EDTestCasePlugin.preProcess(self)
        if(EDUtilsPath.EDNA_SITE == None):
            raise RuntimeError, "EDNA_SITE must be set"
        # Load the plugin that should be executed
        self._edPlugin = EDFactoryPluginStatic.loadPlugin(self.getPluginName())
        if(self._edPlugin is not None):
            for strInputDataKey in self._dictStrDataInputFiles.keys():
                if (type(self._dictStrDataInputFiles[ strInputDataKey ]) == types.ListType):
                    for strDataInputFile in self._dictStrDataInputFiles[ strInputDataKey ]:
                        strXMLData = self.readAndParseFile(strDataInputFile)
                        if (strInputDataKey == self._strDefaultInputDataKey):
                            self._edPlugin.setDataInput(strXMLData)
                        else:
                            self._edPlugin.setDataInput(strXMLData, strInputDataKey)
                else:
                    strXMLData = self.readAndParseFile(self._dictStrDataInputFiles[ strInputDataKey ])
                    if (strInputDataKey == self._strDefaultInputDataKey):
                        self._edPlugin.setDataInput(strXMLData)
                    else:
                        self._edPlugin.setDataInput(strXMLData, strInputDataKey)
            #self._edPlugin.setDataInput( self._strXMLData, "inputMXCuBE" )
        else:
            EDVerbose.ERROR("Cannot load plugin: %s" % self.getPluginName())
            raise RuntimeError
        self._edPlugin.setConfig(self.getPluginConfig())


    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)


    def getErrorMessages(self):
        """
        Returns the error messages for the plugin launcher
        """
        return self._edPlugin.getErrorMessages()
    errorMessages = property(getErrorMessages, doc="read-only only property")


    def getWarningMessages(self):
        """
        Returns the warning messages for the plugin launcher
        """
        return self._edPlugin.getWarningMessages()
    warningMessages = property(getWarningMessages, doc="read-only only property")


    def getRefConfigFile(self):
        """
        Returns the reference configuration file (from edna/conf directory)
        """
        return self._strRefConfigFile


    def setDataInputFile(self, _strDataInputFile, _strDataInputKey=None):
        """
        Sets the data input file
        """
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self._strDefaultInputDataKey
        if (strDataInputKey == self._strDefaultInputDataKey):
            # Do not create a list for the default key, just replace the existing value
            self._dictStrDataInputFiles[ strDataInputKey ] = _strDataInputFile
        else:
            if (not strDataInputKey in self._dictStrDataInputFiles.keys()):
                self._dictStrDataInputFiles[ strDataInputKey ] = []
            self._dictStrDataInputFiles[ strDataInputKey ].append(_strDataInputFile)


    def getDataInputFile(self, _strDataInputKey=None):
        """
        Returns the data input file
        """
        strDataInputFile = None
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self._strDefaultInputDataKey
        if (strDataInputKey in self._dictStrDataInputFiles.keys()):
            strDataInputFile = self._dictStrDataInputFiles[ strDataInputKey ]
        else:
            strErrorMessage = "ERROR: " + str(self.__class__) + ".setDataInputFile, no data input file defined for key: " + strDataInputKey
            EDVerbose.error(strErrorMessage)
            raise RuntimeError, strErrorMessage
        return strDataInputFile



    def setReferenceDataOutputFile(self, _strReferenceDataOutputFile, _strDataOutputKey=None):
        """
        Sets the data input file
        """
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self._strDefaultOutputDataKey
        if (strDataOutputKey == self._strDefaultOutputDataKey):
            # Do not create a list for the default key, just replace the existing value
            self._dictStrReferenceDataOutputFiles[ strDataOutputKey ] = _strReferenceDataOutputFile
        else:
            if (not strDataOutputKey in self._dictStrReferenceDataOutputFiles.keys()):
                self._dictStrReferenceDataOutputFiles[ strDataOutputKey ] = []
            self._dictStrReferenceDataOutputFiles[ strDataOutputKey ].append(_strReferenceDataOutputFile)


    def getReferenceDataOutputFile(self, _strDataOutputKey=None):
        """
        Returns the data input file
        """
        strReferenceDataOutputFile = None
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self._strDefaultOutputDataKey
        if (strDataOutputKey in self._dictStrReferenceDataOutputFiles.keys()):
            strReferenceDataOutputFile = self._dictStrReferenceDataOutputFiles[ strDataOutputKey ]
        else:
            strErrorMessage = "ERROR: " + str(self.__class__) + ".getReferenceDataOutputFile, no data output file defined for key: " + strDataOutputKey
            EDVerbose.error(strErrorMessage)
            raise RuntimeError, strErrorMessage
        return strReferenceDataOutputFile


    def getEdnaSite(self):
        """
        Returns the EDNA_SITE environment variable
        """
        return EDUtilsPath.EDNA_SITE


    def run(self):
        """
        Executes the plugin and checks that the data output is not None
        """
        EDVerbose.DEBUG("EDTestCasePluginExecute: Executing " + self.getPluginName())
        self._edPlugin.executeSynchronous()
        # Check that the plugin didn't end in failure
        EDAssert.equal(self._bAcceptPluginFailure , self._edPlugin.isFailure(), \
                       "Plugin failure assert: should be %r, was %r" % (self._bAcceptPluginFailure , self._edPlugin.isFailure()))
        # Checks the number of error messages
        EDAssert.equal(self._iNoExpectedErrorMessages, len(self._edPlugin.getListOfErrorMessages()), \
                           "Number of error messages: expected %d, got %d" % (self._iNoExpectedErrorMessages, len(self._edPlugin.getListOfErrorMessages())))
        # Checks the number of warning messages
        EDAssert.equal(self._iNoExpectedWarningMessages, len(self._edPlugin.getListOfWarningMessages()), \
                           "Number of warning messages: expected %d, got %d" % (self._iNoExpectedWarningMessages, len(self._edPlugin.getListOfWarningMessages())))
        # Check the output data
        listOfDataOutputKeys = self._edPlugin.getListOfDataOutputKeys()
        for strReferenceOutputDataKey in self._dictStrReferenceDataOutputFiles.keys():
            # Only check the reference data keys
            if (strReferenceOutputDataKey in listOfDataOutputKeys):
                EDVerbose.unitTest("Testing data output for %s" % strReferenceOutputDataKey)
                listReferenceFile = self._dictStrReferenceDataOutputFiles[ strReferenceOutputDataKey ]
                if (type(listReferenceFile) != types.ListType):
                    listReferenceFile = [ listReferenceFile ]
                listReferenceOutput = []
                for strReferenceFile in listReferenceFile:
                    listReferenceOutput.append(self.readAndParseFile(strReferenceFile))
                # Obtained output
                listObtainedOutputXML = []
                pyObjectObtainedDataOutput = self._edPlugin.getDataOutput(strReferenceOutputDataKey)
                listObtainedOutput = None
                if (type(pyObjectObtainedDataOutput) == types.ListType):
                    listObtainedOutput = pyObjectObtainedDataOutput
                else:
                    listObtainedOutput = [ pyObjectObtainedDataOutput ]
                for xsDataOutput in listObtainedOutput:
                    listObtainedOutputXML.append(xsDataOutput.marshal())
                # Compare the lists, sort them first
                listReferenceOutput.sort()
                listObtainedOutputXML.sort()
                for iIndex in range(len(listReferenceOutput)):
                    # Check of deprecated tests - if default data key only warn
                    if (strReferenceOutputDataKey == self._strDefaultOutputDataKey):
                        if (listReferenceOutput[ iIndex ] != listObtainedOutputXML[ iIndex ]):
                            EDVerbose.unitTest("WARNING! Expected output is not corresponding to obtained output.")
                    else:
                        EDAssert.equal(listReferenceOutput[ iIndex ], listObtainedOutputXML[ iIndex ])
                # Legacy - save output data
                if (strReferenceOutputDataKey == self._strDefaultOutputDataKey):
                    if (self.m_edObtainedOutputDataFile is None):
                        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"
                    EDUtilsFile.writeFile(self.m_edObtainedOutputDataFile, self._edPlugin.getDataOutput().marshal())


    def setNoExpectedWarningMessages(self, _iNoExpectedWarningMessages):
        self._iNoExpectedWarningMessages = _iNoExpectedWarningMessages


    def setNoExpectedErrorMessages(self, _iNoExpectedErrorMessages):
        self._iNoExpectedErrorMessages = _iNoExpectedErrorMessages


    def setAcceptPluginFailure(self, _bValue):
        self._bAcceptPluginFailure = _bValue
