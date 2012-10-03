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
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF Grenoble"
__date__ = "20120829"
__status__ = "Production"

import os, shutil
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataEdnaSaxs")
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataCommon       import XSDataString, XSDataStatus, XSDataFile, XSDataTime, XSDataInteger
from XSDataBioSaxsv1_0  import XSDataInputBioSaxsSmartMergev1_0, XSDataResultBioSaxsSmartMergev1_0
from XSDataEdnaSaxs     import XSDataInputDatcmp, XSDataInputDataver, XSDataInputAutoSub, XSDataInputDatop
from XSDataWaitFilev1_0 import XSDataInputWaitMultiFile

def cmp(a, b):
    """
    Helper function to sort XSDataFile object
    """
    strA = a.path.value
    strB = a.path.value
    if strA > strB:
        return 1
    elif strA < strB:
        return - 1
    else:
        return 0


class EDPluginBioSaxsSmartMergev1_3(EDPluginControl):
    """
    This plugin takes a set of input data files (1D SAXS) measure
    their differences (versus previous and versus first) and merge those which are equivalent
    v1.1 adds information from AutoSub
    
    Controlled plugins:
     - Execplugins/WaitMultifile
     - EdnaSaxs/Atsas/DatCmp
     - EdnaSaxs/Atsas/DatAver
     - EdnaSaxs/Atsas/AutoSub
    """
    #dictAve = {} #key=?; value=path to average file
    lastBuffer = None
    lastSample = None

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.__strControlledPluginDataver = "EDPluginExecDataverv1_0"
        self.__strControlledPluginDatcmp = "EDPluginExecDatcmpv1_0"
        self.__strControlledPluginWaitFile = "EDPluginWaitMultiFile"
        self.__strControlledPluginAutoSub = "EDPluginAutoSubv1_0"
#        self.__strControlledPluginDatop = "EDPluginExecDatopv1_0"

        self.__edPluginExecDatcmp = None
        self.__edPluginExecDataver = None
        self.__edPluginExecWaitFile = None
        self.__edPluginExecAutoSub = None
        self.__edPluginExecDataop = None
        self.setXSDataInputClass(XSDataInputBioSaxsSmartMergev1_0)
        self.__edPluginExecDatCmp = None
        self.lstInput = []
        self.lstMerged = []
        self.lstXsdInput = []
        self.absoluteFidelity = None
        self.relativeFidelity = None
        self.dictSimilarities = {} #key: 2-tuple of images, similarities
        self.lstSummary = []
        self.lstStrInput = []
#        self.sample = XSDataSample()
        self.autoRg = None
        self.strRadiationDamage = None
        self.strMergedFile = None
