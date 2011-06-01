# coding: utf8
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer
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
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"

import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataShiftv1_0                     import XSDataResultStitchOffsetedImage
from EDAssert                            import EDAssert
from EDUtilsPlatform                     import EDUtilsPlatform
from EDFactoryPluginStatic               import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

import numpy
import fabio


class EDTestCasePluginExecuteExecStitchOffsetedImagev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin StitchOffsetedImagev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginExecStitchOffsetedImagev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_StitchOffsetedImage.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputStitchOffsetedImage_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultStitchOffsetedImage_reference.xml"))
        self.outdir = "/tmp/edna-%s" % os.environ["USER"]
        self.outFile = os.path.join(self.outdir, "stitched.edf")
        self.refFile = os.path.join(self.getTestsDataImagesHome(), "AlignImg1.tif")

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/diff6105.edf 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "AlignImg1.tif", "AlignImg2.tif", "AlignImg3.tif" ])
        if not os.path.isdir(self.outdir):
            os.makedirs(self.outdir)
        if os.path.isfile(self.outFile):
            os.remove(self.outFile)

    def testExecute(self):
        """
        """
        self.run()
        xsdout = self.getPlugin().getDataOutput().marshal()
        print self.getReferenceDataOutputFile()
        xsdRef = XSDataResultStitchOffsetedImage.parseString(self.readAndParseFile(self.getReferenceDataOutputFile())).marshal()
        EDAssert.strAlmostEqual(xsdRef, xsdout, "Xsd are the same")
#        fabio.edfimage.edfimage(data=fabio.open(self.outFile).data - fabio.open(self.refFile).data).write("/tmp/delta.edf")
        EDAssert.arraySimilar(fabio.open(self.outFile).data, fabio.open(self.refFile).data, "Arrays are the same", _fAbsMaxDelta=1)

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



if __name__ == '__main__':

    testStitchOffsetedImagev1_0instance = EDTestCasePluginExecuteControlStitchOffsetedImagev1_0("EDTestCasePluginExecuteExecStitchOffsetedImagev1_0")
    testStitchOffsetedImagev1_0instance.execute()
