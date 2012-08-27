#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Principal author:      Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Karl Levik"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

import os.path


from EDAssert                         import EDAssert
from EDUtilsFile                      import EDUtilsFile
from EDTestCasePluginExecute          import EDTestCasePluginExecute
from EDUtilsTest                      import EDUtilsTest
from XSDataCommon                     import XSDataString
from EDFactoryPluginStatic            import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataInterfacev1_2")
from XSDataInterfacev1_2              import XSDataInputInterface

class EDTestCasePluginExecuteMxv1ParamsToXMLv1_0(EDTestCasePluginExecute):
    """
    """

    def __init__(self, _edStringTestName=None):
        """
        Sets config file + input and output reference files. 
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginMxv1ParamsToXMLv1_0", "EDPluginGroupMxv1ParamsToXML-v1.0", _edStringTestName)
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "paramString.txt"), "paramString")

    def testExecute(self):
        """
        Runs the plugin and marshals the obtained XML file into an XSDataInputInterface object 
        """
        self.run()
        edPlugin = self.getPlugin()
        xsDataOutputObtained = edPlugin.getDataOutput()
        strXMLFile = xsDataOutputObtained.getPath().getValue()
        
        strObtainedOutput = self.readAndParseFile(strXMLFile)
        xsDataInputInterfaceObtained = XSDataInputInterface.parseString(strObtainedOutput)

        self.DEBUG("Checking obtained result...")
        self.DEBUG("Found class of type: %s" % xsDataInputInterfaceObtained.__class__.__name__)
        # Just quickly check that we have an actual XSDataInputInterface object 
        EDAssert.equal(xsDataInputInterfaceObtained.__class__.__name__ == "XSDataInputInterface", True)


##############################################################################

    def process(self):
        """
        Adds the plugin execute test methods
        """
        self.addTestMethod(self.testExecute)

##############################################################################

if __name__ == '__main__':
    edTestCasePluginExecuteMxv1ParamsToXMLv1_0 = EDTestCasePluginExecuteMxv1ParamsToXMLv1_0("EDTestCasePluginExecuteMxv1ParamsToXMLv1_0")
    edTestCasePluginExecuteMxv1ParamsToXMLv1_0.execute()
