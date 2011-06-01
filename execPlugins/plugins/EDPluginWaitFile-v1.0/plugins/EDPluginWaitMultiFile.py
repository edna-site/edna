# coding: utf8
#
#    Project: execplugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
#
#    Contributing author:    Olof Svensson
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

__authors__ = ["Jerome Kieffer", "Olof Svensson"]
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__data__ = "20011/05/09"

import time, os, sys
from EDPluginControl            import EDPluginControl
from EDConfiguration            import EDConfiguration
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon               import XSDataString, XSDataInteger, XSDataFile
from XSDataWaitFilev1_0         import XSDataInputWaitMultiFile, XSDataResultWaitMultiFile, \
                                    XSDataInputWaitFile, XSDataResultWaitFile, XSDataBoolean
EDFactoryPluginStatic.loadModule("XSDataAccumulatorv1_0")
from XSDataAccumulatorv1_0      import XSDataInputAccumulator, XSDataResultAccumulator, XSDataQuery


class EDPluginWaitMultiFile(EDPluginControl):
    """
    Plugins that waits for a set of files to be written and reach a certain minimum size
    """
    #offers some extra seconds between official timeout and allows the plugin to finish gracefully.
    EXTRA_TIME = 5
    DELTA_TIME = 1


    def __init__(self):
        """
        Constructor of the class ...
        """
        EDPluginControl.__init__(self)
        self.__strControlledPluginWaitFile = "EDPluginWaitFile"
        self.__strControlledPluginAccumulator = "EDPluginAccumulatorv1_0"
        self.setXSDataInputClass(XSDataInputWaitMultiFile)
        self.__filesize = None
        self.__actualMinSize = sys.maxint
        self.__bAnyTimeOut = False
        self.__expectedSize = None
        self.__listEdPluginsControled = []
        self.listXsdFiles = None
        self.listXsdStrings = None
        self.listXsdFiles = []
        self.listXsdStrings
        self.xsdDataOut = XSDataResultWaitMultiFile()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginWaitMultiFile.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedFile(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedSize(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginWaitMultiFile.preProcess")
        self.__expectedSize = self.getDataInput().getExpectedSize().getValue()
        self.listXsdFiles = self.getDataInput().getExpectedFile()
        if not isinstance(self.listXsdFiles, list):
            self.listXsdFiles = [self.listXsdFiles]
        self.listXsdStrings = [ xsd.getPath() for xsd in  self.listXsdFiles]

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginWaitMultiFile.process")
        self.DEBUG("EDPluginWaitMultiFile global time-out is set to: %s (default value)" % (self.getTimeOut()))
        self.setTimeInit()
################################################################################
# Initialize the accumulator with the query
################################################################################
        xsdiAccumulator = XSDataInputAccumulator()
        xsdQuery = XSDataQuery()
        xsdQuery.setRemoveItems(XSDataBoolean(1))
        xsdQuery.setItem(self.listXsdStrings)
        xsdiAccumulator.setQuery([xsdQuery])
        edPluginAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
        self.__listEdPluginsControled.append(edPluginAccumulator)
        edPluginAccumulator.setDataInput(xsdiAccumulator)
        edPluginAccumulator.connectSUCCESS(self.doSuccessAccumulator)
        edPluginAccumulator.connectFAILURE(self.doFailureAccumulator)
        edPluginAccumulator.execute()


        for oneXSDImage in self.listXsdFiles:
            xsdiWaitFile = XSDataInputWaitFile()
            xsdiWaitFile.setExpectedFile(oneXSDImage)
            xsdiWaitFile.setExpectedSize(self.getDataInput().getExpectedSize())
            xsdiWaitFile.setTimeOut(self.getDataInput().getTimeOut())
            edPluginWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)
            self.__listEdPluginsControled.append(edPluginWaitFile)
            edPluginWaitFile.setDataInput(xsdiWaitFile)
            edPluginWaitFile.connectSUCCESS(self.doSuccessWaitFile)
            edPluginWaitFile.connectFAILURE(self.doFailureWaitFile)
            edPluginWaitFile.execute()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginWaitMultiFile.Synchronize")
        bAllPluginEnded = False
        bOnePluginIsRunning = True
        while not bAllPluginEnded:
            bAllPluginEnded = True
#            self.DEBUG("list plugins= %s" % self.__listEdPluginsControled)
            for onePlugin in self.__listEdPluginsControled[:]: #a copy of the list .... because it may vary
                self.DEBUG("inLoop: AllEnded=%s, next= %s" % (bAllPluginEnded, onePlugin.getName()))
                bAllPluginEnded = onePlugin.isEnded() and  bAllPluginEnded
                onePlugin.synchronize()

        self.DEBUG("EDPluginWaitMultiFile.postProcess: Waited for %.3f s" % self.getRunTime())
#        self.xsdDataOut.setActualFile(xsDataFile)
        self.xsdDataOut.setActualMinSize(XSDataInteger(self.__actualMinSize))
        self.xsdDataOut.setTimedOut(XSDataBoolean(self.__bAnyTimeOut))
        # Create some output data
        self.setDataOutput(self.xsdDataOut)


    def doSuccessAccumulator(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginWaitMultiFile.doSuccessAccumulator")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginWaitMultiFile.doSuccessAccumulator")
        xsdQueries = _edPlugin.getDataOutput().getQuery()
        if xsdQueries is not None and len(xsdQueries) == 1 :
            xsdQuery = xsdQueries[0]
            if (xsdQuery is not None) and (len(xsdQuery.getItem()) == len(self.listXsdFiles)):
#                self.DEBUG("xsdQuery=%s" % xsdQuery.marshal())
                self.xsdDataOut.setActualFile([XSDataFile(xsd) for xsd in xsdQuery.getItem() ])
        self.synchronizeOff()

    def doFailureAccumulator(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginWaitMultiFile.doFailureAccumulator")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginWaitMultiFile.doFailureAccumulator")
        self.ERROR("XSDataInput from EDPluginAccumulator that failed: \n%s" % _edPlugin.getDataInput().marshal())
        self.ERROR("XSDataResult from EDPluginAccumulator that failed: \n%s" % _edPlugin.getDataOutput().marshal())
        self.setFailure()
        self.synchronizeOff()


    def doSuccessWaitFile(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginWaitMultiFile.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginWaitMultiFile.doSuccessWaitFile")
        xsdFile = _edPlugin.getDataOutput().getActualFile()
        if _edPlugin.getDataOutput().getActualSize() is None:
            self.WARNING("Wait for file %s finished in timeout!" % _edPlugin.getDataInput().getExpectedFile().getPath().getValue())
            self.DEBUG("Please check why XSDataResultWaitFile is:\n%s" % _edPlugin.getDataOutput().marshal())
            self.DEBUG("This usually happens when EDPluginWaitFile has no configuration file or EDNA_SITE is undefined")
            self.setFailure()
        else:
            if _edPlugin.getDataOutput().getActualSize().getValue() < self.__actualMinSize:
                self.__actualMinSize = _edPlugin.getDataOutput().getActualSize().getValue()
            if _edPlugin.getDataOutput().getTimedOut().getValue():
                self.__bAnyTimeOut = True
            if xsdFile is not None:
                xsdiAccumulator = XSDataInputAccumulator()
                xsdiAccumulator.setItem([xsdFile.getPath()]) #Mandatory to be a list !!!
                edPluginAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
                edPluginAccumulator.setDataInput(xsdiAccumulator)
                edPluginAccumulator.connectSUCCESS(self.doSuccessAccumulator)
                edPluginAccumulator.connectFAILURE(self.doFailureAccumulator)
                edPluginAccumulator.execute()
                self.__listEdPluginsControled.append(edPluginAccumulator)
        self.synchronizeOff()

    def doFailureWaitFile(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginWaitMultiFile.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginWaitMultiFile.doFailureWaitFile")
        self.WARNING("XSDataResult from EDPluginWaitFile that failed: \n%s" % _edPlugin.getDataOutput().marshal())
        self.setFailure()
        self.synchronizeOff()






