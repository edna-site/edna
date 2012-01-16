#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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


__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
The purpose of this plugin execute class is to be subclassed for
creating plugins that execute external programs through scripts.
"""

import os, sys
from EDAssert import EDAssert
from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDTestCase import EDTestCase
from EDUtilsPlatform import EDUtilsPlatform
from EDUtilsPath import EDUtilsPath

class EDTestCaseEDPluginExecProcessScript(EDTestCase):


    def __init__(self, _strTestName="EDTestCaseEDPluginExecProcessScript"):
        EDTestCase.__init__(self, _strTestName)


    def testGenerateScript(self):
        listCommandPreExecution = ['PRE-EXECUTION1', 'PRE-EXECUTION2 PATATE']
        listCommandExecution = ['COMMAND1', 'COMMAND2 BANANA']
        listCommandPostExecution = ['POST-EXECUTION1', 'POST-EXECUTION2 FRAISE']
        edPluginExecProcessScript = EDPluginExecProcessScript()
        edPluginExecProcessScript.setScriptShell("/bin/bash")
        edPluginExecProcessScript.setScriptBaseName("TestCaseGenerateScript")
        edPluginExecProcessScript.setListCommandPreExecution(listCommandPreExecution)
        edPluginExecProcessScript.setListCommandExecution(listCommandExecution)
        edPluginExecProcessScript.setListCommandPostExecution(listCommandPostExecution)
        edPluginExecProcessScript.setRequireCCP4(True)
        edPluginExecProcessScript.setSetupCCP4("/usr/local/xtal/ccp4-6.0.2/include/ccp4.setup-bash")
        edPluginExecProcessScript.setScriptExecutable("cat")
        edPluginExecProcessScript.configure()
        strScript = edPluginExecProcessScript.prepareScript()
        lstScriptReference = ["#!/bin/bash",
                              "cd %s" % edPluginExecProcessScript.getWorkingDirectory(),
                              ". /usr/local/xtal/ccp4-6.0.2/include/ccp4.setup-bash",
                              "PRE-EXECUTION1",
                              "PRE-EXECUTION2 PATATE",
                              "cat  > TestCaseGenerateScript.log 2> TestCaseGenerateScript.err << EOF-EDPluginExecProcessScript &",
                              "COMMAND1",
                              "COMMAND2 BANANA",
                              "EOF-EDPluginExecProcessScript",
                              "ednaJobPid=$!",
                              "ednaJobHostName=$(hostname)",
                              'echo "$ednaJobHostName $ednaJobPid" > %s' % edPluginExecProcessScript.getPathToHostNamePidFile(),
                              'wait $ednaJobPid',
                              'POST-EXECUTION1',
                              'POST-EXECUTION2 FRAISE',
                              '']
        strScriptReference = EDUtilsPlatform.linesep.join(lstScriptReference)
        EDAssert.equal(strScriptReference, strScript)



    def testGenerateExecutableScript(self):
        listCommands = ['COMMAND1', 'COMMAND2 BANANA']
        edPluginExecProcessScript = EDPluginExecProcessScript()
        edPluginExecProcessScript.setScriptShell("/bin/bash")
        edPluginExecProcessScript.setScriptBaseName("TestCaseGenerateScript")
        edPluginExecProcessScript.setListCommandExecution(listCommands)
        edPluginExecProcessScript.setRequireCCP4(True)
        edPluginExecProcessScript.setSetupCCP4("/usr/local/xtal/ccp4-6.0.2/include/ccp4.setup-bash")
        edPluginExecProcessScript.setScriptExecutable("cat")
        edPluginExecProcessScript.configure()
        strScript = edPluginExecProcessScript.prepareScript()
        edPluginExecProcessScript.writeExecutableScript(strScript)
        strScriptFileName = edPluginExecProcessScript.getScriptFileName()
        strScriptFromFile = edPluginExecProcessScript.readProcessFile(strScriptFileName)
        lstScriptReference = ["#!/bin/bash",
                             "cd %s" % edPluginExecProcessScript.getWorkingDirectory(),
                             ". /usr/local/xtal/ccp4-6.0.2/include/ccp4.setup-bash",
                             "cat  > TestCaseGenerateScript.log 2> TestCaseGenerateScript.err << EOF-EDPluginExecProcessScript &",
                             "COMMAND1",
                             "COMMAND2 BANANA",
                             "EOF-EDPluginExecProcessScript",
                             "ednaJobPid=$!",
                             "ednaJobHostName=$(hostname)",
                             'echo "$ednaJobHostName $ednaJobPid" > %s' % edPluginExecProcessScript.getPathToHostNamePidFile(),
                             "wait $ednaJobPid",
                             ""]
        strScriptReference = EDUtilsPlatform.linesep.join(lstScriptReference)
        EDAssert.equal(strScriptFromFile, strScriptReference)


    def testExecuteScript(self):
        listCommandExecution = list(['COMMAND1', 'COMMAND2 BANANA'])
        strLogReference = EDUtilsPlatform.linesep.join(["COMMAND1", "COMMAND2 BANANA", ""])
        edPluginExecProcessScript = EDPluginExecProcessScript()
        edPluginExecProcessScript.setListCommandExecution(listCommandExecution)
        edPluginExecProcessScript.setRequireCCP4(False)

        edPluginExecProcessScript.setScriptExecutable("%s %s" % (sys.executable,
                                                      os.path.join(EDUtilsPath.EDNA_HOME, "kernel", "bin", "cat.py")))
        edPluginExecProcessScript.setTimeOut(15.0)
        edPluginExecProcessScript.setScriptShell("python")
        from XSDataCommon import XSData
        edPluginExecProcessScript.setXSDataInputClass(XSData)
        edPluginExecProcessScript.execute()
        edPluginExecProcessScript.synchronize()
        strScriptLogFileName = edPluginExecProcessScript.getScriptLogFileName()
        strLogFromFile = edPluginExecProcessScript.readProcessLogFile()
        EDAssert.equal(strLogFromFile, strLogReference)


    def process(self):
        self.addTestMethod(self.testGenerateScript)
        self.addTestMethod(self.testGenerateExecutableScript)
        self.addTestMethod(self.testExecuteScript)


if __name__ == '__main__':

    edTestCaseEDPluginExecProcessScript = EDTestCaseEDPluginExecProcessScript("TestCase EDPluginExecProcessScript")
    edTestCaseEDPluginExecProcessScript.execute()
