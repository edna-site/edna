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


import numpy, os

from EDPluginExec import EDPluginExec
from EDUtilsFile import EDUtilsFile
from EDUtilsArray import EDUtilsArray
from EDFactoryPluginStatic import EDFactoryPluginStatic 

from XSDataCalibrateEnergyv1_0 import XSDataInputCalibrateEnergy
from XSDataCalibrateEnergyv1_0 import XSDataResultCalibrateEnergy


class EDPluginExecCalibrateEnergyv1_0( EDPluginExec ):
    """
    This plugin reads an ascii file of DEXAFS data produced by the ID24 beamline at the ESRF.
    The energy calibration coefficients must be given as input. 
    """

    def __init__( self ):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputCalibrateEnergy)   

    
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecCalibrateEnergyv1_0.process")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputFile, "Data Input 'inputFile' is None")
        self.checkMandatoryParameters(self.dataInput.elementName, "Data Input 'energyuCalibration' is None")
        # Load calibration data
        calibratedData = self.loadCalibratedData(self.dataInput.elementName.value)
        # Normalize
        minData = numpy.min(calibratedData[:,1])
        maxData = numpy.max(calibratedData[:,1])
        print minData, maxData
        calibratedData[:,1] = (calibratedData[:,1] - minData) / (maxData - minData)
        from pylab import *
        plot(calibratedData[:,0], calibratedData[:,1])
        # Load input data
        xsDataFile = self.dataInput.inputFile
        numpyDataArray = numpy.genfromtxt(xsDataFile.path.value, skip_header=1)
        # Normalize
        minData = numpy.min(numpyDataArray[:,1])
        maxData = numpy.max(numpyDataArray[:,1])
        print minData, maxData
        numpyDataArray[:,1] = (numpyDataArray[:,1] - minData) / (maxData - minData)
        
        calibrationPoly = numpy.poly1d([0.001, 23.65])
        print calibrationPoly(numpyDataArray[:,0])
        plot(calibrationPoly(numpyDataArray[:,0]), numpyDataArray[:,1])
        show()
            
    
    
    
    def loadCalibratedData(self, _strElementName):
        """
        This method reads a file containing the calibrated energy spectra
        """
        calibratedData = None
        strModuleLocation = EDFactoryPluginStatic.getModuleLocation(self.getPluginName())
        strEnergyDataFile = os.path.join(os.path.dirname(strModuleLocation), "calibrationData", _strElementName+".dat")
        if os.path.exists(strEnergyDataFile):
            listLines = []
            with open(strEnergyDataFile, 'r') as f:
                listLines = f.readlines()
            iSkipHeader = 0
            iSkipFooter = 0
            bIsHeader = True
            for strLine in listLines:
                if strLine.startswith('#'):
                    if bIsHeader:
                        iSkipHeader += 1
                    else:
                        iSkipFooter += 1
                else:
                    bIsHeader = False
            calibratedData = numpy.genfromtxt(strEnergyDataFile, skip_header=iSkipHeader, skip_footer=iSkipFooter)
        return calibratedData
                    
                
                
                
                 
        
    

 