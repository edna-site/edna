#
#    Project: mxPluginExec
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath




class EDTestCasePluginExecuteBestv1_2(EDTestCasePluginExecute):


    def __init__(self, _oalStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBestv1_2")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputBest_reference.xml"))
        #
        # If on Linux, check if run on Intel processor
        #
        self.m_bRunOnIntel = False
        pyStrSystem = os.uname()[0]
        if (pyStrSystem == "Linux"):
            pyFile = open("/proc/cpuinfo", "r")
            pyListCpuInfo = pyFile.readlines()
            pyFile.close()
            for pyStrLine in pyListCpuInfo:
                if (pyStrLine.find("vendor_id") != -1):
                    if (pyStrLine.find("GenuineIntel") != -1):
                         self.m_bRunOnIntel = True
        if (self.m_bRunOnIntel):
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultBest_referenceForIntel.xml"))
        else:
            self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultBest_reference.xml"))


    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    edTestCasePluginExecuteBestv1_2 = EDTestCasePluginExecuteBestv1_2("EDTestCasePluginExecuteBestv1_2")
    edTestCasePluginExecuteBestv1_2.execute()
