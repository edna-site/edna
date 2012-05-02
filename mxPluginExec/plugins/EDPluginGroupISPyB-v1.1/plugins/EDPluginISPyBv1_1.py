#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:  Marie-Francoise Incardona (incardon@esrf.fr)
#                           Olof Svensson (svensson@esrf.fr) 
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

from EDPluginExec       import EDPluginExec
from EDVerbose          import EDVerbose
from EDMessage          import EDMessage
from EDConfiguration    import EDConfiguration
from EDUtilsXML         import EDUtilsXML

from XSDataCommon   import XSData
from XSDataCommon   import XSDataInteger
from XSDataCommon   import XSDataString

from XSDataISPyBv1_1 import XSDataISPyBImage
from XSDataISPyBv1_1 import XSDataISPyBScreening
from XSDataISPyBv1_1 import XSDataISPyBScreeningInput
from XSDataISPyBv1_1 import XSDataISPyBScreeningOutput
from XSDataISPyBv1_1 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_1 import XSDataISPyBScreeningRank
from XSDataISPyBv1_1 import XSDataISPyBScreeningRankSet
from XSDataISPyBv1_1 import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_1 import XSDataInputISPyB
from XSDataISPyBv1_1 import XSDataResultISPyB
from XSDataISPyBv1_1 import XSDataResultStatus
from XSDataISPyBv1_1 import XSDatadbstatus

from EDImportSystem import PyHttplib
from EDImportSystem import PyOs
from EDImportSystem import PyString
from EDImportSystem import PySocket

