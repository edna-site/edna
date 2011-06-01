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


__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, sys, tempfile, threading, shutil, time, subprocess, signal
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller, installLibrary
from EDVerbose                  import EDVerbose
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDUtilsTest                import EDUtilsTest
from XSDataSPDv1_0              import XSDataInputSPD
from EDApplication              import EDApplication
from EDAssert                   import EDAssert
from EDFactoryPluginStatic      import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")

import fabio.openimage
from fabio.openimage import openimage

class EDTestCasePluginExecuteSPDCorrectv10(EDTestCasePluginExecute):
    """
    This is the unit test case for spd plugin to correct a tilted and noisy image.
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        self.refInput = "MokeImage-2th21-tilt3-rot30.edf"
        self.refOutput = "MokeImage-2th21-tilt3-rot30.cor.edf"
        EDTestCasePluginExecute.__init__(self, "EDPluginSPDCorrectv10")

        self.setConfigurationFile(self.getRefConfigFile())

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputSPDCorrect_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultSPDCorrect_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        strSplineFileName = "frelon_spline_file_to_correct_SPD.spline"
        strPathToSplineFile = os.path.join(self.getTestsDataImagesHome(), strSplineFileName)
        if (not os.path.exists(strPathToSplineFile)):
            shutil.copy(os.path.join(self.getPluginTestsDataHome(), strSplineFileName), \
                                  strPathToSplineFile)


    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ self.refInput, self.refOutput ])
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
        EDVerbose.DEBUG("outfile = %s" % xsDataResultSPD.getCorrectedFile().getPath().getValue())
        EDVerbose.DEBUG("reffile = %s" % os.path.join(self.getTestsDataImagesHome(), self.refOutput))
        outputData = openimage(xsDataResultSPD.getCorrectedFile().getPath().getValue()).data
        referenceData = openimage(os.path.join(self.getTestsDataImagesHome(), self.refOutput)).data
#        res = 100 * (abs(outputData - referenceData).max() - referenceData.min()) / (referenceData.max() - referenceData.min())
#        EDVerbose.screen("Maximum error = %.2f%%" % res)
#        EDAssert.equal((res < 5), True)
        EDAssert.arraySimilar(outputData, referenceData, "Simple comparison")
        EDAssert.arraySimilar(outputData, referenceData, _fAbsMaxDelta=0.01, _fScaledMaxDelta=0.05, _strComment="Images comparison")

#        EDAssert.arraySimilar(outputData, referenceData, _fRelMaxDelta=0.01, _strComment="Relative comparison")
#        EDAssert.arraySimilar(outputData, referenceData, _fRfactor=0.1, _strComment="R-factor comparison")

##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

    def makeRandomImage(self):
        """make a couple of images with  """
        self.npDark = numpy.random.random(self.__size)
        f = EDF.WriteImage(os.path.join(self.__testdir, "dark.edf"))


##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteSPDCorrectv10 = EDTestCasePluginExecuteSPDCorrectv10("EDTestCasePluginExecuteSPDCorrectv10")
    edTestCasePluginExecuteSPDCorrectv10.execute()
