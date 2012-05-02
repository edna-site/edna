#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 INSTITUTE_LINE_1
#                            INSTITUTE_LINE_2
#
#    Principal author:       PRINCIPAL_AUTHOR
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

import os
from EDImportLib                         import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsFile                         import EDUtilsFile




class EDTestCasePluginExecuteFIT2DCakev1_0(EDTestCasePluginExecute):
    """
    """

    def __init__(self):
        """
        """
        self.EPSILON_REL = 0.01 #1 percent error
        self.EPSILON_ABS = 0.0001 #1 percent error
        EDTestCasePluginExecute.__init__(self, "EDPluginFIT2DCakev1_0", "EDPluginControlFIT2D-v1.0")

        self.setConfigurationFile(self.getRefConfigFile())

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputFIT2DCake_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultFIT2DCake_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        strSplineFileName = "frelon_spline_file_to_correct_SPD.spline"
        strPathToSplineFile = os.path.join(self.getTestsDataImagesHome(), strSplineFileName)
        if (not os.path.exists(strPathToSplineFile)):
            EDUtilsFile.copyFile(os.path.join(self.getPluginTestsDataHome(), strSplineFileName), \
                                  strPathToSplineFile)

        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.edf", "darks0001.edf", "flats0001.edf" ])



    def testExecute(self):
        """
        """
        self.run()

        # Checks that there are no error messages

        plugin = self.getPlugin()

        EDVerbose.DEBUG("Checking error messages...")
        EDAssert.equal(self.m_iNoErrorMessages, self.getErrorMessages().getNumberObjects())

        EDVerbose.DEBUG("Checking warning messages...")
        EDAssert.equal(self.m_iNoWarningMessages, self.getWarningMessages().getNumberObjects())

        # Checking obtained results
        xsDataResultsFIT2DCake = plugin.getDataOutput()
        strPathToChiOutput = xsDataResultsFIT2DCake.getResultFile().getPath().getValue()
        strDataObtained = EDUtilsFile.readFile(strPathToChiOutput)
        strDataReference = EDUtilsFile.readFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                             "EDPluginFIT2DCakev1_0.chi"))
        bEqual = (strDataReference == strDataObtained)
        if not bEqual:
            lstDataReference = strDataReference.split()
            lstDataObtained = strDataObtained.split()
            if len(lstDataReference) == len(lstDataObtained):
                EDVerbose.DEBUG("Checking for small numerical error...Relative:%s Absolute: %s" % (self.EPSILON_REL, self.EPSILON_ABS))
                bEqual = True
                for i in xrange(len(lstDataReference)):
                    if lstDataReference[i] != lstDataObtained[i]:
                        try:
                            r = float(lstDataReference[i])
                            o = float(lstDataObtained[i])
                        except Exception:
                            bEqual = False
                            break
                        if (2 * abs(r - o) / (o + r) > self.EPSILON_REL) and abs(r - o) > self.EPSILON_ABS:
                            EDVerbose.DEBUG("MisMatch: %s,%s" % (r, o))
                            bEqual = False
                            break

        EDAssert.equal(bEqual, True)



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteFIT2Dv1_0 = EDTestCasePluginExecuteFIT2Dv1_0()
    edTestCasePluginExecuteFIT2Dv1_0.execute()
