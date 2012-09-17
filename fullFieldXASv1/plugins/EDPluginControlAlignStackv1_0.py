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
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010-, European Synchrotron Radiation Facility, Grenoble"
__contact__ = "jerome.kieffer@esrf.fr"
__date__ = "20120613"
__status__ = "production"

import os, sys
if sys.version_info < (3, 0):
    from Queue import Queue
else:
    from queue import Queue
from EDVerbose                  import EDVerbose
from EDPluginControl            import EDPluginControl
from EDUtilsArray               import EDUtilsArray
from EDFactoryPlugin            import edFactoryPlugin as EDFactoryPluginStatic
from EDUtilsPlatform            import EDUtilsPlatform
from EDUtilsParallel            import EDUtilsParallel
from EDShare                    import EDShare
from EDThreading                import Semaphore
from EDUtilsPath                import EDUtilsPath
EDFactoryPluginStatic.loadModule("XSDataFullFieldXAS")
EDFactoryPluginStatic.loadModule("EDPluginAccumulatorv1_0")
from EDPluginAccumulatorv1_0    import EDPluginAccumulatorv1_0
from XSDataCommon               import XSDataString, XSDataBoolean, XSDataDouble, XSDataInteger, \
    XSDataImageExt
EDFactoryPluginStatic.loadModule("XSDataFullFieldXAS")
from XSDataFullFieldXAS         import XSDataInputAlignStack
from XSDataFullFieldXAS         import XSDataResultAlignStack
EDFactoryPluginStatic.loadModule("XSDataHDF5v1_0")
from XSDataHDF5v1_0             import XSDataInputHDF5StackImages
EDFactoryPluginStatic.loadModule("XSDataShiftv1_0")
from XSDataShiftv1_0            import XSDataInputShiftImage, XSDataInputMeasureOffset
EDFactoryPluginStatic.loadModule("XSDataAccumulatorv1_0")
from XSDataAccumulatorv1_0      import XSDataQuery, XSDataInputAccumulator
EDFactoryPluginStatic.loadModule("EDPluginAccumulatorv1_0")
EDFactoryPluginStatic.loadModule("EDPluginExecMeasureOffsetv1_0")
EDFactoryPluginStatic.loadModule("EDPluginExecShiftImagev1_0")
EDFactoryPluginStatic.loadModule("EDPluginHDF5StackImagesv10")
from EDPluginHDF5 import EDPluginHDF5


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
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
    __semaphore = Semaphore()
    MaxOffset = None

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputAlignStack)
        self.iFrames = []
        self.npArrays = []
        self.xsdMeasureOffset = None
        self.hdf5ExtraAttributes = None
        self.xsdHDF5File = None
        self.xsdHDF5Internal = None
        self.bAlwaysMOvsRef = True
        self.bDoAlign = True
        self.semAccumulator = Semaphore()
        self.semMeasure = Semaphore()
        self.semShift = Semaphore()
        self.lstSem = [self.locked(), self.semAccumulator, self.semMeasure, self.semShift]
        self.queue = Queue()
        self.__strControlledPluginAccumulator = "EDPluginAccumulatorv1_0"
        self.__strControlledPluginMeasureFFT = "EDPluginExecMeasureOffsetv1_0"
        self.__strControlledPluginMeasureSIFT = "EDPluginExecMeasureOffsetv2_0"
        self.__strControlledPluginShift = "EDPluginExecShiftImagev1_1"
        self.__strControlledPluginHDF5 = "EDPluginHDF5StackImagesv10"

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAlignStackv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.getHDF5File(), "No Output HDF5 file provided")
        self.checkMandatoryParameters(self.dataInput.getInternalHDF5Path(), "No output HDF5 internal path provided")
        self.checkMandatoryParameters(self.dataInput.images, "No images to process provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.preProcess")

        sdi = self.dataInput
        self.xsdHDF5File = sdi.HDF5File
        self.xsdHDF5Internal = sdi.internalHDF5Path
        self.hdf5ExtraAttributes = sdi.extraAttributes
        if  sdi.dontAlign is not None:
            self.bDoAlign = not(bool(sdi.dontAlign.value))

        self.iFrames = [ xsd.value for xsd in sdi.index]

        for idx, oneXSDFile in enumerate(sdi.images):
            self.npArrays.append(EDUtilsArray.getArray(oneXSDFile))
            if len(self.iFrames) <= idx:
                if (oneXSDFile.number is not None):
                    self.iFrames.append(oneXSDFile.number.value)
                elif oneXSDFile.path is not None :
                    number = ""
                    filename = oneXSDFile.path.value
                    basename = os.path.splitext(filename)[0]
                    for i in basename[-1:0:-1]:
                        if i.isdigit():
                            number = i + number
                        else: break
                    self.iFrames.append(int(number))

        if self.npArrays == []:
            strError = "EDPluginControlAlignStackv1_0.preProcess: You should either provide an images or an arrays, but I got: %s" % sdi.marshal()
            self.ERROR(strError)
            self.setFailure()

        self.xsdMeasureOffset = sdi.measureOffset
        if self.xsdMeasureOffset.alwaysVersusRef is not None:
            self.bAlwaysMOvsRef = bool(self.xsdMeasureOffset.alwaysVersusRef.value)

        with self.__class__.__semaphore:
            if (self.__class__.__iRefFrame is None):
                self.DEBUG("reference Frame is: %s" % sdi.frameReference.value)
                if  sdi.getFrameReference() is not None:
                    self.__class__.__iRefFrame = sdi.frameReference.value
                else:
                    self.__class__.__iRefFrame = 0

        if len(self.iFrames) == len(self.npArrays):
            for i, j in zip(self.iFrames, self.npArrays):
                self.addFrame(i, j)
        else:
            self.ERROR("EDPluginControlAlignStackv1_0.preProcess: You should either provide an images with a frame number or precise it in the XML !  I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.process")

        for iFrame in self.iFrames:
            edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
            queryRaw = XSDataQuery()
            queryShift = XSDataQuery()
            queryRaw.setRemoveItems(XSDataBoolean(False))
            queryShift.setRemoveItems(XSDataBoolean(False))
            xsdataAcc = XSDataInputAccumulator()
            if  (EDPluginControlAlignStackv1_0.__iRefFrame == iFrame) or (self.bDoAlign == False) :
                EDPluginControlAlignStackv1_0.__dictAbsShift[iFrame] = (0.0, 0.0)
                EDPluginControlAlignStackv1_0.__dictRelShift[iFrame] = (0.0, 0.0)
                self.hdf5_offset(index=iFrame, offset=[0.0, 0.0])
                edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
                xsdata = XSDataInputShiftImage(index=XSDataInteger(iFrame),
                                               offset=[XSDataDouble(i) for i in EDPluginControlAlignStackv1_0.__dictAbsShift[iFrame]],
                                               inputImage=self.getFrameRef(iFrame),
                                               outputImage=XSDataImageExt(shared=XSDataString("Shifted-%06i" % iFrame)))
                edPluginExecShift.setDataInput(xsdata)
                edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
                edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
                self.queue.put(edPluginExecShift)
                if (self.bDoAlign == False):
                    self.executeControlledPlugins()
                    return

            elif EDPluginControlAlignStackv1_0.__iRefFrame < iFrame:
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
            if (EDPluginControlAlignStackv1_0.__iRefFrame == iFrame):
                self.saveReferenceFrame(iFrame)

            xsdataAcc.setItem([XSDataString("raw %04i" % iFrame)])
            edPluginExecAccumulator.setDataInput(xsdataAcc)
            edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
            edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
            self.queue.put(edPluginExecAccumulator)
        self.executeControlledPlugins()

    def executeControlledPlugins(self):
        """
        Execute all plugins under control: 
        """
        bAllFinished = False
        while not bAllFinished:
            #acquire all semaphores to be sure no plugins are under configuration !
            for sem in self.lstSem:
                with sem:
                    pass
            if self.queue.empty():
                self.synchronizePlugins()
                bAllFinished = self.queue.empty()
            else:
                while not self.queue.empty():
                    try:
                        plugin = self.queue.get()
                    except Exception:
                        self.WARNING("In EDPluginControlAlignStackv1_0, exception in self.queue.get()")
                        break
                    else:
                        #this is a hack to prevent thousands of threads to be launched at once.
                        with EDUtilsParallel.getSemaphoreNbThreads():
                            pass
                        plugin.execute()
                self.synchronizePlugins()

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAlignStackv1_0.postProcess")
        self.executeControlledPlugins()
        self.synchronizePlugins()
        # Create some output data
        xsDataResult = XSDataResultAlignStack()
        xsDataResult.setHDF5File(self.xsdHDF5File)
        xsDataResult.setInternalHDF5Path(self.xsdHDF5Internal)
        self.setDataOutput(xsDataResult)
        self.emptyListOfLoadedPlugin()


    def doSuccessExecMeasureOffset(self, _edPlugin=None):
        with self.semMeasure:
            self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecMeasureOffset")
            self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecMeasureOffset")
            listIndex = [ i.getValue() for i in _edPlugin.dataInput.index]
            listIndex.sort()
            dataOutput = _edPlugin.dataOutput
            if self.bAlwaysMOvsRef:
                if min(listIndex) < EDPluginControlAlignStackv1_0.__iRefFrame:
                    iToShift, iRef = tuple(listIndex)
                    EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift] = tuple([ -i.getValue() for i in dataOutput.getOffset()])
                else:
                    iRef, iToShift = tuple(listIndex)
                    EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift] = tuple([ i.getValue() for i in dataOutput.getOffset()])
                self.screen("Frame number %i has absolute offset of %.3f,%.3f" %
                                     (iToShift, EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift][0], EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift][1]))
                edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
                xsdata = XSDataInputShiftImage(index=XSDataInteger(iToShift),
                                               offset=[XSDataDouble(i) for i in EDPluginControlAlignStackv1_0.__dictAbsShift[iToShift]],
                                               inputImage=self.getFrameRef(iToShift),
                                               outputImage=XSDataImageExt(shared=XSDataString("Shifted-%06i" % iToShift)))
                edPluginExecShift.setDataInput(xsdata)
                edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
                edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
                self.queue.put(edPluginExecShift)
            else:
                if min(listIndex) < EDPluginControlAlignStackv1_0.__iRefFrame:

                    iToShift, iRef = tuple(listIndex)
                    EDPluginControlAlignStackv1_0.__dictRelShift[iToShift] = tuple([ -i.value for i in dataOutput.offset])
                else:
                    iRef, iToShift = tuple(listIndex)
                    EDPluginControlAlignStackv1_0.__dictRelShift[iToShift] = tuple([ i.value for i in dataOutput.offset])
                self.screen("Frame number %i has relative offset of %.3f,%.3f" %
                                     (iToShift, EDPluginControlAlignStackv1_0.__dictRelShift[iToShift][0], EDPluginControlAlignStackv1_0.__dictRelShift[iToShift][1]))

                xsdata = XSDataInputAccumulator(item=[XSDataString("shift %04i" % iToShift)])
                edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
                edPluginExecAccumulator.setDataInput(xsdata)
                edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumultor)
                edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
                self.queue.put(edPluginExecAccumulator)


    def doFailureExecMeasureOffset(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecMeasureOffset")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecMeasureOffset")
        self.ERROR("Failure in execution of the MeasureOffset with input: %s and output %s" % (_edPlugin.dataInput.marshal()[:1000], _edPlugin.dataOutput.marshal()[:1000]))
        self.setFailure()


    def doSuccessExecShiftImage(self, _edPlugin=None):
        with self.semShift:
            edPluginExecHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
            self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecShiftImage")
            self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecShiftImage")
            xsdIdx = _edPlugin.dataInput.index
            self.__class__.MaxOffset = _edPlugin.MAX_OFFSET_VALUE
            self.hdf5_offset(index=xsdIdx.value, offset=[i.value for i in _edPlugin.dataInput.offset])
            xsdata = XSDataInputHDF5StackImages(chunkSegmentation=XSDataInteger(32),
                                                forceDtype=XSDataString("float32"),
                                                extraAttributes=self.hdf5ExtraAttributes,
                                                internalHDF5Path=self.xsdHDF5Internal,
                                                HDF5File=self.xsdHDF5File,
                                                index=[xsdIdx],
                                                inputImageFile=[_edPlugin.dataOutput.outputImage])
