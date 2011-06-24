# coding: utf8
#
#    Project: BioSaxs: bio-saxs data reduction
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@esrf.eu)
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2010, ESRF Grenoble"

import os

from EDVerbose                  import EDVerbose
from EDAssert                   import EDAssert
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDUtilsPlatform           import EDUtilsPlatform

import os, sys
from EDFactoryPluginStatic      import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSpecClient")

################################################################################
# EDNA_SITE is not needed for this plugin so why bother !
################################################################################
if "EDNA_SITE" not in  os.environ:
    os.environ["EDNA_SITE"] = "edna"



class EDTestCasePluginExecuteBioSaxsReprocessv1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsReprocessv1_0")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
                                               "XSConfiguration_BioSaxsReprocess.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsReprocess_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsReprocess_reference.xml"))


    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsReprocessv1_0 = EDTestCasePluginExecuteBioSaxsReprocessv1_0("EDTestCasePluginExecuteBioSaxsReprocessv1_0")
    edTestCasePluginExecuteBioSaxsReprocessv1_0.execute()
