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

import os, itertools

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataSAS import XSDataInputDammif
from XSDataSAS import XSDataResultDammif

from XSDataSAS import XSDataString, XSDataFile, XSDataDouble


class EDPluginExecDammifv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for ab-initio model determination using DAMMIF
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDammif)

        self.__strMode = 'fast'
        self.__strUnit = 'ANGSTROM'
        self.__strSymmetry = 'P1'
        self.__strParticleShape = 'UNKNOWN'
        self.__strConstant = ''
        self.__strChained = ''

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getGnomOutputFile(), "No GNOM output file specified")

        self.checkDammifModeInput()
        self.checkDammifUnitInput()
        self.checkDammifSymmetryInput()
        self.checkDammifParticleShapeInput()
        self.checkDammifConstant()
        self.checkDammifChained()

    def checkDammifModeInput(self):
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.checkDammifMode")
        try:
            if self.getDataInput().getMode().getValue().lower() in ['fast', 'slow']:
                self.__strMode = self.getDataInput().getMode().getValue().lower()
        except:
            EDVerbose.WARNING("Running DAMMIF in fast mode by default")

    def checkDammifUnitInput(self):
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.checkDammifUnit")
        try:
            if self.getDataInput().getUnit().getValue().lower() in ['angstrom', 'nanometer']:
                self.__strUnit = self.getDataInput().getUnit().getValue().upper()
        except:
            EDVerbose.WARNING("Using A-1 units for q-axis values by default")

    def checkDammifSymmetryInput(self):
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.checkDammifSymmetryInput")
        _knownSymmetry = []
        # Should be able to go up to P19, but DAMMIF only seems to work for symmetries up to P12 
        _knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i), range(1, 13)))
        _knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i) + '2', range(2, 13)))

        try:
            if self.getDataInput().getSymmetry().getValue() in _knownSymmetry:
                self.__strSymmetry = self.getDataInput().getSymmetry().getValue()
        except:
            EDVerbose.WARNING("Symmetry wasn't specified. Setting symmetry to P1")

    def checkDammifParticleShapeInput(self):
        particleShape = ['PROLATE', 'OBLATE', 'UNKNOWN']
        try:
            if self.getDataInput().getExpectedParticleShape().getValue() in range(3):
                self.__strParticleShape = particleShape[self.getDataInput().getExpectedParticleShape().getValue()]
        except:
            EDVerbose.WARNING("Using Unknown particle shape")

    def checkDammifConstant(self):
        try:
            self.__strConstant = '--constant=' + str(self.getDataInput().getConstant().getValue())
        except:
            EDVerbose.WARNING("Constant to subtract will be defined automatically")

    def checkDammifChained(self):
        try:
            if self.getDataInput().getChained().getValue():
                self.__strChained = '--chained'
        except:
            EDVerbose.WARNING("Atoms in the output model are not chained")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.preProcess")
        #self.generateDammifScript_v2()
        self.generateDammifScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.postProcess")
        # Create some output data

        pathLogFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammif.log"))
        pathFitFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammif.fit"))
        pathMoleculeFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammif-1.pdb"))
        pathSolventFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammif-0.pdb"))

        xsLogFile = XSDataFile(pathLogFile)
        xsFitFile = XSDataFile(pathFitFile)
        xsMoleculeFile = XSDataFile(pathMoleculeFile)
        xsSolventFile = XSDataFile(pathSolventFile)

        xsDataResult = XSDataResultDammif()
        if os.path.exists(pathLogFile.getValue()):
            xsDataResult.setLogFile(xsLogFile)
        if os.path.exists(pathFitFile.getValue()):
            xsDataResult.setFitFile(xsFitFile)
        if os.path.exists(pathMoleculeFile.getValue()):
            xsDataResult.setPdbMoleculeFile(xsMoleculeFile)
        if os.path.exists(pathSolventFile.getValue()):
            xsDataResult.setPdbSolventFile(xsSolventFile)

        xsDataResult.setChiSqrt(self.returnDammifChiSqrt())
        xsDataResult.setRfactor(self.returnDammifRFactor())

        self.setDataOutput(xsDataResult)

    def generateDammifScript(self):
        EDVerbose.DEBUG("*** EDPluginExecDammifv0_1.generateDammifScript")

        # Dammif doesn't accept file names longer than 64 characters.
        # Using symlink to work around this issue
        tmpInputFileName = self.getDataInput().getGnomOutputFile().getPath().getValue()
        os.symlink(tmpInputFileName, os.path.join(self.getWorkingDirectory(), "dammif.out"))

        commandLine = ['--mode', self.__strMode, \
                       #'--unit', self.__strUnit, \
                       '--symmetry', self.__strSymmetry, \
                       '--anisometry', self.__strParticleShape, \
                       self.__strConstant, self.__strChained, 'dammif.out']

        self.setScriptCommandline(' '.join(commandLine))


    def returnDammifChiSqrt(self):
        logFile = open(os.path.join(self.getWorkingDirectory(), "dammif.fir"))
        return XSDataDouble(float(logFile.readline().split('=')[-1]))

    def returnDammifRFactor(self):
        logFile = open(os.path.join(self.getWorkingDirectory(), "dammif.log"))

        tmpRfactor = None

        for line in logFile:
            wordsLine = [tmpStr for tmpStr in line.split(' ') if tmpStr is not '']
            if wordsLine[0] == "Rf:":
                tmpRfactor = float(wordsLine[1][:-1])

        return XSDataDouble(tmpRfactor)

    def generateExecutiveSummary(self,__edPlugin=None):
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("Results of DAMMIF run:")
        self.addExecutiveSummarySeparator()
        tmpRFactor = "RFactor = %1.4f" % self.getDataOutput().getRfactor().getValue()
        tmpChiSqrt = "Chi(Sqrt) = %3.3f" % self.getDataOutput().getChiSqrt().getValue()
        tmpStrLine = "\t".join([tmpChiSqrt, tmpRFactor])
        self.addExecutiveSummaryLine(tmpStrLine)
        
        self.addExecutiveSummaryLine("DAMMIF fit file : %s" % os.path.join(self.getWorkingDirectory(), "dammif.fit"))
        self.addExecutiveSummaryLine("DAMMIF log file : %s" % os.path.join(self.getWorkingDirectory(), "dammif.log"))
        self.addExecutiveSummarySeparator()
        
        dammifLog = open(os.path.join(self.getWorkingDirectory(), "dammif.log"))
        for line in dammifLog:
            self.addExecutiveSummaryLine(line)
