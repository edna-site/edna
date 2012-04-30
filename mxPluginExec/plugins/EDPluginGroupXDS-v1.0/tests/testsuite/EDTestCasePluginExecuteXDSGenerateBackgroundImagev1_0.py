#
#    Project: EDNA mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteXDSGenerateBackgroundImagev1_0.py 1505 2010-05-10 10:18:00Z svensson $"
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"

import os

from EDVerbose                        import EDVerbose
from EDAssert                         import EDAssert
from EDUtilsPath                      import EDUtilsPath
from EDTestCasePluginExecute          import EDTestCasePluginExecute
from EDUtilsTest                      import EDUtilsTest




class EDTestCasePluginExecuteXDSGenerateBackgroundImagev1_0(EDTestCasePluginExecute):


    def __init__(self, _pyStrTestName="EDPluginXDSGenerateBackgroundImagev1_0"):
        EDTestCasePluginExecute.__init__(self, _pyStrTestName)

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSIndexing_reference.xml"))

        #self.setReferenceDataOutputFile( os.path.join( self.getPluginTestsDataHome(), "XSDataResultXDSIndexing_reference.xml"))
        #self.m_oedObtainedOutputDataFile = self.getPluginName() + "_output.xml"



    def testExecute(self):
        self.run()




    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteMOSFLMv1_0Indexing = EDTestCasePluginExecuteMOSFLMv1_0Indexing("EDTestCasePluginExecuteMOSFLMv1_0Indexing")
    edTestCasePluginExecuteMOSFLMv1_0Indexing.execute()
