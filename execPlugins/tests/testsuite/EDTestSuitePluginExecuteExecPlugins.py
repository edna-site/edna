#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteMXPluginExec.py 923 2009-10-27 13:35:32Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
#                            Jerome Kieffer (Jerome.Kieffer@esrf.fr)
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
__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDTestSuite                        import EDTestSuite
from EDUtilsLibraryInstaller            import installLibrary
from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_6")
EDFactoryPluginStatic.loadModule("EDInstallScipyv0_7_1")
EDFactoryPluginStatic.loadModule("EDInstallH5Pyv1_3_0")


################################################################################
# EDNA_SITE is not needed for this plugin so why bother !
################################################################################
if "EDNA_SITE" not in  os.environ:
    os.environ["EDNA_SITE"] = "edna"





class EDTestSuitePluginExecuteExecPlugins(EDTestSuite):


    def process(self):
        """
        List of execution tests to be run
        """
# accumulator
        self.addTestSuiteFromName("EDTestSuitePluginExecuteAccumulatorv1_0")


#Command Line
        self.addTestCaseFromName("EDTestCasePluginExecuteExecCommandLinev10")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecCommandLinev10_fireAndForget")
#Thumbnail
        self.addTestSuiteFromName("EDTestSuitePluginExecThumbnailv10")
#Video
        self.addTestCaseFromName("EDTestCasePluginExecuteExecVideov10")
        self.addTestCaseFromName("EDTestCasePluginExecuteExecVideov10_minimal")
#Fit2D
#        self.addTestCaseFromName("EDTestCasePluginExecuteFIT2DCakev1_0")
#SPD
        self.addTestSuiteFromName("EDTestSuiteExecuteSPDv10")
#SAXS
        self.addTestSuiteFromName("EDTestSuitePluginExecuteGroupSaxsv1_0")
# HDF5
        self.addTestSuiteFromName("EDTestSuitePluginExecuteHDF5")
#WaitFile
        self.addTestSuiteFromName("EDTestSuitePluginExecuteWaitFile")
#EDF
        self.addTestSuiteFromName("EDTestSuitePluginExecuteEDFv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteFilterImage")
#Atsas        
        self.addTestSuiteFromName("EDTestSuiteExecuteAtsas")
#Shift
        self.addTestSuiteFromName("EDTestSuitePluginExecExecuteShift")
##############################################################################
if __name__ == '__main__':

    edTestSuitePluginExecuteExecPlugins = EDTestSuitePluginExecuteExecPlugins("EDTestSuitePluginExecuteExecPlugins")
    edTestSuitePluginExecuteExecPlugins.execute()

##############################################################################
