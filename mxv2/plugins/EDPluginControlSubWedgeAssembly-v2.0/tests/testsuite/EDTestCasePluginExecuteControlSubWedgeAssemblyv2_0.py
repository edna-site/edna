#
#    Project: EDNA MXv
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0(EDTestCasePluginExecute):

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlSubWedgeAssemblyv2_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeAssemble_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultSubWedgeAssemble_reference.xml"), "mxv1Assemble")
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "mxv2_XSDataCollection_reference.xml"), "mxv2DataCollection")


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()
        #edPlugin = self.getPlugin()
        # Checks the expected result
#        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        from XSDataMXv1 import XSDataSubWedge
#        xsDataSubWedgeObtained = edPlugin.getDataOutput()
#        xsDataSubWedgeReference = XSDataSubWedge.parseString(strExpectedOutput)
#        EDVerbose.DEBUG("Checking obtained result...")
#        EDAssert.equal(xsDataSubWedgeReference.marshal(), xsDataSubWedgeObtained.marshal())




    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteControlSubWedgeAssemblyv2_0 = EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0("EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0")
    edTestCasePluginExecuteControlSubWedgeAssemblyv2_0.execute()
