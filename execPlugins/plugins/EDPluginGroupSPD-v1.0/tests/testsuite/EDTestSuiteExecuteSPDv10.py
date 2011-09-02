#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#
#    Principal author:       Jerome Kieffer (kieffer@esrf.fr)
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

import os, sys


from EDTestSuite                import EDTestSuite
from EDVerbose                  import EDVerbose
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller, installLibrary
from EDFactoryPluginStatic      import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")


################################################################################
# EDNA_SITE is not needed for this plugin so why bother !
################################################################################
if not "EDNA_SITE" in  os.environ:
    os.environ["EDNA_SITE"] = "edna"




class EDTestSuiteExecuteSPDv10(EDTestSuite):


    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_0")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_0withCIFOutput")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_1withCIFOutput")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCorrectv10")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_5")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_5_MokeImage")
        self.addTestCaseFromName("EDTestCasePluginExecuteSPDCakev1_5_mask")
##############################################################################
if __name__ == '__main__':

    edTestSuiteExecuteSPDv10 = EDTestSuiteExecuteSPDv10("EDTestSuiteExecuteSPDv10")
    edTestSuiteExecuteSPDv10.execute()

##############################################################################
