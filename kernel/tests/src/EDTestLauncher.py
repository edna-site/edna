#coding: utf8
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
#                       Jérôme Kieffer 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"

import os, sys, time

from EDVerbose import EDVerbose
from EDCommandLine import EDCommandLine
from EDUtilsTest import EDUtilsTest
from EDApplication import EDApplication
from EDTestSuite import EDTestSuite



class EDTestLauncher(EDApplication):
    """
    Some DocStrings ?
    """
    TEST_LABEL = "--test"
    QUIET_LABEL = "--quiet"

    def __init__ (self):
        EDApplication.__init__(self)
        self.__edTestCase = None
        EDVerbose.setTestOn()


    def preProcess(self):
        """
        Scans the command line.
        """
        EDVerbose.DEBUG("EDTestLauncher.preProcess")
        edCommandLine = EDCommandLine(sys.argv)
        EDVerbose.log(self.getEdCommandLine().getCommandLine())
        self.processCommandLineDebugVerboseLogFile()
        bContinue = True
        strTestName = edCommandLine.getArgument(EDTestLauncher.TEST_LABEL)
        EDVerbose.DEBUG("EDTestLauncher.preProcess: test name = %r" % strTestName)
        if (strTestName is None):
            EDVerbose.screen("ERROR - no --test argument found")
            bContinue = False
        else:
            self.__edTestCase = EDUtilsTest.getFactoryPluginTest().loadPlugin(strTestName)
        if (bContinue):
            # Determine the base directory
            if(self.getBaseDir() is None):
                self.processCommandLineBaseDirectory()
            # Create the application working directory  
            strApplicationInstanceName = strTestName + "_" + time.strftime("%Y%m%d-%H%M%S", time.localtime())
            if(self.getWorkingDir() is None):
                self.setWorkingDir(strApplicationInstanceName)
            self.createApplicationWorkingDirectory()
            # Set the name of the log file
            EDVerbose.setLogFileName(os.path.join(self.getBaseDir(), strApplicationInstanceName + ".log"))
            # The check for --quiet and --DEBUG should ideally be placed elsewhere,
            # for example in EDApplication.
            if (edCommandLine.existCommand(EDTestLauncher.QUIET_LABEL)):
                EDVerbose.setVerboseOff()
                EDVerbose.setTestOff()
            if (edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_1) or \
                edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_2)):
                EDVerbose.setVerboseDebugOn()
                EDVerbose.DEBUG("EDTestLauncher.preProcess: Debug mode")



    def process(self):
        """
        Executes the test case / test suite
        """
        EDVerbose.DEBUG("EDTestLauncher.process")
        if (self.__edTestCase is not None):
            EDVerbose.DEBUG("EDTestLauncher.process: launching test : %s" % self.__edTestCase.getTestName())
            self.__edTestCase.execute()


    def isFailure(self):
        """
        Returns True if the number of failures (test methods and test cases) is 0.
        Returns False if the number of failures (test methods and test cases) is different than 0.
        Returns None if there's no test case or test suite defined.
        """
        bValue = None
        if (self.__edTestCase is not None):
            bValue = self.__edTestCase.getNumberTestMethodFailure() != 0
            if isinstance(self.__edTestCase, EDTestSuite):
                bValue = bValue or (self.__edTestCase.getNumberTestCaseFailure() != 0)
        return bValue
