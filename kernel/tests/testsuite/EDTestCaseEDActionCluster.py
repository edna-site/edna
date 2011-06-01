#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseEDActionCluster.py 1472 2010-05-03 12:51:05Z svensson $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
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

__author__ = "Olof Svensson" 
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDAction import EDAction
from EDActionCluster import EDActionCluster
from EDAssert import EDAssert
from EDTestCase import EDTestCase


class EDActionSuccess(EDAction):

    def process(self, _edAction=None):
        self.DEBUG("Processing EDActionSuccess with id %s" % str(self.getId()))
    

class EDActionFailure(EDAction):

    def process(self, _edAction=None):
        self.DEBUG("Processing EDActionFailure with id %s" % str(self.getId()))
        self.setFailure()


class EDTestCaseEDActionCluster(EDTestCase):
    """
    This is the test case for the plugin base class EDPlugin.
    """

    def testExecuteActionClusterWithSuccess(self):
        """
        Test the EDActionCluster with actions ending in success
        """
        edActionCluster = EDActionCluster()
        for i in range(10):
            edAction = EDActionSuccess()
            edActionCluster.addAction(edAction)
        edActionCluster.executeSynchronous()
        EDAssert.equal(False, edActionCluster.isFailure(), "EDActionCluster ended in success")

    
    def testExecuteActionClusterWithFailure(self):
        """
        Test the EDActionCluster with actions ending in success
        """
        edActionCluster = EDActionCluster()
        for i in range(10):
            edAction = EDActionSuccess()
            edActionCluster.addAction(edAction)
        edActionFailure = EDActionFailure()
        edActionCluster.addAction(edActionFailure)
        edActionCluster.executeSynchronous()
        EDAssert.equal(True, edActionCluster.isFailure(), "EDActionCluster ended in failure")

    
    
    def process(self):
        self.addTestMethod(self.testExecuteActionClusterWithSuccess)
        self.addTestMethod(self.testExecuteActionClusterWithFailure)




if __name__ == '__main__':

    EDTestCaseEDActionCluster = EDTestCaseEDActionCluster("TestCase EDPluginExecProcessScript")
    EDTestCaseEDActionCluster.execute()
