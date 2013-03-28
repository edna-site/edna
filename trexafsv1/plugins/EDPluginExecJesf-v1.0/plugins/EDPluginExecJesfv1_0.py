# coding: utf8
#
#    Project: Time-Resolved EXAFS
#             http://www.edna-site.org
#
#    Project: Time-Resolved EXAFS
#             http://www.edna-site.org
#
#    Copyright (C)      2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__author__="<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"

import os, numpy

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsArray import EDUtilsArray

from XSDataCommon import XSDataDouble

from XSDataJesfv1_0 import XSDataInputJesf
from XSDataJesfv1_0 import XSDataResultJesf

class EDPluginExecJesfv1_0(EDPluginExecProcessScript):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__(self ):
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputJesf)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecJesfv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Plugin input is None")
        self.checkMandatoryParameters(self.dataInput.data, "Data is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecJesfv1_0.preProcess")
        numpyData = EDUtilsArray.xsDataToArray(self.dataInput.data)
        numpy.savetxt(os.path.join(self.getWorkingDirectory(), "spectra.dat"), numpyData)
        self.addListCommandExecution("spectra.dat")

        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecJesfv1_0.postProcess")
        # Create some output data
        xsDataResultJesf = self.readJesfResults()
        self.setDataOutput(xsDataResultJesf)
    
    def readJesfResults(self):
        xsDataResultJesf = XSDataResultJesf()
        strWorkDir = self.getWorkingDirectory()
        # Read log file
        strLog = self.readProcessLogFile()
        listLogLines = strLog.split("\n")
        for strLogLine in listLogLines:
            if strLogLine.startswith(" MATRICE SINGOLARE!!!!!"):
                strErrorMessage = "Jesf reports singular matrix!"
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                break
            if strLogLine.startswith(" EDGE="):
                fEdge = float(strLogLine.split("=")[1])
                xsDataResultJesf.edge = XSDataDouble(fEdge)
            elif strLogLine.startswith(" SLOPE="):
                fSlope = float(strLogLine.split("=")[1])
                xsDataResultJesf.slope = XSDataDouble(fSlope)
            elif strLogLine.startswith(" JUMP="):
                fJump = float(strLogLine.split("=")[1])
                xsDataResultJesf.jump = XSDataDouble(fJump)
            elif strLogLine.startswith(" EWL="):
                fEWL = float(strLogLine.split("=")[1])
                xsDataResultJesf.ewl = XSDataDouble(fEWL)
            elif strLogLine.startswith(" hwl="):
                fHwl = float(strLogLine.split("=")[1])
                xsDataResultJesf.hwl = XSDataDouble(fHwl)
        if not self.isFailure():
            # Read fort92
            numpyFort92 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.92"))
            xsDataArrayFort92 = EDUtilsArray.arrayToXSData(numpyFort92)
            xsDataResultJesf.setFort92(xsDataArrayFort92)
            # Read fort95
            numpyFort95 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.95"))
            xsDataArrayFort95 = EDUtilsArray.arrayToXSData(numpyFort95)
            xsDataResultJesf.setFort92(xsDataArrayFort95)
            # Read fort96
            numpyFort96 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.96"))
            xsDataArrayFort96 = EDUtilsArray.arrayToXSData(numpyFort96)
            xsDataResultJesf.setFort96(xsDataArrayFort96)
            # Read fort97
            numpyFort97 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.97"))
            xsDataArrayFort97 = EDUtilsArray.arrayToXSData(numpyFort97)
            xsDataResultJesf.setFort97(xsDataArrayFort97)
            # Read fort98
            numpyFort98 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.98"))
            xsDataArrayFort98 = EDUtilsArray.arrayToXSData(numpyFort98)
            xsDataResultJesf.setFort98(xsDataArrayFort98)
            # Read fort99
            numpyFort99 = numpy.genfromtxt(os.path.join(strWorkDir,"fort.99"))
            xsDataArrayFort99 = EDUtilsArray.arrayToXSData(numpyFort99)
            xsDataResultJesf.setFort99(xsDataArrayFort99)
        return xsDataResultJesf
        