#        self.tKey = (None,)
        self.lstSub = []
        self.strSubFile = None
        self.fConcentration = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputCurves, "Input curve list is empty")
        self.checkMandatoryParameters(self.dataInput.mergedCurve, "Output curve filename  is empty")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.preProcess")
        # Load the execution plugin
        if self.dataInput.absoluteFidelity is not None:
            self.absoluteFidelity = self.dataInput.absoluteFidelity.value
            if self.absoluteFidelity == 0.0:
                self.absoluteFidelity = None
        if self.dataInput.relativeFidelity is not None:
            self.relativeFidelity = self.dataInput.relativeFidelity.value
            if self.relativeFidelity == 0.0:
                self.relativeFidelity = None
        self.lstInput = self.dataInput.inputCurves
        self.lstStrInput = [i.path.value for i in self.lstInput]
        self.__edPluginExecWaitFile = self.loadPlugin(self.__strControlledPluginWaitFile)

        if self.dataInput.mergedCurve is not None:
            self.strMergedFile = self.dataInput.mergedCurve.path.value

        if self.dataInput.subtractedCurve is not None:
            self.strSubFile = self.dataInput.subtractedCurve.path.value
            dirname = os.path.dirname(self.strSubFile)
            if not os.path.isdir(dirname):
                os.mkdir(dirname)

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.process")

        xsdwf = XSDataInputWaitMultiFile(timeOut=XSDataTime(30),
                                        expectedSize=XSDataInteger(10000),
                                        expectedFile=[XSDataFile(i.path) for i in self.lstInput])
        self.__edPluginExecWaitFile.setDataInput(xsdwf)
        self.__edPluginExecWaitFile.connectFAILURE(self.doFailureExecWait)
        self.__edPluginExecWaitFile.connectSUCCESS(self.doSuccessExecWait)
        self.__edPluginExecWaitFile.executeSynchronous()
        if self.isFailure():
            return
        if len(self.lstInput) == 1:
            inp = self.lstInput[0].path.value
            dst = self.dataInput.mergedCurve.path.value
            if not os.path.isdir(os.path.dirname(dst)):
                 self.error("Output directory for %s does not exist"%dst)
                 os.makedirs(os.path.dirname(dst))
            if not os.path.exists(inp):
                 self.warning("Input %s does not (yet?) exist"%inp)
                 time.sleep(1.0)
            shutil.copyfile(inp, dst)
        else:
            self.lstMerged = []
            if (self.absoluteFidelity is not None) or (self.relativeFidelity is not None):
                if self.absoluteFidelity is not None :
                    for idx, oneFile in enumerate(self.lstInput[1:]):
                        self.DEBUG("Calculating similarity of 0 and %s" % idx)
                        edPluginExecAbsoluteFidelity = self.loadPlugin(self.__strControlledPluginDatcmp)
                        xsd = XSDataInputDatcmp(inputCurve=[self.lstInput[0], oneFile])
                        edPluginExecAbsoluteFidelity.setDataInput(xsd)
                        edPluginExecAbsoluteFidelity.connectFAILURE(self.doFailureExecDatcmp)
                        edPluginExecAbsoluteFidelity.connectSUCCESS(self.doSuccessExecDatcmp)
                        edPluginExecAbsoluteFidelity.execute()
                if (self.relativeFidelity is not None):
                    if (self.absoluteFidelity is  None):
                        self.DEBUG("Calculating similarity of 0 and 1")
                        edPluginExecAbsoluteFidelity = self.loadPlugin(self.__strControlledPluginDatcmp)
                        xsd = XSDataInputDatcmp(inputCurve=[self.lstInput[0], self.lstInput[1] ])
                        edPluginExecAbsoluteFidelity.setDataInput(xsd)
                        edPluginExecAbsoluteFidelity.connectFAILURE(self.doFailureExecDatcmp)
                        edPluginExecAbsoluteFidelity.connectSUCCESS(self.doSuccessExecDatcmp)
                        edPluginExecAbsoluteFidelity.execute()
                    if (len(self.lstInput) > 2):
                        for idx, oneFile in enumerate(self.lstInput[2:]):
                            self.DEBUG("Calculating similarity of %s and %s" % (idx, idx + 1))
                            edPluginExecRelativeFidelity = self.loadPlugin(self.__strControlledPluginDatcmp)
                            xsd = XSDataInputDatcmp(inputCurve=[self.lstInput[idx + 1], oneFile])
                            edPluginExecRelativeFidelity.setDataInput(xsd)
                            edPluginExecRelativeFidelity.connectFAILURE(self.doFailureExecDatcmp)
                            edPluginExecRelativeFidelity.connectSUCCESS(self.doSuccessExecDatcmp)
                            edPluginExecRelativeFidelity.execute()
            self.synchronizePlugins()

            for idx, oneFile in enumerate(self.lstInput):
                if idx == 0:
                    self.lstMerged.append(oneFile)
                elif (self.absoluteFidelity is not None) and (self.relativeFidelity is not None):
                    if (idx - 1, idx) not in self.dictSimilarities:
                        self.ERROR("dict missing %i,%i: \n" % (idx - 1, idx) + "\n".join([ "%s: %s" % (key, self.dictSimilarities[key]) for key in self.dictSimilarities]))
                    if (0, idx) not in self.dictSimilarities:
                        self.ERROR("dict missing %i,%i: \n" % (0, idx) + "\n".join([ "%s: %s" % (key, self.dictSimilarities[key]) for key in self.dictSimilarities]))

                    if (self.dictSimilarities[(0, idx)] >= self.absoluteFidelity) and (self.dictSimilarities[(idx - 1, idx)] >= self.relativeFidelity):
                        self.lstMerged.append(oneFile)
                    else:
                        break
                elif (self.absoluteFidelity is not None) :
                    if (0, idx) not in self.dictSimilarities:
                        self.ERROR("dict missing %i,%i: \n" % (0, idx) + "\n".join([ "%s: %s" % (key, self.dictSimilarities[key]) for key in self.dictSimilarities]))

                    if (self.dictSimilarities[(0, idx)] >= self.absoluteFidelity):
                        self.lstMerged.append(oneFile)
                    else:
                        break
                elif (self.relativeFidelity is not None) :
                    if (idx - 1, idx) not in self.dictSimilarities:
                        self.ERROR("dict missing %i,%i: \n" % (idx - 1, idx) + "\n".join([ "%s: %s" % (key, self.dictSimilarities[key]) for key in self.dictSimilarities]))

                    if (self.dictSimilarities[(idx - 1, idx)] >= self.relativeFidelity):
                        self.lstMerged.append(oneFile)
                    else:
                        break
                else:
                    self.lstMerged.append(oneFile)
            self.lstMerged.sort(cmp)
            if len(self.lstMerged) != len(self.lstInput):
                self.strRadiationDamage = "Radiation damage detected, merged %i curves" % len(self.lstMerged)
                self.WARNING(self.strRadiationDamage)
                self.lstSummary.append("WARNING: " + self.strRadiationDamage)
            self.lstSummary.append("Merging files: " + " ".join([os.path.basename(i.path.value) for i in self.lstMerged]))
            if len(self.lstMerged) == 1:
                self.rewriteHeader(self.lstMerged[0].path.value, self.strMergedFile)
            else:
                self.__edPluginExecDataver = self.loadPlugin(self.__strControlledPluginDataver)
                xsd = XSDataInputDataver(inputCurve=self.lstMerged)
                #outputCurve=self.dataInput.mergedCurve,
                self.__edPluginExecDataver.setDataInput(xsd)
                self.__edPluginExecDataver.connectSUCCESS(self.doSuccessExecDataver)
                self.__edPluginExecDataver.connectFAILURE(self.doFailureExecDataver)
                self.__edPluginExecDataver.executeSynchronous()

            if (self.fConcentration == 0) and (self.strSubFile is not None):
                if (self.__class__.lastBuffer is not None) and (self.__class__.lastSample is not None):
                    self.__edPluginExecAutoSub = self.loadPlugin(self.__strControlledPluginAutoSub)
                    base = "_".join(os.path.basename(self.__class__.lastSample.path.value).split("_")[:-1])
                    suff = os.path.basename(self.strSubFile).split("_")[-1]
                    sub = os.path.join(os.path.dirname(self.strSubFile), base + "_" + suff)
                    xsd = XSDataInputAutoSub(sampleCurve=self.__class__.lastSample,
                                             buffers=[self.__class__.lastBuffer, self.dataInput.mergedCurve],
                                             subtractedCurve=XSDataFile(XSDataString(sub))
                                             )
                    self.__edPluginExecAutoSub.setDataInput(xsd)
                    self.__edPluginExecAutoSub.connectSUCCESS(self.doSuccessExecAutoSub)
                    self.__edPluginExecAutoSub.connectFAILURE(self.doFailureExecAutoSub)
                    self.__edPluginExecAutoSub.executeSynchronous()
                self.__class__.lastBuffer = self.dataInput.mergedCurve
                self.__class__.lastSample = None
            else:
                self.__class__.lastSample = self.dataInput.mergedCurve


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsSmartMergev1_0()
        xsDataResult.mergedCurve = self.dataInput.mergedCurve
        executiveSummary = os.linesep.join(self.lstSummary)
        xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        if self.autoRg is not None:
            xsDataResult.autoRg = self.autoRg
        if self.strSubFile is not None and os.path.isfile(self.strSubFile):
            xsDataResult.subtractedCurve = XSDataFile(XSDataString(self.strSubFile))
        self.setDataOutput(xsDataResult)
