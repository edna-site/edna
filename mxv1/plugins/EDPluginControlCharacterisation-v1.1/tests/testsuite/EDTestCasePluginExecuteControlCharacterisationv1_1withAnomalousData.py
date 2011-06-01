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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert
from EDUtilsTest                         import EDUtilsTest

from EDTestCasePluginExecuteControlCharacterisationv1_1 import EDTestCasePluginExecuteControlCharacterisationv1_1


class EDTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData(EDTestCasePluginExecuteControlCharacterisationv1_1):


    def __init__(self, _oedStringTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv1_1.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_withAnomalousData.xml"))






    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData = EDTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData("EDTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData")
    edTestCasePluginExecuteControlCharacterisationv1_1withAnomalousData.execute()
