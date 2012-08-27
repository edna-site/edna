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

import os.path, glob

from EDVerbose import EDVerbose
from EDMessage import EDMessage
from EDApplication import EDApplication
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataIfeffit import XSDataInputSpline
from XSDataIfeffit import XSDataInputFFTF
from XSDataIfeffit import XSDataInputXAFSDataBatchProcessing

from XSDataIfeffit import XSDataFloat

class EDApplicationXAFSBatchProcessing(EDApplication):

    APPLICATION_NAME = "EDApplicationXAFSBatchProcessing"
    APPLICATION_VERSION = "0.1"
    DATASET_PARAM_LABEL = "--data"
    NXSENERGY_PARAM_LABEL = "--nxsEnergy"
    NXSI0_PARAM_LABEL = "--nxsI0"
    NXSIREF_PARAM_LABEL = "--nxsIref"
    NXSIT_PARAM_LABEL = "--nxsIt"
    NXSTIME_PARAM_LABEL = "--nxsTime"
    NXSLNI0IREF_PARAM_LABEL = "--nxsLnI0Iref"
    NXSLNI0IT_PARAM_LABEL = "--nxsLnI0It"
    RBKG_PARAM_LABEL = "--rbkg"
    KMIN_PARAM_LABEL = "--kmin"
    KMAX_PARAM_LABEL = "--kmax"
    DK_PARAM_LABEL = "--dk"
    KWEIGHT_PARAM_LABEL = "--kweight"
    VERSION_PARAM_LABEL = "--version or -v"
    DEBUG_PARAM_LABEL = "--DEBUG"


    """
    Derives from EDApplication in order to add a Configuration Feature
    """
    def __init__(self, _strPluginName=None, _strConfigurationFileName=None, _bUseWSGI=False):
        """
        @param _strPluginName: name of control plugin to load
        @type  _strPluginName: string
        @param _strConfigurationFileName: the configuration file to use  
        @type _strConfigurationFileName: string
        """
        EDApplication.__init__(self, _strName=EDApplicationXAFSBatchProcessing.APPLICATION_NAME, \
                                _strVersion=EDApplicationXAFSBatchProcessing.APPLICATION_VERSION, \
                                _strPluginName=_strPluginName, \
                                _strConfigurationFileName=_strConfigurationFileName)
        self.__strDatasetFileName = None
        self.__strDataInputFilePath = None
        
        self.__strNxsEnergy = '/entry1/counterTimer01/Energy'
        self.__strNxsI0 = '/entry1/counterTimer01/I0'
        self.__strNxsIref = '/entry1/counterTimer01/Iref'
        self.__strNxsIt = '/entry1/counterTimer01/It'
        self.__strNxsTime = '/entry1/counterTimer01/Time'
        self.__strNxsLnI0Iref = '/entry1/counterTimer01/lnI0Iref'
        self.__strNxsLnI0It = '/entry1/counterTimer01/lnI0It'
        self.__strNxsScanIndex = '/entry1/entry_identifier'
        
        self.__fRbkg = 1.0
        self.__fftfKmin = 2.0
        self.__fftfKmax = 17.0
        self.__fftfDk = 1.0
        self.__fftfKweight = 2.0
        
        self.__bProcess = True
        self.__bUseWSGI = _bUseWSGI
        
        self.__edPlugin = None
        

    def preProcess(self):
        """
        Processes the command line, creates the plugins
        """
        EDApplication.preProcess(self)
        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.preProcess")

        # Read command line parameters and check if they are ok
        if not self.__bUseWSGI:
            self.__bProcess = self.readAndProcessCommandLine()

    def process(self):
        """
        Calls the Plugin to be executed
        """
        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.process")
        if (not self.isFailure()) and (self.__bProcess):
            self.__edPlugin = EDFactoryPluginStatic.loadPlugin(self.getPluginName())
            if(self.__edPlugin is not None):
                self.__edPlugin.setBaseDirectory(self.getFullApplicationWorkingDirectory())
                self.__edPlugin.setBaseName(self.getPluginName())

                self.setPluginInput(self.__edPlugin)

                self.__edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                self.__edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.process: Executing " + self.getPluginName())
                self.__edPlugin.execute()
                self.__edPlugin.synchronize()
            else:
                EDVerbose.error("EDApplicationXAFSBatchProcessing .process : plugin not loaded : %s" % self.getPluginName())
                self.setFailure(True)


    def setPluginInput(self, _edPlugin):
        
        _edPlugin.setDataInput(XSDataInputXAFSDataBatchProcessing())
        
        xsDataInputSpline = XSDataInputSpline()
        if (self.__fRbkg):
            xsDataInputSpline.setRbkg(XSDataFloat(self.__fRbkg))
        _edPlugin.getDataInput().setSplineDataInput(xsDataInputSpline)
        
        xsDataInputFFTF = XSDataInputFFTF()
        if (self.__fftfKmin):
            xsDataInputFFTF.setKmin(XSDataFloat(self.__fftfKmin))
        if (self.__fftfKmax):
            xsDataInputFFTF.setKmax(XSDataFloat(self.__fftfKmax))
        if (self.__fftfDk):
            xsDataInputFFTF.setDk(XSDataFloat(self.__fftfDk))
        if (self.__fftfKweight):
            xsDataInputFFTF.setKweight(XSDataFloat(self.__fftfKweight))
        _edPlugin.getDataInput().setFftfDataInput(xsDataInputFFTF)
        
        if (not self.__strDatasetFileNames is None):
            try:
                if (self.__strNxsEnergy and self.__strNxsLnI0It):
                    _edPlugin.readXAFSNexusFiles(self.__strDatasetFileNames, self.__strNxsEnergy, self.__strNxsLnI0It, self.__strNxsScanIndex)
            except Exception:
                errorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % ("EDApplicationXAFSBatchProcessing.setPluginInput", self.__strDatasetFileNames)
                EDVerbose.error(errorMessage)
                raise RuntimeError, errorMessage
            
    def setDatasetFileNames(self, _strDatasetFileNames):
        self.__strDatasetFileNames = _strDatasetFileNames


    def getXAFSPlugin(self):
        return self.__edPlugin


    def readAndProcessCommandLine(self):
        """
        Reads and processes the command line
        """
        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.readAndProcessCommandLine")
        bCommandLineIsOk = False
        # Check if m_strDATASET_PARAM_LABEL is given:
        _dataPattern = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.DATASET_PARAM_LABEL)
        self.__strDatasetFileNames = [os.path.abspath(tmp) for tmp in filter(lambda tmp: os.path.isfile(tmp), glob.glob(_dataPattern))]
        if (self.__strDatasetFileNames is not None):
            for _tmpName in self.__strDatasetFileNames:
                EDVerbose.screen("Reading input data from : %s" % _tmpName)
            bCommandLineIsOk = True
        else:
            self.usage()
            return bCommandLineIsOk
                
        strNxsEnergy = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSENERGY_PARAM_LABEL)
        if (strNxsEnergy is not None):
            self.__strNxsEnergy = strNxsEnergy
            EDVerbose.screen("Path to energy values in Nexus file                         : %s " % (self.__strNxsEnergy))
            
        strNxsI0 = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSI0_PARAM_LABEL)
        if (strNxsI0 is not None):
            self.__strNxsI0 = strNxsI0
            EDVerbose.screen("Path to I0 values in Nexus file                         : %s " % (self.__strNxsI0))
            
        strNxsIref = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSIREF_PARAM_LABEL)
        if (strNxsIref is not None):
            self.__strNxsIref = strNxsIref
            EDVerbose.screen("Path to Iref values in Nexus file                         : %s " % (self.__strNxsIref))
            
        strNxsIt = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSIT_PARAM_LABEL)
        if (strNxsIt is not None):
            self.__strNxsIt = strNxsIt
            EDVerbose.screen("Path to It values in Nexus file                         : %s " % (self.__strNxsIt))
            
        strNxsTime = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSTIME_PARAM_LABEL)
        if (strNxsTime is not None):
            self.__strNxsTime = strNxsTime
            EDVerbose.screen("Path to time values in Nexus file                         : %s " % (self.__strNxsTime))
            
        strNxsLnI0Iref = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSLNI0IREF_PARAM_LABEL)
        if (strNxsLnI0Iref is not None):
            self.__strNxsLnI0Iref = strNxsLnI0Iref
            EDVerbose.screen("Path to ln(I0/Iref) values in Nexus file                         : %s " % (self.__strNxsLnI0Iref))
            
        strNxsLnI0It = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.NXSLNI0IT_PARAM_LABEL)
        if (strNxsLnI0It is not None):
            self.__strNxsLnI0It = strNxsLnI0It
            EDVerbose.screen("Path to ln(I0/It) values in Nexus file                         : %s " % (self.__strNxsLnI0It))

        strRbkg = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.RBKG_PARAM_LABEL)
        if (strRbkg is not None):
            self.__fRbkg = float(strRbkg)
            EDVerbose.screen("rbkg setting                          : %2.3f " % (self.__fRbkg))
        else:
            EDVerbose.screen("Using default rbkg setting                          : %2.3f " % (self.__fRbkg))
            
        strKmin = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.KMIN_PARAM_LABEL)
        if (strKmin is not None):
            self.__fftfKmin = float(strKmin)
            EDVerbose.screen("kmin setting                          : %2.3f " % (self.__fftfKmin))
        else:
            EDVerbose.screen("Using default kmin setting                          : %2.3f " % (self.__fftfKmin))
            
        strKmax = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.KMAX_PARAM_LABEL)
        if (strKmax is not None):
            self.__fftfKmax = float(strKmax)
            EDVerbose.screen("kmax setting                          : %2.3f " % (self.__fftfKmax))
        else:
            EDVerbose.screen("Using default kmax setting                          : %2.3f " % (self.__fftfKmax))
            
        strDk = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.DK_PARAM_LABEL)
        if (strDk is not None):
            self.__fftfDk = float(strDk)
            EDVerbose.screen("dk setting                          : %2.3f " % (self.__fftfDk))
        else:
            EDVerbose.screen("Using default dk setting                          : %2.3f " % (self.__fftfDk))
            
        strKweight = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.KWEIGHT_PARAM_LABEL)
        if (strKweight is not None):
            self.__fftfKweight = float(strKweight)
            EDVerbose.screen("kweight setting                          : %2.3f " % (self.__fftfKweight))
        else:
            EDVerbose.screen("Using default kweight setting                          : %2.3f " % (self.__fftfKweight))
            
        return bCommandLineIsOk


