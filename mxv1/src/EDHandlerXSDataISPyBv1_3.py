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

from XSDataISPyBv1_3 import XSDataInputISPyBScreening,\
    XSDataISPyBScreeningStrategyContainer
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
from XSDataISPyBv1_3 import XSDataISPyBScreeningStrategyWedgeContainer
from XSDataISPyBv1_3 import XSDataISPyBScreeningStrategyWedge
from XSDataISPyBv1_3 import XSDataISPyBScreeningStrategySubWedge
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

        # ScreeningOutputContainer
        xsDataISPyBScreeningOutputContainer = EDHandlerXSDataISPyBv1_3.generateXSDataISPyBScreeningOutputContainer(xsDataResultCharacterisation, _strStatusMessage)

        # Assemble the input
        xsDataISPyBScreening.dataCollectionId = xsDataIntegerDataCollectionId
        xsDataInputISPyBScreening.diffractionPlan = xsDataISPyBDiffractionPlan
        xsDataInputISPyBScreening.screening = xsDataISPyBScreening
        xsDataInputISPyBScreening.screeningInput = xsDataISPyBScreeningInput
        xsDataInputISPyBScreening.addScreeningOutputContainer(xsDataISPyBScreeningOutputContainer)

        return xsDataInputISPyBScreening

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
        xsDataISPyBScreeningInput = XSDataISPyBScreeningInput()
        xsDataCollection = _xsDataResultCharacterisation.dataCollection
        if xsDataCollection is not None:
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
    
    @staticmethod
    def generateXSDataISPyBScreeningOutputContainer(_xsDataResultCharacterisation, _strStatusMessage = None):
        xsDataISPyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()
        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningStrategyContainer = XSDataISPyBScreeningStrategyContainer()
        # Indexing information
        bSuccessfulIndexing = False
        xsDataIndexingResult = _xsDataResultCharacterisation.getIndexingResult()
        if (xsDataIndexingResult is not None):
            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
            if (xsDataIndexingSolutionSelected is not None):
                bSuccessfulIndexing = True
                xsDataStatisticsIndexing = xsDataIndexingSolutionSelected.getStatistics()
                if (xsDataStatisticsIndexing is not None):
                    xsDataISPyBScreeningOutput.beamShiftX = xsDataStatisticsIndexing.beamPositionShiftX
                    xsDataISPyBScreeningOutput.beamShiftY = xsDataStatisticsIndexing.beamPositionShiftY
                    xsDataISPyBScreeningOutput.spotDeviationR = xsDataStatisticsIndexing.spotDeviationAngular
                    xsDataISPyBScreeningOutput.spotDeviationTheta = xsDataStatisticsIndexing.spotDeviationPositional
                    if ((xsDataStatisticsIndexing.spotsTotal is not None) and (xsDataStatisticsIndexing.spotsUsed is not None)):
                        iSpotsTotal = xsDataStatisticsIndexing.spotsTotal.value
                        iSpotsUsed = xsDataStatisticsIndexing.spotsUsed.value
                        xsDataISPyBScreeningOutput.numSpotsFound = xsDataStatisticsIndexing.spotsTotal
                        xsDataISPyBScreeningOutput.numSpotsUsed = xsDataStatisticsIndexing.spotsUsed
                        xsDataISPyBScreeningOutput.numSpotsRejected = XSDataInteger(iSpotsTotal - iSpotsUsed)
                xsDataCrystal = xsDataIndexingSolutionSelected.crystal
                xsDataISPyBScreeningOutput.mosaicityEstimated = XSDataBoolean(False)
                if (xsDataCrystal is not None):
                    if xsDataCrystal.mosaicity is not None:
                        xsDataISPyBScreeningOutput.mosaicity = xsDataCrystal.mosaicity
                        xsDataISPyBScreeningOutput.mosaicityEstimated = XSDataBoolean(True)
                    xsDataCell = xsDataCrystal.cell
                    if xsDataCell is not None:
                        xsDataISPyBScreeningOutputLattice.unitCell_a = xsDataCell.length_a
                        xsDataISPyBScreeningOutputLattice.unitCell_b = xsDataCell.length_b
                        xsDataISPyBScreeningOutputLattice.unitCell_c = xsDataCell.length_c
                        xsDataISPyBScreeningOutputLattice.unitCell_alpha = xsDataCell.angle_alpha
                        xsDataISPyBScreeningOutputLattice.unitCell_beta = xsDataCell.angle_beta
                        xsDataISPyBScreeningOutputLattice.unitCell_gamma = xsDataCell.angle_gamma
                    xsDataSpaceGroup = xsDataCrystal.spaceGroup
                    if xsDataSpaceGroup is not None:
                        xsDataISPyBScreeningOutputLattice.spaceGroup = xsDataSpaceGroup.name
        if (bSuccessfulIndexing):
            xsDataISPyBScreeningOutput.setScreeningSuccess(XSDataBoolean(True))
            if _strStatusMessage:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing successful"))
        else:
            xsDataISPyBScreeningOutput.setScreeningSuccess(XSDataBoolean(False))
            if _strStatusMessage:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing failed"))
        

        # Strategy information
        xsDataResultStrategy = _xsDataResultCharacterisation.strategyResult
        xsDataISPyBScreeningStrategyWedgeContainer = None
        if xsDataResultStrategy is not None:
            xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
            listXSDataCollectionPlan = xsDataResultStrategy.collectionPlan
            if listXSDataCollectionPlan != []:
                xsDataISPyBScreeningStrategyWedgeContainer = XSDataISPyBScreeningStrategyWedgeContainer()
                for xsDataCollectionPlan in listXSDataCollectionPlan:
                    numberOfImagesWedge = None
                    xsDataISPyBScreeningStrategyWedge = XSDataISPyBScreeningStrategyWedge()
                    xsDataISPyBScreeningStrategyWedge.wedgeNumber = xsDataCollectionPlan.collectionPlanNumber
                    strCollectionPlanComment = None
                    if (xsDataCollectionPlan.getComment() is not None):
                        strCollectionPlanComment = xsDataCollectionPlan.getComment().getValue()
                    xsDataStrategySummary = xsDataCollectionPlan.strategySummary
                    if xsDataStrategySummary is not None:
                        xsDataISPyBScreeningStrategyWedge.completeness = xsDataStrategySummary.completeness
                        xsDataISPyBScreeningStrategyWedge.resolution   = xsDataStrategySummary.resolution
                        xsDataISPyBScreeningStrategyWedge.multiplicity = xsDataStrategySummary.redundancy
                        xsDataISPyBScreeningStrategy.rankingResolution = xsDataStrategySummary.rankingResolution
                    xsDataCollectionStrategy = xsDataCollectionPlan.collectionStrategy
                    if xsDataCollectionStrategy is not None:
                        for xsDataSubWedge in xsDataCollectionStrategy.subWedge:
                            numberOfImagesSubWedge = None
                            xsDataISPyBScreeningStrategySubWedge = XSDataISPyBScreeningStrategySubWedge()
                            xsDataISPyBScreeningStrategySubWedge.subWedgeNumber = xsDataSubWedge.subWedgeNumber
                            xsDataISPyBScreeningStrategySubWedge.axisStart = xsDataSubWedge.experimentalCondition.goniostat.rotationAxisStart
                            xsDataISPyBScreeningStrategySubWedge.axisEnd = xsDataSubWedge.experimentalCondition.goniostat.rotationAxisEnd
                            xsDataISPyBScreeningStrategySubWedge.oscillationRange = xsDataSubWedge.experimentalCondition.goniostat.oscillationWidth
                            # Number of images
                            if  (xsDataSubWedge.experimentalCondition.goniostat.rotationAxisStart is not None) and \
                                (xsDataSubWedge.experimentalCondition.goniostat.rotationAxisEnd is not None) and \
                                (xsDataSubWedge.experimentalCondition.goniostat.oscillationWidth is not None):
                                numberOfImagesSubWedge = int( (xsDataSubWedge.experimentalCondition.goniostat.rotationAxisEnd.value - \
                                                 xsDataSubWedge.experimentalCondition.goniostat.rotationAxisStart.value) / \
                                                 xsDataSubWedge.experimentalCondition.goniostat.oscillationWidth.value + 0.5) 
                                xsDataISPyBScreeningStrategySubWedge.numberOfImages = XSDataInteger(numberOfImagesSubWedge)
                                if numberOfImagesWedge is None:
                                    numberOfImagesWedge = numberOfImagesSubWedge
                                else:
                                    numberOfImagesWedge += numberOfImagesSubWedge
                            xsDataISPyBScreeningStrategySubWedge.exposureTime = xsDataSubWedge.experimentalCondition.beam.exposureTime
                            xsDataISPyBScreeningStrategySubWedge.transmission = xsDataSubWedge.experimentalCondition.beam.transmission
                        xsDataISPyBScreeningStrategyWedgeContainer.addScreeningStrategySubWedge(xsDataISPyBScreeningStrategySubWedge)
                    if numberOfImagesWedge is not None:
                        xsDataISPyBScreeningStrategyWedge.numberOfImages = XSDataInteger(numberOfImagesWedge)
                    xsDataISPyBScreeningStrategyWedgeContainer.screeningStrategyWedge = xsDataISPyBScreeningStrategyWedge
                xsDataISPyBScreeningStrategyContainer.addScreeningStrategyWedgeContainer(xsDataISPyBScreeningStrategyWedgeContainer)   
            xsDataISPyBScreeningStrategyContainer.screeningStrategy = xsDataISPyBScreeningStrategy
#                                xsDataISPyBScreeningStrategy.setProgram(XSDataString(strProgram))
#                                xsDataISPyBScreeningOutputContainer.addScreeningStrategy(xsDataISPyBScreeningStrategy)


#        screeningOutputLattice : XSDataISPyBScreeningOutputLattice [] optional
#        screeningStrategyContainer : XSDataISPyBScreeningStrategyContainer [] optional
        # Assembly
        xsDataISPyBScreeningOutputContainer.screeningOutput = xsDataISPyBScreeningOutput
        xsDataISPyBScreeningOutputContainer.addScreeningOutputLattice(xsDataISPyBScreeningOutputLattice)
        xsDataISPyBScreeningOutputContainer.addScreeningStrategyContainer(xsDataISPyBScreeningStrategyContainer)

        
        return xsDataISPyBScreeningOutputContainer
