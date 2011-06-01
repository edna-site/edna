#
#    Project: EDNA MXv2
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


import os

from EDTestCasePluginExecuteControlKappaStrategyv2_0 import EDTestCasePluginExecuteControlKappaStrategyv2_0

class EDTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition(EDTestCasePluginExecuteControlKappaStrategyv2_0):

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecuteControlKappaStrategyv2_0.__init__(self, "EDPluginControlKappaStrategyv2_0")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputStrategy_reference_03.xml") , "mxv1InputStrategy")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "mxv2_XSDataCollection_reference.xml") , "mxv2DataCollection")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "mxv1_XSDataIndexingResult_reference.xml") , "mxv1IndexingResult")

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultStrategy_reference_03.xml"))




    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition = EDTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition("EDTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition")
    edTestCasePluginExecuteControlKappaStrategyv2_0WithoutChemComposition.execute()
