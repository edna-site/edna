# coding: utf8
#
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

import os, threading, time
from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDUtilsArray import EDUtilsArray
from XSDataShiftv1_0 import XSDataInputMeasureOffset, XSDataInputMeasureOffsetSift
from XSDataShiftv1_0 import XSDataResultMeasureOffset, XSDataInputSiftDescriptor
from XSDataCommon import XSDataBoolean, XSDataFile, XSDataString, XSDataInteger
from EDAssert import EDAssert
from EDActionCluster import EDActionCluster
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataExecThumbnail")
from XSDataExecThumbnail import XSDataInputExecThumbnail
from EDUtilsPlatform   import EDUtilsPlatform

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
scipy = EDFactoryPluginStatic.preImport("scipy", scipyPath)

try:
    from fabio.openimage import openimage
except:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")



class EDPluginExecMeasureOffsetv2_0(EDPluginControl):
    """
    An exec plugin that takes two images and measures the offset between the two.
    In facts it is not an ExecPlugin but a control plugin that:
    * Converts the pair of images in colored JPEG
    * Extract the SIFT descriptor of each image
    * Measure the offset between the two images using the Autopano tool
    * return the measured offset and the file describing the control points.
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMeasureOffset)
        self.__strControlledPluginThumbnail = "EDPluginExecThumbnailv10"
        self.__strControlledPluginSift = "EDPluginExecSiftDescriptorv1_0"
        self.__strControlledPluginAutopano = "EDPluginExecSiftOffsetv1_0"
        self.semThumbnail = threading.Semaphore()
        self.semSift = threading.Semaphore()
        self.ACThumbnail = EDActionCluster()
        self.ACSift = EDActionCluster()
        self.xsdImages = []
        self.xsdThumb = []
        self.xsdKeys = []
        self.xsdIdx = []
        self.tCrop = [0, 0]
        self.inputImages = []
        self.tOffset = None
        self.xsdPTO = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlMeasureOffsetv2_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.preProcess")
        sdi = self.getDataInput()

        crop = sdi.getCropBorders()
        if len(crop) == 2:
            self.tCrop = (crop[0].getValue(), crop[1].getValue())
        elif len(crop) == 1:
            self.tCrop = (crop[0].getValue(), crop[0].getValue())

#
        if len(sdi.getImage()) == 2:
            for i in sdi.getImage():

                array = openimage(i.getPath().getValue()).data
                shape = array.shape
                if (self.tCrop != [0, 0]) and (shape[0] > self.tCrop[0]) and (shape[1] > self.tCrop[1]):
                    array = array[self.tCrop[0]:-self.tCrop[0], self.tCrop[1]:-self.tCrop[1] ]
                    EDVerbose.DEBUG("After Crop, images have shape : (%s,%s) " % (array.shape))
                self.xsdImages.append(EDUtilsArray.arrayToXSData(array))
        elif len(sdi.getArray()) == 2:
            if (self.tCrop == [0, 0]) :
                self.xsdImages = sdi.getArray()
            else:
                for xsdArray  in  sdi.getArray():
                    array = EDUtilsArray.xsDataToArray(xsdArray)
                    shape = array.shape
                    if (shape[0] > self.tCrop[0]) and (shape[1] > self.tCrop[1]):
                        array = array[self.tCrop[0]:-self.tCrop[0], self.tCrop[1]:-self.tCrop[1] ]
                        EDVerbose.DEBUG("After Crop, images have shape : (%s,%s) " % (array.shape))
                    self.xsdImages.append(EDUtilsArray.arrayToXSData(array))
        else:
            strError = "EDPluginExecMeasureOffsetv2_0.preProcess: You should either provide two images or two arrays, but I got: %s" % sdi.marshal()
            EDVerbose.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.xsdImages len=%i %s" % (len(self.xsdImages), self.xsdImages))
        EDAssert.equal(self.xsdImages[0].getShape() , self.xsdImages[1].getShape(), "Images have the same size")
        self.xsdIdx = sdi.getIndex()
        if len(self.xsdIdx) < len(self.xsdImages):
            self.xsdIdx = [XSDataInteger(i) for i in range(len(self.xsdImages))]


    def process(self, _edObject=None):
        """
        """
        for  i in range(2):
            execPlugin = self.loadPlugin(self.__strControlledPluginThumbnail)
            xsdin = XSDataInputExecThumbnail()
            xsdin.setInputArray(self.xsdImages[i])
            xsdFile = XSDataFile()
            xsdFile.setPath(XSDataString(os.path.join(self.getWorkingDirectory(), "image%i.jpg" % self.xsdIdx[i].getValue())))
            xsdin.setOutputPath(xsdFile)
            xsdin.setLevelsColorize(XSDataBoolean(1))
            xsdin.setLevelsEqualize(XSDataBoolean(1))

            execPlugin.setDataInput(xsdin)
            execPlugin.connectSUCCESS(self.doSuccessThumb)
            execPlugin.connectFAILURE(self.doFailureThumb)
            self.ACThumbnail.addAction(execPlugin)
        self.ACThumbnail.execute()

        while len(self.xsdThumb) < 2:
            time.sleep(1)

        for  oneImage in self.xsdThumb:
            execPlugin = self.loadPlugin(self.__strControlledPluginSift)
            xsdin = XSDataInputSiftDescriptor()
            xsdin.setImage(oneImage)
            execPlugin.setDataInput(xsdin)
            execPlugin.connectSUCCESS(self.doSuccessSift)
            execPlugin.connectFAILURE(self.doFailureSift)
            self.ACSift.addAction(execPlugin)
        self.ACSift.execute()
#
#        else:
#            strError = "There are only %s images in self.xsdThumb" % len(self.xsdThumb)
#            EDVerbose.ERROR(strError)
#            self.setFailure()
#            raise RuntimeError(strError)

################################################################################
# This should be executed only after the Sift actions cluster finishes 
################################################################################
        while len(self.xsdKeys) < 2:
            time.sleep(1)

        execPlugin = self.loadPlugin(self.__strControlledPluginAutopano)
        xsdin = XSDataInputMeasureOffsetSift()
        xsdin.setDescriptorFile(self.xsdKeys)
        execPlugin.setDataInput(xsdin)
        execPlugin.connectSUCCESS(self.doSuccessAutopano)
        execPlugin.connectFAILURE(self.doFailureAutopano)
        execPlugin.executeSynchronous()




    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMeasureOffset()
        xsDataResult.setOffset(self.tOffset)
        xsDataResult.setPanoFile(self.xsdPTO)
        self.setDataOutput(xsDataResult)
        self.xsdImages = []

    def doSuccessThumb(self, _edPlugin=None):
        self.semThumbnail.acquire()
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doSuccessThumb")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doSuccessThumb")
        self.xsdThumb.append(_edPlugin.getDataOutput().getThumbnailPath())
        self.semThumbnail.release()


    def doFailureThumb(self, _edPlugin=None):
        self.semThumbnail.acquire()
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doFailureThumb")
        self.retrieveFailureMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doFailureThumb")
        self.setFailure()
        strError = "Error in converting to Jpeg with this input: %s" % _edPlugin.getDataInput().marshal()
        EDVerbose.ERROR(strError)
        self.semThumbnail.release()
        raise RuntimeError(strError)


    def doSuccessSift(self, _edPlugin=None):
        self.semSift.acquire()
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doSuccessSift")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doSuccessSift")
        self.xsdKeys.append(_edPlugin.getDataOutput().getDescriptorFile())
        self.semSift.release()


    def doFailureSift(self, _edPlugin=None):
        self.semSift.acquire()
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doFailureSift")
        self.retrieveFailureMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doFailureSift")
        self.setFailure()
        strError = "Error in extracting SIFT keys with this input: %s" % _edPlugin.getDataInput().marshal()
        EDVerbose.ERROR(strError)
        self.semSift.release()
        raise RuntimeError(strError)


    def doSuccessAutopano(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doSuccessAutopano")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doSuccessSift")
        self.tOffset = _edPlugin.getDataOutput().getOffset()
        self.xsdPTO = _edPlugin.getDataOutput().getPanoFile()


    def doFailureAutopano(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginExecMeasureOffsetv2_0.doFailureAutopano")
        self.retrieveFailureMessages(_edPlugin, "EDPluginExecMeasureOffsetv2_0.doFailureAutopano")
        self.setFailure()
        strError = "Error in Autopano execution of with this input: %s" % _edPlugin.getDataInput().marshal()
        EDVerbose.ERROR(strError)
        raise RuntimeError(strError)

