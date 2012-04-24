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

from XSDataSAS import XSDataInputDamaver
from XSDataSAS import XSDataResultDamaver

from XSDataSAS import XSDataString, XSDataFile, XSDataDouble

class EDPluginExecDamaverv0_1(EDPluginExecProcessScript):
    """
    Execution plugin running DAMAVER pipeline for alignment of input pdb models,
    selecting the most typical one and building an averaged model  
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDamaver)

        self.__xsDataResult = XSDataResultDamaver()

        self.__strSymmetry = ''
        self.__bAutomatic = True

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDamaverv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getPdbInputFiles(), "PDB input files are missing")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamaverv0_1.preProcess")

        self.checkDamaverPath()
        self.checkDamaverAutomaticInput()
        self.checkDamaverSymmetryInput()
        self.generateDamaverScript()

    def checkDamaverPath(self):
        if '.' in self.getScriptExecutable():
            EDVerbose.WARNING('Damaver might not run properly when \'.\' is present in the path to launch it')

    def checkDamaverAutomaticInput(self):
        try:
            if self.getDataInput().getAutomatic():
                self.__bAutomatic = self.getDataInput().getAutomatic().getValue()
        except Exception:
            EDVerbose.WARNING("Running Damaver automation pipeline by default.")
        
    def checkDamaverSymmetryInput(self):
        EDVerbose.DEBUG("EDPluginExecDammifv0_1.checkDammifSymmetryInput")

        knownSymmetry = []
        knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i), range(1, 20)))
        knownSymmetry.extend(itertools.imap(lambda i: 'P' + str(i) + '2', range(2, 13)))

        try:
            if self.getDataInput().getSymmetry().getValue() in knownSymmetry:
                self.__strSymmetry = self.getDataInput().getSymmetry().getValue()
        except Exception:
            EDVerbose.WARNING("Symmetry wasn't specified. Setting symmetry to P1")


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDamaverv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamaverv0_1.postProcess")
        # Create some output data
        xsDataResult = XSDataResultDamaver()
        self.setDataOutput(xsDataResult)

        self.outputDamaverPdbFiles()
        if self.__bAutomatic:
            self.parseDamselLog()

        self.setDataOutput(self.__xsDataResult)

    def outputDamaverPdbFiles(self):
        pathDamaverFile = XSDataString(os.path.join(self.getWorkingDirectory(), "damaver.pdb"))
        xsDamaverFile = XSDataFile(pathDamaverFile)
        if os.path.exists(pathDamaverFile.getValue()):
            self.__xsDataResult.setDamaverPdbFile(xsDamaverFile)
        
        if self.__bAutomatic:
            pathDamfilterFile = XSDataString(os.path.join(self.getWorkingDirectory(), "damfilt.pdb"))
            pathDamstartFile = XSDataString(os.path.join(self.getWorkingDirectory(), "damstart.pdb"))
            xsDamfilterFile = XSDataFile(pathDamfilterFile)
            xsDamstartFile = XSDataFile(pathDamstartFile)

            if os.path.exists(pathDamfilterFile.getValue()):
                self.__xsDataResult.setDamfilterPdbFile(xsDamfilterFile)
            if os.path.exists(pathDamstartFile.getValue()):
                self.__xsDataResult.setDamstartPdbFile(xsDamstartFile)

    def parseDamselLog(self):
        damselLog = open(os.path.join(self.getWorkingDirectory(), "damsel.log"))

        for line in damselLog:
            wordsLine = [tmpStr for tmpStr in line.split(' ') if tmpStr is not '']
            if wordsLine[:4] == ['Mean', 'value', 'of', 'NSD']:
                self.__xsDataResult.setMeanNSD(XSDataDouble(float(wordsLine[-1])))
            if wordsLine[:3] == ['Variation', 'of', 'NSD']:
                self.__xsDataResult.setVariationNSD(XSDataDouble(float(wordsLine[-1])))



    def generateDamaverScript(self):
        EDVerbose.DEBUG("*** EDPluginExecDammifv0_1.generateDammifScript")

        dataFileNames = []
        for idx, pdbInputFile in enumerate(self.getDataInput().getPdbInputFiles()):
            tmpInputFileName = pdbInputFile.getPath().getValue()
            os.symlink(tmpInputFileName, os.path.join(self.getWorkingDirectory(), 'dammif-' + str(idx + 1) + '.pdb'))
            dataFileNames.append('dammif-' + str(idx + 1) + '.pdb')
            
        if self.__bAutomatic:
            commandScriptLine = ['/a', self.__strSymmetry]
        else:
            damsupLog = open(os.path.join(self.getWorkingDirectory(), "damsup.log"), 'w')
            damsupLog.write('\n'.join(dataFileNames))
            damsupLog.close()
            commandScriptLine = ['damsup.log']
            
        self.setScriptCommandline(' '.join(commandScriptLine))
        
    def generateExecutiveSummary(self,__edPlugin=None):
        self.addExecutiveSummaryLine("Results of model averaging using DAMAVER pipeline")
        self.addExecutiveSummarySeparator()
        self.addExecutiveSummaryLine("DAMAVER output pdb model : %s" % os.path.join(self.getWorkingDirectory(), "damaver.pdb"))
        
        if self.__bAutomatic:
            self.addExecutiveSummaryLine("DAMFILT output pdb model : %s" % os.path.join(self.getWorkingDirectory(), "damfilt.pdb"))
            self.addExecutiveSummaryLine("DAMSTART output pdb model : %s" % os.path.join(self.getWorkingDirectory(), "damstart.pdb"))
            damselLog = open(os.path.join(self.getWorkingDirectory(), "damsel.log"))
            for line in damselLog:
                self.addExecutiveSummaryLine(line)
                
        self.addExecutiveSummarySeparator()
        
