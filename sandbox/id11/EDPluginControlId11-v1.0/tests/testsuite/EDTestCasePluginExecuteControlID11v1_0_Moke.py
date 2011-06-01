#
#    Project: ID11
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF
#
#    Principal author:       Regis Perdreau
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
from XSDataID11v1_0 import XSDataResultID11

__author__ = "Regis Perdreau"
__license__ = "GPLv3+"
__copyright__ = "Copyright (c) 2011 ESRF"

import os

from EDVerbose                          import EDVerbose
from EDAssert                           import EDAssert
from EDTestCasePluginExecute            import EDTestCasePluginExecute
from EDFactoryPluginStatic              import EDFactoryPluginStatic
from XSDataID11v1_0                     import XSDataResultID11
EDFactoryPluginStatic.loadModule("EDPluginSPDCakev1_5")
from EDPluginSPDCakev1_5 import EDPluginSPDCakev1_5

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")


class EDTestCasePluginExecuteControlID11v1_0_Moke(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlID11v1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputID11_reference_Moke.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultID11_reference_Moke.xml"))

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        listFiles = ["moke.edf", "moke.spr", "moke.azim"]
        self.loadTestImage(listFiles)
        tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(tmpdir):
            os.mkdir(tmpdir)
        for i in os.listdir(tmpdir):
            if i in listFiles:
                os.remove(os.path.join(tmpdir, i))


    def testExecute(self):
        self.run()
        plugin = self.getPlugin()
        plugin.synchronize()
        xmlobtain = plugin.getDataOutput().marshal()
        xmlexpected = XSDataResultID11.parseString(self.readAndParseFile(self.getReferenceDataOutputFile())).marshal()
        EDAssert.strAlmostEqual(xmlexpected, xmlobtain, "XSData comparaison")
        #EDPluginSPDCakev1_5.killAllWorkers()
        outputData = open(plugin.getDataOutput().getOutputFile()[0].getPath().getValue(), "rb").read()
        referenceData = open(os.path.join(self.getTestsDataImagesHome(), "moke.spr"), "rb").read()

        EDAssert.strAlmostEqual(referenceData, outputData, " file are the same")

    def process(self):
        self.addTestMethod(self.testExecute)

    def postProcess(self):
        EDPluginSPDCakev1_5.killAllWorkers()





if __name__ == '__main__':

    edTestCasePluginExecuteControlID11v1_0 = EDTestCasePluginExecuteControlID11v1_0_Moke("EDTestCasePluginExecuteControlID11v1_0_Moke")
    edTestCasePluginExecuteControlID11v1_0.execute()
