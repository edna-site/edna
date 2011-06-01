#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString

from XSDataMXv1 import XSDataIndexingResult
from XSDataMXv1 import XSDataImageQualityIndicators

class EDPluginExecEvaluationIndexingv10(EDPluginExec):
    """
    This plugin evaluates the results of the indexing and image quality indicators.
    
    The "indexingSuccess" output is of type XSDataBoolean
    
    The "indexingComments" output is of type XSDataString
    """


    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataIndexingResult, "indexingResult")
        self.setXSDataInputClass(XSDataImageQualityIndicators, "imageQualityIndicators")
        self.__xsDataIndexingResult = None
        self.__listXSDataImageQualityIndicator = None
        self.__bIndexingSuccess = False
        self.__strStatusMessageIndexing = None
        self.__strStatusMessageImageQualityIndicators = None


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        # Read in input data (if any)
        if self.hasDataInput("indexingResult"):
            self.__xsDataIndexingResult = self.getDataInput("indexingResult")[0]
        if self.hasDataInput("imageQualityIndicators"):
            self.__listXSDataImageQualityIndicator = self.getDataInput("imageQualityIndicators")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecEvaluationIndexingv10.process")
        #
        # Check for eventual warning messages due to few number of spots, ice rings etc:
        #
        bMessageAdded = False
        strStatusMessageImageQualityIndicators = ""
        if self.__listXSDataImageQualityIndicator != None:
            # Sort the images
            listXSDataImageQualityIndicatorSorted = sorted(self.__listXSDataImageQualityIndicator, key=lambda xsDataImageQualityIndicator: xsDataImageQualityIndicator.getImage().getNumber().getValue())
            for xsDataImageQualityIndicator in listXSDataImageQualityIndicatorSorted:
                iImageNo = xsDataImageQualityIndicator.getImage().getNumber().getValue()
                strImageStatusMessage = "Image no %d:" % iImageNo
                iNumberOfGoodBraggCandidates = xsDataImageQualityIndicator.getGoodBraggCandidates().getValue()
                iIceRings = xsDataImageQualityIndicator.getIceRings().getValue()
                bImageMessageAdded = False
                if iNumberOfGoodBraggCandidates < 5:
                    strImageStatusMessage += " blank image"
                    bImageMessageAdded = True
                elif iNumberOfGoodBraggCandidates < 40:
                    strImageStatusMessage += " WARNING: only %d spots" % iNumberOfGoodBraggCandidates
                    bImageMessageAdded = True
                if iIceRings == 1:
                    if bImageMessageAdded:
                        strImageStatusMessage += ", "
                    strImageStatusMessage += " ice/powder ring detected"
                    bImageMessageAdded = True
                elif iIceRings > 1:
                    if bImageMessageAdded:
                        strImageStatusMessage += ", "
                    strImageStatusMessage += " %d ice/powder rings detected" % iIceRings
                    bImageMessageAdded = True
                if bImageMessageAdded:
                    if bMessageAdded:
                        strStatusMessageImageQualityIndicators += " "
                    strStatusMessageImageQualityIndicators += strImageStatusMessage + "."
                    bMessageAdded = True
        #
        # Try to evaluate the results. Evidently, if there's no xsDataIndexingResult 
        # as input the result should be failure:
        #
        strStatusMessageIndexing = ""
        if self.__xsDataIndexingResult == None:
            self.__bIndexingSuccess = False
            strStatusMessageIndexing += "Indexing FAILURE."
        else:
            self.__bIndexingSuccess = True
            xsDataIndexingSolutionSelected = self.__xsDataIndexingResult.getSelectedSolution()
            xsDataCrystal = xsDataIndexingSolutionSelected.getCrystal()
            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
            strSpaceGroupName = xsDataSpaceGroup.getName().getValue()
            strStatusMessageIndexing += "Indexing successful (%s)." % strSpaceGroupName
        self.__strStatusMessageImageQualityIndicators = strStatusMessageImageQualityIndicators
        self.__strStatusMessageIndexing = strStatusMessageIndexing



    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        if self.__xsDataIndexingResult != None:
            self.setDataOutput(self.__xsDataIndexingResult, "indexingResult")
        else:
            self.__bIndexingSuccess = False
        self.setDataOutput(XSDataBoolean(self.__bIndexingSuccess), "indexingSuccess")
        if self.__strStatusMessageIndexing != None:
            self.setDataOutput(XSDataString(self.__strStatusMessageIndexing), "statusMessageIndexing")
        if self.__strStatusMessageImageQualityIndicators != None:
            self.setDataOutput(XSDataString(self.__strStatusMessageImageQualityIndicators), "statusMessageImageQualityIndicators")


