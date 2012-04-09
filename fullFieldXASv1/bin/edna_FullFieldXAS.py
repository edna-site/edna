#!/usr/bin/env python2.6
#-*- coding: utf8 -*-
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "2011, European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120313"

import os, time, sys, tempfile, string, shlex, socket

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
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", EDUtilsPlatform.architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="version.version")
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", EDUtilsPlatform.architecture)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath, _strMethodVersion="version")
h5pyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "H5Py-1.3.0", EDUtilsPlatform.architecture)
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.api_version", _strForceVersion="1.8")
from EDShare                import EDShare
EDFactoryPluginStatic.loadModule('EDPluginHDF5StackImagesv10')
EDFactoryPluginStatic.loadModule('EDPluginControlAlignStackv1_0')
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

    def __init__(self):
        """Constructor of the class"""
        self.pluginName = "EDPluginControlFullFieldXASv1_0"
        self.xsdHDF5 = None #
        self.xsdInternalHdf5 = None #
        self.xsdMeasureOffset = None
        self.xsdReference = None #
        self.xsdDarks = []
        self.dirname = None #
        self.prefix = None #
        self.suffix = ".edf" #
        self.headers = {}
        self.exposureTime = {}
        self.normalizedSuffix = None#""#"_norm.edf"
        self.flatPrefix = None
        self.iLinewidth = 50
        self.listInput = []
        self.bNewerOnly = False
        self.strMode = "OffLine"
        self.dontAlign = None
        self.iErrCount = 0
        self.lstSubscanSize = None
        self.fScaleData = 1.0
        self.fScaleDark = 1.0
        self.fScaleFlat = 1.0


    def load(self, filename):
        """
        Retrieve information from XML file
        """
        xsdi = XSDataInputFullFieldXAS.parseFile(filename)
        self.xsdHDF5 = xsdi.getHDF5File()
        self.xsdInternalHdf5 = xsdi.getInternalHDF5Path()
        self.xsdMeasureOffset = xsdi.getMeasureOffset()
        self.xsdReference = xsdi.getReference()
        self.xsdDarks = xsdi.getDark()
