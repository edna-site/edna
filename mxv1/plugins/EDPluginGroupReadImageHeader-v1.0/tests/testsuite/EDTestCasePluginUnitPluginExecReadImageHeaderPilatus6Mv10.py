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

from EDTestCasePluginUnit import EDTestCasePluginUnit

class EDTestCasePluginUnitPluginExecReadImageHeaderPilatus6Mv10(EDTestCasePluginUnit):


    def __init__(self, _strTestName="EDPluginExecReadImageHeaderPilatus6Mv10"):
        EDTestCasePluginUnit.__init__(self, _strTestName)


    def testReadHeaderPilatus6M(self):
        edPluginExecReadImageHeaderPilatus6Mv10 = self.createPlugin()
        self.loadTestImage([ "FAE_1_1_00001.cbf" ])
        strPathToTestImage = os.path.join(self.getTestsDataImagesHome(), "FAE_1_1_00001.cbf")
        dictObtained = edPluginExecReadImageHeaderPilatus6Mv10.readHeaderPilatus6M(strPathToTestImage)



    def process(self):
        """
        """
        self.addTestMethod(self.testReadHeaderPilatus6M)


if __name__ == '__main__':

    edTestCasePluginUnitPluginExecReadImageHeaderPilatus6Mv10 = EDTestCasePluginUnitPluginExecReadImageHeaderPilatus6Mv10("EDTestCasePluginUnitPluginExecReadImageHeaderPilatus6Mv10")
    edTestCasePluginUnitPluginExecReadImageHeaderPilatus6Mv10.execute()

