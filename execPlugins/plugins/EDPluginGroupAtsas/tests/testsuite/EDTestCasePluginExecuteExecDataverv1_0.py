# coding: utf8
#
#    Project: templatev1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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

__author__="Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011 ESRF, Grenoble"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataAtsas                         import XSDataResultDataver

class EDTestCasePluginExecuteExecDataverv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin Dataverv1_0
    """
    
    def __init__(self, _strTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDataverv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_Dataver.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDataver_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDataver_reference.xml"))
                 
    def preProcess(self):
        """
        Download reference 1D curves
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "noise1.dat", "noise2.dat" ])
        

    def testExecute(self):
        """
        """ 
        self.run()
        xsdOut = self.getPlugin().getDataOutput()
        EDAssert.strAlmostEqual(XSDataResultDataver.parseFile(self.getReferenceDataOutputFile()).marshal(),
                                xsdOut.marshal() , "XSData are almost the same", _fAbsError=0.1)
        EDAssert.lowerThan(xsdOut.chi.value, 1.0, "Chi2 is lower than 1")
        EDAssert.equal(xsdOut.fidelity.value, 1.0, "Fidelity is 1")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        

if __name__ == '__main__':

    testDataverv1_0instance = EDTestCasePluginExecuteControlDataverv1_0("EDTestCasePluginExecuteExecDataverv1_0")
    testDataverv1_0instance.execute()
