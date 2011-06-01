#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlCCP4iv1_1.py 705 2009-05-13 09:52:07Z svensson $"
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

from EDActionCluster    import EDActionCluster
from EDVerbose          import EDVerbose
from EDMessage          import EDMessage
from EDUtilsFile        import EDUtilsFile

from XSDataCommon    import XSDataString
from XSDataCCP4iv1_1  import XSDataInputCCP4i
from XSDataCCP4iv1_1  import XSDataResultCCP4i

from EDPluginControlInterfacev1_1 import EDPluginControlInterfacev1_1

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataInputSubWedgeAssemble

import os

class EDPluginControlCCP4iv1_1(EDPluginControlInterfacev1_1):
    """
    This is the plugin interface to launch the characterisation from an ccp4i gui.
    """

    def __init__ (self):
        """
        """
        EDPluginControlInterfacev1_1.__init__(self)
        self.setXSDataInputClass(XSDataInputCCP4i)
        self.__strPluginControlSubWedgeAssembleName = "EDPluginControlSubWedgeAssemblev1_1"


    def buildInput(self, _edObject=None):
        """
        This method creates an XSDataInputCharacterisation object depending on the input:
        - If dataFile input is provided, uses the "createDataInputCharacterisationFromDataFiles" to retrieve the data collection.
        - If dataSet input is provided, uses the "createDataInputCharacterisationFromDataSets" method to retrieve the data collection.
        After having retrieved an initial XSDataInputCharacterisation object, it then uses the method "updateDataInputCharacterisation" for
        updating certain parameters.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.buildInput...")
        xsDataInputCCP4i = self.getDataInput()
        pyListXSDataFile = xsDataInputCCP4i.getDataFile()
        if(len(pyListXSDataFile) > 0):
            # Ok, we got data files - assemble these to an XSDataInputCharacterisation object.
            xsDataInputCharacterisation = self.createDataInputCharacterisationFromDataFiles(pyListXSDataFile)
        else:
            # No data file input - check for image files:
            pyListXSDataCCP4iDataSet = xsDataInputCCP4i.getDataSet()
            if (pyListXSDataCCP4iDataSet is None):
                pyStrErrorMessage = "No input data!"
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv1_1.buildInput', 'EDPluginControlCCP4iv1_1', pyStrErrorMessage)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                raise RuntimeError, errorMessage
            else:
                xsDataInputCharacterisation = self.createDataInputCharacterisationFromDataSets(pyListXSDataCCP4iDataSet)
        # Update the data collection with other parameters
        if (xsDataInputCharacterisation is None):
            strError = "EDPluginControlCCP4iv1_1.buildInput: failed when building input."
            EDVerbose.ERROR(strError)
            self.addErrorMessage(strError)
            self.setFailure()
        else:
            self.updateDataInputCharacterisation(xsDataInputCharacterisation)
        return xsDataInputCharacterisation


    def createDataInputCharacterisationFromDataFiles(self, _pyListXSDataFile):
        """
        This method takes as input a list of paths to XML data files. It parses
        these files and create a single XSDataInputCharacterisation object.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.createDataInputCharacterisationFromDataFiles")
        xsDataInputCharacterisation = None
        for xsDataInputFile in _pyListXSDataFile:
            try:
                pyStrInputFileContent = EDUtilsFile.readFile(xsDataInputFile.getPath().getValue())
                xsDataInputCharacterisationCurrent = XSDataInputCharacterisation.parseString(pyStrInputFileContent)
            except Exception, detail:
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv1_1.preProcess', 'EDPluginControlCCP4iv1_1', detail)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                raise RuntimeError, errorMessage
            if (xsDataInputCharacterisationCurrent is None):
                errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlCCP4iv1_1.preProcess', 'EDPluginControlCCP4iv1_1', "None data collection")
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                raise RuntimeError, errorMessage
            else:
                # Instantiate the xsDataInputCharacterisation object if it's not already done.  
                if (xsDataInputCharacterisation is None):
                    xsDataInputCharacterisation = XSDataInputCharacterisation()
                xsDataInputCharacterisation.setDataCollection(xsDataInputCharacterisationCurrent.getDataCollection())
        return xsDataInputCharacterisation


    def createDataInputCharacterisationFromDataSets(self, _pyListXSDataCCP4iDataSet):
        """
        This method takes as input a list of ccp4i data sets. Each data set can contain several
        paths to image files. It runs the EDPluginControlSubWedgeAssemble plugin to read the
        experimental information from the image headers and then creates a single XSDataInputCharacterisation object.
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.createDataInputCharacterisationFromDataSets")
        xsDataInputCharacterisation = None
        # We might have to run the plugin several times
        edActionCluster = EDActionCluster()
        pyListPluginControlSubWedgeAssemble = []
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
            pyListPluginControlSubWedgeAssemble.append(edPluginControlSubWedgeAssemble)
            self.addPluginToActionCluster(edPluginControlSubWedgeAssemble)
            iIndex += 1
        # Run the action cluster synchronously
        self.executeActionCluster()
        self.synchronizeActionCluster()
        # Recuperate the output
        for edPluginControlSubWedgeAssemble in pyListPluginControlSubWedgeAssemble:
            if (edPluginControlSubWedgeAssemble.isFailure()):
                self.setFailure()
            else:
                xsDataResultSubWedgeAssemble = edPluginControlSubWedgeAssemble.getDataOutput()
                for xsDataSubWedge in xsDataResultSubWedgeAssemble.getSubWedge():
                    # Instantiate the xsDataInputCharacterisation object if it's not already done.
                    xsDataCollection = None
                    if (xsDataInputCharacterisation is None):
                        xsDataInputCharacterisation = XSDataInputCharacterisation()
                    else:
                        xsDataCollection = xsDataInputCharacterisation.getDataCollection()
                    if (xsDataCollection is None):
                        xsDataCollection = XSDataCollection()
                    xsDataCollection.addSubWedge(xsDataSubWedge)
                    xsDataInputCharacterisation.setDataCollection(xsDataCollection)
        return xsDataInputCharacterisation


    def doSuccessActionSubWedgeAssemble(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.doSuccessActionSubWedgeAssemble...")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCCP4iv1_1.doSuccessActionSubWedgeAssemble")


    def doFailureActionSubWedgeAssemble(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.doFailureActionSubWedgeAssemble...")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCCP4iv1_1.doFailureActionSubWedgeAssemble")
        self.setFailure()


    def updateDataInputCharacterisation(self, _xsDataInputCharacterisation):
        """
        This method updates the xsDataInputCharacterisation object given as argument with the following
        parameters (if available) goven as input:
        - Diffraction plan
        - Beam size
        - Beam flux
        - Min exposure time per image
        - Max oscillation speed
        - Min oscillation width
        - Sample information
        """
        EDVerbose.DEBUG("EDPluginControlCCP4iv1_1.createDataInputCharacterisationFromDataSets")
        xsDataCollection = _xsDataInputCharacterisation.getDataCollection()
        if (_xsDataInputCharacterisation is not None):
            xsDataInputCCP4i = self.getDataInput()
            # Update with diffraction plan
            xsDiffactionPlan = xsDataInputCCP4i.getDiffractionPlan()
            if(xsDiffactionPlan is not None):
                xsDataCollection.setDiffractionPlan(xsDiffactionPlan)
            # Update the data collection subwedges with additional experimental conditions
            for xsDataSubWedge in xsDataCollection.getSubWedge():
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
                        xsDataTransmission = xsDataBeam.getTransmission()
                        if(xsDataTransmission is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setTransmission(xsDataTransmission)
                        xsDataWavelength = xsDataBeam.getWavelength()
                        if(xsDataWavelength is not None):
                            xsDataSubWedge.getExperimentalCondition().getBeam().setWavelength(xsDataWavelength)
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
                xsDataCollection.setSample(xsDataSample)


    def doSuccessActionCharacterisation(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDPluginControlInterfacev1_1.doSuccessActionCharacterisation(self, _edPlugin)

        # Generate file with executive summary...
        pyStrCharacterisationExecutiveSummary = ""
        pyListExecutiveSummaryLines = self.getPluginCharacterisation().getListExecutiveSummaryLines()
        for pyStrLine in pyListExecutiveSummaryLines:
            pyStrCharacterisationExecutiveSummary += pyStrLine + "\n"
        pyStrSummaryDirectory = self.getWorkingDirectory()
        pyStrSummaryPath = os.path.join(pyStrSummaryDirectory, "CharacterisationExecutiveSummary.txt")
        EDUtilsFile.writeFile(pyStrSummaryPath, pyStrCharacterisationExecutiveSummary)

        xsDataResultCCP4i = XSDataResultCCP4i()
        # Construct the listOfOutputFiles string...

        pyStrListOfOutputFiles = '\n'
        pyStrListOfOutputFiles = pyStrListOfOutputFiles + self.getBaseDirectory() + '\n'
        xsDataOutput = self.getPluginCharacterisation().getDataOutput()
        pyListPredictionImages = xsDataOutput.getIndexingResult().getPredictionResult().getPredictionImage()
        for xsDataImagePrediction in pyListPredictionImages:
            strImagePath = xsDataImagePrediction.getPath().getValue()
            pyStrListOfOutputFiles = pyStrListOfOutputFiles + strImagePath + '\n'

        pyStrCharacterisationDirectory = os.path.join(self.getWorkingDirectory(), "Characterisation")
        # "Hack" for determining if we use version 1.1 or 1.2 of the BEST plugin...
        pyStrBestWorkingDirectory = os.path.join(pyStrCharacterisationDirectory, "Strategy")
        pyStrBestPlotFilePath = None
        pyStrBestLogFilePath = None
        if (os.path.exists(os.path.join(pyStrBestWorkingDirectory, "Bestv1_1"))):
            pyStrBestWorkingDirectory = os.path.join(pyStrBestWorkingDirectory, "Bestv1_1")
            pyStrBestPlotFilePath = os.path.join(pyStrBestWorkingDirectory, "Bestv1_1_plots.mtv")
            pyStrBestLogFilePath = os.path.join(pyStrBestWorkingDirectory, "Bestv1_1.log")
        elif (os.path.exists(os.path.join(pyStrBestWorkingDirectory, "Bestv1_2"))):
            pyStrBestWorkingDirectory = os.path.join(pyStrBestWorkingDirectory, "Bestv1_2")
            pyStrBestPlotFilePath = os.path.join(pyStrBestWorkingDirectory, "Bestv1_2_plots.mtv")
            pyStrBestLogFilePath = os.path.join(pyStrBestWorkingDirectory, "best.log")
        pyStrCharacterisationOutput = None
        if self.getPluginCharacterisation().getClassName() == "EDPluginControlCharacterisationv1_1":
            pyStrCharacterisationOutput = os.path.join(pyStrCharacterisationDirectory, "ControlCharacterisationv1_1_dataOutput.xml")
        elif self.getPluginCharacterisation().getClassName() == "EDPluginControlCharacterisationv1_2":
            pyStrCharacterisationOutput = os.path.join(pyStrCharacterisationDirectory, "ControlCharacterisationv1_2_dataOutput.xml")

        pyStrListOfOutputFiles = pyStrListOfOutputFiles + pyStrCharacterisationOutput + '\n'
        if (pyStrBestLogFilePath is not None):
            pyStrListOfOutputFiles = pyStrListOfOutputFiles + pyStrBestLogFilePath + '\n'
            pyStrListOfOutputFiles = pyStrListOfOutputFiles + pyStrBestPlotFilePath + '\n'
        pyStrListOfOutputFiles = pyStrListOfOutputFiles + pyStrSummaryPath + '\n'

        xsDataStringListOfOutputFiles = XSDataString(pyStrListOfOutputFiles)
        xsDataResultCCP4i.setListOfOutputFiles(xsDataStringListOfOutputFiles)

        self.setDataOutput(xsDataResultCCP4i)


