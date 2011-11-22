# coding: utf8
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
#
#    Contributing author:    Olof Svensson
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

__authors__ = ["Jerome Kieffer", "Olof Svensson"]
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "2011-05-09"
__status__ = "production"

import time, os
from EDPlugin           import EDPlugin
from EDConfiguration    import EDConfiguration
from EDApplication      import EDApplication
from XSDataWaitFilev1_0 import XSDataInputWaitFile, XSDataResultWaitFile
from XSDataCommon       import XSDataString, XSDataInteger, XSDataFile, XSPluginItem, XSDataBoolean


class EDPluginWaitFile(EDPlugin):
    """
    Plugins that waits for a file to be written and reach a certain size
    """
    #offers some extra seconds between officiel timeout and allows the plugin to finish gracefully.
    EXTRA_TIME = 5
    DELTA_TIME = 1
    DEFAULT_TIMEOUT = 2

    def __init__(self):
        """
        """
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataInputWaitFile)
        self.__filename = None
        self.__exists = None
        self.__filesize = None
        self.__expectedSize = None
        self.__timeout = self.DEFAULT_TIMEOUT



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginWaitFile.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedFile(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedSize(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginWaitFile.preProcess")
        self.__filename = self.getDataInput().getExpectedFile().getPath().getValue()
        self.__expectedSize = self.getDataInput().getExpectedSize().getValue()
        if self.getDataInput().getTimeOut():
            self.__timeout = self.getDataInput().getTimeOut().getValue()
            self.setTimeOut(self.getDataInput().getTimeOut().getValue() + EDPluginWaitFile.EXTRA_TIME)


    def process(self, _edObject=None):
        EDPlugin.process(self)
        self.DEBUG("EDPluginWaitFile.process")
        self.DEBUG("EDPluginWaitFile Plugin TimeOut is set to: %s, internal TimeOut is %s" % (self.getTimeOut(), self.__timeout))
        self.setTimeInit()
        dirname = os.path.dirname(self.__filename)
        while self.getRunTime() < self.__timeout:
            if os.path.isdir(dirname):
                fd = os.open(dirname, os.O_RDONLY)
                os.fstat(fd)
                os.close(fd)
                if os.path.exists(self.__filename):
                    self.__filesize = os.path.getsize(self.__filename)
                    if self.__filesize >= self.__expectedSize:
                        break
            time.sleep(EDPluginWaitFile.DELTA_TIME)
        self.setTimeEnd()


    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginWaitFile.postProcess: Waited for %.3f s" % self.getRunTime())
        xsDataResult = XSDataResultWaitFile()
        if os.path.exists(self.__filename):
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.__filename))
            xsDataResult.setActualFile(xsDataFile)
            xsDataResult.setActualSize(XSDataInteger(os.path.getsize(self.__filename)))
        xsDataResult.setTimedOut(XSDataBoolean(self.getRunTime() >= self.__timeout))
        # Create some output data
        self.setDataOutput(xsDataResult)


    def configure(self):
        """
        
        Configuration step of the plugin: mainly extend the timeout by 5 seconds to let the plugin finish. 

        """
        self.DEBUG("EDPluginWaitFile.configure : %s" % self.getClassName())
        xsPluginItem = self.getConfiguration()
        if xsPluginItem is None:
            xsPluginItem = EDApplication.getApplicationPluginConfiguration(self.getPluginName())
            if (xsPluginItem is None):
                # No application wide configuration file found! Try to find a project specific config file:
                xsPluginItem = EDApplication.getProjectPluginConfiguration(self.getPluginName())

            if (xsPluginItem is None):
                self.DEBUG("EDPlugin.execute: No plugin configuration found for " + self.getPluginName())
                xsPluginItem = XSPluginItem()
            else:
                self.setConfiguration(xsPluginItem)
        # Try to get time out from plugin configuration
        iTimeOut = EDConfiguration.getIntegerParamValue(xsPluginItem, EDPlugin.CONF_TIME_OUT)
        if iTimeOut is not None:
            self.DEBUG("EDPlugin.configure: Setting time out to %d s from plugin configuration." % iTimeOut)
            self.__timeout = iTimeOut
            self.setTimeOut(iTimeOut + EDPluginWaitFile.EXTRA_TIME)




