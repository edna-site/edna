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

from EDPluginControlIndexingv10 import EDPluginControlIndexingv10

from XSDataCommon import XSDataBoolean

class EDPluginControlIndexingMOSFLMv10(EDPluginControlIndexingv10):
    """
    This plugin is derived from EDPluginControlIndexingv10, and implements
    only the specific parts needed for executing the MOSFLM execution plugin.
    """

    def __init__ (self):
        EDPluginControlIndexingv10.__init__(self)
        self.setPluginIndexingName("EDPluginMOSFLMIndexingv10")
        self.setPluginIndexingExecutiveSummaryName("MOSFLM")
        self.setGeneratePredictionImage(True)
        self.__xsDataMOSFLMIndexingInput = None


    def setDataInput(self, _dataInput):
        """
        Sets the Plugin input data. A part from using the EDPlugin.setDataInput method,
        this method also converts the input data to the MOSFLM specific data model indexing input.
        """
        self.verboseDebug("EDPluginControlIndexingMOSFLMv10.setDataInput")
        EDPluginControlIndexingv10.setDataInput(self, _dataInput)
        # Convert the input data to MOSFLM specific input data
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        self.__xsDataMOSFLMIndexingInput = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(self.getDataInput())


    def loadPluginIndexingInputData(self):
        self.verboseDebug("EDPluginControlIndexingMOSFLMv10.loadPluginIndexingInputData...")
        self.getPluginIndexing().setDataInput(self.__xsDataMOSFLMIndexingInput)


    def getDataIndexingResult(self, _edPlugin):
        """
        This method retrieves the indexing results from a MOSFLM indexing plugin.
        """
        self.verboseDebug("EDPluginControlIndexingv10.getDataIndexingResultFromMOSFLM")
        xsDataMOSFLMOutputIndexing = _edPlugin.getDataOutput()
        from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10
        xsDataIndexingResult = EDHandlerXSDataMOSFLMv10.generateXSDataIndexingResult(xsDataMOSFLMOutputIndexing, self.getExperimentalCondition())
        xsDataIndexingResult.setLabelitIndexing(XSDataBoolean(False))
        return xsDataIndexingResult

