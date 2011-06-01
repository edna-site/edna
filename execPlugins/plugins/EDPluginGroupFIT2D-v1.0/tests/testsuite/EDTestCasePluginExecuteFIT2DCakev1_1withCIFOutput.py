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
#from EDUtilsPath                         import EDUtilsPath
from EDUtilsFile                         import EDUtilsFile


from EDTestCasePluginExecuteFIT2DCakev1_1 import EDTestCasePluginExecuteFIT2DCakev1_1

class EDTestCasePluginExecuteFIT2DCakev1_1withCIFOutput(EDTestCasePluginExecuteFIT2DCakev1_1):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecuteFIT2DCakev1_1.__init__(self, "EDPluginFIT2DCakev1_1withCIFOutput")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputFIT2DCake_withCIFOutput.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultFIT2DCake_reference.xml"))








##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################


if __name__ == '__main__':
    edTestCasePluginExecuteFIT2Dv1_1 = EDTestCasePluginExecuteFIT2Dv1_1()
    edTestCasePluginExecuteFIT2Dv1_1.execute()
