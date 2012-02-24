#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger


import time

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_3")

from XSDataISPyBv1_3 import XSDataInputISPyBScreening
from XSDataISPyBv1_3 import XSDataISPyBDiffractionPlan
from XSDataISPyBv1_3 import XSDataISPyBScreening
from XSDataISPyBv1_3 import XSDataISPyBScreeningInput
from XSDataISPyBv1_3 import XSDataISPyBScreeningOutput
from XSDataISPyBv1_3 import XSDataISPyBScreeningRank
from XSDataISPyBv1_3 import XSDataISPyBScreeningRankSet
from XSDataISPyBv1_3 import XSDatadbstatus
from XSDataISPyBv1_3 import XSDataISPyBScreeningOutputContainer
from XSDataISPyBv1_3 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_3 import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_3 import XSDataISPyBDataCollection
from XSDataISPyBv1_3 import XSDataISPyBImage
from XSDataISPyBv1_3 import XSDataResultStatus


class EDHandlerXSDataISPyBv1_3:

    @staticmethod
    def generateXSDataInputISPyB(_xsDataInputControlISPyB, _strStatusMessage=None):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_3")

        xsDataInputISPyBScreening = XSDataInputISPyBScreening()

        xsDataResultCharacterisation = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataIntegerDataCollectionId = _xsDataInputControlISPyB.getDataCollectionId()

        # Diffraction plan
        xsDataISPyBDiffractionPlan = EDHandlerXSDataISPyBv1_3.generateXSDataISPyBDiffractionPlan(xsDataResultCharacterisation)

        # Screening
        xsDataISPyBScreening = EDHandlerXSDataISPyBv1_3.generateXSDataISPyBScreening()

        # ScreeningInput
        xsDataISPyBScreeningInput = EDHandlerXSDataISPyBv1_3.generateXSDataISPyBScreeningInput(xsDataResultCharacterisation)


