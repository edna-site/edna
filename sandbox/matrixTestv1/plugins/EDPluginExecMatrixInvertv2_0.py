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
from EDPluginExec           import EDPluginExec
from XSDataMatrixv1         import XSDataInputMatrixInvertv2, XSDataResultMatrixInvertv2, XSDataImageExt
from EDUtilsArray           import EDUtilsArray
from EDShare                import EDShare
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPlatform        import EDUtilsPlatform

architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
import numpy.linalg


class EDPluginExecMatrixInvertv2_0(EDPluginExec):
    """
    Testing matix inversion from a shared array (via HDF5)
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMatrixInvertv2)
        self.xsdMatIn = None
        self.matIn = None
        self.matOut = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMatrixInvertv2_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.inputMatrix, "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecMatrixInvertv2_0.preProcess")
        self.xsdMatIn = self.dataInput.inputMatrix
        if self.xsdMatIn.path is not None:
            self.matIn = fabio.open(self.xsdMatIn.path.value).data
        elif self.xsdMatIn.shared is not None:
            self.matIn = EDShare[self.xsdMatIn.shared.value]
        elif self.xsdMatIn.array is not None:
            self.matIn = EDUtilsArray.xsDataToArray(self.xsdMatIn.array)
        else:
            self.ERROR("No valid input array provided")
        if self.matIn is None:
            self.ERROR("Input array is None")
            self.setFailure()
#        else:
#            print self.xsdMatIn

    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecMatrixInvertv2_0.process")
        self.matOut = numpy.linalg.inv(self.matIn)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecMatrixInvertv2_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMatrixInvertv2()
        xsd = XSDataImageExt()
        if self.dataInput.outputMatrix is not None:
            if self.dataInput.outputMatrix.path is not None:
                fabio.edfimage.edfimage(data=self.matOut).write(self.dataInput.outputMatrix.path.value)
                xsd.path = self.dataInput.outputMatrix.path
            elif self.dataInput.outputMatrix.shared is not None:
                EDShare[self.dataInput.outputMatrix.shared.value] = self.matOut
                xsd.shared = self.dataInput.outputMatrix.shared
        else:
            xsd.array = EDUtilsArray.arrayToXSData(self.matOut, _bIncludeMd5sum=False)
        xsDataResult.setOutputMatrix(xsd)
        self.setDataOutput(xsDataResult)