#        if xsdi.dontAlign is not None:
#            self.dontAlign = bool(xsdi.dontAlign.value)


    def save(self, filename):
        """
        Save configuration to file
        """
        xsdi = XSDataInputFullFieldXAS()
        xsdi.setHDF5File(self.xsdHDF5)
        xsdi.setInternalHDF5Path(self.xsdInternalHdf5)
        xsdi.setMeasureOffset(self.xsdMeasureOffset)
        xsdi.setReference(self.xsdReference)
        xsdi.setDark(self.xsdDarks)
        open(filename, "wb").write(xsdi.marshal())


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
        if len(txt) > self.iLinewidth:
            self.iLinewidth = len(txt)
        else:
            txt = txt.ljust(self.iLinewidth)
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
        if self.xsdHDF5 is not None:
            tmpHDF5 = self.xsdHDF5.path.value
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
                self.xsdHDF5 = XSDataFile(path=XSDataString(os.path.abspath(strtmp)))
                bOK = True
        if self.xsdInternalHdf5 is not None:
            tmpHDF5 = self.xsdInternalHdf5.value
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
                self.xsdInternalHdf5 = XSDataString(strtmp)
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
        if self.xsdReference is not None:
            tmpRef = self.xsdReference.value
        else:
            tmpRef = None
        bOK = False
        while not bOK:
            strtmp = self.raw_input("What is the reference frame [%s]: " % tmpRef)
            if strtmp != "":
                try:
                    tmpRef = int(strtmp)
                except:
                    tmpRef = None
            if isinstance(tmpRef, int):
                self.xsdReference = XSDataInteger(tmpRef)
                bOK = True


    def readMeasureOffset(self):
        if self.xsdMeasureOffset is not None:
            print("Currently the offset is measured according to this :")
            print self.xsdMeasureOffset.marshal()
        else:
            print("No settings are available for measuring offset")
        strtmp = self.raw_input("Do you want to change them [N|y] ").lower()
        if strtmp.find("y") == 0:
            if self.xsdMeasureOffset is None :
                 self.xsdMeasureOffset = MeasureOffset()
            strtmp = self.raw_input("Measure Offset versus reference (not versus the next) [0|1]: ")
            if len(strtmp) > 0:
                self.xsdMeasureOffset.setAlwaysVersusRef(XSDataBoolean(int(strtmp)))
            strtmp = self.raw_input("Remove background for measuring offset [0|1]: ")
            if len(strtmp) > 0:
                self.xsdMeasureOffset.setRemoveBackground(XSDataBoolean(int(strtmp)))
            strtmp = self.raw_input("Crop borders before measuring offset (0, 1 or 2 integers): ")
            if len(strtmp) > 0:
                try:
                    ints = [int(i) for i in strtmp.split()]
                except:
                    print("error in reading integers from %s" % strtmp)
                else:
                    if ints == [0]:
                        self.xsdMeasureOffset.smoothBorders = []
                    else:
                        self.xsdMeasureOffset.setCropBorders([XSDataInteger(i) for i in ints])
            strtmp = self.raw_input("Smooth borders before measuring offset (0, 1 or 2 integers): ")
            if len(strtmp) > 0:
                try:
                    ints = [int(i) for i in strtmp.split()]
                except:
                    print("error in reading integers from %s" % strtmp)
                else:
                    if ints == [0]:
                        self.xsdMeasureOffset.smoothBorders = []
                    else:
                        self.xsdMeasureOffset.smoothBorders([XSDataInteger(i) for i in ints])
            strtmp = self.raw_input("Use Sobel filter to enhance feature detections [0|1]: ")
            if len(strtmp) > 0:
                if strtmp != "0":
                    self.xsdMeasureOffset.setSobelFilter(XSDataBoolean(int(strtmp)))
            strtmp = self.raw_input("Use SIFT instead of FFT correlation [0|1]: ")
            if len(strtmp) > 0:
                if strtmp[0] not in ["0", "n", "N"]:
                    try:
                        import feature
                    except:
                        print("Unable to import feature: fall back on FFT")
                        self.xsdMeasureOffset.setUseSift(XSDataBoolean(False))
                    else:
                        self.xsdMeasureOffset.setUseSift(XSDataBoolean(True))
                else:
                    self.xsdMeasureOffset.setUseSift(XSDataBoolean(False))


    def readDark(self):
        if len(self.xsdDarks) > 0:
            print("List of dark images with exposure times:")
            for oneXSDark in self.xsdDarks:
                print("%s\t\t%s" % (oneXSDark.path.value, oneXSDark.getExposureTime().value))
        else:
            print("No dark images are defined, you should define some !")
        strtmp = self.raw_input("Do you want to change anything [N|y]: ").lower()
        if  strtmp.find("y") == 0:
            self.xsdDarks = []
            strtmp = self.raw_input("Enter the list of all dark images, spaces separated: ")
            for oneFile in shlex.split(strtmp):
                if os.path.isfile(oneFile):
                    xsdata = XSDataImageExt()
                    xsdata.setPath(XSDataString(os.path.abspath(oneFile)))
                    expTime = self.getExposureTime(oneFile)
                    while expTime is None:
                        strtmp = self.raw_input("What is the exposure time of %s: " % os.path.basename(oneFile))
                        try:
                            expTime = float(strtmp)
                        except:
                            print("Unable to understand this %s !!" % strtmp)
                    xsdata.setExposureTime(XSDataTime(expTime))
                    self.xsdDarks.append(xsdata)

    def readSubscanSize(self):
        """
        
        """
        strtmp = self.raw_input("Size of the sub-scans (space separated):")
        try:
            self.lstSubscanSize = [int(i) for i in strtmp.split()]
        except:
            self.lstSubscanSize = None
        else:
            print("Setting scan size to %s" % self.lstSubscanSize)

    def readScale(self):
        strtmp = self.raw_input("Scale factor for data frames (division):")
        try:
            self.fScaleData = float(strtmp)
        except:
            self.fScaleData = 1
        strtmp = self.raw_input("Scale factor for ref frames (division):")
        try:
            self.fScaleFlat = float(strtmp)
        except:
            self.fScaleFlat = 1
        strtmp = self.raw_input("Scale factor for dark frames (division):")
        try:
            self.fScaleDark = float(strtmp)
        except:
            self.fScaleDark = 1


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
            except:
                value = None
        elif "count_time" in header:
            try:
                value = float(header["count_time"])
            except:
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
            except:
                value = None
        else:
            EDVerbose.WARNING("No energyin file %s" % filename)
        return value



    def makeXML(self, filename):
        """Here we create the XML string to be passed to the EDNA plugin from the input filename
        This can / should be modified by the final user
        
        @param filename: full path of the input file
        @type filename: python string representing the path
        @rtype: XML string
        @return: python string  
        """
    #Ti_slow_data_0000_0000_0000.edf
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

        xsd = XSDataInputFullFieldXAS()
        if self.dontAlign:
            xsd.dontAlign = XSDataBoolean(self.dontAlign)
        extendedPrefix = ""
        number = ""
        started = False
        if self.lstSubscanSize:
            subScanDigit = []
            for i in basename[len(self.prefix):]:
                extendedPrefix += i
                if started and i == "_":
                    if len(number) > 0:
                        subScanDigit.append(int(number))
                        number = ""
                    continue
                if started and not i.isdigit():
                    if number:
                        subScanDigit.append(int(number))
                    number = ""
                    break
                if not started and i.isdigit():
                    started = True
                if started:
                    number += i
            if not subScanDigit:
                print("ERROR: no index guessed !!!")
                return ""
            elif len(subScanDigit) == 1:
                index = subScanDigit[0]
            else:# len(subScanDigit) > 1:
                index = 0
                for i in range(subScanDigit[0]):
                    index += self.lstSubscanSize[i]
                index += subScanDigit[1]
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

        xsd.setIndex(XSDataInteger(index))

        xsd.HDF5File = self.xsdHDF5
        xsd.internalHDF5Path = self.xsdInternalHdf5
        xsd.reference = self.xsdReference
        xsd.measureOffset = self.xsdMeasureOffset
        xsd.data = [XSDataImageExt(path=XSDataString(filename),
                                   exposureTime=XSDataTime(self.getExposureTime(filename)))]
        xsd.dataScaleFactor = XSDataDouble(self.fScaleData)
        xsd.darkScaleFactor = XSDataDouble(self.fScaleDark)
        xsd.flatScaleFactor = XSDataDouble(self.fScaleFlat)
        if self.normalizedSuffix:
            pr = os.path.splitext(os.path.abspath(filename))[0]
            xsd.saveNormalized = XSDataFile(path=XSDataString(pr + self.normalizedSuffix))
        energy = self.getEnergy(filename)
        if energy is not None:
            xsd.energy = XSDataDouble(energy)
        xsd.dark = self.xsdDarks

        flatprefix = self.flatPrefix + extendedPrefix
        listFlats = [  ]
        for oneFile in os.listdir(dirname):
            if oneFile.startswith(flatprefix) and oneFile.endswith(self.suffix):
                oneCompleteFile = os.path.abspath(os.path.join(dirname, oneFile))
                xsdFileFlat1 = XSDataImageExt(path=XSDataString(oneCompleteFile),
                                              exposureTime=XSDataTime(self.getExposureTime(oneCompleteFile)))
                listFlats.append(xsdFileFlat1)
        xsd.setFlat(listFlats)

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
        self.iErrCount += 1





