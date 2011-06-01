#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) Copyright (c) 2011 ESRF
#
#    Principal author:        Regis Perdreau
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

__author__ = "Regis Perdreau"
__license__ = "GPLv3+"
__copyright__ = "Copyright (c) 2011 ESRF"

import os

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsTest import EDUtilsTest
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataSPDv1_0")
from XSDataSPDv1_0 import XSDataInputSPDCake

from XSDataID11v1_0 import XSDataInputID11

from XSDataCommon import XSDataString, XSDataBoolean
from XSDataCommon import XSDataFile


class EDTestCasePluginUnitControlID11v1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlID11v1_0")
        self.dictID11Reference = {'1 DEGREE AZ': 'NO',
 'ANGLE OF TILT': '-0.63004673688',
 'AZIMUTH BINS': '36',
 'CONSERVE INT.': 'NO',
 'DARK CURRENT': 'YES',
 'DC FILE': os.path.join(EDUtilsTest.getTestsDataImagesHome(), "ID11-Dark.edf"),
 'DIM1_DATA': '2048',
 'DIM2_DATA': '2048',
 'DISTANCE': '136.908',
 'END AZIMUTH': '360',
 'FF FILE': os.path.join(EDUtilsTest.getTestsDataImagesHome(), "ID11-Flat.edf"),
 'FF MULTIPLIER': '1000.000',
 'FF SCALE': 'NO',
 'FLAT-FIELD': 'YES',
 'GEOMETRY COR.': 'YES',
 'INNER RADIUS': '5',
 'MASK FILE': 'None',
 'OUTER RADIUS': '1000',
 'POLARISATION': 'YES',
 'RADIAL BINS': '20',
 'SCAN TYPE': '2-THETA',
 'SD FILE': os.path.join(EDUtilsTest.getTestsDataImagesHome(), "ID11-Frelon.spline"),
 'SPATIAL DIS.': 'YES',
 'START AZIMUTH': '0.0',
 'TILT ROTATION': '-2.51342948328',
 'USE MASK': 'NO',
 'WAVELENGTH': '0.2952',
 'X-BEAM CENTRE': '1002.509',
 'X-PIXEL SIZE': '50',
 'Y-BEAM CENTRE': '999.6282',
 'Y-PIXEL SIZE': '50',
 'input_extn': 'edf',
 'output_extn': 'spr',
 'saving_format': 'SPREAD SHEET',
 'output_dir' : "/tmp/edna-" + os.environ["USER"]}


    def preProcess(self):
        """
        """
        EDTestCasePluginUnit.preProcess(self)
        self.loadTestImage(["ID11-Dark.edf", "ID11-Flat.edf", "ID11-Frelon.spline"])
        tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(tmpdir):
            os.mkdir(tmpdir)


    def testCheckParameters(self):
        xsDataInput = XSDataInputID11()
        xsDataInput.setParameterFile(XSDataFile(XSDataString("/dummy/path")))
        edPluginControlID11 = self.createPlugin()
        edPluginControlID11.setDataInput(xsDataInput)
        edPluginControlID11.checkParameters()


    def testParseParameterFile(self):
        edPluginControlID11 = self.createPlugin()
        # Path to test parameter file
        strDataPath = self.getPluginTestsDataHome()
        strTestParameterFile = "id11_parameterFile_reference.txt"
        strPath = os.path.join(strDataPath, strTestParameterFile)
        dictID11 = edPluginControlID11.parseParameterFiles(strPath)
#        dictSub = os.environ.copy()
#        dictSub["TEST_DATA_IMAGES_HOME"] = EDUtilsTest.getTestsDataImagesHome()
#        for keyId11 in dictID11:
#            for key in dictSub:
#                dictID11[keyId11] = dictID11[keyId11].replace("${%s}" % key , dictSub[ key ])
        EDAssert.equal(self.dictID11Reference, dictID11, "Dictionaries are the same")

    def testPopulateXSDataInputSPDCake(self):
        edPluginControlID11 = self.createPlugin()
        xsDataInputSPDCake = edPluginControlID11.populateXSDataInputSPDCake(self.dictID11Reference)
        strDataPath = self.getPluginTestsDataHome()
        strReferenceFile = "XSDataInputSPDCake_fromDict.xml"
        strPath = os.path.join(strDataPath, strReferenceFile)
        xsDataInputSPDCakeReference = XSDataInputSPDCake.parseString(self.readAndParseFile(strPath))
        xsDataInputSPDCakeReference.setDeleteCorImg(XSDataBoolean(not(EDVerbose.isVerboseDebug())))
        EDAssert.equal(xsDataInputSPDCakeReference.marshal(), xsDataInputSPDCake.marshal())


    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testParseParameterFile)
        self.addTestMethod(self.testPopulateXSDataInputSPDCake)



if __name__ == '__main__':

    EDTestCasePluginUnitControlID11v1_0 = EDTestCasePluginUnitControlID11v1_0("EDTestCasePluginUnitControlID11v1_0")
    EDTestCasePluginUnitControlID11v1_0.Execute()
