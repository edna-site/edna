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
__contact__ = "jerome.kieffer@esrf.fr"

import os, sys, threading, time
from EDVerbose                  import EDVerbose
from EDPluginControl            import EDPluginControl
from EDUtilsArray               import EDUtilsArray
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDUtilsPlatform            import EDUtilsPlatform
from EDUtilsParallel import EDUtilsParallel

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
EDFactoryPluginStatic.loadModule("EDPluginExecMeasureOffsetv1_0")
EDFactoryPluginStatic.loadModule("EDPluginExecShiftImagev1_0")
EDFactoryPluginStatic.loadModule("EDPluginHDF5StackImagesv10")
from EDPluginAccumulatorv1_0 import EDPluginAccumulatorv1_0


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)

EDVerbose.setTestOff()


class EDPluginControlAlignStackv1_0(EDPluginControl):
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
        self.xsdMeasureOffset = None
        self.hdf5ExtraAttributes = None
        self.xsdHDF5File = None
        self.xsdHDF5Internal = None
        self.bAlwaysMOvsRef = False

        self.semAccumulator = threading.Semaphore()
        self.semMeasure = threading.Semaphore()
        self.semShift = threading.Semaphore()

        self.__strControlledPluginAccumulator = "EDPluginAccumulatorv1_0"
        self.__strControlledPluginMeasure = "EDPluginExecMeasureOffsetv1_0"
        self.__strControlledPluginShift = "EDPluginExecShiftImagev1_0"
        self.__strControlledPluginHDF5 = "EDPluginHDF5StackImagesv10"

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAlignStackv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getHDF5File(), "No Output HDF5 file provided")
        self.checkMandatoryParameters(self.getDataInput().getInternalHDF5Path(), "No output HDF5 internal path provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.preProcess")

        sdi = self.getDataInput()
        self.xsdHDF5File = sdi.getHDF5File()
        self.xsdHDF5Internal = sdi.getInternalHDF5Path()
        self.hdf5ExtraAttributes = sdi.extraAttributes

        self.iFrames = [ xsd.getValue() for xsd in sdi.getIndex()]

#        print self.iFrames
        for idx, oneXSDFile in enumerate(sdi.getImage()):
            filename = oneXSDFile.getPath().getValue()
            self.xsdArrays.append(EDUtilsArray.arrayToXSData(fabio.open(filename).data))
