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


import numpy

from EDPluginExec import EDPluginExec
from EDUtilsFile import EDUtilsFile
from EDUtilsArray import EDUtilsArray

from XSDataReadDataBM23v1_0 import XSDataInputReadDataBM23
from XSDataReadDataBM23v1_0 import XSDataResultReadDataBM23


class EDPluginExecReadDataBM23v1_0( EDPluginExec ):
    """
    This plugin reads an ascii file of DEXAFS data produced by the BM23 beamline at the ESRF.
    The energy calibration coefficients must be given as input. 
    """

    def __init__( self ):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputReadDataBM23)   

    
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecReadDataBM23v1_0.process")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputFile, "Data Input 'inputFile' is None")
        # Load input data
        numpyDataArray = numpy.genfromtxt(self.dataInput.inputFile.path.value)
        print numpyDataArray
        print numpyDataArray[:,0]
        print numpyDataArray[:,1:]
        print numpyDataArray.shape
        # Create some output data
        xsDataResultReadDataBM23 = XSDataResultReadDataBM23()
        xsDataResultReadDataBM23.energy = EDUtilsArray.arrayToXSData(numpyDataArray[:,0])
        xsDataResultReadDataBM23.dataArray = EDUtilsArray.arrayToXSData(numpyDataArray[:,1:])
        self.setDataOutput(xsDataResultReadDataBM23)
    

    def loadInputData(self, _strPath):
        """
        This method tries to read the data in the file _strPath. If successful
        a numpy array containing the data is returned.
        """
        returnArray = None
        strData = EDUtilsFile.readFile(_strPath)
        listDataLines = strData.split("\n")
        # Loop through all data lines in order to find data dimensions
        iNumberOfRows    = 0
        iNumberOfColumns = 0
        iMaxNumberOfRows = 100000
        iMaxNumberOfColumns = 10000
        iIndexRow = 0
        # Create numpy array
        dataArray = numpy.ndarray((iMaxNumberOfRows,iMaxNumberOfColumns - 1))
        for strDataLine in listDataLines:
            # Try to convert fist column to a numerical value:
            listColumns = strDataLine.split()
            if "" in listColumns:
                listColumns.remove("")
            try:
                listValues = map(float, listColumns)
                iColumns = len(listColumns)
                if iColumns > 2:
                    dataArray[iNumberOfRows, 0:iColumns-1] = listValues[1:]
                    iNumberOfRows += 1
                    if iNumberOfColumns == 0:
                        iNumberOfColumns = iColumns
            except:
                pass
        returnArray = dataArray[0:iNumberOfRows-1, 0:iNumberOfColumns-1]
        return returnArray
        
        
