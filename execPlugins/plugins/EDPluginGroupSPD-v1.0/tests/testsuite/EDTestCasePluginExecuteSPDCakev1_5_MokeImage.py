#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#                            INSTITUTE_LINE_2
#
#    Principal author:       Jerome KIEFFER (kieffer@esrf.fr)
#
#    Contributing author:    CONTRIBUTING_AUTHOR
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

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, sys, tempfile, threading, shutil, time, subprocess, signal
from EDVerbose                  import EDVerbose
from EDAssert                   import EDAssert
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDUtilsFile                import EDUtilsFile
from EDUtilsPlatform           import EDUtilsPlatform
from EDFactoryPluginStatic      import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDPluginEDFReadHeaderv1_0")

from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")

from    EdfFile     import EdfFile as EDF



class EDTestCasePluginExecuteSPDCakev1_5_MokeImage(EDTestCasePluginExecute):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        self.refInput = "MokeImage-2th21-tilt3-rot30.edf"
        self.refOutput = "MokeImage-2th21-tilt3-rot30.azim"
        EDTestCasePluginExecute.__init__(self, "EDPluginSPDCakev1_5", _edStringTestName)
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputSPDCakev1_5_MokeImage.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultSPDCakev1_5_MokeImage.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        strSplineFileName = "frelon_spline_file_to_correct_SPD.spline"
        strPathToSplineFile = os.path.join(self.getTestsDataImagesHome(), strSplineFileName)
        if (not os.path.isfile(strPathToSplineFile)):
            EDUtilsFile.copyFile(os.path.join(self.getPluginTestsDataHome(), strSplineFileName), \
                                  strPathToSplineFile)

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([self.refInput , self.refOutput ])
        tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(tmpdir):
            os.mkdir(tmpdir)
        if os.path.isfile(os.path.join(tmpdir, self.refOutput)):
            os.remove(os.path.join(tmpdir, self.refOutput))



    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()
        plugin.killAllWorkers()
        if EDVerbose.isVerboseDebug():
             plugin.cleanDispMat(plugin.getWorkingDirectory())
        else:
            plugin.cleanDispMat()


# Checking obtained results
        xsDataResultSPD = plugin.getDataOutput()
        outputData = EDF(xsDataResultSPD.getCakedFile().getPath().getValue()).GetData(0)
        referenceData = EDF(os.path.join(self.getTestsDataImagesHome(), self.refOutput)).GetData(0)
        relError = 100 * (abs(outputData - referenceData).max() - referenceData.min()) / (referenceData.max() - referenceData.min())
        absError = abs(outputData - referenceData).max()
        if relError > 5:
            EDAssert.lowerThan(relError, 5, "Maximum relative error = %.2f%%, Maximum Absolute Error %.2f" % (relError, absError))
        else:
            EDAssert.lowerThan(absError, 5, "Maximum relative error = %.2f%%, Maximum Absolute Error %.2f " % (relError, absError))


##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteSPDCakev1_5 = EDTestCasePluginExecuteSPDCakev1_5_MokeImage("EDTestCasePluginExecuteSPDCakev1_5_MokeImage")
    edTestCasePluginExecuteSPDCakev1_5.execute()