#            print idx
            if len(self.iFrames) <= idx:
                number = ""
                basename = os.path.splitext(filename)[0]
                for i in basename[-1:0:-1]:
                    if i.isdigit():
                        number = i + number
                    else: break
                self.iFrames.append(int(number))
        for oneXSDArray in sdi.getArray():
            self.xsdArrays.append(oneXSDArray)
        if self.xsdArrays == []:
            strError = "EDPluginControlAlignStackv1_0.preProcess: You should either provide an images or an arrays, but I got: %s" % sdi.marshal()
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)


        self.xsdMeasureOffset = sdi.getMeasureOffset()
        if self.xsdMeasureOffset.getAlwaysVersusRef() is not None:
            self.bAlwaysMOvsRef = (self.xsdMeasureOffset.getAlwaysVersusRef().getValue() in [1, "true", "True", True])

        EDPluginControlAlignStackv1_0.__semaphore.acquire()
        if (EDPluginControlAlignStackv1_0.__iRefFrame is None):
            self.DEBUG("reference Frame is: %s" % sdi.getFrameReference().getValue())
            if  sdi.getFrameReference() is not None:
                EDPluginControlAlignStackv1_0.__iRefFrame = sdi.getFrameReference().getValue()
            else:
                EDPluginControlAlignStackv1_0.__iRefFrame = 0
        EDPluginControlAlignStackv1_0.__semaphore.release()

        if len(self.iFrames) != len(self.xsdArrays):
            self.ERROR("EDPluginControlAlignStackv1_0.preProcess: You should either provide an images with a frame number or precise it in the XML !  I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError
        else:
            for i in range(len(self.iFrames)):
                EDPluginControlAlignStackv1_0.addFrame(self.iFrames[i], self.xsdArrays[i])

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.process")

        for iFrame in self.iFrames:
            if self.bAlwaysMOvsRef:
                EDPluginControlAlignStackv1_0.__dictUsed[iFrame] = 1
            else:
                EDPluginControlAlignStackv1_0.__dictUsed[iFrame] = 2
            edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
            queryRaw = XSDataQuery()
            queryShift = XSDataQuery()
            queryRaw.setRemoveItems(XSDataBoolean(0))
            queryShift.setRemoveItems(XSDataBoolean(0))
            xsdataAcc = XSDataInputAccumulator()
            if EDPluginControlAlignStackv1_0.__iRefFrame < iFrame:
                if self.bAlwaysMOvsRef:
                    queryRaw.setItem([XSDataString("raw %04i" % (EDPluginControlAlignStackv1_0.__iRefFrame)), XSDataString("raw %04i" % iFrame)])
                    xsdataAcc.setQuery([queryRaw])
                else:
                    queryRaw.setItem([XSDataString("raw %04i" % (iFrame - 1)), XSDataString("raw %04i" % iFrame)])
                    queryShift.setItem([XSDataString("shift %04i" % i) for i in range(EDPluginControlAlignStackv1_0.__iRefFrame + 1, iFrame + 1)])
                    xsdataAcc.setQuery([queryRaw, queryShift])
            elif EDPluginControlAlignStackv1_0.__iRefFrame > iFrame:
                if self.bAlwaysMOvsRef:
                    queryRaw.setItem([ XSDataString("raw %04i" % iFrame), XSDataString("raw %04i" % (EDPluginControlAlignStackv1_0.__iRefFrame))])
                    xsdataAcc.setQuery([queryRaw])
                else:
                    queryRaw.setItem([XSDataString("raw %04i" % (iFrame + 1)), XSDataString("raw %04i" % iFrame)])
                    queryShift.setItem([XSDataString("shift %04i" % i) for i in range(EDPluginControlAlignStackv1_0.__iRefFrame - 1, iFrame - 1, -1)])
                    xsdataAcc.setQuery([queryRaw, queryShift])
            else:
                #We are the frame reference !!!!
                EDPluginControlAlignStackv1_0.__dictAbsShift[EDPluginControlAlignStackv1_0.__iRefFrame] = (0.0, 0.0)
                EDPluginControlAlignStackv1_0.__dictRelShift[EDPluginControlAlignStackv1_0.__iRefFrame] = (0.0, 0.0)
                xsdata = XSDataInputHDF5StackImages(chunkSegmentation=XSDataInteger(8),
                                                    forceDtype=XSDataString("float32"),
                                                    extraAttributes=self.hdf5ExtraAttributes,
                                                    internalHDF5Path=self.xsdHDF5Internal,
                                                    HDF5File=self.xsdHDF5File,
                                                    index=[XSDataInteger(iFrame)],
                                                    inputArray=[EDPluginControlAlignStackv1_0.__dictFrame[iFrame]])
                edPluginExecHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
                edPluginExecHDF5.setDataInput(xsdata)
                edPluginExecHDF5.connectSUCCESS(self.doSuccessExecStackHDF5)
                edPluginExecHDF5.connectFAILURE(self.doFailureExecStackHDF5)
                edPluginExecHDF5.execute()

            xsdataAcc.setItem([XSDataString("raw %04i" % iFrame)])
            edPluginExecAccumulator.setDataInput(xsdataAcc)
            edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
            edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
            edPluginExecAccumulator.execute()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.postProcess")
        # Create some output data
        self.synchronizePlugins()
        EDPluginControlAlignStackv1_0.__semaphore.acquire()
        for oneKey in list(EDPluginControlAlignStackv1_0.__dictFrame.keys()):
            if (oneKey in  EDPluginControlAlignStackv1_0.__dictUsed) and EDPluginControlAlignStackv1_0.__dictUsed[oneKey] < 1:
                self.DEBUG("EDPluginControlAlignStackv1_0.postProcess: pop frame %i" % oneKey)
                if not(self.bAlwaysMOvsRef and oneKey == EDPluginControlAlignStackv1_0.__iRefFrame):
                    EDPluginControlAlignStackv1_0.__dictFrame.pop(oneKey)
        EDPluginControlAlignStackv1_0.__semaphore.release()
        xsDataResult = XSDataResultAlignStack()
        xsDataResult.setHDF5File(self.xsdHDF5File)
        xsDataResult.setInternalHDF5Path(self.xsdHDF5Internal)
        self.setDataOutput(xsDataResult)
        self.emptyListOfLoadedPlugin()
        self.xsdArrays = []


    def doSuccessExecMeasureOffset(self, _edPlugin=None):
        self.semMeasure.acquire()
        self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecMeasureOffset")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecMeasureOffset")
        listIndex = [ i.getValue() for i in _edPlugin.getDataInput().getIndex()]
        listIndex.sort()
        if self.bAlwaysMOvsRef:
            if min(listIndex) < EDPluginControlAlignStackv1_0.__iRefFrame:
                iToShift, iRef = tuple(listIndex)
                EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift] = tuple([ -i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            else:
                iRef, iToShift = tuple(listIndex)
                EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift] = tuple([ i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            self.screen("Frame number %i has absolute offset of %.3f,%.3f" %
                                 (iToShift, EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift][0], EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift][1]))
            edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
            xsdata = XSDataInputShiftImage()
            xsdata.setIndex(XSDataInteger(iToShift))
            xsdata.setOffset([XSDataDouble(i) for i in EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift]])
            xsdata.setInputArray(EDPluginControlAlignStackv1_0.__dictFrame[iToShift])
            edPluginExecShift.setDataInput(xsdata)
            edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
            edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
            edPluginExecShift.execute()
            self.synchronizeOn()
            EDPluginControlAlignStackv1_0.__dictUsed[iRef] -= 1
            self.synchronizeOff()
        else:
            if min(listIndex) < EDPluginControlAlignStackv1_0.__iRefFrame:

                iToShift, iRef = tuple(listIndex)
                EDPluginControlAlignStackv1_0.__dictRelShift[iToShift] = tuple([ -i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            else:
                iRef, iToShift = tuple(listIndex)
                EDPluginControlAlignStackv1_0.__dictRelShift[iToShift] = tuple([ i.getValue() for i in _edPlugin.getDataOutput().getOffset()])
            self.screen("Frame number %i has relative offset of %.3f,%.3f" %
                                 (iToShift, EDPluginControlAlignStackv1_0.__dictRelShift[iToShift][0], EDPluginControlAlignStackv1_0.__dictRelShift[iToShift][1]))

            xsdata = XSDataInputAccumulator()
            xsdata.setItem([XSDataString("shift %04i" % iToShift)])
            edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
            edPluginExecAccumulator.setDataInput(xsdata)
            edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
            edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
            edPluginExecAccumulator.execute()
            self.synchronizeOn()
            EDPluginControlAlignStackv1_0.__dictUsed[iRef] -= 1
            self.synchronizeOff()
        self.semMeasure.release()
        self.removeLoadedPlugin(_edPlugin)


    def doFailureExecMeasureOffset(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecMeasureOffset")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecMeasureOffset")
        self.ERROR("Failure in execution of the MeasureOffset with input: %s and output %s" % (_edPlugin.getDataInput().marshal()[:1000], _edPlugin.getDataOutput().marshal()[:1000]))
        self.setFailure()
        self.removeLoadedPlugin(_edPlugin)


    def doSuccessExecShiftImage(self, _edPlugin=None):
        self.semShift.acquire()
        self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecShiftImage")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecShiftImage")
        xsdIdx = _edPlugin.getDataInput().getIndex()
        xsdata = XSDataInputHDF5StackImages(chunkSegmentation=XSDataInteger(8),
                                            forceDtype=XSDataString("float32"),
                                            extraAttributes=self.hdf5ExtraAttributes,
                                            internalHDF5Path=self.xsdHDF5Internal,
                                            HDF5File=self.xsdHDF5File,
                                            index=[xsdIdx],
                                            inputArray=[_edPlugin.getDataOutput().getOutputArray()])
        edPluginExecHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
        edPluginExecHDF5.setDataInput(xsdata)
        edPluginExecHDF5.connectSUCCESS(self.doSuccessExecStackHDF5)
        edPluginExecHDF5.connectFAILURE(self.doFailureExecStackHDF5)
        edPluginExecHDF5.execute()
        self.synchronizeOn()
        EDPluginControlAlignStackv1_0.__dictUsed[xsdIdx.value] -= 1
        self.synchronizeOff()
        self.semShift.release()
        self.removeLoadedPlugin(_edPlugin)


    def doFailureExecShiftImage(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecShiftImage")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecShiftImage")
        self.ERROR("Failure in execution of the ExecShiftImage with input: %s and output %s" % (_edPlugin.getDataInput().marshal()[:1000], _edPlugin.getDataOutput().marshal()[:1000]))
        self.setFailure()
        self.removeLoadedPlugin(_edPlugin)

    def doSuccessExecStackHDF5(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecStackHDF5")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecStackHDF5")


    def doFailureExecStackHDF5(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecStackHDF5")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecStackHDF5")
        self.ERROR("Failure in execution of the ExecStackHDF5 with input: %s " % (_edPlugin.getDataInput().marshal()[:1000]))
        if _edPlugin.getDataOutput() is not None:
            self.ERROR("Failure in execution of the ExecStackHDF5 with output %s" % (_edPlugin.getDataOutput().marshal()[:1000]))


    def doSuccessExecAccumultor(self, _edPlugin=None):
        self.semAccumulator.acquire()
        self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecAccumultor")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecAccumultor")
        for query in _edPlugin.getDataOutput().getQuery():
            self.addExtraTime(60)
            _edPlugin.addExtraTime(60)
            accType = query.getItem()[0].getValue().split()[0]
            listInt = [int(i.getValue().split()[1]) for i in query.getItem()]
