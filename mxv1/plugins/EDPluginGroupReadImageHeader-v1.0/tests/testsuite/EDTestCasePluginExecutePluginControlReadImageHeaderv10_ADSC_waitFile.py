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


import os, tempfile, shutil

from threading import Timer

from EDTestCasePluginExecutePluginControlReadImageHeaderv10 import EDTestCasePluginExecutePluginControlReadImageHeaderv10


class EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile(EDTestCasePluginExecutePluginControlReadImageHeaderv10):


    def __init__(self, _strTestName="EDPluginControlReadImageHeaderv10"):
        EDTestCasePluginExecutePluginControlReadImageHeaderv10.__init__(self, _strTestName)
        self.strTmpDir = tempfile.mkdtemp(prefix="EDPluginControlReadImageHeaderv10_")
        os.environ["EDNA_TMP_DIR"] = self.strTmpDir
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputReadImageHeader_ADSC_waitFile.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultReadImageHeader_ADSC_reference.xml"))
        self.strInputDataFile = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_001.img")
        self.strInputDataFileNew = os.path.join(self.strTmpDir, "ref-testscale_1_001.img")


    def preProcess(self):
        EDTestCasePluginExecutePluginControlReadImageHeaderv10.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img" ])


    def copyFile(self):
        shutil.copyfile(self.strInputDataFile, self.strInputDataFileNew)


    def testExecute(self):
        # Start a timer for copying the file
        pyTimer = Timer(5, self.copyFile)
        pyTimer.start()
        self.run()
        pyTimer.cancel()


    def process(self):
        self.addTestMethod(self.testExecute)

    def postProcess(self):
        EDTestCasePluginExecutePluginControlReadImageHeaderv10.postProcess(self)
        shutil.rmtree(self.strTmpDir)




if __name__ == '__main__':

    edTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile = EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile("EDTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile")
    edTestCasePluginExecutePluginControlReadImageHeaderv10_ADSC_waitFile.execute()
