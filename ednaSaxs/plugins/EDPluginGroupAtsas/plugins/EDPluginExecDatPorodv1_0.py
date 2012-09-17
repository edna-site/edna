# coding: utf8
#
#    Project: EdnaSaxs/Atsas
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012, ESRF Grenoble
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
__copyright__ = "2012, ESRF Grenoble"
__date__ = "2012-08-31"
__status__ = "Development"

import os
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataEdnaSaxs import XSDataInputDatPorod, XSDataResultDatPorod
from XSDataCommon import XSDataString, XSDataDouble, XSDataFile, XSDataLength, \
    XSDataDoubleWithUnit

class EDPluginExecDatPorodv1_0(EDPluginExecProcessScript):
    """
    Plugin that simply runs datporod on a gnom file to calculate the volume according to the porod formula:

    VP = 2π2I(0)/Q
    where
    Q = ∫s2[I(s) - K]ds
    where K is a constant determined to ensure the asymptotical intensity decay proportional to s-4 at higher angles
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDatPorod)
        self.gnomFile = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDatPorodv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.gnomFile, "No input Curve file provided")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecDatPorodv1_0.preProcess")
        self.gnomFile = self.dataInput.gnomFile.path.value
        self.generateCommandLineOptions()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecDatPorodv1_0.postProcess")
        # Create some output data
        logfile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        out = open(logfile, "r").read().split()
        try:
            res = float(out[0])
        except (ValueError, IndexError):
            self.error("Unable to read porod log file: " + logfile)
            self.setFailure()
        xsDataResult = XSDataResultDatPorod(volume=XSDataDoubleWithUnit(value=res))
        self.setDataOutput(xsDataResult)

    def generateCommandLineOptions(self):
        self.setScriptCommandline(self.gnomFile)
