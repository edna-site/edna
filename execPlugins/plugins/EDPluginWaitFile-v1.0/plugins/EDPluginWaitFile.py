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

from __future__ import with_statement
__authors__ = ["Jerome Kieffer", "Olof Svensson"]
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "2012-09-24"
__status__ = "production"

import time, os
from EDPlugin           import EDPlugin
from EDConfiguration    import EDConfiguration
from EDApplication      import EDApplication
from XSDataWaitFilev1_0 import XSDataInputWaitFile, XSDataResultWaitFile
from XSDataCommon       import XSDataString, XSDataInteger, XSDataFile, XSPluginItem, XSDataBoolean
from EDThreading        import Semaphore

class EDPluginWaitFile(EDPlugin):
    """
    Plugins that waits for a file to be written and reach a certain size
    """
    #offers some extra seconds between officiel timeout and allows the plugin to finish gracefully.
    EXTRA_TIME = 5
    DELTA_TIME = 1
    DEFAULT_TIMEOUT = 2
    config_timeout = None
    writeXmlInOut = True
    writeDataXMLOutput = True
    writeDataXMLInput = True
    sem = Semaphore()

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

    def configure(self):
        """

        Configuration step of the plugin: mainly extend the timeout by 5 seconds to let the plugin finish.

        """
        if self.__class__.config_timeout is None:
            with self.__class__.sem:
                if self.__class__.config_timeout is None:
                    iTimeOut = self.config.get(EDPlugin.CONF_TIME_OUT, None)
                    if iTimeOut is not None:
                        self.DEBUG("EDPlugin.configure: Setting time out to %d s from plugin configuration." % iTimeOut)
                        self.__class__.config_timeout = iTimeOut
                    else:
                        self.__class__.config_timeout = self.getDefaultTimeOut()
                    self.__class__.writeXmlInOut = bool(self.config.get(self.CONF_WRITE_XML_INPUT_OUTPUT, True))
                    self.__class__.writeDataXMLOutput = bool(self.config.get(self.CONF_WRITE_XML_OUTPUT, True))
                    self.__class__.writeDataXMLInput = bool(self.config.get(self.CONF_WRITE_XML_INPUT, True))
        self.__timeout = self.__class__.config_timeout
        self.setTimeOut(self.__class__.config_timeout + EDPluginWaitFile.EXTRA_TIME)
        self.setWriteXMLInputOutput(self.writeXmlInOut)
        self.setWriteXMLOutput(self.writeDataXMLOutput)
        self.setWriteXMLInput(self.writeDataXMLInput)

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


