#
#    Project: EdnaSaxs/Atsas
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

import os, itertools, math
from math import pi, cos, sin

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataEdnaSaxs import XSDataInputSupcomb, XSDataResultSupcomb
from XSDataCommon import XSDataString, XSDataFile, XSDataDouble, XSDataRotation, XSDataVectorDouble
from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("EDPDBFilter")
from EDPDBFilter import EDPDBFilter

class EDPluginExecSupcombv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for ab-initio model determination using Supcomb
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSupcomb)

        self.__bEnantiomorphs = True
        self.__bBackbone = False

        self.__strOutputFileNameRaw = 'result_raw.pdb'
        self.__strOutputFileName = 'result.pdb'
        self.__fNSD = None
        self.__vecRot = None
        self.__vecTrns = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getTemplateFile(), "No template file specified")
        self.checkMandatoryParameters(self.getDataInput().getSuperimposeFile(), "No superimpose file specified")

        self.checkSupcombEnantiomorphsInput()
        self.checkSupcombBackboneInput()

    def checkSupcombEnantiomorphsInput(self):
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.checkEnantiomorphs")
        try:
            if self.getDataInput().getEnantiomorphs().getValue():
                self.__bEnantiomorphs = self.getDataInput().getEnantiomorphs().getValue()
        except Exception:
            EDVerbose.WARNING("Enabling enantiomorphs in Supcomb by default")

    def checkSupcombBackboneInput(self):
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.checkBackbone")
        try:
            if self.getDataInput().getBackbone().getValue():
                self.__bBackbone = self.getDataInput().getBackbone().getValue()
        except Exception:
            EDVerbose.WARNING("Using all atoms in Supcomb by default")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.preProcess")
        self.generateSupcombScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSupcombv0_1.postProcess")

        self.setDataOutput(self.parseSupcombOutputFile())

    def generateSupcombScript(self):
        EDVerbose.DEBUG("*** EDPluginExecSupcombv0_1.generateSupcombScript")

        self.setScriptCommandline("")

        _tmpTemplateFileName = self.getDataInput().getTemplateFile().getPath().getValue()
        _tmpSuperimposeFileName = self.getDataInput().getSuperimposeFile().getPath().getValue()
        if self.__bBackbone:
            _tmpBackbone = '1'
        else:
            _tmpBackbone = ''
        if not self.__bEnantiomorphs:
            _tmpEnantiomorphs = 'No'
        else:
            _tmpEnantiomorphs = ''
        os.symlink(_tmpTemplateFileName, os.path.join(self.getWorkingDirectory(), "template.pdb"))
        os.symlink(_tmpSuperimposeFileName, os.path.join(self.getWorkingDirectory(), "supimpose.pdb"))

        commandLine = ['template.pdb', _tmpBackbone, \
                       'supimpose.pdb', _tmpEnantiomorphs, \
                       self.__strOutputFileNameRaw]

        self.addListCommandExecution('\n'.join(commandLine))


    def returnRotation(self, logLines):

        _psi = pi * float(logLines[0].split()[-1]) / 180.0
        _theta = pi * float(logLines[1].split()[-1]) / 180.0
        _phi = pi * float(logLines[2].split()[-1]) / 180.0

        q = [cos(_phi / 2) * cos(_theta / 2) * cos(_psi / 2) + sin(_phi / 2) * sin(_theta / 2) * sin(_psi / 2), \
             sin(_phi / 2) * cos(_theta / 2) * cos(_psi / 2) - cos(_phi / 2) * sin(_theta / 2) * sin(_psi / 2), \
             cos(_phi / 2) * sin(_theta / 2) * cos(_psi / 2) + sin(_phi / 2) * cos(_theta / 2) * sin(_psi / 2), \
             cos(_phi / 2) * cos(_theta / 2) * sin(_psi / 2) - sin(_phi / 2) * sin(_theta / 2) * cos(_psi / 2)]

        return XSDataRotation(q[0], q[1], q[2], q[3])


    def returnTranslation(self, logLines):

        _vecTmp = []
        for line in logLines:
            _vecTmp.append(float(line.split()[-1]))

        return XSDataVectorDouble(_vecTmp[0], _vecTmp[1], _vecTmp[2])


    def parseSupcombOutputFile(self):

        logFile = self.readProcessLogFile()
        logLines = logFile.splitlines()

        xsRot = self.returnRotation(logLines[-3:])
        xsTrns = self.returnTranslation(logLines[-6:-3])
        xsNSD = XSDataDouble(float(logLines[-8].split()[-1]))

        xsDataResult = XSDataResultSupcomb()
        xsDataResult.setNSD(xsNSD)
        xsDataResult.setRot(xsRot)
        xsDataResult.setTrns(xsTrns)

        EDPDBFilter.filterPDBFile(os.path.join(self.getWorkingDirectory(), self.__strOutputFileNameRaw), \
                                 os.path.join(self.getWorkingDirectory(), self.__strOutputFileName))

        pathOutputFile = XSDataString(os.path.join(self.getWorkingDirectory(), self.__strOutputFileName))
        xsDataResult.setOutputFilename(XSDataFile(pathOutputFile))

        return xsDataResult

    def generateExecutiveSummary(self, __edPlugin=None):
            self.addExecutiveSummaryLine(self.readProcessLogFile())
