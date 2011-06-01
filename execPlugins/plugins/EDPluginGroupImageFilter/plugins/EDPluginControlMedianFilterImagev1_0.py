#
# coding: utf8
#
#    Project: Image Filter
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF"

import os
from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import  EDFactoryPluginStatic
from XSDataCommon import XSDataImage, XSDataString, XSDataBoolean
from XSDataImageFilter import XSDataInputMedianFilterImage, XSDataInputMedianFilter
from XSDataImageFilter import XSDataResultMedianFilterImage
EDFactoryPluginStatic.loadModule("XSDataAccumulatorv1_0")
from XSDataAccumulatorv1_0 import XSDataQuery, XSDataInputAccumulator

class EDPluginControlMedianFilterImagev1_0(EDPluginControl):
    """
    Apply a median Filter from frames -with/2 to frame -with/2, pixel by pixel.    
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMedianFilterImage)
        self.__strControlledPluginAccumulator = "EDPluginAccumulatorv1_0"
        self.__strControlledPluginMedian = "EDPluginExecMedianFilterv1_0"
        self.__edPluginExecAccumulator = None
        self.__edPluginExecMedian = None
        self.query = XSDataQuery()
        self.xsdMedian = None
        self.filename = None
        self.outputImage = None
        self.width = None
        self.xsdOut = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImage(), "No Input Image")
        self.checkMandatoryParameters(self.getDataInput().getFilterWidth(), "No Median Filter Width provided")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.preProcess")
        # Load the execution plugin
        self.__edPluginExecAccumulator = self.loadPlugin(self.__strControlledPluginAccumulator)
        self.image = os.path.abspath(self.getDataInput().getInputImage().getPath().getValue())
        self.width = self.getDataInput().getFilterWidth().getValue()
        if self.getDataInput().getMedianFilteredImage() is not None:
            self.outputImage = os.path.abspath(self.getDataInput().getMedianFilteredImage().getPath().getValue())
        xsdAcc = XSDataInputAccumulator()
        xsdAcc.setQuery([self.prepareQuery(self.image, self.width)])
        xsdAcc.setItem([XSDataString(self.image)])
        self.__edPluginExecAccumulator.setDataInput(xsdAcc)

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.process")
        self.__edPluginExecAccumulator.connectSUCCESS(self.doSuccessExecAccumulator)
        self.__edPluginExecAccumulator.connectFAILURE(self.doFailureExecAccumulator)
        self.__edPluginExecAccumulator.executeSynchronous()

        if self.xsdMedian:
            self.__edPluginExecMedian = self.loadPlugin(self.__strControlledPluginMedian)
            self.__edPluginExecMedian.setDataInput(self.xsdMedian)
            self.__edPluginExecMedian.connectSUCCESS(self.doSuccessExecMedian)
            self.__edPluginExecMedian.connectFAILURE(self.doFailureExecMedian)
            self.__edPluginExecMedian.executeSynchronous()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMedianFilterImage()
        if self.xsdOut is not None:
            if self.xsdOut.getOutputImage() is not None:
                xsDataResult.setMedianFilteredImage(self.xsdOut.getOutputImage())
            else:
                xsDataResult.setMedianFilteredArray(self.xsdOut.getOutputArray())
        self.setDataOutput(xsDataResult)


    def doSuccessExecAccumulator(self, _edPlugin=None):
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.doSuccessExecAccumulator")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlMedianFilterImagev1_0.doSuccessExecAccumulator")
        xdOut = _edPlugin.getDataOutput()
        if (xdOut is not None) and (xdOut.getQuery() != []):
            query = xdOut.getQuery()[0]
            self.xsdMedian = XSDataInputMedianFilter()
            self.xsdMedian.setInputImages([XSDataImage(i) for i in query.getItem() ])
            if self.outputImage is not None:
                self.xsdMedian.setOutputImage(XSDataImage(XSDataString(self.outputImage)))

    def doFailureExecAccumulator(self, _edPlugin=None):
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.doFailureExecAccumulator")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlMedianFilterImagev1_0.doFailureExecAccumulator")
        self.setFailure()

    def doSuccessExecMedian(self, _edPlugin=None):
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.doSuccessExecMedian")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlMedianFilterImagev1_0.doSuccessExecMedian")
        self.xsdOut = _edPlugin.getDataOutput()


    def doFailureExecMedian(self, _edPlugin=None):
        self.DEBUG("EDPluginControlMedianFilterImagev1_0.doFailureExecMedian")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlMedianFilterImagev1_0.doFailureExecMedian")
        self.setFailure()

    @classmethod
    def prepareQuery(cls, filename, width):
        """
        prepare the query to be submitted
        @return: query
        @rtype: XSDataQuery 
        """
        query = XSDataQuery()
        query.setRemoveItems(XSDataBoolean(0))

        dirname, basename = os.path.split(filename)
        prefix, ext = os.path.splitext(basename)
        suffix = ext
        bStarted = False
        strNum = ""
        for i, c in enumerate(prefix[-1::-1]):
            if bStarted and not c.isdigit():
                prefix = prefix[:-i]
                break
            if c.isdigit():
                bStarted = True
                strNum = c + strNum
            else:
                suffix = c + suffix
        if strNum == "":
            EDVerbose.WARNING("EDPluginControlMedianFilterImagev1_0.prepareQuery: No number in this filename !!! ")
            query.setItem([XSDataString(filename)])
        else:
            num = int(strNum)
            l = len(strNum)
            minNum = num - width // 2
            maxNum = minNum + width
            query.setItem([XSDataString(os.path.join(dirname, prefix + "0" * (l - len(str(i))) + str(i) + suffix))
                           for i in range(minNum, maxNum)])
        return query
