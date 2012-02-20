# coding: utf8
#
#    Project: Solution Scattering
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 DLS
#                  2012 ESRF
#
#    Principal author:       irakli
#                            Jérôme Kieffer
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
from EDUtilsArray import EDUtilsArray

__authors__ = ["irakli", "Jérôme Kieffer"]
__license__ = "GPLv3+"
__copyright__ = "2011 DLS, 2012 ESRF"

import os
from StringIO import StringIO
from EDVerbose                 import EDVerbose
from EDUtilsFile               import EDUtilsFile
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataSAS                 import XSDataInputGnom, XSDataResultGnom
from XSDataCommon              import XSDataFile, XSDataString, XSDataDouble
from EDUtilsPlatform           import  EDUtilsPlatform
from EDUtilsPath               import EDUtilsPath
from EDFactoryPlugin import edFactoryPlugin as EDFactoryPluginStatic
architecture = EDUtilsPlatform.architecture
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
matplotlibPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "Matplotlib-1.0.1", architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
matplotlib = EDFactoryPluginStatic.preImport("matplotlib", matplotlibPath)
pyplot = EDFactoryPluginStatic.preImport("matplotlib.pyplot", matplotlibPath)

class EDPluginExecGnomv0_2(EDPluginExecProcessScript):
    """
    Execution plugin for small  angle scattering data processing using GNOM
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputGnom)
        self.fAngularScale = 1
        self.npaExperimentalDataQ = None
        self.npaExperimentalDataI = None
        self.npaExperimentalDataStdDev = None
        self.npaFitDataQ = None
        self.npaFitDataI = None
        self.npaR = None
        self.npaPR = None
        self.npaPRerr = None
        self.fRadiusOfGir = None
        self.fFitQuality = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecGnomv0_2.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecGnomv0_2.preProcess")
        if self.dataInput.angularScale is not None:
            self.fAngularScale = self.dataInput.angularScale.value
        dataInput = self.dataInput

        inputFile = None
        if len(dataInput.experimentalDataQ) > 0:
            self.npaExperimentalDataQ = numpy.array([i.value for i in dataInput.experimentalDataQ])
        elif dataInput.experimentalDataQArray is not None:
            self.npaExperimentalDataQ = EDUtilsArray.xsDataToArray(dataInput.experimentalDataQArray)
        elif dataInput.experimentalDataFile is not None:
            inputFile = dataInput.experimentalDataFile.path.value
        else:
            strErrorMessage = "EDPluginExecGnomv0_2: input parameter is missing: experimentalDataQ or experimentalDataQArray or experimentalDataFile"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage

        if len(dataInput.experimentalDataValues) > 0:
            self.npaExperimentalDataI = numpy.array([i.value for i in dataInput.experimentalDataValues])
        elif dataInput.experimentalDataIArray is not None:
            self.npaExperimentalDataI = EDUtilsArray.xsDataToArray(dataInput.experimentalDataIArray)
        elif dataInput.experimentalDataFile is not None:
            inputFile = dataInput.experimentalDataFile.path.value
        else:
            strErrorMessage = "EDPluginExecGnomv0_2: input parameter is missing: experimentalDataValues or experimentalDataIArray or experimentalDataFile"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage

        if len(dataInput.experimentalDataStdDev) > 0:
            self.npaExperimentalDataStdDev = numpy.array([i.value for i in dataInput.experimentalDataStdDev])
        elif dataInput.experimentalDataStdArray is not None:
            self.npaExperimentalDataStdDev = EDUtilsArray.getArray(dataInput.experimentalDataStdArray)

        if inputFile:
            self.loadDataFile(inputFile)

        self.generateGnomConfigFile()
        self.generateGnomScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginExecGnomv0_2.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecGnomv0_2.postProcess")
        # Create some output data
        self.parseGnomOutputFile()
        xsDataResult = XSDataResultGnom(radiusOfGyration=XSDataDouble(self.fRadiusOfGir),
                                        arrayErr=EDUtilsArray.arrayToXSData(self.npaPRerr),
                                        arrayPr=EDUtilsArray.arrayToXSData(self.npaPR),
                                        arrayR=EDUtilsArray.arrayToXSData(self.npaR),
                                        scatteringFitIArray=EDUtilsArray.arrayToXSData(self.npaFitDataI),
                                        scatteringFitQArray=EDUtilsArray.arrayToXSData(self.npaFitDataQ),
                                        output=XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), "gnom.out"))),
                                        fitQuality=XSDataDouble(self.fFitQuality))
        self.dataOutput = xsDataResult


    def generateGnomScript(self):
        self.DEBUG("*** EDPluginExecGnomv0_2.generateGnomScript")
        self.generateGnomInputFile()
        self.setScriptCommandline("")
        commandString = 'gnom_tmp.dat' + \
                        '\n' * 5 + str(self.fAngularScale) + \
                        '\n' * 5 + str(self.dataInput.rMax.value) + \
                        '\n' * 3 + 'No' + '\n' * 6
        self.addListCommandExecution(commandString)


    def generateGnomInputFile(self):
        if self.npaExperimentalDataStdDev is not None:
            data = numpy.vstack((self.npaExperimentalDataQ, self.npaExperimentalDataI, self.npaExperimentalDataStdDev)).T
        else:
            data = numpy.vstack((self.npaExperimentalDataQ, self.npaExperimentalDataI)).T
        tmpInputFileName = os.path.join(self.getWorkingDirectory(), "gnom_tmp.dat")
        with open(tmpInputFileName, "w") as datFile:
            datFile.write('Gnom data file' + os.linesep)
            numpy.savetxt(datFile, data)
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


    def parseGnomOutputFile(self):
        logFile = os.path.join(self.getWorkingDirectory(), "gnom.out")
        pr = StringIO("")
        reg = StringIO("")
        do_pr = False
        do_reg = False
        with open(logFile, "r") as logLines:
            for idx, line in enumerate(logLines):
                words = line.split()
                if "Total  estimate" in line:
                    self.fFitQuality = float(line.split()[3])
                if "Reciprocal space:" in line:
                    do_pr = False
                if "Distance distribution" in line :
                    do_reg = False
                if len(words) > 0:
                    if do_reg:
                        reg.write("%s %s\n" % (words[0], words[-1]))
                    if do_pr:
                        pr.write(line)
                if "I REG" in line:
                    do_reg = True
                if "P(R)" in line:
                    do_pr = True
        self.fRadiusOfGir = float(line.split()[4])
        reg.seek(0)
        pr.seek(0)
        self.npaFitDataQ, self.npaFitDataI = numpy.loadtxt(reg, unpack=True, dtype="float32")
        self.npaR, self.npaPR, self.npaPRerr = numpy.loadtxt(pr, unpack=True, dtype="float32")

    def plotFittingResults(self):
        """
        Plot results of Rmax optimization procedure and best fit of the experimental data
        """
        if self.npaFitDataQ is None:
            self.WARNING("Please execute the plugin before plotting data")
            return
        fig = matplotlib.pyplot.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.semilogy(self.npaExperimentalDataQ, self.npaExperimentalDataI, linestyle='None', marker='o', markersize=5, label="Experimental Data")
        ax.semilogy(self.npaFitDataQ, self.npaFitDataI, label="Fitting curve")
        ax.set_xlabel('q')
        ax.set_ylabel('I(q)')
        fig.suptitle("RMax : %3.2f. Fit quality : %1.3f" % (self.dataInput.rMax.value, self.dataOutput.fitQuality.value))
        ax.legend(*ax.get_legend_handles_labels())
        fig.savefig(os.path.join(self.getWorkingDirectory(), "gnomFittingResults.png"))
        fig.clf()
        del ax, fig


    def generateExecutiveSummary(self, __edPlugin=None):
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Results of GNOM run:")
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Input value for RMax = %3.2f" % self.dataInput.getRMax().getValue())
        self.addExecutiveSummaryLine("Estimated Rg = %3.2f" % self.dataOutput.getRadiusOfGyration().getValue())
        self.addExecutiveSummaryLine("Output fit quality : %1.3f" % self.dataOutput.getFitQuality().getValue())
        self.addExecutiveSummaryLine("GNOM output file : %s" % os.path.join(self.getWorkingDirectory(), "gnom.out"))
        self.addExecutiveSummarySeparator()

        gnomLog = open(os.path.join(self.getWorkingDirectory(), "gnom.out"))
        for line in gnomLog:
            self.addExecutiveSummaryLine(line)



    def loadDataFile(self, fileName):
        """
        load a Q/I(/std) ascii file
        """
        data = None
        if not os.path.isfile(fileName):
            strErrorMessage = "EDPluginExecGnomv0_2: experimentalDataFile: %s does not exist" % fileName
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        for i in range(5):
            try:
                data = numpy.loadtxt(fileName, skiprows=i)
            except:
                pass
            else:
                break
        if data is None:
            strErrorMessage = "EDPluginExecGnomv0_2: Unable to parse %s with numpy.loadtxt" % fileName
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        elif data.shape[1] == 3:
            self.npaExperimentalDataQ, self.npaExperimentalDataI, self.npaExperimentalDataStdDev = data.T
        elif data.shape[1] == 2:
            self.npaExperimentalDataQ, self.npaExperimentalDataI = data.T
        else:
            strErrorMessage = "EDPluginExecGnomv0_2: %s contains an numpy object of shape %s" % (fileName, data.shape)
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage


