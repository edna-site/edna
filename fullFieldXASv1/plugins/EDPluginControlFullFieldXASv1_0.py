#coding: utf8
#
#    Project: Full Field XRay Absorption Spectroscopy
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010-2011, ESRF, Grenoble
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
__copyright__ = "2011, ESRF, Grenoble"
__contact__ = "jerome.kieffer@esrf.eu"

import threading, os, time
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataFullFieldXAS")
EDFactoryPluginStatic.loadModule("EDPluginHDF5")
EDFactoryPluginStatic.loadModule("EDPluginExecNormalizeImagev1_0")
from EDPluginHDF5           import EDPluginHDF5
from EDUtilsPlatform        import EDUtilsPlatform
from EDUtilsArray           import EDUtilsArray
from XSDataFullFieldXAS     import XSDataInputFullFieldXAS, XSDataResultFullFieldXAS, \
                                XSDataInputAlignStack, XSDataHDF5Attributes
from XSDataNormalizeImage   import XSDataInputNormalize
from XSDataCommon           import XSDataFile, XSDataString, XSDataInteger, \
                                XSDataDictionary, XSDataKeyValuePair, XSDataImageExt


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
h5pyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "H5Py-1.3.0", architecture)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath)


class EDPluginControlFullFieldXASv1_0(EDPluginControl):
    """
    Plugin to control  Full Field XRay Absorption Spectroscopy Experiment, ID21 ESRF
    """
    _semaphore = threading.Semaphore()
    energyAttr = {"unit":"keV",
                  "long_name": "Energy of the monochromated beam",
                  "interpretation": "scalar",
                  "axis" : "1"
                  }
    maxIntAttr = {"long_name": "Mean of the last percentil on the frame",
                  "interpretation": "scalar",
                  "monitor": "1"
                  }
    TITLE = "FullField XANES mapping"
    start_time = time.time()

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputFullFieldXAS)
        self.__strControlledNormalize = "EDPluginExecNormalizeImagev1_0"
        self.__strControlledAlign = "EDPluginControlAlignStackv1_0"
        self.index = None
        self.energy = None
        self.reference = 0
        self.HDF5filename = None
        self.internalHDF5Path = None
        self.xsdMeasureOffset = None
        self.xsdNormalizedFilename = None
        self.xsdAlignStack = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlFullFieldXASv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getIndex(), "No index given for data input ")
        self.checkMandatoryParameters(self.getDataInput().getHDF5File(), "No HDF5 file given for data input")
        self.checkMandatoryParameters(self.getDataInput().getInternalHDF5Path(), "No HDF5 internal path given for data input")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlFullFieldXASv1_0.preProcess")
        sdi = self.getDataInput()
        self.index = sdi.getIndex().getValue()
        self.HDF5filename = sdi.getHDF5File()
        self.internalHDF5Path = sdi.getInternalHDF5Path()
        self.xsdMeasureOffset = sdi.getMeasureOffset()
        if sdi.getEnergy() is not None:
            self.energy = sdi.getEnergy().getValue()
        if sdi.getReference() is not None:
            self.reference = sdi.getReference().getValue()
        self.xsdNormalizedFilename = sdi.getSaveNormalized()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlFullFieldXASv1_0.process")
        if self.energy is not None:
            self.makeHDF5EnergyStructure()
        edPluginExecNormalize = self.loadPlugin(self.__strControlledNormalize)
        edPluginExecNormalize.connectSUCCESS(self.doSuccessExecNormalize)
        edPluginExecNormalize.connectFAILURE(self.doFailureExecNormalize)
        xsdInNorm = XSDataInputNormalize()
        sdi = self.getDataInput()
        print sdi.marshal()
        xsdInNorm.setData(sdi.getData())
        xsdInNorm.setFlat(sdi.getFlat())
        xsdInNorm.setDark(sdi.getDark())
        if self.xsdNormalizedFilename is not None:
            xsdInNorm.output = XSDataImageExt(path=self.xsdNormalizedFilename.path)
        print xsdInNorm.marshal()
        edPluginExecNormalize.setDataInput(xsdInNorm)
        edPluginExecNormalize.executeSynchronous()

        if self.xsdAlignStack is not None:
            edPluginAlign = self.loadPlugin(self.__strControlledAlign)
            edPluginAlign.setDataInput(self.xsdAlignStack)
            edPluginAlign.connectSUCCESS(self.doSuccessExecAlign)
            edPluginAlign.connectFAILURE(self.doFailureExecAlign)
            edPluginAlign.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlFullFieldXASv1_0.postProcess")
        # Create some output data
        self.synchronizePlugins()
        self.makeHDF5NeXus()
        xsDataResult = XSDataResultFullFieldXAS()
        xsDataResult.setHDF5File(self.getDataInput().getHDF5File())
        xsDataResult.setInternalHDF5Path(self.getDataInput().getInternalHDF5Path())
        self.setDataOutput(xsDataResult)
        self.emptyListOfLoadedPlugin()
        self.xsdMeasureOffset = None
        self.xsdNormalizedFilename = None
        self.xsdAlignStack = None


    def doSuccessExecNormalize(self, _edPlugin=None):
        self.synchronizeOn()
        self.DEBUG("EDPluginControlFullFieldXASv1_0.doSuccessExecNormalize")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlFullFieldXASv1_0.doSuccessExecNormalize")
        self.xsdAlignStack = XSDataInputAlignStack()
        self.xsdAlignStack.setMeasureOffset(self.xsdMeasureOffset)
        normFile = _edPlugin.dataOutput.getNormalizedFile()
        if normFile is not None:
            data = fabio.open(normFile.getPath().getValue()).data.flatten()
            data.sort()
            self.xsdAlignStack.setImage([normFile])
        else:
            data = _edPlugin.dataOutput.getNormalizedArray()
            self.xsdAlignStack.setArray([ data])
            data = EDUtilsArray.xsDataToArray(data).flatten()
            data.sort()

        self.xsdAlignStack.setIndex([XSDataInteger(self.index)])
        self.xsdAlignStack.setFrameReference(XSDataInteger(self.reference))
        self.xsdAlignStack.setHDF5File(self.getDataInput().getHDF5File())
        self.xsdAlignStack.setInternalHDF5Path(self.getDataInput().getInternalHDF5Path())

        keyValuePair1 = XSDataKeyValuePair(key=XSDataString("axes"), value=XSDataString("energy"))
        keyValuePair2 = XSDataKeyValuePair(key=XSDataString("long_name"), value=XSDataString(self.TITLE))
        keyValuePair3 = XSDataKeyValuePair(key=XSDataString("interpretation"), value=XSDataString("image"))
        keyValuePair4 = XSDataKeyValuePair(key=XSDataString("signal"), value=XSDataString("1"))

        xsAttrDataset = XSDataHDF5Attributes(h5path=XSDataString(self.internalHDF5Path.value.rstrip("/") + "/data"),
                        metadata=XSDataDictionary([keyValuePair1, keyValuePair2, keyValuePair3, keyValuePair4]))
        xsAttrData = XSDataHDF5Attributes(h5path=self.internalHDF5Path, \
                        metadata=XSDataDictionary([XSDataKeyValuePair(key=XSDataString("NX_class"), value=XSDataString("NXdata")),
                                                   ]),
                                           )
        xsAttrEntry = XSDataHDF5Attributes(h5path=XSDataString("/".join(self.internalHDF5Path.value.split("/")[:2])),
                        metadata=XSDataDictionary([XSDataKeyValuePair(key=XSDataString("NX_class"), value=XSDataString("NXentry")),
                                                   XSDataKeyValuePair(key=XSDataString("index"), value=XSDataString("1"))]),
                                           )
