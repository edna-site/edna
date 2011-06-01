#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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

"""
Unit test for multi-SPD caking
"""
__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose              import EDVerbose
from EDTestCasePluginUnit   import EDTestCasePluginUnit
from EDUtilsTest            import EDUtilsTest
from EDAssert               import EDAssert

from XSDataSPDv1_0 import XSDataInputSPDCake

class EDTestCasePluginUnitSPDCakev1_5(EDTestCasePluginUnit):
    """
    This is the unit test case for spd plugin
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginSPDCakev1_5")
        edStringPluginTestDataHome = self.getPluginTestsDataHome()
        self.m_edStringReferenceInputFileName = os.path.join(edStringPluginTestDataHome, "XSDataInputSPDCorrect_simple.xml")
        self.loadTestImage(["MokeImage-2th21-tilt3-rot30.edf"])


    def testCheckParameters(self):
        edPluginSPD = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(edStringXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.checkParameters()

    def testKillAllWorkers(self):
        edPluginSPD = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(edStringXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.killAllWorkers()

    def testCleanDispMat(self):
        edPluginSPD = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(edStringXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.cleanDispMat()

    def testGenerateSPDCommand(self):
        edPluginSPD = self.createPlugin()
        edStringXMLInput = EDUtilsTest.readAndParseFile(self.m_edStringReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(edStringXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.configure()
        edPluginSPD.getInputParameter()
        #edPluginSPD.preProcess()
        edPluginSPD.generateSPDCommand()
        EDVerbose.screen("SPD configuration:\n %s" % edPluginSPD.getSPDConfig())
        if EDVerbose.isVerboseDebug():
            expected = """off_1=0 off_2=0 verbose=2 src_ext=.edf wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_distortion=0 do_dark=0 cor_ext=.cor azim_int=1 azim_pass=0 azim_ext=.cor azim_r_num=1489"""
#            """do_distortion=2 off_1=0 off_2=0  verbose=2 src_ext=.edf wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_dark=0 cor_ext=.cor azim_int=1 azim_pass=0 azim_ext=.cor azim_r_num=1489"""
        else:
            expected = """off_1=0 off_2=0 verbose=0 src_ext=.edf wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_distortion=0 do_dark=0 cor_ext=.cor azim_int=1 azim_pass=0 azim_ext=.cor azim_r_num=1489"""
#            """do_distortion=2 off_1=0 off_2=0  verbose=0 src_ext=.edf wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_dark=0 cor_ext=.cor azim_int=1 azim_pass=0 azim_ext=.cor azim_r_num=1489"""

        EDAssert.equal(edPluginSPD.getSPDConfig(), expected)
    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testCleanDispMat)
        self.addTestMethod(self.testGenerateSPDCommand)
        self.addTestMethod(self.testKillAllWorkers)


##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitSPDCakev1_5 = EDTestCasePluginUnitSPDCakev1_5("EDTestCasePluginUnitSPDCakev1_5")
    edTestCasePluginUnitSPDCakev1_5.execute()
