#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20121004"
__status__ = "beta"

import os

from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble

from XSDataRdfitv1_0 import XSDataInputRdfit
from XSDataRdfitv1_0 import XSDataResultRdfit

class EDTestCasePluginUnitRdfitv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginRdfitv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

        self.strDataPath = self.getPluginTestsDataHome()
        self.strObtainedInputFile = "XSDataInputRaddosev10.xml"
        self.strObtainedInputFile2 = "XSDataInputRaddosev10FromObject_02.xml"
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataRaddosev10Input_reference.xml")
        self.strReferenceInputFile2 = os.path.join(self.strDataPath, "XSDataRaddosev10Input_reference_02.xml")

        self.strReferenceScriptLogFileName = os.path.join(self.strDataPath, "edPluginRdfitv10.log")
        self.strReferenceScriptLogFileNamev2 = os.path.join(self.strDataPath, "edPluginRdfitv10_Raddosev2.log")


    def createTestDataInput(self):
        xsDataInputRdfit = XSDataInputRdfit()
        xsDataInputRdfit.setBestXmlFile(XSDataFile(XSDataString("1.xml")))
        xsDataInputRdfit.addXdsHklFile(XSDataFile(XSDataString("xds_1.hkl")))
        xsDataInputRdfit.addXdsHklFile(XSDataFile(XSDataString("xds_2.hkl")))
        xsDataInputRdfit.addXdsHklFile(XSDataFile(XSDataString("xds_3.hkl")))
        xsDataInputRdfit.addXdsHklFile(XSDataFile(XSDataString("xds_4.hkl")))
        xsDataInputRdfit.setDmin(XSDataDouble(1.0))
        xsDataInputRdfit.setDefaultBeta(XSDataDouble(2.0))
        xsDataInputRdfit.setDefaultGama(XSDataDouble(3.0))
        xsDataInputRdfit.setBFactorMtvplotFile(XSDataFile(XSDataString("2")))
        xsDataInputRdfit.setBScaleIntensityMtvPlotFile(XSDataFile(XSDataString("3")))
        xsDataInputRdfit.setBScaleIntensityGleFile(XSDataFile(XSDataString("4")))
        xsDataInputRdfit.setResultsFile(XSDataFile(XSDataString("5")))
        xsDataInputRdfit.setResultsXmlFile(XSDataFile(XSDataString("6")))
        return xsDataInputRdfit
    
    
    def testSetDataInput(self):
        edPluginRdfit = self.createPlugin()
        xsDataInputRdfit = self.createTestDataInput()
        edPluginRdfit.setDataInput(xsDataInputRdfit)
        edPluginRdfit.checkParameters()
        
    def testGenerateCommands(self):
        edPluginRdfit = self.createPlugin()
        xsDataInputRdfit = self.createTestDataInput()
        strCommandLine = edPluginRdfit.generateCommands(xsDataInputRdfit)
        strCommandLineReference = " -d 1.xml -dmin 1.000000 -beta 2.000000 -gama 3.000000 -gb 2 -glb 3 -glr 4 -result 5 -xml 6 xds_1.hkl xds_2.hkl xds_3.hkl xds_4.hkl"
        EDAssert.equal(strCommandLineReference, strCommandLine, "Command line")


    def testGetOutputDataFromDNATableFile(self):
        edPluginRdfit = self.createPlugin()
        strPathToTableFile = os.path.join(self.strDataPath, "rdfit.xml")
        xsDataResultRdfit = edPluginRdfit.getOutputDataFromDNATableFile(strPathToTableFile)
        strPathToReference = os.path.join(self.strDataPath, "XSDataResultRdfit_reference.xml")
        xsDataResultRdfitReference = XSDataResultRdfit.parseFile(strPathToReference)
        EDAssert.equal(xsDataResultRdfitReference.marshal(), xsDataResultRdfit.marshal(), "Test parsing result 'DNA' xml file")

    def process(self):
        self.addTestMethod(self.testSetDataInput)
        self.addTestMethod(self.testGenerateCommands)
        self.addTestMethod(self.testGetOutputDataFromDNATableFile)
