#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Michael Hellmig (michael.hellmig@bessy.de)
#                            Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Michael Hellmig" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import struct

from EDUtilsFile     import EDUtilsFile
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDConfiguration import EDConfiguration

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataString

from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataResultReadImageHeader

EDFactoryPluginStatic.loadModule("XSDataWaitFilev1_0")
from XSDataWaitFilev1_0 import XSDataInputWaitFile

class EDPluginControlReadImageHeaderv10(EDPluginControl):


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputReadImageHeader)
        self.edPluginExecReadImageHeader = None
        self.strReadImageHeaderPluginName = None
        self.xsDataResultReadImageHeader = None
        self.strFileImagePath = None
        # Default time out for wait file
        self.fWaitFileTimeOut = 30 #s
        # Map between image suffix and image type
        self.strSuffixADSC = "img"
        self.strSuffixMARCCD1 = "mccd"
        self.strSuffixMARCCD2 = "marccd"
        self.strSuffixPilatus6M = "cbf"
        # Recognised types of detectors
        self.strADSC = "ADSC"
        self.strMARCCD = "MARCCD"
        self.strPilatus6M = "Pilatus6M"
        #
        self.strPluginExecWaitFile = "EDPluginWaitFile"
        self.strPluginExecReadImageHeaderADSC = "EDPluginExecReadImageHeaderADSCv10"
        self.strPluginExecReadImageHeaderMARCCD = "EDPluginExecReadImageHeaderMARCCDv10"
        self.strPluginExecReadImageHeaderPilatus6M = "EDPluginExecReadImageHeaderPilatus6Mv10"
        # Table mapping image suffix with detector type
        self.dictSuffixToImageType = { \
              self.strSuffixADSC    : self.strADSC, \
              self.strSuffixMARCCD1 : self.strMARCCD, \
              self.strSuffixMARCCD2 : self.strMARCCD, \
              self.strSuffixPilatus6M : self.strPilatus6M \
                                                    }
		# Table mapping image type with exec read image header plugin
        self.dictImageTypeToPluginName = { \
			  self.strADSC   : self.strPluginExecReadImageHeaderADSC, \
              self.strMARCCD : self.strPluginExecReadImageHeaderMARCCD, \
              self.strPilatus6M : self.strPluginExecReadImageHeaderPilatus6M
                									 }

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlReadImageHeaderv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def configure(self, _edPlugin = None):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.configure")
        self.fWaitFileTimeOut = float(self.config.get("waitFileTimeOut", self.fWaitFileTimeOut))
        
        

    def preProcess(self, _edObject=None):
        """
        """
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.preProcess")
        # First determine the type of image
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFileImage = xsDataInputReadImageHeader.getImage()
        self.strFileImagePath = xsDataFileImage.getPath().getValue()
        # Plugin for waiting for files
        self.edPluginExecWaitFile = self.loadPlugin(self.strPluginExecWaitFile)
        xsDataInputWaitFile = XSDataInputWaitFile()
        xsDataInputWaitFile.setExpectedFile(XSDataFile(XSDataString(self.strFileImagePath)))
        xsDataInputWaitFile.setExpectedSize(XSDataInteger(100000))
        xsDataInputWaitFile.setTimeOut(XSDataTime(self.fWaitFileTimeOut))
        self.edPluginExecWaitFile.setDataInput(xsDataInputWaitFile)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.process")
        if self.edPluginExecWaitFile is not None:
            self.edPluginExecWaitFile.connectSUCCESS(self.doSuccessWaitFile)
            self.edPluginExecWaitFile.connectFAILURE(self.doFailureWaitFile)
            self.executePluginSynchronous(self.edPluginExecWaitFile)


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.finallyProcess")
        if self.xsDataResultReadImageHeader is None:
            # Create empty xsDataResult
            self.xsDataResultReadImageHeader = XSDataResultReadImageHeader() 
        self.setDataOutput(self.xsDataResultReadImageHeader)


    def doSuccessWaitFile(self, _edPlugin):
        """
        The file has appeared on the disk 
        """
        self.DEBUG("EDPluginControlReadImageHeaderv10.doSuccessWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doSuccessWaitFile")
        # Check that we have some output
        if self.edPluginExecWaitFile.getDataOutput().getActualFile():
            # Read image header plugin
            strFileImagePath = self.edPluginExecWaitFile.getDataOutput().getActualFile().getPath().getValue()
            strImageType = self.determineImageType(strFileImagePath)
            if (strImageType is not None):
                strReadImageHeaderPluginName = self.determineExecReadImageHeaderPluginName(strImageType)
                # Will be changed once code review #240 is ready
                self.edPluginExecReadImageHeader = self.loadPlugin(strReadImageHeaderPluginName)
                self.edPluginExecReadImageHeader.connectSUCCESS(self.doSuccessActionReadImageHeader)
                self.edPluginExecReadImageHeader.connectFAILURE(self.doFailureActionReadImageHeader)
                self.edPluginExecReadImageHeader.setDataInput(self.getDataInput())
                self.executePluginSynchronous(self.edPluginExecReadImageHeader)
        else:
            self.doFailureWaitFile(_edPlugin)

    
    def doFailureWaitFile(self, _edPlugin):
        """
        The file has not appeared on the disk 
        """
        self.DEBUG("EDPluginControlReadImageHeaderv10.doFailureWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doFailureWaitFile")
        self.ERROR("Timeout when waiting for image %s" % self.strFileImagePath)
        self.setFailure()

    
    def doSuccessActionReadImageHeader(self, _edPlugin):
        """
        Retrieve the potential warning messages
        """
        self.DEBUG("EDPluginControlReadImageHeaderv10.doSuccessActionReadImageHeader")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doSuccessActionReadImageHeader")
        self.xsDataResultReadImageHeader = _edPlugin.getDataOutput()


    def doFailureActionReadImageHeader(self, _edPlugin):
        """
        Retrieve the potential warning messages
        Retrieve the potential error messages
        """
        self.DEBUG("EDPluginControlReadImageHeaderv10.doFailureActionReadImageHeader")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlReadImageHeaderv10.doFailureActionReadImageHeader")


    def isAdscImageFormat(self, _strImageFileName):
        """
        Detects ADSC image format and returns True after successful identification.
        """
        strKeyword = None
        pyFile = None
        bIsAdscFormat = False
        try:
            pyFile = open(_strImageFileName, "r")
        except:
            self.warning("EDPluginControlReadImageHeaderv10.isAdscImageFormat: couldn't open file: " + _strImageFileName)

        if pyFile != None:
            self.DEBUG("EDPluginControlReadImageHeaderv10.isAdscImageFormat: detecting image format from file " + _strImageFileName)
            pyFile.seek(0, 0)
            strLine = pyFile.readline()
            if strLine[0] == "{":
                strLine = pyFile.readline()
                listSplit = strLine.split("=")
                strKeyword = listSplit[0]
        if strKeyword == "HEADER_BYTES":
            bIsAdscFormat = True
            pyFile.close()
        return bIsAdscFormat


    def isMarccdImageFormat(self, _strFileName):
        """
        Detects MARCCD image format and returns True after successful identification.
        """
        strValue = None
        strFormat = None
        #
        #  Created by Krister Larsson on 08/11/5.
        #  Modified by Olof Svensson 20090401
        #  Reduced to simple format checking by Michael Hellmig 20091008
        #
        strChar = 's'

        pyListRow = [strChar, 'header_name', 16]

        pyFile = None
        try:
        	pyFile = open(_strFileName, "rb")
        except:
        	self.warning("EDPluginControlReadImageHeaderv10.isMarccdImageFormat: couldn't open file: " + _strFileName)
        if (pyFile is not None):
            self.DEBUG("EDPluginControlReadImageHeaderv10.isMarccdImageFormat: detecting image format from file " + _strFileName)

            # Move to marccd part of header
            pyFile.seek(1028)

            if len(pyListRow) == 3:
                strFormat = str(pyListRow[2]) + str(pyListRow[0])
            else:
                strFormat = pyListRow[0]

            iReadSize = struct.calcsize(strFormat)
            pyRawData = pyFile.read(iReadSize)
            pyFile.close()

            strValue = struct.unpack(strFormat, pyRawData)
            if len(strValue) == 1:
                strValue = strValue[0]
            if pyListRow[0] == strChar:
                strValue = strValue.strip('\x00')

        # identify MARCCD format, implementation based on CCP4 DiffractionImage library
        if ((strValue == 'MMX') or (strValue == 'MARCCD')):
            return True
        else:
            return False


    def isPilatus6MImageFormat(self, _strImageFileName):
        """
        Detects Pilatus 6M CBF image format and returns True after successful identification.
        """
        strKeyword = None
        pyFile = None
        bIsPilatus6MFormat = False
        try:
            pyFile = open(_strImageFileName, "r")
        except:
            self.warning("EDPluginControlReadImageHeaderv10.isPilatus6MImageFormat: couldn't open file: " + _strImageFileName)

        if pyFile != None:
            self.DEBUG("EDPluginControlReadImageHeaderv10.isPilatus6MImageFormat: detecting image format from file " + _strImageFileName)
            pyFile.seek(0, 0)
            strLine = pyFile.readline()
            if strLine.find("SLS/DECTRIS PILATUS detectors") != -1:
                bIsPilatus6MFormat = True
            elif strLine.find("###CBF: VERSION 1.5") != -1:
                bIsPilatus6MFormat = True
            pyFile.close()
        return bIsPilatus6MFormat




    def determineImageType(self, _strImagePath):
        """
        This method determines the type of an image, i.e. ADSC, MAR CCD etc.
        """
        strImageType = None
        bUnknownImageType = False
        self.DEBUG("EDPluginControlReadImageHeaderv10.determineImageType")
        # First look at the image extension, then try to distinguish between MARCCD and ADSC based on header information
        strImageSuffix = EDUtilsFile.getFileExtension(_strImagePath)
        if strImageSuffix in self.dictSuffixToImageType.keys():
            # find out image type depending on the content of the respective image header
            if self.isMarccdImageFormat(_strImagePath):
                strImageType = self.strMARCCD
            elif self.isAdscImageFormat(_strImagePath):
                strImageType = self.strADSC
            elif self.isPilatus6MImageFormat(_strImagePath):
                strImageType = self.strPilatus6M
            else:
                bUnknownImageType = True
        else:
            bUnknownImageType = True

        if bUnknownImageType:
            strErrorMessage = "EDPluginControlReadImageHeaderv10.determineImageType: Unknown image type for image %s " % _strImagePath
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            self.DEBUG("EDPluginControlReadImageHeaderv10.determineImageType: file: " + _strImagePath + \
                             ", type: " + strImageType)
        return strImageType


    def determineExecReadImageHeaderPluginName(self, _strImageType):
        """
        This method determines the name of the exec plugin read image header
        """
        strReadImageHeaderPluginName = None
        self.DEBUG("EDPluginControlReadImageHeaderv10.determinePluginName")
        # For the moment, only look on the image suffix
        if _strImageType in self.dictImageTypeToPluginName.keys():
            strReadImageHeaderPluginName = self.dictImageTypeToPluginName[ _strImageType ]
        else:
            strErrorMessage = "EDPluginControlReadImageHeaderv10.determineExecReadImageHeaderPluginName: Unknown image type: %s" % _strImageType
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        return strReadImageHeaderPluginName