#            self.screen("Processing Success Accumulator %s for %s" % (accType, listInt))
            if accType == "raw":
                listFrame = [EDPluginControlAlignStackv1_0.__dictFrame[i] for i in listInt]
                #this is a hack to prevent thousands of threads to be launched at once.
                EDUtilsParallel.semaphoreNbThreadsAcquire()
                EDUtilsParallel.semaphoreNbThreadsRelease()
                edPluginExecMeasure = self.loadPlugin(self.__strControlledPluginMeasure)
                xsdata = XSDataInputMeasureOffset()
                xsdata.setArray(listFrame)
                if self.xsdMeasureOffset is not None:
                    xsdata.setCropBorders(self.xsdMeasureOffset.getCropBorders())
                    xsdata.setSmoothBorders(self.xsdMeasureOffset.getSmoothBorders())
                    xsdata.setBackgroundSubtraction(self.xsdMeasureOffset.getRemoveBackground())
                if max(listInt) > EDPluginControlAlignStackv1_0.__iRefFrame:
                    listInt.sort()
                else:
                    listInt.sort(reverse=True)
#                self.screen("Processing Success Accumulator raw for %s" % (listInt))
                xsdata.setIndex([XSDataInteger(i) for i in listInt ])
                edPluginExecMeasure.setDataInput(xsdata)
                edPluginExecMeasure.connectSUCCESS(self.doSuccessExecMeasureOffset)
                edPluginExecMeasure.connectFAILURE(self.doFailureExecMeasureOffset)
                edPluginExecMeasure.execute()

            elif accType == "shift":
                shift_1 = 0.0
                shift_2 = 0.0

                for frame in listInt:
                    shift_1 += EDPluginControlAlignStackv1_0.__dictRelShift[frame][0]
                    shift_2 += EDPluginControlAlignStackv1_0.__dictRelShift[frame][1]
                if listInt[0] > EDPluginControlAlignStackv1_0.__iRefFrame:
                    iFrameShift = max(listInt)
