#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2.py 1682 2010-06-24 11:57:23Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2             import EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2
from EDAssert import EDAssert

class EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2_withDamPar(EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2.__init__(self, "EDPluginControlInterfaceToMXCuBEv1_2")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputMXCuBE_withDamPar.xml"))


    def preProcess(self):
        EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2.preProcess(self)
        self.loadTestImage([ "fewSpots_1_001.img" ])


    def testExecute(self):
        self.run()




    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlInterfaceToMXCuBEv1_2_withDamPar = EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2("EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_2_withDamPar")
    edTestCasePluginExecuteControlInterfaceToMXCuBEv1_2_withDamPar.execute()
