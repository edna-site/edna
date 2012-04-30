#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
Translation between XSDataMOSFLMv10 and MXv1 data models.
"""

import os

from EDVerbose import EDVerbose

#from EDMessage    import EDMessage
from EDUtilsImage import EDUtilsImage
from EDFactoryPluginStatic import EDFactoryPluginStatic

#from XSDataCommon import XSDataMatrix
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataWavelength
#from XSDataCommon import XSDataImage

from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataStatisticsIntegrationAverageAndNumberOfReflections
from XSDataMXv1 import XSDataStatisticsIntegrationPerResolutionBin
from XSDataMXv1 import XSDataStatisticsIntegrationPerReflectionType
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataIndexingResult
from XSDataMXv1 import XSDataIndexingSolution
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataOrientation
from XSDataMXv1 import XSDataStatisticsIndexing
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataIntegrationSubWedgeResult
from XSDataMXv1 import XSDataStatisticsIntegration


class EDHandlerXSDataMOSFLMv10:
    """
    Translation between XSDataMOSFLMv10 and MXv1 data models.
    """

    def generateXSDataMOSFLMInputIndexing(_xsDataIndexingInput):
        """
        Translation from XSDataIndexingInput to XSDataMOSFLMInputIndexing.
        """
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIndexing
        from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
        from XSDataMOSFLMv10 import XSDataMOSFLMImage

        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing")

        xsDataCollection = _xsDataIndexingInput.getDataCollection()
        xsDataExperimentalCondition = _xsDataIndexingInput.getExperimentalCondition()
        xsDataCrystal = _xsDataIndexingInput.getCrystal()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()
        xsDataMOSFLMInputIndexing = XSDataMOSFLMInputIndexing()

        if (xsDataExperimentalCondition is None):
            xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()

        xsDataBeam = xsDataExperimentalCondition.getBeam()
        xsDataDetector = xsDataExperimentalCondition.getDetector()
        xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()

        dWavelength = xsDataBeam.getWavelength().getValue()
        dDistance = xsDataDetector.getDistance().getValue()
        dBeamPositionX = xsDataDetector.getBeamPositionX().getValue()
        dBeamPositionY = xsDataDetector.getBeamPositionY().getValue()

        xsDataMOSFLMBeamPosition = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeamPosition.setX(XSDataLength(dBeamPositionX))
        xsDataMOSFLMBeamPosition.setY(XSDataLength(dBeamPositionY))
        xsDataMOSFLMInputIndexing.setBeam(xsDataMOSFLMBeamPosition)

        xsDataMOSFLMDetector = EDHandlerXSDataMOSFLMv10.getXSDataMOSFLMDetector(xsDataDetector)
        xsDataMOSFLMInputIndexing.setDetector(xsDataMOSFLMDetector)

        xsDataMOSFLMInputIndexing.setWavelength(XSDataWavelength(dWavelength))
        xsDataMOSFLMInputIndexing.setDistance(XSDataLength(dDistance))

        xsDataSubWedgeFirst = xsDataSubWedgeList[0]
        xsDataImageFirst = xsDataSubWedgeFirst.getImage()[0]
        strPath = xsDataImageFirst.getPath().getValue()
        strFileName = os.path.basename(strPath)
        strDirectory = os.path.dirname(strPath)

        strMOSFLMTemplate = EDUtilsImage.getTemplate(strFileName, "#")
        xsDataMOSFLMInputIndexing.setTemplate(XSDataString(strMOSFLMTemplate))
        xsDataMOSFLMInputIndexing.setDirectory(XSDataString(strDirectory))

        if (xsDataCrystal is not None):
            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
            if (xsDataSpaceGroup is not None):
                xsDataStringName = xsDataSpaceGroup.getName()
                if (xsDataStringName is not None):
                    xsDataMOSFLMInputIndexing.setSymmetry(XSDataString(xsDataStringName.getValue()))

        # Loop through the list of sub wedges 

        for xsDataSubWedge in xsDataSubWedgeList:

            xsDataImageList = xsDataSubWedge.getImage()
            xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()
            fGonioStatOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
            fGonioStatOscillationRange = xsDataGoniostat.getOscillationWidth().getValue()

            # First find the lowest image number
            iLowestImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                if (iLowestImageNumber is None):
                    iLowestImageNumber = iImageNumber
                elif (iImageNumber < iLowestImageNumber):
                    iLowestImageNumber = iImageNumber

            # Loop through the list of images

            for xsDataImage in xsDataImageList:
                # Create the MOSFLM image object

                xsDataMOSFLMImage = XSDataMOSFLMImage()

                iImageNumber = xsDataImage.getNumber().getValue()
                xsDataMOSFLMImage.setNumber(XSDataInteger(iImageNumber))

                fImageOscillationStart = fGonioStatOscillationStart + (iImageNumber - iLowestImageNumber) * fGonioStatOscillationRange
                xsDataMOSFLMImage.setRotationAxisStart(XSDataAngle(fImageOscillationStart))
                xsDataMOSFLMImage.setRotationAxisEnd(XSDataAngle(fImageOscillationStart + fGonioStatOscillationRange))

                xsDataMOSFLMInputIndexing.addImage(xsDataMOSFLMImage)

        return xsDataMOSFLMInputIndexing
    generateXSDataMOSFLMInputIndexing = staticmethod(generateXSDataMOSFLMInputIndexing)



    def generateXSDataIndexingResult(_xsDataMOSFLMIndexingOutput, _xsDataExperimentalCondition=None):
        """
        Translation from XSDataMOSFLMIndexingOutput to XSDataIndexingResult.
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.generateXSDataIndexingOutput")
        xsDataMOSFLMBeamPositionRefined = _xsDataMOSFLMIndexingOutput.getRefinedBeam()
        xsDataMOSFLMBeamPositionShift = _xsDataMOSFLMIndexingOutput.getBeamShift()
        dDeviationAngular = _xsDataMOSFLMIndexingOutput.getDeviationAngular().getValue()
        dDeviationPositional = _xsDataMOSFLMIndexingOutput.getDeviationPositional().getValue()
        dMosaicityEstimation = _xsDataMOSFLMIndexingOutput.getMosaicityEstimation().getValue()
        dDistanceRefined = _xsDataMOSFLMIndexingOutput.getRefinedDistance().getValue()
        iSelectedSolution = _xsDataMOSFLMIndexingOutput.getSelectedSolutionNumber().getValue()
        iSpotsTotal = _xsDataMOSFLMIndexingOutput.getSpotsTotal().getValue()
        iSpotsUsed = _xsDataMOSFLMIndexingOutput.getSpotsUsed().getValue()
        xsDataCellRefined = _xsDataMOSFLMIndexingOutput.getRefinedNewmat().getRefinedCell()
        xsDataMatrixA = _xsDataMOSFLMIndexingOutput.getRefinedNewmat().getAMatrix()
        xsDataMatrixU = _xsDataMOSFLMIndexingOutput.getRefinedNewmat().getUMatrix()
        strSelectedSpaceGroupName = _xsDataMOSFLMIndexingOutput.getSelectedSolutionSpaceGroup().getValue()
        iSelectedSpaceGroupNumber = _xsDataMOSFLMIndexingOutput.getSelectedSolutionSpaceGroupNumber().getValue()

        xsDataIndexingResult = XSDataIndexingResult()
        xsDataIndexingSolutionSelected = None

        for possibleSolutions in _xsDataMOSFLMIndexingOutput.getPossibleSolutions():
            xsDataCrystal = XSDataCrystal()
            xsDataSpaceGroup = XSDataSpaceGroup()
            xsDataSpaceGroup.setName(XSDataString(possibleSolutions.getLattice().getValue()))
            xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)
            xsDataCrystal.setCell(possibleSolutions.getCell())
            xsDataIndexingSolution = XSDataIndexingSolution()
            xsDataIndexingSolution.setCrystal(xsDataCrystal)
            iIndex = possibleSolutions.getIndex().getValue()
            xsDataIndexingSolution.setNumber(XSDataInteger(iIndex))
            xsDataIndexingSolution.setPenalty(XSDataFloat(possibleSolutions.getPenalty().getValue()))
            xsDataIndexingResult.addSolution(xsDataIndexingSolution)
            if (iIndex == iSelectedSolution):
                xsDataIndexingSolutionSelected = XSDataIndexingSolutionSelected()
                xsDataIndexingSolutionSelected.setNumber(XSDataInteger(iIndex))
                xsDataIndexingSolutionSelected.setPenalty(XSDataFloat(possibleSolutions.getPenalty().getValue()))

        xsDataCrystalSelected = XSDataCrystal()
        xsDataSpaceGroupSelected = XSDataSpaceGroup()
        xsDataSpaceGroupSelected.setName(XSDataString(strSelectedSpaceGroupName))
        xsDataSpaceGroupSelected.setITNumber(XSDataInteger(iSelectedSpaceGroupNumber))
        xsDataCrystalSelected.setSpaceGroup(xsDataSpaceGroupSelected)
        xsDataCrystalSelected.setCell(xsDataCellRefined)
        xsDataCrystalSelected.setMosaicity(XSDataDouble(dMosaicityEstimation))
        xsDataIndexingSolutionSelected.setCrystal(xsDataCrystalSelected)

        xsDataOrientation = XSDataOrientation()
        xsDataOrientation.setMatrixA(xsDataMatrixA)
        xsDataOrientation.setMatrixU(xsDataMatrixU)
        xsDataIndexingSolutionSelected.setOrientation(xsDataOrientation)

        xsDataStatisticsIndexing = XSDataStatisticsIndexing()

        xsDataStatisticsIndexing.setBeamPositionShiftX(XSDataLength(xsDataMOSFLMBeamPositionShift.getX().getValue()))
        xsDataStatisticsIndexing.setBeamPositionShiftY(XSDataLength(xsDataMOSFLMBeamPositionShift.getY().getValue()))
        xsDataStatisticsIndexing.setSpotDeviationAngular(XSDataAngle(dDeviationAngular))
        xsDataStatisticsIndexing.setSpotDeviationPositional(XSDataLength(dDeviationPositional))
        xsDataStatisticsIndexing.setSpotsUsed(XSDataInteger(iSpotsUsed))
        xsDataStatisticsIndexing.setSpotsTotal(XSDataInteger(iSpotsTotal))
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

        xsDataDetector.setBeamPositionX(XSDataLength(xsDataMOSFLMBeamPositionRefined.getX().getValue()))
        xsDataDetector.setBeamPositionY(XSDataLength(xsDataMOSFLMBeamPositionRefined.getY().getValue()))
        xsDataDetector.setDistance(XSDataLength(dDistanceRefined))

        xsDataExperimentalConditionRefined.setDetector(xsDataDetector)
        xsDataIndexingSolutionSelected.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

        xsDataIndexingResult.setSelectedSolution(xsDataIndexingSolutionSelected)

        return xsDataIndexingResult
    generateXSDataIndexingResult = staticmethod(generateXSDataIndexingResult)


    def generateXSDataMOSFLMInputIntegration(_xsDataIntegrationInput):
        """
        Translation from XSDataIntegrationInput to XSDataMOSFLMInputIntegration.
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIntegration")
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
        from XSDataMOSFLMv10 import XSDataMOSFLMInputIntegration
        from XSDataMOSFLMv10 import XSDataMOSFLMNewmat
        from XSDataMOSFLMv10 import XSDataMOSFLMMissettingsAngles
        xsDataCrystalRefined = _xsDataIntegrationInput.getCrystalRefined()
        xsDataIndexingSolutionSelected = _xsDataIntegrationInput.getSelectedIndexingSolution()

        if (xsDataCrystalRefined is None):
            xsDataCrystalRefined = xsDataIndexingSolutionSelected.getCrystal()

        xsDataCollection = _xsDataIntegrationInput.getDataCollection()
        xsDataSubWedge = xsDataCollection.getSubWedge()[0]
        xsDataImageList = xsDataSubWedge.getImage()
        xsDataImageFirst = xsDataImageList[0]
        xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()

        xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
        xsDataOrientation = xsDataIndexingSolutionSelected.getOrientation()
        xsDataExperimentalCondition = xsDataIndexingSolutionSelected.getExperimentalConditionRefined()
        xsDataDetector = xsDataExperimentalCondition.getDetector()
        xsDataBeam = xsDataExperimentalCondition.getBeam()
        xsDataMatrixA = xsDataOrientation.getMatrixA()
        xsDataMatrixU = xsDataOrientation.getMatrixU()
        xsDataCell = xsDataCrystal.getCell()

        xsDataMOSFLMInputIntegration = XSDataMOSFLMInputIntegration()
        xsDataMOSFLMNewmat = XSDataMOSFLMNewmat()
        xsDataMOSFLMNewmat.setRefinedCell(xsDataCell)
        xsDataMOSFLMNewmat.setAMatrix(xsDataMatrixA)
        xsDataMOSFLMNewmat.setUMatrix(xsDataMatrixU)
        xsDataMOSFLMInputIntegration.setMatrix(xsDataMOSFLMNewmat)

        xsDataMOSFLMMissettingsAngles = XSDataMOSFLMMissettingsAngles()
        xsDataMOSFLMMissettingsAngles.setPhix(XSDataAngle(0.0))
        xsDataMOSFLMMissettingsAngles.setPhiy(XSDataAngle(0.0))
        xsDataMOSFLMMissettingsAngles.setPhiz(XSDataAngle(0.0))
        xsDataMOSFLMNewmat.setMissettingAngles(xsDataMOSFLMMissettingsAngles)

        xsDataMOSFLMBeamPosition = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeamPosition.setX(xsDataDetector.getBeamPositionX())
        xsDataMOSFLMBeamPosition.setY(xsDataDetector.getBeamPositionY())
        xsDataMOSFLMInputIntegration.setBeam(xsDataMOSFLMBeamPosition)

        xsDataMOSFLMInputIntegration.setMosaicity(xsDataCrystal.getMosaicity())
        xsDataMOSFLMInputIntegration.setSymmetry(xsDataCrystal.getSpaceGroup().getName())

        strPathFirst = xsDataImageFirst.getPath().getValue()
        strDirectoryFirst = os.path.dirname(strPathFirst)
        strFilenameFirst = os.path.basename(strPathFirst)
        fOscillationRange = xsDataGoniostat.getOscillationWidth().getValue()

        xsDataMOSFLMInputIntegration.setWavelength(xsDataBeam.getWavelength())
        xsDataMOSFLMInputIntegration.setDistance(xsDataDetector.getDistance())
        xsDataMOSFLMInputIntegration.setDirectory(XSDataString(strDirectoryFirst))
        xsDataMOSFLMInputIntegration.setOscillationWidth(XSDataAngle(fOscillationRange))
        xsDataMOSFLMDetector = EDHandlerXSDataMOSFLMv10.getXSDataMOSFLMDetector(xsDataDetector)
        xsDataMOSFLMInputIntegration.setDetector(xsDataMOSFLMDetector)

        strMOSFLMTemplate = EDUtilsImage.getTemplate(strFilenameFirst, "#")
        xsDataMOSFLMInputIntegration.setTemplate(XSDataString(strMOSFLMTemplate))

        iImageStart = None
        iImageEnd = None
        for xsDataImage in xsDataImageList:
            iImageNumber = xsDataImage.getNumber().getValue()
            if (iImageStart is None):
                iImageStart = iImageNumber
            elif (iImageStart > iImageNumber):
                iImageStart = iImageNumber
            if (iImageEnd is None):
                iImageEnd = iImageNumber
            elif (iImageEnd < iImageNumber):
                iImageEnd = iImageNumber

        xsDataMOSFLMInputIntegration.setImageStart(XSDataInteger(iImageStart))
        xsDataMOSFLMInputIntegration.setImageEnd(XSDataInteger(iImageEnd))
        xsDataMOSFLMInputIntegration.setRotationAxisStart(xsDataGoniostat.getRotationAxisStart())

        #print xsDataMOSFLMInputIntegration.marshal()

        return xsDataMOSFLMInputIntegration
    generateXSDataMOSFLMInputIntegration = staticmethod(generateXSDataMOSFLMInputIntegration)


    def generateXSDataMOSFLMInputGeneratePrediction(xsDataGeneratePredictionInput):
        """
        Translation from XSDataGeneratePredictionInput to XSDataMOSFLMInputGeneratePrediction.
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputGeneratePrediction")
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
        from XSDataMOSFLMv10 import XSDataMOSFLMImage
        from XSDataMOSFLMv10 import XSDataMOSFLMNewmat
        from XSDataMOSFLMv10 import XSDataMOSFLMMissettingsAngles
        from XSDataMOSFLMv10 import XSDataMOSFLMInputGeneratePrediction

        xsDataIndexingSolutionSelected = xsDataGeneratePredictionInput.getSelectedIndexingSolution()

        xsDataCollection = xsDataGeneratePredictionInput.getDataCollection()
        xsDataSubWedge = xsDataCollection.getSubWedge()[0]
        xsDataImageList = xsDataSubWedge.getImage()
        xsDataImageFirst = xsDataImageList[0]

        xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
        xsDataOrientation = xsDataIndexingSolutionSelected.getOrientation()
        xsDataExperimentalCondition = xsDataIndexingSolutionSelected.getExperimentalConditionRefined()
        xsDataDetector = xsDataExperimentalCondition.getDetector()
        xsDataBeam = xsDataExperimentalCondition.getBeam()
        xsDataMatrixA = xsDataOrientation.getMatrixA()
        xsDataMatrixU = xsDataOrientation.getMatrixU()
        xsDataCell = xsDataCrystal.getCell()

        xsDataMOSFLMInputGeneratePrediction = XSDataMOSFLMInputGeneratePrediction()
        xsDataMOSFLMNewmat = XSDataMOSFLMNewmat()
        xsDataMOSFLMNewmat.setRefinedCell(xsDataCell)
        xsDataMOSFLMNewmat.setAMatrix(xsDataMatrixA)
        xsDataMOSFLMNewmat.setUMatrix(xsDataMatrixU)
        xsDataMOSFLMInputGeneratePrediction.setMatrix(xsDataMOSFLMNewmat)

        xsDataMOSFLMMissettingsAngles = XSDataMOSFLMMissettingsAngles()
        xsDataMOSFLMMissettingsAngles.setPhix(XSDataAngle(0.0))
        xsDataMOSFLMMissettingsAngles.setPhiy(XSDataAngle(0.0))
        xsDataMOSFLMMissettingsAngles.setPhiz(XSDataAngle(0.0))
        xsDataMOSFLMNewmat.setMissettingAngles(xsDataMOSFLMMissettingsAngles)

        xsDataMOSFLMBeamPosition = XSDataMOSFLMBeamPosition()
        xsDataMOSFLMBeamPosition.setX(xsDataDetector.getBeamPositionX())
        xsDataMOSFLMBeamPosition.setY(xsDataDetector.getBeamPositionY())
        xsDataMOSFLMInputGeneratePrediction.setBeam(xsDataMOSFLMBeamPosition)

        xsDataMOSFLMInputGeneratePrediction.setMosaicity(xsDataCrystal.getMosaicity())
        xsDataMOSFLMInputGeneratePrediction.setSymmetry(xsDataCrystal.getSpaceGroup().getName())

        strPathFirst = xsDataImageFirst.getPath().getValue()
        strDirectoryFirst = os.path.dirname(strPathFirst)
        strFilenameFirst = os.path.basename(strPathFirst)

        xsDataMOSFLMInputGeneratePrediction.setWavelength(xsDataBeam.getWavelength())
        xsDataMOSFLMInputGeneratePrediction.setDistance(xsDataDetector.getDistance())
        xsDataMOSFLMInputGeneratePrediction.setDirectory(XSDataString(strDirectoryFirst))
        xsDataMOSFLMDetector = EDHandlerXSDataMOSFLMv10.getXSDataMOSFLMDetector(xsDataDetector)
        xsDataMOSFLMInputGeneratePrediction.setDetector(xsDataMOSFLMDetector)

        strMOSFLMTemplate = EDUtilsImage.getTemplate(strFilenameFirst, "#")
        xsDataMOSFLMInputGeneratePrediction.setTemplate(XSDataString(strMOSFLMTemplate))

        # The MOSFLM plugin can only handle one image 

        xsDataImage = xsDataSubWedge.getImage()[0]
        xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()

        xsDataMOSFLMImage = XSDataMOSFLMImage()

        iImageNumber = xsDataImage.getNumber().getValue()
        xsDataMOSFLMImage.setNumber(XSDataInteger(iImageNumber))

        fOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
        fOscillationRange = xsDataGoniostat.getOscillationWidth().getValue()
        xsDataMOSFLMImage.setRotationAxisStart(XSDataAngle(fOscillationStart))
        xsDataMOSFLMImage.setRotationAxisEnd(XSDataAngle(fOscillationStart + fOscillationRange))

        xsDataMOSFLMInputGeneratePrediction.setImage(xsDataMOSFLMImage)

        return xsDataMOSFLMInputGeneratePrediction
    generateXSDataMOSFLMInputGeneratePrediction = staticmethod(generateXSDataMOSFLMInputGeneratePrediction)



    def generateXSDataIntegrationSubWedgeResult(_xsDataMOSFLMOutputIntegration, _xsDataExperimentalCondition=None):
        """
        Translation from XSDataMOSFLMOutputIntegration to XSDataIntegrationSubWedgeResult.
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.generateXSDataIntegrationInput")
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        xsDataIntegrationSubWedgeResult = XSDataIntegrationSubWedgeResult()
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

        xsDataIntegrationSubWedgeResult.setBestfilePar(XSDataString(_xsDataMOSFLMOutputIntegration.getBestfilePar().getValue()))
        xsDataIntegrationSubWedgeResult.setBestfileDat(XSDataString(_xsDataMOSFLMOutputIntegration.getBestfileDat().getValue()))
        xsDataIntegrationSubWedgeResult.setBestfileHKL(XSDataString(_xsDataMOSFLMOutputIntegration.getBestfileHKL().getValue()))

        xsDataLengthRefinedDistance = _xsDataMOSFLMOutputIntegration.getRefinedDistance()
        if (xsDataLengthRefinedDistance is not None):
            xsDataDetector.setDistance(xsDataLengthRefinedDistance)

        xsDataMOSFLMBeamPositionRefined = _xsDataMOSFLMOutputIntegration.getRefinedBeam()
        if (xsDataMOSFLMBeamPositionRefined is not None):
            xsDataDetector.setBeamPositionX(XSDataLength(xsDataMOSFLMBeamPositionRefined.getX().getValue()))
            xsDataDetector.setBeamPositionY(XSDataLength(xsDataMOSFLMBeamPositionRefined.getY().getValue()))

        xsDataExperimentalConditionRefined.setDetector(xsDataDetector)
        xsDataIntegrationSubWedgeResult.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

        if (_xsDataMOSFLMOutputIntegration.getGeneratedMTZFile() is not None):
            xsDataIntegrationSubWedgeResult.setGeneratedMTZFile(_xsDataMOSFLMOutputIntegration.getGeneratedMTZFile())

        xsDataStatisticsIntegration = XSDataStatisticsIntegration()
        if (_xsDataMOSFLMOutputIntegration.getOverallIOverSigma() is not None):
            xsDataStatisticsIntegration.setIOverSigmaOverall(XSDataDouble(_xsDataMOSFLMOutputIntegration.getOverallIOverSigma().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getHighestResolutionIOverSigma() is not None):
            xsDataStatisticsIntegration.setIOverSigmaAtHighestResolution(XSDataDouble(_xsDataMOSFLMOutputIntegration.getHighestResolutionIOverSigma().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getRMSSpotDeviation() is not None):
            xsDataStatisticsIntegration.setRMSSpotDeviation(XSDataLength(_xsDataMOSFLMOutputIntegration.getRMSSpotDeviation().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfBadReflections() is not None):
            xsDataStatisticsIntegration.setNumberOfBadReflections(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfBadReflections().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfFullyRecordedReflections() is not None):
            xsDataStatisticsIntegration.setNumberOfFullyRecordedReflections(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfFullyRecordedReflections().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfNegativeReflections() is not None):
            xsDataStatisticsIntegration.setNumberOfNegativeReflections(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfNegativeReflections().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfOverlappedReflections() is not None):
            xsDataStatisticsIntegration.setNumberOfOverlappedReflections(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfOverlappedReflections().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfPartialReflections() is not None):
            xsDataStatisticsIntegration.setNumberOfPartialReflections(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfPartialReflections().getValue()))
        if (_xsDataMOSFLMOutputIntegration.getNumberOfReflectionsGenerated() is not None):
            xsDataStatisticsIntegration.setNumberOfReflectionsGenerated(XSDataInteger(_xsDataMOSFLMOutputIntegration.getNumberOfReflectionsGenerated().getValue()))

        xsDataIntegrationSubWedgeResult.setStatistics(xsDataStatisticsIntegration)
        xsDataIntegrationSubWedgeResult.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

        for xsDataMOSFLMIntegrationStatisticsPerResolutionBin in _xsDataMOSFLMOutputIntegration.getStatisticsPerResolutionBin():
            xsDataStatisticsIntegrationPerResolutionBin = XSDataStatisticsIntegrationPerResolutionBin()
            if (xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMaxResolution() is not None):
                xsDataStatisticsIntegrationPerResolutionBin.setMaxResolution(XSDataDouble(xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMaxResolution().getValue()))
            if (xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMinResolution() is not None):
                xsDataStatisticsIntegrationPerResolutionBin.setMinResolution(XSDataDouble(xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMinResolution().getValue()))

            xsDataStatisticsIntegrationPerResolutionBin.setProfileFitted(EDHandlerXSDataMOSFLMv10.generateXSDataIntegrationStatisticsPerReflectionType(xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getProfileFitted()))
            xsDataStatisticsIntegrationPerResolutionBin.setSummation(EDHandlerXSDataMOSFLMv10.generateXSDataIntegrationStatisticsPerReflectionType(xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getSummation()))

            xsDataIntegrationSubWedgeResult.addStatisticsPerResolutionBin(xsDataStatisticsIntegrationPerResolutionBin)

        return xsDataIntegrationSubWedgeResult
    generateXSDataIntegrationSubWedgeResult = staticmethod(generateXSDataIntegrationSubWedgeResult)


    def generateXSDataIntegrationStatisticsPerReflectionType(_xsDataMOSFLMIntegrationStatisticsPerReflectionType):
        xsDataStatisticsIntegrationPerReflectionType = None
        if (_xsDataMOSFLMIntegrationStatisticsPerReflectionType is not None):
            xsDataStatisticsIntegrationPerReflectionType = XSDataStatisticsIntegrationPerReflectionType()
            xsDataStatisticsIntegrationPerReflectionType.setFullyRecorded(EDHandlerXSDataMOSFLMv10.generateXSDataStatisticsIntegrationAverageAndNumberOfReflections(_xsDataMOSFLMIntegrationStatisticsPerReflectionType.getFullyRecorded()))
            xsDataStatisticsIntegrationPerReflectionType.setPartials(EDHandlerXSDataMOSFLMv10.generateXSDataStatisticsIntegrationAverageAndNumberOfReflections(_xsDataMOSFLMIntegrationStatisticsPerReflectionType.getPartials()))
        return xsDataStatisticsIntegrationPerReflectionType
    generateXSDataIntegrationStatisticsPerReflectionType = staticmethod(generateXSDataIntegrationStatisticsPerReflectionType)


    def generateXSDataStatisticsIntegrationAverageAndNumberOfReflections(_xsDataMOSFLMIntegrationStatistics):
        xsDataStatisticsIntegrationAverageAndNumberOfReflections = None
        if (_xsDataMOSFLMIntegrationStatistics is not None):
            xsDataStatisticsIntegrationAverageAndNumberOfReflections = XSDataStatisticsIntegrationAverageAndNumberOfReflections()
            if (_xsDataMOSFLMIntegrationStatistics.getAverageIntensity() is not None):
                xsDataStatisticsIntegrationAverageAndNumberOfReflections.setAverageIntensity(XSDataDouble(_xsDataMOSFLMIntegrationStatistics.getAverageIntensity().getValue()))
            if (_xsDataMOSFLMIntegrationStatistics.getAverageIOverSigma() is not None):
                xsDataStatisticsIntegrationAverageAndNumberOfReflections.setAverageIOverSigma(XSDataDouble(_xsDataMOSFLMIntegrationStatistics.getAverageIOverSigma().getValue()))
            if (_xsDataMOSFLMIntegrationStatistics.getAverageSigma() is not None):
                xsDataStatisticsIntegrationAverageAndNumberOfReflections.setAverageSigma(XSDataDouble(_xsDataMOSFLMIntegrationStatistics.getAverageSigma().getValue()))
            if (_xsDataMOSFLMIntegrationStatistics.getNumberOfReflections() is not None):
                xsDataStatisticsIntegrationAverageAndNumberOfReflections.setNumberOfReflections(XSDataInteger(_xsDataMOSFLMIntegrationStatistics.getNumberOfReflections().getValue()))
        return xsDataStatisticsIntegrationAverageAndNumberOfReflections
    generateXSDataStatisticsIntegrationAverageAndNumberOfReflections = staticmethod(generateXSDataStatisticsIntegrationAverageAndNumberOfReflections)


    def areInstrumentParametersOK(_xsDataImageList):
        """
        Helper method for checking that the instrument parameters for a list of
        XSDataImage images haven't changed
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.areInstrumentParametersOK")

        returnValue = True

        xsDataImageFirst = _xsDataImageList[0]

        xsDataInstrumentFirst = xsDataImageFirst.getInstrument()
        xsDataBeamFirst = xsDataInstrumentFirst.getBeam()
        xsDataDetectorFirst = xsDataInstrumentFirst.getDetector()

        fWavelengthFirst = xsDataBeamFirst.getWavelength().getValue()
        fDistanceFirst = xsDataDetectorFirst.getDistance().getValue()
        fBeamPositionXFirst = xsDataDetectorFirst.getBeamPositionX().getValue()
        fBeamPositionYFirst = xsDataDetectorFirst.getBeamPositionY().getValue()
        strDetectorTypeFirst = xsDataDetectorFirst.getType().getValue()

        for xsDataImage in _xsDataImageList:
            # Check that the Instrument parameters hasn't changed
            xsDataInstrument = xsDataImage.getInstrument()
            xsDataBeam = xsDataInstrument.getBeam()
            xsDataDetector = xsDataInstrument.getDetector()

            fWavelength = xsDataBeam.getWavelength().getValue()
            fDistance = xsDataDetector.getDistance().getValue()
            fBeamPositionX = xsDataDetector.getBeamPositionX().getValue()
            fBeamPositionY = xsDataDetector.getBeamPositionY().getValue()
            strDetectorType = xsDataDetector.getType().getValue()

            if  (EDHandlerXSDataMOSFLMv10.isDifferent(fWavelengthFirst, fWavelength)):
                #print "Error : different wavelengths!"
                returnValue = False
            elif (EDHandlerXSDataMOSFLMv10.isDifferent(fDistanceFirst, fDistance)):
                #print "Error : different distances!"
                returnValue = False
            elif (EDHandlerXSDataMOSFLMv10.isDifferent(fBeamPositionXFirst, fBeamPositionX)):
                #print "Error : different beam position X!"
                returnValue = False
            elif (EDHandlerXSDataMOSFLMv10.isDifferent(fBeamPositionYFirst, fBeamPositionY)):
                #print "Error : different beam position Y!"
                returnValue = False
            elif (EDHandlerXSDataMOSFLMv10.isDifferent(strDetectorTypeFirst, strDetectorType)):
                #print "Error : different detectors!"
                returnValue = False

        return returnValue
    areInstrumentParametersOK = staticmethod(areInstrumentParametersOK)


    def isDifferent(_edObject1, _edObject2):
        """
        Helper method for checking if two objects are different.
        If the objects are of type float the tolerance is 0.01.
        """
        EDVerbose.DEBUG("EDHandlerXSDataMOSFLMv10.isDifferent")
        returnValue = True
        opyTypeObject1 = type(_edObject1)
        if (opyTypeObject1 == opyTypeObject1):
            if (opyTypeObject1 == int):
                if (_edObject1 != _edObject2):
                    returnValue = False
            elif (opyTypeObject1 == str) or (opyTypeObject1 == type("a")) or (opyTypeObject1 == unicode):
                if (_edObject1 == _edObject2):
                    returnValue = False
            elif (opyTypeObject1 == float):
                if (abs(_edObject1 - _edObject2) < 0.01) :
                    returnValue = False
        return returnValue
    isDifferent = staticmethod(isDifferent)


    def getXSDataMOSFLMDetector(_xsDataDetector):
        """
        Translates an XSDataDetector object to XSDataMOSFLMv10.
        """
        EDFactoryPluginStatic.loadModule("XSDataMOSFLMv10")
        from XSDataMOSFLMv10 import XSDataMOSFLMDetector
        xsDataMOSFLMDetector = XSDataMOSFLMDetector()
        strDetectorType = _xsDataDetector.getType().getValue()
        if (strDetectorType == "q4") or \
             (strDetectorType == "q4-2x") or \
             (strDetectorType == "q210") or \
             (strDetectorType == "q210-2x") or \
             (strDetectorType == "q315") or \
             (strDetectorType == "q315-2x"):
            xsDataMOSFLMDetector.setType(XSDataString("ADSC"))
        elif (strDetectorType == "mar165") or \
               (strDetectorType == "mar225"):
            xsDataMOSFLMDetector.setType(XSDataString("MARCCD"))
        elif (strDetectorType == "pilatus6m" or strDetectorType == "pilatus2m"):
            xsDataMOSFLMDetector.setType(XSDataString("PILATUS"))
        elif (strDetectorType == "raxis4"):
            xsDataMOSFLMDetector.setType(XSDataString("RAXISIV"))
        else:
            # This is a temporary solution for the exception problem pointed out in bug #43.
            # Instead of raising an exception with a known type we send the error message as a string.
            strErrorMessage = "EDHandlerXSDataMOSFLMv10.getXSDataMOSFLMDetector: Unknown detector type : " + strDetectorType
            raise Exception, strErrorMessage
        if (_xsDataDetector.getNumberPixelX() is not None):
            xsDataMOSFLMDetector.setNumberPixelX(_xsDataDetector.getNumberPixelX())
        if (_xsDataDetector.getNumberPixelY() is not None):
            xsDataMOSFLMDetector.setNumberPixelY(_xsDataDetector.getNumberPixelY())
        if (_xsDataDetector.getPixelSizeX() is not None):
            xsDataMOSFLMDetector.setPixelSizeX(_xsDataDetector.getPixelSizeX())
        if (_xsDataDetector.getPixelSizeY() is not None):
            xsDataMOSFLMDetector.setPixelSizeY(_xsDataDetector.getPixelSizeY())
        return xsDataMOSFLMDetector
    getXSDataMOSFLMDetector = staticmethod(getXSDataMOSFLMDetector)
