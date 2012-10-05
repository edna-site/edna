# coding: utf8
#
#    Project: execPlugins: Thumbnail generator
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal authors:       Olof Svensson (svensson@esrf.fr)
#                             Jérôme Kieffer (Jerome.Kieffer@esrf.eu)
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

__authors__ = ["Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, threading, tempfile #sys
from EDVerbose              import EDVerbose
from EDPluginExec           import EDPluginExec
from EDUtilsLibraryInstaller import EDUtilsLibraryInstaller
from EDUtilsArray           import EDUtilsArray
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataFile
from XSDataCommon           import XSDataString
from XSDataPyarchThumbnail    import XSDataInputPyarchThumbnail
from XSDataPyarchThumbnail    import XSDataResultPyarchThumbnail


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsLibraryInstaller.getArchitecture()
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "Fabio-r5080", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)


try:
    import numpy, scipy.ndimage.morphology, Image, fabio
except Exception:
    EDVerbose.ERROR("Error in loading numpy,PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginPyarchThumbnailv10 \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")

import ImageFile, ImageOps
ImageFile.MAXBLOCK = 1000000 # default is 64k
#import fabio.openimage
from fabio.openimage import openimage



colormap = """
0 0 0
0 0 1
1 0 1
1 0 0
1 1 0
1 1 1
"""



