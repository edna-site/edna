#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Marie-Francoise Incardona (incardon@esrf.fr)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose          import EDVerbose
from EDActionCluster    import EDActionCluster
from EDMessage          import EDMessage
from EDUtilsFile        import EDUtilsFile

from XSDataCommon    import XSDataString
from XSDataCCP4iv10  import XSDataInputCCP4i
from XSDataCCP4iv10  import XSDataResultCCP4i

from EDPluginControlInterfacev10 import EDPluginControlInterfacev10

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataInputSubWedgeAssemble


class EDPluginControlCCP4iv10(EDPluginControlInterfacev10):
    """
    This is the plugin interface to launch the characterisation from an ccp4i gui.
    """

    def __init__ (self):
        EDPluginControlInterfacev10.__init__(self)
        self.setXSDataInputClass(XSDataInputCCP4i)
        self.__strPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev10"


    def buildInput(self, _edObject=None):
        """
        This method creates an XSDataCollection object depending on the input:
        - If dataFile input is provided, uses the "createDataCollectionFromDataFiles" to retrieve the data collection.
        - If dataSet input is provided, uses the "createDataCollectionFromDataSets" method to retrieve the data collection.
        After having retrieved an initial XSDataCollection object, it then uses the method "updateDataCollection" for
        updating certain parameters.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.buildInput...")
        xsDataCollection = None
        xsDataInputCCP4i = self.getDataInput()
        pyListXSDataFile = xsDataInputCCP4i.getDataFile()
        if(len(pyListXSDataFile) > 0):
            # Ok, we got data files - assemble these to an XSDataCollection object.
            xsDataCollection = self.createDataCollectionFromDataFiles(pyListXSDataFile)
        else:
            # No data file input - check for image files:
            pyListXSDataCCP4iDataSet = xsDataInputCCP4i.getDataSet()
            if (pyListXSDataCCP4iDataSet is None):
                strErrorMessage = "No input data!"
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv10.buildInput', 'EDPluginControlCCP4iv10', strErrorMessage)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                self.setFailure()
            else:
                xsDataCollection = self.createDataCollectionFromDataSets(pyListXSDataCCP4iDataSet)

        if xsDataCollection is not None:
            # Update the data collection with other parameters
            self.updateDataCollection(xsDataCollection)
        return xsDataCollection


    def createDataCollectionFromDataFiles(self, _pyListXSDataFile):
        """
        This method takes as input a list of paths to XML data files. It parses
        these files and create a single XSDataCollection object.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.createDataCollectionFromDataFiles")
        xsDataCollection = None
        xsDataCollectionCurrent = None
        for xsDataInputFile in _pyListXSDataFile:
            try:
                strInputFileContent = EDUtilsFile.readFile(xsDataInputFile.getPath().getValue())
                xsDataCollectionCurrent = XSDataCollection.parseString(strInputFileContent)
            except Exception, detail:
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv10.preProcess', 'EDPluginControlCCP4iv10', detail)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                self.setFailure()
            if (xsDataCollectionCurrent is None):
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv10.preProcess', 'EDPluginControlCCP4iv10', "None data collection")
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                self.setFailure()
            else:
                # Instantiate the xsDataCollection object if it's not already done.  
                if (xsDataCollection is None):
                    xsDataCollection = XSDataCollection()
                for xsDataSubWedge in xsDataCollectionCurrent.getSubWedge():
                    xsDataCollection.addSubWedge(xsDataSubWedge)
        return xsDataCollection


    def createDataCollectionFromDataSets(self, _pyListXSDataCCP4iDataSet):
        """
        This method takes as input a list of ccp4i data sets. Each data set can contain several
        paths to image files. It runs the EDPluginControlSubWedgeAssemble plugin to read the
        experimental information from the image headers and then creates a single XSDataCollection object.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.createDataCollectionFromDataSets")
        xsDataCollection = None
        # We might have to run the plugin several times
        edActionCluster = EDActionCluster()
        listPluginControlSubWedgeAssemble = []
        # Prepare the action cluster
        iIndex = 1
        for xsDataCCP4iDataSet in _pyListXSDataCCP4iDataSet:
            edPluginControlSubWedgeAssemble = self.loadPlugin(self.__strPluginControlSubWedgeAssembleName, "SubWedgeAssemble-%02d" % iIndex)
            edPluginControlSubWedgeAssemble.connectSUCCESS(self.doSuccessActionSubWedgeAssemble)
            edPluginControlSubWedgeAssemble.connectFAILURE(self.doFailureActionSubWedgeAssemble)
            # Prepare the input for the sub wedge assemble plugin
            xsDataInputSubWedgeAssemble = XSDataInputSubWedgeAssemble()
            for xsDataImageFile in xsDataCCP4iDataSet.getImageFile():
                xsDataInputSubWedgeAssemble.addFile(xsDataImageFile)
            edPluginControlSubWedgeAssemble.setDataInput(xsDataInputSubWedgeAssemble)
            listPluginControlSubWedgeAssemble.append(edPluginControlSubWedgeAssemble)
            self.addPluginToActionCluster(edPluginControlSubWedgeAssemble)
            iIndex += 1
        # Run the action cluster synchronously
        self.executeActionCluster()
        self.synchronizeActionCluster()
        # Recuperate the output
        for edPluginControlSubWedgeAssemble in listPluginControlSubWedgeAssemble:
            xsDataResultSubWedgeAssemble = edPluginControlSubWedgeAssemble.getDataOutput()
            for xsDataSubWedge in xsDataResultSubWedgeAssemble.getSubWedge():
                # Instantiate the xsDataCollection object if it's not already done.  
                if (xsDataCollection is None):
                    xsDataCollection = XSDataCollection()
                xsDataCollection.addSubWedge(xsDataSubWedge)
        return xsDataCollection


    def doSuccessActionSubWedgeAssemble(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.doSuccessActionSubWedgeAssemble...")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCCP4iv10.doSuccessActionSubWedgeAssemble")


    def doFailureActionSubWedgeAssemble(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.doFailureActionSubWedgeAssemble...")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCCP4iv10.doFailureActionSubWedgeAssemble")


    def updateDataCollection(self, _xsDataCollection):
        """
        This method updates the xsDataCollection object given as argument with the following
        parameters (if available) goven as input:
        - Diffraction plan
        - Beam size
        - Beam flux
        - Min exposure time per image
        - Max oscillation speed
        - Min oscillation width
        - Sample information
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv10.createDataCollectionFromDataSets")
        if (_xsDataCollection is not None):
            xsDataInputCCP4i = self.getDataInput()
            # Update with diffraction plan
            xsDiffactionPlan = xsDataInputCCP4i.getDiffractionPlan()
            if(xsDiffactionPlan is not None):
                _xsDataCollection.setDiffractionPlan(xsDiffactionPlan)
            # Update the data collection subwedges with additional experimental conditions
            for xsDataSubWedge in _xsDataCollection.getSubWedge():
                xsDataExperimentalCondition = xsDataInputCCP4i.getExperimentalCondition()
                if(xsDataExperimentalCondition is not None):
                    xsDataBeam = xsDataExperimentalCondition.getBeam()
                    if(xsDataBeam is not None):
                        xsDataBeamSize = xsDataBeam.getSize()
                        if(xsDataBeamSize is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setSize(xsDataBeamSize)
                        xsDataBeamFlux = xsDataBeam.getFlux()
                        if(xsDataBeamFlux is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setFlux(xsDataBeamFlux)
                        xsDataMinExposureTime = xsDataBeam.getMinExposureTimePerImage()
                        if(xsDataMinExposureTime is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setMinExposureTimePerImage(xsDataMinExposureTime)
                    xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()
                    if(xsDataGoniostat is not None):
                        xsDataMaxOscSpeed = xsDataGoniostat.getMaxOscillationSpeed()
                        if(xsDataMaxOscSpeed is not None):
                            xsDataSubWedge.getExperimentalCondition().getGoniostat().setMaxOscillationSpeed(xsDataMaxOscSpeed)
                        xsDataMinOscWidth = xsDataGoniostat.getMinOscillationWidth()
                        if(xsDataMinOscWidth is not None):
                            xsDataSubWedge.getExperimentalCondition().getGoniostat().setMinOscillationWidth(xsDataMinOscWidth)
            # Update with the sample
            xsDataSample = xsDataInputCCP4i.getSample()
            if(xsDataSample is not None):
                _xsDataCollection.setSample(xsDataSample)


    def doSuccessActionCharacterisation(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDPluginControlInterfacev10.doSuccessActionCharacterisation(self, _edPlugin)

        xsDataResultCCP4i = XSDataResultCCP4i()
        # Construct the listOfOutputFiles string...

        strListOfOutputFiles = '\n'
        strListOfOutputFiles = strListOfOutputFiles + self.getBaseDirectory() + '\n'
        xsDataOutput = self.getPluginCharacterisation().getDataOutput()
        listPredictionImages = xsDataOutput.getIndexingResult().getPredictionResult().getPredictionImage()
        for xsDataImagePrediction in listPredictionImages:
            strImagePath = xsDataImagePrediction.getPath().getValue()
            strListOfOutputFiles = strListOfOutputFiles + strImagePath + '\n'

        strCharacterisationDirectory = os.path.join(self.getWorkingDirectory(), "Characterisation")
        strBestWorkingDirectory = os.path.join(strCharacterisationDirectory, "Strategy")
        strBestWorkingDirectory = os.path.join(strBestWorkingDirectory, "EDPluginBestv10")
        strBestPlotFilePath = os.path.join(strBestWorkingDirectory, "EDPluginBestv10_plots.mtv")
        strCharacterisationOutput = os.path.join(strCharacterisationDirectory, "EDPluginControlCharacterisationv10_dataOutput.xml")

        strListOfOutputFiles = strListOfOutputFiles + strCharacterisationOutput + '\n'
        strListOfOutputFiles = strListOfOutputFiles + strBestPlotFilePath + '\n'

        xsDataStringListOfOutputFiles = XSDataString(strListOfOutputFiles)
        xsDataResultCCP4i.setListOfOutputFiles(xsDataStringListOfOutputFiles)

        self.setDataOutput(xsDataResultCCP4i)


