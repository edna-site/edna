# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF Grenoble
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

__author__="Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF Grenoble"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteBioSaxsReduceFileSeriev1_0(EDTestCasePluginExecute):
    

    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsReduceFileSeriev1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_BioSaxsReduceFileSerie.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsReduceFileSerie_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsReduceFileSerie_reference.xml"))
                 
        
    def testExecute(self):
        """
        """ 
        self.run()
        


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)

        
        

if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsReduceFileSeriev1_0 = EDTestCasePluginExecuteBioSaxsReduceFileSeriev1_0("EDTestCasePluginExecuteBioSaxsReduceFileSeriev1_0")
    edTestCasePluginExecuteBioSaxsReduceFileSeriev1_0.execute()