#        self.DEBUG(executiveSummary)


    def rewriteHeader(self, infile=None, output=None, hdr="#", linesep=os.linesep):
        """
        Write the output file with merged data with the good header.

# BSA sample
#Sample c= 0.0 mg/ml
#
# Merged from: file1
# Merged from: file2
# Merged from: file4
#
# Sample Information:
# Concentration: 0.0
# Code: BSA

        @param infile: path of the original data file where original data are taken from
        @param outfile: path of the destination file (by default, from XSD)
        @param hdr: header marker, often "#"
        @param linesep: line separator, usually "\n" or "\r\n" depending on the Operating System 
        @return: None
        """
        Code = Concentration = None
        frameMax = exposureTime = measurementTemperature = storageTemperature = None
        originalFile = self.lstMerged[0].path.value
        headers = [line.strip() for line in open(originalFile) if line.startswith("#")]
        Comments = headers[0][1:].strip()
        for line in headers:
            if "title =" in  line:
                Comments = line.split("=", 1)[1].strip()
            elif "Comments =" in line:
                Comments = line.split("=", 1)[1].strip()
            elif "Concentration:" in line:
                Concentration = line.split(":", 1)[1].strip()
            elif "Concentration =" in line:
                Concentration = line.split("=", 1)[1].strip()
            elif "Code =" in line:
                Code = line.split("=", 1)[1].strip()
            elif "Code:" in line:
                Code = line.split(":", 1)[1].strip()
            elif "Storage Temperature" in line:
                storageTemperature = line.split(":", 1)[1].strip()
            elif "Measurement Temperature" in line:
                measurementTemperature = line.split(":", 1)[1].strip()
            elif "Time per frame" in line:
                exposureTime = line.split("=", 1)[1].strip()
            elif "Frame" in line:
                frameMax = line.split()[-1]
        try:
            c = float(Concentration)
        except Exception:
            c = -1.0
        self.fConcentration = c
        lstHeader = ["%s %s" % (hdr, Comments), "%s Sample c= %s mg/ml" % (hdr, Concentration), hdr]
        if frameMax is not None:
            lstHeader.append(hdr + " Number of frames collected: %s" % frameMax)
        if exposureTime is not None:
            lstHeader.append(hdr + " Exposure time per frame: %s" % exposureTime)

        if self.strRadiationDamage is None:
            lstHeader.append("%s No significant radiation damage detected, merging %i files" % (hdr, len(self.lstMerged)))
        else:
            lstHeader.append("%s WARNING: %s" % (hdr, self.strRadiationDamage))
        lstHeader += [hdr + " Merged from: %s" % i.path.value for i in self.lstMerged]
        if self.lstSub:
            lstHeader.append(hdr)
            lstHeader += ["%s %s" % (hdr, i) for i in self.lstSub]
        lstHeader += [hdr, hdr + " Sample Information:"]
        if storageTemperature is not None:
            lstHeader.append(hdr + " Storage Temperature (degrees C): %s" % storageTemperature)
        if measurementTemperature is not None:
            lstHeader.append(hdr + " Measurement Temperature (degrees C): %s" % measurementTemperature)

        lstHeader += [hdr + " Concentration: %s" % Concentration, "# Code: %s" % Code]
        if infile is None:
            infile = self.strMergedFile
        if output is None:
            output = self.strMergedFile
        data = linesep.join([ i.strip() for i in open(infile) if not i.startswith(hdr)])
        with open(output, "w") as outfile:
            outfile.write(linesep.join(lstHeader))
            if not data.startswith(linesep):
                outfile.write(linesep)
            outfile.write(data)


    def doSuccessExecWait(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doSuccessExecWait")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doSuccessExecWait")
        xsdo = _edPlugin.dataOutput
        #self.error("ExecWait Output:%s"%xsdo.marshal())
        if (xsdo.timedOut is not None) and  bool(xsdo.timedOut.value):
            strErr = "Error in waiting for all input files to arrive"
            self.ERROR(strErr)
            self.setFailure()


    def doFailureExecWait(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doFailureExecWait")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doFailureExecWait")
        strErr = "Error in waiting for all input files to arrive"
        self.ERROR(strErr)
        self.lstSummary.append(self.ERROR)
        self.setFailure()


    def doSuccessExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doSuccessExecDataver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doSuccessExecDataver")
        self.rewriteHeader(_edPlugin.dataOutput.outputCurve.path.value, output=self.strMergedFile)


    def doFailureExecDataver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doFailureExecDataver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doFailureExecDataver")
        strErr = "Error in Processing of Atsas 'dataver'"
        self.lstSummary.append(strErr)
        self.ERROR(strErr)
        self.setFailure()


    def doSuccessExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doSuccessExecDatcmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doSuccessExecDatcmp")
        with self.locked():
            xsdIn = _edPlugin.dataInput
            xsdOut = _edPlugin.getDataOutput()
            file0 = xsdIn.inputCurve[0].path.value
            file1 = xsdIn.inputCurve[1].path.value
            fidelity = xsdOut.fidelity.value
            lstIdx = [self.lstStrInput.index(file0), self.lstStrInput.index(file1)]
            lstIdx.sort()
            self.dictSimilarities[tuple(lstIdx)] = fidelity
            lstIdx.reverse()
            self.dictSimilarities[tuple(lstIdx)] = fidelity
            self.lstSummary.append("Fidelity between %s and %s is %s" % (os.path.basename(file0), os.path.basename(file1), fidelity))


    def doFailureExecDatcmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doFailureExecDatcmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doFailureExecDatcmp")
        self.lstSummary.append("Failure in Processing of Atsas 'datcmp'")
        self.setFailure()


    def doSuccessExecAutoSub(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doSuccessExecAutoSub")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doSuccessExecAutoSub")
        self.autoRg = _edPlugin.dataOutput.autoRg
        self.lstSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)


    def doFailureExecAutoSub(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsSmartMergev1_3.doFailureExecAutoSub")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsSmartMergev1_3.doFailureExecAutoSub")
        strErr = "Error in Processing of EDNA 'AutoSub'"
        self.ERROR(strErr)
        self.lstSummary.append(strErr)
        self.setFailure()

