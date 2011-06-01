#
#    Project: EDNA MXv1
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Gleb Bourenkov" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlSubWedgeAssemblev1_1(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlSubWedgeAssemblev1_1", "EDPluginGroupInterface-v1.1", _edStringTestName)
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeAssemble_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultSubWedgeAssemble_reference.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteControlSubWedgeAssemblev1_1 = EDTestCasePluginExecuteControlSubWedgeAssemblev1_1("EDTestCasePluginExecuteControlSubWedgeAssemblev1_1")
    edTestCasePluginExecuteControlSubWedgeAssemblev1_1.execute()
