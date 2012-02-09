# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF
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
__copyright__ = "2011 ESRF"
__status__ = "Development"
__date__ = "20120105"

import os, threading
from EDPluginControl        import EDPluginControl
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDConfiguration        import EDConfiguration
from EDUtilsPath            import EDUtilsPath
from EDUtilsPlatform        import EDUtilsPlatform
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
EDFactoryPluginStatic.loadModule("XSDataSAS")
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
EDFactoryPluginStatic.loadModule("XSDataExecCommandLine")
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsToSASv1_0, XSDataResultBioSaxsToSASv1_0
from XSDataSAS              import XSDataInputSolutionScattering
from XSDataWaitFilev1_0     import XSDataInputWaitFile
from XSDataExecCommandLine  import XSDataInputRsync
from XSDataCommon           import XSDataInteger, XSDataDouble, XSDataString, XSDataFile, XSPluginItem
architecture = EDUtilsPlatform.architecture
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)



class EDPluginBioSaxsToSASv1_0(EDPluginControl):
    """
	This is basically just a wrapper for Irakli's SAS pipeline, but with parameters optimized for ESRF
    """
    CONF_MAX_THREAD = "maxThreads"
    CONF_FILE_SIZE = "fileSize"
    size = None
    maxThreads = None
    ############################################################################
    # EDPluginControlSolutionScatteringv0_3 uses matplotlin in a non-thread-safe way. This is a global lock for this plugin 
    ############################################################################
    semSAS = threading.Semaphore()


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsToSASv1_0)

        self.__strControlledPluginWait = "EDPluginWaitFile"
        self.__strControlledPluginSAS = "EDPluginControlSolutionScatteringv0_3"
        self.__strControlledPluginRsync = "EDPluginExecRsync"
        self.__edPluginExecWait = None
        self.__edPluginExecSAS = None
        self.__edPluginExecRsync = None

        self.strInFile = None
        self.outFile = None
        self.wd = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsToSASv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.subtractedCurve, "Data Input is None")

    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters:
        - CONF_MAX_THREAD max number of threads in the action cluster
        - CONF_FILE_SIZE minimum file size 
        """
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginBioSaxsToSASv1_0.configure")
        if (self.__class__.size is None) or (self.__class__.maxThreads is None):
            xsPluginItem = self.getConfiguration()
            if (xsPluginItem == None):
                self.warning("EDPluginBioSaxsNormalizev1_1.configure: No plugin item defined.")
                xsPluginItem = XSPluginItem()
            self.__class__.size = int(EDConfiguration.getStringParamValue(xsPluginItem, self.CONF_FILE_SIZE))
            if self.__class__.size is None:
                strMessage = 'EDPluginBioSaxsToSASv1_0.configure: %s Configuration parameter missing: \
    %s, defaulting to "1000"' % (self.getBaseName(), self.CONF_FILE_SIZE)
                self.WARNING(strMessage)
                self.addErrorWarningMessagesToExecutiveSummary(strMessage)
                self.__class__.size = 1000

            self.__class__.maxThreads = int(EDConfiguration.getStringParamValue(xsPluginItem, self.CONF_MAX_THREAD))
            if self.__class__.maxThreads is None:
                strMessage = 'EDPluginBioSaxsToSASv1_0.configure: %s Configuration parameter missing: \
    %s, defaulting to "1"' % (self.getBaseName(), self.CONF_MAX_THREAD)
                self.WARNING(strMessage)
                self.addErrorWarningMessagesToExecutiveSummary(strMessage)
                self.__class__.maxThreads = 1


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsToSASv1_0.preProcess")
        if self.dataInput.subtractedCurve.path is not None:
            self.strInFile = self.dataInput.subtractedCurve.path.value
        if self.dataInput.destinationDirectory is not None:
            self.strWorkingDirectory = self.dataInput.destinationDirectory.path.value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsToSASv1_0.process")
        self.__edPluginExecWait = self.loadPlugin(self.__strControlledPluginWait)
        self.__edPluginExecWait.dataInput = XSDataInputWaitFile(expectedSize=XSDataInteger(self.__class__.size),
                                                                expectedFile=self.dataInput.subtractedCurve)
        self.__edPluginExecWait.connectSUCCESS(self.doSuccessExecWait)
        self.__edPluginExecWait.connectFAILURE(self.doFailureExecWait)
        self.__edPluginExecWait.executeSynchronous()

        if self.isFailure():
            return

        title = open(self.strInFile).readline()
        if title.startswith("#"):
            title = title[1:]
        if self.dataInput.firstPoint is not None:
            firstPoint = self.dataInput.firstPoint.value
        else:
            firstPoint = 0
            for line in open(self.strInFile):
                if line.startswith("# AutoRg: Points"):
                    try:
                        firstPoint = int(line[16:].split()[0])
                    except Exception, error:
                        self.WARNING("Unable to read first data point from line: %s %s" % (error, line))
                        firstPoint = 0
                    else:
                        break
                if line.startswith("# AutoRg: Quality:"):
                    quality = float(line[18:].split("%")[0])
                    if quality < 1:
                        self.warning("The quality of this dataset is very low (%.1f%%): garbage in garbage out !")
        if self.dataInput.lastPoint is not None:
            lastPoint = self.dataInput.lastPoint.value
        else:
            lastPoint = None
        datapoint = numpy.loadtxt(self.strInFile)[firstPoint:lastPoint]

        q = datapoint[:, 0]
        I = datapoint[:, 1]
        s = datapoint[:, 2]
        if self.dataInput.qMax is not None:
            mask = (q < self.dataInput.qMax.value)
        else:
            mask = numpy.ones(q.shape, dtype=bool)
        xsd = XSDataInputSolutionScattering(iNbThreads=XSDataInteger(self.__class__.maxThreads),
                                            angularUnits=None,
                                            rMaxSearchSettings=None,
                                            experimentalDataStdDev=[XSDataDouble(i) for i in s[mask]],
                                            experimentalDataValues=[XSDataDouble(i) for i in I[mask]],
                                            experimentalDataQ=[XSDataDouble(i / 10.0) for i in q[mask]], #convert from nm-1 to A-1 
                                            title=XSDataString(title.strip()))
        self.__edPluginExecSAS = self.loadPlugin(self.__strControlledPluginSAS)
        self.__edPluginExecSAS.dataInput = xsd
        self.__edPluginExecSAS.connectSUCCESS(self.doSuccessExecSAS)
        self.__edPluginExecSAS.connectFAILURE(self.doFailureExecSAS)
        with self.__class__.semSAS:
            self.__edPluginExecSAS.executeSynchronous()

        if self.isFailure():
            return
        if self.dataInput.destinationDirectory is None:
            outdir = os.path.join(os.path.dirname(os.path.dirname(self.strInFile)), "ednaSAS")
        else:
            outdir = self.dataInput.destinationDirectory.path.value
        outdir = os.path.join(outdir, os.path.basename(os.path.splitext(self.strInFile)[0]))
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        self.outFile = os.path.join(outdir, "pipelineResults.html")

        self.__edPluginExecRsync = self.loadPlugin(self.__strControlledPluginRsync)
        self.__edPluginExecRsync.dataInput = XSDataInputRsync(source=XSDataFile(XSDataString(self.wd)) ,
                                                                  destination=XSDataFile(XSDataString(outdir)),
                                                                  options=XSDataString("-avx"))

        self.__edPluginExecRsync.connectSUCCESS(self.doSuccessExecRsync)
        self.__edPluginExecRsync.connectFAILURE(self.doFailureExecRsync)
        self.__edPluginExecRsync.executeSynchronous()

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsToSASv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsToSASv1_0()
        if self.outFile:
            xsDataResult.htmlPage = XSDataFile(XSDataString(self.outFile))

        self.setDataOutput(xsDataResult)


    def doSuccessExecWait(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doSuccessExecWait")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doSuccessExecWait")


    def doFailureExecWait(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doFailureExecWait")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doFailureExecWait")
        self.setFailure()

    def doSuccessExecSAS(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doSuccessExecSAS")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doSuccessExecSAS")
        self.wd = os.path.join(_edPlugin.getWorkingDirectory(), "")

    def doFailureExecSAS(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doFailureExecSAS")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doFailureExecSAS")
        self.setFailure()

    def doSuccessExecRsync(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doSuccessExecRsync")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doSuccessExecRsync")


    def doFailureExecRsync(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsToSASv1_0.doFailureExecRsync")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsToSASv1_0.doFailureExecRsync")
        self.setFailure()
