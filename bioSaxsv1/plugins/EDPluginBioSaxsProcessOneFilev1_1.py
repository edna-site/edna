# coding: utf8
# 
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20111014"
__status__ = "production"

import os, sys
from EDVerbose              import EDVerbose
from EDPluginControl        import EDPluginControl
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataEdnaSaxs")
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsProcessOneFilev1_0, XSDataResultBioSaxsProcessOneFilev1_0, \
                            XSDataInputBioSaxsNormalizev1_0, XSDataInputBioSaxsAzimutIntv1_0
from XSDataCommon           import XSDataStatus, XSDataString, XSDataFile, XSDataImage, XSDataInteger


class EDPluginBioSaxsProcessOneFilev1_1(EDPluginControl):
    """
    Control plugin that does subsequent execution of: 
    * EDPluginBioSaxsNormalizev1_1
    * EDPluginBioSaxsAzimutIntv1_2 #with better headers.
    """

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsProcessOneFilev1_0)
        self.__strControlledPluginNormalize = "EDPluginBioSaxsNormalizev1_1"
        self.__strControlledPluginIntegrate = "EDPluginBioSaxsAzimutIntv1_2"
        self.__edPluginNormalize = None
        self.__edPluginIntegrate = None

        self.rawImageSize = XSDataInteger(1024)
        self.normalizedImage = None
        self.integratedCurve = None
        self.integratedImage = None
        self.lstExecutiveSummary = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image provided")
        self.checkMandatoryParameters(self.dataInput.sample, "No sample information provided")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "No experimental setup provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.preProcess")
        # Load the execution plugin
        self.__edPluginNormalize = self.loadPlugin(self.__strControlledPluginNormalize)
        self.__edPluginIntegrate = self.loadPlugin(self.__strControlledPluginIntegrate)
        if self.dataInput.rawImageSize is not None:
            self.rawImageSize = self.dataInput.rawImageSize

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.process")
        self.__edPluginNormalize.connectSUCCESS(self.doSuccessNormalize)
        self.__edPluginNormalize.connectFAILURE(self.doFailureNormalize)
        xsd = XSDataInputBioSaxsNormalizev1_0()
        xsd.rawImage = self.dataInput.rawImage
        xsd.normalizedImage = self.dataInput.normalizedImage
        xsd.rawImageSize = (self.rawImageSize)
        xsd.experimentSetup = self.dataInput.experimentSetup
        xsd.sample = self.dataInput.sample
        self.__edPluginNormalize.dataInput = xsd
        self.__edPluginNormalize.executeSynchronous()
        if self.isFailure():
            return

        self.__edPluginIntegrate.connectSUCCESS(self.doSuccessIntegrate)
        self.__edPluginIntegrate.connectFAILURE(self.doFailureIntegrate)
        xsd = XSDataInputBioSaxsAzimutIntv1_0()
        xsd.normalizedImage = self.dataInput.normalizedImage
        xsd.normalizedImageSize = (self.rawImageSize)
        xsd.integratedImage = self.dataInput.integratedImage
        xsd.integratedCurve = self.dataInput.integratedCurve
        xsd.experimentSetup = self.dataInput.experimentSetup
        xsd.sample = self.dataInput.sample
        self.__edPluginIntegrate.dataInput = xsd
        self.__edPluginIntegrate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsProcessOneFilev1_0()

        xsDataResult.normalizedImage = self.normalizedImage
        xsDataResult.integratedImage = self.integratedImage
        xsDataResult.integratedCurve = self.integratedCurve
        xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstExecutiveSummary)))
        self.setDataOutput(xsDataResult)


    def doSuccessNormalize(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.doSuccessNormalize")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_1.doSuccessNormalize")
        xsdOut = _edPlugin.dataOutput
        self.normalizedImage = xsdOut.normalizedImage
        self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)

    def doFailureNormalize(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.doFailureNormalize")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_1.doFailureNormalize")
        try:
            xsdOut = _edPlugin.dataOutput
            self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)
        except Exception:
            pass
        self.setFailure()

    def doSuccessIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.doSuccessIntegrate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_1.doSuccessIntegrate")
        xsdOut = _edPlugin.dataOutput
        self.integratedImage = xsdOut.integratedImage
        self.integratedCurve = xsdOut.integratedCurve
        self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)


    def doFailureIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_1.doFailureIntegrate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_1.doFailureIntegrate")
        try:
            xsdOut = _edPlugin.dataOutput
            self.strExecutiveSummary.append(xsdOut.status.executiveSummary.value)
            self.integratedImage = xsdOut.integratedImage
            self.integratedCurve = xsdOut.integratedCurve
        except Exception:
            pass
        self.setFailure()
