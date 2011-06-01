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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from XSDataBestv1_1                 import XSDataInputBest
from XSDataCommon                   import XSDataFloat
from XSDataCommon                   import XSDataAngle
from XSDataMXv1                     import XSDataResultStrategy
from XSDataMXv1                     import XSDataCollection
from XSDataMXv1                     import XSDataCollectionPlan
from XSDataMXv1                     import XSDataSubWedge
from XSDataMXv1                     import XSDataExperimentalCondition



class EDHandlerXSDataBestv1_1:


    def getXSDataInputBest(self, _xsDataBeam, _xsDataSample, _xsDataDetector, _xsDataGoniostat, _xsDataDiffractionPlan,
                               _edStrBestFileContentDat, _edStrBestFileContentPar, _edListBestFileContentHKL):
        """
        """
        xsDataInputBest = XSDataInputBest()

        # Sample      
        xdDataAbsorbedDose = None
        xsDataSusceptibility = None

        # Could be None if sample has not been set
        # It could be not None in case Raddose has calculated an absorbed dose with default sample values
        if(_xsDataSample is not None):
            xdDataAbsorbedDose = _xsDataSample.getAbsorbedDoseRate()
            xsDataSusceptibility = _xsDataSample.getSusceptibility()

        # Could be None if Raddose failed to calculate the absorbed dose
        if(xdDataAbsorbedDose is not None):
            xsDataInputBest.setCrystalAbsorbedDoseRate(_xsDataSample.getAbsorbedDoseRate())

        xsDataInputBest.setCrystalSusceptibility(xsDataSusceptibility)

        # crystalShape
        # Default value is 1 (We assume that Xtal is smaller than beam)
        xsDataFloatCrystalShape = _xsDataSample.getShape()
        if(xsDataFloatCrystalShape is None):
            xsDataInputBest.setCrystalShape(XSDataFloat(1))
        else:
            xsDataInputBest.setCrystalShape(xsDataFloatCrystalShape)

        # Detector
        xsDataInputBest.setDetectorType(_xsDataDetector.getType())

        # Beam
        xsDataInputBest.setBeamExposureTime(_xsDataBeam.getExposureTime())
        xsDataInputBest.setBeamMinExposureTime(_xsDataBeam.getMinExposureTimePerImage())

        # Goniostat
        xsDataInputBest.setGoniostatMaxRotationSpeed(_xsDataGoniostat.getMaxOscillationSpeed())
        xsDataInputBest.setGoniostatMinRotationWidth(_xsDataGoniostat.getMinOscillationWidth())

        # Diffraction plan
        xsDataInputBest.setAimedResolution(_xsDataDiffractionPlan.getAimedResolution())
        xsDataInputBest.setAimedRedundancy(_xsDataDiffractionPlan.getAimedMultiplicity())
        xsDataInputBest.setAimedCompleteness(_xsDataDiffractionPlan.getAimedCompleteness())
        xsDataInputBest.setAimedIOverSigma(_xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution())
        xsDataInputBest.setBeamMaxExposureTime(_xsDataDiffractionPlan.getMaxExposureTimePerDataCollection())
        xsDataInputBest.setComplexity(_xsDataDiffractionPlan.getComplexity())
        xsDataInputBest.setAnomalousData(_xsDataDiffractionPlan.getAnomalousData())

        # Best Files
        xsDataInputBest.setBestFileContentDat(_edStrBestFileContentDat)
        xsDataInputBest.setBestFileContentPar(_edStrBestFileContentPar)
        xsDataInputBest.setBestFileContentHKL(_edListBestFileContentHKL)

        return xsDataInputBest


    def getXSDataResultStrategy(self, _xsDataResultBest, _xsDataExperimentalCondition, _xsDataSample):
        xsDataResultStrategy = XSDataResultStrategy()


        #xsDataCollectionRunsBest = _xsDataResultBest.getCollectionRun()
        xsDataCollectionPlansBest = _xsDataResultBest.getCollectionPlan()

        for xsDataCollectionPlanBest in xsDataCollectionPlansBest:

            xsDataCollectionPlan = XSDataCollectionPlan()
            xsDataCollectionStrategy = XSDataCollection()

            xsDataDoubleTransmission = xsDataCollectionPlanBest.getStrategySummary().getAttenuation()

            for xsDataCollectionRunBest in xsDataCollectionPlanBest.getCollectionRun():
                xsDataSubWedge = XSDataSubWedge()
                strXmlStringDataExperimentalCondition = _xsDataExperimentalCondition.marshal()
                xsDataExperimentalCondition = XSDataExperimentalCondition.parseString(strXmlStringDataExperimentalCondition)
                xsDataExperimentalCondition.getBeam().setExposureTime(xsDataCollectionRunBest.getExposureTime())
                xsDataExperimentalCondition.getBeam().setTransmission(xsDataDoubleTransmission)
                xsDataExperimentalCondition.getDetector().setDistance(xsDataCollectionRunBest.getDistance())
                xsDataExperimentalCondition.getGoniostat().setRotationAxisStart(xsDataCollectionRunBest.getPhiStart())
                xsDataExperimentalCondition.getGoniostat().setOscillationWidth(xsDataCollectionRunBest.getPhiWidth())
                fRotationAxisEnd = xsDataCollectionRunBest.getPhiStart().getValue() + xsDataCollectionRunBest.getNumberOfImages().getValue() * xsDataCollectionRunBest.getPhiWidth().getValue()
                xsDataExperimentalCondition.getGoniostat().setRotationAxisEnd(XSDataAngle(fRotationAxisEnd))
                xsDataSubWedge.setExperimentalCondition(xsDataExperimentalCondition)
                xsDataSubWedge.setSubWedgeNumber(xsDataCollectionRunBest.getCollectionRunNumber())
                xsDataCollectionStrategy.addSubWedge(xsDataSubWedge)

            xsDataCollectionStrategy.setSample(_xsDataSample)

            xsDataCollectionPlan.setCollectionStrategy(xsDataCollectionStrategy)
            xsDataStrategySummary = xsDataCollectionPlanBest.getStrategySummary()
            xsDataCollectionPlan.setStrategySummary(xsDataStrategySummary)

            xsDataStatistics = xsDataCollectionPlanBest.getStatisticalPrediction()
            xsDataCollectionPlan.setStatistics(xsDataStatistics)

            xsDataCollectionPlan.setCollectionPlanNumber(xsDataCollectionPlanBest.getCollectionPlanNumber())

            xsDataResultStrategy.addCollectionPlan(xsDataCollectionPlan)

        return xsDataResultStrategy
