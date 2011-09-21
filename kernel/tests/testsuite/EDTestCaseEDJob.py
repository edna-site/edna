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

"""This is the EDJob interface for launching jobs"""

import  time
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDJob                               import EDJob



class EDTestCaseEDJob(EDTestCase):
    """
    Unit & execution test for the EDParallelExecute class
    """
    strPluginName = "EDPluginTestPluginFactory"
    strXmlInput = """<?xml version="1.0" ?>
<XSDataString>
    <value>Test string value.</value>
</XSDataString>"""
    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDJob")
#        self.__edpluginPE = EDParallelExecute("EDPluginTestPluginFactory", fakeXML)


    def unitTestInitialState(self):
        """
        check the status after a job creation
        """
        EDVerbose.DEBUG("EDTestCaseEDJob.unitTestInitialState")
        edJob = EDJob(self.strPluginName)
        strJobId = edJob.getJobId()
        EDVerbose.DEBUG("EDJobId is: %s" % strJobId)
        EDAssert.equal(2, len(strJobId.split("-")), "JobID is composed of 2 parts")
        EDAssert.equal(True, strJobId.split("-")[1].isdigit(), "JobID's second part is an integer")
        EDAssert.equal("uninitialized", edJob.getStatus(), "Initial stat is ''uninitialized''")


    def unitTestSetGetData(self):
        """
        check the status after a job creation
        """
        EDVerbose.DEBUG("EDTestCaseEDJob.unitTestSetGetData")
        edJob = EDJob(self.strPluginName)
        edJob.setDataInput(self.strXmlInput)
        EDAssert.equal(self.strXmlInput, edJob.getDataInput().strip(), "Data Input is correctly set")
        EDAssert.equal("uninitialized", edJob.getStatus(), "Job %s is still ''uninitialized''" % edJob.getJobId())

    def unitTestExecute(self):
        """
        check the execution of a job (without callback)
        """
        EDVerbose.DEBUG("EDTestCaseEDJob.unitTestExecute")
        edJob = EDJob(self.strPluginName)
        strJobId = edJob.getJobId()
        edJob.setDataInput(self.strXmlInput)
        ref = edJob.execute()
        EDAssert.equal(strJobId, ref, "JobId has not changed")
        strStatus = edJob.getStatus()
        EDVerbose.WARNING("Job %s in State %s" % (strJobId, strStatus))

        while strStatus in ["running", "uninitialized"]:
            EDVerbose.WARNING("Job %s in state %s" % (strJobId, strStatus))
            time.sleep(0.01)
            strStatus = edJob.getStatus()

        xsdOut = edJob.getDataOutput()
        while xsdOut is None:
            EDVerbose.WARNING("No Output data, still waiting for output data to arrive, %s" % edJob.getStatus())
            time.sleep(0.01)
            xsdOut = edJob.getDataOutput()
        strOutput = xsdOut.strip()
        strStatus = edJob.getStatus()
        while strStatus == "running":
            EDVerbose.WARNING("Job %s is still in state %s" % (strJobId, strStatus))
            time.sleep(0.01)
            strStatus = edJob.getStatus()

        EDAssert.equal(strOutput, self.strXmlInput, "Output is OK")
        EDAssert.equal("success", edJob.getStatus(), "Job %s is finished with ''success''" % edJob.getJobId())


    def callBack(self, _strJobId):
        """
        Example of Call Back function ... 
        """
        myJob = EDJob.getJobFromID(_strJobId)
        strOutput = myJob.getDataOutput().strip()
        EDAssert.equal(strOutput, self.strXmlInput, "From Callback: Output is OK")
        EDAssert.equal("success", myJob.getStatus(), "From Callback: Job %s is finished with ''success''" % _strJobId)


    def unitTestExecuteCallback(self):
        """
        check the execution of a job (without callback)
        """
        EDVerbose.DEBUG("EDTestCaseEDJob.unitTestExecuteCallback")
        edJob = EDJob(self.strPluginName)
        edJob.connectCallBack(self.callBack)
        edJob.setDataInput(self.strXmlInput)
        strJobId = edJob.execute()
        strStatus = edJob.getStatus()
        EDVerbose.DEBUG("Job %s in State ''%s''" % (strJobId, strStatus))

    def unitTestExecuteCallbackSuccess(self):
        """
        check the execution of a job (without callback)
        """
        EDVerbose.DEBUG("EDTestCaseEDJob.unitTestExecuteCallbackSuccess")
        edJob = EDJob(self.strPluginName)
        edJob.connectSUCCESS(self.callBack)
        edJob.setDataInput(self.strXmlInput)
        strJobId = edJob.execute()
        strStatus = edJob.getStatus()
        EDVerbose.DEBUG("Job %s in State ''%s''" % (strJobId, strStatus))


    def process(self):
        self.addTestMethod(self.unitTestInitialState)
        self.addTestMethod(self.unitTestSetGetData)
        self.addTestMethod(self.unitTestExecuteCallback)
        self.addTestMethod(self.unitTestExecuteCallbackSuccess)
        self.addTestMethod(self.unitTestExecute)


if __name__ == '__main__':

    edTestCaseEDJob = EDTestCaseEDJob("EDTestCaseEDJob")
    edTestCaseEDJob.execute()
