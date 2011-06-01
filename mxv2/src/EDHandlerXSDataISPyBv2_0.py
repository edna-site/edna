#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDHandlerXSDataISPyBv2_0.py 1385 2010-04-20 11:41:19Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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

__author__ = "Olof Svensson, Karl Levik"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDVerbose import EDVerbose

import time

class EDHandlerXSDataISPyBv2_0:
    """
    """
    def generateXSDataISPyBScreening(_xsDataInputControlISPyB, _strShortComments=None, _strComments=None):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_2")
        from XSDataISPyBv1_2 import XSDataString
        from XSDataISPyBv1_2 import XSDataISPyBScreening

        xsDataIntegerDataCollectionId = _xsDataInputControlISPyB.getDataCollectionId()

        # General information
        xsDataISPyBScreening = XSDataISPyBScreening()
        xsDataISPyBScreening.setProgramVersion(XSDataString("EDNA MXv1"))
        pyStrTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S")
        xsDataISPyBScreening.setTimeStamp(XSDataString(pyStrTimeStamp))
        if (not _strShortComments is None):
            xsDataISPyBScreening.setShortComments(XSDataString(_strShortComments))
        if (not _strComments is None):
            xsDataISPyBScreening.setComments(XSDataString(_strComments))

        # Use dataCollectionId if provided in the input
        if (xsDataIntegerDataCollectionId is not None):
            xsDataISPyBScreening.setDataCollectionId(xsDataIntegerDataCollectionId)

        return xsDataISPyBScreening
    generateXSDataISPyBScreening = staticmethod(generateXSDataISPyBScreening)


    def getDataCollectionFromSuggestedStrategy(_xsDataResultCharacterisation):
        xsDataCollection = None
        xsDataResultStrategy = _xsDataResultCharacterisation.getSuggestedStrategy()
        if xsDataResultStrategy is not None:
            xsDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            if xsDataCollectionPlan is not None:
                EDVerbose.DEBUG("EDHandlerXSDataISPyBv2_0.getDataCollectionFromSuggestedStrategy: number of collections: " + str(len(xsDataCollectionPlan)))
                xsDataCollectionPlanFirst = xsDataCollectionPlan[0]
                xsDataCollection = xsDataCollectionPlanFirst.getCollectionStrategy()
        return xsDataCollection
    getDataCollectionFromSuggestedStrategy = staticmethod(getDataCollectionFromSuggestedStrategy)


    def generateXSDataISPyBScreeningInput(_xsDataInputControlISPyB):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_2")
        from XSDataISPyBv1_2 import XSDataISPyBScreeningInput
        from XSDataISPyBv1_2 import XSDataDouble

        xsDataResultCharacterisation = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataISPyBScreeningInput = XSDataISPyBScreeningInput()

        xsDataCollection = EDHandlerXSDataISPyBv2_0.getDataCollectionFromSuggestedStrategy(xsDataResultCharacterisation)

        # Data collection information
        if (xsDataCollection is not None):
            xsDataSubWedgeList = xsDataCollection.getSubWedge()
            if (xsDataSubWedgeList is not None):
                xsDataSubWedgeFirst = xsDataSubWedgeList[0]
                xsDataExperimentalCondition = xsDataSubWedgeFirst.getExperimentalCondition()
                if (xsDataExperimentalCondition is not None):
                    xsDataDetector = xsDataExperimentalCondition.getDetector()
                    if (xsDataDetector is not None):
                        fBeamPositionX = xsDataDetector.getBeamPositionX().getValue()
                        fBeamPositionY = xsDataDetector.getBeamPositionY().getValue()
                        xsDataISPyBScreeningInput.setBeamX(XSDataDouble(fBeamPositionX))
                        xsDataISPyBScreeningInput.setBeamY(XSDataDouble(fBeamPositionY))

        return xsDataISPyBScreeningInput
    generateXSDataISPyBScreeningInput = staticmethod(generateXSDataISPyBScreeningInput)


    def generateXSDataISPyBScreeningOutputContainer(_xsDataInputControlISPyB, _strStatusMessage=None):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_2")
        from XSDataISPyBv1_2 import XSDataISPyBScreeningOutputContainer
        from XSDataISPyBv1_2 import XSDataISPyBScreeningOutput
        from XSDataISPyBv1_2 import XSDataISPyBScreeningOutputLattice
        from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategyContainer
        from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategyWedgeContainer
        from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategy
        from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategyWedge
        from XSDataISPyBv1_2 import XSDataISPyBScreeningStrategySubWedge
        from XSDataISPyBv1_2 import XSDataDouble
        from XSDataISPyBv1_2 import XSDataInteger
        from XSDataISPyBv1_2 import XSDataBoolean
        from XSDataISPyBv1_2 import XSDataString
        import math
        EDFactoryPluginStatic.loadModule("EDHandlerXSDataCommon") # Needed for getting kappa and phi 
        from EDHandlerXSDataCommon import EDHandlerXSDataCommon   #

        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutputContainer.setScreeningOutput(xsDataISPyBScreeningOutput)

        xsDataResultCharacterisationv2_0 = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataResultCharacterisation = xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()
        xsDataResultStrategySuggested = xsDataResultCharacterisationv2_0.getSuggestedStrategy()

        # Determine whether anomalous data:
        bAnomalousData = None
        #xsDataCollection = xsDataResultCharacterisation.getDataCollection()
        xsDataCollection = EDHandlerXSDataISPyBv2_0.getDataCollectionFromSuggestedStrategy(xsDataResultCharacterisationv2_0)
        if (xsDataCollection is not None):
            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
            if (xsDataDiffractionPlan is not None):
                if (xsDataDiffractionPlan.getAnomalousData() is not None):
                    bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()


        # Indexing information (populate xsDataISPyBScreeningOutputContainer, xsDataIPSyBScreeningOutput and xsDataISPyBScreeningOutputLattice)
        bSuccessfulIndexing = False
        
        xsDataIndexingResult = xsDataResultCharacterisation.getIndexingResult()
        if (xsDataIndexingResult is not None):
            xsDataIndexingSolutionSelected = xsDataIndexingResult.getSelectedSolution()
            if (xsDataIndexingSolutionSelected is not None):
                bSuccessfulIndexing = True
                xsDataStatisticsIndexing = xsDataIndexingSolutionSelected.getStatistics()
                if (xsDataStatisticsIndexing is not None):
                    fBeamPositionShiftX = xsDataStatisticsIndexing.getBeamPositionShiftX().getValue()
                    fBeamPositionShiftY = xsDataStatisticsIndexing.getBeamPositionShiftY().getValue()
                    xsDataISPyBScreeningOutput.setBeamShiftX(XSDataDouble(fBeamPositionShiftX))
                    xsDataISPyBScreeningOutput.setBeamShiftY(XSDataDouble(fBeamPositionShiftY))
                    fSpotDeviationAngular = xsDataStatisticsIndexing.getSpotDeviationAngular().getValue()
                    fSpotDeviationPositional = xsDataStatisticsIndexing.getSpotDeviationPositional().getValue()
                    xsDataISPyBScreeningOutput.setSpotDeviationR(XSDataDouble(fSpotDeviationPositional))
                    xsDataISPyBScreeningOutput.setSpotDeviationTheta(XSDataDouble(fSpotDeviationAngular))
                    if ((xsDataStatisticsIndexing.getSpotsTotal() is not None) and (xsDataStatisticsIndexing.getSpotsUsed is not None)):
                        iSpotsTotal = xsDataStatisticsIndexing.getSpotsTotal().getValue()
                        iSpotsUsed = xsDataStatisticsIndexing.getSpotsUsed().getValue()
                        xsDataISPyBScreeningOutput.setNumSpotsFound(XSDataInteger(iSpotsTotal))
                        xsDataISPyBScreeningOutput.setNumSpotsUsed(XSDataInteger(iSpotsUsed))
                        xsDataISPyBScreeningOutput.setNumSpotsRejected(XSDataInteger(iSpotsTotal - iSpotsUsed))
                xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
                xsDataISPyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(False))
                if (xsDataCrystal is not None):
                    if (xsDataCrystal.getMosaicity() is not None):
                        fMosaicity = xsDataCrystal.getMosaicity().getValue()
                        xsDataISPyBScreeningOutput.setMosaicity(XSDataDouble(fMosaicity))
                        xsDataISPyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(True))
                    xsDataCell = xsDataCrystal.getCell()
                    if (xsDataCell is not None):
                        fLength_a = xsDataCell.getLength_a().getValue()
                        fLength_b = xsDataCell.getLength_b().getValue()
                        fLength_c = xsDataCell.getLength_c().getValue()
                        fAngle_alpha = xsDataCell.getAngle_alpha().getValue()
                        fAngle_beta = xsDataCell.getAngle_beta().getValue()
                        fAngle_gamma = xsDataCell.getAngle_gamma().getValue()

                        xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()
                        xsDataISPyBScreeningOutputContainer.getScreeningOutputLattice().append(xsDataISPyBScreeningOutputLattice)

                        xsDataISPyBScreeningOutputLattice.setUnitCell_a(XSDataDouble(fLength_a))
                        xsDataISPyBScreeningOutputLattice.setUnitCell_b(XSDataDouble(fLength_b))
                        xsDataISPyBScreeningOutputLattice.setUnitCell_c(XSDataDouble(fLength_c))
                        xsDataISPyBScreeningOutputLattice.setUnitCell_alpha(XSDataDouble(fAngle_alpha))
                        xsDataISPyBScreeningOutputLattice.setUnitCell_beta(XSDataDouble(fAngle_beta))
                        xsDataISPyBScreeningOutputLattice.setUnitCell_gamma(XSDataDouble(fAngle_gamma))
                    xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
                    if (xsDataSpaceGroup is not None):
                        pyStrSpaceGroupName = xsDataSpaceGroup.getName().getValue()
                        xsDataISPyBScreeningOutputLattice.setSpaceGroup(XSDataString(pyStrSpaceGroupName))
        if (bSuccessfulIndexing):
            if _strStatusMessage == None:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing successful"))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            xsDataISPyBScreeningOutput.setScreeningSuccess(XSDataBoolean(True))
        else:
            if _strStatusMessage == None:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString("Indexing failed"))
            else:
                xsDataISPyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            xsDataISPyBScreeningOutput.setScreeningSuccess(XSDataBoolean(False))



        # Strategy information (populate xsDataISPyBScreeningStrategyContainer, xsDataISPyBScreeningStrategyWedge, xsDataISPyBScreeningStrategySubWedge)
        xsDataResultStrategy = xsDataResultStrategySuggested # xsDataResultCharacterisation.getStrategyResult()

        xsDataISPyBScreeningStrategyContainer = XSDataISPyBScreeningStrategyContainer()
        xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
        xsDataISPyBScreeningStrategyContainer.setScreeningStrategy(xsDataISPyBScreeningStrategy)
        xsDataISPyBScreeningOutputContainer.getScreeningStrategyContainer().append(xsDataISPyBScreeningStrategyContainer)
        fAccumulatedExposureTime = 0.0

        if (bAnomalousData is not None):
            xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(bAnomalousData))
        else:
            xsDataISPyBScreeningStrategy.setAnomalous(XSDataBoolean(False))

        xsDataISPyBScreeningStrategy.setProgram(XSDataString("STAC"))

        if (xsDataResultStrategy is not None):
            lXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            if (lXSDataCollectionPlan is not None):
                for xsDataCollectionPlan in lXSDataCollectionPlan:
                    iCollectionPlanNumber = xsDataCollectionPlan.getCollectionPlanNumber().getValue()

                    #strCollectionPlanComment = None
                    #if (xsDataCollectionPlan.getComment() is not None):
                    #    strCollectionPlanComment = xsDataCollectionPlan.getComment().getValue()
                    fCompleteness = None
                    fMultiplicity = None
                    fResolution = None
                    fRankingResolution = None
                    fTransmission = None
                    iWedgeNumberOfImages = 0
                    fWedgeDoseTotal = 0.0
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
                            xsDataISPyBScreeningStrategy.setRankingResolution(XSDataDouble(fRankingResolution))

                    xsDataISPyBScreeningStrategyWedgeContainer = XSDataISPyBScreeningStrategyWedgeContainer()
                    xsDataISPyBScreeningStrategyWedge = XSDataISPyBScreeningStrategyWedge()
                    xsDataISPyBScreeningStrategyWedgeContainer.setScreeningStrategyWedge(xsDataISPyBScreeningStrategyWedge)
                    xsDataISPyBScreeningStrategyContainer.getScreeningStrategyWedgeContainer().append(xsDataISPyBScreeningStrategyWedgeContainer)

                    xsDataISPyBScreeningStrategyWedge.setWedgeNumber(XSDataInteger(iCollectionPlanNumber))
                    xsDataISPyBScreeningStrategyWedge.setCompleteness(XSDataDouble(fCompleteness))
                    xsDataISPyBScreeningStrategyWedge.setMultiplicity(XSDataDouble(fMultiplicity))
                    xsDataISPyBScreeningStrategyWedge.setResolution(XSDataDouble(fResolution))
                    
                    # Find kappa and phi
                    xsDataStringComment = xsDataCollectionPlan.getComment()
                    xsDataDoubleOmega = EDHandlerXSDataCommon.getElements(xsDataStringComment, "OMEGA=")
                    xsDataDoubleKappa = EDHandlerXSDataCommon.getElements(xsDataStringComment, "KAPPA=")
                    xsDataDoublePhi = EDHandlerXSDataCommon.getElements(xsDataStringComment, "PHI=")
                                        
                    xsDataISPyBScreeningStrategyWedge.setKappa(xsDataDoubleKappa)
                    xsDataISPyBScreeningStrategyWedge.setPhi(xsDataDoublePhi)

                    xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                    if (xsDataCollectionStrategy is not None):
                        lXSDataSubWedge = xsDataCollectionStrategy.getSubWedge()
                        if (lXSDataSubWedge is not None):
                            for xsDataSubWedge in lXSDataSubWedge:
                                iSubWedgeNumber = xsDataSubWedge.getSubWedgeNumber().getValue()
                                fPhiStart = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()
                                fPhiEnd = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
                                fRotation = xsDataSubWedge.getExperimentalCondition().getGoniostat().getOscillationWidth().getValue()
                                fExposureTime = xsDataSubWedge.getExperimentalCondition().getBeam().getExposureTime().getValue()
                                fAccumulatedExposureTime += fExposureTime
                                xsDataDoubleTransmission = xsDataSubWedge.getExperimentalCondition().getBeam().getTransmission()
                                if (xsDataDoubleTransmission is not None): 
                                    fTransmission = xsDataDoubleTransmission.getValue()
                                else:
                                    fTransmission = None
                                if (not xsDataSubWedge.getExperimentalCondition().getBeam().getFlux() is None):
                                    fFlux = xsDataSubWedge.getExperimentalCondition().getBeam().getFlux().getValue()
                                else:
                                    fFlux = None
                                iNumberOfImages = int(math.ceil((fPhiEnd - fPhiStart) / fRotation))

                                xsDataISPyBScreeningStrategySubWedge = XSDataISPyBScreeningStrategySubWedge()
                                xsDataISPyBScreeningStrategyWedgeContainer.getScreeningStrategySubWedge().append(xsDataISPyBScreeningStrategySubWedge)

                                xsDataISPyBScreeningStrategySubWedge.setSubWedgeNumber(XSDataInteger(iSubWedgeNumber))
                                xsDataISPyBScreeningStrategySubWedge.setAxisStart(XSDataDouble(fPhiStart))
                                xsDataISPyBScreeningStrategySubWedge.setAxisEnd(XSDataDouble(fPhiEnd))
                                xsDataISPyBScreeningStrategySubWedge.setRotationAxis(XSDataString("Omega"))
                                xsDataISPyBScreeningStrategySubWedge.setOscillationRange(XSDataDouble(fRotation))
                                xsDataISPyBScreeningStrategySubWedge.setExposureTime(XSDataDouble(fExposureTime))
                                if (fTransmission is not None):
                                    xsDataISPyBScreeningStrategySubWedge.setTransmission(XSDataDouble(fTransmission))
                                xsDataISPyBScreeningStrategySubWedge.setNumberOfImages(XSDataInteger(iNumberOfImages))
                                iWedgeNumberOfImages += iNumberOfImages

                                if (fFlux is not None):
                                    xsDataISPyBScreeningStrategySubWedge.setDoseTotal(XSDataDouble(fFlux))
                                    fWedgeDoseTotal += fFlux
                                if (fCompleteness is not None):
                                    xsDataISPyBScreeningStrategySubWedge.setCompleteness(XSDataDouble(fCompleteness))
                                if (fMultiplicity is not None):
                                    xsDataISPyBScreeningStrategySubWedge.setMultiplicity(XSDataDouble(fMultiplicity))
                                if (fResolution is not None):
                                    xsDataISPyBScreeningStrategySubWedge.setResolution(XSDataDouble(fResolution))

                    xsDataISPyBScreeningStrategyWedge.setNumberOfImages(XSDataInteger(iWedgeNumberOfImages))
                    xsDataISPyBScreeningStrategyWedge.setDoseTotal(XSDataDouble(fWedgeDoseTotal))

        xsDataISPyBScreeningStrategy.setExposureTime(XSDataDouble(fAccumulatedExposureTime))
        return xsDataISPyBScreeningOutputContainer
    generateXSDataISPyBScreeningOutputContainer = staticmethod(generateXSDataISPyBScreeningOutputContainer)


    def generateXSDataISPyBImage(_xsDataInputControlISPyB):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_2")
        from XSDataISPyBv1_2 import XSDataString
        from XSDataISPyBv1_2 import XSDataISPyBImage
        xsDataResultCharacterisationv2_0 = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataResultCharacterisation = xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()

        xsDataISPyBImage = None
        # Find path to first image from data collection information
        strPathToFirstImage = None
        xsDataCollection = xsDataResultCharacterisation.getDataCollection()
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
                strImageBaseName = EDUtilsFile.getBaseName(strPathToFirstImage)
                strDirectoryName = EDUtilsPath.getFolderName(strPathToFirstImage)
                xsDataISPyBImage.setFileName(XSDataString(strImageBaseName))
                xsDataISPyBImage.setFileLocation(XSDataString(strDirectoryName))
        return xsDataISPyBImage
    generateXSDataISPyBImage = staticmethod(generateXSDataISPyBImage)


