# coding: utf8
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, numpy

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsArray import EDUtilsArray

from XSDataCommon import XSDataDouble

from XSDataReadDataID24v1_0 import XSDataInputReadDataID24
from XSDataReadDataID24v1_0 import XSDataEnergyCalibration

class EDTestCasePluginUnitExecReadDataID24v1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Control plugin Dexafsv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecReadDataID24v1_0")
              
    def preProcess(self):
        """
        Download reference file
        """
        EDTestCasePluginUnit.preProcess(self)
        self.loadTestImage(["data_debora.dat"])


    def testCheckParameters(self):
        strPath = os.path.join(self.getPluginTestsDataHome(), "XSDataInputReadDataID24_debora.xml")
        xsDataInputReadDataID24 = XSDataInputReadDataID24.parseFile(strPath)
        edPluginExecReadDataID24 = self.createPlugin()
        edPluginExecReadDataID24.setDataInput(xsDataInputReadDataID24)
        edPluginExecReadDataID24.checkParameters()
        
    def testLoadInputData(self):
        strPath = os.path.join(self.getTestsDataImagesHome(), "data_debora.dat")
        edPluginExecReadDataID24 = self.createPlugin()
        numpyArray = edPluginExecReadDataID24.loadInputData(strPath)
#        print numpyArray.shape
#        print numpyArray
        
    def testCreateEnergyCalibrationArray(self):
        xsDataEnergyCalibration = XSDataEnergyCalibration()
        xsDataEnergyCalibration.a = XSDataDouble(1.0e0)
        xsDataEnergyCalibration.b = XSDataDouble(1.0e-1)
        xsDataEnergyCalibration.c = XSDataDouble(1.0e-2)
        xsDataEnergyCalibration.d = XSDataDouble(1.0e-3)
        edPluginExecReadDataID24 = self.createPlugin()
        numpyArray = edPluginExecReadDataID24.createEnergyCalibrationArray(100, xsDataEnergyCalibration)
#        print numpyArray
        
    
    def process(self):
        self.addTestMethod(self.testCheckParameters)
        self.addTestMethod(self.testLoadInputData)
        self.addTestMethod(self.testCreateEnergyCalibrationArray)

    

if __name__ == '__main__':

    edTestCasePluginUnitExecReadDataID24v1_0 = EDTestCasePluginUnitExecReadDataID24v1_0("EDTestCasePluginUnitExecReadDataID24v1_0")
    edTestCasePluginUnitExecReadDataID24v1_0.execute()