#        # Data collection information
#        bAnomalousData = None
#        strPathToFirstImage = None
#        xsDataCollection = xsDataResultCharacterisation.getDataCollection()
#        if (xsDataCollection is not None):
#            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
#            xsDataSubWedgeList = xsDataCollection.getSubWedge()
#            if (xsDataSubWedgeList is not None):
#                xsDataSubWedgeFirst = xsDataSubWedgeList[0]
#                xsDataExperimentalCondition = xsDataSubWedgeFirst.getExperimentalCondition()
#                if (xsDataExperimentalCondition is not None):
#                    xsDataDetector = xsDataExperimentalCondition.getDetector()
#                    if (xsDataDetector is not None):
#                        xsDataISPyBScreeningInput.setBeamX(xsDataDetector.beamPositionX)
#                        xsDataISPyBScreeningInput.setBeamY(xsDataDetector.beamPositionY)
#                listXSDataImage = xsDataSubWedgeFirst.getImage()
#                if (listXSDataImage is not None):
#                    xsDataImageFirst = listXSDataImage[ 0 ]
#                    strPathToFirstImage = xsDataImageFirst.getPath().getValue()
#            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
#            if (xsDataDiffractionPlan is not None):
#                if (xsDataDiffractionPlan.getAnomalousData() is not None):
#                    bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()
#        # Use dataCollectionId if provided in the input
#        else:
#            # Add an image path if the dataCollectionId is not present...
#            if (strPathToFirstImage is not None):
#                xsDataISPyBImage = XSDataISPyBImage()
#                strImageBaseName = EDUtilsFile.getBaseName(strPathToFirstImage)
#                strDirectoryName = EDUtilsPath.getFolderName(strPathToFirstImage)
#                xsDataISPyBImage.setFileName(XSDataString(strImageBaseName))
#                xsDataISPyBImage.setFileLocation(XSDataString(strDirectoryName))
#                xsDataInputISPyBScreening.setImage(xsDataISPyBImage)
#
#        # Indexing information
#        bSuccessfulIndexing = False
#        xsDataIndexingResult = xsDataResultCharacterisation.getIndexingResult()
#        if (xsDataIndexingResult is not None):
#            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
#            if (xsDataIndexingSolutionSelected is not None):
#                bSuccessfulIndexing = True
#                xsDataStatisticsIndexing = xsDataIndexingSolutionSelected.getStatistics()
#                if (xsDataStatisticsIndexing is not None):
#                    fBeamPositionShiftX = xsDataStatisticsIndexing.getBeamPositionShiftX().getValue()
#                    fBeamPositionShiftY = xsDataStatisticsIndexing.getBeamPositionShiftY().getValue()
#                    xsDataIPSyBScreeningOutput.setBeamShiftX(XSDataDouble(fBeamPositionShiftX))
#                    xsDataIPSyBScreeningOutput.setBeamShiftY(XSDataDouble(fBeamPositionShiftY))
#            fSpotDeviationAngular = None
#            if xsDataStatisticsIndexing.getSpotDeviationAngular() is not None:
#                    fSpotDeviationAngular = xsDataStatisticsIndexing.getSpotDeviationAngular().getValue()
#                    fSpotDeviationPositional = xsDataStatisticsIndexing.getSpotDeviationPositional().getValue()
#                    xsDataIPSyBScreeningOutput.setSpotDeviationR(XSDataDouble(fSpotDeviationPositional))
#            if fSpotDeviationAngular is not None:
#                xsDataIPSyBScreeningOutput.setSpotDeviationTheta(XSDataDouble(fSpotDeviationAngular))
#                if ((xsDataStatisticsIndexing.getSpotsTotal() is not None) and (xsDataStatisticsIndexing.getSpotsUsed is not None)):
#                    iSpotsTotal = xsDataStatisticsIndexing.getSpotsTotal().getValue()
#                    iSpotsUsed = xsDataStatisticsIndexing.getSpotsUsed().getValue()
#                    xsDataIPSyBScreeningOutput.setNumSpotsFound(XSDataInteger(iSpotsTotal))
#                    xsDataIPSyBScreeningOutput.setNumSpotsUsed(XSDataInteger(iSpotsUsed))
#                    xsDataIPSyBScreeningOutput.setNumSpotsRejected(XSDataInteger(iSpotsTotal - iSpotsUsed))
#                xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
#                xsDataIPSyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(False))
#                if (xsDataCrystal is not None):
#                    if (xsDataCrystal.getMosaicity() is not None):
#                        fMosaicity = xsDataCrystal.getMosaicity().getValue()
#                        xsDataIPSyBScreeningOutput.setMosaicity(XSDataDouble(fMosaicity))
#                        xsDataIPSyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(True))
#                    xsDataCell = xsDataCrystal.getCell()
#                    if (xsDataCell is not None):
#                        fLength_a = xsDataCell.getLength_a().getValue()
#                        fLength_b = xsDataCell.getLength_b().getValue()
#                        fLength_c = xsDataCell.getLength_c().getValue()
#                        fAngle_alpha = xsDataCell.getAngle_alpha().getValue()
#                        fAngle_beta = xsDataCell.getAngle_beta().getValue()
#                        fAngle_gamma = xsDataCell.getAngle_gamma().getValue()
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_a(XSDataDouble(fLength_a))
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_b(XSDataDouble(fLength_b))
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_c(XSDataDouble(fLength_c))
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_alpha(XSDataDouble(fAngle_alpha))
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_beta(XSDataDouble(fAngle_beta))
#                        xsDataISPyBScreeningOutputLattice.setUnitCell_gamma(XSDataDouble(fAngle_gamma))
#                    xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
#                    if (xsDataSpaceGroup is not None):
#                        strSpaceGroupName = xsDataSpaceGroup.getName().getValue()
#                        xsDataISPyBScreeningOutputLattice.setSpaceGroup(XSDataString(strSpaceGroupName))
#        if (bSuccessfulIndexing):
#            xsDataIPSyBScreeningOutput.setScreeningSuccess(XSDataBoolean(True))
#            if _strStatusMessage:
#                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
#            else:
#                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString("Indexing successful"))
#        else:
#            xsDataIPSyBScreeningOutput.setScreeningSuccess(XSDataBoolean(False))
#            if _strStatusMessage:
#                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
#            else:
#                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString("Indexing failed"))
#
#
#
#        # Strategy information
#        xsDataResultStrategy = xsDataResultCharacterisation.getStrategyResult()
#        if (xsDataResultStrategy is not None):
#            listXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
#            if (listXSDataCollectionPlan is not None):
#                for xsDataCollectionPlan in listXSDataCollectionPlan:
#                    iCollectionPlanNumber = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
#                    strCollectionPlanComment = None
#                    if (xsDataCollectionPlan.getComment() is not None):
#                        strCollectionPlanComment = xsDataCollectionPlan.getComment().getValue()
#                    fCompleteness = None
#                    fMultiplicity = None
#                    fResolution = None
#                    fRankingResolution = None
#                    fTransmission = None
#                    xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
#                    if (xsDataStrategySummary is not None):
#                        if (xsDataStrategySummary.getCompleteness() is not None):
#                            fCompleteness = xsDataStrategySummary.getCompleteness().getValue()
#                        if (xsDataStrategySummary.getRedundancy() is not None):
#                            fMultiplicity = xsDataStrategySummary.getRedundancy().getValue()
#                        if (xsDataStrategySummary.getResolution() is not None):
#                            fResolution = xsDataStrategySummary.getResolution().getValue()
#                        if (xsDataStrategySummary.getRankingResolution() is not None):
#                            fRankingResolution = xsDataStrategySummary.getRankingResolution().getValue()
#                    xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
#                    if (xsDataCollectionStrategy is not None):
#                        listXSDataSubWedge = xsDataCollectionStrategy.getSubWedge()
#                        if (listXSDataSubWedge is not None):
#                            for xsDataSubWedge in listXSDataSubWedge:
#                                iSubWedgeNumber = xsDataSubWedge.getSubWedgeNumber().getValue()
#                                xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
#                                fPhiStart = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()
#                                fPhiEnd = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
#                                fRotation = xsDataSubWedge.getExperimentalCondition().getGoniostat().getOscillationWidth().getValue()
#                                fExposureTime = xsDataSubWedge.getExperimentalCondition().getBeam().getExposureTime().getValue()
#                                if xsDataSubWedge.getExperimentalCondition().getBeam().getTransmission() != None:
#                                    fTransmission = xsDataSubWedge.getExperimentalCondition().getBeam().getTransmission().getValue()
#                                strProgram = "BEST: Wedge no %d," % iCollectionPlanNumber
#                                if (strCollectionPlanComment is not None):
#                                    strProgram += " ( %s )" % strCollectionPlanComment
#                                strProgram += " sub wedge no %d" % iSubWedgeNumber
#                                xsDataISPyBScreeningStrategy.setPhiStart(XSDataDouble(fPhiStart))
#                                xsDataISPyBScreeningStrategy.setPhiEnd(XSDataDouble(fPhiEnd))
#                                xsDataISPyBScreeningStrategy.setRotation(XSDataDouble(fRotation))
#                                xsDataISPyBScreeningStrategy.setExposureTime(XSDataDouble(fExposureTime))
#                                xsDataISPyBScreeningStrategy.setTransmission(XSDataDouble(fTransmission))
#                                if (fCompleteness is not None):
#                                    xsDataISPyBScreeningStrategy.setCompleteness(XSDataDouble(fCompleteness))
#                                if (fMultiplicity is not None):
#                                    xsDataISPyBScreeningStrategy.setMultiplicity(XSDataDouble(fMultiplicity))
#                                if (fResolution is not None):
#                                    xsDataISPyBScreeningStrategy.setResolution(XSDataDouble(fResolution))
#                                if (fRankingResolution is not None):
#                                    xsDataISPyBScreeningStrategy.setRankingResolution(XSDataDouble(fRankingResolution))
#                                if (bAnomalousData is not None):
#                                    xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(bAnomalousData))
#                                else:
#                                    xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(False))
#                                xsDataISPyBScreeningStrategy.setProgram(XSDataString(strProgram))
#                                xsDataISPyBScreeningOutputContainer.addScreeningStrategy(xsDataISPyBScreeningStrategy)
#
#
#
        xsDataISPyBScreening.dataCollectionId = xsDataIntegerDataCollectionId
        xsDataInputISPyBScreening.diffractionPlan = xsDataISPyBDiffractionPlan
        xsDataInputISPyBScreening.screening = xsDataISPyBScreening
        xsDataInputISPyBScreening.screeningInput = xsDataISPyBScreeningInput
