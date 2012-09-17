#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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
__date__ = "20120712"
__status__ = "deprecated"



from EDConfiguration           import EDConfiguration
from EDMessage                 import EDMessage
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSPluginItem

from XSDataLabelitv10 import XSDataCell
from XSDataLabelitv10 import XSDataInputLabelit
from XSDataLabelitv10 import XSDataResultLabelit
from XSDataLabelitv10 import XSDataLabelitScreenSolution
from XSDataLabelitv10 import XSDataLabelitScreenOutput
from XSDataLabelitv10 import XSDataLabelitMosflmScriptsOutput

class EDPluginLabelitv10(EDPluginExecProcessScript):
    """
    This plugin runs the labelit.screen command for indexing reference images.
    If the labelit.sceen command is successful, the labelit.mosflm_scripts command is run
    for generating the orientation matrices (in MOSFLM format).
    
    The plugin requires that the path to the Labelit "setpath.sh" script is configured
    using the configuration keyword "pathToLabelitSetpathScript".
    """

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputLabelit)
        self.strCONF_PATH_TO_LABELIT_SETPATH_SCRIPT = "pathToLabelitSetpathScript"
        self.strPathToLabelitSetpathScript = None


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginControlLabelitv10.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            self.warning("EDPluginControlLabelitv10.configure: No Labelit plugin item defined.")
            xsPluginItem = XSPluginItem()
        strPathToLabelitSetpathScript = EDConfiguration.getStringParamValue(xsPluginItem, self.strCONF_PATH_TO_LABELIT_SETPATH_SCRIPT)
        if(strPathToLabelitSetpathScript == None):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlLabelitv10.configure', self.getClassName(), "Configuration parameter missing: " + self.strCONF_PATH_TO_LABELIT_SETPATH_SCRIPT)
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage
        else:
            self.setPathToLabelitSetpathScript(strPathToLabelitSetpathScript)


    def setPathToLabelitSetpathScript(self, _strPathToLabelitSetpathScript):
        self.strPathToLabelitSetpathScript = _strPathToLabelitSetpathScript


    def getPathToLabelitSetpathScript(self):
        return self.strPathToLabelitSetpathScript


    def preProcess(self, _edObject=None):
        """
        Sets up the Labelit command line
        """
        EDPluginExecProcessScript.preProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitv10.preProcess...")

        self.setScriptExecutable("labelit.screen")

        self.initaliseLabelitCommandLine()

        self.addListCommandPreExecution("export PYTHONPATH=\"\" ")
        self.addListCommandPreExecution(". %s" % self.getPathToLabelitSetpathScript())

        self.addListCommandPostExecution("[ -f \"LABELIT_possible\" ] && labelit.mosflm_scripts")


    def postProcess(self, _edObject=None):
        """
        Parses the labelit.screen log file and the generated MOSFLM script
        """
        EDPluginExecProcessScript.postProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitv10.postProcess...")
        strLabelitLog = self.readProcessLogFile()
        if (strLabelitLog is None):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginLabelitv10.postProcess", self.getClassName(), "Could not read the Labelit log file")
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
        else:
            xsDataLabelitScreenOutput = self.parseLabelitScreenOutput(strLabelitLog)
            xsDataIntegerSelectedSolutionNumber = xsDataLabelitScreenOutput.getSelectedSolutionNumber()
            if (xsDataIntegerSelectedSolutionNumber is None):
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginLabelitv10.postProcess", self.getClassName(), "No selected solution")
                self.error(errorMessage)
                self.addErrorMessage(errorMessage)
            else:
                strLabelitMosflmScriptsOutput = self.readProcessFile(self.generateMosflmScriptName(xsDataIntegerSelectedSolutionNumber.getValue()))
                xsDataLabelitMosflmScriptsOutput = self.parseMosflmScriptsOutput(strLabelitMosflmScriptsOutput)
                xsDataResultLabelit = XSDataResultLabelit()
                xsDataResultLabelit.setLabelitScreenOutput(xsDataLabelitScreenOutput)
                xsDataResultLabelit.setLabelitMosflmScriptsOutput(xsDataLabelitMosflmScriptsOutput)
                self.setDataOutput(xsDataResultLabelit)


    def initaliseLabelitCommandLine(self):
        """
        Initialises the Labelit.screen command line
        """
        self.DEBUG("EDPluginLabelitv10.initaliseLabelitCommandLine")

        strCommandLabelit = "--index_only"
        xsDataInputLabelit = self.getDataInput()
        xsDataImageList = xsDataInputLabelit.getImage()
        for xsDataImage in xsDataImageList:
            strCommandLabelit = strCommandLabelit + " " + xsDataImage.getPath().getValue()
        self.setScriptCommandline(strCommandLabelit)


    def parseLabelitScreenOutput(self, _strLabelitLogText):
        """
        This method parses the labelit.screen log and populates the relevant
        parts of the XSDataLabelitScreenOutput object which is then returned.
        """
        self.DEBUG("EDPluginLabelitv10.parseLabelitLogText")
        xsDataLabelitScreenOutput = None

        iIndex = 0
        listLogLines = _strLabelitLogText.split('\n')
        bFoundLabelitIndexingResults = False
        bContinue = True

        while (bContinue) :
            if (listLogLines[ iIndex ].find("LABELIT Indexing results:") != -1) :
                bFoundLabelitIndexingResults = True
                bContinue = False
            else:
                if (iIndex < (len(listLogLines) - 2)):
                    iIndex += 1
                else:
                    bContinue = False

        if (bFoundLabelitIndexingResults == False):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ("EDPluginLabelitv10.parseLabelitLogText", self.getClassName(), "Labelit log message: %s" % _strLabelitLogText)
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
        else:
            # We found some indexing results!
            xsDataLabelitScreenOutput = XSDataLabelitScreenOutput()

            iIndex += 1
            strBeamDistanceMosaicity = listLogLines[ iIndex ]
            strBeamDistanceMosaicity = strBeamDistanceMosaicity.replace(',', '')
            strBeamDistanceMosaicity = strBeamDistanceMosaicity.replace('mm', ' ')
            strBeamDistanceMosaicity = strBeamDistanceMosaicity.replace('=', ' ')
            listStringBeamDistanceMosaicity = strBeamDistanceMosaicity.split()

            fBeamX = float(listStringBeamDistanceMosaicity[3])
            fBeamY = float(listStringBeamDistanceMosaicity[5])
            xsDataLabelitScreenOutput.setBeamCentreX(XSDataLength(fBeamX))
            xsDataLabelitScreenOutput.setBeamCentreY(XSDataLength(fBeamY))
            fDistance = float(listStringBeamDistanceMosaicity[7])
            xsDataLabelitScreenOutput.setDistance(XSDataLength(fDistance))

            fMosaicity = float(listStringBeamDistanceMosaicity[11])
            xsDataLabelitScreenOutput.setMosaicity(XSDataAngle(fMosaicity))

            iIndex += 3
            bContinue = True
            bFoundSelectedSolution = False
            while (bContinue):
                xsDataLabelitScreenSolution = XSDataLabelitScreenSolution()
                strLabelitSolution = listLogLines[ iIndex ]
                listStringLabelitSolution = strLabelitSolution.split()

                if listStringLabelitSolution[0] == ":)" :
                    xsDataLabelitScreenSolution.setHappy(XSDataBoolean(True))
                else:
                    xsDataLabelitScreenSolution.setHappy(XSDataBoolean(False))

                iSolutionNumber = int(listStringLabelitSolution[1])
                xsDataLabelitScreenSolution.setSolutionNumber(XSDataInteger(iSolutionNumber))

                fMetricFitValue = float(listStringLabelitSolution[2])
                xsDataLabelitScreenSolution.setMetricFitValue(XSDataDouble(fMetricFitValue))

                strMetricFitCode = listStringLabelitSolution[3]
                xsDataLabelitScreenSolution.setMetricFitCode(XSDataString(strMetricFitCode))

                fRMSD = float(listStringLabelitSolution[4])
                xsDataLabelitScreenSolution.setRmsd(XSDataLength(fRMSD))

                iNumberOfSpots = int(listStringLabelitSolution[5])
                xsDataLabelitScreenSolution.setNumberOfSpots(XSDataInteger(iNumberOfSpots))

                xsDataLabelitScreenSolution.setCrystalSystem(XSDataString(listStringLabelitSolution[6]))
                xsDataLabelitScreenSolution.setBravaisLattice(XSDataString(listStringLabelitSolution[7]))

                xsDataCell = XSDataCell()
                xsDataCell.setLength_a(XSDataLength(float(listStringLabelitSolution[ 8])))
                xsDataCell.setLength_b(XSDataLength(float(listStringLabelitSolution[ 9])))
                xsDataCell.setLength_c(XSDataLength(float(listStringLabelitSolution[10])))
                xsDataCell.setAngle_alpha(XSDataAngle(float(listStringLabelitSolution[11])))
                xsDataCell.setAngle_beta(XSDataAngle(float(listStringLabelitSolution[12])))
                xsDataCell.setAngle_gamma(XSDataAngle(float(listStringLabelitSolution[13])))
                xsDataLabelitScreenSolution.setUnitCell(xsDataCell)

                iVolume = int(listStringLabelitSolution[14])
                xsDataLabelitScreenSolution.setVolume(XSDataInteger(iVolume))

                # Find the selected solution
                if (bFoundSelectedSolution == False):
                    if (xsDataLabelitScreenSolution.getHappy().getValue() == True):
                        xsDataLabelitScreenOutput.setSelectedSolutionNumber(XSDataInteger(iSolutionNumber))
                        bFoundSelectedSolution = True


                xsDataLabelitScreenOutput.addLabelitScreenSolution(xsDataLabelitScreenSolution)
                if (iIndex < (len(listLogLines) - 2)):
                    iIndex += 1
                else:
                    bContinue = False


        return xsDataLabelitScreenOutput


    def parseMosflmScriptsOutput(self, _strMOSFLMScript):
        """
        This method parses the MOSFLM script generated by Labelit and populates
        the A- and U-matrices in the XSDataLabelitMosflmScriptsOutput object.
        """
        self.DEBUG("EDPluginLabelitv10.parseMOSFLMMatrices")
        xsDataLabelitMosflmScriptsOutput = XSDataLabelitMosflmScriptsOutput()
        listMOSFLMScriptLines = _strMOSFLMScript.split("\n")

        XSDataMatrixDoubleA = XSDataMatrixDouble()
        # Fix for bug 315: it's not enough to just spit the lines
        listMOSFLMScriptLine2 = [ listMOSFLMScriptLines[2][0:12],
                                    listMOSFLMScriptLines[2][12:24],
                                    listMOSFLMScriptLines[2][24:] ]
        listMOSFLMScriptLine3 = [ listMOSFLMScriptLines[3][0:12],
                                    listMOSFLMScriptLines[3][12:24],
                                    listMOSFLMScriptLines[3][24:] ]
        listMOSFLMScriptLine4 = [ listMOSFLMScriptLines[4][0:12],
                                    listMOSFLMScriptLines[4][12:24],
                                    listMOSFLMScriptLines[4][24:] ]
        XSDataMatrixDoubleA.setM11(float(listMOSFLMScriptLine2[0]))
        XSDataMatrixDoubleA.setM12(float(listMOSFLMScriptLine2[1]))
        XSDataMatrixDoubleA.setM13(float(listMOSFLMScriptLine2[2]))
        XSDataMatrixDoubleA.setM21(float(listMOSFLMScriptLine3[0]))
        XSDataMatrixDoubleA.setM22(float(listMOSFLMScriptLine3[1]))
        XSDataMatrixDoubleA.setM23(float(listMOSFLMScriptLine3[2]))
        XSDataMatrixDoubleA.setM31(float(listMOSFLMScriptLine4[0]))
        XSDataMatrixDoubleA.setM32(float(listMOSFLMScriptLine4[1]))
        XSDataMatrixDoubleA.setM33(float(listMOSFLMScriptLine4[2]))
        xsDataLabelitMosflmScriptsOutput.setAMatrix(XSDataMatrixDoubleA)

        XSDataMatrixDoubleU = XSDataMatrixDouble()
        listMOSFLMScriptLine6 = [ listMOSFLMScriptLines[6][0:12],
                                    listMOSFLMScriptLines[6][12:24],
                                    listMOSFLMScriptLines[6][24:] ]
        listMOSFLMScriptLine7 = [ listMOSFLMScriptLines[7][0:12],
                                    listMOSFLMScriptLines[7][12:24],
                                    listMOSFLMScriptLines[7][24:] ]
        listMOSFLMScriptLine8 = [ listMOSFLMScriptLines[8][0:12],
                                    listMOSFLMScriptLines[8][12:24],
                                    listMOSFLMScriptLines[8][24:] ]
        XSDataMatrixDoubleU.setM11(float(listMOSFLMScriptLine6[0]))
        XSDataMatrixDoubleU.setM12(float(listMOSFLMScriptLine6[1]))
        XSDataMatrixDoubleU.setM13(float(listMOSFLMScriptLine6[2]))
        XSDataMatrixDoubleU.setM21(float(listMOSFLMScriptLine7[0]))
        XSDataMatrixDoubleU.setM22(float(listMOSFLMScriptLine7[1]))
        XSDataMatrixDoubleU.setM23(float(listMOSFLMScriptLine7[2]))
        XSDataMatrixDoubleU.setM31(float(listMOSFLMScriptLine8[0]))
        XSDataMatrixDoubleU.setM32(float(listMOSFLMScriptLine8[1]))
        XSDataMatrixDoubleU.setM33(float(listMOSFLMScriptLine8[2]))
        xsDataLabelitMosflmScriptsOutput.setUMatrix(XSDataMatrixDoubleU)

        return xsDataLabelitMosflmScriptsOutput


    def generateMosflmScriptName(self, _iSelectedSolutionNumber):
        """
        This method generates the name of the MOSFLM script given a solution number.
        """
        self.DEBUG("EDPluginLabelitv10.generateMOSFLMScriptName")
        return "integration%02d.csh" % _iSelectedSolutionNumber


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the Labelit plugin.
        """
        self.DEBUG("EDPluginLabelitv10.generateExecutiveSummary")
        xsDataInputLabelit = self.getDataInput()
        xsDataResultLabelit = self.getDataOutput()
        xsDataLabelitScreenOutput = xsDataResultLabelit.getLabelitScreenOutput()
        if not self.isFailure():
            self.addExecutiveSummaryLine("Execution of Labelit indexing successful.")
        iIndex = 1
        for xsDataImage in xsDataInputLabelit.getImage():
            self.addExecutiveSummaryLine("Image %d                : %s" % (iIndex, xsDataImage.getPath().getValue()))
            iIndex += 1
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("Labelit Indexing results:")
        self.addExecutiveSummaryLine("Beam centre             : x=%5.1f mm, y=%5.1f mm" % \
                                      (xsDataLabelitScreenOutput.getBeamCentreX().getValue(), \
                                        xsDataLabelitScreenOutput.getBeamCentreY().getValue()))
        self.addExecutiveSummaryLine("Distance                : %5.1f mm" % xsDataLabelitScreenOutput.getDistance().getValue())
        self.addExecutiveSummaryLine("Mosaicity               : %5.2f degrees" % xsDataLabelitScreenOutput.getMosaicity().getValue())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("Solution  Metric fit  rmsd  #spots  crystal_system   unit_cell                                  volume")
        for xsDataLabelitScreenSolution in xsDataLabelitScreenOutput.getLabelitScreenSolution():
            strSmiley = None
            if (xsDataLabelitScreenSolution.getHappy().getValue() == True):
                strSmiley = ":)"
            else:
                strSmiley = ";("
            self.addExecutiveSummaryLine("%2s %3d %10.4f %2s %5.3f %6d %13s %2s  %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %8d" % (\
                                                           strSmiley, \
                                                           xsDataLabelitScreenSolution.getSolutionNumber().getValue(), \
                                                           xsDataLabelitScreenSolution.getMetricFitValue().getValue(), \
                                                           xsDataLabelitScreenSolution.getMetricFitCode().getValue(), \
                                                           xsDataLabelitScreenSolution.getRmsd().getValue(), \
                                                           xsDataLabelitScreenSolution.getNumberOfSpots().getValue(), \
                                                           xsDataLabelitScreenSolution.getCrystalSystem().getValue(), \
                                                           xsDataLabelitScreenSolution.getBravaisLattice().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getLength_a().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getLength_b().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getLength_c().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getAngle_alpha().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getAngle_beta().getValue(), \
                                                           xsDataLabelitScreenSolution.getUnitCell().getAngle_gamma().getValue(), \
                                                           xsDataLabelitScreenSolution.getVolume().getValue(), \
                                                           ))