#                    shift_1 *=1
#                    shift_2 *=1
                else:
                    iFrameShift = min(listInt)
#                    shift_1 *= -1
#                    shift_2 *= -1
                EDPluginControlAlignStackv1_0.__dictAbsShift[iFrameShift] = (shift_1, shift_2)
                self.screen("Frame number %i has absolute offset of %.3f,%.3f" % (iFrameShift, shift_1, shift_2))

                #this is a hack to prevent thousands of threads to be launched at once.
                EDUtilsParallel.semaphoreNbThreadsAcquire()
                EDUtilsParallel.semaphoreNbThreadsRelease()

                edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
                xsdata = XSDataInputShiftImage()
                xsdata.setIndex(XSDataInteger(iFrameShift))
                xsdata.setOffset([XSDataDouble(shift_1), XSDataDouble(shift_2)])
                xsdata.setInputArray(EDPluginControlAlignStackv1_0.__dictFrame[iFrameShift])
                edPluginExecShift.setDataInput(xsdata)
                edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
                edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
                edPluginExecShift.execute()
        self.DEBUG("Items: %s" % EDPluginAccumulatorv1_0.getItems())
        self.DEBUG("Queries: %s" % EDPluginAccumulatorv1_0.getQueries())
        self.semAccumulator.release()


    def doFailureExecAccumulator(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecAccumulator")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecAccumulator")
        self.ERROR("Failure in execution of the accumulator with input: %s and output %s" % (_edPlugin.getDataInput().marshal()[:1000], _edPlugin.getDataOutput().marshal()[:1000]))
        self.setFailure()

    @staticmethod
    def showData():
        EDVerbose.screen("*"*20 + "EDPluginControlAlignStackv1_0" + "*" * 20)
        EDVerbose.screen("Reference Frame: %s" % EDPluginControlAlignStackv1_0.__iRefFrame)
        if len(EDPluginControlAlignStackv1_0.__dictRelShift) < len(EDPluginControlAlignStackv1_0.__dictAbsShift):
            mydict = EDPluginControlAlignStackv1_0.__dictAbsShift.copy()
        else:
            mydict = EDPluginControlAlignStackv1_0.__dictRelShift.copy()
        for i in mydict:
            EDVerbose.screen("Frame %i relative: %s absolute: %s" % \
                             (i, EDPluginControlAlignStackv1_0.__dictRelShift.get(i), EDPluginControlAlignStackv1_0.__dictAbsShift.get(i)))
        items = EDPluginAccumulatorv1_0.getItems()
        items.sort()
        EDVerbose.screen("Items in the accumultor: %s" % (items))
        querylist = [" "] + [ str(i) for i in EDPluginAccumulatorv1_0.getQueries().keys()]
        EDVerbose.screen("Queries in the accumultor: " + os.linesep.join(querylist))
        EDVerbose.screen("Frames still in memory: %s" % list(EDPluginControlAlignStackv1_0.__dictFrame.keys()))


    @staticmethod
    def addFrame(index, value):
        """
        Just add the value to the dictionnary
        """
        EDPluginControlAlignStackv1_0.__semaphore.acquire()
        EDPluginControlAlignStackv1_0.__dictFrame[index] = value
        EDPluginControlAlignStackv1_0.__semaphore.release()


    @staticmethod
    def cleanUp():
        """
        Clean up of the dictionary containing images
        """
        EDPluginControlAlignStackv1_0.__semaphore.acquire()
        for oneFrame in EDPluginControlAlignStackv1_0.__dictFrame:
            if ((oneFrame - 1) in EDPluginControlAlignStackv1_0.__dictAbsShift) and ((oneFrame + 1) in EDPluginControlAlignStackv1_0.__dictAbsShift) and (oneFrame  in EDPluginControlAlignStackv1_0.__dictAbsShift):
                EDVerbose.DEBUG("Cleaning up frame nr: %s" % oneFrame)
                EDPluginControlAlignStackv1_0.__dictFrame.pop(oneFrame)
        EDPluginControlAlignStackv1_0.__semaphore.release()
