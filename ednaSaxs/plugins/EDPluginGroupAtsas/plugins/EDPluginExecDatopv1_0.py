# coding: utf8
#
#    Project: EdnaSaxs/Atsas
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF Grenoble
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
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF Grenoble"

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataEdnaSaxs import XSDataInputDatop, XSDataResultDatop


class EDPluginExecDatopv1_0(EDPluginExecProcessScript):
    """
    Plugin that simply performs an operation on a (couple of) curves. 
    operations can be  ADD, SUB, MUL, DIV 
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDatop)
        self.strOperation = None
        self.lstInputFiles = []
        self.outputFile = None
        self.const = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDatopv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputCurve, "No input Curve file provided")
        self.checkMandatoryParameters(self.dataInput.outputCurve, "No output Curve file is provided")
        self.checkMandatoryParameters(self.dataInput.operation, "No arithmetic operation provided ")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecDatopv1_0.preProcess")
        self.outputFile = self.dataInput.outputCurve.path.value
        self.strOperation = self.dataInput.operation.value.replace("+", "ADD").replace("-", "SUB").replace("*", "MUL").replace("/", "DIV")
        self.lstInputFiles = [ i.path.value for i in  self.dataInput.inputCurve]
        if self.dataInput.constant is not None:
            self.const = self.dataInput.constant.value
        self.generateCommandLineOptions()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecDatopv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultDatop(outputCurve=self.dataInput.outputCurve)
        self.setDataOutput(xsDataResult)

    def generateCommandLineOptions(self):
        if self.const :
            strCommandLine = "--output='%s' %s '%s' '%s'" % (self.outputFile, self.strOperation, self.lstInputFiles[0], self.const)
        else:
            strCommandLine = "--output='%s' %s " % (self.outputFile, self.strOperation) + " ".join(["'%s'" % i for i in self.lstInputFiles])
        self.setScriptCommandline(strCommandLine)
