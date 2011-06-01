#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
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


from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

import time as PyTime

class EDHandlerXSDataISPyBv1_1:
    """
    """
    def generateXSDataInputISPyB(_xsDataInputControlISPyB, _strStatusMessage=None):
        """
        """
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_1")
        from XSDataISPyBv1_1 import XSDataString
        from XSDataISPyBv1_1 import XSDataBoolean
        from XSDataISPyBv1_1 import XSDataDouble
        from XSDataISPyBv1_1 import XSDataInteger
        from XSDataISPyBv1_1 import XSDataInputISPyB
        from XSDataISPyBv1_1 import XSDataISPyBScreening
        from XSDataISPyBv1_1 import XSDataISPyBScreeningInput
        from XSDataISPyBv1_1 import XSDataISPyBScreeningOutput
        from XSDataISPyBv1_1 import XSDataISPyBScreeningRank
        from XSDataISPyBv1_1 import XSDataISPyBScreeningRankSet
        from XSDataISPyBv1_1 import XSDatadbstatus
        from XSDataISPyBv1_1 import XSDataISPyBScreeningOutputContainer
        from XSDataISPyBv1_1 import XSDataISPyBScreeningOutputLattice
        from XSDataISPyBv1_1 import XSDataISPyBScreeningStrategy
        from XSDataISPyBv1_1 import XSDataISPyBDataCollection
        from XSDataISPyBv1_1 import XSDataISPyBImage
        from XSDataISPyBv1_1 import XSDataResultStatus

        xsDataInputISPyB = XSDataInputISPyB()
        xsDataISPyBScreeningInput = XSDataISPyBScreeningInput()
        xsDataIPSyBScreeningOutput = XSDataISPyBScreeningOutput()
        xsDataISPyBScreeningOutputContainer = XSDataISPyBScreeningOutputContainer()
        xsDataISPyBScreeningOutputLattice = XSDataISPyBScreeningOutputLattice()

        xsDataResultCharacterisation = _xsDataInputControlISPyB.getCharacterisationResult()
        xsDataIntegerDataCollectionId = _xsDataInputControlISPyB.getDataCollectionId()

        # General information
        xsDataISPyBScreening = XSDataISPyBScreening()
        xsDataISPyBScreening.setProgramVersion(XSDataString("EDNA MXv1"))
        pyStrTimeStamp = PyTime.strftime("%Y-%m-%d %H:%M:%S")
        xsDataISPyBScreening.setTimeStamp(XSDataString(pyStrTimeStamp))

        # Data collection information
        bAnomalousData = None
        pyStrPathToFirstImage = None
        xsDataCollection = xsDataResultCharacterisation.getDataCollection()
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
                pyListXSDataImage = xsDataSubWedgeFirst.getImage()
                if (pyListXSDataImage is not None):
                    xsDataImageFirst = pyListXSDataImage[ 0 ]
                    pyStrPathToFirstImage = xsDataImageFirst.getPath().getValue()
            xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
            if (xsDataDiffractionPlan is not None):
                if (xsDataDiffractionPlan.getAnomalousData() is not None):
                    bAnomalousData = xsDataDiffractionPlan.getAnomalousData().getValue()

        # Use dataCollectionId if provided in the input
        if (xsDataIntegerDataCollectionId is not None):
            xsDataISPyBScreening.setDataCollectionId(xsDataIntegerDataCollectionId)
        else:
            # Add an image path if the dataCollectionId is not present...
            if (pyStrPathToFirstImage is not None):
                xsDataISPyBImage = XSDataISPyBImage()
                pyStrImageBaseName = EDUtilsFile.getBaseName(pyStrPathToFirstImage)
                pyStrDirectoryName = EDUtilsPath.getFolderName(pyStrPathToFirstImage)
                xsDataISPyBImage.setFileName(XSDataString(pyStrImageBaseName))
                xsDataISPyBImage.setFileLocation(XSDataString(pyStrDirectoryName))
                xsDataInputISPyB.setImage(xsDataISPyBImage)

        # Indexing information
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
                    xsDataIPSyBScreeningOutput.setBeamShiftX(XSDataDouble(fBeamPositionShiftX))
                    xsDataIPSyBScreeningOutput.setBeamShiftY(XSDataDouble(fBeamPositionShiftY))
		    fSpotDeviationAngular = None
		    if xsDataStatisticsIndexing.getSpotDeviationAngular() is not None:
                        fSpotDeviationAngular = xsDataStatisticsIndexing.getSpotDeviationAngular().getValue()
                    fSpotDeviationPositional = xsDataStatisticsIndexing.getSpotDeviationPositional().getValue()
                    xsDataIPSyBScreeningOutput.setSpotDeviationR(XSDataDouble(fSpotDeviationPositional))
		    if fSpotDeviationAngular is not None:
                    	xsDataIPSyBScreeningOutput.setSpotDeviationTheta(XSDataDouble(fSpotDeviationAngular))
                    if ((xsDataStatisticsIndexing.getSpotsTotal() is not None) and (xsDataStatisticsIndexing.getSpotsUsed is not None)):
                        iSpotsTotal = xsDataStatisticsIndexing.getSpotsTotal().getValue()
                        iSpotsUsed = xsDataStatisticsIndexing.getSpotsUsed().getValue()
                        xsDataIPSyBScreeningOutput.setNumSpotsFound(XSDataInteger(iSpotsTotal))
                        xsDataIPSyBScreeningOutput.setNumSpotsUsed(XSDataInteger(iSpotsUsed))
                        xsDataIPSyBScreeningOutput.setNumSpotsRejected(XSDataInteger(iSpotsTotal - iSpotsUsed))
                xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
                xsDataIPSyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(False))
                if (xsDataCrystal is not None):
                    if (xsDataCrystal.getMosaicity() is not None):
                        fMosaicity = xsDataCrystal.getMosaicity().getValue()
                        xsDataIPSyBScreeningOutput.setMosaicity(XSDataDouble(fMosaicity))
                        xsDataIPSyBScreeningOutput.setMosaicityEstimated(XSDataBoolean(True))
                    xsDataCell = xsDataCrystal.getCell()
                    if (xsDataCell is not None):
                        fLength_a = xsDataCell.getLength_a().getValue()
                        fLength_b = xsDataCell.getLength_b().getValue()
                        fLength_c = xsDataCell.getLength_c().getValue()
                        fAngle_alpha = xsDataCell.getAngle_alpha().getValue()
                        fAngle_beta = xsDataCell.getAngle_beta().getValue()
                        fAngle_gamma = xsDataCell.getAngle_gamma().getValue()
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
            xsDataIPSyBScreeningOutput.setScreeningSuccess(XSDataBoolean(True))
	    if _strStatusMessage:
                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString("Indexing successful"))
        else:
            xsDataIPSyBScreeningOutput.setScreeningSuccess(XSDataBoolean(False))
	    if _strStatusMessage:
                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString(_strStatusMessage))
            else:
                xsDataIPSyBScreeningOutput.setStatusDescription(XSDataString("Indexing failed"))



        # Strategy information
        xsDataResultStrategy = xsDataResultCharacterisation.getStrategyResult()
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
                                xsDataISPyBScreeningStrategy = XSDataISPyBScreeningStrategy()
                                fPhiStart = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()
                                fPhiEnd = xsDataSubWedge.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
                                fRotation = xsDataSubWedge.getExperimentalCondition().getGoniostat().getOscillationWidth().getValue()
                                fExposureTime = xsDataSubWedge.getExperimentalCondition().getBeam().getExposureTime().getValue()
                                fTransmission = xsDataSubWedge.getExperimentalCondition().getBeam().getTransmission().getValue()
                                pyStrProgram = "BEST: Wedge no %d," % iCollectionPlanNumber
                                if (pyStrCollectionPlanComment is not None):
                                    pyStrProgram += " ( %s )" % pyStrCollectionPlanComment
                                pyStrProgram += " sub wedge no %d" % iSubWedgeNumber
                                xsDataISPyBScreeningStrategy.setPhiStart(XSDataDouble(fPhiStart))
                                xsDataISPyBScreeningStrategy.setPhiEnd(XSDataDouble(fPhiEnd))
                                xsDataISPyBScreeningStrategy.setRotation(XSDataDouble(fRotation))
                                xsDataISPyBScreeningStrategy.setExposureTime(XSDataDouble(fExposureTime))
                                xsDataISPyBScreeningStrategy.setTransmission(XSDataDouble(fTransmission))
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
                                xsDataISPyBScreeningOutputContainer.addScreeningStrategy(xsDataISPyBScreeningStrategy)



        xsDataInputISPyB.setScreening(xsDataISPyBScreening)
        xsDataInputISPyB.addScreeningInput(xsDataISPyBScreeningInput)
        xsDataISPyBScreeningOutputContainer.setScreeningOutput(xsDataIPSyBScreeningOutput)
        xsDataISPyBScreeningOutputContainer.addScreeningOutputLattice(xsDataISPyBScreeningOutputLattice)
        xsDataInputISPyB.addScreeningOutputContainer(xsDataISPyBScreeningOutputContainer)

        return xsDataInputISPyB
    generateXSDataInputISPyB = staticmethod(generateXSDataInputISPyB)

