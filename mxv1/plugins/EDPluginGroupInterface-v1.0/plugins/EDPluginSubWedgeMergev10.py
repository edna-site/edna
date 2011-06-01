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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Gleb Bourenkov"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose    import EDVerbose
from EDMessage    import EDMessage
from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataAngle

from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataInputSubWedgeMerge
from XSDataMXv1 import XSDataResultSubWedgeMerge

class EDPluginSubWedgeMergev10(EDPluginExec):
    """
    This plugin takes as input a list of sub wedges and merges them (if possible)
    """


    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputSubWedgeMerge)
        self.__listResultSubWedgeMerge = []


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getSubWedge(), "No subwedges provided")


    def process(self, _edObject=None):
        EDPluginExec.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.process...")

        xsDataInputSubWedgeMerge = self.getDataInput()

        # 1. Sort the incoming subwedges in groupes of similar experimental conditions
        listSubWedgeSorted = self.sortSubWedgesOnExperimentalCondition(xsDataInputSubWedgeMerge)

        # 2. Merge subwedges which are adjascent with respect to the orientation matrix
        for listSubWedge in listSubWedgeSorted:
            listSubWedgeMerged = self.mergeListOfSubWedgesWithAdjascentRotationAxis(listSubWedge)
            self.__listResultSubWedgeMerge.extend(listSubWedgeMerged)


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.postProcess")
        xsDataResultSubWedgeMerge = XSDataResultSubWedgeMerge()
        for xsDataSubWedgeMerge in self.__listResultSubWedgeMerge:
            xsDataResultSubWedgeMerge.addSubWedge(xsDataSubWedgeMerge)
        self.setDataOutput(xsDataResultSubWedgeMerge)



    def compareTwoValues(self, _value1, _value2, _dTolerance=0.000001):
        """
        This method compares two values which can be of type double, integer or string.
        The types of the two values two be compared must be identical.
        If the value is of type double, an optional tolerance can be passed as an
        argument to the method. If both values are None the methods returns True.
        """
        bReturnValue = False
        if (_value1 is None):
            if (_value2 is None):
                bReturnValue = True
        elif (type (_value1) != type(_value2)):
            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginSubWedgeMergev10.compareTwoValues', self.getClassName(), "Types of values different : value1=%r, value2=%r" % (type(_value1), type(_value2)))
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise Exception, strErrorMessage
        elif (type(_value1) == type(0.1)):
            if (abs(_value1 - _value2) < _dTolerance):
                bReturnValue = True
        elif (type(_value1) == type(1)):
            if (_value1 == _value2):
                bReturnValue = True
        elif type(_value1) == type("aaa") or type(_value1) == type(u'unicode'):
            if _value1 == _value2:
                bReturnValue = True
        else:
            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginSubWedgeMergev10.compareTwoValues', self.getClassName(), "Unknown value type : %r for value %r" % (type(_value1), _value1))
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise Exception, strErrorMessage
        return bReturnValue


    def isSameExperimentalCondition(self, _xsDataExperimentalCondition1, _xsDataExperimentalCondition2):
        """
        This method compares two XSDataExperimentaCondition objects in order to verify if
        they can belong to the same sub wedge. The following parameters are checked:
        beam.exposureTime [s], tolerance 0.001
        beam.wavelength [A], tolerance 0.001
        detector.beamPositionX [mm], tolerance 0.1
        detector.beamPositionY [mm], tolerance 0.1
        detector.distance [mm], tolerance 0.1
        detector.name [string]
        detector.numberPixelX [int]
        detector.numberPixelY [int]
        detector.serialNumber [string]
        detector.twoTheta [degrees], tolerance 0.1
        goniostat.oscillationWidth [degrees], tolerance 0.001
        goniostat.rotationAxis [string]
        """
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.isSameExperimentalCondition")
        bReturnValue = True
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getBeam().getExposureTime().getValue(),
                                    _xsDataExperimentalCondition2.getBeam().getExposureTime().getValue(),
                                    0.001
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getBeam().getWavelength().getValue(),
                                    _xsDataExperimentalCondition2.getBeam().getWavelength().getValue(),
                                    0.001
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getDistance().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getDistance().getValue(),
                                    0.1
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getName().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getName().getValue(),
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getBeamPositionX().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getBeamPositionX().getValue(),
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getBeamPositionY().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getBeamPositionY().getValue(),
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getNumberPixelX().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getNumberPixelX().getValue(),
                                    ) == False):
            bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getNumberPixelY().getValue(),
                                    _xsDataExperimentalCondition2.getDetector().getNumberPixelY().getValue(),
                                    ) == False):
            bReturnValue = False
        # The detector serial number could be missing in image header data
        if (_xsDataExperimentalCondition1.getDetector().getSerialNumber() is not None and
             _xsDataExperimentalCondition2.getDetector().getSerialNumber() is not None):
            if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getSerialNumber().getValue(),
                                            _xsDataExperimentalCondition2.getDetector().getSerialNumber().getValue(),
                                            ) == False):
                bReturnValue = False
        else:
            # Check if only one serial number is available
            if (_xsDataExperimentalCondition1.getDetector().getSerialNumber() is not None or
                 _xsDataExperimentalCondition2.getDetector().getSerialNumber() is not None):
                bReturnValue = False
        # The detector two theta value is sometimes missing in image header data
        if (_xsDataExperimentalCondition1.getDetector().getTwoTheta() is not None and
             _xsDataExperimentalCondition2.getDetector().getTwoTheta() is not None):
            if (self.compareTwoValues(_xsDataExperimentalCondition1.getDetector().getTwoTheta().getValue(),
                                        _xsDataExperimentalCondition2.getDetector().getTwoTheta().getValue(),
                                        0.1
                                        ) == False):
                bReturnValue = False
        else:
            # Check if only one two theta is available
            if (_xsDataExperimentalCondition1.getDetector().getTwoTheta() is not None or
                 _xsDataExperimentalCondition2.getDetector().getTwoTheta() is not None):
                bReturnValue = False
        if (self.compareTwoValues(_xsDataExperimentalCondition1.getGoniostat().getOscillationWidth().getValue(),
                                        _xsDataExperimentalCondition2.getGoniostat().getOscillationWidth().getValue(),
                                        0.001
                                        ) == False):
            bReturnValue = False
        # The detector two theta value is sometimes missing in image header data
        if (_xsDataExperimentalCondition1.getGoniostat().getRotationAxis() is not None and
             _xsDataExperimentalCondition2.getGoniostat().getRotationAxis() is not None):
            if (self.compareTwoValues(_xsDataExperimentalCondition1.getGoniostat().getRotationAxis().getValue(),
                                            _xsDataExperimentalCondition2.getGoniostat().getRotationAxis().getValue(),
                                            ) == False):
                bReturnValue = False
        else:
            # Check if only one rotation axis is available
            if (_xsDataExperimentalCondition1.getGoniostat().getRotationAxis() is not None or
                 _xsDataExperimentalCondition2.getGoniostat().getRotationAxis() is not None):
                bReturnValue = False
        return bReturnValue



    def isSameExperimentalConditionInSubWedge(self, _xsDataSubWedge1, _xsDataSubWedge2):
        """
        This method compares two XSDataSubWedge objects in order to verify if
        they can belong to the same sub wedge. The two experimental condition
        objects are compared using the method "isSameExperimentalCondition"
        """
        xsDataExperimentalCondition1 = _xsDataSubWedge1.getExperimentalCondition()
        xsDataExperimentalCondition2 = _xsDataSubWedge2.getExperimentalCondition()
        return self.isSameExperimentalCondition(xsDataExperimentalCondition1, xsDataExperimentalCondition2)



    def sortIdenticalObjects(self, _listOfObjects, _methodForComparison):
        """
        This method takes as input a list of objects with the same type.
        It returns a list containing list of identical objects. If an object
        is not identical to another it is returned in a list alone.
        """
        listResult = []
        iNumberOfObjects = len(_listOfObjects)
        if (iNumberOfObjects == 0):
            pass
        elif (iNumberOfObjects == 1):
            listResult.append(_listOfObjects)
        else:
            # More than 1 object
            listOfRemainingObjects = _listOfObjects
            while (len(listOfRemainingObjects) > 0):
                iIndex = 0
                oCurrentObject = listOfRemainingObjects[0]
                listOfRemainingObjects = listOfRemainingObjects[1:]
                listOfSortedObjects = []
                listOfSortedObjects.append(oCurrentObject)
                #print "Before loop: ", oCurrentObject, listOfRemainingObjects, iNumberOfRemainingObjects
                while (iIndex < len(listOfRemainingObjects)):
                    oCompareObject = listOfRemainingObjects[ iIndex ]
                    bAreEqualObjects = _methodForComparison(oCurrentObject, oCompareObject)
                    #print "   In the loop:", iIndex, oCompareObject, bAreEqualObjects, listOfSortedObjects, listOfRemainingObjects
                    if (bAreEqualObjects):
                        listOfSortedObjects.append(oCompareObject)
                        listOfRemainingObjectsTmp = listOfRemainingObjects[ 0:iIndex ]
                        if (iIndex < len(listOfRemainingObjects)):
                            listOfRemainingObjectsTmp.extend(listOfRemainingObjects[ iIndex + 1: ])
                        listOfRemainingObjects = listOfRemainingObjectsTmp
                    else:
                        iIndex += 1
                listResult.append(listOfSortedObjects)
        return listResult


    def sortSubWedgesOnExperimentalCondition(self, _xsDataInputSubWedgeMerge):
        """
        This method sorts a list of sub wedges into a new list containing lists of
        sub wegdes with identical experimental conditions.
        """
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.sortSubWedgesOnExperimentalCondition")
        # Create a list with all incoming sub wedges
        listSubWedge = _xsDataInputSubWedgeMerge.getSubWedge()
        # Sort it
        listSubWedgeSorted = self.sortIdenticalObjects(listSubWedge, self.isSameExperimentalConditionInSubWedge)
        return listSubWedgeSorted



    def mergeTwoSubWedgesAdjascentInRotationAxis(self, _subWedge1, _subWedge2):
        """
        This method takes as input two sub wedges and merges them to an unique subwedge, if possible,
        and returns the resulting merged sub wedge. If the merge is not possible a None is returned.
        """
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.mergeTwoSubWedgesAdjascentInRotationAxis")
        xsDataSubWedgeMerged = None
        # First check that the two sub wedges have identical experimental conditions
        if (self.isSameExperimentalConditionInSubWedge(_subWedge1, _subWedge2)):
            # Check if sub wedges are adjascent:
            dRoationAxisEnd1 = _subWedge1.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
            dRoationAxisStart2 = _subWedge2.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()
            #print dRoationAxisEnd1, dRoationAxisStart2
            if (self.compareTwoValues(dRoationAxisEnd1, dRoationAxisStart2, 0.001)):
                # Same sub wedge! Let's merge them
                xsDataSubWedgeMerged = XSDataSubWedge.parseString(_subWedge1.marshal())
                xsDataSubWedge2 = XSDataSubWedge.parseString(_subWedge2.marshal())
                dRoationAxisEnd2 = xsDataSubWedge2.getExperimentalCondition().getGoniostat().getRotationAxisEnd().getValue()
                xsDataSubWedgeMerged.getExperimentalCondition().getGoniostat().setRotationAxisEnd(XSDataAngle(dRoationAxisEnd2))
                for xsDataImage in xsDataSubWedge2.getImage():
                    xsDataSubWedgeMerged.addImage(xsDataImage)
        return xsDataSubWedgeMerged


    def mergeListOfSubWedgesWithAdjascentRotationAxis(self, _listOfSubWedgesWithIdenticalExperimentalConditions):
        """
        This method merges sub wedges in a list if they are adjascent in phi.
        """
        EDVerbose.DEBUG("EDPluginSubWedgeMergev10.mergeSubWedgesWithAdjascentRotationAxis")
        # Copy the incoming list to a new list
        listOfSubWedgesWithIdenticalExperimentalConditions = []
        for xsDataSubWedge in _listOfSubWedgesWithIdenticalExperimentalConditions:
            listOfSubWedgesWithIdenticalExperimentalConditions.append(XSDataSubWedge.parseString(xsDataSubWedge.marshal()))
        listOfMergedSubWedges = []
        if (len(listOfSubWedgesWithIdenticalExperimentalConditions) == 0):
            pass
        elif (len(listOfSubWedgesWithIdenticalExperimentalConditions) == 1):
            listOfMergedSubWedges = listOfSubWedgesWithIdenticalExperimentalConditions
        else:
            # First sort the list as function of rotation axis start
            listOfSubWedgesWithIdenticalExperimentalConditions.sort(lambda x, y: cmp(x.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue(), \
                                                                                        y.getExperimentalCondition().getGoniostat().getRotationAxisStart().getValue()))
            # Then loop through the subwedges and merge them if possible
            listRemainingSubWedges = listOfSubWedgesWithIdenticalExperimentalConditions
            oCurrentSubWedge = listRemainingSubWedges[0]
            listRemainingSubWedges = listRemainingSubWedges[1:]
            while (len(listRemainingSubWedges) > 0):
                oNextSubWedge = listRemainingSubWedges[0]
                listRemainingSubWedges = listRemainingSubWedges[1:]
                xsDataSubWedgeMerged = self.mergeTwoSubWedgesAdjascentInRotationAxis(oCurrentSubWedge, oNextSubWedge)
                if (xsDataSubWedgeMerged is None):
                    listOfMergedSubWedges.append(oCurrentSubWedge)
                    oCurrentSubWedge = oNextSubWedge
                else:
                    oCurrentSubWedge = xsDataSubWedgeMerged
            listOfMergedSubWedges.append(oCurrentSubWedge)
        return listOfMergedSubWedges
