#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteControlImageQualityIndicatorsv1_1.py 1419 2010-04-26 07:08:07Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
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


import os

from threading import Timer

from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlImageQualityIndicatorsv1_1_waitFile(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlImageQualityIndicatorsv1_1")
        self.setRequiredPluginConfiguration("EDPluginDistlSignalStrengthv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputControlImageQualityIndicators_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultControlImageQualityIndicators_reference.xml"))
        self.strInputDataFile = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_001.img")
        self.strInputDataFileNew = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_001.img.renamed")



    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def moveFileBack(self):
        os.rename(self.strInputDataFileNew, self.strInputDataFile)


    def testExecute(self):
        os.rename(self.strInputDataFile, self.strInputDataFileNew)
        # Start a timer for copying the file
        pyTimer = Timer(5, self.moveFileBack)
        pyTimer.start()
        self.run()
        pyTimer.cancel()


    def process(self):
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':
    edTestCasePluginExecuteControlGeneratePredictionv10 = EDTestCasePluginExecuteControlImageQualityIndicatorsv1_1_waitFile("EDTestCasePluginExecuteControlImageQualityIndicatorsv1_1_waitFile")
    edTestCasePluginExecuteControlGeneratePredictionv10.execute()
