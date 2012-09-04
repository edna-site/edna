#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
#
#    Contributors:           Marie-Francoise Incardona (incardon@esrf.fr)
#                            Karl Levik (karl.levik@diamond.ac.uk)
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDUtilsSymmetry import EDUtilsSymmetry
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength

from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataIndexingResult
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataIndexingSolution
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataStatisticsIndexing
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataOrientation


class EDHandlerXSDataLabelitv10:


    @staticmethod
    def generateXSDataInputLabelit(_xsDataIndexingInput):

        EDFactoryPluginStatic.loadModule("XSDataLabelitv10")
        from XSDataLabelitv10 import XSDataInputLabelit
        xsDataInputLabelit = XSDataInputLabelit()

        xsDataCollection = _xsDataIndexingInput.getDataCollection()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()

        xsDataInputLabelit.addImage(xsDataSubWedgeList[0].getImage()[0])
        fPhiStartFirst = xsDataSubWedgeList[0].getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()

        if (len(xsDataSubWedgeList) > 1):

            xsDataImageSecond = xsDataSubWedgeList[-1].getImage()[0]
            fPhiStartSecond = xsDataSubWedgeList[-1].getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()

            # Add modulus!            
            if (abs(fPhiStartSecond - fPhiStartFirst) > 4):

                xsDataInputLabelit.addImage(xsDataImageSecond)

        return xsDataInputLabelit


    @staticmethod
    def generateXSDataIndexingResult(_xsDataResultLabelit, _xsDataExperimentalCondition=None):

        xsDataLabelitScreenOutput = _xsDataResultLabelit.getLabelitScreenOutput()
        xsDataLabelitMosflmScriptsOutput = _xsDataResultLabelit.getLabelitMosflmScriptsOutput()

        iSelectedSolutionNumber = xsDataLabelitScreenOutput.getSelectedSolutionNumber().getValue()

        xsDataIndexingResult = XSDataIndexingResult()
        xsDataIndexingSolutionSelected = None

        for xsDataLabelitSolution in xsDataLabelitScreenOutput.getLabelitScreenSolution():
            xsDataCrystal = XSDataCrystal()
            xsDataSpaceGroup = XSDataSpaceGroup()
            edStringSpaceGroupName = EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(xsDataLabelitSolution.getBravaisLattice().getValue())
            xsDataSpaceGroup.setName(XSDataString(edStringSpaceGroupName))
            xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)
            xsDataCrystal.setCell(xsDataLabelitSolution.getUnitCell())
            xsDataIndexingSolution = XSDataIndexingSolution()
            xsDataIndexingSolution.setCrystal(xsDataCrystal)
            iIndex = xsDataLabelitSolution.getSolutionNumber().getValue()
            xsDataIndexingSolution.setNumber(XSDataInteger(iIndex))
            xsDataIndexingResult.addSolution(xsDataIndexingSolution)
            if (iIndex == iSelectedSolutionNumber):
                xsDataIndexingSolutionSelected = XSDataIndexingSolutionSelected()
                xsDataIndexingSolutionSelected.setNumber(XSDataInteger(iIndex))
                edStringSelectedSpaceGroupName = edStringSpaceGroupName
                xsDataCellSelected = xsDataLabelitSolution.getUnitCell()
                fRmsdSelected = xsDataLabelitSolution.getRmsd().getValue()
                iNumberOfSpotsSelected = xsDataLabelitSolution.getNumberOfSpots().getValue()

        xsDataCrystalSelected = XSDataCrystal()
        xsDataSpaceGroupSelected = XSDataSpaceGroup()
        xsDataSpaceGroupSelected.setName(XSDataString(edStringSelectedSpaceGroupName))
        #xsDataSpaceGroupSelected.setITNumber( XSDataInteger( iSelectedSpaceGroupNumber ) )
        xsDataCrystalSelected.setSpaceGroup(xsDataSpaceGroupSelected)
        xsDataCrystalSelected.setCell(xsDataCellSelected)
        xsDataCrystalSelected.setMosaicity(XSDataDouble(xsDataLabelitScreenOutput.getMosaicity().getValue()))
        xsDataIndexingSolutionSelected.setCrystal(xsDataCrystalSelected)

        xsDataOrientation = XSDataOrientation()
        xsDataOrientation.setMatrixA(xsDataLabelitMosflmScriptsOutput.getAMatrix())
        xsDataOrientation.setMatrixU(xsDataLabelitMosflmScriptsOutput.getUMatrix())
        xsDataIndexingSolutionSelected.setOrientation(xsDataOrientation)

        xsDataStatisticsIndexing = XSDataStatisticsIndexing()

        if (_xsDataExperimentalCondition is not None):
            fBeamPositionXOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionX().getValue()
            fBeamPositionYOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionY().getValue()
            fBeamPositionXNew = xsDataLabelitScreenOutput.getBeamCentreX().getValue()
            fBeamPositionYNew = xsDataLabelitScreenOutput.getBeamCentreY().getValue()
            xsDataStatisticsIndexing.setBeamPositionShiftX(XSDataLength(fBeamPositionXOrig - fBeamPositionXNew))
            xsDataStatisticsIndexing.setBeamPositionShiftY(XSDataLength(fBeamPositionYOrig - fBeamPositionYNew))

        #xsDataStatisticsIndexing.setSpotDeviXSDataLength( dDistanceRefinedationAngular( XSDataAngle( dDeviationAngular ) )
        xsDataStatisticsIndexing.setSpotDeviationPositional(XSDataLength(fRmsdSelected))
        xsDataStatisticsIndexing.setSpotsUsed(XSDataInteger(iNumberOfSpotsSelected))
        xsDataStatisticsIndexing.setSpotsTotal(XSDataInteger(iNumberOfSpotsSelected))
        xsDataIndexingSolutionSelected.setStatistics(xsDataStatisticsIndexing)

        xsDataExperimentalConditionRefined = None
        if (_xsDataExperimentalCondition is None):
            xsDataExperimentalConditionRefined = XSDataExperimentalCondition()
        else:
            # Copy the incoming experimental condition
            xmlExperimentalCondition = _xsDataExperimentalCondition.marshal()
            xsDataExperimentalConditionRefined = XSDataExperimentalCondition.parseString(xmlExperimentalCondition)

        xsDataDetector = xsDataExperimentalConditionRefined.getDetector()
        if (xsDataDetector is None):
            xsDataDetector = XSDataDetector()

        xsDataDetector.setBeamPositionX(xsDataLabelitScreenOutput.getBeamCentreX())
        xsDataDetector.setBeamPositionY(xsDataLabelitScreenOutput.getBeamCentreY())
        xsDataDetector.setDistance(xsDataLabelitScreenOutput.getDistance())

        xsDataExperimentalConditionRefined.setDetector(xsDataDetector)
        xsDataIndexingSolutionSelected.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

        xsDataIndexingResult.setSelectedSolution(xsDataIndexingSolutionSelected)

        return xsDataIndexingResult
