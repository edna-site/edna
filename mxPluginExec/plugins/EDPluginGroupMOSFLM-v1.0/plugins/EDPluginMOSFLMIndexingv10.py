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

from EDUtilsTable      import EDUtilsTable
from EDPluginMOSFLMv10 import EDPluginMOSFLMv10

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataMOSFLMv10 import XSDataCell
from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
from XSDataMOSFLMv10 import XSDataMOSFLMInputIndexing
from XSDataMOSFLMv10 import XSDataMOSFLMIndexingSolution
from XSDataMOSFLMv10 import XSDataMOSFLMOutputIndexing

from XSDataDnaTables import dna_tables


class EDPluginMOSFLMIndexingv10(EDPluginMOSFLMv10):


    def __init__(self):
        EDPluginMOSFLMv10.__init__(self)
        self.setXSDataInputClass(XSDataMOSFLMInputIndexing)


    def preProcess(self, _edObject=None):
        EDPluginMOSFLMv10.preProcess(self)
        self.DEBUG("EDPluginMOSFLMIndexingv10.preProcess")
        self.generateMOSFLMCommands()


    def finallyProcess(self, _edObject=None):
        EDPluginMOSFLMv10.finallyProcess(self)
        self.DEBUG("EDPluginMOSFLMIndexingv10.finallyProcess")
        xsDataMOSFLMOutputIndexing = self.createDataMOSFLMOutputIndexing()
        self.setDataOutput(xsDataMOSFLMOutputIndexing)


    def configure(self):
        EDPluginMOSFLMv10.configure(self)
        self.DEBUG("EDPluginMOSFLMIndexingv10.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            self.DEBUG("EDPluginMOSFLMIndexingv10.configure: xsPluginItem is None")


    def checkParameters(self):
        """
        Checks the mandatory parameters for MOSLFM indexing
        """
        EDPluginMOSFLMv10.checkParameters(self)
        self.DEBUG("EDPluginMOSFLMIndexingv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "image")


    def generateMOSFLMCommands(self):
        """
        This method creates a list of MOSFLM indexing commands given a valid
        XSDataMOSFLMIndexingingInput as self.getDataInput()
        """
        EDPluginMOSFLMv10.generateMOSFLMCommands(self)
        self.DEBUG("EDPluginMOSFLMIndexingv10.generateMOSFLMCommands")

        xsDataMOSFLMIndexingInput = self.getDataInput()

        if (xsDataMOSFLMIndexingInput != None):

            self.addListCommandExecution("NEWMAT " + self.getNewmatFileName())

            xsDataMOSFLMImageList = xsDataMOSFLMIndexingInput.getImage()
            for xsDataMOSFLMImage in xsDataMOSFLMImageList:
                iImageNumber = xsDataMOSFLMImage.getNumber().getValue()
                fRotationAxisStart = xsDataMOSFLMImage.getRotationAxisStart().getValue()
                fRotationAxisEnd = xsDataMOSFLMImage.getRotationAxisEnd().getValue()
                self.addListCommandExecution("AUTOINDEX DPS REFINE IMAGE " + str(iImageNumber) + " " \
                                                     "PHI " + str(fRotationAxisStart) + " " + str(fRotationAxisEnd))
            self.addListCommandExecution("GO")
            for xsDataImage in xsDataMOSFLMImageList:
                self.addListCommandExecution("MOSAIC ESTIMATE %d" % xsDataImage.getNumber().getValue())
                self.addListCommandExecution("GO")

#            strPrefix = strTemplate.split("#")[0][:-1]
#            strGenFileName = strPrefix + ".gen"
#            strSptFileName = strPrefix + ".spt"
        # Force name of log file
        self.setScriptLogFileName(self.compactPluginName(self.getClassName())+".log")

        self.DEBUG("Finished EDPluginMOSFLMIndexingv10.generateMOSFLMIndexingCommands")


    def createDataMOSFLMOutputIndexing(self):
        self.DEBUG("EDPluginMOSFLMIndexingv10.createDataMOSFLMOutputIndexing")
        xsDataMOSFLMOutputIndexing = XSDataMOSFLMOutputIndexing()
        # Read Newmat file
        xsDataMOSFLMNewmat = self.getDataMOSFLMNewmat()
        if (xsDataMOSFLMNewmat is None):
            strError = "MOSFLM indexing error : No solution was obtained!"
            self.ERROR(strError)
            self.setFailure()
        else:
            xsDataMOSFLMOutputIndexing.setRefinedNewmat(xsDataMOSFLMNewmat)
            # Then read the XML file
            strDnaTablesXML = self.readProcessFile(self.getScriptBaseName() + "_dnaTables.xml")
            xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)

            listXSTableMosaicityEstimation = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "mosaicity_estimation")
            dMosaicityValueSum = 0.0
            nValues = 0
            for xsTableMosaicityEstimation in listXSTableMosaicityEstimation:
                for xsListMosaicity in EDUtilsTable.getListsFromTable(xsTableMosaicityEstimation, "mosaicity"):
                    dMosaicityValue = float(EDUtilsTable.getItemFromList(xsListMosaicity, "value").getValueOf_())
                    dMosaicityValueSum += dMosaicityValue
                    nValues += 1
            xsDataFloatMosaicityEstimation = XSDataFloat()
            xsDataFloatMosaicityEstimation.setValue(dMosaicityValueSum / nValues)
            xsDataMOSFLMOutputIndexing.setMosaicityEstimation(xsDataFloatMosaicityEstimation)

            xsTableRefinement = EDUtilsTable.getTableFromTables(xsDataDnaTables, "refinement")
            if (xsTableRefinement is None):
                strError = "MOSFLM indexing error : No solution was refined!"
                self.ERROR(strError)
                self.setFailure()
            else:
                xsListDeviations = EDUtilsTable.getListsFromTable(xsTableRefinement, "deviations")[0]
                dDeviationAngular = float(EDUtilsTable.getItemFromList(xsListDeviations, "angular").getValueOf_())
                dDeviationPositional = float(EDUtilsTable.getItemFromList(xsListDeviations, "positional").getValueOf_())
                xsDataMOSFLMOutputIndexing.setDeviationAngular(XSDataAngle(dDeviationAngular))
                xsDataMOSFLMOutputIndexing.setDeviationPositional(XSDataLength(dDeviationPositional))
                xsListResults = EDUtilsTable.getListsFromTable(xsTableRefinement, "results")[0]
                dDetectorDistance = float(EDUtilsTable.getItemFromList(xsListResults, "detector_distance").getValueOf_())
                xsDataMOSFLMOutputIndexing.setRefinedDistance(XSDataLength(dDetectorDistance))
                xsListParameters = EDUtilsTable.getListsFromTable(xsTableRefinement, "parameters")[0]
                iSpotsUsed = int(EDUtilsTable.getItemFromList(xsListParameters, "used").getValueOf_())
                iSpotsTotal = int(EDUtilsTable.getItemFromList(xsListParameters, "out_of").getValueOf_())
                xsDataMOSFLMOutputIndexing.setSpotsUsed(XSDataInteger(iSpotsUsed))
                xsDataMOSFLMOutputIndexing.setSpotsTotal(XSDataInteger(iSpotsTotal))

                xsTableSolutionRefinement = EDUtilsTable.getTableFromTables(xsDataDnaTables, "solution_refinement")
                xsListParameters = EDUtilsTable.getListsFromTable(xsTableSolutionRefinement, "selection")[0]
                iSelectedSolutionNumber = int(EDUtilsTable.getItemFromList(xsListParameters, "number").getValueOf_())
                xsDataMOSFLMOutputIndexing.setSelectedSolutionNumber(XSDataInteger(iSelectedSolutionNumber))
                strSelectedSolutionSpaceGroup = (EDUtilsTable.getItemFromList(xsListParameters, "spacegroup").getValueOf_())
                xsDataMOSFLMOutputIndexing.setSelectedSolutionSpaceGroup(XSDataString(strSelectedSolutionSpaceGroup))
                iSelectedSolutionSpaceGroupNumber = int(EDUtilsTable.getItemFromList(xsListParameters, "spacegroup_number").getValueOf_())
                xsDataMOSFLMOutputIndexing.setSelectedSolutionSpaceGroupNumber(XSDataInteger(iSelectedSolutionSpaceGroupNumber))

                xsTableAutoIndexSolutions = EDUtilsTable.getTableFromTables(xsDataDnaTables, "autoindex_solutions")
                xsListsSolution = xsTableAutoIndexSolutions.getList()
                for xsListSolution in xsListsSolution:
                    xsDataMOSFLMIndexingSolution = XSDataMOSFLMIndexingSolution()
                    xsDataCell = XSDataCell()
                    iSolutionNumber = int(EDUtilsTable.getItemFromList(xsListSolution, "index").getValueOf_())
                    xsDataMOSFLMIndexingSolution.setIndex(XSDataInteger(iSolutionNumber))
                    iPenalty = int(EDUtilsTable.getItemFromList(xsListSolution, "penalty").getValueOf_())
                    xsDataMOSFLMIndexingSolution.setPenalty(XSDataInteger(iPenalty))
                    strLattice = (EDUtilsTable.getItemFromList(xsListSolution, "lattice").getValueOf_())
                    xsDataMOSFLMIndexingSolution.setLattice(XSDataString(strLattice))
                    dA = float(EDUtilsTable.getItemFromList(xsListSolution, "a").getValueOf_())
                    xsDataCell.setLength_a(XSDataLength(dA))
                    dB = float(EDUtilsTable.getItemFromList(xsListSolution, "b").getValueOf_())
                    xsDataCell.setLength_b(XSDataLength(dB))
                    dC = float(EDUtilsTable.getItemFromList(xsListSolution, "c").getValueOf_())
                    xsDataCell.setLength_c(XSDataLength(dC))
                    dAlpha = float(EDUtilsTable.getItemFromList(xsListSolution, "alpha").getValueOf_())
                    xsDataCell.setAngle_alpha(XSDataAngle(dAlpha))
                    dBeta = float(EDUtilsTable.getItemFromList(xsListSolution, "beta").getValueOf_())
                    xsDataCell.setAngle_beta(XSDataAngle(dBeta))
                    dGamma = float(EDUtilsTable.getItemFromList(xsListSolution, "gamma").getValueOf_())
                    xsDataCell.setAngle_gamma(XSDataAngle(dGamma))
                    xsDataMOSFLMIndexingSolution.setCell(xsDataCell)
                    xsDataMOSFLMOutputIndexing.addPossibleSolutions(xsDataMOSFLMIndexingSolution)

                xsTableBeamRefinement = EDUtilsTable.getTableFromTables(xsDataDnaTables, "beam_refinement")
                xsDataMOSFLMBeamPositionRefined = XSDataMOSFLMBeamPosition()
                xsDataMOSFLMBeamPositionShift = XSDataMOSFLMBeamPosition()
                dInitialBeamX = 0.0
                dInitialBeamY = 0.0
                dRefinedBeamX = 0.0
                dRefinedBeamY = 0.0
                xsListInitialBeam = EDUtilsTable.getListsFromTable(xsTableBeamRefinement, "initial_beam")[0]
                fInitialBeamPositionX = float(EDUtilsTable.getItemFromList(xsListInitialBeam, "x").getValueOf_())
                fInitialBeamPositionY = float(EDUtilsTable.getItemFromList(xsListInitialBeam, "y").getValueOf_())
                xsListRefinedBeam = EDUtilsTable.getListsFromTable(xsTableBeamRefinement, "refined_beam")[0]
                fRefinedBeamPositionX = float(EDUtilsTable.getItemFromList(xsListRefinedBeam, "x").getValueOf_())
                fRefinedBeamPositionY = float(EDUtilsTable.getItemFromList(xsListRefinedBeam, "y").getValueOf_())
                xsDataMOSFLMBeamPositionRefined.setX(XSDataLength(fRefinedBeamPositionX))
                xsDataMOSFLMBeamPositionRefined.setY(XSDataLength(fRefinedBeamPositionY))
                xsDataMOSFLMBeamPositionShift.setX(XSDataLength(fInitialBeamPositionX - fRefinedBeamPositionX))
                xsDataMOSFLMBeamPositionShift.setY(XSDataLength(fInitialBeamPositionY - fRefinedBeamPositionY))
                xsDataMOSFLMOutputIndexing.setRefinedBeam(xsDataMOSFLMBeamPositionRefined)
                xsDataMOSFLMOutputIndexing.setBeamShift(xsDataMOSFLMBeamPositionShift)
        # Path to log file
        xsDataMOSFLMOutputIndexing.setPathToLogFile(XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))))
        return xsDataMOSFLMOutputIndexing


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDPluginMOSFLMv10.generateExecutiveSummary(self, _edPlugin)
        self.DEBUG("EDPluginMOSFLMIndexingv10.createDataMOSFLMOutputIndexing")
        xsDataMOSFLMInputIndexing = self.getDataInput()
        xsDataMOSFLMOutputIndexing = self.getDataOutput()
        if not self.isFailure():
            self.addExecutiveSummaryLine("Execution of MOSFLM indexing successful.")
        self.addExecutiveSummaryLine("Image directory         : %s" % xsDataMOSFLMInputIndexing.getDirectory().getValue())
        self.addExecutiveSummaryLine("Image template          : %s" % xsDataMOSFLMInputIndexing.getTemplate().getValue())
        strImagesUsed = "Images used in indexing : "
        for xsDataMOSFLMImage in xsDataMOSFLMInputIndexing.getImage():
            strImagesUsed += "%3d" % xsDataMOSFLMImage.getNumber().getValue()
        self.addExecutiveSummaryLine(strImagesUsed)
        if (xsDataMOSFLMInputIndexing.getSymmetry() is not None):
            self.addExecutiveSummaryLine("Target symmetry     : %s" % xsDataMOSFLMInputIndexing.getSymmetry().getValue())
            self.addExecutiveSummaryLine("")
        if (xsDataMOSFLMOutputIndexing is not None):
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("List of possible solutions (index, penalty, lattice and cell):")
            iSelectedSolutionNumber = xsDataMOSFLMOutputIndexing.getSelectedSolutionNumber().getValue()
            # Add all solutions with penalty < 100 + 1 solution with penalty > 100
            bAddSolution = False
            listMOSFLMOutputIndexing = xsDataMOSFLMOutputIndexing.getPossibleSolutions()
            iNumberOfSolutions = len(listMOSFLMOutputIndexing)
            for i in range(iNumberOfSolutions):

                iPenalty = listMOSFLMOutputIndexing[i].getPenalty().getValue()
                if (i < (iNumberOfSolutions - 1)):
                    iPenaltyNext = listMOSFLMOutputIndexing[i + 1].getPenalty().getValue()
                    if ((iPenalty >= 100) and (iPenaltyNext <= 100)):
                        bAddSolution = True
                if (bAddSolution):
                    iIndex = listMOSFLMOutputIndexing[i].getIndex().getValue()
                    xsDataCell = listMOSFLMOutputIndexing[i].getCell()
                    strLattice = listMOSFLMOutputIndexing[i].getLattice().getValue()
                    strPossibleSolution = "%3d %4d %2s %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f" % \
                                                (iIndex, iPenalty, strLattice, \
                                                  xsDataCell.getLength_a().getValue(),
                                                  xsDataCell.getLength_b().getValue(),
                                                  xsDataCell.getLength_c().getValue(),
                                                  xsDataCell.getAngle_alpha().getValue(),
                                                  xsDataCell.getAngle_beta().getValue(),
                                                  xsDataCell.getAngle_gamma().getValue(),
                                                 )
                    self.addExecutiveSummaryLine(strPossibleSolution)
                iPenaltyOld = iPenalty
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Choosen solution number   : %14d" % iSelectedSolutionNumber)
            strSelectedSpaceGroup = xsDataMOSFLMOutputIndexing.getSelectedSolutionSpaceGroup().getValue()
            self.addExecutiveSummaryLine("Selected space group      : %14s" % (strSelectedSpaceGroup))
            xsDataCellRefined = xsDataMOSFLMOutputIndexing.getRefinedNewmat().getRefinedCell()
            self.addExecutiveSummaryLine("Refined cell              : %6.2f %7.2f %7.2f %5.1f %5.1f %5.1f" % (\
                                          xsDataCellRefined.getLength_a().getValue(),
                                          xsDataCellRefined.getLength_b().getValue(),
                                          xsDataCellRefined.getLength_c().getValue(),
                                          xsDataCellRefined.getAngle_alpha().getValue(),
                                          xsDataCellRefined.getAngle_beta().getValue(),
                                          xsDataCellRefined.getAngle_gamma().getValue()
                                          ))
            iSpotsTotal = xsDataMOSFLMOutputIndexing.getSpotsTotal().getValue()
            iSpotsUsed = xsDataMOSFLMOutputIndexing.getSpotsUsed().getValue()
            self.addExecutiveSummaryLine("Number of spots used      : %14d " % (iSpotsUsed))
            self.addExecutiveSummaryLine("Number of spots total     : %14d " % (iSpotsTotal))
            fDeviationPositional = xsDataMOSFLMOutputIndexing.getDeviationPositional().getValue()
            fDeviationAngular = xsDataMOSFLMOutputIndexing.getDeviationAngular().getValue()
            self.addExecutiveSummaryLine("Spot deviation positional : %14.2f [mm]" % (fDeviationPositional))
            self.addExecutiveSummaryLine("Spot deviation angular    : %14.2f [degrees]" % (fDeviationAngular))
            fBeamshiftX = xsDataMOSFLMOutputIndexing.getBeamShift().getX().getValue()
            fBeamshiftY = xsDataMOSFLMOutputIndexing.getBeamShift().getY().getValue()
            self.addExecutiveSummaryLine("Beam shift (X, Y)         : %6.3f, %6.3f [mm]" % \
                                          (fBeamshiftX, fBeamshiftY))
            fMosaicityEstimated = xsDataMOSFLMOutputIndexing.getMosaicityEstimation().getValue()
            self.addExecutiveSummaryLine("Estimated mosaicity       : %14.2f [degrees]" % fMosaicityEstimated)
