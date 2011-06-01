#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#                            Grenoble France
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
#
#    Contributing author:    CONTRIBUTING_AUTHOR
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


__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsFile                         import EDUtilsFile
from XSDataSPDv1_0                       import XSDataResultSPDCake
from EDTestCasePluginExecuteSPDCakev1_1 import EDTestCasePluginExecuteSPDCakev1_1

class EDTestCasePluginExecuteSPDCakev1_1withCIFOutput(EDTestCasePluginExecuteSPDCakev1_1):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecuteSPDCakev1_1.__init__(self, )

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputSPDCake_withCIFOutput.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultSPDCake_withCIFOutput.xml"))

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.edf", "darks0001.edf", "flats0001.edf", "EDPluginSPDCakev1_1.cif" ])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultSPDCake.parseString(strExpectedOutput)
        outputFileName = xsDataResultReference.getCakedFile().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if not os.path.isdir(os.path.dirname(outputFileName)):
            os.makedirs(os.path.dirname(outputFileName))
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)

    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultSPDCake.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
#        EDVerbose.DEBUG("Reference XML:%s" + xsDataResultReference.marshal())
#        EDVerbose.DEBUG("Obtained XML:%s" + xsDataResultObtained.marshal())
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")


        # Checking obtained results
        xsDataResultsSPDCake = plugin.getDataOutput()
        strPathToChiOutput = xsDataResultsSPDCake.getCakedFile().getPath().getValue()
        strDataObtained = EDUtilsFile.readFile(strPathToChiOutput)
        strDataReference = EDUtilsFile.readFile(os.path.join(self.getTestsDataImagesHome(), "EDPluginSPDCakev1_1.cif"))
        EDAssert.strAlmostEqual(strDataReference, strDataObtained, "Comparing PowderCIF output")



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    edTestCasePluginExecuteSPDv1_1 = EDTestCasePluginExecuteSPDCakev1_1withCIFOutput("EDTestCasePluginExecuteSPDv1_1")
    edTestCasePluginExecuteSPDv1_1.execute()
