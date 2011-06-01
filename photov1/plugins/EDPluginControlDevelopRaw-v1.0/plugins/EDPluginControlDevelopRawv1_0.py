#
#    Project: Photov1 Demo
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
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
__copyright__ = "ESRF, Grenoble"

import os
from EDVerbose                  import EDVerbose
from EDPluginControl            import EDPluginControl
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataCommon               import XSDataString, XSDataFile, XSDataBoolean
from XSDataPhotov1              import XSDataInputDevelopRawv1
from XSDataPhotov1              import XSDataResultDevelopRawv1
from XSDataPhotov1              import XSDataInputExecDcrawv1
from XSDataPhotov1              import XSDataInputCopyExifv1
EDFactoryPluginStatic.loadModule("XSDataExecCommandLine")
from XSDataExecCommandLine      import XSDataInputExecCommandLine
EDFactoryPluginStatic.loadModule("XSDataExecThumbnail")
from XSDataExecThumbnail        import XSDataInputExecThumbnail

class EDPluginControlDevelopRawv1_0(EDPluginControl):
    """
    Control plugin that builds the pipeline  
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputDevelopRawv1)
        self.__strControlledPluginDcraw = "EDPluginExecDcrawv1_0"
        self.__strControlledPluginThumbnail = "EDPluginExecThumbnailv10"
        self.__strControlledPluginMetadata = "EDPluginCopyExifv1_0"
        self.__strControlledPluginBzip2 = "EDPluginExecCommandLinev10"
        self.__edPluginExecDcraw = None
        self.__edPluginExecThumbnail = None
        self.__edPluginExecMetadata = None
        self.__edPluginExecBzip2 = None

        self.strRawFile = None
        self.strJpegFile = None
        self.bCleanUp = None
        self.bCompressRaw = None
        self.bCopyExif = None
        self.xsdTempFile = None
        self.xsdfJpeg = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputRaw(), "No Raw input file provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.preProcess")
        self.strRawFile = self.getDataInput().getInputRaw().getPath().getValue()
        if self.getDataInput().getOutputJpeg() is None:
            self.strJpegFile = os.path.splitext(self.strRawFile)[0] + "-raw.jpg"
        else:
            self.strJpegFile = self.getDataInput().getOutputJpeg().getPath().getValue()

        if self.getDataInput().getCopyExifTag() is None:
            self.bCopyExif = True
        else:
            self.bCopyExif = (self.getDataInput().getCopyExifTag().getValue() in [1, "true", "True", True])

        if self.getDataInput().getCompressRaw() is None:
            self.bCompressRaw = True
        else:
            self.bCompressRaw = (self.getDataInput().getCompressRaw().getValue() in [1, "true", "True", True])

        if self.getDataInput().getCleanUp() is None:
            self.bCleanUp = True
        else:
            self.bCleanUp = (self.getDataInput().getCleanUp().getValue() in [1, "true", "True", True])


        # Load the execution plugin
        self.__edPluginExecDcraw = self.loadPlugin(self.__strControlledPluginDcraw)
        self.__edPluginExecThumbnail = self.loadPlugin(self.__strControlledPluginThumbnail)
        if self.bCompressRaw is True:
            self.__edPluginExecBzip2 = self.loadPlugin(self.__strControlledPluginBzip2)
        if self.bCopyExif is True:
            self.__edPluginExecMetadata = self.loadPlugin(self.__strControlledPluginMetadata)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.process")
        xsdin = XSDataInputExecDcrawv1()
        xsdin.setRawImagePath(self.getDataInput().getInputRaw())
#        EDVerbose.DEBUG("xsdin: %s" % xsdin.marshal())
        self.__edPluginExecDcraw.setDataInput(xsdin)
        self.__edPluginExecDcraw.connectSUCCESS(self.doSuccessExecDcraw)
        self.__edPluginExecDcraw.connectFAILURE(self.doFailureExecDcraw)
        self.__edPluginExecDcraw.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultDevelopRawv1()
        self.setDataOutput(xsDataResult)


    def doSuccessExecDcraw(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doSuccessExecDcraw")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doSuccessExecDcraw")
        self.xsdTempFile = _edPlugin.getDataOutput().getOutputPath()
        xsdin = XSDataInputExecThumbnail()
        xsdin.setInputImagePath(self.xsdTempFile)
        self.xsdfJpeg = XSDataFile(XSDataString(self.strJpegFile))
        xsdin.setOutputPath(self.xsdfJpeg)
        self.__edPluginExecThumbnail.setDataInput(xsdin)
        self.__edPluginExecThumbnail.connectSUCCESS(self.doSuccessExecThumbnail)
        self.__edPluginExecThumbnail.connectFAILURE(self.doFailureExecThumbnail)
        self.__edPluginExecThumbnail.executeSynchronous()


    def doFailureExecDcraw(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doFailureExecDcraw")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doFailureExecDcraw")
        self.setFailure()


    def doSuccessExecThumbnail(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doSuccessExecThumbnail")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doSuccessExecThumbnail")
        if self.bCleanUp:
            tmpfile = self.xsdTempFile.getPath().getValue()
            if os.path.isfile(tmpfile):
                EDVerbose.DEBUG("Removing temp-file %s as requested" % tmpfile)
                os.remove(tmpfile)
        if self.bCopyExif is True:
            xsdin = XSDataInputCopyExifv1()
            xsdin.setInputImagePath(self.getDataInput().getInputRaw())
            xsdin.setOutputImagePath(self.xsdfJpeg)
            self.__edPluginExecMetadata.setDataInput(xsdin)
            self.__edPluginExecMetadata.connectSUCCESS(self.doSuccessExecMetadata)
            self.__edPluginExecMetadata.connectFAILURE(self.doFailureExecMetadata)
            self.__edPluginExecMetadata.executeSynchronous()

        elif self.bCompressRaw is True:
            self.compressRaw()

    def compressRaw(self):
        xsdin = XSDataInputExecCommandLine()
        xsdin.setFireAndForget(XSDataBoolean(1))
        xsdin.setInputFileName(self.getDataInput().getInputRaw())
        xsdin.setCommandLineOptions(XSDataString("-9"))
        xsdf = XSDataFile()
        xsdf.setPath(XSDataString("/bin/bzip2"))
        xsdin.setCommandLineProgram(xsdf)
        self.__edPluginExecBzip2.setDataInput(xsdin)
        self.__edPluginExecBzip2.connectSUCCESS(self.doSuccessExecBzip2)
        self.__edPluginExecBzip2.connectFAILURE(self.doFailureExecBzip2)
        self.__edPluginExecBzip2.executeSynchronous()

    def doFailureExecThumbnail(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doFailureExecThumbnail")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doFailureExecThumbnail")
        self.setFailure()


    def doSuccessExecMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doSuccessExecMetadata")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doSuccessExecMetadata")
        if self.bCompressRaw is True:
            self.compressRaw()

    def doFailureExecMetadata(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doFailureExecMetadata")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doFailureExecMetadata")
        self.setFailure()

    def doSuccessExecBzip2(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doSuccessExecBzip2")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doSuccessExecBzip2")


    def doFailureExecBzip2(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlDevelopRawv1_0.doFailureExecBzip2")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDevelopRawv1_0.doFailureExecBzip2")
        self.setFailure()
