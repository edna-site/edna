# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseParallelExecute.py 2548 2010-12-01 09:14:01Z kieffer $"
#
#    Copyright (C) 2011-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (Jerome.Kieffer@esrf.eu)
#                        
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

__authors__ = ["Jérôme Kieffer", "Olof Svensson"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110722"

"""Test cases for testing EDShare"""

import  time, tempfile, os
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDShare                             import EDShare
from EDFactoryPluginStatic               import EDFactoryPluginStatic
from EDUtilsPath                         import EDUtilsPath
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallH5Pyv1_3_0")
if "USER" not in os.environ:
    os.environ["USER"] = "ednatester"



class EDTestCaseEDShare(EDTestCase):
    """
    Unit test for EDNA-share for sharing large objects between plugins
    """

    def unitTestInitialState(self):
        """
        Check the initialization of the share:
        """
        EDAssert.equal(False, EDShare.isInitialized(), "Check that EDShare is uninitialized")
        strEdnaUserTempFolder = EDUtilsPath.getEdnaUserTempFolder()
        EDShare.initialize(strEdnaUserTempFolder)
        EDShare["test1"] = range(10)
        EDVerbose.screen("Backend used is %s" % EDShare.backend)
        EDAssert.equal(1, len(EDShare.items()))
        EDAssert.equal(True, "test1" in EDShare, "list is actually present")
        for i, j in zip(range(10), EDShare["test1"]):
            EDAssert.equal(i, j, "elements are the same")
        EDShare.close()
        EDShare.initialize(strEdnaUserTempFolder)
        EDAssert.equal(True, "test1" in EDShare, "list is still present")
        for i, j in zip(range(10), EDShare["test1"]):
            EDAssert.equal(i, j, "elements are still the same")
        filename = EDShare.filename
        EDShare.close(remove=True)
        EDAssert.equal(False, os.path.isfile(filename), "dump-file has been removed")


    def process(self):
        self.addTestMethod(self.unitTestInitialState)


if __name__ == '__main__':

    edTestCase = EDTestCaseEDShare("EDTestCaseEDShare")
    edTestCase.execute()
