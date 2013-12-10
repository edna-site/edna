#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2013 European Synchrotron Radiation Facility
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, tempfile, shutil

from threading import Timer

from EDTestCasePluginExecute import EDTestCasePluginExecute
from EDUtilsPath import EDUtilsPath


class EDTestCasePluginExecuteControlImageQualityIndicatorsv1_3_waitFile(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlImageQualityIndicatorsv1_3")
        self.strTmpDir = tempfile.mkdtemp(prefix="EDPluginControlImageQualityIndicatorsv1_3_", dir=EDUtilsPath.getEdnaTestDataImagesPath())
        os.chmod(self.strTmpDir, 0755)
        if "EDNA_TMP_DIR" in os.environ.keys():
            self.strTmpDirOrig = os.environ["EDNA_TMP_DIR"]
        else:
            self.strTmpDirOrig = None
        os.environ["EDNA_TMP_DIR"] = self.strTmpDir
        self.setRequiredPluginConfiguration("EDPluginDistlSignalStrengthv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputControlImageQualityIndicators_waitFile.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultControlImageQualityIndicators_reference.xml"))
        self.strInputDataFile1 = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_001.img")
        self.strInputDataFile2 = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_002.img")
        self.strInputDataFileNew1 = None
        self.strInputDataFileNew2 = None


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])
        self.strInputDataFileNew1 = os.path.join(self.strTmpDir, "ref-testscale_1_001.img")
        self.strInputDataFileNew2 = os.path.join(self.strTmpDir, "ref-testscale_1_002.img")


    def copyFile(self):
        self.screen("Copying file %s to %s" % (self.strInputDataFile1, self.strInputDataFileNew1))
        shutil.copyfile(self.strInputDataFile1, self.strInputDataFileNew1)
        self.screen("Copying file %s to %s" % (self.strInputDataFile2, self.strInputDataFileNew2))
        shutil.copyfile(self.strInputDataFile2, self.strInputDataFileNew2)


    def testExecute(self):
        # Start a timer for copying the file
        pyTimer = Timer(5, self.copyFile)
        pyTimer.start()
        self.run()
        pyTimer.cancel()


    def process(self):
        self.addTestMethod(self.testExecute)

    def finallyProcess(self):
        EDTestCasePluginExecute.finallyProcess(self)
        shutil.rmtree(self.strTmpDir)
        if self.strTmpDirOrig is not None:
            os.environ["EDNA_TMP_DIR"] = self.strTmpDirOrig

