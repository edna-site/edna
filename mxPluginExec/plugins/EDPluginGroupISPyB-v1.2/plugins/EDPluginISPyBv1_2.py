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

__author__ = "Karl Levik, Marie-Francoise Incardona, Olof Svensson"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"
__date__ = "20120712"
__status__ = "production"

from EDPluginExec       import EDPluginExec

from EDMessage          import EDMessage
from EDConfiguration    import EDConfiguration
from EDUtilsXML         import EDUtilsXML
from XSDataCommon       import XSData
from XSDataCommon       import XSDataInteger
from XSDataCommon       import XSDataString

from XSDataISPyBv1_2 import XSDataISPyBImage
from XSDataISPyBv1_2 import XSDataISPyBScreening
from XSDataISPyBv1_2 import XSDataISPyBScreeningInput
from XSDataISPyBv1_2 import XSDataISPyBScreeningOutputContainer
from XSDataISPyBv1_2 import XSDataISPyBScreeningOutput
from XSDataISPyBv1_2 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_2 import XSDataISPyBScreeningRank
from XSDataISPyBv1_2 import XSDataISPyBScreeningRankSet
from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategyWedge
from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategySubWedge
from XSDataISPyBv1_2 import XSDataISPyBScreeningFile
from XSDataISPyBv1_2 import XSDataISPyBImage
#from XSDataISPyBv1_2 import XSDataISPyBv1_2
from XSDataISPyBv1_2 import XSDataResultISPyB
from XSDataISPyBv1_2 import XSDataResultStatus
from XSDataISPyBv1_2 import XSDatadbstatus

import httplib, os, socket, string


