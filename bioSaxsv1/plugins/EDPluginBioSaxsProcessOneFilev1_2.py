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
__date__ = "20120824"
__status__ = "development"

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


class EDPluginBioSaxsProcessOneFilev1_2(EDPluginControl):
    """
    Control plugin that does subsequent execution of: 
    * EDPluginBioSaxsNormalizev1_1
    * EDPluginBioSaxsAzimutIntv1_3 #with pyFAI

    """
    __strControlledPluginNormalize = "EDPluginBioSaxsNormalizev1_1"
    __strControlledPluginIntegrate = "EDPluginBioSaxsAzimutIntv1_3"

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsProcessOneFilev1_0)
        self.__edPluginNormalize = None
        self.__edPluginIntegrate = None

        self.rawImageSize = XSDataInteger(1024)
        self.normalizedImage = None
        self.integratedCurve = None
        self.integratedImage = None
        self.lstExecutiveSummary = []
        self.sample = None
        self.experimentSetup = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image provided")
        self.checkMandatoryParameters(self.dataInput.sample, "No sample information provided")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "No experimental setup provided")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.preProcess")
        # Load the execution plugin
        self.__edPluginNormalize = self.loadPlugin(self.__strControlledPluginNormalize)
        self.__edPluginIntegrate = self.loadPlugin(self.__strControlledPluginIntegrate)
        if self.dataInput.rawImageSize is not None:
            self.rawImageSize = self.dataInput.rawImageSize
        self.sample = self.dataInput.sample
        self.experimentSetup = self.dataInput.experimentSetup


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.process")

        self.__edPluginNormalize.connectSUCCESS(self.doSuccessNormalize)
        self.__edPluginNormalize.connectFAILURE(self.doFailureNormalize)
        xsd = XSDataInputBioSaxsNormalizev1_0()
        xsd.rawImage = self.dataInput.rawImage
        xsd.normalizedImage = self.dataInput.normalizedImage
        xsd.rawImageSize = (self.rawImageSize)
        xsd.experimentSetup = self.experimentSetup
        xsd.sample = self.sample
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
        xsd.experimentSetup = self.experimentSetup
        xsd.sample = self.sample
        self.__edPluginIntegrate.dataInput = xsd
        self.__edPluginIntegrate.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.postProcess")
        # Create some output data
        xsDataResult = XSDataResultBioSaxsProcessOneFilev1_0()

        xsDataResult.normalizedImage = self.normalizedImage
        xsDataResult.integratedImage = self.integratedImage
        xsDataResult.integratedCurve = self.integratedCurve
        xsDataResult.sample = self.sample
        xsDataResult.experimentSetup = self.experimentSetup

        xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstExecutiveSummary)))
        self.setDataOutput(xsDataResult)


    def doSuccessNormalize(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.doSuccessNormalize")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_2.doSuccessNormalize")
        xsdOut = _edPlugin.dataOutput
        self.normalizedImage = xsdOut.normalizedImage
        self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)

    def doFailureNormalize(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.doFailureNormalize")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_2.doFailureNormalize")
        try:
            xsdOut = _edPlugin.dataOutput
            self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)
        except Exception:
            pass
        self.setFailure()

    def doSuccessIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.doSuccessIntegrate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_2.doSuccessIntegrate")
        xsdOut = _edPlugin.dataOutput
        self.integratedImage = xsdOut.integratedImage
        self.integratedCurve = xsdOut.integratedCurve
        self.sample = xsdOut.sample
        self.experimentSetup = xsdOut.experimentSetup
        self.lstExecutiveSummary.append(xsdOut.status.executiveSummary.value)


    def doFailureIntegrate(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsProcessOneFilev1_2.doFailureIntegrate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsProcessOneFilev1_2.doFailureIntegrate")
        try:
            xsdOut = _edPlugin.dataOutput
            if xsdOut.experimentSetup:
                self.experimentSetup = xsdOut.experimentSetup
            if xsdOut.sample:
                self.sample = xsdOut.sample
            self.strExecutiveSummary.append(xsdOut.status.executiveSummary.value)
            self.integratedImage = xsdOut.integratedImage
            self.integratedCurve = xsdOut.integratedCurve
        except Exception:
            pass
        self.setFailure()
