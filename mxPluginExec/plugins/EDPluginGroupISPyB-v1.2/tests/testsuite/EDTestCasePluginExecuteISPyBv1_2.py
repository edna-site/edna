#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:  Marie-Francoise Incardona (incardon@esrf.fr)
#                           Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Karl Levik, Marie-Francoise Incardona, Olof Svensson"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"
__date__ = "20120712"
__status__ = "production"

import os.path

from EDImportLib                      import EDVerbose
from EDAssert                         import EDAssert
from EDUtilsFile                      import EDUtilsFile
from EDTestCasePluginExecute          import EDTestCasePluginExecute
from EDUtilsTest                      import EDUtilsTest

from XSDataISPyBv1_2                  import XSDataResultISPyB
from XSDataISPyBv1_2                  import XSDataISPyBScreeningStrategy
from XSDataCommon                     import XSDataString

class EDTestCasePluginExecuteISPyBv1_2(EDTestCasePluginExecute):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginISPyBv1_2", "EDPluginGroupISPyB-v1.2", _edStringTestName)

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screening.xml"), "screening")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screeningInput.xml"), "screeningInput")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screeningOutputContainer.xml"), "screeningOutputContainer")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screeningRank.xml"), "screeningRank")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screeningRankSet.xml"), "screeningRankSet")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_screeningFile.xml"), "screeningFile")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataISPyBv1_2Input_reference_image.xml"), "image")




        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultISPyB_reference.xml"))
        self.__strObtainedOutputDataFile = self.getPluginName() + "_output.xml"

    def preProcess(self):
        """
        Deletes the obtained output from the previous run. 
        """
        EDTestCasePluginExecute.preProcess(self)
        EDUtilsFile.deleteFile(self.__strObtainedOutputDataFile)

    def testHttpPost(self):
        """
        A test for whether the httpPost method can send a request to the dbserver and receive a response
        """
        edPluginISPyB = self.createPlugin()
        xsPluginItemISPyB = self.getPluginConfiguration(os.path.join(self.getPluginTestsDataHome(), "XSConfiguration.xml"))
        edPluginISPyB.setConfiguration(xsPluginItemISPyB)
        edPluginISPyB.configure()

        strXML = '<?xml version="1.0" encoding="UTF-8"?><Proposal><code>nt</code><number>20</number></Proposal>'
        strResponse = edPluginISPyB.httpPost(edPluginISPyB.getDbserverHost(), edPluginISPyB.getDbserverPort(), '/proposal_request', strXML)
        if strResponse != None:
            self.DEBUG("*** EDTestCasePluginExecuteISPyBv1_2.testHttpPost response: " + strResponse)

        EDAssert.equal(strResponse != None, True)


    def testExecute(self):
        """
        Runs the plugin and then compares expected output with obtained output to verify that it executed correctly. 
        """
        self.run()

        # Checks the obtained result against the expected result
        edStringExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        edStringObtainedOutput = self.readAndParseFile(self.__strObtainedOutputDataFile)

        xsDataResultISPyBExpected = XSDataResultISPyB.parseString(edStringExpectedOutput)
        xsDataResultISPyBObtained = XSDataResultISPyB.parseString(edStringObtainedOutput)

        self.DEBUG("Checking obtained result...")

        xsDataIntegerExpDataCollectionId = xsDataResultISPyBExpected.getDataCollectionId()
        xsDataResultStatusExpScreening = xsDataResultISPyBExpected.getScreeningStatus()
        xsDataResultStatusExpScreeningInputs = xsDataResultISPyBExpected.getScreeningInputStatus()
        xsDataResultStatusExpScreeningOutputs = xsDataResultISPyBExpected.getScreeningOutputStatus()
        xsDataResultStatusExpScreeningOutputLattices = xsDataResultISPyBExpected.getScreeningOutputLatticeStatus()
        xsDataResultStatusExpScreeningStrategies = xsDataResultISPyBExpected.getScreeningStrategyStatus()
        xsDataResultStatusExpScreeningStrategyWedges = xsDataResultISPyBExpected.getScreeningStrategyWedgeStatus()
        xsDataResultStatusExpScreeningStrategySubWedges = xsDataResultISPyBExpected.getScreeningStrategySubWedgeStatus()
        xsDataResultStatusExpScreeningRanks = xsDataResultISPyBExpected.getScreeningRankStatus()
        xsDataResultStatusExpScreeningRankSet = xsDataResultISPyBExpected.getScreeningRankSetStatus()

        xsDataIntegerDataCollectionId = xsDataResultISPyBObtained.getDataCollectionId()
        xsDataResultStatusScreening = xsDataResultISPyBObtained.getScreeningStatus()
        xsDataResultStatusScreeningInputs = xsDataResultISPyBObtained.getScreeningInputStatus()
        xsDataResultStatusScreeningOutputs = xsDataResultISPyBObtained.getScreeningOutputStatus()
        xsDataResultStatusScreeningOutputLattices = xsDataResultISPyBObtained.getScreeningOutputLatticeStatus()
        xsDataResultStatusScreeningStrategies = xsDataResultISPyBObtained.getScreeningStrategyStatus()
        xsDataResultStatusScreeningStrategyWedges = xsDataResultISPyBObtained.getScreeningStrategyWedgeStatus()
        xsDataResultStatusScreeningStrategySubWedges = xsDataResultISPyBObtained.getScreeningStrategySubWedgeStatus()
        xsDataResultStatusScreeningRanks = xsDataResultISPyBObtained.getScreeningRankStatus()
        xsDataResultStatusScreeningRankSet = xsDataResultISPyBObtained.getScreeningRankSetStatus()

        if xsDataIntegerExpDataCollectionId != None:
            self.DEBUG("Checking dataCollectionId ...")
            EDAssert.equal(xsDataIntegerDataCollectionId.getValue(), xsDataIntegerExpDataCollectionId.getValue())
        if xsDataResultStatusExpScreening != None:
            self.DEBUG("Checking screening ...")
            EDAssert.equal(xsDataResultStatusScreening.getCode().getValue(), "ok")
            iId = xsDataResultStatusScreening.getId().getValue()
            EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningInputs != None:
            self.DEBUG("Checking inputs...")
            for xsDataResultStatusScreeningInput in xsDataResultStatusScreeningInputs:
                EDAssert.equal(xsDataResultStatusScreeningInput.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningInput.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningOutputs != None:
            self.DEBUG("Checking outputs ...")
            for xsDataResultStatusScreeningOutput in xsDataResultStatusScreeningOutputs:
                EDAssert.equal(xsDataResultStatusScreeningOutput.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningOutput.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningOutputLattices != None:
            self.DEBUG("Checking output lattices...")
            for xsDataResultStatusScreeningOutputLattice in xsDataResultStatusScreeningOutputLattices:
                EDAssert.equal(xsDataResultStatusScreeningOutputLattice.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningOutputLattice.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningStrategies != None:
            self.DEBUG("Checking strategies...")
            for xsDataResultStatusScreeningStrategy in xsDataResultStatusScreeningStrategies:
                EDAssert.equal(xsDataResultStatusScreeningStrategy.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningStrategy.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningStrategyWedges != None:
            self.DEBUG("Checking strategy wedges...")
            for xsDataResultStatusScreeningStrategyWedge in xsDataResultStatusScreeningStrategyWedges:
                EDAssert.equal(xsDataResultStatusScreeningStrategyWedge.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningStrategyWedge.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningStrategySubWedges != None:
            self.DEBUG("Checking strategy subwedges...")
            for xsDataResultStatusScreeningStrategySubWedge in xsDataResultStatusScreeningStrategySubWedges:
                EDAssert.equal(xsDataResultStatusScreeningStrategySubWedge.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningStrategySubWedge.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusExpScreeningRanks != None:
            self.DEBUG("Checking ranks...")
            for xsDataResultStatusScreeningRank in xsDataResultStatusScreeningRanks:
                EDAssert.equal(xsDataResultStatusScreeningRank.getCode().getValue(), "ok")
                iId = xsDataResultStatusScreeningRank.getId().getValue()
                EDAssert.equal((iId >= 0), True)
        if xsDataResultStatusScreeningRankSet != None:
            self.DEBUG("Checking rank sets...")
            EDAssert.equal(xsDataResultStatusScreeningRankSet.getCode().getValue(), "ok")
            iId = xsDataResultStatusScreeningRankSet.getId().getValue()
            EDAssert.equal((iId >= 0), True)

##############################################################################

    def process(self):
        """
        Adds the plugin execute test methods
        """
        #self.addTestMethod( self.testHttpPost )
        self.addTestMethod(self.testExecute)

##############################################################################

if __name__ == '__main__':
    edTestCasePluginExecuteISPyBv1_2 = EDTestCasePluginExecuteISPyBv1_2("EDTestCasePluginExecuteISPyBv1_2")
    edTestCasePluginExecuteISPyBv1_2.execute()