#    def processCommandLinePluginName(self):
#        """
#        """
#        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.processCommandLinePluginName")
#        if (not self.getEdCommandLine().existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
#            EDVerbose.DEBUG("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
#        else:
#            self.__strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
#            EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self.__strPluginName))
#
#
    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.processCommandLineInputFilePath")
        if (not self.getEdCommandLine().existCommand(EDApplicationXAFSBatchProcessing.DATASET_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found!" % EDApplicationXAFSBatchProcessing.DATASET_PARAM_LABEL)
        else:
            self.__strDataInputFilePath = self.getCommandLineArgument(EDApplicationXAFSBatchProcessing.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.processCommandLineInputFilePath : %s = %s" % (EDApplicationXAFSBatchProcessing.DATASET_PARAM_LABEL, self.__strDataInputFilePath))


    def usage(self):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("----- ")
        EDVerbose.screen("")
        EDVerbose.screen("   runXAFSDataProcession --data xafs_input_NeXus_file")
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : starting value in rMax search interval [10.0 (default)]" % (EDApplicationXAFSBatchProcessing.RMAXSTART_PARAM_LABEL))
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : final value in rMax search interval [200.0 (default)]" % (EDApplicationXAFSBatchProcessing.RMAXSTOP_PARAM_LABEL))
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : number of rMax search interval subdivisions [10 (default)]" % (EDApplicationXAFSBatchProcessing.RMAXINTERVALS_PARAM_LABEL))
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : maximal variation of fit quality in final rMax search interval [0.1 (default)]" % (EDApplicationXAFSBatchProcessing.RMAXABSTOL_PARAM_LABEL))
        #EDVerbose.screen("")
        #EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        #EDVerbose.screen("")
        #EDVerbose.screen(" Additional options available:")
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : DEBUG log traces" % (EDApplicationXAFSBatchProcessing.DEBUG_PARAM_LABEL))
        #EDVerbose.screen("")
        #EDVerbose.screen("%35s : Executable version info" % (EDApplicationXAFSBatchProcessing.VERSION_PARAM_LABEL))
        EDVerbose.screen("")


    def doFailureActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDApplication.doFailureActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.doFailureActionPlugin")
        EDVerbose.screen("Execution of " + _edPlugin.getPluginName() + " failed.")
        EDVerbose.screen("Please inspect the log file for further information.")


    def doSuccessActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDApplication.doSuccessActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationXAFSBatchProcessing.doSuccessActionPlugin")

        if (_edPlugin.getListOfErrorMessages() != []):
            self.doFailureActionPlugin(_edPlugin)
        elif (_edPlugin.getListOfWarningMessages() != []):
            EDVerbose.screen("XAFS data processing successful with warning messages, please check the log file.")
        else:
            EDVerbose.screen("XAFS data processing successful!")
