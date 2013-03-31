# coding: utf8
#
#    Project: Time-Resolved EXAFS
#             http://www.edna-site.org
#
#    Copyright (C)      2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, numpy

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsArray import EDUtilsArray

from XSDataJesfv1_0 import XSDataInputJesf

class EDTestCasePluginUnitExecJesfv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Jesfv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecJesfv1_0")
              

    def testCheckParameters(self):
        xsDataInputJesf = XSDataInputJesf()
        numpyData = numpy.genfromtxt(os.path.join(self.getPluginTestsDataHome(),"spectra.dat"))
        xsDataArray = EDUtilsArray.arrayToXSData(numpyData)
        xsDataInputJesf.setData(xsDataArray)
        #print xsDataInputJesf.marshal()
        xsDataInputJesf.exportToFile(os.path.join(self.getPluginTestsDataHome(),"XSDataInputJesfv1_0_reference.xml"))
        edPluginExecJesf = self.createPlugin()
        edPluginExecJesf.setDataInput(xsDataInputJesf)
        edPluginExecJesf.checkParameters()
        
    def testReadJesfResults(self):
        edPluginExecJesf = self.createPlugin()
        edPluginExecJesf.setWorkingDirectory(self.getPluginTestsDataHome())
        edPluginExecJesf.setScriptLogFileName(os.path.join(self.getPluginTestsDataHome(), "jesf.log"))
        xsDataResultJesf = edPluginExecJesf.readJesfResults()
#        print xsDataResultJesf.marshal()
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testReadJesfResults)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecJesfv1_0 = EDTestCasePluginUnitExecJesfv1_0("EDTestCasePluginUnitExecJesfv1_0")
    edTestCasePluginUnitExecJesfv1_0.execute()
