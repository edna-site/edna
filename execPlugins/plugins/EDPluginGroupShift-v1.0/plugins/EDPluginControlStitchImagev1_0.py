# coding: utf8
#
#    Project: execPlugins/shiftImage
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:        Jerome Kieffer
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
__date__ = "2011/05/09"
import os
from EDPluginControl import EDPluginControl
from XSDataShiftv1_0 import XSDataInputStitchImage, XSDataInteger, \
    XSDataResultStitchImage, XSDataFile, XSDataString, XSDataBoolean, XSDataInputMeasureOffset, \
    XSDataInputStitchOffsetedImage, OffsetedImage, XSDataDouble, XSDataImage, XSDataArray

from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPlatform        import EDUtilsPlatform
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", EDUtilsPlatform.architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)

class EDPluginControlStitchImagev1_0(EDPluginControl):
    """
    Control plugin doing automatic image alignment and stitching.
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputStitchImage)
        self.__strControlledPluginMeasure = "EDPluginExecMeasureOffsetv1_0"
        self.__strControlledPluginStitch = "EDPluginExecStitchOffsetedImagev1_0"
        self.lInputFiles = []
        self.xDummy = None
        self.xDeltaDummy = None
        self.xAutoscale = None
        self.xBlending = None
        self.xOutFile = None
        self.xMask = None
        self.result = None
        self.ndaDistance = None
        self.xCenter = []
        self.xWidth = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlStitchImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImages(), "No input Images")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlStitchImagev1_0.preProcess")
        self.lInputFiles = [ i.path.value for i in self.getDataInput().getInputImages() if os.path.isfile(i.path.value) ]
        l = len(self.lInputFiles)
        self.ndaDistance = numpy.zeros((l, l, 2), dtype="float32")
        self.xDummy = self.getDataInput().dummyValue
        self.xDeltaDummy = self.getDataInput().deltaDummy
        self.xOutFile = self.getDataInput().outputImage
        self.xAutoscale = self.getDataInput().autoscale
        self.xCenter = self.getDataInput().centerROI
        self.xWidth = self.getDataInput().widthROI
        self.xBlending = self.getDataInput().blending
        self.xMask = self.getDataInput().mask
        print [i.value for i in self.xCenter]
        print [i.value for i in self.xWidth]


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlStitchImagev1_0.process")
        for idx1, im1 in enumerate(self.lInputFiles[:-1]):
            for idx2, im2 in enumerate(self.lInputFiles[idx1 + 1:]):
                plugin = self.loadPlugin(self.__strControlledPluginMeasure)
                xsd = XSDataInputMeasureOffset()
                xsd.setImage([XSDataImage(XSDataString(im1)), XSDataImage(XSDataString(im2))])
                xsd.setIndex([XSDataInteger(idx1), XSDataInteger(idx2 + idx1 + 1)])
                xsd.setCenter(self.xCenter)
                xsd.setWidth(self.xWidth)
                plugin.setDataInput(xsd)
                plugin.connectSUCCESS(self.doSuccessExecMeasure)
                plugin.connectFAILURE(self.doFailureExecMeasure)
                plugin.execute()
        self.synchronizePlugins()
        d = (self.ndaDistance ** 2).sum(axis= -1).sum(axis= -1)
        ref = d.argmin()
        self.DEBUG("Offsets= %s\n Sum distances = %s\n using ref=%s " % (self.ndaDistance, d, ref))
        pluginStitch = self.loadPlugin(self.__strControlledPluginStitch)
        xsdIn = XSDataInputStitchOffsetedImage(autoscale=self.xAutoscale,
                                               blending=self.xBlending,
                                               dummyValue=self.xDummy,
                                               outputImage=self.xOutFile,
                                               centerROI=self.xCenter,
                                               widthROI=self.xWidth,
                                               mask=self.xMask)
        xsdImgs = []
        for idx, img in  enumerate(self.lInputFiles):
            offsetedImg = OffsetedImage(dummyValue=self.xDummy, deltaDummy=self.xDeltaDummy)
            offsetedImg.setOffset([XSDataDouble(self.ndaDistance[ref, idx, 0]), XSDataDouble(self.ndaDistance[ref, idx, 1])])
            offsetedImg.setFile(file=XSDataImage(path=XSDataString(value=img)))

            xsdImgs.append(offsetedImg)
        xsdIn.setInputImages(xsdImgs)
        pluginStitch.setDataInput(xsdIn)
        pluginStitch.connectSUCCESS(self.doSuccessExecStitch)
        pluginStitch.connectFAILURE(self.doFailureExecStitch)
        pluginStitch.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlStitchImagev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultStitchImage()
        if isinstance(self.result, (XSDataFile, XSDataImage)):
            xsDataResult.setOutputImage(self.result)
        elif isinstance(self.result, XSDataArray):
            xsDataResult.setOutputArray(self.result)
        self.setDataOutput(xsDataResult)
        self.result = None


    def doSuccessExecMeasure(self, _edPlugin=None):
        self.DEBUG("EDPluginControlStitchImagev1_0.doSuccessExecMeasure")
        self.synchronizeOn()
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlStitchImagev1_0.doSuccessExecMeasure")
        [idx1, idx2] = [i.value for i in _edPlugin.getDataInput().index]
        offset = [ i.value for i in  _edPlugin.getDataOutput().offset]
        self.DEBUG("Got offset %.3f,%.3f for pair %i %i" % (offset[0], offset[1], idx1, idx2))
        self.ndaDistance[idx1, idx2, 0] = offset[0]
        self.ndaDistance[idx1, idx2, 1] = offset[1]
        self.ndaDistance[idx2, idx1, 0] = -offset[0]
        self.ndaDistance[idx2, idx1, 1] = -offset[1]
        self.synchronizeOff()

    def doFailureExecMeasure(self, _edPlugin=None):
        self.DEBUG("EDPluginControlStitchImagev1_0.doFailureExecMeasure")

        self.retrieveFailureMessages(_edPlugin, "EDPluginControlStitchImagev1_0.doFailureExecMeasure")
        strErr = "%s-%s failed with XsdIn: %s " % (_edPlugin.getName(), _edPlugin.getId(), _edPlugin.getDataInput().marshal())
        self.ERROR(strErr)
        self.synchronizeOff()

    def doFailureExecStitch(self, _edPlugin=None):
        self.DEBUG("EDPluginControlStitchImagev1_0.doFailureExecStitch")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlStitchImagev1_0.doFailureExecStitch")
        strErr = "%s-%s failed with XsdIn: %s " % (_edPlugin.getName(), _edPlugin.getId(), _edPlugin.getDataInput().marshal())
        self.ERROR(strErr)
        self.synchronizeOff()

    def doSuccessExecStitch(self, _edPlugin=None):
        self.DEBUG("EDPluginControlStitchImagev1_0.doSuccessExecStitch")
        if self.xOutFile is None:
            self.result = _edPlugin.getDataOutput().getOutputArray()
        else:
            self.result = _edPlugin.getDataOutput().getOutputImage()
