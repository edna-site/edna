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
        EDVerbose.DEBUG("EDPluginExecCommandLinev10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getCommandLineProgram(), "No command line program provided")
        self.checkMandatoryParameters(self.getDataInput().getInputFileName(), "No input filename provided")



    def preProcess(self, _edObject=None):
        """
        Pre-Process: Generate the script 
        """
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecCommandLinev10.preProcess")
        self.generateScript()

    def postProcess(self, _edObject=None):
        """
        Post-Process: set the output of the plugin
        """
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecCommandLinev10.postProcess")

        # Create some output data
        xsDataResult = XSDataResultExecCommandLine()
        if self.getDataInput().getFireAndForget() is not None:
            if self.getDataInput().getFireAndForget().getValue() is True:
                self.setDataOutput(xsDataResult)
                return
        if self.getDataInput().getOutfileFromStdout() is not None:
            #EDVerbose.DEBUG("*** getOutfileFromStdout = %s" % self.getDataInput().getOutfileFromStdout().getValue())
            if self.getDataInput().getOutfileFromStdout().getValue() : # this is not clean ... should be 1 or True ... or whatever
                if self.getDataInput().getOutputPath() is not None:
                    outputPath = self.getDataInput().getOutputPath().getPath().getValue()
                    stdout = os.path.join(self.getWorkingDirectory() , self.getScriptLogFileName())

                    self.synchronizeOn()
                    if os.path.isdir(outputPath):
                        outfile = os.path.join(outputPath, os.path.split(self.getDataInput().getInputFileName().getPath().getValue())[1])
                    else:
                        outfile = outputPath
#                        outpath = os.path.dirname(outfile)
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
        EDVerbose.DEBUG("EDPluginExecCommandLinev10.configure")
        self.setScriptExecutable(self.getDataInput().getCommandLineProgram().getPath().getValue())
        if self.getDataInput().getCommandLineOptions() :
            strOptions = self.getDataInput().getCommandLineOptions().getValue() + " " + self.getDataInput().getInputFileName().getPath().getValue()
        else:
            strOptions = self.getDataInput().getInputFileName().getPath()
        self.setScriptCommandline(strOptions)
        xsPluginItem = XSPluginItem()
        self.setConfiguration(xsPluginItem)

        if self.getDataInput().getOutfileFromStdout() is not None:
            if self.getDataInput().getOutfileFromStdout().getValue() :
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
        EDVerbose.DEBUG("EDPluginExecCommandLine.generateScript")

        strScript = "#!" + self.getScriptShell() + "\ncd " + self.getWorkingDirectory() + "\n"
        # Execution
        strScript += self.getScriptExecutable() + " " + self.getScriptCommandline() + " > " + self.getScriptLogFileName() + " 2> " + self.getScriptErrorLogFileName()
        strScript += "&\nednaJobPid=$!\n"
        strScript += "ednaJobHostName=$(hostname)\n"
        strScript += "echo \"$ednaJobHostName $ednaJobPid\" > %s\n" % self.getPathToHostNamePidFile()
        strScript += "wait $ednaJobPid\n"
        # Add post-execution commands - if any
        if (len(self.getListCommandPostExecution()) > 0):
            for strCommandPostExecution in self.getListCommandPostExecution():
                strScript += strCommandPostExecution + "\n"
        return strScript

        return strScript




