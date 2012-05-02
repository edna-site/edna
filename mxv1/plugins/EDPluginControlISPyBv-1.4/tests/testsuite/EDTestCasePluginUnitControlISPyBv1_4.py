#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Olof Svensson, Karl Levik"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from XSDataMXv1             import XSDataInputControlISPyB
from XSDataMXv1             import XSDataResultCharacterisation

class EDTestCasePluginUnitControlISPyBv1_4(EDTestCasePluginUnit):

    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlISPyBv1_4")


    def testCheckParameters(self):
        xsDataInputControlISPyB = XSDataInputControlISPyB()
        xsDataResultCharacterisation = XSDataResultCharacterisation()
        xsDataInputControlISPyB.setCharacterisationResult(xsDataResultCharacterisation)
        edPluginControlISPyB = self.createPlugin()
        edPluginControlISPyB.setDataInput(xsDataInputControlISPyB)
        edPluginControlISPyB.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    edTestCasePluginUnitControlISPyBv1_4 = EDTestCasePluginUnitControlISPyBv1_4("EDTestCasePluginUnitControlISPyBv1_4")
    edTestCasePluginUnitControlISPyBv1_4.execute()
