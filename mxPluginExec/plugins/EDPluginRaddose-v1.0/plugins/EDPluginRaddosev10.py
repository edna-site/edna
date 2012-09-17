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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os


from EDMessage                    import EDMessage
from EDPluginExecProcessScript    import EDPluginExecProcessScript

from XSDataCommon                 import XSDataAbsorbedDoseRate
from XSDataCommon                 import XSDataDouble
from XSDataCommon                 import XSDataTime
from XSDataCommon                 import XSDataFile
from XSDataCommon                 import XSDataString

from XSDataRaddosev10             import XSDataRaddoseInput
from XSDataRaddosev10             import XSDataRaddoseOutput



class EDPluginRaddosev10(EDPluginExecProcessScript):
    """
    """

    # Depending on RADDOSE version, Absorbed keyword in the log file is different
    # in Raddose 1: (actually no version stamped for Raddose coming with ccp4 4.2) keyword is "Dose in Grays"
    # in Raddose 2: keyword is "Total absorbed dose (Gy)"
    __listABSORBED_DOSE = [ "Dose in Grays", "Total absorbed dose (Gy)" ]
    __strSOLVENT = "Solvent Content (%)"
    __iMIN_SOLVENT_PERCENTAGE = 25
    __iMAX_SOLVENT_PERCENTAGE = 75
    __fHENDERSON_LIMIT = 2e7

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.__strCommandBeamSize = None
        self.__strCommandBeamFlux = None
        self.__strCommandBeamWavelength = None

        self.__strCommandCrystalSize = None
        self.__strCommandCrystalCell = None
        self.__strCommandCrystalNRES = None
        self.__strCommandCrystalNMON = None
        self.__strCommandCrystalNDNA = None
        self.__strCommandCrystalNRNA = None
        self.__strCommandCrystalPATM = None
        self.__strCommandCrystalSATM = None

        self.__strCommandExposureTime = None
        self.__strCommandImages = None

        self.__listCommandsRaddose = []

        self.__dictResults = {}

        # ugly workaround while waiting for RADDOSE XML output file
        for strAbsorbedDoseKeyword in EDPluginRaddosev10.__listABSORBED_DOSE:
            self.__dictResults[ strAbsorbedDoseKeyword ] = None

        self.__dictResults[ EDPluginRaddosev10.__strSOLVENT ] = None

        self.__fSolvent = None
        self.__fTimeToReachHendersonLimit = None

        self.setXSDataInputClass(XSDataRaddoseInput)


    def getCommandCrystalSize(self):
        return self.__strCommandCrystalSize


    def getCommandCrystalCell(self):
        return self.__strCommandCrystalCell


    def getCommandCrystalNRES(self):
        return self.__strCommandCrystalNRES


    def getCommandCrystalNMON(self):
        return self.__strCommandCrystalNMON


    def getCommandCrystalNDNA(self):
        return self.__strCommandCrystalNDNA


    def getCommandCrystalNRNA(self):
        return self.__strCommandCrystalNRNA


    def getCommandCrystalPATM(self):
        return self.__strCommandCrystalPATM


    def getCommandCrystalSATM(self):
        return self.__strCommandCrystalSATM


    def getCommandBeamSize(self):
        return self.__strCommandBeamSize


    def getCommandBeamWavelength(self):
        return self.__strCommandBeamWavelength


    def getCommandBeamFlux(self):
        return self.__strCommandBeamFlux


    def getCommandExposureTime(self):
        return self.__strCommandExposureTime


    def getCommandImages(self):
        return self.__strCommandImages


    def getListCommandsRaddose(self):
        return self.__listCommandsRaddose


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginRaddosev10.configure")
        self.setRequireCCP4(True)


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginRaddosev10.preProcess")
        self.setScriptLogFileName("raddose.log")
        # Fix for bug 432: if flux is close to zero or negative failure
        if (self.getDataInput().getBeamFlux().getValue() < 0.1):
            strErrorMessage = "EDPluginRaddosev10.preProcess ERROR: Input flux is negative or close to zero. Execution of characterisation aborted."
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            self.initializeCommandExecution()


    def initializeCommandExecution(self):
        self.__strCommandBeamSize = self.sizeToCommand(self.getDataInput().getBeamSize(), "BEAM")
        self.addListCommandExecution (self.__strCommandBeamSize)
        self.__strCommandBeamFlux = self.singleValueToCommand(self.getDataInput().getBeamFlux(), "PHOSEC")
        self.addListCommandExecution(self.__strCommandBeamFlux)
        self.__strCommandBeamWavelength = self.singleValueToCommand(self.getDataInput().getBeamWavelength(), "WAVELENGTH")
        self.addListCommandExecution(self.__strCommandBeamWavelength)

        self.__strCommandCrystalSize = self.sizeToCommand(self.getDataInput().getCrystalSize(), "CRYSTAL")
        self.addListCommandExecution(self.__strCommandCrystalSize)
        self.__strCommandCrystalNRES = self.singleValueToCommand(self.getDataInput().getCrystalNRES(), "NRES")
        self.addListCommandExecution(self.__strCommandCrystalNRES)
        self.__strCommandCrystalNMON = self.singleValueToCommand(self.getDataInput().getCrystalNMON(), "NMON")
        self.addListCommandExecution(self.__strCommandCrystalNMON)
        self.__strCommandCrystalNDNA = self.singleValueToCommand(self.getDataInput().getCrystalNDNA(), "NDNA")
        self.addListCommandExecution(self.__strCommandCrystalNDNA)
        self.__strCommandCrystalNRNA = self.singleValueToCommand(self.getDataInput().getCrystalNRNA(), "NRNA")
        self.addListCommandExecution(self.__strCommandCrystalNRNA)
        self.__strCommandCrystalPATM = self.atomCompositionToCommand(self.getDataInput().getCrystalPATM(), "PATM")
        self.addListCommandExecution(self.__strCommandCrystalPATM)
        self.__strCommandCrystalSATM = self.atomCompositionToCommand(self.getDataInput().getCrystalSATM(), "SATM")
        self.addListCommandExecution(self.__strCommandCrystalSATM)
        self.__strCommandCrystalCell = self.cellToCommand(self.getDataInput().getCrystalCell(), "CELL")
        self.addListCommandExecution(self.__strCommandCrystalCell)

        self.__strCommandExposureTime = self.singleValueToCommand(self.getDataInput().getBeamExposureTime(), "EXPOSURE")
        self.addListCommandExecution(self.__strCommandExposureTime)
        self.__strCommandImages = self.singleValueToCommand(self.getDataInput().getNumberOfImages(), "IMAGES")
        self.addListCommandExecution(self.__strCommandImages)

        self.addListCommandExecution("END")



    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)

        strRaddoseError = self.readProcessErrorLogFile()
        if((strRaddoseError is not None) and (strRaddoseError != "")):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginRaddosev10.postProcess', 'EDPluginRaddosev10', strRaddoseError)
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage

        resultDict = self.analyseScriptLogFileName(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))

        strSolvent = self.__dictResults[ EDPluginRaddosev10.__strSOLVENT ]

        # ugly workaround while waiting for RADDOSE XML output file
        strAbsorbedDose = None
        for strAbsorbedDoseKeyword in EDPluginRaddosev10.__listABSORBED_DOSE:
            strAbsorbedDose = self.__dictResults[ strAbsorbedDoseKeyword ]
            if (strAbsorbedDose is not None):
                break

        if(strSolvent is None):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginRaddosev10.postProcess', "Raddose", "No Result for Keyword [" + EDPluginRaddosev10.__strSOLVENT + "] see: " + self.getScriptLogFileName())
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage

        if(strAbsorbedDose is None):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginRaddosev10.postProcess', "Raddose", "No Result for Keyword [" + strAbsorbedDoseKeyword + "] see: " + self.getScriptLogFileName())
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage


        self.__fSolvent = float(strSolvent)
        if(self.__fSolvent < EDPluginRaddosev10.__iMIN_SOLVENT_PERCENTAGE or self.__fSolvent > EDPluginRaddosev10.__iMAX_SOLVENT_PERCENTAGE):
            warningMessage = "Inconsistent solvent percentage value: %.1f" % self.__fSolvent
            self.warning(warningMessage)
            self.addWarningMessage(warningMessage)

        iNumberOfImages = self.getDataInput().getNumberOfImages().getValue()
        fExposureTimePerImageInSec = self.getDataInput().getBeamExposureTime().getValue()
        fTotalExposureTime = iNumberOfImages * fExposureTimePerImageInSec
        fAbsorbedDoseSpeed = float(strAbsorbedDose) / fTotalExposureTime
        xsDataAbsorbedDoseRate = XSDataAbsorbedDoseRate(fAbsorbedDoseSpeed)

        xsDataAbsorbedDose = XSDataDouble(float(strAbsorbedDose))

        self.__fTimeToReachHendersonLimit = EDPluginRaddosev10.__fHENDERSON_LIMIT / fAbsorbedDoseSpeed

        xsDataRaddosev10Output = XSDataRaddoseOutput()
        xsDataRaddosev10Output.setAbsorbedDose(xsDataAbsorbedDose)
        xsDataRaddosev10Output.setAbsorbedDoseRate(xsDataAbsorbedDoseRate)
        xsDataRaddosev10Output.setTimeToReachHendersonLimit(XSDataTime(self.__fTimeToReachHendersonLimit))

        xsDataFilePathToLog = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())))
        xsDataRaddosev10Output.setPathToLogFile(xsDataFilePathToLog)

        self.setDataOutput(xsDataRaddosev10Output)


    def analyseScriptLogFileName(self, _strFileName):
        resultDict = None

        f = None
        try:
            f = open(_strFileName)
        except:
            errorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ('EDPluginRaddosev10.analyseScriptLogFileName', self.getScriptLogFileName())
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage

        for strLine in f.xreadlines():
            strLine = strLine.replace('\n', "")
            resultDict = self.addResultToDict(strLine)

        return resultDict


    def addResultToDict(self, _strLine):
        for strKey in self.__dictResults.keys():
            if (_strLine.find(strKey) != -1) :
                tokenList = _strLine.split(" ")
                value = tokenList[-1]
                self.__dictResults[ strKey ] = value

        return self.__dictResults


    def checkParameters(self):
        """
        Checks the data input object
        """

        EDPluginExecProcessScript.checkParameters(self)
        # Checks the mandatory parameters:

        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getCrystalCell(), "crystalCell")
        self.checkMandatoryParameters(self.getDataInput().getBeamWavelength(), "beamWavelength")
        self.checkMandatoryParameters(self.getDataInput().getBeamFlux(), "beamFlux")
        self.checkMandatoryParameters(self.getDataInput().getBeamSize(), "beamSize")

        #self.checkMandatoryParameters( self.getDataInput().getCrystalSize(), "crystalSize")
        # Default is 0.1 0.1 0.1

        # Default is 0.1 0.1
        # self.checkMandatoryParameters( self.getDataInput().getBeamExposureTime(), "beamExposureTime")
        # self.checkMandatoryParameters( self.getDataInput().getNumberOfImages(), "numberOfImages")

        self.checkImportantParameters(self.getDataInput().getCrystalNMON(), "NMON (Check your Crystal chemical composition consistency)")


    def singleValueToCommand(self, _xsSimpleObject, _strKeyword):
        strCommand = None
        if(_xsSimpleObject is not None):
            strCommand = _strKeyword
            strValue = str(_xsSimpleObject.getValue())
            strCommand = strCommand + " " + strValue

        return strCommand


    def atomCompositionToCommand(self, _xsAtomComposition, _strKeyword):
        strCommand = None
        if(_xsAtomComposition is not None):
            strCommand = _strKeyword
            pyListAtom = _xsAtomComposition.getAtom()

            for xsDataAtom in pyListAtom:
                strAtomSymbol = xsDataAtom.getSymbol().getValue()
                strAtomAmount = None
                if(xsDataAtom.getNumberOf() is not None):
                    strAtomAmount = str(xsDataAtom.getNumberOf().getValue())
                elif(xsDataAtom.getConcentration() is not None):
                    strAtomAmount = str(xsDataAtom.getConcentration().getValue())
                strCommand = strCommand + " " + strAtomSymbol + " " + strAtomAmount

        return strCommand


    def sizeToCommand(self, _xsSize, _strKeyword):
        strCommand = None
        if(_xsSize is not None):
            strCommand = _strKeyword
            strX = str(_xsSize.getX().getValue())
            strY = str(_xsSize.getY().getValue())

            strZ = None
            # if it is a 3D object
            if(_xsSize.getZ() is not None):
                strZ = str(_xsSize.getZ().getValue())

            strCommand = strCommand + " " + strX + " " + strY

            if(strZ is not None):
                strCommand = strCommand + " " + strZ

        return strCommand


    def cellToCommand(self, _xsCell, _strKeyword):
        strCommand = None
        if(_xsCell is not None):
            strCommand = _strKeyword
            strA = str(_xsCell.getLength_a().getValue())
            strB = str(_xsCell.getLength_b().getValue())
            strC = str(_xsCell.getLength_c().getValue())
            strAlpha = str(_xsCell.getAngle_alpha().getValue())
            strBeta = str(_xsCell.getAngle_beta().getValue())
            strGamma = str(_xsCell.getAngle_gamma().getValue())

            strCommand = strCommand + " " + strA + " " + strB + " " + strC + " " + strAlpha + " " + strBeta + " " + strGamma

        return strCommand


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginRaddosev10.generateExecutiveSummary")
        if (self.getStringVersion() is not None):
            self.addExecutiveSummaryLine(self.getStringVersion())
        xsDataRaddoseInput = self.getDataInput()
        xsDataRaddoseOutput = self.getDataOutput()
        self.addExecutiveSummaryLine("Execution of radiation dose estimation successful.")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("Flux                            : %21.2g [photons/s]" % xsDataRaddoseInput.getBeamFlux().getValue())
        if(xsDataRaddoseInput.getCrystalSize() is not None):
            self.addExecutiveSummaryLine("Crystal size                    : %.3f x %.3f x %.3f [mm]" % (xsDataRaddoseInput.getCrystalSize().getX().getValue(), \
                                                                                              xsDataRaddoseInput.getCrystalSize().getY().getValue(), \
                                                                                              xsDataRaddoseInput.getCrystalSize().getZ().getValue()))
        else:
            self.addExecutiveSummaryLine("Crystal size                    : 0.100 x 0.100 x 0.100 [mm] (not set, taking default)")
        self.addExecutiveSummaryLine("Beam size                       :         %.3f x %.3f [mm]" % (xsDataRaddoseInput.getBeamSize().getX().getValue(), \
                                                                                   xsDataRaddoseInput.getBeamSize().getY().getValue()))
        self.addExecutiveSummaryLine("Solvent                         : %21.2f [%%]" % self.__fSolvent)
        self.addExecutiveSummaryLine("Dose rate                       : %21.2g [Grays/s]" % xsDataRaddoseOutput.getAbsorbedDoseRate().getValue())
        self.addExecutiveSummaryLine("Time to reach Henderson limit   : %21.2g [s]" % self.__fTimeToReachHendersonLimit)

