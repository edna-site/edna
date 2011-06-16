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
from EDUtilsArray   import EDUtilsArray
from XSDataMatrixv1 import XSDataInputWriteMatrix
from XSDataMatrixv1 import XSDataResultWriteMatrix
from EDFactoryPluginStatic  import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

import numpy
from  fabio.edfimage import edfimage



class EDPluginExecMatrixWritev1_0(EDPluginExec):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputWriteMatrix)
        self.matIn = None
        self.xsdMatIn = None
        self.outputFile = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecMatrixWritev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputMatrix(), "No Input Matrix")
        self.checkMandatoryParameters(self.getDataInput().getOutputMatrixFile(), "No Output File")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecMatrixWritev1_0.preProcess")
        self.outputFile = self.getDataInput().getOutputMatrixFile().getPath().getValue()
        self.xsdMatIn = self.getDataInput().getInputMatrix()
        self.matIn = EDUtilsArray.xsDataToArray(self.xsdMatIn)



    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecMatrixWritev1_0.process")
        f = edfimage(self.matIn, {})
        f.write(self.outputFile, force_type=self.matIn.dtype)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecMatrixWritev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultWriteMatrix()
        xsDataResult.setOutputMatrixFile(self.getDataInput().getOutputMatrixFile())
        self.setDataOutput(xsDataResult)

