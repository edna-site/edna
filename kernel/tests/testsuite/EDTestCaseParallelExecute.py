# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (Jerome.Kieffer@esrf.eu)
#                       Olof Svensson (svensson@esrf.fr) 
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

"""This is the parallel Execute testing program """

import os, tempfile, types

from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDParallelExecute                   import EDParallelExecute
from EDUtilsParallel                     import EDUtilsParallel

def fakeXML(strInput):
    """Just a fake function that returns an empty XML string"""
    return "<xml></xml>"

class EDTestCaseParallelExecute(EDTestCase):
    """
    Unit & execution test for the EDParallelExecute class
    """

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseParallelExecute")
        self.__edpluginPE = EDParallelExecute("EDPluginTestPluginFactory", fakeXML)


    def unitTestMoveToTempDir(self):
        """
        test the execution of self.movetoTempDir
        """
        initcwd = os.getcwd()
        self.__edpluginPE.moveToTempDir()
        EDAssert.equal(os.path.abspath(os.path.dirname(os.getcwd())), os.path.abspath(tempfile.gettempdir()), "Test Move to Temporary Directory...")
        os.chdir(initcwd)


    def unitTestDetectNumberOfCPUs(self):
        """
        test the execution of detectNumberOfCPUs
        """
        iNbCPU = EDUtilsParallel.detectNumberOfCPUs()
        EDVerbose.unitTest("Detection of the number of Cores: %s" % iNbCPU)
        EDAssert.equal(types.IntType, type(iNbCPU), "Number of CPU is an integer")
        iNbCPU = EDUtilsParallel.detectNumberOfCPUs(1) #limited to 1
        EDAssert.equal(1, iNbCPU, "Limit number of CPU")
        iNbCPU = EDUtilsParallel.detectNumberOfCPUs(100, True) #forced to 100
        EDAssert.equal(100, iNbCPU, "Force number of CPU")

    def process(self):
        self.addTestMethod(self.unitTestMoveToTempDir)
        self.addTestMethod(self.unitTestDetectNumberOfCPUs)
        EDUtilsParallel.uninitializeNbThread()



if __name__ == '__main__':

    edTestCaseEDUtilsTable = EDTestCaseParallelExecute("EDTestCaseParallelExecute")
    edTestCaseEDUtilsTable.execute()
