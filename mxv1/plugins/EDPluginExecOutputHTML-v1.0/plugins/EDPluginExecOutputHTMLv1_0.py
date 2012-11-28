#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Olof Svensson
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

"""
This plugin is using EDNA2html written by P. Briggs for creating an HTML
page containing the summary of an EDNA MXv1 characterisation.
"""

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, subprocess, shutil

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDConfiguration import EDConfiguration

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation


class EDPluginExecOutputHTMLv1_0(EDPluginExec):
    """
    This plugin does not need any input data, it can use its directory hierarchy
    for providing the necessary "--run_basename" for EDNA2html. However, if inputs 
    are provided, then these will be used instead.

    There are three optional input parameters:
      "title"       : The title to use for the strategy
      "basename"    : The directory where the HTML should go ("_html" is automatically appended)
      "workingDir"  : The directory containing the EDNA MXv1 application run files
    
    There are two output data items:
    
      "htmlFile" : Path to the generated HTML file
      "htmlDir"  : Path to the generated HTML directory
      
    In order for this plugin to work the path to the "EDNA2html" package written
    by Peter Briggs should either be configured in the plugin configuration 
    (name=EDNA2html,value=pathToEDNA2html) or the environment variable
    "EDNA2html" should be set to this path.
    """


    CONF_EDNA2html = "EDNA2html"

    def __init__(self):
        EDPluginExec.__init__(self)
        self.strWorkingDirectory = None
        self.strWorkingDir = None
        self.strEDNA2html = None
        self.strTitle = None
        self.strBasename = None
        self.strPath = None
        
#        if not os.environ.has_key("EDNA2html"):
#            self.setRequiredToHaveConfiguration(True)
        if os.environ.has_key("PATH"):
            self.strPath = os.environ["PATH"]
        self.setXSDataInputClass(XSDataString, "title")
        self.setXSDataInputClass(XSDataString, "basename")
        self.setXSDataInputClass(XSDataString, "workingDir")
        self.setXSDataInputClass(XSDataFile, "dnaFileDirectory")


    def configure(self):
        EDPluginExec.configure(self)
        EDVerbose.DEBUG("EDPluginExecOutputHTMLv1_0.configure")
        self.strEDNA2html = self.config.get(self.CONF_EDNA2html)
        if self.strEDNA2html is None and os.environ.has_key("EDNA2html"):
            self.strEDNA2html = os.environ["EDNA2html"]
        else:
            self.strEDNA2html = EDFactoryPluginStatic.getModuleLocation("EDNA2html")
        pass


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecOutputHTMLv1_0.process")
        dictEnv = os.environ.copy()
        dictEnv["PATH"] = self.strPath + ":" + dictEnv["PATH"]
        
        if self.strEDNA2html is None:
            EDVerbose.ERROR("Cannot find EDNA2html directory!")
            self.setFailure()
        else:
            strCommandArgs = os.path.join(self.strEDNA2html, "EDNA2html")

            if (self.hasDataInput("basename") and self.hasDataInput("workingDir")):

                if self.hasDataInput("title"):
                    self.strTitle = self.getDataInput("title")[0].getValue()
                    if self.strTitle != "":
                        strCommandArgs += " --title=\""+self.strTitle+"\"" 
                
                if self.hasDataInput("basename"):
                    self.strBasename = self.getDataInput("basename")[0].getValue()
                    strCommandArgs += " --basename="+os.path.join(self.strBasename, "edna") 

                if self.hasDataInput("workingDir"):
                    self.strWorkingDir = self.getDataInput("workingDir")[0].getValue()
                    strCommandArgs += " --run_basename=" + self.strWorkingDir
                    
                strCommandArgs += " --portable"

                #
                # Execute the script
                #
                subprocessEDNA2html = subprocess.Popen(strCommandArgs, shell=True, env={"EDNA2html": self.strEDNA2html,\
                                                                                        "PATH": dictEnv["PATH"]})
                subprocessEDNA2html.wait()
                
            else:
                # We have now to find the "basename" directory. This is a horrible hack -
                # we simply look for a directory and a file with the same name +".log"...
                # Look at most four levels above
                for iLevels in range(4):
                    strBaseDir = self.getWorkingDirectory()
                    for j in range(iLevels):
                        strBaseDir = os.path.abspath(os.path.join(strBaseDir, ".."))
                    EDVerbose.DEBUG("strBaseDir: " + strBaseDir)
                    # Now search for a .log file...
                    for strFileName in os.listdir(strBaseDir):
                    
                        if strFileName.endswith(".log"):
                            # Check that the corresponding direcory exists...
                            strDirectoryName = strFileName[:-4]
                            if os.path.isdir(os.path.join(strBaseDir, strDirectoryName)):
                                # Final check - is the directory name in the working dir
                                if self.getWorkingDirectory().find(strDirectoryName) != -1:
                                    # Ok, we found it!
                                    self.strWorkingDir = os.path.join(strBaseDir, strDirectoryName)
                                    break
                if self.strWorkingDir is not None:
                    strCommandArgs += " --run_basename=" + self.strWorkingDir + " --portable"
                    #
                    # Execute the script
                    #
                    subprocessEDNA2html = subprocess.Popen(strCommandArgs, shell=True, env={"EDNA2html": self.strEDNA2html,\
                                                                                            "PATH": dictEnv["PATH"]})
                    subprocessEDNA2html.wait()


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecOutputHTMLv1_0.postProcess")
        if self.strWorkingDir != None:
            xsDataFileHTMLFile = XSDataFile()
            xsDataFileHTMLDir = XSDataFile()
            
            if self.strBasename is None:
                strHTMLFilePath = os.path.join(self.strWorkingDir, "edna.html")
                strHTMLDirPath = os.path.join(self.strWorkingDir, "edna_html")
            else:
                strHTMLFilePath = os.path.join(self.strBasename, "edna.html")
                strHTMLDirPath = os.path.join(self.strBasename, "edna_html")
            
            if os.path.exists(strHTMLFilePath):
                strFileContent = EDUtilsFile.readFile(strHTMLFilePath)
                strFileContent = strFileContent.replace("table,td,th { border-style: none;", "div.edna table,td,th { border-style: none;")
                strFileContent = strFileContent.replace("td,th { border-style: solid;", "div.edna td,th { border-style: solid;")
                strFileContent = strFileContent.replace("th { background-color: gray;", "div.edna th { background-color: gray;")
                strFileContent = strFileContent.replace("<body onload=\"initTable('strategyData',false,false);\">", "<body onload=\"initTable('strategyData',false,false);\"><div class = 'edna'> ")
                strFileContent = strFileContent.replace("</body>", "</div></body>")
                EDUtilsFile.writeFile(strHTMLFilePath, strFileContent)
                xsDataFileHTMLFile.setPath(XSDataString(strHTMLFilePath))
                xsDataFileHTMLDir.setPath(XSDataString(strHTMLDirPath))
                self.setDataOutput(xsDataFileHTMLFile, "htmlFile")
                self.setDataOutput(xsDataFileHTMLDir, "htmlDir")
            else:
                EDVerbose.ERROR("EDPluginExecOutputHTMLv1_0.postProcess: file doesn't exist: " + strHTMLFilePath)


