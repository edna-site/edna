#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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
__contact__ = "Jerome.Kieffer@ESRF.eu"
__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, shutil, string
from EDVerbose                  import EDVerbose
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from XSDataCommon               import XSDataFile
from XSDataCommon               import XSDataString
from XSDataCommon               import XSPluginItem
from XSDataExecCommandLine      import XSDataInputExecCommandLine
from XSDataExecCommandLine      import XSDataResultExecCommandLine


class EDPluginExecCommandLinev10(EDPluginExecProcessScript):
    """
    This is execution plugin that will create a shell script, running the command line program 
    with the given options and filename and puts the processed file in the output directory    
    """


    def __init__(self):
        """
        Initialization of the plugin Exec CommandLine
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputExecCommandLine)

    def checkParameters(self):
        """
        Checks the mandatory parameters like the name of the program and the input filename
        """
        self.DEBUG("EDPluginExecCommandLinev10.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.commandLineProgram, "No command line program provided")
        self.checkMandatoryParameters(self.dataInput.inputFileName, "No input filename provided")



    def preProcess(self, _edObject=None):
        """
        Pre-Process: Generate the script 
        """
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecCommandLinev10.preProcess")
        self.generateScript()

    def postProcess(self, _edObject=None):
        """
        Post-Process: set the output of the plugin
        """
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecCommandLinev10.postProcess")

        # Create some output data
        xsDataResult = XSDataResultExecCommandLine()
        if self.dataInput.getFireAndForget() is not None:
            if self.dataInput.getFireAndForget().value is True:
                self.setDataOutput(xsDataResult)
                return
        if self.dataInput.getOutfileFromStdout() is not None:
            #self.DEBUG("*** getOutfileFromStdout = %s" % self.dataInput.getOutfileFromStdout().value)
            if self.dataInput.getOutfileFromStdout().value : # this is not clean ... should be 1 or True ... or whatever
                if self.dataInput.getOutputPath() is not None:
                    outputPath = self.dataInput.getOutputPath().path.value
                    stdout = os.path.join(self.getWorkingDirectory() , self.getScriptLogFileName())

                    self.synchronizeOn()
                    if os.path.isdir(outputPath):
                        outfile = os.path.join(outputPath, os.path.split(self.dataInput.inputFileName.path.value)[1])
                    else:
                        outfile = outputPath
                    if os.path.isfile(outfile):
                            takenNames = []
                            [mydir, myname] = os.path.split(outfile)
                            for onefile in os.listdir(mydir):
                                if onefile.find(myname) == 0:
                                    takenNames.append(onefile)
                            for ext in string.digits + string.ascii_lowercase:
                                if not (outfile + ext) in takenNames:
                                    outfile += ext
                                    break
                    shutil.move(stdout , outfile)
                    self.synchronizeOff()

                    xsDataFile = XSDataFile()
                    xsDataFile.setPath(XSDataString(outfile))
                    xsDataResult.setOutputFilename(xsDataFile)
                else:
                    xsDataResult.setOutputFilename(self.getScriptLogFileName())
        self.setDataOutput(xsDataResult)

    def configure(self):
        """
        Here we override the EDPluginExecProcessScript.configure method BEFORE calling it.
        we define especially the executable that should come from the input-XML and not from the Site-XML.
        This is the main difference with EDPluginExecProcessScript.

        The configure method modifies also the stdout from .log to .out ... if we are re-using stdout for the result  

        """
        self.DEBUG("EDPluginExecCommandLinev10.configure")
        self.setScriptExecutable(self.dataInput.commandLineProgram.path.value)
        if self.dataInput.getCommandLineOptions() :
            strOptions = self.dataInput.getCommandLineOptions().value + " " + self.dataInput.inputFileName.path.value
        else:
            strOptions = self.dataInput.inputFileName.path
        self.setScriptCommandline(strOptions)
        xsPluginItem = XSPluginItem()
        self.setConfiguration(xsPluginItem)

        if self.dataInput.getOutfileFromStdout() is not None:
            if self.dataInput.getOutfileFromStdout().value :
                if (self.getScriptBaseName() == None):
                    self.setScriptBaseName(self.getBaseName())
                if (self.getScriptLogFileName() == None):
                    self.setScriptLogFileName(self.getScriptBaseName() + ".out")
        # And finally we call the configure method of the parent.  
        EDPluginExecProcessScript.configure(self)

    def prepareScript(self):
        """
        Returns a string containing the script to be excuted, either by a shell or by a a cluster management tool.
        """
        self.DEBUG("EDPluginExecCommandLine.generateScript")
        lstScript = ["#!%s" % self.getScriptShell()]
        lstScript.append("cd %s" % self.getWorkingDirectory())
        # Execution
        lstScript.append("%s %s > %s 2> %s &" % (self.getScriptExecutable(),
                                           self.getScriptCommandline(),
                                           self.getScriptLogFileName(),
                                           self.getScriptErrorLogFileName()))

        lstScript.append("ednaJobPid=$! ")
        lstScript.append("ednaJobHostName=$(hostname)")
        lstScript.append("echo ${ednaJobHostName} ${ednaJobPid} > %s" % self.getPathToHostNamePidFile())
        lstScript.append("wait $ednaJobPid")

        # Add post-execution commands - if any
        lstScript += self.getListCommandPostExecution()
        return os.linesep.join(lstScript)





