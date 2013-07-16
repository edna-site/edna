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


import numpy, os, scipy.ndimage, pprint
import pylab
from numpy.linalg import solve

from EDPluginExec import EDPluginExec
from EDUtilsFile import EDUtilsFile
from EDUtilsArray import EDUtilsArray
from EDFactoryPluginStatic import EDFactoryPluginStatic 

from XSDataCalibrateEnergyv1_0 import XSDataInputCalibrateEnergy
from XSDataCalibrateEnergyv1_0 import XSDataResultCalibrateEnergy

ODD_SIGN = 1.0

class EDPluginExecCalibrateEnergyv1_0( EDPluginExec ):
    """
    This plugin reads an ascii file of DEXAFS data produced by the ID24 beamline at the ESRF.
    The energy calibration coefficients must be given as input. 
    """

    def __init__( self ):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputCalibrateEnergy)   


    def fitFunc(self, x, yArray, a0, a1, a2):
        xPoints = (numpy.arange(yArray.shape[0]) - a0)*a1
        if x > a0:
            value = numpy.interp(x, xPoints, yArray) + x*a2
        else:
            value = numpy.interp(x, xPoints, yArray)
        return value
        

    
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecCalibrateEnergyv1_0.process")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputFile, "Data Input 'inputFile' is None")
        self.checkMandatoryParameters(self.dataInput.elementName, "Data Input 'energyuCalibration' is None")
        # Load calibration data
        calibratedData = self.loadCalibratedData(self.dataInput.elementName.value)
#        # Normalize
        minData = numpy.min(calibratedData[:,1])
        maxData = numpy.max(calibratedData[:,1])
        normCalibratedData = (calibratedData[:,1] - minData) / (maxData - minData)
        #  Derivative:
        derivativeClaibratedData = numpy.diff(calibratedData[:,1])
        # Normalize
        maxDerCalibData = numpy.amax(derivativeClaibratedData)
        maxCalibIndex = numpy.unravel_index(derivativeClaibratedData.argmax(), derivativeClaibratedData.shape)[0]
        print maxCalibIndex 
        normDerCalibData = derivativeClaibratedData / maxDerCalibData
#        pylab.show()
#        # Load input data
        xsDataFile = self.dataInput.inputFile
        numpyDataArray = numpy.genfromtxt(xsDataFile.path.value, skip_header=1)
        numpyAverageDataArray = numpy.average(numpyDataArray[:,1:], axis=1)
#        # Normalize
        minData = numpy.min(numpyAverageDataArray)
        maxData = numpy.max(numpyAverageDataArray)
        normData = (numpyAverageDataArray - minData) / (maxData - minData)
        #  Derivative:
        derivativeData = numpy.diff(numpyAverageDataArray)
        # Normalize
        maxDerData = numpy.amax(derivativeData)
        maxIndex = numpy.unravel_index(derivativeData.argmax(), derivativeData.shape)[0]
        print maxIndex 
        derivativeData = derivativeData / maxDerData
#        pylab.plot(numpy.arange(normDerCalibData.shape[0]) - maxCalibIndex, normDerCalibData)
#        pylab.plot((numpy.arange(derivativeData.shape[0]) - maxIndex)*0.8, derivativeData)
#        pylab.plot(numpy.arange(normCalibratedData.shape[0]) - maxCalibIndex, normCalibratedData)
#        pylab.plot((numpy.arange(normData.shape[0]) - maxIndex), normData)
        
        xValues = numpy.arange(normData.shape[0]-1000)-maxIndex
        print xValues.shape
        pylab.plot(xValues, normData[:-1000])
        pylab.plot(xValues, [self.fitFunc(x, normCalibratedData, maxCalibIndex, 1.5, 0.0000) for x in xValues])
#        from scipy.optimize import curve_fit
#        popt, pcov = curve_fit(self.fitFunc, xValues, normData[:-1000])
#        print popt, pcov 
        # Attempt to fit...
#        polyFit = numpy.polyfit(normCalibratedData, normData, 1)
        pylab.show()
        
        
        
        
##        # Normalize
#        minData = numpy.min(calibratedData[:,1])
#        maxData = numpy.max(calibratedData[:,1])
#        calibratedData[:,1] = (calibratedData[:,1] - minData) / (maxData - minData)
#        peaksCalibrationX = self.findLocalMaxima(calibratedData[:,1])
#        from pylab import *
#        plot(calibratedData[:,1])
#        plot(peaksCalibrationX, calibratedData[peaksCalibrationX,1], "ro" )
#        # Load input data
#        xsDataFile = self.dataInput.inputFile
#        numpyDataArray = numpy.genfromtxt(xsDataFile.path.value, skip_header=1)
        
        
        
        
##        # Normalize
#        minData = numpy.min(numpyDataArray[:,1])
#        maxData = numpy.max(numpyDataArray[:,1])
#        numpyDataArray[:,1] = (numpyDataArray[:,1] - minData) / (maxData - minData)
#        peaksDataX = self.findLocalMaxima(numpyDataArray[:,1])
#        from pylab import *
#        # Fit data points
#        polyFit = numpy.polyfit(peaksDataX, peaksCalibrationX, 1)
#        print peaksCalibrationX
#        print peaksDataX
#        print polyFit
#        poly = numpy.poly1d(polyFit)
#        print poly(peaksDataX)
#        plot(poly(numpyDataArray[:,0]), numpyDataArray[:,1])
#        plot(poly(peaksDataX), numpyDataArray[peaksDataX,1], "ro" )        
#        show()
            
    
    
    
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
                    
                
                
                

    
    def findLocalMaxima(self, data):
        # From http://stackoverflow.com/questions/9111711/get-coordinates-of-local-maxima-in-2d-array-above-certain-value
        neighborhood_size = 10
        threshold = 0.015
        
       
        data_max = scipy.ndimage.filters.maximum_filter(data, neighborhood_size)
        maxima = (data == data_max)
        data_min = scipy.ndimage.filters.minimum_filter(data, neighborhood_size)
        diff = ((data_max - data_min) > threshold)
        maxima[diff == 0] = 0
        
        labeled, num_objects = scipy.ndimage.label(maxima)
        slices = scipy.ndimage.find_objects(labeled)
#        print("slices: %s" % pprint.pformat(slices))
        x = []
        for slice in slices:
            dx = slice[0]
            x_center = (dx.start + dx.stop - 1)/2
            x.append(x_center)
#        print("data:")
#        print(pprint.pformat(data))
#        print("x: %s" % pprint.pformat(x))
        # Return the three strongest peaks
        peaks = [[posX, data[posX]] for posX in x]
        peaksSorted = sorted(peaks, key=lambda peak: peak[1], reverse=True)
        if len(peaksSorted) > 2:
            peaksSorted = peaksSorted[0:2]
        print(peaksSorted)
        return [peak[0] for peak in peaksSorted]
             