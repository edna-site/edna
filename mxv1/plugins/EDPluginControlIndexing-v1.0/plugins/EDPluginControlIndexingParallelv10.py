#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose import EDVerbose
from EDPluginControlIndexingv10 import EDPluginControlIndexingv10

class EDPluginControlIndexingParallelv10(EDPluginControlIndexingv10):
    """
    This plugin can launch several control indexing plugins in parallel.
    
    Although the parallel execution is functional, there's yet to
    implementation of a ranking of the indexing results, hence this plugin
    is not yet operational.
    """

    def __init__ (self):
        EDPluginControlIndexingv10.__init__(self)
        self.setPluginIndexingExecutiveSummaryName("Parallel")
        self.setPluginIndexingName(None)
        self.__listPluginIndexingName = None
        self.__listPluginIndexing = None
        self.__xsDataIndexingResult = None


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControlIndexingv10.preProcess(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingParallelv10.preProcess...")
        self.__listPluginIndexingName = []
        self.__listPluginIndexing = []
        self.__listPluginIndexingName.append("EDPluginControlIndexingMOSFLMv10")
        self.__listPluginIndexingName.append("EDPluginControlIndexingLabelitv10")
        # Load the indexing plugins
        iIndex = 1
        for strPluginIndexingName in self.__listPluginIndexingName:
            strPluginIndexingBaseName = strPluginIndexingName + "-%02d" % iIndex
            edPluginIndexing = self.loadPlugin(strPluginIndexingName, strPluginIndexingBaseName)
            if (edPluginIndexing is not None):
                edPluginIndexing.setDataInput(self.getDataInput())
                self.__listPluginIndexing.append(edPluginIndexing)


    def process(self, _edObject=None):
        EDPluginControlIndexingv10.process(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingParallelv10.process")
        for edPluginIndexing in self.__listPluginIndexing:
            edPluginIndexing.connectSUCCESS(self.doSuccessActionIndexingParallel)
            edPluginIndexing.connectFAILURE(self.doFailureActionIndexingParallel)
            self.addPluginToActionCluster(edPluginIndexing)
        self.executeActionCluster()
        self.synchronizeActionCluster()


    def postProcess(self, _edObject=None):
        EDPluginControlIndexingv10.postProcess(self, _edObject)
        self.verboseDebug("EDPluginControlIndexingParallelv10.postProcess")
        self.setDataOutput(self.__xsDataIndexingResult)


    def doSuccessActionIndexingParallel(self, _edPlugin=None):
        self.verboseDebug("EDPluginControlIndexingParallelv10.doSuccessActionIndexing")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlIndexingParallelv10.doSuccessActionIndexing")
        # Retrieve the output from the plugin
        self.__xsDataIndexingResult = self.getDataIndexingResult(_edPlugin)


    def getDataIndexingResult(self, _edPlugin):
        """
        This method retrieves the indexing results from a MOSFLM indexing plugin.
        """
        self.verboseDebug("EDPluginControlIndexingParallelv10.getDataIndexingResult")
        return _edPlugin.getDataOutput()


    def doFailureActionIndexingParallel(self, _edPlugin=None):
        self.verboseDebug("EDPluginControlIndexingParallelv10.doFailureActionIndexing")
        EDVerbose.screen("Execution of " + _edPlugin.getName() + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlIndexingParallelv10.doFailureActionIndexing")


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.verboseDebug("EDPluginControlIndexingParallelv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of indexing with %s :" % self.strPluginIndexingName)
        self.addErrorWarningMessagesToExecutiveSummary("Indexing failure! Error messages: ")
        for edPluginIndexing in self.__listPluginIndexing:
            if (edPluginIndexing is not None):
                self.appendExecutiveSummary(edPluginIndexing, edPluginIndexing.getPluginName() + " : ")