#                                                inputArray=[_edPlugin.dataOutput.outputArray])
            edPluginExecHDF5.setDataInput(xsdata)
            edPluginExecHDF5.connectSUCCESS(self.doSuccessExecStackHDF5)
            edPluginExecHDF5.connectFAILURE(self.doFailureExecStackHDF5)
            self.queue.put(edPluginExecHDF5)


    def doFailureExecShiftImage(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecShiftImage")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecShiftImage")
        self.ERROR("Failure in execution of the ExecShiftImage with input: %s and output %s" % (_edPlugin.dataInput.marshal()[:1000], _edPlugin.dataOutput.marshal()[:1000]))
        self.setFailure()

    def doSuccessExecStackHDF5(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecStackHDF5")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecStackHDF5")


    def doFailureExecStackHDF5(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecStackHDF5")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecStackHDF5")
        self.ERROR("Failure in execution of the ExecStackHDF5 with input: %s " % (_edPlugin.dataInput.marshal()[:1000]))
        if _edPlugin.dataOutput is not None:
            self.ERROR("Failure in execution of the ExecStackHDF5 with output %s" % (_edPlugin.dataOutput.marshal()[:1000]))


    def doSuccessExecAccumultor(self, _edPlugin=None):
        with self.semAccumulator:
            self.DEBUG("EDPluginControlAlignStackv1_0.doSuccessExecAccumultor")
            self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doSuccessExecAccumultor")
            for query in _edPlugin.dataOutput.getQuery():
                self.addExtraTime(60)
                _edPlugin.addExtraTime(60)
                accType = query.getItem()[0].getValue().split()[0]
                listInt = [int(i.getValue().split()[1]) for i in query.getItem()]
                if accType == "raw":
                    listFrame = [self.getFrameRef(i) for i in listInt]

                    xsdata = XSDataInputMeasureOffset(image=listFrame)
                    doSIFT = False
                    if self.xsdMeasureOffset is not None:
                        xsdata.setCropBorders(self.xsdMeasureOffset.getCropBorders())
                        xsdata.setSmoothBorders(self.xsdMeasureOffset.getSmoothBorders())
                        xsdata.setBackgroundSubtraction(self.xsdMeasureOffset.getRemoveBackground())
                        if self.xsdMeasureOffset.useSift is not None:
                            doSIFT = self.xsdMeasureOffset.useSift.value
                    if max(listInt) > EDPluginControlAlignStackv1_0.__iRefFrame:
                        listInt.sort()
                    else:
                        listInt.sort(reverse=True)
                    xsdata.setIndex([XSDataInteger(i) for i in listInt ])
                    if doSIFT:
                        edPluginExecMeasure = self.loadPlugin(self.__strControlledPluginMeasureSIFT)
                    else:
                        edPluginExecMeasure = self.loadPlugin(self.__strControlledPluginMeasureFFT)
                    edPluginExecMeasure.setDataInput(xsdata)
                    edPluginExecMeasure.connectSUCCESS(self.doSuccessExecMeasureOffset)
                    edPluginExecMeasure.connectFAILURE(self.doFailureExecMeasureOffset)
                    self.queue.put(edPluginExecMeasure)

                elif accType == "shift":
                    shift_1 = 0.0
                    shift_2 = 0.0

                    for frame in listInt:
                        shift_1 += EDPluginControlAlignStackv1_0.__dictRelShift[frame][0]
                        shift_2 += EDPluginControlAlignStackv1_0.__dictRelShift[frame][1]
                    if listInt[0] > EDPluginControlAlignStackv1_0.__iRefFrame:
                        iFrameShift = max(listInt)
                    else:
                        iFrameShift = min(listInt)
                    EDPluginControlAlignStackv1_0.__dictAbsShift[iFrameShift] = (shift_1, shift_2)
                    self.screen("Frame number %i has absolute offset of %.3f,%.3f" % (iFrameShift, shift_1, shift_2))

                    edPluginExecShift = self.loadPlugin(self.__strControlledPluginShift)
                    edPluginExecShift.dataInput = XSDataInputShiftImage(index=XSDataInteger(iFrameShift),
                                                   offset=[XSDataDouble(shift_1), XSDataDouble(shift_2)],
                                                   inputImage=self.getFrameRef(iFrameShift),
                                                   outputImage=XSDataImageExt(shared=XSDataString("Shifted-%06i" % iFrameShift)))

                    edPluginExecShift.connectSUCCESS(self.doSuccessExecShiftImage)
                    edPluginExecShift.connectFAILURE(self.doFailureExecShiftImage)
                    self.queue.put(edPluginExecShift)
            self.DEBUG("Items: %s" % EDPluginAccumulatorv1_0.getItems())
            self.DEBUG("Queries: %s" % EDPluginAccumulatorv1_0.getQueries())


    def doFailureExecAccumulator(self, _edPlugin=None):
        self.DEBUG("EDPluginControlAlignStackv1_0.doFailureExecAccumulator")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAlignStackv1_0.doFailureExecAccumulator")
        self.ERROR("Failure in execution of the accumulator with input: %s and output %s" % (_edPlugin.dataInput.marshal()[:1000], _edPlugin.dataOutput.marshal()[:1000]))
        self.setFailure()


    def saveReferenceFrame(self, iFrame):
        """
        Save the reference frame to the HDF5 file
        @param iFrame: frame number to save as reference frame
        """
        ref = "reference_frame"
        hdf5file = self.xsdHDF5File.path.value
        edpluginHDF5 = self.loadPlugin(self.__strControlledPluginHDF5)
        with edpluginHDF5.getFileLock(hdf5file):
            #Seems strange to redefine h5Grp but if there is a flush in between: h5Grp could be closed 
            entry = edpluginHDF5.getHDF5File(hdf5file)[self.xsdHDF5Internal.value]
            if ref in entry:
                del entry[ref]
            entry[ref] = self.getFrame(iFrame)
            entry[ref].attrs["index"] = iFrame


    def hdf5_offset(self, index, offset):
        with EDPluginHDF5.getFileLock(self.xsdHDF5File.path.value):
            grp = EDPluginHDF5.getHDF5File(self.xsdHDF5File.path.value)[self.xsdHDF5Internal.value]
            ds = grp["Offsets"]
            if self.MaxOffset:
                if "MaxOffset" not in ds.attrs:
                    ds.attrs["MaxOffset"] = self.MaxOffset
            ds[index, :] = offset


    @classmethod
    def showData(cls):
        EDVerbose.screen("*"*20 + "EDPluginControlAlignStackv1_0" + "*" * 20)
        EDVerbose.screen("Reference Frame: %s" % cls.__iRefFrame)
        if len(cls.__dictRelShift) < len(cls.__dictAbsShift):
            mydict = cls.__dictAbsShift.copy()
        else:
            mydict = cls.__dictRelShift.copy()
        lstTxt = []
        for i in mydict:
            txt = "Frame %4i:\t" % i
            rela = cls.__dictRelShift.get(i)
            abso = cls.__dictAbsShift.get(i)
            if rela:
                txt += "relative: (%.3f, %.3f)\t" % rela
            else:
                txt += "relative: %12s\t" % rela
            if abso:
                txt += "absolute:  (%.3f, %.3f)" % abso
            else:
                txt += "absolute:  %12s" % abso
            lstTxt.append(txt)
        EDVerbose.screen(os.linesep.join(lstTxt))
        items = EDPluginAccumulatorv1_0.getItems()
        items.sort()
        EDVerbose.screen("Items in the accumulator: %s" % (items))
        querylist = [" "] + [ str(i) for i in EDPluginAccumulatorv1_0.getQueries().keys()]
        EDVerbose.screen("Queries in the accumulator: " + os.linesep.join(querylist))


    @classmethod
    def addFrame(cls, index, value):
        """
        Just store the value to EDShare 
        """
        key = "Normalized-%06i" % int(index)
        if key not in EDShare:
            EDShare[key] = value


    @classmethod
    def getFrame(cls, index):
        """
        Just Retrieves the value from EDShare 
        """
        return EDShare["Normalized-%06i" % int(index)]


    @classmethod
    def getFrameRef(cls, index):
        """
        Just retrieves the reference in the EDShare store 
        @return: reference to the frame in EDShare
        @rtype: XSDataImageExt
        """
        return XSDataImageExt(shared=XSDataString("Normalized-%06i" % int(index)))


    @classmethod
    def cleanUp(cls):
        """
        Clean up of the dictionary containing images: Left for compatibility reasons
        """
        EDShare.flush()

