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
__date__ = "20120712"
__status__ = "production"

import os


from EDPluginLabelitv1_1 import EDPluginLabelitv1_1

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataMatrixDouble

from XSDataLabelitv1_1 import XSDataCell
from XSDataLabelitv1_1 import XSDataLabelitScreenSolution
from XSDataLabelitv1_1 import XSDataLabelitScreenOutput
from XSDataLabelitv1_1 import XSDataLabelitMosflmScriptsOutput

class EDPluginLabelitIndexingv1_1(EDPluginLabelitv1_1):
    """
    This plugin runs the labelit.screen command for indexing reference images.
    If the labelit.sceen command is successful, the labelit.mosflm_scripts command is run
    for generating the orientation matrices (in MOSFLM format).
    
    The plugin requires that the path to the Labelit "setpath.sh" script is configured
    using the configuration keyword "pathToLabelitSetpathScript".
    """

    def __init__(self):
        EDPluginLabelitv1_1.__init__(self)
        self.setXSDataInputClass(XSDataString, "forcedSpaceGroup")
        self.__strForcedSpaceGroup = None


    def preProcess(self, _edObject=None):
        """
        Sets up the Labelit command line
        """
        EDPluginLabelitv1_1.preProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitIndexingv1_1.preProcess...")
        self.setScriptExecutable("labelit.screen")
        self.initaliseLabelitCommandLine()
        if self.hasDataInput("forcedSpaceGroup"):
            self.__strForcedSpaceGroup = self.getDataInput("forcedSpaceGroup")[0].getValue()
            if self.__strForcedSpaceGroup != "":
                strScriptCommandline = self.getScriptCommandline()
                self.setScriptCommandline("known_symmetry=%s %s" % (self.__strForcedSpaceGroup, strScriptCommandline))
        self.addListCommandPreExecution("export PYTHONPATH=\"\" ")
        self.addListCommandPreExecution(". %s" % self.getPathToLabelitSetpathScript())
        self.addListCommandPostExecution("[ -f \"LABELIT_possible\" ] && labelit.mosflm_scripts")
        # Force name of log file
        self.setScriptLogFileName(self.compactPluginName(self.getClassName())+".log")


    def postProcess(self, _edObject=None):
        """
        Parses the labelit.screen log file and the generated MOSFLM script
        """
        EDPluginLabelitv1_1.postProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitIndexingv1_1.postProcess...")
        strLabelitLog = self.readProcessLogFile()
        if (strLabelitLog is None):
            strErrorMessage = "EDPluginLabelitIndexingv1_1.postProcess : Could not read the Labelit log file"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataLabelitScreenOutput = self.parseLabelitScreenOutput(strLabelitLog)
            if xsDataLabelitScreenOutput is None:
                strErrorMessage = "EDPluginLabelitIndexingv1_1.postProcess : Cannot parse output"
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                xsDataIntegerSelectedSolutionNumber = xsDataLabelitScreenOutput.getSelectedSolutionNumber()
                if (xsDataIntegerSelectedSolutionNumber is None):
                    strErrorMessage = "EDPluginLabelitIndexingv1_1.postProcess : No selected solution"
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                else:
                    strLabelitMosflmScriptsOutput = self.readProcessFile(self.generateMosflmScriptName(xsDataIntegerSelectedSolutionNumber.getValue()))
                    xsDataLabelitMosflmScriptsOutput = self.parseMosflmScriptsOutput(strLabelitMosflmScriptsOutput)
                    # Path to log file
                    xsDataLabelitScreenOutput.setPathToLogFile(XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))))
                    self.setDataOutput(xsDataLabelitScreenOutput, "labelitScreenOutput")
                    self.setDataOutput(xsDataLabelitMosflmScriptsOutput, "mosflmScriptsOutput")




    def parseLabelitScreenOutput(self, _strLabelitLogText):
        """
        This method parses the labelit.screen log and populates the relevant
        parts of the XSDataLabelitScreenOutput object which is then returned.
        """
        self.DEBUG("EDPluginLabelitIndexingv1_1.parseLabelitLogText")
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
            strErrorMessage = "EDPluginLabelitIndexingv1_1.parseLabelitLogText : Labelit log message: %s" % _strLabelitLogText
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
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

                if (listStringLabelitSolution[0] == ":)"):
                    xsDataLabelitScreenSolution.setHappy(XSDataBoolean(True))
                elif (listStringLabelitSolution[0] == ":("):
                    xsDataLabelitScreenSolution.setHappy(XSDataBoolean(False))
                elif (listStringLabelitSolution[0] == ";("):
                    xsDataLabelitScreenSolution.setHappy(XSDataBoolean(False))
                else:
                    # We have an error...
                    strErrorMessage = "Indexing with labelit.screen failed! Log file:"
                    self.ERROR(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.ERROR(_strLabelitLogText)
                    self.addErrorMessage(_strLabelitLogText)
                    self.setFailure()
                    bContinue = False

                if bContinue:

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

                    strCrystalSystem = listStringLabelitSolution[6]
                    strBravaisLattice = listStringLabelitSolution[7]
                    xsDataLabelitScreenSolution.setCrystalSystem(XSDataString(strCrystalSystem))
                    xsDataLabelitScreenSolution.setBravaisLattice(XSDataString(strBravaisLattice))

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
                            # Check if forced space group
                            if self.__strForcedSpaceGroup == None or self.__strForcedSpaceGroup == "":
                                bFoundSelectedSolution = True
                                xsDataLabelitScreenOutput.setSelectedSolutionNumber(XSDataInteger(iSolutionNumber))
                            else:
                                listBravaisLattice = self.getBravaisLatticeFromSpaceGroup(self.__strForcedSpaceGroup)
                                for strPossibleBravaisLattice in listBravaisLattice:
                                    if strBravaisLattice == strPossibleBravaisLattice:
                                        bFoundSelectedSolution = True
                                        xsDataLabelitScreenOutput.setSelectedSolutionNumber(XSDataInteger(iSolutionNumber))

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
        self.DEBUG("EDPluginLabelitIndexingv1_1.parseMOSFLMMatrices")
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
        self.DEBUG("EDPluginLabelitIndexingv1_1.generateMOSFLMScriptName")
        return "integration%02d.csh" % _iSelectedSolutionNumber


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the Labelit plugin.
        """
        self.DEBUG("EDPluginLabelitIndexingv1_1.generateExecutiveSummary")
        #xsDataInputLabelit = self.getDataInput()
        #xsDataResultLabelit = self.getDataOutput()
        if self.hasDataOutput("labelitScreenOutput"):
            xsDataLabelitScreenOutput = self.getDataOutput("labelitScreenOutput")[0]
            if not self.isFailure():
                self.addExecutiveSummaryLine("Execution of Labelit indexing successful.")
            iIndex = 1
            for xsDataImage in self.getDataInput("referenceImage"):
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







    def getBravaisLatticeFromSpaceGroup(self, _strSpaceGroupName):
        """
        This static method returns a list containing all the two-letter Bravais
        Lattices that corresponds to a given name of the space group. 

        If the space group is not recognised a "None" object is returned.
        
        Only works for protein crystals... 
        From http://strucbio.biologie.uni-konstanz.de/xdswiki/index.php/Old_way_of_Space_group_determination:

            BRAVAIS-            POSSIBLE SPACE-GROUPS FOR PROTEIN CRYSTALS
            TYPE                     [SPACE GROUP NUMBER,SYMBOL]
             aP      [1,P1]
             mP      [3,P2] [4,P2(1)]
            mC,mI    [5,C2]
             oP      [16,P222] [17,P222(1)] [18,P2(1)2(1)2] [19,P2(1)2(1)2(1)]
             oC      [21,C222] [20,C222(1)]
             oF      [22,F222]
             oI      [23,I222] [24,I2(1)2(1)2(1)]
             tP      [75,P4] [76,P4(1)] [77,P4(2)] [78,P4(3)] [89,P422] [90,P42(1)2]
                     [91,P4(1)22] [92,P4(1)2(1)2] [93,P4(2)22] [94,P4(2)2(1)2]
                     [95,P4(3)22] [96,P4(3)2(1)2]
             tI      [79,I4] [80,I4(1)] [97,I422] [98,I4(1)22]
             hP      [143,P3] [144,P3(1)] [145,P3(2)] [149,P312] [150,P321] [151,P3(1)12]
                     [152,P3(1)21] [153,P3(2)12] [154,P3(2)21] [168,P6] [169,P6(1)]
                     [170,P6(5)] [171,P6(2)] [172,P6(4)] [173,P6(3)] [177,P622]
                     [178,P6(1)22] [179,P6(5)22] [180,P6(2)22] [181,P6(4)22] [182,P6(3)22]
             hR      [146,R3] [155,R32]
             cP      [195,P23] [198,P2(1)3] [207,P432] [208,P4(2)32] [212,P4(3)32]
                     [213,P4(1)32]
             cF      [196,F23] [209,F432] [210,F4(1)32]
             cI      [197,I23] [199,I2(1)3] [211,I432] [214,I4(1)32]

        """
        strBravaisLattice = None
        strSpaceGroupName = _strSpaceGroupName.upper()
        
        if strSpaceGroupName in ["P1"]:
            listBravaisLattice = ["aP"]

        elif strSpaceGroupName in ["P2", "P21"]:
            listBravaisLattice = ["mP"]

        elif strSpaceGroupName in ["C2"]:
            listBravaisLattice = ["mC", "mI"]

        elif strSpaceGroupName in ["P222", "P2221", "P21212", "P212121"]:
            listBravaisLattice = ["oP"]

        elif strSpaceGroupName in ["C222", "C2221"]:
            listBravaisLattice = ["oA", "oB", "oC", "oS"]

        elif strSpaceGroupName in ["F222"]:
            listBravaisLattice = ["oF"]

        elif strSpaceGroupName in ["I222", "I212121"]:
            listBravaisLattice = ["oI"]

        elif strSpaceGroupName in ["P4", "P41", "P42", "P43", "P422", "P4212", "P4122", "P41212", "P4222", "P42212", "P4322", "P43212"]:
            listBravaisLattice = ["tP", "tC"]

        elif strSpaceGroupName in ["I4", "I41", "I422", "I4122"]:
            listBravaisLattice = ["tI", "tF"]

        elif strSpaceGroupName in ["P3", "P31", "P32", "P312", "P321", "P3112", "P3121", "P3212", "P3221", "P6", "P61", "P65", \
                                    "P62", "P64", "P63", "P622", "P6122", "P6522", "P6222", "P6422", "P6322"]:
            listBravaisLattice = ["hP"]

        elif strSpaceGroupName in ["H3", "R3", "H32", "R32"]:
            listBravaisLattice = ["hR"]

        elif strSpaceGroupName in ["P23", "P213", "P432", "P4232", "P4332", "P4132"]:
            listBravaisLattice = ["cP"]

        elif strSpaceGroupName in ["F23", "F432", "F4132"]:
            listBravaisLattice = ["cF"]

        elif strSpaceGroupName in ["I23", "I213", "I432", "I4132"]:
            listBravaisLattice = ["cI"]

        return listBravaisLattice

