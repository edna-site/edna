#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
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

import math

from EDObject import EDObject
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose import EDVerbose

from XSDataCommon                   import XSDataDouble
from XSDataCommon                   import XSDataAngle
from XSDataCommon                   import XSDataString

from XSDataMXv1                     import XSDataResultStrategy
from XSDataMXv1                     import XSDataCollection
from XSDataMXv1                     import XSDataCollectionPlan
from XSDataMXv1                     import XSDataSubWedge
from XSDataMXv1                     import XSDataExperimentalCondition
from XSDataMXv1 import XSDataStrategySummary
from XSDataMXv1 import XSDataStatisticsStrategy

EDFactoryPluginStatic.loadModule("XSDataBestv1_2")
from XSDataBestv1_2 import XSDataInputBest


class EDHandlerXSDataBestv1_2(EDObject):

    def __init__(self):
        EDObject.__init__(self)


    def getXSDataInputBest(self, _xsDataInputStrategy):
        xsDataBeam = _xsDataInputStrategy.getExperimentalCondition().getBeam()
        xsDataSample = _xsDataInputStrategy.getSample()
        xsDataDetector = _xsDataInputStrategy.getExperimentalCondition().getDetector()
        xsDataGoniostat = _xsDataInputStrategy.getExperimentalCondition().getGoniostat()
        xsDataDiffractionPlan = _xsDataInputStrategy.getDiffractionPlan()
        xsDataStringBestFileContentDat = _xsDataInputStrategy.getBestFileContentDat()
        xsDataStringBestFileContentPar = _xsDataInputStrategy.getBestFileContentPar()
        xsDataFileXdsBackgroundImage = _xsDataInputStrategy.getXdsBackgroundImage()
        listXSDataStringBestFileContentHKL = _xsDataInputStrategy.getBestFileContentHKL()
        xsDataInputBest = XSDataInputBest()

        # Sample      
        xdDataAbsorbedDose = None
        xsDataSusceptibility = None

        # Could be None if sample has not been set
        # It could be not None in case Raddose has calculated an absorbed dose with default sample values
        if(xsDataSample is not None):
            xdDataAbsorbedDose = xsDataSample.getAbsorbedDoseRate()
            xsDataSusceptibility = xsDataSample.getSusceptibility()
            # crystalShape
            # Default value is 1 (We assume that Xtal is smaller than beam)
            xsDataDoubleCrystalShape = xsDataSample.getShape()
            if(xsDataDoubleCrystalShape is None):
                if (xsDataSample.getSize() is None) or (xsDataBeam.getSize() is None):
                    xsDataDoubleCrystalShape = XSDataDouble(1)
                else:
                    fCrystalSizeY = xsDataSample.getSize().getY().getValue()
                    fCrystalSizeZ = xsDataSample.getSize().getZ().getValue()
                    fDiagonal = math.sqrt(fCrystalSizeY ** 2 + fCrystalSizeZ ** 2)
                    fBeamSizeX = xsDataBeam.getSize().getX().getValue()
                    fCrystalShape = None
                    if fBeamSizeX > fDiagonal:
                        fCrystalShape = 1.0
                    else:
                        fCrystalShape = int(10 * fDiagonal / fBeamSizeX) / 10.0
                    xsDataDoubleCrystalShape = XSDataDouble(fCrystalShape)
            xsDataInputBest.setCrystalShape(xsDataDoubleCrystalShape)

        # Could be None if Raddose failed to calculate the absorbed dose
        if(xdDataAbsorbedDose is not None):
            xsDataInputBest.setCrystalAbsorbedDoseRate(xsDataSample.getAbsorbedDoseRate())

        xsDataInputBest.setCrystalSusceptibility(xsDataSusceptibility)


        # Detector
        xsDataInputBest.setDetectorType(xsDataDetector.getType())

        # Minimum exposure time per image
        xsDataTimeMinExposureTimePerImage = None
        if xsDataBeam:
            xsDataTimeMinExposureTimePerImage = xsDataBeam.getMinExposureTimePerImage()
        if xsDataTimeMinExposureTimePerImage == None:
            xsDataTimeMinExposureTimePerImage = xsDataDiffractionPlan.getMinExposureTimePerImage()
        xsDataInputBest.setBeamMinExposureTime(xsDataTimeMinExposureTimePerImage)

        # Max rotation speed
        xsDataAngularSpeedMax = None
        if xsDataGoniostat:
            xsDataAngularSpeedMax = xsDataGoniostat.getMaxOscillationSpeed()
        if xsDataDiffractionPlan and xsDataAngularSpeedMax == None:
            xsDataAngularSpeedMax = xsDataDiffractionPlan.getGoniostatMaxOscillationSpeed()
        xsDataInputBest.setGoniostatMaxRotationSpeed(xsDataAngularSpeedMax)

        # Min rotation width
        xsDataAngleMin = None
        if xsDataGoniostat:
            xsDataAngleMin = xsDataGoniostat.getMinOscillationWidth()
        if xsDataDiffractionPlan and xsDataAngleMin == None:
            xsDataAngleMin = xsDataDiffractionPlan.getGoniostatMinOscillationWidth()
        xsDataInputBest.setGoniostatMinRotationWidth(xsDataAngleMin)

        # Other beam parameters
        if xsDataBeam:
            xsDataInputBest.setBeamExposureTime(xsDataBeam.getExposureTime())
            if xsDataBeam.getTransmission():
                # Fix for bug 741: if the transmission is zero don't set it and warn the user
                fTransmission = xsDataBeam.getTransmission().getValue()
                if (abs(fTransmission) < 0.1):
                    EDVerbose.warning("Input transmission to BEST ignored because it is zero or close to zero: %f" % fTransmission)
                else:
                    xsDataInputBest.setTransmission(xsDataBeam.getTransmission())

        # Other diffraction plan parameters
        if xsDataDiffractionPlan:
            xsDataInputBest.setAimedResolution(xsDataDiffractionPlan.getAimedResolution())
            xsDataInputBest.setAimedRedundancy(xsDataDiffractionPlan.getAimedMultiplicity())
            xsDataInputBest.setAimedCompleteness(xsDataDiffractionPlan.getAimedCompleteness())
            xsDataInputBest.setAimedIOverSigma(xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution())
            xsDataInputBest.setBeamMaxExposureTime(xsDataDiffractionPlan.getMaxExposureTimePerDataCollection())
            xsDataInputBest.setComplexity(xsDataDiffractionPlan.getComplexity())
            xsDataInputBest.setAnomalousData(xsDataDiffractionPlan.getAnomalousData())
            xsDataInputBest.setStrategyOption(xsDataDiffractionPlan.getStrategyOption())
            xsDataInputBest.setMinTransmission(xsDataDiffractionPlan.getMinTransmission())
            xsDataInputBest.setNumberOfCrystalPositions(xsDataDiffractionPlan.getNumberOfPositions())
            xsDataInputBest.setDetectorDistanceMin(xsDataDiffractionPlan.getDetectorDistanceMin())
            xsDataInputBest.setDetectorDistanceMax(xsDataDiffractionPlan.getDetectorDistanceMax())

        # Best Files
        xsDataInputBest.setBestFileContentDat(xsDataStringBestFileContentDat)
        xsDataInputBest.setBestFileContentPar(xsDataStringBestFileContentPar)
        xsDataInputBest.setBestFileContentHKL(listXSDataStringBestFileContentHKL)
        xsDataInputBest.setXdsBackgroundImage(xsDataFileXdsBackgroundImage)

        return xsDataInputBest


    def getXSDataResultStrategy(self, _xsDataResultBest, _xsDataExperimentalCondition, _xsDataSample):
        xsDataResultStrategy = XSDataResultStrategy()

        listXSDataBestCollectionPlan = _xsDataResultBest.getCollectionPlan()

        for xsDataBestCollectionPlan in listXSDataBestCollectionPlan:

            xsDataCollectionPlan = XSDataCollectionPlan()
            xsDataCollectionStrategy = XSDataCollection()

            xsDataBestStrategySummary = xsDataBestCollectionPlan.getStrategySummary()

            xsDataDoubleTransmission = xsDataBestStrategySummary.getTransmission()

            for xsDataBestCollectionRun in xsDataBestCollectionPlan.getCollectionRun():
                xsDataSubWedge = XSDataSubWedge()
                strXmlStringDataExperimentalCondition = _xsDataExperimentalCondition.marshal()
                xsDataExperimentalCondition = XSDataExperimentalCondition.parseString(strXmlStringDataExperimentalCondition)
                xsDataExperimentalCondition.getBeam().setExposureTime(xsDataBestCollectionRun.getExposureTime())
                if (xsDataBestCollectionRun.getTransmission() is None):
                    xsDataExperimentalCondition.getBeam().setTransmission(xsDataDoubleTransmission)
                else:
                    xsDataExperimentalCondition.getBeam().setTransmission(xsDataBestCollectionRun.getTransmission())
                xsDataExperimentalCondition.getDetector().setDistance(xsDataBestStrategySummary.getDistance())
                xsDataExperimentalCondition.getGoniostat().setRotationAxisStart(xsDataBestCollectionRun.getPhiStart())
                xsDataExperimentalCondition.getGoniostat().setOscillationWidth(xsDataBestCollectionRun.getPhiWidth())
                fRotationAxisEnd = xsDataBestCollectionRun.getPhiStart().getValue() + xsDataBestCollectionRun.getNumberOfImages().getValue() * xsDataBestCollectionRun.getPhiWidth().getValue()
                xsDataExperimentalCondition.getGoniostat().setRotationAxisEnd(XSDataAngle(fRotationAxisEnd))
                xsDataSubWedge.setExperimentalCondition(xsDataExperimentalCondition)
                xsDataSubWedge.setSubWedgeNumber(xsDataBestCollectionRun.getCollectionRunNumber())
                if xsDataBestCollectionRun.getCrystalPosition():
                    xsDataSubWedge.setAction(XSDataString("Crystal position: %d" % xsDataBestCollectionRun.getCrystalPosition().getValue()))
                else:
                    xsDataSubWedge.setAction(xsDataBestCollectionRun.getAction())
                xsDataCollectionStrategy.addSubWedge(xsDataSubWedge)

            xsDataCollectionStrategy.setSample(_xsDataSample)

            xsDataCollectionPlan.setCollectionStrategy(xsDataCollectionStrategy)

            xsDataStrategySummary = XSDataStrategySummary()
            xsDataStrategySummary.setCompleteness(xsDataBestStrategySummary.getCompleteness())
            xsDataStrategySummary.setISigma(xsDataBestStrategySummary.getISigma())
            xsDataStrategySummary.setRankingResolution(xsDataBestStrategySummary.getRankingResolution())
            xsDataStrategySummary.setRedundancy(xsDataBestStrategySummary.getRedundancy())
            xsDataStrategySummary.setResolution(xsDataBestStrategySummary.getResolution())
            xsDataStrategySummary.setResolutionReasoning(xsDataBestStrategySummary.getResolutionReasoning())
            xsDataStrategySummary.setTotalDataCollectionTime(xsDataBestStrategySummary.getTotalDataCollectionTime())
            xsDataStrategySummary.setTotalExposureTime(xsDataBestStrategySummary.getTotalExposureTime())
            xsDataCollectionPlan.setStrategySummary(xsDataStrategySummary)

            if xsDataBestCollectionPlan.getStatisticalPrediction() is not None:
                xsDataStatisticsStrategy = XSDataStatisticsStrategy.parseString(xsDataBestCollectionPlan.getStatisticalPrediction().marshal())
                xsDataCollectionPlan.setStatistics(xsDataStatisticsStrategy)

            xsDataCollectionPlan.setCollectionPlanNumber(xsDataBestCollectionPlan.getCollectionPlanNumber())

            xsDataResultStrategy.addCollectionPlan(xsDataCollectionPlan)

        if _xsDataResultBest.getPathToLogFile() != None:
            xsDataResultStrategy.setBestLogFile(_xsDataResultBest.getPathToLogFile())

        return xsDataResultStrategy
