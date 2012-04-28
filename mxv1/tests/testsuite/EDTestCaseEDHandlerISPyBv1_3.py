#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
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


__authors__ = [ "Olof Svensson", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, tempfile

from EDAssert                            import EDAssert
from EDTestCase                          import EDTestCase
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath
from EDUtilsFile                         import EDUtilsFile
from EDFactoryPluginStatic               import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDHandlerXSDataISPyBv1_3")
from EDHandlerXSDataISPyBv1_3 import EDHandlerXSDataISPyBv1_3

from XSDataMXv1 import XSDataInputControlISPyB

class EDTestCaseEDHandlerISPyBv1_3(EDTestCase):


    def __init__(self, _pyStrTestName=None):
        EDTestCase.__init__(self, _pyStrTestName)
        strMXv1DataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDHandlerISPyBv1_3"
        self.strDataPath = os.path.join(strMXv1DataHome, strDataDir)
        self.dictReplace = {"${EDNA_TESTIMAGES}": EDUtilsPath.EDNA_TESTIMAGES,
                       "${EDNA_HOME}": EDUtilsPath.getEdnaHome(),
                       "${USER}":  os.getenv("USER", "UndefindedUser"),
                       "${TMPDIR}": os.getenv("TMPDIR", tempfile.gettempdir()),
                        }


    def testGenerateXSDataInputISPyB(self):
        """
        This method is testing the generation of the XSDataInputISPyB object given a XSDataIndexingInput object.
        """
        strReferenceInputControlISPyBFile = EDUtilsPath.mergePath(self.strDataPath, "XSDataInputControlISPyB_reference.xml")
        strPath = os.path.join(self.strDataPath, strReferenceInputControlISPyBFile)
        strXMLIndexingInput = EDUtilsFile.readFileAndParseVariables(strPath, self.dictReplace)
        xsDataInputControlISPyB = XSDataInputControlISPyB.parseString(strXMLIndexingInput)
        xsDataInputISPyB = EDHandlerXSDataISPyBv1_3.generateXSDataInputISPyBStoreScreening(xsDataInputControlISPyB)
        print xsDataInputISPyB.marshal()
        strReferenceInputISPyBFile = EDUtilsPath.mergePath(self.strDataPath, "XSDataInputISPyB_reference.xml")
        strReferencePath = os.path.join(self.strDataPath, strReferenceInputISPyBFile)
        strXMLInputISPyBReference = EDUtilsFile.readFileAndParseVariables(strReferencePath, self.dictReplace)
        EDFactoryPluginStatic.loadModule("XSDataISPyBv1_3")
        #xsDataInputISPyBReference = XSDataInputISPyBScreening.parseString(strXMLInputISPyBReference)
        # Remove the time strings since they otherwise make the test fail
        #xsDataInputISPyBReference.getScreening().setTimeStamp(None)
        #xsDataInputISPyB.getScreening().setTimeStamp(None)
        #EDAssert.equal(xsDataInputISPyBReference.marshal(), xsDataInputISPyB.marshal())



    def process(self):
        self.addTestMethod(self.testGenerateXSDataInputISPyB)



if __name__ == '__main__':

    edTestCaseEDHandlerISPyBv1_3 = EDTestCaseEDHandlerISPyBv1_3("EDTestCaseEDHandlerISPyBv1_3")
    edTestCaseEDHandlerISPyBv1_3.execute()

