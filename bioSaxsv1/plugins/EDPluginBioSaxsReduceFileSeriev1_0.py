# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF Grenoble
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
__copyright__ = "2011, ESRF Grenoble"

import time, os
from EDPluginControl import EDPluginControl
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsReduceFileSeriev1_0, XSDataResultBioSaxsReduceFileSeriev1_0, \
    XSDataInputBioSaxsProcessOneFilev1_0, XSDataInputBioSaxsSmartMergev1_0
from XSDataCommon import XSDataInteger, XSDataString, XSDataFile, XSDataImage, \
    XSDataStatus

class EDPluginBioSaxsReduceFileSeriev1_0(EDPluginControl):
    """
    Control plugin that does: 
    
    * n times processOneFile
    * synchronize plugins
    * smart merge at the end
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsReduceFileSeriev1_0)
        self.__strControlledPluginProcessOneFile = "EDPluginBioSaxsProcessOneFilev1_0"
        self.__strControlledPluginSmartMerge = "EDPluginBioSaxsSmartMergev1_0"
        self.__edPluginExecSmartMerge = None
        self.bSkipProcess = False
        self.sample = None
        self.experimentSetup = None
        self.lstRawImg = []
        self.lstCorImg = []
        self.lstIntImg = []
        self.lstIntCrv = []
        self.lstLogFil = []
        self.strMergedCurve = ""
        self.lstCurves = [] #list of 1D curves produced by the data reduction
        self.lstSummary = []
        self.strSummary = ""
        self.absoluteFidelity = None
        self.relativeFidelity = None
        self.forceReprocess = False
        self.rawImageSize = XSDataInteger(1024)
        self.directory1D = None
        self.directory2D = None
        self.directoryMisc = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.fileSerie, "No file serie provided")
        self.checkMandatoryParameters(self.dataInput.sample, "No sample information provided")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "No experimental setup provided")
        self.checkMandatoryParameters(self.dataInput.directory1D, "No directory for 1D curves provided")
        self.checkMandatoryParameters(self.dataInput.directory2D, "No directory for storing 2D processed data")
        self.checkMandatoryParameters(self.dataInput.directoryMisc, "No directory for storing misc data provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.preProcess")
        self.sample = self.dataInput.sample
        self.experimentSetup = self.dataInput.experimentSetup
        self.lstRawImg = [XSDataImage(i.path) for i in self.dataInput.fileSerie.files]
        self.directory1D = self.dataInput.directory1D.path.value
        self.directory2D = self.dataInput.directory2D.path.value
        self.directoryMisc = self.dataInput.directoryMisc.path.value
        if self.dataInput.forceReprocess is not None:
            self.forceReprocess = bool(self.dataInput.forceReprocess.value)
        if self.dataInput.rawImageSize is not None:
            self.rawImageSize = self.dataInput.rawImageSize

        bForceNewDirectories = False
        listBasname = [os.path.basename(i.path.value) for i in self.lstRawImg]
        common = os.path.commonprefix(listBasname)
        self.strMergedCurve = os.path.join(self.directory1D, common + "ave.dat")
        list2D = [os.path.join(self.directory2D, i) for i in listBasname]
        list1D = [os.path.join(self.directory1D, os.path.splitext(i)[0] + ".dat") for i in listBasname]
        listMisc = [os.path.join(self.directoryMisc, os.path.splitext(i)[0] + ".ang") for i in listBasname]
        found = [os.path.exists(i) for i in list1D + list2D + [self.strMergedCurve]]
        found.sort()
        if found[0]: #all files exists
            self.WARNING("All destination files already exists")
            self.lstSummary.append("All destination files already exists")
            if not self.forceReprocess: #then everything is already done
                self.bSkipProcess = True
            else:
                bForceNewDirectories = True
        elif found[-1]:
            self.WARNING("At lease few destination files already exists, but not all ... I will reprocess in another directory")
            self.lstSummary.append("At lease few destination files already exists, but not all ... I will reprocess in another directory")
            bForceNewDirectories = True

        if bForceNewDirectories:
            suffix = time.strftime("-%Y%m%d%H%M%S", time.localtime())
            self.lstSummary.append("Adding suffix %s to directories" % suffix)
            self.directory1D += suffix
            self.directory2D += suffix
            self.directoryMisc += suffix
            self.strMergedCurve = os.path.join(self.directory1D, common + "ave.dat")

        if not os.path.isdir(self.directory1D):
            os.makedirs(self.directory1D)
        if not os.path.isdir(self.directory2D):
            os.makedirs(self.directory2D)
        if not os.path.isdir(self.directoryMisc):
            os.makedirs(self.directoryMisc)

        self.lstCorImg = [ XSDataImage(XSDataString(i)) for i in list2D]
        self.lstIntImg = [ XSDataImage(XSDataString(i)) for i in listMisc]
        self.lstIntCrv = [ XSDataFile(XSDataString(i)) for i in list1D]
        self.lstLogFil = [XSDataFile(XSDataString(os.path.join(self.directoryMisc, os.path.splitext(i)[0] + ".log")))\
                           for i in listBasname]


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.process")

        if self.bSkipProcess:
            return


        for oneRaw, oneCor, oneInt, oneCrv, oneLog in zip(self.lstRawImg, self.lstCorImg, self.lstIntImg, self.lstIntCrv, self.lstLogFil):
            pluginProcessOneFile = self.loadPlugin(self.__strControlledPluginProcessOneFile)
            xsd = XSDataInputBioSaxsProcessOneFilev1_0(integratedCurve=oneCrv,
                                                       integratedImage=oneInt,
                                                       normalizedImage=oneCor,
                                                       rawImageSize=self.rawImageSize,
                                                       experimentSetup=self.experimentSetup,
                                                       sample=self.sample,
                                                       rawImage=oneRaw,
                                                       logFile=oneLog)
            pluginProcessOneFile.dataInput = xsd
            pluginProcessOneFile.connectSUCCESS(self.doSuccessExecProcessOneFile)
            pluginProcessOneFile.connectFAILURE(self.doFailureExecProcessOneFile)
            pluginProcessOneFile.execute()

        self.synchronizePlugins()
        self.lstCurves.sort()
        xsdMerge = XSDataInputBioSaxsSmartMergev1_0()
        xsdMerge.absoluteFidelity = self.dataInput.absoluteFidelity
        xsdMerge.relativeFidelity = self.dataInput.relativeFidelity
        xsdMerge.inputCurves = [XSDataFile(XSDataString(i)) for i in self.lstCurves]
        xsdMerge.mergedCurve = XSDataFile(XSDataString(self.strMergedCurve))
        edPluginExecSmartMerge = self.loadPlugin(self.__strControlledPluginSmartMerge)
        edPluginExecSmartMerge.dataInput = xsdMerge
        edPluginExecSmartMerge.connectSUCCESS(self.doSuccessExecSmartMerge)
        edPluginExecSmartMerge.connectFAILURE(self.doFailureExecSmartMerge)
        edPluginExecSmartMerge.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.postProcess")
        # Create some output data
        executiveSummary = os.linesep.join(self.lstSummary)
        xsDataResult = XSDataResultBioSaxsReduceFileSeriev1_0()
        xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        xsDataResult.directory1D = XSDataFile(XSDataString(self.directory1D))
        xsDataResult.directory2D = XSDataFile(XSDataString(self.directory2D))
        xsDataResult.directoryMisc = XSDataFile(XSDataString(self.directoryMisc))
        xsDataResult.mergedCurve = XSDataFile(XSDataString(self.strMergedCurve))
        self.setDataOutput(xsDataResult)
        self.DEBUG(executiveSummary)

    def doSuccessExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.doSuccessExecProcessOneFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsReduceFileSeriev1_0.doSuccessExecProcessOneFile")
        self.synchronizeOn()
        xsdOut = _edPlugin.dataOutput
        self.lstSummary.append(xsdOut.status.executiveSummary.value)
        self.lstCurves.append(xsdOut.integratedCurve.path.value)
        self.synchronizeOff()


    def doFailureExecProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.doFailureExecProcessOneFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsReduceFileSeriev1_0.doFailureExecProcessOneFile")
        self.synchronizeOn()
        self.setFailure()
        pluginId = "Unknown"
        try:
            pluginId = _edPlugin.getId()
            xsdOut = _edPlugin.dataOutput
        except Exception:
            self.ERROR("ExecProcessOneFile: No dataOutput")
        else:
            try:
                self.lstSummary.append(xsdOut.status.executiveSummary.value)
                self.lstCurves.append(xsdOut.integratedCurve.path.value)
            except Exception:
                pass
        self.lstSummary.append("EDPluginBioSaxsProcessOneFilev1_0 %s failed" % pluginId)
        self.synchronizeOff()


    def doSuccessExecSmartMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.doSuccessExecSmartMerge")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsReduceFileSeriev1_0.doSuccessExecSmartMerge")
        self.synchronizeOn()
        pluginId = "Unknown"
        try:
            pluginId = _edPlugin.getId()
            xsdOut = _edPlugin.dataOutput
        except Exception:
            self.ERROR("ExecProcessOneFile: No dataOutput")
        else:
            try:
                if xsdOut.status is not None:
                    self.lstSummary.append(xsdOut.status.executiveSummary.value)
            except Exception:
                pass
        self.lstSummary.append("EDPluginBioSaxsSmartMergev1_0 %s failed" % pluginId)
        self.synchronizeOff()


    def doFailureExecSmartMerge(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsReduceFileSeriev1_0.doFailureExecSmartMerge")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsReduceFileSeriev1_0.doFailureExecSmartMerge")
        self.synchronizeOn()
        self.setFailure()
        pluginId = "Unknown"
        try:
            pluginId = _edPlugin.getId()
            xsdOut = _edPlugin.dataOutput
        except Exception:
            self.ERROR("ExecProcessOneFile: No dataOutput")
        else:
            try:
                self.lstSummary.append(xsdOut.status.executiveSummary.value)
                self.xsdMergedCurve = xsdOut
            except Exception:
                pass
        self.lstSummary.append("EDPluginBioSaxsSmartMergev1_0 %s failed" % pluginId)
        self.synchronizeOff()
