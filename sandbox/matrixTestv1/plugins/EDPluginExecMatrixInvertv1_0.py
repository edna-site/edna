#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer, jerome.kieffer@esrf.fr
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

__author__ = "Jerome Kieffer, jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"


import os, sys
from EDVerbose      import EDVerbose
from EDPluginExec   import EDPluginExec
from XSDataMatrixv1 import XSDataInputMatrixInvert
from XSDataMatrixv1 import XSDataResultMatrixInvert
from EDUtilsArray   import EDUtilsArray

from EDFactoryPluginStatic              import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")

import numpy
import numpy.linalg


class EDPluginExecMatrixInvertv1_0(EDPluginExec):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMatrixInvert)
        self.xsdMatIn = None
        self.matIn = None
        self.matOut = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecMatrixInvertv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputMatrix(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecMatrixInvertv1_0.preProcess")
        self.xsdMatIn = self.getDataInput().getInputMatrix()
        self.matIn = EDUtilsArray.xsDataToArray(self.xsdMatIn)

    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecMatrixInvertv1_0.process")
        self.matOut = numpy.linalg.inv(self.matIn)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecMatrixInvertv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMatrixInvert()
        xsdMatOut = EDUtilsArray.arrayToXSData(self.matOut, _bIncludeMd5sum=False)
        xsDataResult.setOutputMatrix(xsdMatOut)
        self.setDataOutput(xsDataResult)

