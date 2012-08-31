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

import os

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataEdnaSaxs import XSDataInputDamstart
from XSDataEdnaSaxs import XSDataResultDamstart

from XSDataCommon import XSDataFile, XSDataString


class EDPluginExecDamstartv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for ab-initio model determination using Damstart
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDamstart)

        self.__strInputPdbFileName = 'input.pdb'
        self.__strOutputPdbFileName = 'damstart.pdb'

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDamstartv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputPdbFile(), "No template file specified")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamstartv0_1.preProcess")
        self.generateDamstartScript()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecDamstartv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDamstartv0_1.postProcess")

        xsDataResult = XSDataResultDamstart()

        pathOutputFile = XSDataString(os.path.join(self.getWorkingDirectory(), self.__strOutputPdbFileName))
        xsDataResult.setOutputPdbFile(XSDataFile(pathOutputFile))

        self.setDataOutput(xsDataResult)

    def generateDamstartScript(self):
        EDVerbose.DEBUG("*** EDPluginExecDamstartv0_1.generateDamstartScript")

        _tmpInputFileName = self.getDataInput().getInputPdbFile().getPath().getValue()
        os.symlink(_tmpInputFileName, os.path.join(self.getWorkingDirectory(), self.__strInputPdbFileName))

        self.setScriptCommandline("")
        commandString = 'input.pdb' + '\n' * 5
        self.addListCommandExecution(commandString)
        #self.setScriptCommandline(self.__strInputPdbFileName)

    def generateExecutiveSummary(self, __edPlugin=None):
            self.addExecutiveSummaryLine(self.readProcessLogFile())
