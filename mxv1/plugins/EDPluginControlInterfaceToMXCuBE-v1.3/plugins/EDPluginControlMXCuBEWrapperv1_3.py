#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, time, string, random

from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile
from EDUtilsPath import EDUtilsPath
from XSDataMXCuBEv1_3 import XSDataInputMXCuBE
from XSDataMXCuBEv1_3 import XSDataResultMXCuBE


class EDPluginControlMXCuBEWrapperv1_3( EDPluginControl ):
    """
    The purpose of this plugin is to run the EDPluginControlInterfaceToMXCuBEv1_3
    in a new process.
    """

    def __init__( self ):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMXCuBE)   
        self.strMXCuBEPlugin = "EDPluginControlInterfaceToMXCuBEv1_3"


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlMXCuBEWrapperv1_3.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataSet(), "dataSet")

    
    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlMXCuBEWrapperv1_3.process")
        # Check that if image path contains RAW_DATA the current working directory should be PROCESSED_DATA
        strTimeString = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time())) + "-%06d" % random.randint(0,1000000)
        strWorkingDir = self.getWorkingDirectory()
        strProcessedDataDir = strWorkingDir
        xsDataMXCuBEDataSet = self.getDataInput().getDataSet()[0]
        strFirstImagePath = xsDataMXCuBEDataSet.getImageFile()[0].getPath().getValue()
        if strFirstImagePath.find("RAW_DATA") != -1:
            strCurrentWorkingDirectory = os.getcwd()
            strCurrentProcessedDataDir = os.path.dirname(strCurrentWorkingDirectory)
            strProcessedDataDir = os.path.dirname(string.replace(strFirstImagePath, "RAW_DATA", "PROCESSED_DATA"))
            if strCurrentProcessedDataDir != strProcessedDataDir:
                strEDAppliDir = "EDApplication_" + strTimeString
                strNewLogFileName = os.path.join(strProcessedDataDir, strEDAppliDir + ".log")
                strWorkingDir = os.path.join(strProcessedDataDir, strEDAppliDir, self.getBaseName())
                if not os.path.exists(strWorkingDir):
                    os.makedirs(strWorkingDir, 0755)
        # Write out input XML file
        strPathToInputFile = os.path.join(strProcessedDataDir, "EDNA_Input_%s.xml" % strTimeString)
        strPathToOutputFile = os.path.join(strProcessedDataDir, "EDNA_Output_%s.xml" % strTimeString)
        EDUtilsFile.writeFile(strPathToInputFile, self.getDataInput().marshal())
        strScript = "export EDNA_SITE=%s\n" % EDUtilsPath.getEdnaSite()
        strScript += "/opt/pxsoft/bin/edna-plugin-launcher"
        strScript += " --execute %s" % self.strMXCuBEPlugin
        strScript += " --inputFile %s" % strPathToInputFile
        strScript += " --outputFile %s" % strPathToOutputFile
        strScript += " --basedir %s" % strProcessedDataDir
        strScript += " 2>&1\n"
        strScriptFileName = "edna_start_%s.sh" % strTimeString
        strScriptPath = os.path.join(strProcessedDataDir, strScriptFileName)
        EDUtilsFile.writeFile(strScriptPath, strScript)
        # TODO: Make the script executable
        os.system("bash %s" % strScriptPath)
        xsDataResultMXCuBE = XSDataResultMXCuBE()
        if os.path.exists(strPathToOutputFile):
            strOutput = EDUtilsFile.readFile(strPathToOutputFile)
            xsDataResultMXCuBE = XSDataResultMXCuBE.parseString(strOutput)
        self.setDataOutput(xsDataResultMXCuBE)
            
