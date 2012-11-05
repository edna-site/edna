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
__date__ = "2012-08-30"
__status__ = "Development"

import os
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataEdnaSaxs import XSDataInputDatGnom, XSDataResultDatGnom, XSDataGnom
from XSDataCommon import XSDataString, XSDataDouble, XSDataFile, XSDataLength

class EDPluginExecDatGnomv1_0(EDPluginExecProcessScript):
    """
    Plugin that simply runs datgnom; a clever version of gnom; on a 1D curve.  
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDatGnom)
        self.datFile = None
        self.outFile = None
        self.Rg = None
        self.skip = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDatGnomv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputCurve, "No input Curve file provided")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecDatGnomv1_0.preProcess")
        self.datFile = self.dataInput.inputCurve.path.value
        if self.dataInput.output is not None:
            self.outFile = self.dataInput.output.path.value
        else:
            self.outFile = os.path.join(self.getWorkingDirectory(), os.path.splitext(os.path.basename(self.datFile)))
        if self.dataInput.rg is not None:
            self.rg = self.dataInput.rg.value
        if self.dataInput.skip is not None:
            self.skip = self.dataInput.skip.value

        self.generateCommandLineOptions()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecDatGnomv1_0.postProcess")
        # Create some output data
        if not os.path.isfile(self.outFile):
            self.error("EDPluginExecDatGnomv1_0 did not produce output file %s as expected !" % self.outFile)
            self.setFailure()


        gnom = XSDataGnom(gnomFile=XSDataFile(XSDataString(self.outFile)))
        logfile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        out = open(logfile, "r").read().split()
        for key, val, typ in (("Dmax", "dmax", XSDataLength),
                            ("Guinier", "rgGuinier", XSDataLength),
                            ("Gnom", "rgGnom", XSDataLength),
                            ("Total", "total", XSDataDouble)):
            idx = out.index(key)
            if idx == -1:
                self.error("No key %s in file %s" % (key, logfile))
                self.setFailure()
            res = out[idx + 2]
            gnom.__setattr__(val, typ(float(res)))
        self.dataOutput = XSDataResultDatGnom(gnom=gnom)

    def generateCommandLineOptions(self):
        lstArg = [self.datFile, "-o", self.outFile]
        if self.rg:
            lstArg += ["-r", str(self.rg)]
        if self.skip and self.skip > 0:
            lstArg += ["-s", str(self.skip)]
        self.setScriptCommandline(" ".join(lstArg))
