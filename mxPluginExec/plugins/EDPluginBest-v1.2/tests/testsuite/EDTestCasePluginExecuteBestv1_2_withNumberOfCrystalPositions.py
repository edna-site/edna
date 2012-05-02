#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions.py 1943 2010-08-23 13:59:41Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath
from EDTestCasePluginExecuteBestv1_2     import EDTestCasePluginExecuteBestv1_2



class EDTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions(EDTestCasePluginExecuteBestv1_2):

    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecuteBestv1_2.__init__(self, "EDPluginBestv1_2")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputBest_withNumberOfCrystalPositions.xml"))
        if (self.m_bRunOnIntel):
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultBest_withNumberOfCrystalPositionsForIntel.xml"))
        else:
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultBest_withNumberOfCrystalPositions.xml"))

    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions = EDTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions("EDTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions")
    edTestCasePluginExecuteBestv1_2_withNumberOfCrystalPositions.execute()