class EDPluginPyarchThumbnailv10(EDPluginExec):
    """
    This is the excution plugin called Thumbnail that creates a JPEG (or PNG) thumbnail image from a CCD image 
    It makes use of both Fabio, PIL and Numpy libraries. So please check that those three libraries, all located 
    at  $EDNA_HOME/libraries have been compiled for your computer.
    """
    __palette = None
    __semaphore = threading.Semaphore()

    def __init__(self):
        """
        Constructor of the plugin 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputPyarchThumbnail)
        self.inputFilename = None
        self.strOutputPath = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginPyarchThumbnailv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#        self.checkMandatoryParameters(self.getDataInput().getInputImagePath().getPath().getValue(), "No Input image")


    def preProcess(self, _edObject=None):
        """
        Preprocess of the plugin: 
        check parameters and extract from EDNA format into something more simple & pythonic
        """
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginPyarchThumbnailv10.preProcess")
        sdi = self.getDataInput()
        if sdi.getInputImagePath() is not None:
            self.inputFilename = sdi.getInputImagePath().getPath().getValue()
            if not os.path.isfile(self.inputFilename):
                EDVerbose.ERROR("The input file provided is not a valid file: " + self.inputFilename)
                raise "Not a valid file " + self.inputFilename

            # Output path
            strImageNameWithoutExt = os.path.basename(os.path.splitext(self.inputFilename)[0])
            strImageDirname = os.path.dirname(self.inputFilename)
            strOutputDirname = self.createPyarchFilePath(strImageDirname)
            # Check that output pyarch path exists and is writeable:
            bIsOk = False
            if strOutputDirname:
                if not os.path.exists(strOutputDirname):
                    # Try to create the directory
                    try:
                        os.makedirs(strOutputDirname)
                        bIsOk = True
                    except BaseException, e:
                        EDVerbose.WARNING("Couldn't create the directory %s" % strOutputDirname)
                elif os.access(strOutputDirname, os.W_OK):
                    bIsOk = True
            if not bIsOk:
                EDVerbose.warning("Cannot write to pyarch directory: %s" % strOutputDirname)
                strOutputDirname = tempfile.mkdtemp("", "EDPluginPyarchThumbnailv10_", "/tmp")
                EDVerbose.warning("Writing thumbnail images to: %s" % strOutputDirname)

            self.strOutputPath = os.path.join(strOutputDirname, strImageNameWithoutExt + ".jpeg")
            self.strOutputPathThumb = os.path.join(strOutputDirname, strImageNameWithoutExt + ".thumb.jpeg")



    def process(self, _edObject=None):
        """
        This is the main method of the plugin, it does the job, not the EDNA name conversions which were done in the preprocess. 
        """

        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginPyarchThumbnailv10.process")
        if self.inputFilename:
            #        Read the image using FABIO
            fabioImage = openimage(self.inputFilename)
            # Convert an FabioImage to a PIL image
            npaImageRaw = fabioImage.data

            iMinLevel = 2
            iMaxLevel = 1000
            npaImageRaw = numpy.minimum(npaImageRaw, iMaxLevel * numpy.ones_like(npaImageRaw))
            npaImageRaw = numpy.maximum(npaImageRaw, iMinLevel * numpy.ones_like(npaImageRaw))

            npaImage = scipy.ndimage.morphology.grey_dilation(npaImageRaw, size=(5, 5))
            npaImageThumb = scipy.ndimage.morphology.grey_dilation(npaImageRaw, size=(10, 10))

            dtype = str(npaImage.dtype)
            if dtype == "uint8":
                NPAImageFloat = npaImage.astype("float") / 255.0
                NPAImageFloatThumb = npaImageThumb.astype("float") / 255.0
            elif dtype == "uint16":
                NPAImageFloat = npaImage.astype("float") / 65535.0
                NPAImageFloatThumb = npaImageThumb.astype("float") / 65535.0
            else: #for float or whatever
                vmin = npaImage.min()
                vmax = npaImage.max()
                NPAImageFloat = (npaImage.astype(float) - vmin) / (vmax - vmin)
                vminThumb = npaImageThumb.min()
                vmaxThumb = npaImageThumb.max()
                NPAImageFloatThumb = (npaImageThumb.astype(float) - vminThumb) / (vmax - vminThumb)

            NPAImageInt = (255.0 * (NPAImageFloat ** 0.3)).astype("uint8")
            NPAImageIntThumb = (255.0 * (NPAImageFloatThumb ** 0.3)).astype("uint8")

            pilImage = Image.fromarray(NPAImageInt, 'L')
            pilImageThumb = Image.fromarray(NPAImageIntThumb, 'L')
            # For ISPyB we use for the moment only 1024x1024 and 256x256
            pilImage.thumbnail((1024, 1024), Image.ANTIALIAS)
            pilImageThumb.thumbnail((256, 256), Image.ANTIALIAS)

            pilImage = ImageOps.invert(pilImage)
            pilImageThumb = ImageOps.invert(pilImageThumb)

            self.synchronizeOn()
            if 1024 * 1024 > ImageFile.MAXBLOCK:
                ImageFile.MAXBLOCK = 1024 * 1024


            pilImage.save(self.strOutputPath, "JPEG", quality=50, optimize=True)
            pilImageThumb.save(self.strOutputPathThumb, "JPEG", quality=85, optimize=True)

            self.synchronizeOff()

    def postProcess(self, _edObject=None):
        """
        Postprocess of the plugin:
         
        * set output of the plugin
        * free some memory from large arrays
        """
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginPyarchThumbnailv10.postProcess")
        # Create some output data
        if self.strOutputPath:
            xsDataResult = XSDataResultPyarchThumbnail()
            if os.path.isfile(self.strOutputPath):
                xsDataFile = XSDataFile()
                xsDataFile.setPath(XSDataString(self.strOutputPath))
                xsDataResult.setThumbnailPath(xsDataFile)
            self.setDataOutput(xsDataResult)


    def createPyarchFilePath(self, _strDNAFileDirectoryPath):
        """
        This method translates from a "visitor" path to a "pyarch" path:
        /data/visitor/mx415/id14eh1/20100209 -> /data/pyarch/id14eh1/mx415/20100209
        """
        strPyarchDNAFilePath = None
        listOfDirectories = _strDNAFileDirectoryPath.split(os.sep)
        listBeamlines = ["bm14", "id14eh1", "id14eh2", "id14eh3", "id14eh4", "id23eh1", "id23eh2", "id29"]
        # Check that we have at least four levels of directories:
        if (len(listOfDirectories) > 4):
            strDataDirectory = listOfDirectories[ 1 ]
            strSecondDirectory = listOfDirectories[ 2 ]
            strProposal = None
            strBeamline = None
            if ((strDataDirectory == "data") and (strSecondDirectory == "visitor")):
                strProposal = listOfDirectories[ 3 ]
                strBeamline = listOfDirectories[ 4 ]
            elif ((strDataDirectory == "data") and (strSecondDirectory in listBeamlines)):
                strBeamline = strSecondDirectory
                strProposal = listOfDirectories[ 4 ]
            if (strProposal != None) and (strBeamline != None):
                strPyarchDNAFilePath = os.path.join(os.sep, "data")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, "pyarch")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strBeamline)
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strProposal)
                for strDirectory in listOfDirectories[ 5: ]:
                    strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strDirectory)
        if (strPyarchDNAFilePath is None):
            EDVerbose.WARNING("EDPluginControlInterfaceToMXCuBEv1_3.createPyarchFilePath: path not converted for pyarch: %s " % _strDNAFileDirectoryPath)
        return strPyarchDNAFilePath

