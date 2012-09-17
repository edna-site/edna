#
#    Project: mxPluginExec
#             http://www.edna-site.org
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

from EDMessage          import EDMessage
from EDConfiguration    import EDConfiguration
from EDUtilsXML         import EDUtilsXML

from XSDataCommon   import XSData
from XSDataCommon   import XSDataInteger
from XSDataCommon   import XSDataString

from XSDataISPyBv10 import XSDataISPyBImage
from XSDataISPyBv10 import XSDataISPyBScreening
from XSDataISPyBv10 import XSDataISPyBScreeningInput
from XSDataISPyBv10 import XSDataISPyBScreeningOutput
from XSDataISPyBv10 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv10 import XSDataISPyBScreeningRank
from XSDataISPyBv10 import XSDataISPyBScreeningRankSet
from XSDataISPyBv10 import XSDataISPyBScreeningStrategy
from XSDataISPyBv10 import XSDataInputISPyB
from XSDataISPyBv10 import XSDataResultISPyB
from XSDataISPyBv10 import XSDataResultStatus
from XSDataISPyBv10 import XSDatadbstatus

from EDImportSystem import PyHttplib
from EDImportSystem import PyOs
from EDImportSystem import PyString
from EDImportSystem import PySocket

class EDPluginISPyBv10(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using the DNA/ISPyB dbserver 
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyB)
        self.__strDbserverHost = "localhost"
        self.m_iDbserverPort = 9090

    def getDbserverHost(self):
        return self.__strDbserverHost

    def setDbserverHost(self, _strDbserverHost):
        self.__strDbserverHost = _strDbserverHost

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
            self.DEBUG("*** EDPluginISPyBv10.configure: pluginConfiguration is None, using default settings")
        else:
            self.DEBUG("*** EDPluginISPyBv10.configure: pluginConfiguration found, using settings from there")
            pyStrDbserverHost = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverHost")
            if(pyStrDbserverHost == None):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverHost")
                self.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            else:
                self.setDbserverHost(pyStrDbserverHost)

            pyStrDbserverPort = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverPort")
            if(pyStrDbserverPort == None):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverPort")
                self.error(pyStrErrorMessage)
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
        self.DEBUG("*** EDPluginISPyBv10.process")
        xsDataInputISPyB = self.getDataInput()
        self.m_xsDataResultISPyB = XSDataResultISPyB()

        xsDataISPyBScreening = xsDataInputISPyB.getScreening()
        if xsDataISPyBScreening == None:
            xsDataISPyBScreening = XSDataISPyBScreening()

        xsDataISPyBImage = xsDataInputISPyB.getImage()

        if xsDataISPyBScreening.getDataCollectionId() == None:
            if ((xsDataISPyBImage == None) or (xsDataISPyBImage.getFileName() == None) or (xsDataISPyBImage.getFileLocation() == None)):
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "process", \
                                                                     "Neither a dataCollectionId nor a image filename + path are provided.")
                self.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                return

            strXML = EDUtilsXML.dnaMarshal(xsDataISPyBImage)

            # Send the XML to request the dataCollectionId from the dbserver:
            edStringResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/get_datacollectionid", strXML)

            if edStringResponse != None:
                # Handle response:
                self.DEBUG(edStringResponse)
                xsDatadbstatus = XSDatadbstatus.parseString(edStringResponse)
                pyStrCode = xsDatadbstatus.getCode()
                pyStrMessage = xsDatadbstatus.getMessage()
                self.DEBUG("dbserver returns code: " + pyStrCode)
                self.DEBUG("dbserver returns message: " + pyStrMessage)

                if (pyStrCode == "error") or (xsDatadbstatus.getDataCollectionId() == -1):
                    if xsDatadbstatus.getDataCollectionId() == -1:
                        pyStrMessage = "An image corresponding to the given fileName and fileLocation was not found."
                    pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "process", pyStrMessage)
                    self.error(pyStrErrorMessage)
                    self.addErrorMessage(pyStrErrorMessage)
                    return

                if xsDatadbstatus.getDataCollectionId() != -1:
                    xsDataISPyBScreening.setDataCollectionId(XSDataInteger(xsDatadbstatus.getDataCollectionId()))
                    self.DEBUG("dataCollectionId is: " + str(xsDataISPyBScreening.getDataCollectionId().getValue()))

        xsDataISPyBScreeningInput = xsDataInputISPyB.getScreeningInput()
        xsDataISPyBScreeningOutput = xsDataInputISPyB.getScreeningOutput()
        xsDataISPyBScreeningOutputLattice = xsDataInputISPyB.getScreeningOutputLattice()
        xsDataISPyBScreeningRank = xsDataInputISPyB.getScreeningRank()
        xsDataISPyBScreeningRankSet = xsDataInputISPyB.getScreeningRankSet()
        xsDataISPyBScreeningStrategy = xsDataInputISPyB.getScreeningStrategy()

        for xsDataISPyBScreeningObject in [ xsDataISPyBScreening, xsDataISPyBScreeningRankSet, xsDataISPyBScreeningInput, xsDataISPyBScreeningOutput, \
                                      xsDataISPyBScreeningOutputLattice, xsDataISPyBScreeningRank, xsDataISPyBScreeningStrategy ]:

            if xsDataISPyBScreeningObject != None:

                # Set any missing foreign key attributes in xsDataScreeningObject:
                self.setForeignKeyAttributes(xsDataISPyBScreeningObject, self.m_xsDataResultISPyB)

                # Create DNA compatible XML from xsDataScreeningObject:
                strXML = EDUtilsXML.dnaMarshal(xsDataISPyBScreeningObject)

                # Send the XML to the dbserver:
                edStringResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/store_object_request", strXML)

                if edStringResponse != None:
                    # Handle response:
                    self.DEBUG(edStringResponse)

                    xsDatadbstatus = XSDatadbstatus.parseString(edStringResponse)

                    pyStrCode = xsDatadbstatus.getCode()
                    pyStrMessage = xsDatadbstatus.getMessage()
                    xsDataStrCode = XSDataString(pyStrCode)
                    xsDataStrMessage = XSDataString(pyStrMessage)
                    self.DEBUG("dbserver returns code: " + pyStrCode)
                    self.DEBUG("dbserver returns message: " + pyStrMessage)

                    xsDataResultStatusList = self.m_xsDataResultISPyB.getResultStatus()
                    xsDataResultStatus = XSDataResultStatus(xsDataISPyBScreeningObject, xsDataStrCode, xsDataStrMessage)
                    xsDataResultStatusList.append(xsDataResultStatus)

                    self.addToXSDataResultISPyB(self.m_xsDataResultISPyB, xsDatadbstatus)

                    if pyStrCode == "error":
                        pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "process", pyStrMessage)
                        self.error(pyStrErrorMessage)
                        self.addErrorMessage(pyStrErrorMessage)
                        return
                else:
                    return

    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("*** EDPluginISPyBv10.postProcess")
        if (self.m_xsDataResultISPyB is not None):
            self.setDataOutput(self.m_xsDataResultISPyB)

            xsDataResultStatusList = self.m_xsDataResultISPyB.getResultStatus()
            for xsDataResultStatus in xsDataResultStatusList:
                xsDataObject = xsDataResultStatus.getScreeningObject()
                xsDataStrCode = xsDataResultStatus.getCode()
                xsDataStrMessage = xsDataResultStatus.getMessage()

                if xsDataStrCode.getValue() == "error":
                    pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "postProcess", "Could not store object of class %s." \
                                                                         % xsDataObject.__class__.__name__)
                    self.error(pyStrErrorMessage)
                    self.addErrorMessage(pyStrErrorMessage)

        if len(xsDataResultStatusList) == 0:
            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "postProcess", "No objects stored.")
            self.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)

    def setForeignKeyAttributes(self, _xsDataISPyBScreeningObject, _xsDataResultISPyB):
        """
        Sets missing foreign key attributes in _xsDataISPyBScreeningObject if available
        """
        className = _xsDataISPyBScreeningObject.__class__.__name__
        # Set required foreign key attributes:
        if className in ["XSDataISPyBScreeningInput", "XSDataISPyBScreeningOutput", "XSDataISPyBScreeningRank" ]:
            if _xsDataISPyBScreeningObject.getScreeningId() == None:
                xsDataInteger = _xsDataResultISPyB.getScreeningId()
                _xsDataISPyBScreeningObject.setScreeningId(xsDataInteger)
        if className == "XSDataISPyBScreeningRank":
            if _xsDataISPyBScreeningObject.getScreeningRankId() == None:
                xsDataInteger = _xsDataResultISPyB.getScreeningRankId()
                _xsDataISPyBScreeningObject.setScreeningRankId(xsDataInteger)
        if className in [ "XSDataISPyBScreeningStrategy", "XSDataISPyBScreeningOutputLattice" ]:
            if _xsDataISPyBScreeningObject.getScreeningOutputId() == None:
                xsDataInteger = _xsDataResultISPyB.getScreeningOutputId()
                _xsDataISPyBScreeningObject.setScreeningOutputId(xsDataInteger)

    def httpPost(self, _strHost, _iPort, _strPath, _strXML):
        """
        Sends XML to the dbserver on the specified host and port with the specified path.
        Returns the response XML from the dbserver.
        """
        try:
            pyHTTPConnection = PyHttplib.HTTPConnection(_strHost, _iPort)
            pyHTTPConnection.putrequest("POST", _strPath)
            pyHTTPConnection.putheader("Content-type", "text/xml")
            pyHTTPConnection.putheader("Content-length", "%d" % len(_strXML))
            pyHTTPConnection.putheader('Accept', 'text/plain')
            if "HOSTNAME" in PyOs.environ.keys():
                pyHTTPConnection.putheader('Host', PyOs.environ["HOSTNAME"])
            pyHTTPConnection.endheaders()
            pyHTTPConnection.send(_strXML)
            pyHTTPResponse = pyHTTPConnection.getresponse()
            pyStrMsg = pyHTTPResponse.msg
            pyStrHeaders = pyHTTPResponse.getheaders()
            pyStrReply = str(pyHTTPResponse.status) + ' - ' + pyHTTPResponse.reason

            pyStrContentLength = pyHTTPResponse.getheader("Content-Length")
            if pyStrContentLength is None:
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "httpPost", \
                                                           "No header returned for %s, host %s, port %d. HTTP resonse was: %s" \
                                                           % (_strPath, _strHost, _iPort, pyStrReply))
                self.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage
            try:
                ilength = PyString.atoi(pyStrContentLength)
            except:
                pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "httpPost", \
                                                           "Cannot convert Content-Length %s to integer for %s, host %s, port %d!" \
                                                           % (pyStrContentLength, _strPath, _strHost, _iPort))
                self.error(pyStrErrorMessage)
                self.addErrorMessage(pyStrErrorMessage)
                raise RuntimeError, pyStrErrorMessage

            pyStrData = pyHTTPResponse.read()
        except (PySocket.error, PyHttplib.BadStatusLine), (msg):
            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv10", "httpPost", \
                                                                 "Have you set up a connection to the dbserver? Error is: %s" % (msg))
            self.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)
            return None

        return pyStrData

    def addToXSDataResultISPyB(self, _xsDataResultISPyB, _xsDatadbstatus):
        """
        Creates an XSDataResultISPyB object from an XSDatadbserver object which contains the primary key ID(s) 
        for the stored object(s) as returned from the dbserver. 
        """

        if _xsDatadbstatus.getScreeningId() != -1:
            _xsDataResultISPyB.setScreeningId(XSDataInteger(_xsDatadbstatus.getScreeningId()))
            self.DEBUG("screeningId is: " + str(_xsDataResultISPyB.getScreeningId().getValue()))
        if _xsDatadbstatus.getScreeningRankId() != -1:
            _xsDataResultISPyB.setScreeningRankId(XSDataInteger(_xsDatadbstatus.getScreeningRankId()))
            self.DEBUG("screeningRankId is: " + str(_xsDataResultISPyB.getScreeningRankId().getValue()))
        if _xsDatadbstatus.getScreeningRankSetId() != -1:
            _xsDataResultISPyB.setScreeningRankSetId(XSDataInteger(_xsDatadbstatus.getScreeningRankSetId()))
            self.DEBUG("screeningRankSetId is: " + str(_xsDataResultISPyB.getScreeningRankSetId().getValue()))
        if _xsDatadbstatus.getScreeningStrategyId() != -1:
            _xsDataResultISPyB.setScreeningStrategyId(XSDataInteger(_xsDatadbstatus.getScreeningStrategyId()))
            self.DEBUG("screeningStrategyId is: " + str(_xsDataResultISPyB.getScreeningStrategyId().getValue()))
        if _xsDatadbstatus.getScreeningInputId() != -1:
            _xsDataResultISPyB.setScreeningInputId(XSDataInteger(_xsDatadbstatus.getScreeningInputId()))
            self.DEBUG("screeningInputId is: " + str(_xsDataResultISPyB.getScreeningInputId().getValue()))
        if _xsDatadbstatus.getScreeningOutputId() != -1:
            _xsDataResultISPyB.setScreeningOutputId(XSDataInteger(_xsDatadbstatus.getScreeningOutputId()))
            self.DEBUG("screeningOutputId is: " + str(_xsDataResultISPyB.getScreeningOutputId().getValue()))
        if _xsDatadbstatus.getScreeningOutputLatticeId() != -1:
            _xsDataResultISPyB.setScreeningOutputLatticeId(XSDataInteger(_xsDatadbstatus.getScreeningOutputLatticeId()))
            self.DEBUG("screeningOutputLatticeId is: " + str(_xsDataResultISPyB.getScreeningOutputLatticeId().getValue()))
        return _xsDataResultISPyB

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("*** EDPluginISPyBv10.generateExecutiveSummary")

        xsDataResultISPyB = self.getDataOutput()
        if xsDataResultISPyB != None:

            self.addExecutiveSummaryLine("")

            if xsDataResultISPyB.getScreeningId() != None:
                self.addExecutiveSummaryLine("screening stored with id: " + str(xsDataResultISPyB.getScreeningId()))
            if xsDataResultISPyB.getScreeningInputId() != None:
                self.addExecutiveSummaryLine("screeningInput stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningInputId()))
            if xsDataResultISPyB.getScreeningRankId() != None:
                self.addExecutiveSummaryLine("screeningRank stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningRankId()))
            if xsDataResultISPyB.getScreeningRankSetId() != None:
                self.addExecutiveSummaryLine("screeningRankSet stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningRankSetId()))
            if xsDataResultISPyB.getScreeningStrategyId() != None:
                self.addExecutiveSummaryLine("screeningStrategy stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningStrategyId()))
            if xsDataResultISPyB.getScreeningOutputId() != None:
                self.addExecutiveSummaryLine("screeningOutput stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningOutputId()))
            if xsDataResultISPyB.getScreeningOutputLatticeId() != None:
                self.addExecutiveSummaryLine("screeningOutputLattice stored with id: " + \
                                              str(xsDataResultISPyB.getScreeningOutputLatticeId()))
