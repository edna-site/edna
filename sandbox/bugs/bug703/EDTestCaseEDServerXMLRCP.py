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
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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

"""Test case for the EDNA XML/RCP server for plugin wrappers"""

import  time
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDJob                               import EDJob

from EDServerXMLRCP import EDServerXMLRCP

from EDPluginWrapperForJobScheduler import EDPluginWrapperForJobScheduler


class EDTestCaseEDServerXMLRCP(EDTestCase):
    """
    Unit & execution test for the EDParallelExecute class
    """
    strPluginName = "EDPluginTestPluginFactory"
    strXmlInput = """<?xml version="1.0" ?>
<XSDataString>
    <value>Test string value.</value>
</XSDataString>"""
    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDServerXMLRCP")


    def testStartServer(self):
        """
        check the status after a job creation
        """
        edServer = EDServerXMLRCP.getInstance()
        if not edServer:
            EDAssert.equal(not None, edServer, "Server instance None")


    def testRegisterPluginWrapper(self):
        edServer = EDServerXMLRCP.getInstance()
        strPluginName = "EDPluginTestPluginFactory"
        edPlugin = EDPluginWrapperForJobScheduler(strPluginName)
        edServer.registerPlugin(edPlugin)
        strId = str(edPlugin.getId())
        edPluginRegistered = edServer.getRegisteredPlugin(strId)
        if not  edPluginRegistered:
            EDAssert.equal(not None, edPluginRegistered, "Registered plugin")
        edServer.unRegisterPlugin(edPlugin)
        edPluginRegistered = edServer.getRegisteredPlugin(strId)
        EDAssert.equal(None, edPluginRegistered, "Plugin unregistered")

    def callBackSUCCESS(self, _edPlugin):
        """
        Example of Call Back function ... 
        """
        EDAssert.equal(False, _edPlugin.isFailure(), "From Callback: Plugin %d is finished with ''success''" % _edPlugin.getId())


    def testCallbackSUCCESS(self):
        edServer = EDServerXMLRCP.getInstance()
        strPluginName = "EDPluginTestPluginFactory"
        edPlugin = EDPluginWrapperForJobScheduler(strPluginName)
        edPlugin.connectSUCCESS(self.callBackSUCCESS)
        edServer.registerPlugin(edPlugin)
        edPlugin.executeSynchronous()
        edServer.shutdown()



    def process(self):
        self.addTestMethod(self.testStartServer)
        self.addTestMethod(self.testRegisterPluginWrapper)
        self.addTestMethod(self.testCallbackSUCCESS)


if __name__ == '__main__':

    edTestCaseEDServerXMLRCP = EDTestCaseEDJob("EDTestCaseEDServerXMLRCP")
    edTestCaseEDServerXMLRCP.execute()