class EDPluginISPyBv1_1(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using the DNA/ISPyB dbserver 
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyB)
        self.m_edStrDbserverHost = "localhost"
        self.m_iDbserverPort = 9090

    def getDbserverHost(self):
        return self.m_edStrDbserverHost

    def setDbserverHost(self, _edStrDbserverHost):
        self.m_edStrDbserverHost = _edStrDbserverHost

    def getDbserverPort(self):
        return self.m_iDbserverPort

    def setDbserverPort(self, _iDbserverPort):
        self.m_iDbserverPort = _iDbserverPort

    def configure(self):
        """
        Gets the dbserver parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            EDVerbose.DEBUG("*** EDPluginISPyBv1_1.configure: pluginConfiguration is None, using default settings")
        else:
            EDVerbose.DEBUG("*** EDPluginISPyBv1_1.configure: pluginConfiguration found, using settings from there")
            pyStrDbserverHost = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverHost")
            if(pyStrDbserverHost == None):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverHost")
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            else:
                self.setDbserverHost(pyStrDbserverHost)

            pyStrDbserverPort = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverPort")
            if(pyStrDbserverPort == None):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverPort")
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            else:
                self.setDbserverPort(int (pyStrDbserverPort))

    def process(self, _edObject=None):
        """
        Sends a store request and the screening object to the dbserver. Returns success or failure.
        
        Note that:
        * Any objects referred to by the object returned by self.getDataInput() will be stored. 
        * Primary key attributes should not be set.
        * If a foreign key attribute is not set, this method will attempt to find the foreign object among those 
        referred to by the self.getDataInput() object, and use the primary key attribute of this object when it 
        has been stored. If such an object is not found, the method fails.
        * The method will not attempt to store any more objects once an error is encountered
        """

        EDPluginExec.process(self)
        EDVerbose.DEBUG("*** EDPluginISPyBv1_1.process")

        xsDataInputISPyB = self.getDataInput()
        self.m_xsDataResultISPyB = XSDataResultISPyB()

        xsDataISPyBScreening = xsDataInputISPyB.getScreening()
        if xsDataISPyBScreening == None:
            xsDataISPyBScreening = XSDataISPyBScreening()

        xsDataISPyBImage = xsDataInputISPyB.getImage()

        if xsDataISPyBScreening.getDataCollectionId() == None:
            if ((xsDataISPyBImage == None) or (xsDataISPyBImage.getFileName() == None) or (xsDataISPyBImage.getFileLocation() == None)):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "process", \
                                                                     "Neither a dataCollectionId nor a image filename + path are provided.")
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                return

            pyStrXML = EDUtilsXML.dnaMarshal(xsDataISPyBImage)

            # Send the XML to request the dataCollectionId from the dbserver:
            pyStrResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/get_datacollectionid", pyStrXML)

            if pyStrResponse != None:
                # Handle response:
                xsDatadbstatus = XSDatadbstatus.parseString(pyStrResponse)
                pyStrCode = xsDatadbstatus.getCode()
                pyStrMessage = xsDatadbstatus.getMessage()
                EDVerbose.DEBUG("dbserver returns code: " + pyStrCode)
                EDVerbose.DEBUG("dbserver returns message: " + pyStrMessage)

                if (pyStrCode == "error") or (xsDatadbstatus.getDataCollectionId() == -1):
                    if xsDatadbstatus.getDataCollectionId() == -1:
                        pyStrMessage = "An image corresponding to the given fileName and fileLocation was not found."
                    pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "process", pyStrMessage)
                    EDVerbose.error(pyStrErrorMessage)
                    self.addErrorMessage(pyStrErrorMessage)
                    return

                if xsDatadbstatus.getDataCollectionId() != -1:
                    xsDataISPyBScreening.setDataCollectionId(XSDataInteger(xsDatadbstatus.getDataCollectionId()))
                    self.m_xsDataResultISPyB.setDataCollectionId(XSDataInteger(xsDatadbstatus.getDataCollectionId()))

        xsDataISPyBScreeningInputs = xsDataInputISPyB.getScreeningInput()
        xsDataISPyBScreeningOutputContainers = xsDataInputISPyB.getScreeningOutputContainer()
        xsDataISPyBScreeningRanks = xsDataInputISPyB.getScreeningRank()
        xsDataISPyBScreeningRankSet = xsDataInputISPyB.getScreeningRankSet()

        xsDataIntegerScreeningId = self.store(xsDataISPyBScreening)

        if xsDataISPyBScreeningInputs != None:
            for xsDataISPyBScreeningInput in xsDataISPyBScreeningInputs:
                xml = xsDataISPyBScreeningInput.marshal()
                xsDataISPyBScreeningInput.setScreeningId(xsDataIntegerScreeningId)
                self.store(xsDataISPyBScreeningInput)

        if xsDataISPyBScreeningRankSet != None:
            xsDataIntegerScreeningRankSetId = self.store(xsDataISPyBScreeningRankSet)

            for xsDataISPyBScreeningRank in xsDataISPyBScreeningRanks:
                xsDataISPyBScreeningRank.setScreeningId(xsDataIntegerScreeningId)
                xsDataISPyBScreeningRank.setScreeningRankSetId(xsDataIntegerScreeningRankSetId)
                self.store(xsDataISPyBScreeningRank)

        if xsDataISPyBScreeningOutputContainers != None:
            for xsDataISPyBScreeningOutputContainer in xsDataISPyBScreeningOutputContainers:
                xsDataISPyBScreeningOutput = xsDataISPyBScreeningOutputContainer.getScreeningOutput()
                xsDataISPyBScreeningOutput.setScreeningId(xsDataIntegerScreeningId)
                xsDataIntegerScreeningOutputId = self.store(xsDataISPyBScreeningOutput)

            xsDataISPyBScreeningOutputLattices = xsDataISPyBScreeningOutputContainer.getScreeningOutputLattice()
            if xsDataISPyBScreeningOutputLattices != None:
                for xsDataISPyBScreeningOutputLattice in xsDataISPyBScreeningOutputLattices:
                    xsDataISPyBScreeningOutputLattice.setScreeningOutputId(xsDataIntegerScreeningOutputId)
                    self.store(xsDataISPyBScreeningOutputLattice)

            xsDataISPyBScreeningStrategies = xsDataISPyBScreeningOutputContainer.getScreeningStrategy()
            if xsDataISPyBScreeningStrategies != None:
                for xsDataISPyBScreeningStrategy in xsDataISPyBScreeningStrategies:
                    xsDataISPyBScreeningStrategy.setScreeningOutputId(xsDataIntegerScreeningOutputId)
                    self.store(xsDataISPyBScreeningStrategy)

    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginISPyBv1_1.postProcess")
        if (self.m_xsDataResultISPyB is not None):
            self.setDataOutput(self.m_xsDataResultISPyB)

    def httpPost(self, _pyStrHost, _iPort, _pyStrPath, _pyStrXML):
        """
        Sends XML to the dbserver on the specified host and port with the specified path.
        Returns the response XML from the dbserver.
        """
        pyStrData = None
        try:
            pyHTTPConnection = PyHttplib.HTTPConnection(_pyStrHost, _iPort)
            pyHTTPConnection.putrequest("POST", _pyStrPath)
            pyHTTPConnection.putheader("Content-type", "text/xml")
            pyHTTPConnection.putheader("Content-length", "%d" % len(_pyStrXML))
            pyHTTPConnection.putheader('Accept', 'text/plain')
            if "HOSTNAME" in PyOs.environ.keys():
                pyHTTPConnection.putheader('Host', PyOs.environ["HOSTNAME"])
            pyHTTPConnection.endheaders()
            pyHTTPConnection.send(_pyStrXML)
            pyHTTPResponse = pyHTTPConnection.getresponse()
            pyStrMsg = pyHTTPResponse.msg
            pyStrHeaders = pyHTTPResponse.getheaders()
            pyStrReply = str(pyHTTPResponse.status) + ' - ' + pyHTTPResponse.reason

            pyStrContentLength = pyHTTPResponse.getheader("Content-Length")
            if pyStrContentLength is None:
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "httpPost", \
                                                           "No header returned for %s, host %s, port %d. HTTP resonse was: %s" \
                                                           % (_pyStrPath, _pyStrHost, _iPort, pyStrReply))
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            try:
                ilength = PyString.atoi(pyStrContentLength)
            except:
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "httpPost", \
                                                           "Cannot convert Content-Length %s to integer for %s, host %s, port %d!" \
                                                           % (pyStrContentLength, _pyStrPath, _pyStrHost, _iPort))
                EDVerbose.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage

            pyStrData = pyHTTPResponse.read()
        except (PySocket.error, PyHttplib.BadStatusLine), (msg):
            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "httpPost", \
                                                                 "Have you set up a connection to the dbserver? Error is: %s" % (msg))
            EDVerbose.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)
            self.setFailure()
            raise RuntimeError, pyStrErrorMessage

        return pyStrData

    def store(self, _xsDataISPyBScreeningObject):
        # Create DNA compatible XML from xsDataScreeningObject:
        pyStrXML = EDUtilsXML.dnaMarshal(_xsDataISPyBScreeningObject)

        # Send the XML to the dbserver:
        pyStrResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/store_object_request", pyStrXML)

        if pyStrResponse != None:
            # Handle response:
            EDVerbose.DEBUG(pyStrResponse)

            xsDatadbstatus = XSDatadbstatus.parseString(pyStrResponse)

            EDVerbose.DEBUG("dbserver returns code: " + xsDatadbstatus.getCode())
            EDVerbose.DEBUG("dbserver returns message: " + xsDatadbstatus.getMessage())

            if xsDatadbstatus.getCode() == "error":
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "process", xsDatadbstatus.getMessage())
                EDVerbose.error(xsDatadbstatus.getMessage())
                self.addErrorMessage(xsDatadbstatus.getMessage())
                return - 1
            else:
                xsDataResultStatus = XSDataResultStatus()
                xsDataResultStatus.setCode(XSDataString(xsDatadbstatus.getCode()))
                xsDataResultStatus.setMessage(XSDataString(xsDatadbstatus.getMessage()))

                iIndex = -1
                pyStrClassName = _xsDataISPyBScreeningObject.__class__.__name__

                if pyStrClassName == "XSDataISPyBScreening":
                    iIndex = xsDatadbstatus.getScreeningId()
                    self.m_xsDataResultISPyB.setScreeningStatus(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningInput":
                    iIndex = xsDatadbstatus.getScreeningInputId()
                    self.m_xsDataResultISPyB.getScreeningInputStatus().append(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningOutput":
                    iIndex = xsDatadbstatus.getScreeningOutputId()
                    self.m_xsDataResultISPyB.getScreeningOutputStatus().append(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningOutputLattice":
                    iIndex = xsDatadbstatus.getScreeningOutputLatticeId()
                    self.m_xsDataResultISPyB.getScreeningOutputLatticeStatus().append(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningStrategy":
                    iIndex = xsDatadbstatus.getScreeningStrategyId()
                    self.m_xsDataResultISPyB.getScreeningStrategyStatus().append(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningRank":
                    iIndex = xsDatadbstatus.getScreeningRankId()
                    self.m_xsDataResultISPyB.getScreeningRankStatus().append(xsDataResultStatus)
                elif pyStrClassName == "XSDataISPyBScreeningRankSet":
                    iIndex = xsDatadbstatus.getScreeningRankSetId()
                    self.m_xsDataResultISPyB.setScreeningRankSetStatus(xsDataResultStatus)
                else:
                    pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_1", "store", \
                                                           "Class type not found.")
                    EDVerbose.error(pyStrErrorMessage)
                    self.addErrorMessage(pyStrErrorMessage)
                    raise RuntimeError, pyStrErrorMessage

                xsDataResultStatus.setId(XSDataInteger(iIndex))
                return XSDataInteger(iIndex)

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("*** EDPluginISPyBv1_1.generateExecutiveSummary")

        xsDataResultISPyB = self.getDataOutput()
        if xsDataResultISPyB != None:

            self.addExecutiveSummaryLine("")

            xsDataResultStatusScreening = xsDataResultISPyB.getScreeningStatus()
            xsDataResultStatusScreeningInputs = xsDataResultISPyB.getScreeningInputStatus()
            xsDataResultStatusScreeningOutputs = xsDataResultISPyB.getScreeningOutputStatus()
            xsDataResultStatusScreeningOutputLattices = xsDataResultISPyB.getScreeningOutputLatticeStatus()
            xsDataResultStatusScreeningStrategies = xsDataResultISPyB.getScreeningStrategyStatus()
            xsDataResultStatusScreeningRanks = xsDataResultISPyB.getScreeningRankStatus()
            xsDataResultStatusScreeningRankSet = xsDataResultISPyB.getScreeningRankSetStatus()

            if xsDataResultStatusScreening != None:
                xsDataIntegerScreeningId = xsDataResultStatusScreening.getId()
                self.addExecutiveSummaryLine("Screening stored with id: %d" % xsDataIntegerScreeningId.getValue())

            for xsDataResultStatusScreeningInput in xsDataResultStatusScreeningInputs:
                if xsDataResultStatusScreeningInput != None:
                    xsDataIntegerScreeningInputId = xsDataResultStatusScreeningInput.getId()
                    self.addExecutiveSummaryLine("ScreeningInput stored with id: %d" % xsDataIntegerScreeningInputId.getValue())

            for xsDataResultStatusScreeningOutput in xsDataResultStatusScreeningOutputs:
                if xsDataResultStatusScreeningOutput != None:
                    xsDataIntegerScreeningOutputId = xsDataResultStatusScreeningOutput.getId()
                    self.addExecutiveSummaryLine("ScreeningOutput stored with id: %d" % xsDataIntegerScreeningOutputId.getValue())

            for xsDataResultStatusScreeningOutputLattice in xsDataResultStatusScreeningOutputLattices:
                if xsDataResultStatusScreeningOutputLattice != None:
                    xsDataIntegerScreeningOutputLatticeId = xsDataResultStatusScreeningOutputLattice.getId()
                    self.addExecutiveSummaryLine("ScreeningOutputLattice stored with id: %d" % xsDataIntegerScreeningOutputLatticeId.getValue())

            for xsDataResultStatusScreeningStrategy in xsDataResultStatusScreeningStrategies:
                if xsDataResultStatusScreeningStrategy != None:
                    xsDataIntegerScreeningStrategyId = xsDataResultStatusScreeningStrategy.getId()
                    self.addExecutiveSummaryLine("ScreeningStrategy stored with id: %d" % xsDataIntegerScreeningStrategyId.getValue())

            for xsDataResultStatusScreeningRank in xsDataResultStatusScreeningRanks:
                if xsDataResultStatusScreeningRank != None:
                    xsDataIntegerScreeningRankId = xsDataResultStatusScreeningRank.getId()
                    self.addExecutiveSummaryLine("ScreeningRank stored with id: %d" % xsDataIntegerScreeningRankId.getValue())

            if xsDataResultStatusScreeningRankSet != None:
                xsDataIntegerScreeningRankSetId = xsDataResultStatusScreeningRankSet.getId()
                self.addExecutiveSummaryLine("ScreeningRankSet stored with id: %d" % xsDataIntegerScreeningRankSetId.getValue())
