#!/usr/bin/env python
#-*- coding: utf8 -*-
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "2011, European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120313"

import os, time, sys, tempfile, string, shlex, socket, json
# Append the EDNA kernel source directory to the python path
if "EDNA_HOME" not in  os.environ:
    pyStrProgramPath = os.path.realpath(os.path.abspath(sys.argv[0]))
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 3:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        pyStrEdnaHomePath = os.heet
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath

try:
    from rfoo.utils import rconsole
    rconsole.spawn_server()
except ImportError:
    print("No socket opened for debuging -> please install rfoo")

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDVerbose              import EDVerbose
if "EDNA_SITE" not in  os.environ:
    os.environ["EDNA_SITE"] = "ESRF"
    EDVerbose.WARNING("EDNA_SITE not defined: Resetting to 'ESRF'")

from EDParallelExecute      import EDParallelExecute
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDJob                  import EDJob
from EDShare                import EDShare
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", EDUtilsPlatform.architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="version.version")
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", EDUtilsPlatform.architecture)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath, _strMethodVersion="version")
h5pyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "H5Py-1.3.0", EDUtilsPlatform.architecture)
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.api_version", _strForceVersion="1.8")
from EDShare                import EDShare
EDFactoryPluginStatic.loadModule('EDPluginHDF5StackImagesv10')
EDFactoryPluginStatic.loadModule('EDPluginControlAlignStackv1_0')
EDFactoryPluginStatic.loadModule("EDPluginAccumulatorv1_0")
from EDPluginAccumulatorv1_0            import EDPluginAccumulatorv1_0
from EDPluginControlAlignStackv1_0      import EDPluginControlAlignStackv1_0
from EDPluginControlFullFieldXASv1_0    import EDPluginControlFullFieldXASv1_0
from EDPluginHDF5StackImagesv10         import EDPluginHDF5StackImagesv10
from XSDataFullFieldXAS                 import MeasureOffset, XSDataInputAlignStack, XSDataInputFullFieldXAS
from XSDataCommon                       import XSDataTime, XSDataFile, XSDataImageExt, XSDataString, XSDataInteger, XSDataBoolean, XSDataDouble


if socket.gethostname() == 'lintaillefer':
    EDShare.initialize("/mnt/data/EDShare")
if socket.gethostname() == 'tabor':
    EDShare.initialize("/mnt/EDShare")
else:
    try:
        dirnames = [i for i in os.listdir("/buffer") if i.startswith(socket.gethostname())]
    except OSError:
        dirnames = []
    if dirnames != []:
         EDShare.initialize(os.path.join("/buffer", dirnames[0]))



EDNAPluginName = "EDPluginControlFullFieldXASv1_0"
class FullFieldXas(object):
    """
    class for the definition and the storage of the metadata as well as the XML generation. 
    """
    REFERENCE_FRAME_NAME = "reference_frame"

    def __init__(self):
        """Constructor of the class"""
        self.pluginName = "EDPluginControlFullFieldXASv1_0"
        self.HDF5 = None #
        self.internalHdf5 = None #
        self.measureOffset = None
        self.reference = None #
        self.darks = []
        self.prefix = None #
        self.suffix = ".edf" #
        self.headers = {}
        self.normalizedSuffix = None#""#"_norm.edf"
        self.flatPrefix = None
        self._iLinewidth = 50
        self.listInput = []
        self.bNewerOnly = False
        self.strMode = "OffLine"
        self.dontAlign = None
        self._lstErrorFile = []
        self.lstSubscanSize = None
        self.fScaleData = None
        self.fScaleDark = None
        self.fScaleFlat = None
        self._xsdDataMeasureOffset = None
        self._xsDataDark = None

    def load(self, filename):
        """
        Retrieve information from XML file
        """
        xsdi = XSDataInputFullFieldXAS.parseFile(filename)
        self.HDF5 = xsdi.HDF5File.path.value
        self.internalHdf5 = xsdi.internalHDF5Path.value
        self.measureOffset = {}
        mo = xsdi.measureOffset
        if mo:
            if mo.alwaysVersusRef:
                self.measureOffset["alwaysVersusRef"] = mo.alwaysVersusRef.value
            if mo.cropBorders:
                self.measureOffset["cropBorders"] = [i.value for i in mo.cropBorders]
            if mo.smoothBorders :
                self.measureOffset["smoothBorders"] = [i.value for i in mo.smoothBorders]
            if mo.sobelFilter :
                self.measureOffset["sobelFilter"] = mo.sobelFilter.value
            if mo.useSift :
                self.measureOffset["useSift"] = mo.useSift.value
            if mo.removeBackground :
                self.measureOffset["removeBackground"] = mo.removeBackground.value
        self.reference = xsdi.reference.value
        self.darks = [{"path":i.path.value, "exposureTime":i.exposureTime.value} for i in xsdi.dark]
