# coding: utf8
#
#    Project: EdnaSaxs/Atsas
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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
__contact__ = "Jérôme.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2011 ESRF, Grenoble"
__date__ = "2011-09-26"
__status__ = "Production"

import os
from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataEdnaSaxs")
from XSDataEdnaSaxs import XSDataInputDataver, XSDataResultDataver
from XSDataCommon import XSDataString, XSDataFile

class EDPluginExecDataverv1_0(EDPluginExecProcessScript):
    """
    Execution plugin that does the (basic) data averaging , part from Atsas package
    """

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDataver)
        self.strOutFile = None
        self.lstInFiles = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDataverv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputCurve, "No input curve filenames provided")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecDataverv1_0.preProcess")
        self.lstInFiles = [i.path.value for i in  self.dataInput.inputCurve]
        if self.dataInput.outputCurve is not None:
            self.strOutFile = self.dataInput.outputCurve.path.value
        self.generateCommandLine()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecDataverv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultDataver()
        xsDataResult.outputCurve = XSDataFile(XSDataString(self.strOutFile))
        self.setDataOutput(xsDataResult)

    def generateCommandLine(self):
        self.DEBUG("EDPluginExecDataverv1_0.generateCommandLine")
        if self.strOutFile is not None:
            self.setScriptCommandline("--output=%s " % self.strOutFile + " ".join(self.lstInFiles))
        else:
            self.setScriptCommandline(" ".join(self.lstInFiles))
            self.strOutFile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
