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

__authors__ = ["Jérôme Kieffer"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""This is the EDJob interface for launching jobs"""

import  time
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDStatus                            import EDStatus


class EDTestCaseEDStatus(EDTestCase):
    """
    Unit test for status
    """
    strPluginName = "EDPluginTestPluginFailure"

    def unitTestInitialState(self):
        """
        check the status after a job creation
        """
        EDVerbose.DEBUG("EDTestCaseEDStatus.unitTestInitialState")
        EDVerbose.DEBUG("Success Plugins: " + ",".join(EDStatus.getSuccess()))
        EDVerbose.DEBUG("Running Plugins: " + ",".join(EDStatus.getRunning()))
        EDVerbose.DEBUG("Failed Plugins: " + ",".join(EDStatus.getFailure()))
        EDAssert.equal(False, self.strPluginName in EDStatus.getRunning(), "Plugin not yet running")
        EDAssert.equal(False, self.strPluginName in EDStatus.getSuccess(), "Plugin not yet Finished")
        EDAssert.equal(False, self.strPluginName in EDStatus.getFailure(), "Plugin not yet Finished")


    def unitTestRunning(self):
        """
        check the status after a job creation
        """
        EDVerbose.DEBUG("EDTestCaseEDStatus.unitTestRunning")
        EDStatus.tellRunning(self.strPluginName)
        EDVerbose.DEBUG("Success Plugins: " + ",".join(EDStatus.getSuccess()))
        EDVerbose.DEBUG("Running Plugins: " + ",".join(EDStatus.getRunning()))
        EDVerbose.DEBUG("Failed Plugins: " + ",".join(EDStatus.getFailure()))
        EDAssert.equal(True, self.strPluginName in EDStatus.getRunning(), "Plugin  running")
        EDAssert.equal(False, self.strPluginName in EDStatus.getSuccess(), "Plugin not yet Finished")
        EDAssert.equal(False, self.strPluginName in EDStatus.getFailure(), "Plugin not yet Finished")

    def unitTestFailed(self):
        """
        check the failure of a plugin is registerd 
        """
        EDVerbose.DEBUG("EDTestCaseEDStatus.unitTestFailed")
        EDStatus.tellFailure(self.strPluginName)
        EDVerbose.DEBUG("Success Plugins: " + ",".join(EDStatus.getSuccess()))
        EDVerbose.DEBUG("Running Plugins: " + ",".join(EDStatus.getRunning()))
        EDVerbose.DEBUG("Failed Plugins: " + ",".join(EDStatus.getFailure()))
        EDAssert.equal(False, self.strPluginName in EDStatus.getRunning(), "Plugin not yet running")
        EDAssert.equal(False, self.strPluginName in EDStatus.getSuccess(), "Plugin not yet Finished")
        EDAssert.equal(True, self.strPluginName in EDStatus.getFailure(), "Plugin Failed as expected")

    def process(self):
        self.addTestMethod(self.unitTestInitialState)
        self.addTestMethod(self.unitTestRunning)
        self.addTestMethod(self.unitTestFailed)


if __name__ == '__main__':

    edTestCase = EDTestCaseEDStatus("EDTestCaseEDStatus")
    edTestCase.execute()
