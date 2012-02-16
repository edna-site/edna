# coding: utf8
#
#    Project: Exec Plugins: SPD
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2012 ESRF
#
#    Principal author:       Jérôme Kieffer (kieffer@esrf.fr)
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
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120213"

import os, sys
from EDVerbose                  import EDVerbose
from EDTestCasePluginUnit       import EDTestCasePluginUnit
from EDUtilsFile                import EDUtilsFile
from EDUtilsPath                import EDUtilsPath
from EDAssert                   import EDAssert
from EDFactoryPluginStatic      import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")

from XSDataSPDv1_0 import XSDataInputSPDCake
from spline import Spline
import fabio



class EDTestCasePluginUnitSPDCorrectv10(EDTestCasePluginUnit):
    """
    This is the unit test case for spd plugin
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginSPDCorrectv10")
        self.strReferenceInputFileName = os.path.join(self.getPluginTestsDataHome(), "XSDataInputSPDCorrect_simple.xml")
        self.loadTestImage(["MokeImage-2th21-tilt3-rot30.edf"])


    def testCheckParameters(self):
        edPluginSPD = self.createPlugin()
        strXMLInput = EDUtilsFile.readFileAndParseVariables(self.strReferenceInputFileName, {"${EDNA_TESTIMAGES}":"toto"})
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(strXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.checkParameters()


    def testKillAllWorkers(self):
        edPluginSPD = self.createPlugin()
        strXMLInput = EDUtilsFile.readFileAndParseVariables(self.strReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(strXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.killAllWorkers()

    def testSpatialDistortion(self):
        strRefX = "spline-3-18x.edf"
        strRefY = "spline-3-18y.edf"
        self.loadTestImage([strRefX, strRefY])
        edPluginSPD = self.createPlugin()
        strXMLInput = EDUtilsFile.readFileAndParseVariables(self.strReferenceInputFileName)
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(strXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.configure()
        edPluginSPD.getInputParameter()
        ########################################################################
        # Enforce some values
        ########################################################################
        edPluginSPD.dictGeometry["SpatialDistortionFile"] = os.path.join(self.getTestsDataImagesHome(), "frelon_spline_file_to_correct_SPD.spline")
        edPluginSPD.dictGeometry["TiltRotation"] = 18
        edPluginSPD.dictGeometry["AngleOfTilt"] = 3
        spline = Spline()
        spline.read(edPluginSPD.dictGeometry["SpatialDistortionFile"])
        edPluginSPD.dictGeometry["PixelSizeX"], edPluginSPD.dictGeometry["PixelSizeY"] = spline.getPixelSize()
        edPluginSPD.createDisplacementMatrix(spline)
        edPluginSPD.cleanDispMat(edPluginSPD.getWorkingDirectory())

        refX = fabio.openimage.openimage(os.path.join(self.getTestsDataImagesHome(), strRefX)).data
        obtX = fabio.openimage.openimage(os.path.join(edPluginSPD.getWorkingDirectory(), "frelon_spline_file_to_correct_SPD-tilted-x.edf")).data
        refY = fabio.openimage.openimage(os.path.join(self.getTestsDataImagesHome(), strRefY)).data
        obtY = fabio.openimage.openimage(os.path.join(edPluginSPD.getWorkingDirectory(), "frelon_spline_file_to_correct_SPD-tilted-y.edf")).data

#        print edPluginSPD.dictGeometry
        EDAssert.arraySimilar(obtX, refX , _fAbsMaxDelta=0.1, _strComment="X displacement Matrix is the same")
        EDAssert.arraySimilar(obtY, refY , _fAbsMaxDelta=0.1, _strComment="Y displacement Matrix is the same")

    def testCleanDispMat(self):
        edPluginSPD = self.createPlugin()
        strXMLInput = EDUtilsFile.readFileAndParseVariables(self.strReferenceInputFileName, EDUtilsPath.getDictOfPaths())
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(strXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        if EDVerbose.isVerboseDebug():
             edPluginSPD.cleanDispMat(edPluginSPD.getWorkingDirectory())
        else:
            edPluginSPD.cleanDispMat()


    def testGenerateSPDCommand(self):
        edPluginSPD = self.createPlugin()
        strXMLInput = EDUtilsFile.readFileAndParseVariables(self.strReferenceInputFileName, EDUtilsPath.getDictOfPaths())
        xsDataInputSPDCake = XSDataInputSPDCake.parseString(strXMLInput)
        edPluginSPD.setDataInput(xsDataInputSPDCake)
        edPluginSPD.configure()
        edPluginSPD.getInputParameter()
        #edPluginSPD.preProcess()
        edPluginSPD.generateSPDCommand()
        EDVerbose.screen("SPD configuration:\n%s" % edPluginSPD.getSPDConfig())
        if EDVerbose.isVerboseDebug():
            expected = """off_1=0 off_2=0 verbose=2 src_ext=.edf cor_ext=.cor wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_distortion=0 do_dark=0"""
            #"do_distortion=2 off_1=0 off_2=0  verbose=2 src_ext=.edf cor_ext=.cor wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_dark=0"
        else:
            expected = """off_1=0 off_2=0 verbose=0 src_ext=.edf cor_ext=.cor wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_distortion=0 do_dark=0"""
            #do_distortion=2 off_1=0 off_2=0  verbose=0 src_ext=.edf cor_ext=.cor wvl=1.000000e-10 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01 pix_1=4.722440e-05 pix_2=4.683150e-05 do_dark=0"
        EDAssert.equal(edPluginSPD.getSPDConfig(), expected)


    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testCleanDispMat)
        self.addTestMethod(self.testGenerateSPDCommand)
        self.addTestMethod(self.testKillAllWorkers)
        self.addTestMethod(self.testSpatialDistortion)

##############################################################################


if __name__ == '__main__':

    edTestCasePluginUnitSPDCorrectv10 = EDTestCasePluginUnitSPDCorrectv10("EDTestCasePluginUnitSPDCorrectv10")
    edTestCasePluginUnitSPDCorrectv10.execute()
