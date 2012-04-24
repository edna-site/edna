# coding: utf8
#
#    Project: Python Fast Azimuthal Integration
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#
#    Principal author:       Jérôme Kieffer <jerome.kieffer@esrf.fr>
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
__author__ = "Jérôme Kieffer <jerome.kieffer@esrf.fr>"
__license__ = "GPLv3+"
__copyright__ = "2012 European Synchrotron Radiation Facility"

from EDPluginExec import EDPluginExec
from EDVerbose import EDVerbose
from EDThreading import Semaphore
from XSDataPyFAIv1_0 import XSDataInputPyFAI
from XSDataPyFAIv1_0 import XSDataResultPyFAI

try:
    import pyFAI
except ImportError:
    EDVerbose.ERROR("Failed to import PyFAI: download and install it from \
        https://forge.epn-campus.eu/projects/azimuthal/files")


class EDPluginExecPyFAIv1_0(EDPluginExec):
    """
    This is the basic plugin of PyFAI for azimuthal integration
    """

    _dictGeo = {}
    _sem = Semaphore()
    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputPyFAI)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecPyFAIv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.preProcess")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.process")


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPyFAI()
        self.setDataOutput(xsDataResult)

