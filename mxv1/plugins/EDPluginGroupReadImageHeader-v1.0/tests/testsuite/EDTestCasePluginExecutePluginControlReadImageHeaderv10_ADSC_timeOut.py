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

from threading import Timer

from EDTestCasePluginExecutePluginControlReadImageHeaderv10 import EDTestCasePluginExecutePluginControlReadImageHeaderv10


class EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_timeOut(EDTestCasePluginExecutePluginControlReadImageHeaderv10):


    def __init__(self, _strTestName="EDPluginControlReadImageHeaderv10"):
        EDTestCasePluginExecutePluginControlReadImageHeaderv10.__init__(self, _strTestName)
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputReadImageHeader_ADSC_timeOut.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultReadImageHeader_ADSC_reference.xml"))
        self.setNoExpectedErrorMessages(1)
        self.setAcceptPluginFailure(True)


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_timeOut = EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_timeOut("EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_timeOut")
    edTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_timeOut.execute()
