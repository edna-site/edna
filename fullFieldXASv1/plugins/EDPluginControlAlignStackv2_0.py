# coding: utf8
#
#    Project: PROJECT Full Field XAS
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
#
#    Principal author:        Jérôme Kieffer
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
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"
__status__="probably broken ... do not use"
import os, sys, threading, time
from EDVerbose                  import EDVerbose
from EDPluginControl            import EDPluginControl
from EDUtilsArray               import EDUtilsArray
from EDUtilsPlatform           import EDUtilsPlatform
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon               import XSDataString, XSDataBoolean, XSDataDouble, XSDataInteger

EDFactoryPluginStatic.loadModule("XSDataFullFieldXAS")
from XSDataFullFieldXAS         import XSDataInputAlignStack
from XSDataFullFieldXAS         import XSDataResultAlignStack
EDFactoryPluginStatic.loadModule("XSDataHDF5v1_0")
from XSDataHDF5v1_0 import XSDataInputHDF5StackImages
EDFactoryPluginStatic.loadModule("XSDataShiftv1_0")
from XSDataShiftv1_0 import XSDataInputShiftImage, XSDataInputMeasureOffset
EDFactoryPluginStatic.loadModule("XSDataAccumulatorv1_0")
from XSDataAccumulatorv1_0 import XSDataQuery, XSDataInputAccumulator
EDFactoryPluginStatic.loadModule("EDPluginAccumulatorv1_0")
EDFactoryPluginStatic.loadModule("EDPluginExecMeasureOffsetv2_0")
EDFactoryPluginStatic.loadModule("EDPluginExecShiftImagev1_0")
EDFactoryPluginStatic.loadModule("EDPluginHDF5StackImagesv10")
from EDPluginAccumulatorv1_0 import EDPluginAccumulatorv1_0




################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "Fabio-r5080", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090711-SciPy-0.7.1", architecture)


if  os.path.isdir(numpyPath) and (numpyPath not in sys.path):
    sys.path.insert(1, numpyPath)

if  os.path.isdir(imagingPath) and (imagingPath not in sys.path):
    sys.path.insert(1, imagingPath)

if  os.path.isdir(fabioPath) and (fabioPath not in sys.path):
    sys.path.insert(1, fabioPath)
if  os.path.isdir(scipyPath) and (scipyPath not in sys.path):
    sys.path.insert(1, scipyPath)


try:
    from fabio.openimage import openimage
    import numpy, scipy.ndimage

