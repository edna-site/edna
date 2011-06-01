#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Gleb Bourenkov"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose       import EDVerbose
from EDPluginControl import EDPluginControl

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger

from XSDataMXv1 import XSDataInputSubWedgeMerge
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataResultSubWedgeAssemble
from XSDataMXv1 import XSDataInputReadImageHeader


class EDPluginControlSubWedgeAssemblev1_1(EDPluginControl):
    """
    This plugin takes as input a list of paths to images. It executes the 
    EDPluginReadImageHeaderv1_1 plugin for each image path in order to read 
    the image header data and produce a XSDataSubWedge instance for each image.
    
    It then executes the EDPluginSubWedgeMergev1_1 plugin for, if possible, 
    merging these subwedges. 
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputSubWedgeAssemble)
        self.__strPluginReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.__edPluginReadImageHeader = None
        self.__strPluginSubWedgeMergeName = "EDPluginSubWedgeMergev1_1"
        self.__edPluginSubWedgeMerge = None
        self.__xsDataResultSubWedgeMerge = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getFile(), "file")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.preProcess")

        self.__edPluginReadImageHeader = self.loadPlugin(self.__strPluginReadImageHeaderName)
        self.__edPluginSubWedgeMerge = self.loadPlugin(self.__strPluginSubWedgeMergeName)


    def process(self, _oedObject=None):
        """
        """
        EDPluginControl.process(self, _oedObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.process")
        if (self.__edPluginReadImageHeader is not None and self.__edPluginSubWedgeMerge is not None):
            self.connectProcess(self.createDataCollectionFromImageHeaders)
            self.__edPluginSubWedgeMerge.connectSUCCESS(self.doSuccessActionSubWedgeMerge)
            self.__edPluginSubWedgeMerge.connectFAILURE(self.doFailureActionSubWedgeMerge)


    def postProcess(self, _oedObject=None):
        EDPluginControl.postProcess(self, _oedObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.postProcess")
        if (self.__xsDataResultSubWedgeMerge is not None):
            xsDataResultSubWedgeAssemble = XSDataResultSubWedgeAssemble()
            xsDataResultSubWedgeAssemble.setSubWedge(self.__xsDataResultSubWedgeMerge.getSubWedge())
            self.setDataOutput(xsDataResultSubWedgeAssemble)



    def createDataCollectionFromImageHeaders(self, _edPlugin):
        """
        This method creates a list of XSDataSubwedges by reading the header of the images
        given as a list of paths as input.
        """
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.createDataCollectionFromImageHeaders")
        xsDataInputSubWedgeAssemble = _edPlugin.getDataInput()
        listXSDataFile = xsDataInputSubWedgeAssemble.getFile()
        if (len(listXSDataFile) > 0):
            listSubWedge = []
            iIndex = 1
            for xsDataFile in listXSDataFile:
                xsDataFileCopy = XSDataFile.parseString(xsDataFile.marshal())
                xsDataInputReadImageHeader = XSDataInputReadImageHeader()
                xsDataInputReadImageHeader.setImage(xsDataFileCopy)
                self.__edPluginReadImageHeader = self.loadPlugin(self.__strPluginReadImageHeaderName, "ReadImageHeader_%d" % (iIndex))
                self.__edPluginReadImageHeader.setDataInput(xsDataInputReadImageHeader)
                self.__edPluginReadImageHeader.executeSynchronous()
                xsDataResultReadImageHeader = self.__edPluginReadImageHeader.getDataOutput()
                bSuccess = False
                if (xsDataResultReadImageHeader is not None):
                    xsDataSubWedge = xsDataResultReadImageHeader.getSubWedge()
                    if (xsDataSubWedge is not None):
                        xsDataSubWedge.setSubWedgeNumber(XSDataInteger(iIndex))
                        listSubWedge.append(xsDataSubWedge)
                        bSuccess = True
                if (not bSuccess):
                    # Fix for bug #223: raise an error if an image could not be read
                    strErrorMessage = "EDPluginControlSubWedgeAssemblev1_1.createDataCollectionFromImageHeaders: %s %s" % (
                                        self.__strPluginReadImageHeaderName, \
                                        "Could not read header from image %s" % xsDataFileCopy.getPath().getValue())
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                iIndex += 1
            if (not self.isFailure()):
                xsDataInputSubWedgeMerge = XSDataInputSubWedgeMerge()
                for xsDataSubWedge in listSubWedge:
                    xsDataInputSubWedgeMerge.addSubWedge(xsDataSubWedge)
                self.__edPluginSubWedgeMerge.setDataInput(xsDataInputSubWedgeMerge)
                self.__edPluginSubWedgeMerge.executeSynchronous()


    def doSuccessActionSubWedgeMerge(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.doSuccessActionSubWedgeMerge")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSubWedgeAssemblev1_1.doSuccessActionSubWedgeMerge")
        self.__xsDataResultSubWedgeMerge = _edPlugin.getDataOutput()


    def doFailureActionSubWedgeMerge(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblev1_1.doFailureActionSubWedgeMerge")
        EDVerbose.screen("Execution of " + self.__strPluginSubWedgeMergeName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSubWedgeAssemblev1_1.doFailureActionSubWedgeMerge")
        self.setFailure()
