# coding: utf8 
#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
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


__author__ = "Jérôme Kieffer"
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"


from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from XSDataDiffractionCTv1 import XSDataInputReadHeader, XSDataResultReadHeader

class EDPluginControlDCTReadHeaderv1_0(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev1_0]
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputReadHeader)
        self.m_edStringControlledPluginName = "EDPluginEDFReadHeaderv1_0"
        self.m_edPluginEDFReadHeader = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.preProcess")
        # Load the execution plugin
        self.m_edPluginEDFReadHeader = self.loadPlugin(self.m_edStringControlledPluginName)
        # No data model handling needed for this plugin
        from XSDataEDFv1_0 import XSDataInputEDFReadHeader
        xsDataInputEDFReadHeader = XSDataInputEDFReadHeader()
        xsDataInputEDFReadHeader.setEdfFile(self.getDataInput().getInputFile())
        self.m_edPluginEDFReadHeader.setDataInput(xsDataInputEDFReadHeader)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.process")
        self.m_edPluginEDFReadHeader.connectSUCCESS(self.doSuccessExecTemplate)
        self.m_edPluginEDFReadHeader.connectFAILURE(self.doFailureExecTemplate)
        self.m_edPluginEDFReadHeader.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.postProcess")


    def doSuccessExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDCTReadHeaderv1_0.doSuccessExecTemplate")
        # Create some output data
        xsDataResultReadHeader = XSDataResultReadHeader()
        xsDataResultReadHeader.setDictionary(self.m_edPluginEDFReadHeader.getDataOutput().getDictionary())
        self.setDataOutput(xsDataResultReadHeader)


    def doFailureExecTemplate(self, _edPlugin=None):
        EDVerbose.DEBUG("*** EDPluginControlDCTReadHeaderv1_0.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDCTReadHeaderv1_0.doFailureExecTemplate")
