#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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


import os
from EDVerbose import EDVerbose
from EDMessage import EDMessage
from EDApplication import EDApplication
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

EDFactoryPluginStatic.loadModule("EDApplicationMXv1Characterisation")
from EDApplicationMXv1Characterisation import EDApplicationMXv1Characterisation

from XSDataMXv2 import XSDataCollection as XSDataCollection_v2

class EDApplicationMXv2Characterisation(EDApplicationMXv1Characterisation):

    APPLICATION_NAME = "EDApplicationMXv2Characterisation"
    APPLICATION_VERSION = "2.0.0"
    MXV2_DATACOLLECTION_FILE_LABEL = "--mxv2DataCollection"
    TEMPLATE_MXV2_PARAM_LABEL = "--generateTemplateMXv2"


    def __init__(self, _strPluginName=None, _strConfigurationFileName=None):
        EDApplicationMXv1Characterisation.__init__(self, _strPluginName, _strConfigurationFileName)
        self.__strGeneratedTemplateFileMXv2 = None
        self.__strDataCollectionMXv2File = None
        self.__bTemplateModeMXv2 = None


#    def process(self):
#        """
#        Calls the Plugin to be executed
#        """
#        EDApplicationMXv1Characterisation.process()
#        EDVerbose.DEBUG("EDApplicationMXv1Characterisation.process")


    def setPluginInput(self, _edPlugin):
        EDApplicationMXv1Characterisation.setPluginInput(self, _edPlugin)
        if (not self.__strGeneratedTemplateFileMXv2 is None):
            _edPlugin.setDataInput(XSDataString(self.__strGeneratedTemplateFileMXv2), "generatedTemplateFileMXv2")
        if self.__bTemplateModeMXv2:
            # Delete the existing entry if any
            if _edPlugin.hasDataInput("templateMode"):
                _edPlugin.setDataInput(None, "templateMode")
            _edPlugin.setDataInput(XSDataBoolean(self.__bTemplateModeMXv2), "templateMode")
        if self.__strDataCollectionMXv2File:
            xsDataCollectionMXv2 = XSDataCollection_v2.parseFile(self.__strDataCollectionMXv2File)
            _edPlugin.setDataInput(xsDataCollectionMXv2, "mxv2DataCollection")


    def processCommandLineItems(self, _strCommandLineItem, _bFoundImageToken):
        bFoundImageToken = EDApplicationMXv1Characterisation.processCommandLineItems(self, _strCommandLineItem, _bFoundImageToken)
        if _strCommandLineItem == EDApplicationMXv2Characterisation.TEMPLATE_MXV2_PARAM_LABEL:
            self.__strGeneratedTemplateFileMXv2 = self.getCommandLineArgument(EDApplicationMXv2Characterisation.TEMPLATE_MXV2_PARAM_LABEL)
            if (self.__strGeneratedTemplateFileMXv2 == None):
                strErrorMessage = EDMessage.ERROR_MANDATORY_PARAM_MISSING_02 % ("EDApplicationMXv2Characterisation.processCommandLineItems", "No argument for command line %s key word found!" % \
                                                                              EDApplicationMXv2Characterisation.TEMPLATE_MXV2_PARAM_LABEL)
                EDVerbose.error(strErrorMessage)
            else:
                if (not os.path.isabs(self.__strGeneratedTemplateFileMXv2)):
                    self.__strGeneratedTemplateFileMXv2 = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.__strGeneratedTemplateFileMXv2))
                self.__bTemplateModeMXv2 = True
        if _strCommandLineItem == EDApplicationMXv2Characterisation.MXV2_DATACOLLECTION_FILE_LABEL:
            self.__strDataCollectionMXv2File = self.getCommandLineArgument(EDApplicationMXv2Characterisation.MXV2_DATACOLLECTION_FILE_LABEL)
            if (self.__strDataCollectionMXv2File == None):
                strErrorMessage = EDMessage.ERROR_MANDATORY_PARAM_MISSING_02 % ("EDApplicationMXv2Characterisation.processCommandLineItems", "No argument for command line %s key word found!" % \
                                                                              EDApplicationMXv2Characterisation.MXV2_DATACOLLECTION_FILE_LABEL)
                EDVerbose.error(strErrorMessage)
            else:
                if (not os.path.isabs(self.__strDataCollectionMXv2File)):
                    self.__strDataCollectionMXv2File = os.path.abspath(os.path.join(self.getCurrentWorkingDirectory(), self.__strDataCollectionMXv2File))
        return bFoundImageToken



    def usage(self):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("----- ")
        EDVerbose.screen("")
        EDVerbose.screen(" Either use:")
        EDVerbose.screen("")
        EDVerbose.screen(" - the full/advanced XML input:")
        EDVerbose.screen("")
        EDVerbose.screen("   edna-mxv2-characterisation --data path_to_xsDataInputCharacterisation_xml_file")
        EDVerbose.screen("")
        EDVerbose.screen(" - or use the --image keyword (note that all these keywords are ignored if the --data option is used):")
        EDVerbose.screen("")
        EDVerbose.screen("   edna-mxv2-characterisation --image image1 [image2 image3 ...]")
        EDVerbose.screen("")
        EDVerbose.screen(" In the case of using the --image command line keyword the following arguments are optional:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : MXv2 data collection input file" % (EDApplicationMXv2Characterisation.MXV2_DATACOLLECTION_FILE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : BEST complexity [none (default), min or full]" % (EDApplicationMXv2Characterisation.COMPLEXITY_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam flux [photon/s]" % (EDApplicationMXv2Characterisation.FLUX_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam size [mm] (beam assumed to be square)" % (EDApplicationMXv2Characterisation.BEAM_SIZE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam position X [mm] (MOSFLM ordering)" % (EDApplicationMXv2Characterisation.BEAM_POS_X_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Beam position Y [mm] (MOSFLM ordering)" % (EDApplicationMXv2Characterisation.BEAM_POS_Y_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Max exposure time per data collection [s]" % (EDApplicationMXv2Characterisation.MAX_EXPOSURE_TIME_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Min exposure time per image [s]" % (EDApplicationMXv2Characterisation.MIN_EXPOSURE_TIME_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Forced space group for indexing" % (EDApplicationMXv2Characterisation.FORCED_SPACE_GROUP_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Anomalous data" % (EDApplicationMXv2Characterisation.ANOMALOUS_DATA_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Optional command to BEST, the currently only supported command is: -DamPar" % (EDApplicationMXv2Characterisation.STRATEGY_OPTION_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" Additional options available:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an (MXv1) xml template input file for edna" % (EDApplicationMXv2Characterisation.TEMPLATE_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an MXv2 xml template input file for edna" % (EDApplicationMXv2Characterisation.TEMPLATE_MXV2_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Generates an xml file containing the characterisation results" % (EDApplicationMXv2Characterisation.RESULTS_FILE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (EDApplicationMXv2Characterisation.DEBUG_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (EDApplicationMXv2Characterisation.VERSION_PARAM_LABEL))
        EDVerbose.screen("")


    def doSuccessActionPlugin(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        """
        EDApplication.doSuccessActionPlugin(self, _edPlugin)

        EDVerbose.DEBUG("EDApplicationMXv2Characterisation.doSuccessActionPlugin")

        if (_edPlugin.getListOfErrorMessages() != []):
            self.doFailureActionPlugin(_edPlugin)
        elif (_edPlugin.getListOfWarningMessages() != []):
            EDVerbose.screen("MXv2 characterisation successful with warning messages, please check the log file.")
        else:
            EDVerbose.screen("MXv2 characterisation successful!")

