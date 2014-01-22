#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2014 European Synchrotron Radiation Facility
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsTest                         import EDUtilsTest


class EDTestCasePluginExecutePluginExecReadImageHeaderADSCv10(EDTestCasePluginExecute):


    def __init__(self, _strTestName="EDPluginExecReadImageHeaderADSCv10"):
        EDTestCasePluginExecute.__init__(self, _strTestName)
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputReadImageHeader_ADSC_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultReadImageHeader_ADSC_reference.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img" ])


    def testExecute(self):
        self.run()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecutePluginExecReadImageHeaderADSCv10 = EDTestCasePluginExecutePluginExecReadImageHeaderADSCv10("EDTestCasePluginExecutePluginExecReadImageHeaderADSCv10")
    edTestCasePluginExecutePluginExecReadImageHeaderADSCv10.execute()
