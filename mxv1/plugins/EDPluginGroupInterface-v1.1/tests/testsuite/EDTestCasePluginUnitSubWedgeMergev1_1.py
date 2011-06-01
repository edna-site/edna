#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Gleb Bourenkov" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAssert                            import EDAssert

from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest

from XSDataCommon import XSDataTime
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataAngle

from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataExperimentalCondition

from XSDataMXv1 import XSDataInputSubWedgeMerge

class EDTestCasePluginUnitSubWedgeMergev1_1(EDTestCasePluginUnit):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginSubWedgeMergev1_1", "EDPluginGroupInterface-v1.1", _edStringTestName)
        self.strPathToReferenceInput = os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeMerge_reference.xml")


    def testCompareTwoValues(self):
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues(1, 1), True)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues(1, 2), False)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues(1.0, 1.0), True)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues(1.0, 1.01), False)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues(1.0, 1.01, 0.1), True)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues("EDNA", "EDNA"), True)
        EDAssert.equal(edPluginSubWedgeMergev1_1.compareTwoValues("EDNA", "DNA"), False)
        # Comparison of two different types should raise an exception
        try:
            bTmp = edPluginSubWedgeMergev1_1.compareTwoValues("EDNA", 1)
            EDAssert.equal(True, False)
        except:
            EDAssert.equal(True, True)
        # Comparison of anything but double, int or string should raise an exception
        try:
            bTmp = edPluginSubWedgeMergev1_1.compareTwoValues([1], [1])
            EDAssert.equal(True, False)
        except:
            EDAssert.equal(True, True)


    def getTestExperimentalCondition(self):
        strPathToTestExperimentalCondition = os.path.join(self.getPluginTestsDataHome(), "XSDataExperimentalCondition_test.xml")
        strXMLInput = self.readAndParseFile(strPathToTestExperimentalCondition)
        xsDataExperimentalCondition = XSDataExperimentalCondition.parseString(strXMLInput)
        return xsDataExperimentalCondition


    def testIsSameExperimentalCondition(self):
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        xsDataExperimentalConditionReference = self.getTestExperimentalCondition()
        xsDataExperimentalConditionSameAsReference = self.getTestExperimentalCondition()
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionSameAsReference),
                                                                              True)
        xsDataExperimentalConditionDifferentExposureTime = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentExposureTime.getBeam().setExposureTime(XSDataTime(10.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentExposureTime),
                                                                              False)
        xsDataExperimentalConditionDifferentWavelength = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentWavelength.getBeam().setWavelength(XSDataWavelength(1.5))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentWavelength),
                                                                              False)
        xsDataExperimentalConditionDifferentBeamPositionX = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentBeamPositionX.getDetector().setBeamPositionX(XSDataLength(20.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentBeamPositionX),
                                                                              False)
        xsDataExperimentalConditionDifferentBeamPositionY = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentBeamPositionY.getDetector().setBeamPositionY(XSDataLength(20.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentBeamPositionY),
                                                                              False)
        xsDataExperimentalConditionDifferentDistance = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentDistance.getDetector().setDistance(XSDataLength(220.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentDistance),
                                                                              False)
        xsDataExperimentalConditionDifferentName = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentName.getDetector().setName(XSDataString(u"EDNA"))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentName),
                                                                              False)
        xsDataExperimentalConditionDifferentNumberPixelX = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentNumberPixelX.getDetector().setNumberPixelX(XSDataInteger(2))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentNumberPixelX),
                                                                              False)
        xsDataExperimentalConditionDifferentNumberPixelY = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentNumberPixelY.getDetector().setNumberPixelY(XSDataInteger(2))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentNumberPixelY),
                                                                              False)
        xsDataExperimentalConditionDifferentSerialNumber = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentSerialNumber.getDetector().setSerialNumber(XSDataString(u"EDNA"))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentSerialNumber),
                                                                              False)
        xsDataExperimentalConditionDifferentTwoTheta = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentTwoTheta.getDetector().setTwoTheta(XSDataAngle(90.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentTwoTheta),
                                                                              False)
        xsDataExperimentalConditionDifferentOscillationWidth = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentOscillationWidth.getGoniostat().setOscillationWidth(XSDataAngle(2.0))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentOscillationWidth),
                                                                              False)
        xsDataExperimentalConditionDifferentRotationAxis = self.getTestExperimentalCondition()
        xsDataExperimentalConditionDifferentRotationAxis.getGoniostat().setRotationAxis(XSDataString(u"EDNA"))
        EDAssert.equal(edPluginSubWedgeMergev1_1.isSameExperimentalCondition(xsDataExperimentalConditionReference,
                                                                              xsDataExperimentalConditionDifferentRotationAxis),
                                                                              False)


    def testSortIdenticalObjects(self):
        listObjects = []
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        listSorted = edPluginSubWedgeMergev1_1.sortIdenticalObjects(listObjects, edPluginSubWedgeMergev1_1.compareTwoValues)
        EDAssert.equal(listSorted, [])
        listObjects = [ 1 ]
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        listSorted = edPluginSubWedgeMergev1_1.sortIdenticalObjects(listObjects, edPluginSubWedgeMergev1_1.compareTwoValues)
        EDAssert.equal(listSorted, [[1]])
        listObjects = [ 1, 2 ]
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        listSorted = edPluginSubWedgeMergev1_1.sortIdenticalObjects(listObjects, edPluginSubWedgeMergev1_1.compareTwoValues)
        EDAssert.equal(listSorted, [[1], [2]])
        listObjects = [ 1, 1 ]
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        listSorted = edPluginSubWedgeMergev1_1.sortIdenticalObjects(listObjects, edPluginSubWedgeMergev1_1.compareTwoValues)
        EDAssert.equal(listSorted, [[1, 1]])
        listObjects = [ 1, 2, 1, 3, 4, 1, 5, 2, 2, 9, 3, 2]
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        listSorted = edPluginSubWedgeMergev1_1.sortIdenticalObjects(listObjects, edPluginSubWedgeMergev1_1.compareTwoValues)
        EDAssert.equal(listSorted, [[1, 1, 1], [2, 2, 2, 2], [3, 3], [4], [5], [9]])


    def testSortSubWedgesOnExperimentalCondition(self):
        # First check two sub wedges with identical experimental conditions
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        edPluginSubWedgeMergev1_1.configure()
        xsDataInputSubWedgeMerge = XSDataInputSubWedgeMerge.parseFile(self.strPathToReferenceInput)
        listSubWedgeSorted = edPluginSubWedgeMergev1_1.sortSubWedgesOnExperimentalCondition(xsDataInputSubWedgeMerge)
        # Check that we got a list with one element
        EDAssert.equal(len(listSubWedgeSorted), 1)
        # Then modify one sub wedge
        xsDataSubWedge1 = xsDataInputSubWedgeMerge.getSubWedge()[0]
        xsDataSubWedge1.getExperimentalCondition().getDetector().setDistance(XSDataLength(300.0))
        listSubWedgeSorted = edPluginSubWedgeMergev1_1.sortSubWedgesOnExperimentalCondition(xsDataInputSubWedgeMerge)
        # Check that we got a list with two elements
        EDAssert.equal(len(listSubWedgeSorted), 2)




    def testMergeTwoSubWedgesAdjascentInRotationAxis(self):
        # First check two sub wedges which shouldn't be merged
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        edPluginSubWedgeMergev1_1.configure()
        xsDataInputSubWedgeMerge = XSDataInputSubWedgeMerge.parseFile(self.strPathToReferenceInput)
        xsDataSubWedge1 = xsDataInputSubWedgeMerge.getSubWedge()[0]
        xsDataSubWedge2 = xsDataInputSubWedgeMerge.getSubWedge()[1]
        xsDataSubWedgeMerged = edPluginSubWedgeMergev1_1.mergeTwoSubWedgesAdjascentInRotationAxis(xsDataSubWedge1, xsDataSubWedge2)
        EDAssert.equal(xsDataSubWedgeMerged, None)
        # Then check two adjascent images
        strPathToInputTwoAdjascentImages = os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeMerge_twoAdjascentImages.xml")
        xsDataInputSubWedgeMerge2 = XSDataInputSubWedgeMerge.parseFile(strPathToInputTwoAdjascentImages)
        xsDataSubWedge1 = xsDataInputSubWedgeMerge2.getSubWedge()[0]
        xsDataSubWedge2 = xsDataInputSubWedgeMerge2.getSubWedge()[1]
        xsDataSubWedgeMerged = edPluginSubWedgeMergev1_1.mergeTwoSubWedgesAdjascentInRotationAxis(xsDataSubWedge1, xsDataSubWedge2)
        xsDataSubWedgeMergedReference = XSDataSubWedge.parseFile(os.path.join(self.getPluginTestsDataHome(), "XSDataSubWedgeMerged_twoImages.xml"))
        EDAssert.equal(xsDataSubWedgeMerged.marshal(), xsDataSubWedgeMergedReference.marshal())


    def testMergeListOfSubWedgesWithAdjascentRotationAxis(self):
        edPluginSubWedgeMergev1_1 = self.createPlugin()
        edPluginSubWedgeMergev1_1.configure()
        # Check a list of nine adjascent images
        strPathToInputNineAdjascentImages = os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeMerge_nineAdjascentImages.xml")
        xsDataInputSubWedgeMergeNine = XSDataInputSubWedgeMerge.parseFile(strPathToInputNineAdjascentImages)
        xsDataSubWedgeMerged = edPluginSubWedgeMergev1_1.mergeListOfSubWedgesWithAdjascentRotationAxis(xsDataInputSubWedgeMergeNine.getSubWedge())
        xsDataSubWedgeMergedReference = XSDataSubWedge.parseFile(os.path.join(self.getPluginTestsDataHome(), "XSDataSubWedgeMerged_nineImages.xml"))
        EDAssert.equal(xsDataSubWedgeMerged[0].marshal(), xsDataSubWedgeMergedReference.marshal())


    def process(self):
        self.addTestMethod(self.testCompareTwoValues)
        self.addTestMethod(self.testIsSameExperimentalCondition)
        self.addTestMethod(self.testSortIdenticalObjects)
        self.addTestMethod(self.testSortSubWedgesOnExperimentalCondition)
        self.addTestMethod(self.testMergeTwoSubWedgesAdjascentInRotationAxis)
        self.addTestMethod(self.testMergeListOfSubWedgesWithAdjascentRotationAxis)



if __name__ == '__main__':

    edTestCasePluginUnitSubWedgeMergev1_1 = EDTestCasePluginUnitSubWedgeMergev1_1("EDTestCasePluginUnitSubWedgeMergev1_1")
    edTestCasePluginUnitSubWedgeMergev1_1.execute()