if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    iNbCPU = None
    dontAlign = None
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
        elif i.lower().find("-h") in [0, 1]:
            print "This is the DiffractionCTv1 application of EDNA %s, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA\n\
            --nCPU=xxx to specify the number of CPUs to use. Usually EDNA autodetects the number of processors.\n\
            --dontAlign to allow the constitution an unaligned stack " % EDNAPluginName
            sys.exit()
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))


    ffx = FullFieldXas()
    if os.path.isfile(".XSDataInputFullFieldXAS.xml"):
        ffx.load(".XSDataInputFullFieldXAS.xml")

    ffx.dontAlign = dontAlign
    if  dontAlign:
        print("*"*80)
        print("*" + "Skipping image alignement part".center(78) + "*")
        print("*"*80)
    ffx.setup(_listInput=paths, _mode=mode)

    ffx.save(".XSDataInputFullFieldXAS.xml")

    edna = EDParallelExecute(ffx.pluginName, ffx.makeXML, _functXMLerr=ffx.error, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(ffx.listInput, ffx.strMode , ffx.bNewerOnly)
    EDVerbose.WARNING("Back to main !")
    EDJob.synchronizeAll()
    EDPluginControlAlignStackv1_0.showData()
    if (ffx.iErrCount == 0) and (not EDVerbose.isVerboseDebug()):
        EDVerbose.WARNING("All processing finished successfully: Remove EDShare's big HDF5 file")
        EDShare.close(remove=True)
    else:
        EDShare.close()
