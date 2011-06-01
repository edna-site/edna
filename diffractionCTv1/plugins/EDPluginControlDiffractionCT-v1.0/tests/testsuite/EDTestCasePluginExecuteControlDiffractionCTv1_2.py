# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
from EDVerbose                  import EDVerbose
from EDAssert                   import EDAssert
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from XSDataDiffractionCTv1      import XSDataResultDiffractionCT
from EDFactoryPluginStatic      import EDFactoryPluginStatic

class EDTestCasePluginExecuteControlDiffractionCTv1_2(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlDiffractionCTv1_2")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDiffractionCTv1_2_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultDiffractionCTv1_2_reference.xml"))


    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage("""DCT2011March.edf
DCT2011March_dark.edf
DCT2011March_flat.edf
DCT2011March.spline
DCT2011March.chi""".split())
        for strFile in [os.path.join("/tmp/edna-" + os.environ["USER"], i) for i in ["testSino.h5", "powder0000/DCT2011March.chi", "powder0000/DCT2011March.edf"]]:
            if os.path.isfile(strFile):
                os.remove(strFile)


    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        # Checks the expected result
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = plugin.getDataOutput().marshal() # EDUtilsTest.readAndParseFile ( self.m_edObtainedOutputDataFile )    
        EDVerbose.DEBUG("Checking obtained result...")


        xsDataResultReference = XSDataResultDiffractionCT.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()# XSDataResultDiffractionCT.parseString(strObtainedOutput)

        EDAssert.equal(xsDataResultReference.marshal(), xsDataResultObtained.marshal())

        ref = self.readAndParseFile(os.path.join(self.getTestsDataImagesHome(), "DCT2011March.chi"))
        obt = self.readAndParseFile(xsDataResultObtained.getIntegratedIntensities().getPath().getValue())
        EDAssert.strAlmostEqual(ref, obt, "Chi files are the same", 0.001)

# clean up SPD when finished
        EDFactoryPluginStatic.loadPlugin("EDPluginSPDCorrectv10").killAllWorkers()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlDiffractionCTv1_2 = EDTestCasePluginExecuteControlDiffractionCTv1_2("EDTestCasePluginExecuteControlDiffractionCTv1_2")
    edTestCasePluginExecuteControlDiffractionCTv1_2.execute()
