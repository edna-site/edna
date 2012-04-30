#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration

from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength

from XSDataMOSFLMv10 import XSDataCell
from XSDataMOSFLMv10 import XSDataMOSFLMNewmat
from XSDataMOSFLMv10 import XSDataMOSFLMMissettingsAngles


class EDPluginMOSFLMv10(EDPluginExecProcessScript):

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)

        self.addCompatibleVersion("Mosflm version 7.0.5 for Image plate and CCD data 12th August 2009")
        self.addCompatibleVersion("Mosflm version 7.0.6 for Image plate and CCD data 26th January 2010")
        self.addCompatibleVersion("Mosflm version 7.0.7 for Image plate and CCD data 20th December 2010")
        self.addCompatibleVersion("Mosflm version 7.0.8  for Image plate and CCD data 12th March 2012")

        self.strMOSFLMNewmatFileName = None
        self.strMOSFLMMatrixFileName = None
        self.bReversephi = False
        self.strRaster = None

    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginMOSFLMv10.process")
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginMOSFLMv10"):
            raise RuntimeError, "ExectuteAbstractPluginError"


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        EDVerbose.DEBUG("EDPluginMOSFLMv10.configure")
        self.setRequireCCP4(True)
        self.setScriptCommandline(" DNA " + self.getScriptBaseName() + "_dnaTables.xml")
        # Check for reversephi configuration option
        if self.getConfiguration():
            xsDataStringParameter = EDConfiguration.getParamItem(self.getConfiguration(), "reversephi")
            if xsDataStringParameter:
                strReversephi = xsDataStringParameter.getValue()
                if  strReversephi is not None:
                    if strReversephi.lower() == "true":
                        self.bReversephi = True
            xsDataStringParameterRaster = EDConfiguration.getParamItem(self.getConfiguration(), "raster")
            if xsDataStringParameterRaster:
                self.strRaster = xsDataStringParameterRaster.getValue()


    def checkParameters(self):
        """
        Checks the mandatory parameters for all MOSLFM plugins
        """
        EDVerbose.DEBUG("EDPluginMOSFLMv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getBeam(), "beamPosition")
        self.checkMandatoryParameters(self.getDataInput().getDetector(), "detector")
        self.checkMandatoryParameters(self.getDataInput().getDirectory(), "directory")
        self.checkMandatoryParameters(self.getDataInput().getDistance(), "distance")
        self.checkMandatoryParameters(self.getDataInput().getTemplate(), "template")
        self.checkMandatoryParameters(self.getDataInput().getWavelength(), "wavelength")


    def generateMOSFLMCommands(self):
        """
        This method creates a list of MOSFLM indexing commands given a valid
        XSDataMOSFLMInput as self.getDataInput()
        """
        EDVerbose.DEBUG("EDPluginMOSFLMv10.generateMOSFLMCommands")
        xsDataMOSFLMInput = self.getDataInput()

        if (xsDataMOSFLMInput is not None):

            xsDataFloatWavelength = xsDataMOSFLMInput.getWavelength()
            if (xsDataFloatWavelength is not None):
                self.addListCommandExecution("WAVELENGTH " + str(xsDataFloatWavelength.getValue()))

            xsDataLengthDistance = xsDataMOSFLMInput.getDistance()
            if (xsDataLengthDistance is not None):
                self.addListCommandExecution("DISTANCE " + str(xsDataLengthDistance.getValue()))

            xsDataMOSFLMBeamPosition = xsDataMOSFLMInput.getBeam()
            if (xsDataMOSFLMBeamPosition is not None):
                strBeamX = str(xsDataMOSFLMBeamPosition.getX().getValue())
                strBeamY = str(xsDataMOSFLMBeamPosition.getY().getValue())
                self.addListCommandExecution("BEAM " + strBeamX + " " + strBeamY)

            xsDataMOSFLMDetector = xsDataMOSFLMInput.getDetector()
            if (xsDataMOSFLMDetector is not None):
                strDetectorType = xsDataMOSFLMDetector.getType()
                if (strDetectorType is not None):
                    self.addListCommandExecution("DETECTOR " + strDetectorType.getValue())

            xsDataStringDirectory = xsDataMOSFLMInput.getDirectory()
            if (xsDataStringDirectory is not None):
                self.addListCommandExecution("DIRECTORY " + xsDataStringDirectory.getValue())

            xsDataStringTemplate = xsDataMOSFLMInput.getTemplate()
            if (xsDataStringTemplate is not None):
                self.addListCommandExecution("TEMPLATE " + xsDataStringTemplate.getValue())

            xsDataStringSymmetry = xsDataMOSFLMInput.getSymmetry()
            if (xsDataStringSymmetry is not None):
                self.addListCommandExecution("SYMMETRY " + xsDataStringSymmetry.getValue())
            strNewmatFileName = self.getNewmatFileName()

            xsDataNewmatMatrix = xsDataMOSFLMInput.getMatrix()
            if (xsDataNewmatMatrix is not None):
                self.writeDataMOSFLMNewmat(xsDataNewmatMatrix, self.getMatrixFileName())
                self.addListCommandExecution("MATRIX " + self.getMatrixFileName())

            xsDataFloatMosaicity = xsDataMOSFLMInput.getMosaicity()
            if (xsDataFloatMosaicity is not None):
                self.addListCommandExecution("MOSAIC " + str(xsDataFloatMosaicity.getValue()))

            # Add exclude regions if Pilatus
            if xsDataMOSFLMInput.getDetector().getType().getValue() == "PILATUS":
                self.addListCommandExecution("LIMITS EXCLUDE  0.0 338.77 434.6 340.24")
                self.addListCommandExecution("LIMITS EXCLUDE  0.0 253.80 434.6 255.28")
                self.addListCommandExecution("LIMITS EXCLUDE  0.0 168.83 434.6 170.21")
                self.addListCommandExecution("LIMITS EXCLUDE  0.0  83.86 434.6  85.24")
                self.addListCommandExecution("LIMITS EXCLUDE 398.18  0.0 401.28 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 361.72  0.0 364.81 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 325.25  0.0 328.35 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 288.79  0.0 291.88 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 252.32  0.0 255.42 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 215.86  0.0 218.96 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 179.40  0.0 182.49 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 142.93  0.0 145.86 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE 106.47  0.0 109.56 423.6")
                self.addListCommandExecution("LIMITS EXCLUDE  70.00  0.0 73.10  423.6")
                self.addListCommandExecution("LIMITS EXCLUDE  33.54  0.0 36.64  423.6")
            
            # Check if reversephi is configured
            if self.bReversephi:
                self.addListCommandExecution("DETECTOR REVERSEPHI")

            # Check if raster is configured
            if self.strRaster:
                self.addListCommandExecution("RASTER %s" % self.strRaster)



    def getNewmatFileName(self):
        if (self.strMOSFLMNewmatFileName is None):
            self.strMOSFLMNewmatFileName = self.getScriptBaseName() + "_newmat.mat"
        return self.strMOSFLMNewmatFileName


    def setNewmatFileName(self, _strMOSFLMNewmatFileName):
        self.strMOSFLMNewmatFileName = _strMOSFLMNewmatFileName


    def getMatrixFileName(self):
        if (self.strMOSFLMMatrixFileName is None):
            self.strMOSFLMMatrixFileName = self.getScriptBaseName() + "_matrix.mat"
        return self.strMOSFLMMatrixFileName


    def setMatrixFileName(self, _strMOSFLMMatrixFileName):
        self.strMOSFLMMatrixFileName = _strMOSFLMMatrixFileName


    def splitStringIntoListOfFloats(self, _strInput):
        EDVerbose.DEBUG("EDPluginMOSFLMv10.splitStringIntoListOfFloats")
        listFloats = []
        listString = _strInput.split()
        for strElement in listString:
            if strElement != "":
                listFloats.append(float(strElement))
        return listFloats


    def getDataMOSFLMMatrix(self, _strMatrixFileName=None):
        EDVerbose.DEBUG("EDPluginMOSFLMv10.getDataMOSFLMMatrix")
        strMatrixFileName = None
        if (_strMatrixFileName is None):
            strMatrixFileName = self.getMatrixFileName()
        else:
            strMatrixFileName = _strMatrixFileName
        xsDataMOSFLMNewmatMatrix = self.getDataMOSFLMNewmat(strMatrixFileName)
        return xsDataMOSFLMNewmatMatrix


    def getDataMOSFLMNewmat(self, _strNewmatFileName=None):
        EDVerbose.DEBUG("EDPluginMOSFLMv10.getDataMOSFLMNewmat")
        xsDataMOSFLMNewmat = None
        strNewmatFileName = None
        listOfListOfFloat = []
        if (_strNewmatFileName == None):
            strNewmatFileName = self.getNewmatFileName()
        else:
            strNewmatFileName = _strNewmatFileName
        strNewmat = None
        try:
            strNewmat = self.readProcessFile(strNewmatFileName)
        except:
            strError = self.readProcessErrorLogFile()
            if (strError is not None) and (strError != ""):
                strErrorMessage = "EDPluginMOSFLMv10.getDataMOSFLMNewmat: %s : error reading newmat file : %s" % \
                                (self.getClassName(), strError)
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                strErrorMessage = "EDPluginMOSFLMv10.getDataMOSFLMNewmat : Cannot read MOSFLM NEWMAT file : " + strNewmatFileName
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
        #print strNewmat
        if (strNewmat is not None):
            listLine = strNewmat.split("\n")
            # Convert into list of lists of float
            for strLine in listLine:
                if not strLine.startswith("SYMM"):
                    listOfListOfFloat.append(self.splitStringIntoListOfFloats(strLine))
            # Fill in the data
            xsDataMOSFLMNewmat = XSDataMOSFLMNewmat()

            XSDataMatrixDoubleA = XSDataMatrixDouble()
            XSDataMatrixDoubleA.setM11(listOfListOfFloat[0][0])
            XSDataMatrixDoubleA.setM12(listOfListOfFloat[0][1])
            XSDataMatrixDoubleA.setM13(listOfListOfFloat[0][2])
            XSDataMatrixDoubleA.setM21(listOfListOfFloat[1][0])
            XSDataMatrixDoubleA.setM22(listOfListOfFloat[1][1])
            XSDataMatrixDoubleA.setM23(listOfListOfFloat[1][2])
            XSDataMatrixDoubleA.setM31(listOfListOfFloat[2][0])
            XSDataMatrixDoubleA.setM32(listOfListOfFloat[2][1])
            XSDataMatrixDoubleA.setM33(listOfListOfFloat[2][2])
            xsDataMOSFLMNewmat.setAMatrix(XSDataMatrixDoubleA)

            xsDataMOSFLMMissettingsAngles = XSDataMOSFLMMissettingsAngles()
            xsDataMOSFLMMissettingsAngles.setPhix(XSDataAngle(listOfListOfFloat[3][0]))
            xsDataMOSFLMMissettingsAngles.setPhiy(XSDataAngle(listOfListOfFloat[3][1]))
            xsDataMOSFLMMissettingsAngles.setPhiz(XSDataAngle(listOfListOfFloat[3][2]))
            xsDataMOSFLMNewmat.setMissettingAngles(xsDataMOSFLMMissettingsAngles)

            XSDataMatrixDoubleU = XSDataMatrixDouble()
            XSDataMatrixDoubleU.setM11(listOfListOfFloat[4][0])
            XSDataMatrixDoubleU.setM12(listOfListOfFloat[4][1])
            XSDataMatrixDoubleU.setM13(listOfListOfFloat[4][2])
            XSDataMatrixDoubleU.setM21(listOfListOfFloat[5][0])
            XSDataMatrixDoubleU.setM22(listOfListOfFloat[5][1])
            XSDataMatrixDoubleU.setM23(listOfListOfFloat[5][2])
            XSDataMatrixDoubleU.setM31(listOfListOfFloat[6][0])
            XSDataMatrixDoubleU.setM32(listOfListOfFloat[6][1])
            XSDataMatrixDoubleU.setM33(listOfListOfFloat[6][2])
            xsDataMOSFLMNewmat.setUMatrix(XSDataMatrixDoubleU)

            xsDataCellRefined = XSDataCell()
            xsDataCellRefined.setLength_a(XSDataLength(listOfListOfFloat[7][0]))
            xsDataCellRefined.setLength_b(XSDataLength(listOfListOfFloat[7][1]))
            xsDataCellRefined.setLength_c(XSDataLength(listOfListOfFloat[7][2]))
            xsDataCellRefined.setAngle_alpha(XSDataAngle(listOfListOfFloat[7][3]))
            xsDataCellRefined.setAngle_beta(XSDataAngle(listOfListOfFloat[7][4]))
            xsDataCellRefined.setAngle_gamma(XSDataAngle(listOfListOfFloat[7][5]))
            xsDataMOSFLMNewmat.setRefinedCell(xsDataCellRefined)

        return xsDataMOSFLMNewmat



    def writeDataMOSFLMNewmat(self, _xsDataMOSFLNNewmat, _strNewmatFileName=None):
        EDVerbose.DEBUG("EDPluginMOSFLMv10.writeDataMOSFLMNewmat")
        strNewmatFileName = None
        if (_strNewmatFileName is None):
            strNewmatFileName = self.getNewmatFileName()
        else:
            strNewmatFileName = _strNewmatFileName
        XSDataMatrixDoubleA = _xsDataMOSFLNNewmat.getAMatrix()
        strNewmat = " %11.8f %11.8f %11.8f\n" % (XSDataMatrixDoubleA.getM11(), XSDataMatrixDoubleA.getM12(), XSDataMatrixDoubleA.getM13())
        strNewmat += " %11.8f %11.8f %11.8f\n" % (XSDataMatrixDoubleA.getM21(), XSDataMatrixDoubleA.getM22(), XSDataMatrixDoubleA.getM23())
        strNewmat += " %11.8f %11.8f %11.8f\n" % (XSDataMatrixDoubleA.getM31(), XSDataMatrixDoubleA.getM32(), XSDataMatrixDoubleA.getM33())
        xsDataMOSFLMMissettingAngles = _xsDataMOSFLNNewmat.getMissettingAngles()
        strNewmat += " %11.3f %11.3f %11.3f\n" % (xsDataMOSFLMMissettingAngles.getPhix().getValue(),
                                                         xsDataMOSFLMMissettingAngles.getPhiy().getValue(),
                                                         xsDataMOSFLMMissettingAngles.getPhiz().getValue())
        XSDataMatrixDoubleU = _xsDataMOSFLNNewmat.getUMatrix()
        strNewmat += " %11.7f %11.7f %11.7f\n" % (XSDataMatrixDoubleU.getM11(), XSDataMatrixDoubleU.getM12(), XSDataMatrixDoubleU.getM13())
        strNewmat += " %11.7f %11.7f %11.7f\n" % (XSDataMatrixDoubleU.getM21(), XSDataMatrixDoubleU.getM22(), XSDataMatrixDoubleU.getM23())
        strNewmat += " %11.7f %11.7f %11.7f\n" % (XSDataMatrixDoubleU.getM31(), XSDataMatrixDoubleU.getM32(), XSDataMatrixDoubleU.getM33())

        xsDataCellRefined = _xsDataMOSFLNNewmat.getRefinedCell()
        strNewmat += " %11.4f %11.4f %11.4f" % (xsDataCellRefined.getLength_a().getValue(),
                                                         xsDataCellRefined.getLength_b().getValue(),
                                                         xsDataCellRefined.getLength_c().getValue())
        strNewmat += " %11.4f %11.4f %11.4f\n" % (xsDataCellRefined.getAngle_alpha().getValue(),
                                                         xsDataCellRefined.getAngle_beta().getValue(),
                                                         xsDataCellRefined.getAngle_gamma().getValue())
        strNewmat += " %11.3f %11.3f %11.3f\n" % (xsDataMOSFLMMissettingAngles.getPhix().getValue(),
                                                         xsDataMOSFLMMissettingAngles.getPhiy().getValue(),
                                                         xsDataMOSFLMMissettingAngles.getPhiz().getValue())

        self.writeProcessFile(strNewmatFileName, strNewmat)



    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        This method is common to all MOSFLM plugins.
        """
        EDVerbose.DEBUG("EDPluginMOSFLMv10.generateExecutiveSummary")
        if (self.getStringVersion() is not None):
            self.addExecutiveSummaryLine(self.getStringVersion())
