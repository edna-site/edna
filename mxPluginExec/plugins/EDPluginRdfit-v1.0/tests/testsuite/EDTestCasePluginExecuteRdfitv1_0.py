#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#


__authors__ = ["Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20121004"
__status__ = "beta"

import os

from EDAssert                         import EDAssert
from EDTestCasePluginExecute          import EDTestCasePluginExecute



class EDTestCasePluginExecuteRdfitv1_0(EDTestCasePluginExecute):

    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginRdfitv1_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputRdfit_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultRdfit_reference.xml"))

    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "rdfit_01.HKL", "rdfit_03.HKL", "rdfit_05.HKL", "rdfit_07.HKL", \
                             "rdfit_09.HKL", "rdfit_11.HKL", "rdfit_13.HKL", "rdfit_15.HKL", \
                             "rdfit_17.HKL", "rdfit_19.HKL", "rdfit_21.HKL" ])

    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)

