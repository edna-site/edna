#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:        irakli 
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os
from EDVerbose import EDVerbose
from EDMessage import EDMessage
from EDApplication import EDApplication
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataBoolean

from XSDataSAS import XSDataInputSolutionScattering
from XSDataSAS import XSDataSolutionScatteringSettings

class EDApplicationSASPipeline(EDApplication):

    APPLICATION_NAME = "EDApplicationSASPipeline"
    APPLICATION_VERSION = "0.1"
    DATASET_PARAM_LABEL = "--data"
    NXSQ_PARAM_LABEL = "--nxsQ"
    NXSDATA_PARAM_LABEL = "--nxsData"
    RMAXSTART_PARAM_LABEL = "--rMaxStart"
    RMAXSTOP_PARAM_LABEL = "--rMaxStop"
    RMAXINTERVALS_PARAM_LABEL = "--rMaxIntervals"
    RMAXABSTOL_PARAM_LABEL = "--rMaxAbsTol"
    UNIT_PARAM_LABEL = "--unit"
    SYMMETRY_PARAM_LABEL = "--symmetry"
    MODE_PARAM_LABEL = "--mode"
    THREADS_PARAM_LABEL = "--threads"
    COLUMNS_PARAM_LABEL = "--columns"
    ONLYGNOM_PARAM_LABEL = "--onlyGnom"
    PLOTFIT_PARAM_LABEL = "--plotFit"
    QMIN_PARAM_LABEL = "--qmin"
    QMAX_PARAM_LABEL = "--qmax"
    VERSION_PARAM_LABEL = "--version or -v"
    DEBUG_PARAM_LABEL = "--DEBUG"


    """
    Derives from EDApplication in order to add a Configuration Feature
    """
    def __init__(self, _strPluginName=None, _strConfigurationFileName=None):
        """
        @param _strPluginName: name of control plugin to load
        @type  _strPluginName: string
        @param _strConfigurationFileName: the configuration file to use  
        @type _strConfigurationFileName: string
        """
        EDApplication.__init__(self, _strName=EDApplicationSASPipeline.APPLICATION_NAME, \
                                _strVersion=EDApplicationSASPipeline.APPLICATION_VERSION, \
                                _strPluginName=_strPluginName, \
                                _strConfigurationFileName=_strConfigurationFileName)
        self.__strDatasetFileName = None
        self.__strNxsQ = None
        self.__strNxsData = None
        self.__strDatasetFileName = None
        self.__bProcess = True
        self.__strPluginName = None
        self.__strDataInputFilePath = None
        self.__fRMaxStart = 10.0
        self.__fRMaxStop = 200.0
        self.__iRMaxIntervals = 10
        self.__fRMaxAbsTol = 0.1
        
        self.__strMode = "Fast"
        self.__strSymmetry = "P1"
        self.__bOnlyGnom = False
        self.__bPlotFit = False
        self.__iThreads = None
        self.__iUnit = 1
        self.__iColumns = 1
        self.__fQMin = None
        self.__fQMax = None

    def preProcess(self):
        """
        Processes the command line, creates the plugins
        """
        EDApplication.preProcess(self)
        EDVerbose.DEBUG("EDApplicationSASPipeline.preProcess")

        # Read command line parameters and check if they are ok
        self.__bProcess = self.readAndProcessCommandLine()

    def process(self):
        """
        Calls the Plugin to be executed
        """
        EDVerbose.DEBUG("EDApplicationSASPipeline.process")
        if (not self.isFailure()) and (self.__bProcess):
            edPlugin = EDFactoryPluginStatic.loadPlugin(self.getPluginName())
            if(edPlugin is not None):
                edPlugin.setBaseDirectory(self.getFullApplicationWorkingDirectory())
                edPlugin.setBaseName(self.getPluginName())

                self.setPluginInput(edPlugin)

                edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplicationSASPipeline.process: Executing " + self.getPluginName())
                edPlugin.execute()
                edPlugin.synchronize()
            else:
                EDVerbose.error("EDApplicationSASPipeline .process : plugin not loaded : %s" % self.getPluginName())
                self.setFailure(True)


    def setPluginInput(self, _edPlugin):
        
        _edPlugin.setDataInput(XSDataInputSolutionScattering())
        
        xsDataSolutionScatteringSettings = XSDataSolutionScatteringSettings()
        
        if (not self.__fRMaxStart is None):
            xsDataSolutionScatteringSettings.setRMaxStart(XSDataDouble(self.__fRMaxStart))
        if (not self.__fRMaxStop is None):
            xsDataSolutionScatteringSettings.setRMaxStop(XSDataDouble(self.__fRMaxStop))
        if (not self.__iRMaxIntervals is None):
            xsDataSolutionScatteringSettings.setRMaxIntervals(XSDataInteger(self.__iRMaxIntervals))
        if (not self.__fRMaxAbsTol is None):
            xsDataSolutionScatteringSettings.setRMaxAbsTol(XSDataDouble(self.__fRMaxAbsTol))
        _edPlugin.getDataInput().setRMaxSearchSettings(xsDataSolutionScatteringSettings)
        #_edPlugin.getDataInput().setDataInput(xsDataSolutionScatteringSettings, "rMaxSearchSettings")

        _edPlugin.getDataInput().setTitle(XSDataString(self.__strDatasetFileName))
        
        if (not self.__iUnit is None):
            _edPlugin.getDataInput().setAngularUnits(XSDataInteger(self.__iUnit))
        if (not self.__strSymmetry is None):
            _edPlugin.getDataInput().setSymmetry(XSDataString(self.__strSymmetry))
        if (not self.__strMode is None):
            _edPlugin.getDataInput().setMode(XSDataString(self.__strMode))
        if (self.__bOnlyGnom):
            _edPlugin.getDataInput().setOnlyGnom(XSDataBoolean(True))
        if (self.__bPlotFit):
            _edPlugin.getDataInput().setPlotFit(XSDataBoolean(True))
            
        if (not self.__iThreads is None):
            _edPlugin.getDataInput().setINbThreads(XSDataInteger(self.__iThreads))
            
        if (not self.__strDatasetFileName is None):
            try:
                if (self.__strNxsQ and self.__strNxsData):
                    _edPlugin.readGnomNexusDataColumns(self.__strDatasetFileName, self.__strNxsQ, self.__strNxsData, self.__iColumns, self.__fQMin, self.__fQMax)
                else:
                    _edPlugin.readGnomDataColumns(self.__strDatasetFileName, self.__iColumns, self.__fQMin, self.__fQMax)
                    
            except:
                errorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ("EDApplicationSASPipeline.setPluginInput", self.__strDatasetFileName)
                EDVerbose.error(errorMessage)
                raise RuntimeError, errorMessage


    def readAndProcessCommandLine(self):
        """
        Reads and processes the command line
        """
        EDVerbose.DEBUG("EDApplicationSASPipeline.readAndProcessCommandLine")
        bCommandLineIsOk = False
        # Check if m_strDATASET_PARAM_LABEL is given:
        self.__strDatasetFileName = self.getCommandLineArgument(EDApplicationSASPipeline.DATASET_PARAM_LABEL)
        if (self.__strDatasetFileName is not None):
            if (not os.path.isabs(self.__strDatasetFileName)):
                self.__strDatasetFileName = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.__strDatasetFileName))
            EDVerbose.screen("Reading input data from : %s" % (self.__strDatasetFileName))
            bCommandLineIsOk = True
        else:
            self.usage()
            return bCommandLineIsOk
                
        strNxsQ = self.getCommandLineArgument(EDApplicationSASPipeline.NXSQ_PARAM_LABEL)
        if (strNxsQ is not None):
            self.__strNxsQ = strNxsQ
            EDVerbose.screen("Path to q values in Nexus file                         : %s " % (self.__strNxsQ))
            
        strNxsData = self.getCommandLineArgument(EDApplicationSASPipeline.NXSDATA_PARAM_LABEL)
        if (strNxsData is not None):
            self.__strNxsData = strNxsData
            EDVerbose.screen("Path to data values in Nexus file                         : %s " % (self.__strNxsData))
            
        strUnit = self.getCommandLineArgument(EDApplicationSASPipeline.UNIT_PARAM_LABEL)
        if (strUnit is not None):
            self.__iUnit = int(strUnit)
            EDVerbose.screen("Angular units index set to                         : %d " % (self.__iUnit))
        else:
            EDVerbose.screen("Using default angular units")
            
        strSymmetry = self.getCommandLineArgument(EDApplicationSASPipeline.SYMMETRY_PARAM_LABEL)
        if (strSymmetry is not None):
            self.__strSymmetry = strSymmetry
            EDVerbose.screen("Symmetry set for model building                         : %10s " % (self.__strSymmetry))
        else:
            EDVerbose.screen("Using default symmetry                             : %10s " % (self.__strSymmetry))
            
        strMode = self.getCommandLineArgument(EDApplicationSASPipeline.MODE_PARAM_LABEL)
        if (strMode is not None):
            self.__strMode = strMode
            EDVerbose.screen("Algorithms used to run executable plugins                         : %10s " % (self.__strMode))
        else:
            EDVerbose.screen("Using default algorithms to run executable plugins                          : %10s " % (self.__strMode))
            
        strRMaxStart = self.getCommandLineArgument(EDApplicationSASPipeline.RMAXSTART_PARAM_LABEL)
        if (strRMaxStart is not None):
            self.__fRMaxStart = float(strRMaxStart)
            EDVerbose.screen("rMax search interval starting value set to                         : %7.1f [A]" % (self.__fRMaxStart))
        else:
            EDVerbose.screen("Using default rMax search interval starting value of                         : %7.1f [A]" % (self.__fRMaxStart))
            
        strRMaxStop = self.getCommandLineArgument(EDApplicationSASPipeline.RMAXSTOP_PARAM_LABEL)
        if (strRMaxStop is not None):
            self.__fRMaxStop = float(strRMaxStop)
            EDVerbose.screen("rMax search interval final value set to                         : %7.1f [A]" % (self.__fRMaxStop))
        else:
            EDVerbose.screen("Using default rMax search interval final value of                         : %7.1f [A]" % (self.__fRMaxStop))
            
        strRMaxIntervals = self.getCommandLineArgument(EDApplicationSASPipeline.RMAXINTERVALS_PARAM_LABEL)
        if (strRMaxIntervals is not None):
            self.__iRMaxIntervals = int(strRMaxIntervals)
            EDVerbose.screen("Number of rMax search interval subdivisions set to                         : %d " % (self.__iRMaxIntervals))
        else:
            EDVerbose.screen("Using default number of rMax search interval subdivisions                         : %d " % (self.__iRMaxIntervals))
            
        strRMaxAbsTol = self.getCommandLineArgument(EDApplicationSASPipeline.RMAXABSTOL_PARAM_LABEL)
        if (strRMaxAbsTol is not None):
            self.__fRMaxAbsTol = float(strRMaxAbsTol)
            EDVerbose.screen("Maximal acceptable variation of fit quality in final rMax search interval                         : %2.4f " % (self.__fRMaxAbsTol))
        else:
            EDVerbose.screen("Using default level of acceptable variation of fit quality in final rMax search interval                         : %2.4f " % (self.__fRMaxAbsTol))
            
        if (EDApplicationSASPipeline.ONLYGNOM_PARAM_LABEL in self.getCommandLineArguments()):
            self.__bOnlyGnom = True
            EDVerbose.screen("Pipeline will run only RMax search step")
        if (EDApplicationSASPipeline.PLOTFIT_PARAM_LABEL in self.getCommandLineArguments()):
            self.__bPlotFit = True
            EDVerbose.screen("Pipeline will run only RMax search step")
            
        strThreads = self.getCommandLineArgument(EDApplicationSASPipeline.THREADS_PARAM_LABEL)
        if (strThreads is not None):
            self.__iThreads = int(strThreads)
            EDVerbose.screen("Number of threads run in parallel                         : %d " % (self.__iThreads))
        else:
            EDVerbose.screen("Number of threads run in parallel is set to match number of available CPUs")

        strColumns = self.getCommandLineArgument(EDApplicationSASPipeline.COLUMNS_PARAM_LABEL)
        if (strColumns is not None):
            self.__iColumns = int(strColumns)
            EDVerbose.screen("Number of columns read in                         : %d " % (self.__iColumns))
        else:
            EDVerbose.screen("Reading first column from the data file")
            
        strQMin = self.getCommandLineArgument(EDApplicationSASPipeline.QMIN_PARAM_LABEL)
        if (strQMin is not None):
            self.__fQMin = float(strQMin)
            EDVerbose.screen("Minimal scattering vector value                          : %1.4f " % (self.__fQMin))
        else:
            EDVerbose.screen("No minimal value set for scattering vector")
        strQMax = self.getCommandLineArgument(EDApplicationSASPipeline.QMAX_PARAM_LABEL)
        if (strQMax is not None):
            self.__fQMax = float(strQMax)
            EDVerbose.screen("Maximal scattering vector value                          : %1.4f " % (self.__fQMax))
        else:
            EDVerbose.screen("No maximal value set for scattering vector")
        return bCommandLineIsOk


