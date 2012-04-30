# coding: utf8
#
#    Project: execPlugins
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

import os
from EDVerbose          import EDVerbose
from EDPluginExec       import EDPluginExec
from EDUtilsArray       import EDUtilsArray
from EDUtilsPlatform   import EDUtilsPlatform
from XSDataShiftv1_0    import XSDataInputShiftImage
from XSDataShiftv1_0    import XSDataResultShiftImage
from XSDataCommon       import XSDataImageExt, XSDataString
from EDFactoryPluginStatic import EDFactoryPluginStatic
################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
scipy = EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)


try:
    from fabio.edfimage import edfimage
    import  scipy.ndimage
except Exception:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


class EDPluginExecShiftImagev1_0(EDPluginExec):
    """
    Shift image by a given value    
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputShiftImage)
        self.npaImage = None
        self.tOffset = (0., 0.)
        self.strOutputImage = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecShiftImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#No mandatory parameters

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecShiftImagev1_0.preProcess")
        sdi = self.getDataInput()
        if sdi.inputImage is not None:
            self.npaImage = numpy.array(EDUtilsArray.getArray(sdi.inputImage))
        elif  sdi.getInputArray() is not None:
            self.npaImage = EDUtilsArray.xsDataToArray(sdi.getInputArray())
        else:
            EDVerbose.ERROR("EDPluginExecShiftImagev1_0.preProcess: You should either provide an images or an arrays, but I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError

        offset = sdi.getOffset()
        if len(offset) == 2:
            self.tOffset = (offset[0].getValue(), offset[1].getValue())
        elif len(offset) == 1:
            self.tOffset = (offset[0].getValue(), offset[0].getValue())

        if sdi.getOutputImage() is not None:
            self.strOutputImage = sdi.getOutputImage().getPath().getValue()


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecShiftImagev1_0.process")
        if self.tOffset != (0., 0.):
            self.npaImage = scipy.ndimage.shift(self.npaImage, self.tOffset, order=3, mode="constant", cval=self.npaImage.min())


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecShiftImagev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultShiftImage()
        if self.strOutputImage is None:
            #ArrayOutput
            xsDataResult.setOutputArray(EDUtilsArray.arrayToXSData(self.npaImage))
        else:
            image = edfimage(data=self.npaImage, header={"Offset_1":self.tOffset[0], "Offset_2":self.tOffset[1]})
            image.write(self.strOutputImage, force_type=self.npaImage.dtype)
            xsdimg = XSDataImageExt(path=XSDataString(self.strOutputImage))
            xsDataResult.setOutputImage(xsdimg)
        self.setDataOutput(xsDataResult)