#        if xsdi.dontAlign is not None:
#            self.dontAlign = bool(xsdi.dontAlign.value)


    def save(self, filename):
        """
        Save configuration to file
        """
        if isinstance(self.reference, int):
            reference = self.reference
        else:
            reference = -1
        xsdi = XSDataInputFullFieldXAS(HDF5File=XSDataFile(XSDataString(self.HDF5)),
                                       internalHDF5Path=XSDataString(self.internalHdf5),
                                       measureOffset=self.getXSDMeasureOffset(),
                                       reference=XSDataInteger(reference),
                                       dark=self.getXsdDark())
        with open(filename, "wb") as xmlFile:
            xmlFile.write(xsdi.marshal())

    def dump(self, filename):
        """
        dump state of the instance into a file using JSON
        """
        dumpdic = {}
        for k, v in self.__dict__.items():
            if k == "headers":
                dumpdic[k] = {}
            elif k.startswith("_") or ("__call__" in dir(v)):
                continue
            else:
                dumpdic[k] = v
        with open(filename, "w") as dumpfile:
            json.dump(dumpdic, dumpfile, indent=2)

    @classmethod
    def replay_from(cls, filename):
        """
        Create an instance from a previous JSON dump 
        """
        dumpdic = {}
        with open(filename, "r") as dumpfile:
            dumpdic = json.load(dumpfile)
        self = cls()
        for k, v in dumpdic.items():
            if k == "headers":
                self.__dict__[k] = {}
            else:
                self.__dict__[k] = v
        return self



    def setup(self, _listInput=[], _mode="offline"):
        """Configure the various options"""
        self.readInputDir(_listInput)
        self.readMode(_mode)
        self.readPrefix()
        self.readFlatPrefix()
        self.readSuffix()
        self.readNormSuffix()
        self.readHDF5()
        self.readReference()
        self.readDark()
        self.readSubscanSize()
        self.readScale()
        self.readMeasureOffset()

    def raw_input(self, txt):
        """
        Same behavour as raw_input but adapted to this program 
        
        @param txt: text to be displayed
        @return: string
        """
        if len(txt) > self._iLinewidth:
            self._iLinewidth = len(txt)
        else:
            txt = txt.ljust(self._iLinewidth)
        return raw_input(txt).strip()

    def readInputDir(self, _listInput):
        bOK = False
        if _listInput == []:
            _listInput = [os.getcwd()]
        while not bOK:
            txt = "What are the input directories (mandatory, space separated) %s: " % _listInput
            strtmp = self.raw_input(txt)
            if len(strtmp) > 0:
                bAllExists = True
                lstTemp = shlex.split(strtmp)
                for oneDir in shlex.split(strtmp):
                    if not os.path.isdir(oneDir):
                        EDVerbose.screen("No such file or directory: %s" % oneDir)
                        bAllExists = False
                if bAllExists is True:
                    self.listInput = lstTemp
                    bOK = True
            else:
                self.listInput = _listInput
                bOK = True


    def readMode(self, _mode):
        bOK = False
        while not bOK:
            txt = "What is operation mode [offline|online|all] (%s): " % _mode
            strtmp = self.raw_input(txt).lower()
            if len(strtmp) == 0:
                strtmp = _mode.lower()
            if strtmp == "offline":
                self.bNewerOnly = False
                self.strMode = "OffLine"
                bOK = True
            elif strtmp == "online":
                self.bNewerOnly = True
                self.strMode = "dirwatch"
                bOK = True
            elif strtmp == "all":
                self.bNewerOnly = False
                self.strMode = "dirwatch"
                bOK = True
            else:
                    bOK = False


    def readHDF5(self):
        if self.HDF5 is not None:
            tmpHDF5 = self.HDF5
        else:
            common = "".join([i for  i, j in zip(self.prefix, self.flatPrefix) if i == j])
            if len(common) < 3:
                common = "entry"
            tmpHDF5 = common.strip("_") + ".h5"
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is the destination HDF5 file [%s]: " % tmpHDF5)
            if strtmp == "":
                strtmp = tmpHDF5
            if (strtmp is not None) and os.path.isdir(os.path.dirname(strtmp)):
                self.HDF5 = os.path.abspath(strtmp)
                bOK = True
        if self.internalHdf5 is not None:
            tmpHDF5 = self.internalHdf5
        elif self.dontAlign:
            tmpHDF5 = "unAligned"
        else:
            tmpHDF5 = "Aligned"
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is the internal HDF5 path  [%s]: " % tmpHDF5)
            if strtmp == "":
                strtmp = tmpHDF5
            if isinstance(strtmp, (str, unicode)):
                self.internalHdf5 = strtmp
                bOK = True

    def readPrefix(self):
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is the input data filename prefix [%s]: " % self.prefix)
            if strtmp != "":
                self.prefix = strtmp
                bOK = True

    def readSuffix(self):
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is common input data suffix [%s]: " % self.suffix)
            if strtmp == "":
                bOK = (self.suffix is not None)
            else:
                self.suffix = strtmp
                bOK = True

    def readFlatPrefix(self):
        bOK = False
        self.flatPrefix = self.prefix.replace("data", "ref")
        while not bOK:
            strtmp = self.raw_input("What is the flat image filename prefix [%s]: " % self.flatPrefix)
            if strtmp == "":
                bOK = (self.suffix is not None)
            else:
                self.flatPrefix = strtmp
                bOK = True

    def readNormSuffix(self):
        strtmp = self.raw_input("What is the suffix for normalized images [%s]: " % self.normalizedSuffix)
        if strtmp != "":
            self.normalizedSuffix = strtmp


    def readReference(self):
        if self.reference is not None:
            tmpRef = self.reference
        else:
            tmpRef = None
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is the reference frame [%s]: " % tmpRef)
            if strtmp != "":
                try:
                    tmpRef = int(strtmp)
                except ValueError:
                    tmpRef = strtmp
            if isinstance(tmpRef, int) or os.path.isfile(tmpRef.split(":")[0]):
                self.reference = tmpRef
                bOK = True


    def readMeasureOffset(self):
        if self.measureOffset:
            print("Currently the offset is measured according to this :")
            print self.measureOffset
        else:
            print("No settings are available for measuring offset")
        strtmp = self.raw_input("Do you want to change them [N|y] ").lower()
        if strtmp.find("y") == 0:
            if self.measureOffset is None :
                 self.measureOffset = {}
            strtmp = self.raw_input("Measure Offset versus reference (not versus the next) [0|1]: ")
            if len(strtmp) > 0:
                self.measureOffset["alwaysVersusRef"] = int(strtmp)
            strtmp = self.raw_input("Remove background for measuring offset [0|1]: ")
            if len(strtmp) > 0:
                self.measureOffset["removeBackground"] = int(strtmp)
            strtmp = self.raw_input("Crop borders before measuring offset (0, 1 or 2 integers): ")
            if len(strtmp) > 0:
                try:
                    ints = [int(i) for i in strtmp.split()]
                except Exception:
                    print("error in reading integers from %s" % strtmp)
                else:
                    if ints == [0]:
                        self.measureOffset["cropBorders"] = []
                    else:
                        self.measureOffset["cropBorders"] = ints
            strtmp = self.raw_input("Smooth borders before measuring offset (0, 1 or 2 integers): ")
            if len(strtmp) > 0:
                try:
                    ints = [int(i) for i in strtmp.split()]
                except Exception:
                    print("error in reading integers from %s" % strtmp)
                else:
                    if ints == [0]:
                        self.measureOffset["smoothBorders"] = []
                    else:
                        self.measureOffset["smoothBorders"] = ints
            strtmp = self.raw_input("Use Sobel filter to enhance feature detections [0|1]: ")
            if len(strtmp) > 0:
                if strtmp != "0":
                    self.measureOffset.sobelFilter = int(strtmp)
            strtmp = self.raw_input("Use SIFT instead of FFT correlation [0|1]: ")
            if len(strtmp) > 0:
                if strtmp[0] not in ["0", "n", "N"]:
                    try:
                        import feature
                    except Exception:
                        print("Unable to import feature: fall back on FFT")
                        self.measureOffset["useSift"] = False
                    else:
                        self.measureOffset["useSift"] = True
                else:
                    self.measureOffset["useSift"] = False


    def readDark(self):
        if len(self.darks) > 0:
            print("List of dark images with exposure times:")
            for oneXSDark in self.darks:
                print("%s\t\t%s" % (oneXSDark["path"], oneXSDark["exposureTime"]))
        else:
            print("No dark images are defined, you should define some !")
        strtmp = self.raw_input("Do you want to change anything [N|y]: ").lower()
        if  strtmp.find("y") == 0:
            self.darks = []
            strtmp = self.raw_input("Enter the list of all dark images, spaces separated: ")
            for oneFile in shlex.split(strtmp):
                if os.path.isfile(oneFile):
                    expTime = self.getExposureTime(oneFile)
                    while expTime is None:
                        strtmp = self.raw_input("What is the exposure time of %s: " % os.path.basename(oneFile))
                        try:
                            expTime = float(strtmp)
                        except Exception:
                            print("Unable to understand this %s !!" % strtmp)
                    self.darks.append({"path":os.path.abspath(oneFile), "exposureTime":expTime})

    def readSubscanSize(self):
        """
        
        """
        strtmp = self.raw_input("Size of the sub-scans (space separated):")
        try:
            self.lstSubscanSize = [int(i) for i in strtmp.split()]
        except Exception:
            self.lstSubscanSize = None
        print("Setting scan size to %s" % self.lstSubscanSize)

    #
    def readScale(self):
        strtmp = self.raw_input("OVERRIDE the scale factor found in files? [N|y]: ").lower()
        if  strtmp.find("y") == 0:
            strtmp = self.raw_input("Scale factor for data frames (division):")
            try:
                self.fScaleData = float(strtmp)
            except Exception:
                self.fScaleData = None
            strtmp = self.raw_input("Scale factor for ref frames (division):")
            try:
                self.fScaleFlat = float(strtmp)
            except Exception:
                self.fScaleFlat = None
            strtmp = self.raw_input("Scale factor for dark frames (division):")
            try:
                self.fScaleDark = float(strtmp)
            except Exception:
                self.fScaleDark = None


    def getHeaders(self, filename):
        if filename not in self.headers:
            header = fabio.open(filename).header
            self.headers[filename] = header
        else:
            header = self.headers[filename]
        return header


    def getExposureTime(self, filename):
        header = self.getHeaders(filename)
        value = None
        if "exposure_time" in header:
            try:
                value = float(header["exposure_time"])
            except Exception:
                value = None
        elif "count_time" in header:
            try:
                value = float(header["count_time"])
            except Exception:
                value = None
        else:
            EDVerbose.WARNING("No exposure time in file %s" % filename)
        return value


    def getEnergy(self, filename):
        header = self.getHeaders(filename)
        value = None
        if "energy" in header:
            try:
                value = float(header["energy"])
            except Exception:
                value = None
        else:
            EDVerbose.WARNING("No energy in file %s" % filename)
        return value


    def getNbFrames(self, filename):
        header = self.getHeaders(filename)
        value = None
        if "nb_frames" in header:
            try:
                value = float(header["nb_frames"])
            except Exception:
                value = 1
        else:
            EDVerbose.WARNING("No 'nb_frames' in file %s" % filename)
        return value


    def makeXML(self, filename):
        """Here we create the XML string to be passed to the EDNA plugin from the input filename
        This can / should be modified by the final user
        
        @param filename: full path of the input file
        @type filename: python string representing the path
        @rtype: XML string
        @return: python string  
        """
        self.header = None
        dirname, basename = os.path.split(filename)
        if not basename.startswith(self.prefix):
            return
        if self.normalizedSuffix and basename.endswith(self.normalizedSuffix):
            return
        if basename.startswith(self.flatPrefix):
            return
        if not basename.endswith(self.suffix):
            return

        if self.fScaleData:
            fScaleData = self.fScaleData
        else:
             fScaleData = self.getNbFrames(filename)
        if not fScaleData:
            fScaleData = 1.0

        if self.fScaleDark:
            fScaleDark = self.fScaleDark
        else:
             fScaleDark = self.getNbFrames(self.darks[0]["path"])
        if not fScaleDark:
            fScaleDark = 1.0

        if isinstance(self.reference, int):
            reference = self.reference
        else:
            reference = -1

        xsd = XSDataInputFullFieldXAS(HDF5File=XSDataFile(path=XSDataString(self.HDF5)),
                                      internalHDF5Path=XSDataString(self.internalHdf5),
                                      measureOffset=self.getXSDMeasureOffset(),
                                      dark=self.getXsdDark(),
                                      reference=XSDataInteger(reference),
                                      data=[XSDataImageExt(path=XSDataString(filename),
                                                             exposureTime=XSDataTime(self.getExposureTime(filename)))],
                                      dataScaleFactor=XSDataDouble(fScaleData),
                                      darkScaleFactor=XSDataDouble(fScaleDark),
                                      )
        if self.dontAlign:
            xsd.dontAlign = XSDataBoolean(self.dontAlign)
        extendedPrefix = ""
        number = ""
        started = False
        if self.lstSubscanSize:
            subScanDigit = []
            for i in basename[len(self.prefix):]:
                if started and i == "_":
                    if len(number) > 0:
                        subScanDigit.append(number)
                        number = ""
                    continue
                if started and not i.isdigit():
                    if number:
                        subScanDigit.append(number)
                    number = ""
                    break
                if not started:
                    if i.isdigit():
                        started = True
                    else:
                        extendedPrefix += i
                if started:
                    number += i

            if not subScanDigit:
                print("ERROR: no index guessed !!!")
                return ""
            elif len(subScanDigit) == 1:
                index = int(subScanDigit[0])
            else:# len(subScanDigit) > 1:
                index = 0
                for i in range(int(subScanDigit[0])):
                    index += self.lstSubscanSize[i]
                index += int(subScanDigit[1])
                extendedPrefix += "_".join(subScanDigit[:2])
        else:
            for i in basename[len(self.prefix):]:
                extendedPrefix += i
                if started and not i.isdigit():
                    break
                if not started and i.isdigit():
                    started = True
                if started:
                    number += i
            index = int(number)
        xsd.index = XSDataInteger(index)

        if self.normalizedSuffix:
            pr = os.path.splitext(os.path.abspath(filename))[0]
            xsd.saveNormalized = XSDataFile(path=XSDataString(pr + self.normalizedSuffix))
        energy = self.getEnergy(filename)
        if energy is not None:
            xsd.energy = XSDataDouble(energy)


        flatprefix = self.flatPrefix + extendedPrefix
        listFlats = []
        for oneFile in os.listdir(dirname):
            if oneFile.startswith(flatprefix) and oneFile.endswith(self.suffix):
                oneCompleteFile = os.path.abspath(os.path.join(dirname, oneFile))
                xsdFileFlat1 = XSDataImageExt(path=XSDataString(oneCompleteFile),
                                              exposureTime=XSDataTime(self.getExposureTime(oneCompleteFile)))
                listFlats.append(xsdFileFlat1)
        xsd.flat = listFlats
        if len(listFlats) != 2:
            EDVerbose.WARNING("Not exactly 2 flats were found:" + " ".join([a.path.value for a in listFlats ]))
            EDVerbose.WARNING("Those are the flat prefix ans suffix: %s\t%s" % (flatprefix, self.suffix))

        if self.fScaleFlat:
            fScaleFlat = self.fScaleFlat
        else:
             fScaleFlat = self.getNbFrames(oneCompleteFile)
        if not fScaleFlat:
            fScaleFlat = 1.0
        xsd.flatScaleFactor = XSDataDouble(fScaleFlat)
        return xsd.marshal()


    def error(self, strXMLin):
        """
        This is an example of XMLerr function ... it prints only the name of the file created
        @param srXMLin: The XML string used to launch the job
        @type strXMLin: python string with the input XML
        @rtype: None
        @return: None     
        """
        if isinstance(strXMLin, (str, unicode)):
            xsd = XSDataInputFullFieldXAS.parseString(strXMLin)
        else:
            xsd = strXMLin
        filenames = [ i.path.value for i in xsd.getData()]
        EDVerbose.ERROR("Error in the processing of: \n %s" % "\n".join(filenames))
        self._lstErrorFile.append(filenames)


    def getXSDMeasureOffset(self):
        """
        return MeasureOffset XSData object
        """
        if self._xsdDataMeasureOffset is None:
            mo = MeasureOffset()
            for key in ["alwaysVersusRef", "removeBackground", "sobelFilter" , "useSift"]:
                if key in self.measureOffset:
                    setattr(mo, key, XSDataBoolean(self.measureOffset[key]))
            for key in ["cropBorders", "smoothBorders"]:
                if key in self.measureOffset:
                    setattr(mo, key, [XSDataInteger(i) for i in self.measureOffset[key]])
            self._xsdDataMeasureOffset = mo
        return self._xsdDataMeasureOffset

    def getXsdDark(self):
        """
        return XSDataDark object
        """

        if self._xsDataDark is None:
            self._xsDataDark = [XSDataImageExt(path=XSDataString(i["path"]),
                               exposureTime=XSDataTime(i["exposureTime"]))
                              for i in self.darks]
        return self._xsDataDark

    def getNrErrors(self):
        if self._lstErrorFile != []:
            EDVerbose.WARNING("Error processing those files:" + os.linesep.join(["\t".join(i) for i in self._lstErrorFile]))
        return len(self._lstErrorFile)

    def uploadReferenceFrame(self, entry):
        paths = entry.split(":")
        if len(paths) == 1 and os.path.isfile(paths[0]):
            obj = fabio.open(paths[0]).data
            EDVerbose.WARNING("Got reference frame %s via fabio" % entry)
            EDPluginControlAlignStackv1_0.addFrame(-1, obj)
            EDPluginAccumulatorv1_0.addItem(XSDataString("raw -001"))
            self.updateAttrRefImage(obj)
        elif len(paths) == 2 and os.path.isfile(paths[0]):
            hdf = h5py.File(paths[0])
            if paths[1] in hdf:
                obj = hdf[paths[1]]
                if obj.__class__.__name__ == "Group":
                    if self.REFERENCE_FRAME_NAME in obj:
                        data = obj[self.REFERENCE_FRAME_NAME][:]
                        EDPluginControlAlignStackv1_0.addFrame(-1, data)
                        EDPluginAccumulatorv1_0.addItem("raw -001")
                        self.updateAttrRefImage(data)
                    else:
                        EDVerbose.ERROR("HDF5: No '%s' in group %s from %s" % (self.REFERENCE_FRAME_NAME, paths[1], paths[0]))
                elif obj.__class__.__name__ == "Dataset":
                    data = obj[:]
                    EDPluginControlAlignStackv1_0.addFrame(-1, data)
                    EDPluginAccumulatorv1_0.addItem(XSDataString("raw -001"))
                    self.updateAttrRefImage(data)
            else:
                EDVerbose.ERROR("HDF5: No such internal path %s in %s" % (paths[1], paths[0]))
        else:
            EDVerbose.ERROR("No such entry %s" % entry)

    def updateAttrRefImage(self, data=None):
        h5grp = EDPluginHDF5StackImagesv10.createStructure(ffx.HDF5, str(self.internalHdf5))
        with EDPluginHDF5StackImagesv10.getFileLock(ffx.HDF5):
            if (self.REFERENCE_FRAME_NAME not in h5grp) and (data is not None):
                h5grp[self.REFERENCE_FRAME_NAME] = data
            if self.REFERENCE_FRAME_NAME  in h5grp:
                referenceDS = h5grp[self.REFERENCE_FRAME_NAME ]
                if isinstance(self.reference, int):
                    referenceDS.attrs["origin"] = self.reference
                else:
                    referenceDS.attrs["origin"] = str(self.reference)
            else:
                EDVerbose.WARNING("Reference frame is not in %s:%s attr not updated" % (self.HDF5, self.internalHdf5))



