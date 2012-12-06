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


from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble


import os, time

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")

from XSDataISPyBv1_4 import XSDataInputISPyBStoreScreening
from XSDataISPyBv1_4 import XSDataISPyBDiffractionPlan
from XSDataISPyBv1_4 import XSDataISPyBScreening
from XSDataISPyBv1_4 import XSDataISPyBScreeningOutput
from XSDataISPyBv1_4 import XSDataISPyBScreeningOutputContainer
from XSDataISPyBv1_4 import XSDataISPyBScreeningOutputLattice
from XSDataISPyBv1_4 import XSDataISPyBScreeningStrategy
from XSDataISPyBv1_4 import XSDataISPyBScreeningStrategyContainer
from XSDataISPyBv1_4 import XSDataISPyBScreeningStrategyWedgeContainer
from XSDataISPyBv1_4 import XSDataISPyBScreeningStrategyWedge
from XSDataISPyBv1_4 import XSDataISPyBScreeningStrategySubWedge
from XSDataISPyBv1_4 import XSDataISPyBImage


class EDHandlerXSDataISPyBv1_4(object):

    @staticmethod
    def generateXSDataInputISPyBStoreScreening(_xsDataInputControlISPyB, _strStatusMessage=None, _strShortComments=None, _strComments=None):

        xsDataInputISPyBStoreScreening = XSDataInputISPyBStoreScreening()

        xsDataResultCharacterisation = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataIntegerDataCollectionId = _xsDataInputControlISPyB.getDataCollectionId()

        # ISPyB image
        xsDataISPyBImage = EDHandlerXSDataISPyBv1_4.generateXSDataISPyBImage(xsDataResultCharacterisation)

        # Diffraction plan
        xsDataISPyBDiffractionPlan = EDHandlerXSDataISPyBv1_4.generateXSDataISPyBDiffractionPlan(xsDataResultCharacterisation)

        # Screening
        # Temporary fix for mxsup717, while waiting for a change of the ISPyB web service
        strComments = _strComments
