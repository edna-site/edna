#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:       irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os

from matplotlib import pylab


from EDVerbose import EDVerbose
from EDUtilsFile                     import EDUtilsFile
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataSAS import XSDataInputGnom
from XSDataSAS import XSDataResultGnom
from XSDataSAS import XSDataFile, XSDataString, XSDataDouble

class EDPluginExecGnomv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for small  angle scattering data processing using GNOM
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputGnom)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecGnomv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExperimentalDataQ(), "Scattering vector values are missing")
        self.checkMandatoryParameters(self.getDataInput().getExperimentalDataValues(), "Experimental intensity values are missing")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecGnomv0_1.preProcess")
        self.generateGnomConfigFile()
        self.generateGnomScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecGnomv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecGnomv0_1.postProcess")
        # Create some output data
        xsDataResult = self.parseGnomOutputFile()

        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(os.path.join(self.getWorkingDirectory(), "gnom.out")))

        xsDataResult.setOutput(xsDataFile)

        self.setDataOutput(xsDataResult)

    def generateGnomScript(self):
        EDVerbose.DEBUG("*** EDPluginExecGnomv0_1.generateGnomScript")
        self.generateGnomInputFile()
        self.setScriptCommandline("")
        if self.getDataInput().getAngularScale() is None:
            fAngularScale = 1
        else:
            fAngularScale = self.getDataInput().getAngularScale().getValue()
        commandString = 'gnom_tmp.dat' + \
                        '\n' * 5 + str(fAngularScale) + \
                        '\n' * 5 + str(self.getDataInput().getRMax().getValue()) + \
                        '\n' * 3 + 'No' + '\n' * 6
        self.addListCommandExecution(commandString)


    def generateGnomInputFile(self):
        xsExperimentalDataQ = self.getDataInput().getExperimentalDataQ()
        xsExperimentalDataValues = self.getDataInput().getExperimentalDataValues()
        xsExperimentalDataStdDev = None
        if self.getDataInput().getExperimentalDataStdDev() is not None:
            xsExperimentalDataStdDev = self.getDataInput().getExperimentalDataStdDev()

        strLines = 'Gnom data file\n'
        for i, dataQ in enumerate(xsExperimentalDataQ):
            if xsExperimentalDataStdDev:
                strStdDev = str(xsExperimentalDataStdDev[i].getValue())
            else:
                strStdDev = ''
            strLines += ' '.join([str(dataQ.getValue()), str(xsExperimentalDataValues[i].getValue()), strStdDev]) + '\n'
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), "gnom_tmp.dat")
        EDUtilsFile.writeFile(tmpInputFileName, strLines)
        return tmpInputFileName

    def generateGnomConfigFile(self):
        tmpConfigFileName = os.path.join(self.getWorkingDirectory(), "gnom.cfg")

        strConfig = '\n'.join(['General configuration file', \
    'PRINTER C [ postscript       ]  Printer type', \
    'FORFAC  C [                  ]  Form factor file (valid for JOB=2)', \
    'EXPERT  C [     none         ]  File containing expert parameters', \
    'INPUT1  C [                  ]  Input file name (first file)', \
    'INPUT2  C [                  ]  Input file name (second file)', \
    'NSKIP1  I [                  ]  No of first points to skip', \
    'NSKIP2  I [                  ]  No of last  points to omit', \
    'OUTPUT  C [                  ]  Output file', \
    'ISCALE  C [                  ]  Angular scale (1\2\3\4)', \
    'PLOINP  C [       n          ]  Plotting flag: input data (Y\N)', \
    'PLORES  C [       n          ]  Plotting flag: results    (Y\N)', \
    'EVAERR  C [                  ]  Error flags: calculate errors   (Y\N)', \
    'PLOERR  C [       n          ]  Plotting flag: p(r) with errors (Y\N)', \
    'LKERN   C [                  ]  Kernel file status (Y\N)', \
    'JOBTYP  I [                  ]  Type of system (0\1\2\3\4\5\6)', \
    'RMIN    R [                  ]  Rmin for evaluating p(r)', \
    'RMAX    R [                  ]  Rmax for evaluating p(r)', \
    'LZRMIN  C [                  ]  Zero condition at r=rmin (Y\N)', \
    'LZRMAX  C [                  ]  Zero condition at r=rmax (Y\N)', \
    'KERNEL  C [                  ]  Kernel-storage file', \
    'DEVIAT  R [      0.0         ]  Default input errors level', \
    'IDET    I [                  ]  Experimental set up (0\1\2)', \
    'FWHM1   R [                  ]  FWHM for 1st run', \
    'FWHM2   R [                  ]  FWHM for 2nd run', \
    'AH1     R [                  ]  Slit-height parameter AH (first  run)', \
    'LH1     R [                  ]  Slit-height parameter LH (first  run)', \
    'AW1     R [                  ]  Slit-width  parameter AW (first  run)', \
    'LW1     R [                  ]  Slit-width  parameter LW (first  run)', \
    'AH2     R [                  ]  Slit-height parameter AH (second run)', \
    'LH2     R [                  ]  Slit-height parameter LH (second run)', \
    'AW2     R [                  ]  Slit-width  parameter AW (second run)', \
    'LW2     R [                  ]  Slit-width  parameter LW (second run)', \
    'SPOT1   C [                  ]  Beam profile file (first run)', \
    'SPOT2   C [                  ]  Beam profile file (second run)', \
    'ALPHA   R [      0.0         ]  Initial ALPHA', \
    'NREAL   R [       0          ]  Number of points in real space', \
    'COEF    R [                  ]', \
    'RAD56   R [                  ]  Radius\thickness (valid for JOB=5,6)', \
    'NEXTJOB C [                  ]'])

        EDUtilsFile.writeFile(tmpConfigFileName, strConfig)

    def parseRadiusOfGyration(self, logLine):
        return XSDataDouble(float(logLine.split()[4]))

    def parseFitQuality(self, logLine):
        return XSDataDouble(float(logLine.split()[3]))

    def parseScatteringFitData(self, idx_start, idx_stop, dataLines, tmpQ, tmpValues):
        for idx in range (idx_start, idx_stop):
            dataLine = dataLines[idx].split()
            tmpQ.append(XSDataDouble(float(dataLine[0])))
            tmpValues.append(XSDataDouble(float(dataLine[-1])))

    def parseDistributionData(self, idx_start, idx_stop, dataLines, tmpR, tmpPr, tmpErr):
        for idx in range (idx_start, idx_stop):
            dataLine = dataLines[idx].split()
            tmpR.append(XSDataDouble(float(dataLine[0])))
            tmpPr.append(XSDataDouble(float(dataLine[1])))
            tmpErr.append(XSDataDouble(float(dataLine[2])))


    def parseGnomOutputFile(self):
        logFile = EDUtilsFile.readFile(os.path.join(self.getWorkingDirectory(), "gnom.out"))
        logLines = logFile.splitlines()

        xsRadiusOfGyration = self.parseRadiusOfGyration(logLines[-1])
        #xsRadiusOfCrossSection = parseCrossSection(logFile)
        for idx, line in enumerate(logLines):
            if (line.find("Total  estimate") != -1):
                xsFitQuality = self.parseFitQuality(line)
            if (line.find("I REG") != -1):
                idx_start = idx + 2
            if (line.find("Distance distribution") != -1):
                idx_stop = idx - 1
            if (line.find("P(R)") != -1):
                idx_pr_start = idx + 2
            if (line.find("Reciprocal space:") != -1):
                idx_pr_stop = idx - 1


        xsScatteringFitQ = []
        xsScatteringFitValues = []
        self.parseScatteringFitData(idx_start, idx_stop, logLines, xsScatteringFitQ, xsScatteringFitValues)

        xsDistributionR = []
        xsDistributionPr = []
        xsDistributionErr = []
        self.parseDistributionData(idx_pr_start, idx_pr_stop, logLines, \
                                   xsDistributionR, xsDistributionPr, xsDistributionErr)

        xsDataResult = XSDataResultGnom()
        xsDataResult.setFitQuality(xsFitQuality)
        xsDataResult.setRadiusOfGyration(xsRadiusOfGyration)
        #xsDataResult.setRadiusOfCrossSection(xsRadiusOfCrossSection)
        xsDataResult.setScatteringFitQ(xsScatteringFitQ)
        xsDataResult.setScatteringFitValues(xsScatteringFitValues)

        xsDataResult.setDistributionR(xsDistributionR)
        xsDataResult.setDistributionPr(xsDistributionPr)
        xsDataResult.setDistributionErr(xsDistributionErr)

        return xsDataResult

    def plotFittingResults(self):
        """
        Plot results of Rmax optimization procedure and best fit of the experimental data
        """
        _listFitQ = [tmp.getValue() for tmp in self.getDataOutput().getScatteringFitQ()]
        _listFitValues = [tmp.getValue() for tmp in self.getDataOutput().getScatteringFitValues()]
        _listExpQ = [tmp.getValue() for tmp in self.getDataInput().getExperimentalDataQ()]
        _listExpValues = [tmp.getValue() for tmp in self.getDataInput().getExperimentalDataValues()]

        #_listExpStdDev = None
        #if self.getDataInput().getExperimentalDataStdDev():
        #    _listExpStdDev = [tmp.getValue() for tmp in self.getDataInput().getExperimentalDataStdDev()]
        #if _listExpStdDev:
        #    pylab.errorbar(_listExpQ, _listExpValues, yerr=_listExpStdDev, linestyle='None', marker='o', markersize=1,  label="Experimental Data")
        #    pylab.gca().set_yscale("log", nonposy='clip')
        #else:         
        #    pylab.semilogy(_listExpQ, _listExpValues, linestyle='None', marker='o', markersize=5,  label="Experimental Data")

        pylab.semilogy(_listExpQ, _listExpValues, linestyle='None', marker='o', markersize=5, label="Experimental Data")
        pylab.semilogy(_listFitQ, _listFitValues, label="Fitting curve")
        pylab.xlabel('q')
        pylab.ylabel('I(q)')
        pylab.suptitle("RMax : %3.2f. Fit quality : %1.3f" % (self.getDataInput().getRMax().getValue(), self.getDataOutput().getFitQuality().getValue()))
        pylab.legend()
        pylab.savefig(os.path.join(self.getWorkingDirectory(), "gnomFittingResults.png"))
        pylab.clf()


    def generateExecutiveSummary(self, __edPlugin=None):
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Results of GNOM run:")
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Input value for RMax = %3.2f" % self.getDataInput().getRMax().getValue())
        self.addExecutiveSummaryLine("Estimated Rg = %3.2f" % self.getDataOutput().getRadiusOfGyration().getValue())
        self.addExecutiveSummaryLine("Output fit quality : %1.3f" % self.getDataOutput().getFitQuality().getValue())
        self.addExecutiveSummaryLine("GNOM output file : %s" % os.path.join(self.getWorkingDirectory(), "gnom.out"))
        self.addExecutiveSummarySeparator()

        gnomLog = open(os.path.join(self.getWorkingDirectory(), "gnom.out"))
        for line in gnomLog:
            self.addExecutiveSummaryLine(line)





