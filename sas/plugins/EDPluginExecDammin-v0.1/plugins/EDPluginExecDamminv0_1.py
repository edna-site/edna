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

from XSDataSAS import XSDataInputDammin
from XSDataSAS import XSDataResultDammin

from XSDataSAS import XSDataString, XSDataFile, XSDataDouble


class EDPluginExecDamminv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for ab-initio model determination using DAMMIN
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDammin)

        self.__strMode = 'F'
        self.__strProjectDesc = ''
        self.__strAngleUnit = ''
        self.__strCurveFit = ''
        self.__strDAM = ''
        self.__strSymmetry = 'P1'
        self.__strParticleShape = ''

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDamminv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getGnomOutputFile(), "No GNOM output file specified")

        self.checkDamminMode()
        self.checkDamminDAMInput()
        self.checkDamminSymmetryInput()        # TODO: Only using P1 because of input discrepancy for higher symmetries 
        self.checkParticleShapeInput()


    def checkDamminMode(self):
        try:
            if self.getDataInput().getMode().getValue().upper() in ['FAST', 'SLOW']:
                self.__strMode = self.getDataInput().getMode().getValue().upper()[0]
        except Exception:
            EDVerbose.WARNING("Running DAMMIN in FAST mode by default")

    def checkDamminSymmetryInput(self):
        knownSymmetry = []
        knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i), range(1, 20)))
        knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i) + '2', range(2, 13)))
        knownSymmetry.extend(['P23', 'P432', 'PICO'])

        # TODO: Some combinations of symmetry and dummy atom models
        #       are incompatible and DAMMIN will reset the dummy atom model.
        #       This should be accounted for to provide proper command input sequence

        try:
            if self.getDataInput().getSymmetry().getValue() in knownSymmetry:
                self.__strSymmetry = self.getDataInput().getSymmetry().getValue()
        except Exception:
            EDVerbose.WARNING("Symmetry wasn't specified. Setting symmetry to P1")

    def checkDamminDAMInput(self):
        DAMModel = ['S', 'E', 'C', 'P']
        try:
            if self.getDataInput().getInitialDummyAtomModel().getValue() in range(4):
                self.__strDAM = DAMModel[self.getDataInput().getInitialDummyAtomModel().getValue()]
                return
        except Exception:
            EDVerbose.WARNING("No standard dummy atom model selected. Looking for a PDB mode file")
        else:
            try:
                tmpInputFileName = self.getDataInput().getPdbInputFile().getPath().getValue()
                os.symlink(tmpInputFileName, os.path.join(self.getWorkingDirectory(), "input.pdb"))
                self.__strDAM = 'input.pdb'
            except Exception:
                EDVerbose.WARNING("Dummy atom model PDB file not specified. Using default model")


        #if self.getDataInput().getInitialDummyAtomModel() is not None:
        #    if self.getDataInput().getInitialDummyAtomModel().getValue() not in range(5):
        #        EDVerbose.ERROR("Unknown dummy atom model index specified")
        #        self.setFailure()
        #    else:
        #        if self.getDataInput().getInitialDummyAtomModel().getValue() == 4:
        #            if self.getDataInput().getPdbInputFile() is None:
        #                EDVerbose.ERROR("No PDB file for dummy atom model specified")
        #                self.setFailure()

    def checkParticleShapeInput(self):
        particleShape = ['P', 'O', 'U']
        try:
            if self.getDataInput().getExpectedParticleShape().getValue() in range(3):
                self.__strParticleShape = particleShape[self.getDataInput().getExpectedParticleShape().getValue()]
        except Exception:
            EDVerbose.ERROR("Using Unknown particle shape")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamminv0_1.preProcess")
        self.generateDamminScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDamminv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamminv0_1.postProcess")
        # Create some output data

        pathLogFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammin.log"))
        pathFitFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammin.fit"))
        pathMoleculeFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammin-1.pdb"))
        pathSolventFile = XSDataString(os.path.join(self.getWorkingDirectory(), "dammin-0.pdb"))

        xsLogFile = XSDataFile(pathLogFile)
        xsFitFile = XSDataFile(pathFitFile)
        xsMoleculeFile = XSDataFile(pathMoleculeFile)
        xsSolventFile = XSDataFile(pathSolventFile)

        xsDataResult = XSDataResultDammin()
        if os.path.exists(pathLogFile.getValue()):
            xsDataResult.setLogFile(xsLogFile)
        if os.path.exists(pathFitFile.getValue()):
            xsDataResult.setFitFile(xsFitFile)
        if os.path.exists(pathMoleculeFile.getValue()):
            xsDataResult.setPdbMoleculeFile(xsMoleculeFile)
        if os.path.exists(pathSolventFile.getValue()):
            xsDataResult.setPdbSolventFile(xsSolventFile)

        xsDataResult.setChiSqrt(self.returnDamminChiSqrt())
        xsDataResult.setRfactor(self.returnDamminRFactor())

        self.setDataOutput(xsDataResult)

#    def generateDamminScript(self):
#        EDVerbose.DEBUG("*** EDPluginExecDamminv0_1.generateDamminScript")
#
#        tmpInputFileName = self.getDataInput().getGnomOutputFile().getPath().getValue()
#        os.symlink(tmpInputFileName, os.path.join(self.getWorkingDirectory(), "dammin.out"))
#        commandLine = "dammin.out /mo Fast"
#        self.setScriptCommandline(commandLine)

    def generateDamminScript(self):
        EDVerbose.DEBUG("*** EDPluginExecDamminv0_1.generateDamminScript_v2")

        # Dammin doesn't accept file names longer than 64 characters.
        # Using symlink to work around this issue
        tmpInputFileName = self.getDataInput().getGnomOutputFile().getPath().getValue()
        os.symlink(tmpInputFileName, os.path.join(self.getWorkingDirectory(), "dammin.out"))

        self.setScriptCommandline("")

        commandString = [self.__strMode, 'dammin.log', 'dammin.out', \
                         self.__strProjectDesc,
                         self.__strAngleUnit,
                         self.__strCurveFit, \
                         self.__strDAM, \
                         self.__strSymmetry]

        if self.__strDAM not in ['', 'S']:
            commandString.extend(self.returnModelDimensions())

        commandString.extend(self.__strParticleShape)
        commandString.extend(5 * [''])                  # Just in case there are more default settings

        self.addListCommandExecution('\n'.join(commandString))


    def returnModelDimensions(self):
        # TODO: For some symmetry groups DAMMIN asks for less dimensions 
        if self.getDataInput().getInitialDummyAtomModel().getValue() in range(1, 4):
            return 3 * ['']
        if self.getDataInput().getInitialDummyAtomModel().getValue() is 4:
            return ['']
        else:
            return ''


    def returnDamminChiSqrt(self):
        logFile = open(os.path.join(self.getWorkingDirectory(), "dammin.fir"))
        return XSDataDouble(float(logFile.readline().split(' ')[-1]))

    def returnDamminRFactor(self):
        logFile = open(os.path.join(self.getWorkingDirectory(), "dammin.log"))

        tmpRfactor = None

        for line in logFile:
            wordsLine = [tmpStr for tmpStr in line.split(' ') if tmpStr is not '']
            if wordsLine[0] == "Rf:":
                tmpRfactor = float(wordsLine[1])

        return XSDataDouble(tmpRfactor)