#        self.screen(xsAttrEntry.marshal())
#        self.screen(xsAttrData.marshal())
#        self.screen(xsAttrDataset.marshal())

        self.xsdAlignStack.extraAttributes = [xsAttrDataset, xsAttrData, xsAttrEntry]

        ########################################################################
        # Selecte the mean of last centile
        ########################################################################

        fMaxSignal = data[int(0.99 * len(data)):].mean()
        self.makeHDF5MaxIntStructure(fMaxSignal)
        self.synchronizeOff()

    def doFailureExecNormalize(self, _edPlugin=None):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.doFailureExecNormalize")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlFullFieldXASv1_0.doFailureExecNormalize")
        self.setFailure()


    def doSuccessExecAlign(self, _edPlugin=None):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.doSuccessExecAlign")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlFullFieldXASv1_0.doSuccessExecAlign")


    def doFailureExecAlign(self, _edPlugin=None):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.doFailureExecAlign")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlFullFieldXASv1_0.doFailureExecAlign")
        self.setFailure()


    def makeHDF5EnergyStructure(self):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.makeHDF5EnergyStructure")
        h5Grp = EDPluginHDF5.createStructure(self.HDF5filename.getPath().getValue(), self.internalHDF5Path.getValue())
        EDPluginControlFullFieldXASv1_0._semaphore.acquire()
        if "energy" in h5Grp:
            dataset = h5Grp["energy"]
        else:
            dataset = h5Grp.create_dataset("energy", shape=(1 + max(self.index, self.reference),), dtype="float32", maxshape=(None,), chunks=(1,))
            for key in  EDPluginControlFullFieldXASv1_0.energyAttr:
                dataset.attrs.create(key, EDPluginControlFullFieldXASv1_0.energyAttr[key])
        if self.index >= dataset.shape[0]:
            dataset.resize((self.index + 1,))
        dataset[self.index] = self.energy
        EDPluginControlFullFieldXASv1_0._semaphore.release()


    def makeHDF5MaxIntStructure(self, _fMaxIntensity):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.makeHDF5MaxIntStructure")
        h5Grp = EDPluginHDF5.createStructure(self.HDF5filename.getPath().getValue(), self.internalHDF5Path.getValue())
        EDPluginControlFullFieldXASv1_0._semaphore.acquire()
        if "maxInt" in h5Grp:
            dataset = h5Grp["maxInt"]
        else:
            dataset = h5Grp.create_dataset("maxInt", shape=(1 + max(self.index, self.reference),), dtype="float32", maxshape=(None,), chunks=(1,))
            for key in  EDPluginControlFullFieldXASv1_0.maxIntAttr:
                dataset.attrs.create(key, EDPluginControlFullFieldXASv1_0.maxIntAttr[key])
        if self.index >= dataset.shape[0]:
            dataset.resize((self.index + 1,))
        dataset[self.index] = _fMaxIntensity
        EDPluginControlFullFieldXASv1_0._semaphore.release()

    def makeHDF5NeXus(self):
        self.DEBUG("EDPluginControlFullFieldXASv1_0.makeHDF5NeXus")
        h5Grp = EDPluginHDF5.createStructure(self.HDF5filename.getPath().getValue(), self.internalHDF5Path.getValue())
        entry = h5Grp.parent
        if not "title" in  entry:
            entry.create_dataset("title", data=self.TITLE)
        if not "program" in  entry:
            entry.create_dataset("program", data="EDNA EDPluginControlFullFieldXASv1_0")
        if not "start_time" in  entry:
            entry.create_dataset("start_time", data=EDPluginHDF5.getIsoTime(self.start_time))
        ########################################################################
        # Huge hack: for scalar modification: use [()] to refer to the data !!!
        ########################################################################
        if "end_time" in  entry:
            entry["end_time"][()] = EDPluginHDF5.getIsoTime()
        else:
            entry.create_dataset("end_time", data=EDPluginHDF5.getIsoTime(), dtype=h5py.special_dtype(vlen=str))
        if "duration" in  entry:
            entry["duration"][()] = data = time.time() - self.start_time
        else:
            entry.create_dataset("duration", data=time.time() - self.start_time, dtype="float")