except:
    EDVerbose.ERROR("Error in loading numpy,  PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


EDVerbose.setTestOff()


class EDPluginControlAlignStackv2_0(EDPluginControl):
    """
    This control plugin aligns a stack on images in a single HDF5 3D-structure 
    """
    __iRefFrame = None
    __dictRelShift = {}#key=frame number N, value= 2-tuple of shift relative to frame N-1
    __dictAbsShift = {}#key=frame number N, value= 2-tuple of shift relative to frame iRefFrame
    __dictFrame = {} #key=frame number N, value= XSD array ... needs to be cleaned up from time to time
    __semaphore = threading.Semaphore()
    __dictUsed = {} #Every frame is used twice: once as reference once for shifting (iframref is used 2x as reference


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputAlignStack)
        self.iFrames = []
        self.xsdArrays = []
        self.xsdCrop = []
        self.xsdSmooth = []
        self.xsdBgSub = None

        self.xsdHDF5File = None
        self.xsdHDF5Internal = None
        self.iRunning = 0 #the number of sub-plugin running
        self.bAlwaysMOvsRef = False

        self.semAccumulator = threading.Semaphore()
        self.semMeasure = threading.Semaphore()
        self.semShift = threading.Semaphore()

        self.__strControlledPluginAccumulator = "EDPluginAccumulatorv1_0"
        self.__strControlledPluginMeasure = "EDPluginExecMeasureOffsetv2_0"
        self.__strControlledPluginShift = "EDPluginExecShiftImagev1_0"
        self.__strControlledPluginHDF5 = "EDPluginHDF5StackImagesv10"

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getHDF5File(), "No Output HDF5 file provided")
        self.checkMandatoryParameters(self.getDataInput().getInternalHDF5Path(), "No output HDF5 internal path provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.preProcess")

        sdi = self.getDataInput()
        self.xsdHDF5File = sdi.getHDF5File()
        self.xsdHDF5Internal = sdi.getInternalHDF5Path()


        for oneXSDFile in sdi.getImage():
            filename = oneXSDFile.getPath().getValue()
            self.xsdArrays.append(EDUtilsArray.arrayToXSData(openimage(filename).data))
            basename = list(os.path.splitext(os.path.basename(filename))[0])
            basename.reverse()
            number = ""
            for i in basename:
                if i.isdigit():
                    number = i + number
                else: break
            self.iFrames.append(int(number))
        for oneXSDArray in sdi.getArray():
            self.xsdArrays.append(oneXSDArray)
        if self.xsdArrays == []:
            EDVerbose.ERROR("EDPluginControlAlignStackv2_0.preProcess: You should either provide an images or an arrays, but I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError

        if sdi.getIndex() != []:
            self.iFrames = [ xsd.getValue() for xsd in sdi.getIndex()]

        if sdi.getAlwaysMOvsRef() is not None:
            self.bAlwaysMOvsRef = (sdi.getAlwaysMOvsRef().getValue() in [1, True, "1", "true"])


        self.xsdCrop = sdi.getCropBordersMO()
        self.xsdSmooth = sdi.getSmoothBordersMO()
        self.xsdBgSub = sdi.getBackgroundSubtractionMO()



        if EDPluginControlAlignStackv2_0.__iRefFrame is None and sdi.getFrameReference() is not None:
            EDPluginControlAlignStackv2_0.__iRefFrame = sdi.getFrameReference().getValue()
        else:
            EDPluginControlAlignStackv2_0.__iRefFrame = 0

        if len(self.iFrames) != len(self.xsdArrays):
            EDVerbose.ERROR("EDPluginControlAlignStackv2_0.preProcess: You should either provide an images with a frame number or precise it in the XML !  I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError
        else:
            for i in range(len(self.iFrames)):
                EDPluginControlAlignStackv2_0.addFrame(self.iFrames[i], self.xsdArrays[i])

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.process")

        for iFrame in self.iFrames:
            if self.bAlwaysMOvsRef:
                EDPluginControlAlignStackv2_0.__dictUsed[iFrame] = 1
            else:
                EDPluginControlAlignStackv2_0.__dictUsed[iFrame] = 2
            edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
            queryRaw = XSDataQuery()
            queryShift = XSDataQuery()
            queryRaw.setRemoveItems(XSDataBoolean(0))
            queryShift.setRemoveItems(XSDataBoolean(0))
            xsdataAcc = XSDataInputAccumulator()
            if EDPluginControlAlignStackv2_0.__iRefFrame < iFrame:
                if self.bAlwaysMOvsRef:
                    queryRaw.setItem([XSDataString("raw %i" % (EDPluginControlAlignStackv2_0.__iRefFrame)), XSDataString("raw %i" % iFrame)])
                    xsdataAcc.setQuery([queryRaw])
                else:
                    queryRaw.setItem([XSDataString("raw %i" % (iFrame - 1)), XSDataString("raw %i" % iFrame)])
                    queryShift.setItem([XSDataString("shift %i" % i) for i in range(EDPluginControlAlignStackv2_0.__iRefFrame + 1, iFrame + 1)])
                    xsdataAcc.setQuery([queryRaw, queryShift])
            elif EDPluginControlAlignStackv2_0.__iRefFrame > iFrame:
                if self.bAlwaysMOvsRef:
                    queryRaw.setItem([ XSDataString("raw %i" % iFrame), XSDataString("raw %i" % (EDPluginControlAlignStackv2_0.__iRefFrame))])
                    xsdataAcc.setQuery([queryRaw])
                else:
                    queryRaw.setItem([XSDataString("raw %i" % (iFrame + 1)), XSDataString("raw %i" % iFrame)])
                    queryShift.setItem([XSDataString("shift %i" % i) for i in range(EDPluginControlAlignStackv2_0.__iRefFrame - 1, iFrame - 1, -1)])
                    xsdataAcc.setQuery([queryRaw, queryShift])
            else:
                #We are the frame reference !!!!
                EDPluginControlAlignStackv2_0.__dictAbsShift[EDPluginControlAlignStackv2_0.__iRefFrame] = (0.0, 0.0)
                EDPluginControlAlignStackv2_0.__dictRelShift[EDPluginControlAlignStackv2_0.__iRefFrame] = (0.0, 0.0)
                edPluginExecHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
                xsdata = XSDataInputHDF5StackImages()
                xsdata.setHDF5File(self.xsdHDF5File)
                xsdata.setInternalHDF5Path(self.xsdHDF5Internal)
                xsdata.setIndex([XSDataInteger(iFrame)])
                xsdata.setInputArray([EDPluginControlAlignStackv2_0.__dictFrame[iFrame]])
                edPluginExecHDF5.setDataInput(xsdata)
                edPluginExecHDF5.connectSUCCESS(self.doSuccessExecStackHDF5)
                edPluginExecHDF5.connectFAILURE(self.doFailureExecStackHDF5)
                self.synchronizeOn()
                self.iRunning += 1
                edPluginExecHDF5.execute()
                self.synchronizeOff()

            xsdataAcc.setItem([XSDataString("raw %i" % iFrame)])
            edPluginExecAccumulator.setDataInput(xsdataAcc)
            edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
            edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
            self.synchronizeOn()
            self.iRunning += 1
            edPluginExecAccumulator.execute()
            self.synchronizeOff()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.postProcess")
        # Create some output data
        while self.iRunning > 0:
            EDVerbose.DEBUG("Number of sub-plugins still running: %i" % self.iRunning)
            time.sleep(1)
        EDPluginControlAlignStackv2_0.__semaphore.acquire()
        for oneKey in list(EDPluginControlAlignStackv2_0.__dictFrame.keys()):
            if (oneKey in  EDPluginControlAlignStackv2_0.__dictUsed) and EDPluginControlAlignStackv2_0.__dictUsed[oneKey] < 1:
                EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.postProcess: pop frame %i" % oneKey)
                if not(self.bAlwaysMOvsRef and oneKey == EDPluginControlAlignStackv2_0.__iRefFrame):
                    EDPluginControlAlignStackv2_0.__dictFrame.pop(oneKey)
        EDPluginControlAlignStackv2_0.__semaphore.release()
        xsDataResult = XSDataResultAlignStack()
        xsDataResult.setHDF5File(self.xsdHDF5File)
        xsDataResult.setInternalHDF5Path(self.xsdHDF5Internal)
        EDVerbose.DEBUG(xsDataResult.marshal())
        self.setDataOutput(xsDataResult)


    def doSuccessExecMeasureOffset(self, _edPlugin=None):
        self.semMeasure.acquire()
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doSuccessExecMeasureOffset")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doSuccessExecMeasureOffset")
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        listIndex = [ i.getValue() for i in _edPlugin.getDataInput().getIndex()]
        listIndex.sort()
        if self.bAlwaysMOvsRef:
            if min(listIndex) < EDPluginControlAlignStackv2_0.__iRefFrame:
                iToShift, iRef = tuple(listIndex)
                EDPluginControlAlignStackv2_0.__dictAbsShift[iToShift] = tuple([ -i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            else:
                iRef, iToShift = tuple(listIndex)
                EDPluginControlAlignStackv2_0.__dictAbsShift[iToShift] = tuple([ i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
        #                EDVerbose.screen("Frame number %i has absolute offset of %.3f,%.3f" % (iToShift, shift_1, shift_2))
            edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
            xsdata = XSDataInputShiftImage()
            xsdata.setIndex(XSDataInteger(iToShift))
            xsdata.setOffset([XSDataDouble(i) for i in EDPluginControlAlignStackv2_0.__dictAbsShift[iToShift]])
            xsdata.setInputArray(EDPluginControlAlignStackv2_0.__dictFrame[iToShift])
            edPluginExecShift.setDataInput(xsdata)
            edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
            edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
            self.synchronizeOn()
            self.iRunning += 1
            edPluginExecShift.execute()
            EDVerbose.DEBUG("Decrease ref for %i" % iRef)
            EDPluginControlAlignStackv2_0.__dictUsed[iRef] -= 1
            self.synchronizeOff()
        else:
            if min(listIndex) < EDPluginControlAlignStackv2_0.__iRefFrame:

                iToShift, iRef = tuple(listIndex)
                EDPluginControlAlignStackv2_0.__dictRelShift[iToShift] = tuple([ -i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            else:
                iRef, iToShift = tuple(listIndex)
                EDPluginControlAlignStackv2_0.__dictRelShift[iToShift] = tuple([ i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            xsdata = XSDataInputAccumulator()
            xsdata.setItem([XSDataString("shift %i" % iToShift)])
            edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
            edPluginExecAccumulator.setDataInput(xsdata)
            edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
            edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
            self.synchronizeOn()
            self.iRunning += 1
            edPluginExecAccumulator.execute()
            EDVerbose.DEBUG("Decrease ref for %i" % iRef)
            EDPluginControlAlignStackv2_0.__dictUsed[iRef] -= 1
            self.synchronizeOff()

        self.semMeasure.release()


    def doFailureExecMeasureOffset(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doFailureExecMeasureOffset")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doFailureExecMeasureOffset")
        if  _edPlugin.getDataOutput().marshal() is None:
            EDVerbose.ERROR("Failure in execution of the MeasureOffset with input: %s " % _edPlugin.getDataInput().marshal())
        else:
            EDVerbose.ERROR("Failure in execution of the MeasureOffset with input: %s and output %s" % (_edPlugin.getDataInput().marshal(), _edPlugin.getDataOutput().marshal()))
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        self.setFailure()


    def doSuccessExecShiftImage(self, _edPlugin=None):
        self.semShift.acquire()
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doSuccessExecShiftImage")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doSuccessExecShiftImage")
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        edPluginExecHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
        xsdata = XSDataInputHDF5StackImages()
        xsdata.setHDF5File(self.xsdHDF5File)
        xsdata.setInternalHDF5Path(self.xsdHDF5Internal)
        xsdIdx = _edPlugin.getDataInput().getIndex()
        xsdata.setIndex([xsdIdx])
        xsdata.setInputArray([_edPlugin.getDataOutput().getOutputArray()])
        edPluginExecHDF5.setDataInput(xsdata)
        edPluginExecHDF5.connectSUCCESS(self.doSuccessExecStackHDF5)
        edPluginExecHDF5.connectFAILURE(self.doFailureExecStackHDF5)
        self.synchronizeOn()
        self.iRunning += 1
        edPluginExecHDF5.execute()
        EDVerbose.DEBUG("Decrease ref for %i" % xsdIdx.getValue())
        EDPluginControlAlignStackv2_0.__dictUsed[xsdIdx.getValue()] -= 1
        self.synchronizeOff()
        self.semShift.release()


    def doFailureExecShiftImage(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doFailureExecShiftImage")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doFailureExecShiftImage")
        if  _edPlugin.getDataOutput().marshal() is None:
            EDVerbose.ERROR("Failure in execution of the ExecShiftImage with input: %s " % _edPlugin.getDataInput().marshal())
        else:
            EDVerbose.ERROR("Failure in execution of the ExecShiftImage with input: %s and output %s" % (_edPlugin.getDataInput().marshal(), _edPlugin.getDataOutput().marshal()))
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        self.setFailure()


    def doSuccessExecStackHDF5(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doSuccessExecStackHDF5")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doSuccessExecStackHDF5")
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()


    def doFailureExecStackHDF5(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doFailureExecStackHDF5")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doFailureExecStackHDF5")
        if  _edPlugin.getDataOutput().marshal() is None:
            EDVerbose.ERROR("Failure in execution of the ExecStackHDF5 with input: %s " % _edPlugin.getDataInput().marshal())
        else:
            EDVerbose.ERROR("Failure in execution of the ExecStackHDF5 with input: %s and output %s" % (_edPlugin.getDataInput().marshal(), _edPlugin.getDataOutput().marshal()))
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()

        self.setFailure()


    def doSuccessExecAccumultor(self, _edPlugin=None):
        self.semAccumulator.acquire()
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doSuccessExecAccumultor")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doSuccessExecAccumultor")
        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        for query in _edPlugin.getDataOutput().getQuery():
            accType = query.getItem()[0].getValue().split()[0]
            listInt = [int(i.getValue().split()[1]) for i in query.getItem()]
#            EDVerbose.screen("Processing Success Accumulator %s for %s" % (accType, listInt))
            if accType == "raw":
                listFrame = [EDPluginControlAlignStackv2_0.__dictFrame[i] for i in listInt]
                edPluginExecMeasure = self.loadPlugin(self.__strControlledPluginMeasure)
                xsdata = XSDataInputMeasureOffset()
                xsdata.setArray(listFrame)
                xsdata.setCropBorders(self.xsdCrop)
                xsdata.setSmoothBorders(self.xsdSmooth)
                xsdata.setBackgroundSubtraction(self.xsdBgSub)
                if max(listInt) > EDPluginControlAlignStackv2_0.__iRefFrame:
                    listInt.sort()
                else:
                    listInt.sort(reverse=True)
#                EDVerbose.screen("Processing Success Accumulator raw for %s" % (listInt))
                xsdata.setIndex([XSDataInteger(i) for i in listInt ])
                edPluginExecMeasure.setDataInput(xsdata)
                edPluginExecMeasure.connectSUCCESS(self.doSuccessExecMeasureOffset)
                edPluginExecMeasure.connectFAILURE(self.doFailureExecMeasureOffset)
                self.synchronizeOn()
                self.iRunning += 1
                edPluginExecMeasure.execute()
                self.synchronizeOff()

            elif accType == "shift":
                shift_1 = 0.0
                shift_2 = 0.0

                for frame in listInt:
                    shift_1 += EDPluginControlAlignStackv2_0.__dictRelShift[frame][0]
                    shift_2 += EDPluginControlAlignStackv2_0.__dictRelShift[frame][1]
                if listInt[0] > EDPluginControlAlignStackv2_0.__iRefFrame:
                    iFrameShift = max(listInt)
#                    shift_1 *=1
#                    shift_2 *=1
                else:
                    iFrameShift = min(listInt)
#                    shift_1 *= -1
#                    shift_2 *= -1
                EDPluginControlAlignStackv2_0.__dictAbsShift[iFrameShift] = (shift_1, shift_2)
#                EDVerbose.screen("Frame number %i has absolute offset of %.3f,%.3f" % (iFrameShift, shift_1, shift_2))
                edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
                xsdata = XSDataInputShiftImage()
                xsdata.setIndex(XSDataInteger(iFrameShift))
                xsdata.setOffset([XSDataDouble(shift_1), XSDataDouble(shift_2)])
                xsdata.setInputArray(EDPluginControlAlignStackv2_0.__dictFrame[iFrameShift])
                edPluginExecShift.setDataInput(xsdata)
                edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
                edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
                self.synchronizeOn()
                self.iRunning += 1
                edPluginExecShift.execute()
                self.synchronizeOff()
        EDVerbose.DEBUG("Items: %s" % EDPluginAccumulatorv1_0.getItems())
        EDVerbose.DEBUG("Queries: %s" % EDPluginAccumulatorv1_0.getQueries())
        self.semAccumulator.release()


    def doFailureExecAccumulator(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlAlignStackv2_0.doFailureExecAccumulator")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv2_0.doFailureExecAccumulator")
        if  _edPlugin.getDataOutput().marshal() is None:
            EDVerbose.ERROR("Failure in execution of the accumulator with input: %s " % _edPlugin.getDataInput().marshal())
        else:
            EDVerbose.ERROR("Failure in execution of the accumulator with input: %s and output %s" % (_edPlugin.getDataInput().marshal(), _edPlugin.getDataOutput().marshal()))

        self.synchronizeOn()
        self.iRunning -= 1
        self.synchronizeOff()
        self.setFailure()

    @staticmethod
    def showData():
        EDVerbose.screen("*"*20 + "EDPluginControlAlignStackv2_0" + "*" * 20)
        EDVerbose.screen("Reference Frame: %s" % EDPluginControlAlignStackv2_0.__iRefFrame)
        if len(EDPluginControlAlignStackv2_0.__dictRelShift) < len(EDPluginControlAlignStackv2_0.__dictAbsShift):
            mydict = EDPluginControlAlignStackv2_0.__dictAbsShift
        else:
            mydict = EDPluginControlAlignStackv2_0.__dictRelShift
        for i in mydict:
            EDVerbose.screen("Frame %i relative: %s absolute: %s" % \
                             (i, EDPluginControlAlignStackv2_0.__dictRelShift.get(i), EDPluginControlAlignStackv2_0.__dictAbsShift.get(i)))
        items = EDPluginAccumulatorv1_0.getItems()
        items.sort()
        EDVerbose.screen("Items in the accumultor: %s" % (items))
        querylist = [" "] + [ str(i) for i in EDPluginAccumulatorv1_0.getQueries().keys()]
        EDVerbose.screen("Queries in the accumultor: " + os.linesep.join(querylist))
        EDVerbose.screen("Frames still in memory: %s" % list(EDPluginControlAlignStackv2_0.__dictFrame.keys()))


    @staticmethod
    def addFrame(index, value):
        """
        Just add the value to the dictionnary
        """
        EDPluginControlAlignStackv2_0.__semaphore.acquire()
        EDPluginControlAlignStackv2_0.__dictFrame[index] = value
        EDPluginControlAlignStackv2_0.__semaphore.release()


    @staticmethod
    def cleanUp():
        """
        Clean up of the dictionary containing images
        """
        EDPluginControlAlignStackv2_0.__semaphore.acquire()
        for oneFrame in EDPluginControlAlignStackv2_0.__dictFrame:
            if ((oneFrame - 1) in EDPluginControlAlignStackv2_0.__dictAbsShift) and ((oneFrame + 1) in EDPluginControlAlignStackv2_0.__dictAbsShift) and (oneFrame  in EDPluginControlAlignStackv2_0.__dictAbsShift):
                EDVerbose.DEBUG("Cleaning up frame nr: %s" % oneFrame)
                EDPluginControlAlignStackv2_0.__dictFrame.pop(oneFrame)
        EDPluginControlAlignStackv2_0.__semaphore.release()
