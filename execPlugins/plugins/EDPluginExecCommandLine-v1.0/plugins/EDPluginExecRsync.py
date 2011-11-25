# coding: utf8
#
#    Project: templatev1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011 ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jérôme.Kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2011 ESRF, Grenoble"
__date__ = "2011-11-25"
__status__ = "Production"

import os
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataExecCommandLine      import XSDataInputRsync, XSDataResultRsync
from XSDataCommon import XSDataString, XSDataFile

class EDPluginExecRsync(EDPluginExecProcessScript):
    """
    Execution plugin that does the synchronization of two directories using rsync
    """

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputRsync)
        self.strSource = None
        self.strDestination = None
        self.strOption = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecRsync.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.source, "No source provided")
        self.checkMandatoryParameters(self.dataInput.destination, "No source provided")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecRsync.preProcess")
        self.strSource = self.dataInput.source.path.value
        self.strDestination = self.dataInput.destination.path.value
        if self.dataInput.options is not None:
            self.strOption = self.dataInput.options.value
        self.generateCommandLine()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecRsync.postProcess")
        # Create some output data
        xsDataResult = XSDataResultRsync(log=XSDataString(""))

        self.setDataOutput(xsDataResult)


    def generateCommandLine(self):
        self.DEBUG("EDPluginExecRsync.generateCommandLine")
        if self.strOption is not None:
            self.setScriptCommandline("%s %s %s" % (self.strOption, self.strSource, self.strDestination))
        else:
            self.setScriptCommandline("%s %s" % (self.strSource, self.strDestination))
