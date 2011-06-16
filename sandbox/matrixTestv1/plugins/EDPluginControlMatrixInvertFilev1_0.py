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

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl

from XSDataMatrixv1 import XSDataInputMatrixInvertFile
from XSDataMatrixv1 import XSDataResultMatrixInvertFile
from XSDataMatrixv1 import XSDataInputMatrixInvert
#from XSDataMatrixv1 import XSDataResultMatrixInvert
from XSDataMatrixv1 import XSDataInputReadMatrix
#from XSDataMatrixv1 import XSDataResultReadMatrix
from XSDataMatrixv1 import XSDataInputWriteMatrix
#from XSDataMatrixv1 import XSDataResultWriteMatrix
#from XSDataCommon import XSDataArray


class EDPluginControlMatrixInvertFilev1_0(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMatrixInvertFile)
        self.__strControlledPluginReader = "EDPluginExecMatrixReadv1_0"
        self.__strControlledPluginInverter = "EDPluginExecMatrixInvertv1_0"
        self.__strControlledPluginWriter = "EDPluginExecMatrixWritev1_0"
        self.__edPluginExecRead = None
        self.__edPluginExecInvert = None
        self.__edPluginExecWrite = None

        self.xsDataResult = XSDataResultMatrixInvertFile()



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputMatrixFile(), "No Input File")
        self.checkMandatoryParameters(self.getDataInput().getOutputMatrixFile(), "No Output file")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginExecRead = self.loadPlugin(self.__strControlledPluginReader)
        self.__edPluginExecInvert = self.loadPlugin(self.__strControlledPluginInverter)
        self.__edPluginExecWrite = self.loadPlugin(self.__strControlledPluginWriter)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.process")
        xsdin = XSDataInputReadMatrix()
        xsdin.setInputMatrixFile(self.getDataInput().getInputMatrixFile())
        self.__edPluginExecRead.setDataInput(xsdin)
        self.__edPluginExecRead.connectSUCCESS(self.doSuccessExecRead)
        self.__edPluginExecRead.connectFAILURE(self.doFailureExecRead)
        self.__edPluginExecRead.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.postProcess")
        # Create some output data
        self.setDataOutput(self.xsDataResult)


    def doSuccessExecRead(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doSuccessExecRead")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doSuccessExecRead")
        xsdmat = _edPlugin.getDataOutput().getOutputMatrix()
        xsdin = XSDataInputMatrixInvert()
        xsdin.setInputMatrix(xsdmat)
        self.__edPluginExecInvert.setDataInput(xsdin)
        self.__edPluginExecInvert.connectSUCCESS(self.doSuccessExecInvert)
        self.__edPluginExecInvert.connectFAILURE(self.doFailureExecInvert)
        self.__edPluginExecInvert.executeSynchronous()

    def doFailureExecRead(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doFailureExecRead")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doFailureExecRead")


    def doSuccessExecInvert(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doSuccessExecInvert")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doSuccessExecInvert")
        xsdmat = _edPlugin.getDataOutput().getOutputMatrix()
        xsdin = XSDataInputWriteMatrix()
        xsdin.setInputMatrix(xsdmat)
        xsdin.setOutputMatrixFile(self.getDataInput().getOutputMatrixFile())
        self.__edPluginExecWrite.setDataInput(xsdin)
        self.__edPluginExecWrite.connectSUCCESS(self.doSuccessExecWrite)
        self.__edPluginExecWrite.connectFAILURE(self.doFailureExecWrite)
        self.__edPluginExecWrite.executeSynchronous()


    def doFailureExecInvert(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doFailureExecInvert")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doFailureExecInvert")


    def doSuccessExecWrite(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doSuccessExecWrite")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doSuccessExecWrite")
        xsdout = _edPlugin.getDataOutput().getOutputMatrixFile()
        self.xsDataResult.setOutputMatrixFile(xsdout)


    def doFailureExecWrite(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlMatrixInvertFilev1_0.doFailureExecWrite")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlMatrixInvertFilev1_0.doFailureExecWrite")
