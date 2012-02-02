#
# coding: utf8
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2010, ESRF, Grenoble"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataShiftv1_0 import XSDataInputShiftImage, XSDataResultShiftImage
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")


class EDTestCasePluginExecuteExecShiftImagev1_1(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin ShiftImagev1_1
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecShiftImagev1_1")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_ShiftImage.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputShiftImage_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultShiftImage_reference.xml"))

        self.image = "rhodo_f1_datanorm_0001.edf"
        self.outdir = "/tmp/edna-%s" % os.environ["USER"]

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([self.image ])
        if not os.path.isdir(self.outdir):
            os.makedirs(self.outdir)
        if os.path.exists(os.path.join(self.outdir, "shift.edf")):
            os.remove(os.path.join(self.outdir, "shift.edf"))


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultShiftImage.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), _fRelError=0.0, _fAbsError=0.3, _strComment="XML out are the same")


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testShiftImagev1_1instance = EDTestCasePluginExecuteControlShiftImagev1_1("EDTestCasePluginExecuteExecShiftImagev1_1")
    testShiftImagev1_1instance.execute()