if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    iNbCPU = None
    dontAlign = None
    replay = None
    keepShare = False
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            mode = "all"
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            iNbCPU = int(i.split("=", 1)[1])
        elif i.lower().find("-dontalign") in [0, 1]:
            dontAlign = True
        elif i.lower().find("-replay=") in [0, 1]:
            path = i.split("=", 1)[1]
            if os.path.isfile(path):
                replay = path
        elif i.lower().find("-keep") in [0, 1]:
            keepShare = True
        elif i.lower().find("-h") in [0, 1]:
            print "This is the DiffractionCTv1 application of EDNA %s, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA\n\
            --nCPU=xxx to specify the number of CPUs to use. Usually EDNA autodetects the number of processors.\n\
            --dontAlign to allow the constitution an unaligned stack \n\
            --replay=filename to replay a former processing\n\
            --keep retain temporary HDF5 shared data file" % EDNAPluginName

            sys.exit()
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))

    if replay:
        ffx = FullFieldXas.replay_from(replay)
    else:
        ffx = FullFieldXas()
        if os.path.isfile(".XSDataInputFullFieldXAS.xml"):
            ffx.load(".XSDataInputFullFieldXAS.xml")

        ffx.dontAlign = dontAlign
        if  dontAlign:
            print("*"*80)
            print("*" + "Skipping image alignement part".center(78) + "*")
            print("*"*80)
        ffx.setup(_listInput=paths, _mode=mode)
    if not isinstance(ffx.reference, int):
        ffx.uploadReferenceFrame(ffx.reference)
    ffx.save(".XSDataInputFullFieldXAS.xml")
    ffx.dump("analysis-%s.json" % time.strftime("%Y%m%d-%Hh%Mm%Ss"))
    edna = EDParallelExecute(ffx.pluginName, ffx.makeXML, _functXMLerr=ffx.error, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(ffx.listInput, ffx.strMode , ffx.bNewerOnly)
    EDVerbose.WARNING("Back to main !")
    EDJob.synchronizeAll()
    ffx.updateAttrRefImage()
    EDPluginControlAlignStackv1_0.showData()
    if keepShare:
        EDShare.close()
    elif (ffx.getNrErrors() == 0) and (not EDVerbose.isVerboseDebug()):
        EDVerbose.WARNING("All processing finished successfully: Remove EDShare's big HDF5 file")
        EDShare.close(remove=True)
    else:
        EDShare.close()