#    def processCommandLinePluginName(self):
#        """
#        """
#        EDVerbose.DEBUG("EDApplicationSASPipeline.processCommandLinePluginName")
#        if (not self.getEdCommandLine().existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
#            EDVerbose.DEBUG("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
#        else:
#            self.__strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
#            EDVerbose.DEBUG("EDApplicationSASPipeline.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self.__strPluginName))
#
#
    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationSASPipeline.processCommandLineInputFilePath")
        if (not self.getEdCommandLine().existCommand(EDApplicationSASPipeline.DATASET_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplicationSASPipeline.DATASET_PARAM_LABEL)
        else:
            self.__strDataInputFilePath = self.getCommandLineArgument(EDApplicationSASPipeline.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationSASPipeline.processCommandLineInputFilePath : %s = %s" % (EDApplicationSASPipeline.DATASET_PARAM_LABEL, self.__strDataInputFilePath))


    def usage(self):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("----- ")
        EDVerbose.screen("")
        EDVerbose.screen("   run-sas-pipeline.py --data 'datafile' [switch [value]]")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : specifies input file. The file can be space separated multicolumn ASCII file or NeXus data file" % (EDApplicationSASPipeline.DATASET_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : (only for NeXus files) specifies path to the scattering vector values in NeXuS data file" % (EDApplicationSASPipeline.NXSQ_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : (only for NeXus files) specifies path to the intensity values in NeXuS data file" % (EDApplicationSASPipeline.NXSDATA_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" OPTIONAL SWITCHES")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets Rmax search interval starting point [10.0 (default)]" % (EDApplicationSASPipeline.RMAXSTART_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets Rmax search interval final point [200.0 (default)]" % (EDApplicationSASPipeline.RMAXSTOP_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets number of subdivisions of Rmax search interval for every search iteration [10 (default)]" % (EDApplicationSASPipeline.RMAXINTERVALS_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets stopping criteria for Rmax search [0.1 (default)]" % (EDApplicationSASPipeline.RMAXABSTOL_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets number of data columns read from the file [1 (default)]" % (EDApplicationSASPipeline.COLUMNS_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets number of threads which would be used to run jobs in parallel on the local machine or number of jobs submitted to a cluster at one time [number of cores (default)]" % (EDApplicationSASPipeline.THREADS_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets minimal value of the scattering vector interval used in data analysis" % (EDApplicationSASPipeline.QMIN_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : sets maximal value of the scattering vector interval used in data analysis" % (EDApplicationSASPipeline.QMAX_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : specify angular units of the q-axis in input data [A^{-1} (default)]" % (EDApplicationSASPipeline.UNIT_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : specify symmetry enforced on the particle by DAMMIF. Supported values are Pn (n=1...19) and Pn2 (n=1...12). [P1 (default)]" % (EDApplicationSASPipeline.SYMMETRY_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s  {fast|slow} : toggles fast or slow mode for running DAMMIF jobs [fast (default)]" % (EDApplicationSASPipeline.MODE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : runs only Rmax search procedure" % (EDApplicationSASPipeline.ONLYGNOM_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : plot data fit for every GNOM job run during Rmax search procedure" % (EDApplicationSASPipeline.PLOTFIT_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (EDApplicationSASPipeline.DEBUG_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (EDApplicationSASPipeline.VERSION_PARAM_LABEL))
        EDVerbose.screen("")

    def doFailureActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDApplication.doFailureActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationSASPipeline.doFailureActionPlugin")
        EDVerbose.screen("Execution of " + _edPlugin.getPluginName() + " failed.")
        EDVerbose.screen("Please inspect the log file for further information.")


    def doSuccessActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDApplication.doSuccessActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationSASPipeline.doSuccessActionPlugin")

        if (_edPlugin.getListOfErrorMessages() != []):
            self.doFailureActionPlugin(_edPlugin)
        elif (_edPlugin.getListOfWarningMessages() != []):
            EDVerbose.screen("SAS pipeline successful with warning messages, please check the log file.")
        else:
            EDVerbose.screen("SAS pipeline successful!")