#        if xsDataResultCharacterisation.getIndexingResult() is not None:
#            if xsDataResultCharacterisation.getIndexingResult().getLabelitIndexing():
#                if strComments is None:
#                    strComments = ""
#                else:
#                    strComments += " "
#                if xsDataResultCharacterisation.getIndexingResult().getLabelitIndexing().getValue():
#                    strComments += "Labelit indexing"
#                else:
#                    strComments += "MOSFLM indexing"
        xsDataISPyBScreening = EDHandlerXSDataISPyBv1_4.generateXSDataISPyBScreening(_strShortComments, strComments)

        # ScreeningOutputContainer
        fKappa = None
        if _xsDataInputControlISPyB.kappa is not None:
            fKappa = _xsDataInputControlISPyB.kappa.value
        fPhi = None
        if _xsDataInputControlISPyB.phi is not None:
            fPhi = _xsDataInputControlISPyB.phi.value
        xsDataISPyBScreeningOutputContainer = EDHandlerXSDataISPyBv1_4.generateXSDataISPyBScreeningOutputContainer(xsDataResultCharacterisation, \
                                                                                                                   _strStatusMessage, fKappa, fPhi)

        # Assemble the input
        xsDataISPyBScreening.dataCollectionId = xsDataIntegerDataCollectionId
        xsDataInputISPyBStoreScreening.image = xsDataISPyBImage
        xsDataInputISPyBStoreScreening.diffractionPlan = xsDataISPyBDiffractionPlan
        xsDataInputISPyBStoreScreening.screening = xsDataISPyBScreening
        xsDataInputISPyBStoreScreening.addScreeningOutputContainer(xsDataISPyBScreeningOutputContainer)

        return xsDataInputISPyBStoreScreening


    def generateXSDataISPyBImage(_xsDataResultCharacterisation):
        xsDataISPyBImage = None
        # Find path to first image from data collection information
        strPathToFirstImage = None
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        if (xsDataCollection is not None):
            lXSDataSubWedge = xsDataCollection.getSubWedge()
            if (lXSDataSubWedge is not None):
                xsDataSubWedgeFirst = lXSDataSubWedge[0]
                lXSDataImage = xsDataSubWedgeFirst.getImage()
                if (lXSDataImage is not None):
                    xsDataImageFirst = lXSDataImage[ 0 ]
                    strPathToFirstImage = xsDataImageFirst.getPath().getValue()

            # Add an image path if the dataCollectionId is not present...
            if (strPathToFirstImage is not None):
                xsDataISPyBImage = XSDataISPyBImage()
                strImageBaseName = os.path.basename(strPathToFirstImage)
                strDirectoryName = os.path.dirname(strPathToFirstImage)
                xsDataISPyBImage.setFileName(XSDataString(strImageBaseName))
                xsDataISPyBImage.setFileLocation(XSDataString(strDirectoryName))
        return xsDataISPyBImage
    generateXSDataISPyBImage = staticmethod(generateXSDataISPyBImage)

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
                xsDataISPyBDiffractionPlan.detectorDistanceMax = xsDataDiffractionPlan.detectorDistanceMax
                xsDataISPyBDiffractionPlan.detectorDistanceMin = xsDataDiffractionPlan.detectorDistanceMin
                xsDataISPyBDiffractionPlan.estimateRadiationDamage = xsDataDiffractionPlan.estimateRadiationDamage
                xsDataISPyBDiffractionPlan.forcedSpaceGroup = xsDataDiffractionPlan.forcedSpaceGroup
                xsDataISPyBDiffractionPlan.goniostatMaxOscillationSpeed = xsDataDiffractionPlan.goniostatMaxOscillationSpeed
                xsDataISPyBDiffractionPlan.goniostatMinOscillationWidth = xsDataDiffractionPlan.goniostatMinOscillationWidth
                strAllKappaStrategyOptions = ""
                for kappaStrategyOption in xsDataDiffractionPlan.kappaStrategyOption:
                    strAllKappaStrategyOptions += kappaStrategyOption.value
                    # Add a comma to separate entries except for the last item
                    if kappaStrategyOption != xsDataDiffractionPlan.kappaStrategyOption[-1]:
                        strAllKappaStrategyOptions += ", "
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
    def generateXSDataISPyBScreening(_xsDataSample=None, _strShortComments=None, _strComments=None):
        xsDataISPyBScreening = XSDataISPyBScreening()
        xsDataISPyBScreening.setProgramVersion(XSDataString("EDNA MX"))
        xsDataStringTimeStamp = XSDataString(time.strftime("%Y-%m-%d %H:%M:%S"))
        xsDataISPyBScreening.setTimeStamp(xsDataStringTimeStamp)
        if _strShortComments:
            xsDataISPyBScreening.shortComments = XSDataString(_strShortComments)
        if _strComments:
            xsDataISPyBScreening.comments = XSDataString(_strComments)
        return xsDataISPyBScreening
    
        
    @staticmethod
    def generateXSDataISPyBScreeningOutputContainer(_xsDataResultCharacterisation, _strStatusMessage, _fKappa, _fPhi):
        xsDataISPyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutput.program = XSDataString("EDNA MXv1")
        xsDataISPyBScreeningOutputLattice = None
        # Indexing information
        bSuccessfulIndexing = False
        xsDataIndexingResult = _xsDataResultCharacterisation.getIndexingResult()
        if (xsDataIndexingResult is not None):
            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
            if (xsDataIndexingSolutionSelected is not None):
                xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()
                bSuccessfulIndexing = True
                xsDataStatisticsIndexing = xsDataIndexingSolutionSelected.getStatistics()
                if (xsDataStatisticsIndexing is not None):
                    xsDataISPyBScreeningOutput.beamShiftX = xsDataStatisticsIndexing.beamPositionShiftX
                    xsDataISPyBScreeningOutput.beamShiftY = xsDataStatisticsIndexing.beamPositionShiftY
                    xsDataISPyBScreeningOutput.spotDeviationR = xsDataStatisticsIndexing.spotDeviationPositional
                    xsDataISPyBScreeningOutput.spotDeviationTheta = xsDataStatisticsIndexing.spotDeviationAngular
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
            xsDataISPyBScreeningOutput.setIndexingSuccess(XSDataBoolean(True))
            if _strStatusMessage:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing successful"))
        else:
            xsDataISPyBScreeningOutput.setIndexingSuccess(XSDataBoolean(False))
            if _strStatusMessage:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing failed"))
            

        # Strategy information
        xsDataResultStrategy = _xsDataResultCharacterisation.strategyResult
        xsDataISPyBScreeningStrategyContainer = None
        xsDataISPyBScreeningStrategyWedgeContainer = None
        if xsDataResultStrategy is None:
            xsDataISPyBScreeningOutput.setStrategySuccess(XSDataBoolean(False))
        else:
            xsDataISPyBScreeningOutput.setStrategySuccess(XSDataBoolean(True))
            xsDataISPyBScreeningStrategyContainer = XSDataISPyBScreeningStrategyContainer()
            xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
            listXSDataCollectionPlan = xsDataResultStrategy.collectionPlan
            fTotalExposureTime = 0.0
            iTotalNumberOfImages = 0
            fTotalRotationRange = 0.0
            for xsDataCollectionPlan in listXSDataCollectionPlan:
                numberOfImagesWedge = None
                xsDataISPyBScreeningStrategyWedge = XSDataISPyBScreeningStrategyWedge()
                xsDataISPyBScreeningStrategyWedgeContainer = XSDataISPyBScreeningStrategyWedgeContainer()
                xsDataISPyBScreeningStrategyWedge.wedgeNumber = xsDataCollectionPlan.collectionPlanNumber
                fWavelength = _xsDataResultCharacterisation.dataCollection.subWedge[0].experimentalCondition.beam.wavelength.value
                xsDataISPyBScreeningStrategyWedge.wavelength = XSDataDouble(fWavelength)
                if _fKappa is not None:
                    xsDataISPyBScreeningStrategyWedge.kappa = XSDataDouble(_fKappa)
                if _fPhi is not None:
                    xsDataISPyBScreeningStrategyWedge.phi = XSDataDouble(_fPhi)                
                if (xsDataCollectionPlan.getComment() is not None):
                    strCollectionPlanComment = xsDataCollectionPlan.getComment().getValue()
                    xsDataISPyBScreeningStrategyWedge.comments = strCollectionPlanComment
                xsDataStrategySummary = xsDataCollectionPlan.strategySummary
                if xsDataStrategySummary is not None:
                    xsDataISPyBScreeningStrategyWedge.completeness = xsDataStrategySummary.completeness
                    xsDataISPyBScreeningStrategyWedge.resolution   = xsDataStrategySummary.resolution
                    xsDataISPyBScreeningStrategyWedge.multiplicity = xsDataStrategySummary.redundancy
                    xsDataISPyBScreeningOutput.rankingResolution = xsDataStrategySummary.rankingResolution
                    if xsDataStrategySummary.totalExposureTime is not None:
                        fTotalExposureTime += xsDataStrategySummary.totalExposureTime.value
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
                            fTotalRotationRange += xsDataSubWedge.experimentalCondition.goniostat.oscillationWidth.value * numberOfImagesSubWedge
                        xsDataISPyBScreeningStrategySubWedge.exposureTime = xsDataSubWedge.experimentalCondition.beam.exposureTime
                        xsDataISPyBScreeningStrategySubWedge.transmission = xsDataSubWedge.experimentalCondition.beam.transmission
                        xsDataISPyBScreeningStrategyWedgeContainer.addScreeningStrategySubWedge(xsDataISPyBScreeningStrategySubWedge)
                if numberOfImagesWedge is not None:
                    xsDataISPyBScreeningStrategyWedge.numberOfImages = XSDataInteger(numberOfImagesWedge)
                    iTotalNumberOfImages +=  numberOfImagesWedge
                xsDataISPyBScreeningStrategyWedgeContainer.screeningStrategyWedge = xsDataISPyBScreeningStrategyWedge
                xsDataISPyBScreeningStrategyContainer.addScreeningStrategyWedgeContainer(xsDataISPyBScreeningStrategyWedgeContainer)
            xsDataISPyBScreeningOutput.totalExposureTime = XSDataDouble(fTotalExposureTime)   
            xsDataISPyBScreeningOutput.totalNumberOfImages = XSDataInteger(iTotalNumberOfImages)
            xsDataISPyBScreeningOutput.totalRotationRange = XSDataDouble(fTotalRotationRange)
            xsDataISPyBScreeningStrategyContainer.screeningStrategy = xsDataISPyBScreeningStrategy
        # Assembly
        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningOutputContainer.screeningOutput = xsDataISPyBScreeningOutput
        if xsDataISPyBScreeningOutputLattice is not None:
            xsDataISPyBScreeningOutputContainer.addScreeningOutputLattice(xsDataISPyBScreeningOutputLattice)
        if xsDataISPyBScreeningStrategyContainer is not None:
            xsDataISPyBScreeningOutputContainer.addScreeningStrategyContainer(xsDataISPyBScreeningStrategyContainer)
        
        return xsDataISPyBScreeningOutputContainer


    @staticmethod
    def generateLegacyXSDataISPyBStrategy(_xsDataResultCharacterisation, _xsDataISPyBScreeningOutputContainer):
        # Anomalus data
        bAnomalousData = False
        xsDataCollection = _xsDataResultCharacterisation.dataCollection
        if xsDataCollection is not None:
            xsDataDiffractionPlan = xsDataCollection.diffractionPlan
            if xsDataDiffractionPlan is not None:
                if xsDataDiffractionPlan.anomalousData is not None:
                    bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()
        # Use the existing xsDataISPyBScreeningStrategy in the _xsDataISPyBScreeningOutputContainer for the first sub wedge:
        if len(_xsDataISPyBScreeningOutputContainer.screeningStrategyContainer) > 0:
            xsDataISPyBScreeningStrategyContainerFirst = _xsDataISPyBScreeningOutputContainer.screeningStrategyContainer[0]
            xsDataISPyBScreeningStrategyFirst = xsDataISPyBScreeningStrategyContainerFirst.screeningStrategy
            # Strategy information
            bFirstStrategy = True
            xsDataResultStrategy = _xsDataResultCharacterisation.getStrategyResult()
            if (xsDataResultStrategy is not None):
                pyListXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
                if (pyListXSDataCollectionPlan is not None):
                    for xsDataCollectionPlan in pyListXSDataCollectionPlan:
                        iCollectionPlanNumber = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
                        pyStrCollectionPlanComment = None
                        if (xsDataCollectionPlan.getComment() is not None):
                            pyStrCollectionPlanComment = xsDataCollectionPlan.getComment().getValue()
                        fCompleteness = None
                        fMultiplicity = None
                        fResolution = None
                        fRankingResolution = None
                        fTransmission = None
                        xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                        if (xsDataStrategySummary is not None):
                            if (xsDataStrategySummary.getCompleteness() is not None):
                                fCompleteness = xsDataStrategySummary.getCompleteness().getValue()
                            if (xsDataStrategySummary.getRedundancy() is not None):
                                fMultiplicity = xsDataStrategySummary.getRedundancy().getValue()
                            if (xsDataStrategySummary.getResolution() is not None):
                                fResolution = xsDataStrategySummary.getResolution().getValue()
                            if (xsDataStrategySummary.getRankingResolution() is not None):
                                fRankingResolution = xsDataStrategySummary.getRankingResolution().getValue()
                        xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                        if (xsDataCollectionStrategy is not None):
                            pyListXSDataSubWedge = xsDataCollectionStrategy.getSubWedge()
                            if (pyListXSDataSubWedge is not None):
                                for xsDataSubWedge in pyListXSDataSubWedge:
                                    iSubWedgeNumber = xsDataSubWedge.getSubWedgeNumber().getValue()
                                    if bFirstStrategy:
                                        xsDataISPyBScreeningStrategy = xsDataISPyBScreeningStrategyFirst
                                    else:
                                        xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
                                        xsDataISPyBScreeningStrategyContainer = XSDataISPyBScreeningStrategyContainer()
                                        xsDataISPyBScreeningStrategyContainer.screeningStrategy = xsDataISPyBScreeningStrategy
                                    fPhiStart = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()
                                    fPhiEnd = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
                                    fRotation = xsDataSubWedge.getExperimentalCondition().getGoniostat().getOscillationWidth().getValue()
                                    fExposureTime = xsDataSubWedge.getExperimentalCondition().getBeam().getExposureTime().getValue()
                                    fTransmission = None
                                    if xsDataSubWedge.experimentalCondition.beam.transmission:
                                        fTransmission = xsDataSubWedge.experimentalCondition.beam.transmission.value
                                    pyStrProgram = "BEST: Wedge no %d," % iCollectionPlanNumber
                                    if (pyStrCollectionPlanComment is not None):
                                        pyStrProgram += " ( %s )" % pyStrCollectionPlanComment
                                    pyStrProgram += " sub wedge no %d" % iSubWedgeNumber
                                    xsDataISPyBScreeningStrategy.setPhiStart(XSDataDouble(fPhiStart))
                                    xsDataISPyBScreeningStrategy.setPhiEnd(XSDataDouble(fPhiEnd))
                                    xsDataISPyBScreeningStrategy.setRotation(XSDataDouble(fRotation))
                                    xsDataISPyBScreeningStrategy.setExposureTime(XSDataDouble(fExposureTime))
                                    if fTransmission is not None:
                                        xsDataISPyBScreeningStrategy.transmission = XSDataDouble(fTransmission)
                                    if (fCompleteness is not None):
                                        xsDataISPyBScreeningStrategy.setCompleteness(XSDataDouble(fCompleteness))
                                    if (fMultiplicity is not None):
                                        xsDataISPyBScreeningStrategy.setMultiplicity(XSDataDouble(fMultiplicity))
                                    if (fResolution is not None):
                                        xsDataISPyBScreeningStrategy.setResolution(XSDataDouble(fResolution))
                                    if (fRankingResolution is not None):
                                        xsDataISPyBScreeningStrategy.setRankingResolution(XSDataDouble(fRankingResolution))
                                    if (bAnomalousData is not None):
                                        xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(bAnomalousData))
                                    else:
                                        xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(False))
                                    xsDataISPyBScreeningStrategy.setProgram(XSDataString(pyStrProgram))
                                    if bFirstStrategy:
                                        bFirstStrategy = False
                                    else:
                                        _xsDataISPyBScreeningOutputContainer.addScreeningStrategyContainer(xsDataISPyBScreeningStrategyContainer)