class EDPluginISPyBv1_2(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using the DNA/ISPyB dbserver 
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataISPyBScreening, "screening")                 # [0, 1]
        self.setXSDataInputClass(XSDataISPyBScreeningInput, "screeningInput")       # [0, infinite] 
        self.setXSDataInputClass(XSDataISPyBScreeningOutputContainer, "screeningOutputContainer") # [0, infinite] 
        self.setXSDataInputClass(XSDataISPyBScreeningRank, "screeningRank")         # [0, infinite]
        self.setXSDataInputClass(XSDataISPyBScreeningRankSet, "screeningRankSet")   # [0, 1]
        self.setXSDataInputClass(XSDataISPyBScreeningFile, "screeningFile")         # [0, infinite]
        self.setXSDataInputClass(XSDataISPyBImage, "image")                        # [0, 1]

        self.__strDbserverHost = "localhost"
        self.__iDbserverPort = 9090


    def getDbserverHost(self):
        return self.__strDbserverHost

    def setDbserverHost(self, _strDbserverHost):
        self.__strDbserverHost = _strDbserverHost

    def getDbserverPort(self):
        return self.__iDbserverPort

    def setDbserverPort(self, _iDbserverPort):
        self.__iDbserverPort = _iDbserverPort

    def configure(self):
        """
        Gets the dbserver parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            self.DEBUG("*** EDPluginISPyBv1_2.configure: pluginConfiguration is None, using default settings")
        else:
            self.DEBUG("*** EDPluginISPyBv1_2.configure: pluginConfiguration found, using settings from there")
            strDbserverHost = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverHost")
            if(strDbserverHost == None):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverHost")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            else:
                self.setDbserverHost(strDbserverHost)

            strDbserverPort = EDConfiguration.getStringParamValue(pluginConfiguration, "dbserverPort")
            if(strDbserverPort == None):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2.configure", self.getClassName(), \
                                                                     "Configuration parameter missing: dbserverPort")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            else:
                self.setDbserverPort(int (strDbserverPort))


    def process(self, _edObject=None):
        """
        Sends store requests with the screening objects to the dbserver. Returns success or failure.
        
        Note that:
        * Any objects referred to by the object returned by self.getDataInput("inputISPyB")[0] will be stored. 
        * Primary key attributes should not be set.
        * If a foreign key attribute is not set, this method will attempt to find the foreign object among the 
        input objects, and then use the primary key attribute of this object when it has been stored. If such 
        an object is not found, the method fails.
        * If an error is encountered, the method will immediately fail and will not attempt to store any more 
        objects. 
        """

        EDPluginExec.process(self)
        self.DEBUG("*** EDPluginISPyBv1_2.process")

        # Basic sanity check of inputs:
        if (self.hasDataInput("screening")):
            if (len(self.getDataInput("screening")) > 1):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "process", "There should only be one input 'screening'.")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

        if (self.hasDataInput("screeningRankSet")):
            if (len(self.getDataInput("screeningRankSet")) > 1):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "process", "There should only be one input 'screeningRankSet'.")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

        # Get the inputs
        xsDataISPyBScreenings = None
        xsDataISPyBScreeningInputs = None
        xsDataISPyBScreeningOutputContainers = None
        xsDataISPyBScreeningRanks = None
        xsDataISPyBScreeningRankSets = None
        xsDataISPyBImages = None
        xsDataISPyBScreeningFiles = None

        if self.hasDataInput("screening"):
            xsDataISPyBScreenings = self.getDataInput("screening")
        if self.hasDataInput("screeningInput"):
            xsDataISPyBScreeningInputs = self.getDataInput("screeningInput")
        if self.hasDataInput("screeningOutputContainer"):
            xsDataISPyBScreeningOutputContainers = self.getDataInput("screeningOutputContainer")
        if self.hasDataInput("screeningRank"):
            xsDataISPyBScreeningRanks = self.getDataInput("screeningRank")
        if self.hasDataInput("screeningRankSet"):
            xsDataISPyBScreeningRankSets = self.getDataInput("screeningRankSet")
        if self.hasDataInput("image"):
            xsDataISPyBImages = self.getDataInput("image")
        if self.hasDataInput("screeningFile"):
            xsDataISPyBScreeningFiles = self.getDataInput("screeningFile")

        self.__xsDataResultISPyB = XSDataResultISPyB()

        if (xsDataISPyBScreenings is None):
            xsDataISPyBScreening = XSDataISPyBScreening()
        else:
            xsDataISPyBScreening = xsDataISPyBScreenings[0]

        if (xsDataISPyBImages is None):
            xsDataISPyBImage = None
        else:
            xsDataISPyBImage = xsDataISPyBImages[0]

        # Another sanity check:
        if xsDataISPyBScreening.getDataCollectionId() == None:
            if ((xsDataISPyBImage == None) or (xsDataISPyBImage.getFileName() == None) or (xsDataISPyBImage.getFileLocation() == None)):
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "process", \
                                                                     "Neither a dataCollectionId nor an image filename + path are provided.")
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                return

            strXML = EDUtilsXML.dnaMarshal(xsDataISPyBImage)

            # Send the XML to request the dataCollectionId from the dbserver:
            strResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/get_datacollectionid", strXML)

            if strResponse != None:
                # Handle response:
                xsDatadbstatus = XSDatadbstatus.parseString(strResponse)
                strCode = xsDatadbstatus.getCode()
                strMessage = xsDatadbstatus.getMessage()
                self.DEBUG("dbserver returns code: " + strCode)
                self.DEBUG("dbserver returns message: " + strMessage)

                if (strCode == "error") or (xsDatadbstatus.getDataCollectionId() == -1):
                    if xsDatadbstatus.getDataCollectionId() == -1:
                        strMessage = "An image corresponding to the given fileName and fileLocation was not found."
                    strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "process", strMessage)
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    return

                if xsDatadbstatus.getDataCollectionId() != -1:
                    xsDataISPyBScreening.setDataCollectionId(XSDataInteger(xsDatadbstatus.getDataCollectionId()))
                    self.__xsDataResultISPyB.setDataCollectionId(XSDataInteger(xsDatadbstatus.getDataCollectionId()))

        if (xsDataISPyBScreeningRankSets is None):
            xsDataISPyBScreeningRankSet = None
        else:
            xsDataISPyBScreeningRankSet = xsDataISPyBScreeningRankSets[0]

        # Store all the different screening* objects:
        xsDataIntegerScreeningId = self.store(xsDataISPyBScreening)

        if xsDataISPyBScreeningInputs != None:
            for xsDataISPyBScreeningInput in xsDataISPyBScreeningInputs:
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

            xsDataISPyBScreeningStrategyContainers = xsDataISPyBScreeningOutputContainer.getScreeningStrategyContainer()
            if xsDataISPyBScreeningStrategyContainers != None:
                for xsDataISPyBScreeningStrategyContainer in xsDataISPyBScreeningStrategyContainers:
                    xsDataISPyBScreeningStrategy = xsDataISPyBScreeningStrategyContainer.getScreeningStrategy()
                    if xsDataISPyBScreeningStrategy != None:
                        xsDataISPyBScreeningStrategy.setScreeningOutputId(xsDataIntegerScreeningOutputId)
                        xsDataIntegerScreeningStrategyId = self.store(xsDataISPyBScreeningStrategy)

                        xsDataISPyBScreeningStrategyWedgeContainers = xsDataISPyBScreeningStrategyContainer.getScreeningStrategyWedgeContainer()
                        if xsDataISPyBScreeningStrategyWedgeContainers != None:
                            for xsDataISPyBScreeningStrategyWedgeContainer in xsDataISPyBScreeningStrategyWedgeContainers:
                                xsDataISPyBScreeningStrategyWedge = xsDataISPyBScreeningStrategyWedgeContainer.getScreeningStrategyWedge()
                                xsDataISPyBScreeningStrategyWedge.setScreeningStrategyId(xsDataIntegerScreeningStrategyId)
                                xsDataIntegerScreeningStrategyWedgeId = self.store(xsDataISPyBScreeningStrategyWedge)

                                xsDataISPyBScreeningStrategySubWedges = xsDataISPyBScreeningStrategyWedgeContainer.getScreeningStrategySubWedge()
                                if xsDataISPyBScreeningStrategySubWedges != None:
                                    for xsDataISPyBScreeningStrategySubWedge in xsDataISPyBScreeningStrategySubWedges:
                                        xsDataISPyBScreeningStrategySubWedge.setScreeningStrategyWedgeId(xsDataIntegerScreeningStrategyWedgeId)
                                        self.store(xsDataISPyBScreeningStrategySubWedge)


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        self.DEBUG("*** EDPluginISPyBv1_2.postProcess")
        if (self.__xsDataResultISPyB is not None):
            self.setDataOutput(self.__xsDataResultISPyB)

    def httpPost(self, _strHost, _iPort, _strPath, _strXML):
        """
        Sends XML to the dbserver on the specified host and port with the specified path.
        Returns the response XML from the dbserver.
        @param _strHost: the host name for the dbserver
        @type  _strHost: string
        @param _iPort: the port for the dbserver
        @type  _iPort: integer
        @param _strPath: the path name for the request
        @type  _strPath: string
        @param _strXML: the XML for the request
        @type  _strXML: string
        """
        strData = None
        try:
            pyHTTPConnection = httplib.HTTPConnection(_strHost, _iPort)
            pyHTTPConnection.putrequest("POST", _strPath)
            pyHTTPConnection.putheader("Content-type", "text/xml")
            pyHTTPConnection.putheader("Content-length", "%d" % len(_strXML))
            pyHTTPConnection.putheader('Accept', 'text/plain')
            if "HOSTNAME" in os.environ.keys():
                pyHTTPConnection.putheader('Host', os.environ["HOSTNAME"])
            pyHTTPConnection.endheaders()
            pyHTTPConnection.send(_strXML)
            pyHTTPResponse = pyHTTPConnection.getresponse()
            strMsg = pyHTTPResponse.msg
            strHeaders = pyHTTPResponse.getheaders()
            strReply = str(pyHTTPResponse.status) + ' - ' + pyHTTPResponse.reason

            strContentLength = pyHTTPResponse.getheader("Content-Length")
            if strContentLength is None:
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "httpPost", \
                                                           "No header returned for %s, host %s, port %d. HTTP resonse was: %s" \
                                                           % (_strPath, _strHost, _iPort, strReply))
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage
            try:
                ilength = string.atoi(strContentLength)
            except:
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "httpPost", \
                                                           "Cannot convert Content-Length %s to integer for %s, host %s, port %d!" \
                                                           % (strContentLength, _strPath, _strHost, _iPort))
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

            strData = pyHTTPResponse.read()
        except (socket.error, httplib.BadStatusLine), (msg):
            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "httpPost", \
                                                                 "Have you set up a connection to the dbserver? Error is: %s" % (msg))
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            raise RuntimeError, strErrorMessage

        return strData

    def store(self, _xsDataISPyBScreeningObject):
        # Create DNA compatible XML from xsDataScreeningObject:
        strXML = EDUtilsXML.dnaMarshal(_xsDataISPyBScreeningObject)

        # Send the XML to the dbserver:
        strResponse = self.httpPost(self.getDbserverHost(), self.getDbserverPort(), "/store_object_request", strXML)

        if strResponse != None:
            # Handle response:
            self.DEBUG(strResponse)

            xsDatadbstatus = XSDatadbstatus.parseString(strResponse)

            self.DEBUG("dbserver returns code: " + xsDatadbstatus.getCode())
            self.DEBUG("dbserver returns message: " + xsDatadbstatus.getMessage())

            if xsDatadbstatus.getCode() == "error":
                strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "store", xsDatadbstatus.getMessage())
                self.error(xsDatadbstatus.getMessage())
                self.addErrorMessage(strErrorMessage)
                return - 1
            else:
                xsDataResultStatus = XSDataResultStatus()
                xsDataResultStatus.setCode(XSDataString(xsDatadbstatus.getCode()))
                xsDataResultStatus.setMessage(XSDataString(xsDatadbstatus.getMessage()))

                iIndex = -1
                strClassName = _xsDataISPyBScreeningObject.__class__.__name__

                if strClassName == "XSDataISPyBScreening":
                    iIndex = xsDatadbstatus.getScreeningId()
                    self.__xsDataResultISPyB.setScreeningStatus(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningInput":
                    iIndex = xsDatadbstatus.getScreeningInputId()
                    self.__xsDataResultISPyB.getScreeningInputStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningOutput":
                    iIndex = xsDatadbstatus.getScreeningOutputId()
                    self.__xsDataResultISPyB.getScreeningOutputStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningOutputLattice":
                    iIndex = xsDatadbstatus.getScreeningOutputLatticeId()
                    self.__xsDataResultISPyB.getScreeningOutputLatticeStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningStrategy":
                    iIndex = xsDatadbstatus.getScreeningStrategyId()
                    self.__xsDataResultISPyB.getScreeningStrategyStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningStrategyWedge":
                    iIndex = xsDatadbstatus.getScreeningStrategyWedgeId()
                    self.__xsDataResultISPyB.getScreeningStrategyWedgeStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningStrategySubWedge":
                    iIndex = xsDatadbstatus.getScreeningStrategySubWedgeId()
                    self.__xsDataResultISPyB.getScreeningStrategySubWedgeStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningFile":
                    iIndex = xsDatadbstatus.getScreeningFileId()
                    self.__xsDataResultISPyB.setScreeningFileStatus(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningRank":
                    iIndex = xsDatadbstatus.getScreeningRankId()
                    self.__xsDataResultISPyB.getScreeningRankStatus().append(xsDataResultStatus)
                elif strClassName == "XSDataISPyBScreeningRankSet":
                    iIndex = xsDatadbstatus.getScreeningRankSetId()
                    self.__xsDataResultISPyB.setScreeningRankSetStatus(xsDataResultStatus)
                else:
                    strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginISPyBv1_2", "store", \
                                                           "Class type not found.")
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    raise RuntimeError, strErrorMessage

                xsDataResultStatus.setId(XSDataInteger(iIndex))
                return XSDataInteger(iIndex)

    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("*** EDPluginISPyBv1_2.generateExecutiveSummary")

        xsDataResultISPyB = self.getDataOutput()
        if xsDataResultISPyB != None:

            self.addExecutiveSummaryLine("")

            xsDataResultStatusScreening = xsDataResultISPyB.getScreeningStatus()
            xsDataResultStatusScreeningInputs = xsDataResultISPyB.getScreeningInputStatus()
            xsDataResultStatusScreeningOutputs = xsDataResultISPyB.getScreeningOutputStatus()
            xsDataResultStatusScreeningOutputLattices = xsDataResultISPyB.getScreeningOutputLatticeStatus()
            xsDataResultStatusScreeningStrategies = xsDataResultISPyB.getScreeningStrategyStatus()
            xsDataResultStatusScreeningStrategyWedges = xsDataResultISPyB.getScreeningStrategyWedgeStatus()
            xsDataResultStatusScreeningStrategySubWedges = xsDataResultISPyB.getScreeningStrategySubWedgeStatus()
            xsDataResultStatusScreeningFiles = xsDataResultISPyB.getScreeningFileStatus()
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

            for xsDataResultStatusScreeningStrategyWedge in xsDataResultStatusScreeningStrategyWedges:
                if xsDataResultStatusScreeningStrategyWedge != None:
                    xsDataIntegerScreeningStrategyWedgeId = xsDataResultStatusScreeningStrategyWedge.getId()
                    self.addExecutiveSummaryLine("ScreeningStrategyWedge stored with id: %d" % xsDataIntegerScreeningStrategyWedgeId.getValue())

            for xsDataResultStatusScreeningStrategySubWedge in xsDataResultStatusScreeningStrategySubWedges:
                if xsDataResultStatusScreeningStrategySubWedge != None:
                    xsDataIntegerScreeningStrategySubWedgeId = xsDataResultStatusScreeningStrategySubWedge.getId()
                    self.addExecutiveSummaryLine("ScreeningStrategySubWedge stored with id: %d" % xsDataIntegerScreeningStrategySubWedgeId.getValue())

            for xsDataResultStatusScreeningFile in xsDataResultStatusScreeningFiles:
                if xsDataResultStatusScreeningFile != None:
                    xsDataIntegerScreeningFileId = xsDataResultStatusScreeningFile.getId()
                    self.addExecutiveSummaryLine("ScreeningFile stored with id: %d" % xsDataIntegerScreeningFileId.getValue())

            for xsDataResultStatusScreeningRank in xsDataResultStatusScreeningRanks:
                if xsDataResultStatusScreeningRank != None:
                    xsDataIntegerScreeningRankId = xsDataResultStatusScreeningRank.getId()
                    self.addExecutiveSummaryLine("ScreeningRank stored with id: %d" % xsDataIntegerScreeningRankId.getValue())

            if xsDataResultStatusScreeningRankSet != None:
                xsDataIntegerScreeningRankSetId = xsDataResultStatusScreeningRankSet.getId()
                self.addExecutiveSummaryLine("ScreeningRankSet stored with id: %d" % xsDataIntegerScreeningRankSetId.getValue())