#        xsDataISPyBScreeningOutputContainer.setScreeningOutput(xsDataIPSyBScreeningOutput)
#        xsDataISPyBScreeningOutputContainer.addScreeningOutputLattice(xsDataISPyBScreeningOutputLattice)
#        xsDataInputISPyBScreening.addScreeningOutputContainer(xsDataISPyBScreeningOutputContainer)
#
        return xsDataInputISPyBScreening


    @staticmethod
    def generateXSDataISPyBDiffractionPlan(_xsDataResultCharacterisation):
        xsDataISPyBDiffractionPlan = None
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        if (xsDataCollection is not None):
            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
            if xsDataDiffractionPlan != None:
                xsDataISPyBDiffractionPlan = XSDataISPyBDiffractionPlan()
                xsDataISPyBDiffractionPlan.aimedCompleteness = xsDataDiffractionPlan.aimedCompleteness
                xsDataISPyBDiffractionPlan.aimedIOverSigmaAtHighestResolution = xsDataDiffractionPlan.aimedIOverSigmaAtHighestResolution
                xsDataISPyBDiffractionPlan.aimedMultiplicity =  xsDataDiffractionPlan.aimedMultiplicity
                xsDataISPyBDiffractionPlan.aimedResolution = xsDataDiffractionPlan.aimedResolution
                xsDataISPyBDiffractionPlan.anomalousData = xsDataDiffractionPlan.anomalousData
                xsDataISPyBDiffractionPlan.complexity = xsDataDiffractionPlan.complexity
                xsDataISPyBDiffractionPlan.detectorMaxResolution = xsDataDiffractionPlan.detectorMaxResolution
                xsDataISPyBDiffractionPlan.detectorMinResolution = xsDataDiffractionPlan.detectorMinResolution
                xsDataISPyBDiffractionPlan.estimateRadiationDamage = xsDataDiffractionPlan.estimateRadiationDamage
                xsDataISPyBDiffractionPlan.forcedSpaceGroup = xsDataDiffractionPlan.forcedSpaceGroup
                xsDataISPyBDiffractionPlan.goniostatMaxOscillationSpeed = xsDataDiffractionPlan.goniostatMaxOscillationSpeed
                xsDataISPyBDiffractionPlan.goniostatMinOscillationWidth = xsDataDiffractionPlan.goniostatMinOscillationWidth
                strAllKappaStrategyOptions = ""
                for strKappaStrategyOption in xsDataDiffractionPlan.kappaStrategyOption:
                    strAllKappaStrategyOptions += strKappaStrategyOption + ", "
                if strAllKappaStrategyOptions != "":
                    xsDataISPyBDiffractionPlan.kappaStrategyOption = XSDataString(strAllKappaStrategyOptions)
                xsDataISPyBDiffractionPlan.maxExposureTimePerDataCollection = xsDataDiffractionPlan.maxExposureTimePerDataCollection
                xsDataISPyBDiffractionPlan.minExposureTimePerImage = xsDataDiffractionPlan.minExposureTimePerImage
                xsDataISPyBDiffractionPlan.minTransmission = xsDataDiffractionPlan.minTransmission
                xsDataISPyBDiffractionPlan.numberOfPositions = xsDataDiffractionPlan.numberOfPositions
                xsDataISPyBDiffractionPlan.requiredCompleteness = xsDataDiffractionPlan.requiredCompleteness
                xsDataISPyBDiffractionPlan.requiredMultiplicity = xsDataDiffractionPlan.requiredMultiplicity
                xsDataISPyBDiffractionPlan.requiredResolution = xsDataDiffractionPlan.requiredResolution
                xsDataISPyBDiffractionPlan.strategyOption = xsDataDiffractionPlan.strategyOption            
        return xsDataISPyBDiffractionPlan
    
    @staticmethod
    def generateXSDataISPyBScreening():
        xsDataISPyBScreening = XSDataISPyBScreening()
        xsDataISPyBScreening.setProgramVersion(XSDataString("EDNA MX"))
        xsDataStringTimeStamp = XSDataString(time.strftime("%Y-%m-%d %H:%M:%S"))
        xsDataISPyBScreening.setTimeStamp(xsDataStringTimeStamp)
        return xsDataISPyBScreening
    
    
    @staticmethod
    def generateXSDataISPyBScreeningInput(_xsDataResultCharacterisation):
        xsDataISPyBScreeningInput = None
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        if (xsDataCollection is not None):
            xsDataISPyBScreeningInput = XSDataISPyBScreeningInput()
            xsDataSubWedgeList = xsDataCollection.getSubWedge()
            if (xsDataSubWedgeList is not None):
                xsDataSubWedgeFirst = xsDataSubWedgeList[0]
                xsDataExperimentalCondition = xsDataSubWedgeFirst.getExperimentalCondition()
                if (xsDataExperimentalCondition is not None):
                    xsDataDetector = xsDataExperimentalCondition.getDetector()
                    if (xsDataDetector is not None):
                        xsDataISPyBScreeningInput.setBeamX(xsDataDetector.beamPositionX)
                        xsDataISPyBScreeningInput.setBeamY(xsDataDetector.beamPositionY)
        return xsDataISPyBScreeningInput