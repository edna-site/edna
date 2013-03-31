#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os


from EDUtilsTable      import EDUtilsTable
from EDPluginMOSFLMv10 import EDPluginMOSFLMv10

from XSDataMOSFLMv10 import XSDataMOSFLMInputIntegration
from XSDataMOSFLMv10 import XSDataMOSFLMOutputIntegration
from XSDataMOSFLMv10 import XSDataMOSFLMBeamPosition
from XSDataMOSFLMv10 import XSDataMOSFLMIntegrationStatistics
from XSDataMOSFLMv10 import XSDataMOSFLMIntegrationStatisticsPerReflectionType
from XSDataMOSFLMv10 import XSDataMOSFLMIntegrationStatisticsPerResolutionBin

from XSDataDnaTables import dna_tables

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile


class EDPluginMOSFLMIntegrationv10(EDPluginMOSFLMv10):


    def __init__(self):
        EDPluginMOSFLMv10.__init__(self)
        self.setXSDataInputClass(XSDataMOSFLMInputIntegration)


    def preProcess(self, _edObject=None):
        EDPluginMOSFLMv10.preProcess(self)
        self.DEBUG("EDPluginMOSFLMIntegrationv10.preProcess")
        self.generateMOSFLMCommands()


    def postProcess(self, _edObject=None):
        EDPluginMOSFLMv10.postProcess(self)
        self.DEBUG("EDPluginMOSFLMIntegrationv10.postProcess")
        xsDataMOSFLMOutputIntegration = self.createDataMOSFLMOutputIntegration()
        if (xsDataMOSFLMOutputIntegration is None):
            strError = "MOSFLM integration error : no integration results obtained."
            self.addExecutiveSummaryLine(strError)
            self.ERROR(strError)
            self.setFailure()
        else:
            self.setDataOutput(xsDataMOSFLMOutputIntegration)


    def checkParameters(self):
        """
        Checks the mandatory parameters for MOSLFM indexing
        """
        EDPluginMOSFLMv10.checkParameters(self)
        self.DEBUG("EDPluginMOSFLMIntegrationv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImageEnd(), "imageEnd")
        self.checkMandatoryParameters(self.getDataInput().getImageStart(), "imageStart")
        self.checkMandatoryParameters(self.getDataInput().getOscillationWidth(), "oscillationWidth")
        self.checkMandatoryParameters(self.getDataInput().getRotationAxisStart(), "rotationAxisStart")


    def generateMOSFLMCommands(self):
        """
        This method creates a list of MOSFLM integration commands given a valid
        XSDataMOSFLMIntegrationingInput as self.getDataInput()
        """
        EDPluginMOSFLMv10.generateMOSFLMCommands(self)
        self.DEBUG("EDPluginMOSFLMIntegrationv10.generateMOSFLMCommands")

        xsDataMOSFLMInputIntegration = self.getDataInput()

        if (xsDataMOSFLMInputIntegration is not None):


            iImageStart = xsDataMOSFLMInputIntegration.getImageStart().getValue()
            iImageEnd = xsDataMOSFLMInputIntegration.getImageEnd().getValue()
            fRotationAxisStart = xsDataMOSFLMInputIntegration.getRotationAxisStart().getValue()
            fOscillationWidth = xsDataMOSFLMInputIntegration.getOscillationWidth().getValue()

            self.addListCommandExecution("HKLOUT process_%d_%d.mtz" %
                                                       (iImageStart, iImageEnd))
            self.addListCommandExecution("PROCESS %d TO %d START %f ANGLE %f" %
                                                       (iImageStart, iImageEnd, fRotationAxisStart, fOscillationWidth))


            self.addListCommandExecution("BEST ON")
            self.addListCommandExecution("GO")
            self.addListCommandExecution("BEST OFF")

        # Force name of log file
        self.setScriptLogFileName(self.compactPluginName(self.getClassName())+".log")

        self.DEBUG("Finished EDPluginMOSFLMIntegrationv10.generateMOSFLMCommands")


    def createDataMOSFLMOutputIntegration(self):
        self.DEBUG("EDPluginMOSFLMIntegrationv10.createDataMOSFLMOutputIntegration")
        xsDataMOSFLMOutputIntegration = XSDataMOSFLMOutputIntegration()
        # Read bestfile.par, bestfile.hkl and bestfile.dat
        strBestfilePar = self.readBestFile("bestfile.par")
        bContinue = True
        if (strBestfilePar is not None):
            xsDataMOSFLMOutputIntegration.setBestfilePar(XSDataString(strBestfilePar))
        else:
            bContinue = False

        if bContinue:
            strBestfileHKL = self.readBestFile("bestfile.hkl")
            if (strBestfileHKL is not None):
                xsDataMOSFLMOutputIntegration.setBestfileHKL(XSDataString(strBestfileHKL))
            else:
                bContinue = False

        if bContinue:
            strBestfileDat = self.readBestFile("bestfile.dat")
            if (strBestfileDat is not None):
                xsDataMOSFLMOutputIntegration.setBestfileDat(XSDataString(strBestfileDat))
            else:
                bContinue = False

        if bContinue:
            strDnaTablesXML = self.readProcessFile(self.getBaseName() + "_dnaTables.xml")
            xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)

            xsTableIntegrationResults = EDUtilsTable.getTableFromTables(xsDataDnaTables, "integration_results")
            xsListFinalResiduals = EDUtilsTable.getListsFromTable(xsTableIntegrationResults, "final_residuals")[0]
            strRMSSpotDeviation = EDUtilsTable.getItemFromList(xsListFinalResiduals, "rms").getValueOf_()
            xsDataMOSFLMOutputIntegration.setRMSSpotDeviation(XSDataLength(float(strRMSSpotDeviation)))
            strBeamPositionX = EDUtilsTable.getItemFromList(xsListFinalResiduals, "xcen").getValueOf_()
            strBeamPositionY = EDUtilsTable.getItemFromList(xsListFinalResiduals, "ycen").getValueOf_()
            xsDataMOSFLMBeamPosition = XSDataMOSFLMBeamPosition()
            xsDataMOSFLMBeamPosition.setX(XSDataLength(float(strBeamPositionX)))
            xsDataMOSFLMBeamPosition.setY(XSDataLength(float(strBeamPositionY)))
            xsDataMOSFLMOutputIntegration.setRefinedBeam(xsDataMOSFLMBeamPosition)

            xsDataMOSFLMNewmatMatrix = self.getDataMOSFLMMatrix()
            xsDataMOSFLMOutputIntegration.setRefinedNewmat(xsDataMOSFLMNewmatMatrix)

            # New results (described in bug #63)

            xsTableIntegrationOutput = EDUtilsTable.getTableFromTables(xsDataDnaTables, "integration_output")
            xsListOutputFiles = EDUtilsTable.getListsFromTable(xsTableIntegrationOutput, "output_files")[0]

            strMTZFilename = EDUtilsTable.getItemFromList(xsListOutputFiles, "hklout").getValueOf_()
            strMTZPath = os.path.join(self.getWorkingDirectory(), strMTZFilename)
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(strMTZPath))
            xsDataMOSFLMOutputIntegration.setGeneratedMTZFile(xsDataFile)

            xsTableSummaryInformation = EDUtilsTable.getTableFromTables(xsDataDnaTables, "summary_information")
            xsListSummary = EDUtilsTable.getListsFromTable(xsTableSummaryInformation, "summary")[0]
            xsListSpots = EDUtilsTable.getListsFromTable(xsTableSummaryInformation, "spots")[0]

            strDistance = EDUtilsTable.getItemFromList(xsListSummary, "distance").getValueOf_()
            xsDataMOSFLMOutputIntegration.setRefinedDistance(XSDataLength(float(strDistance)))

            strYScale = EDUtilsTable.getItemFromList(xsListSummary, "yscale").getValueOf_()
            xsDataMOSFLMOutputIntegration.setRefinedYScale(XSDataFloat(float(strYScale)))

            strOverallIOverSigma = EDUtilsTable.getItemFromList(xsListSummary, "isigall").getValueOf_()
            xsDataMOSFLMOutputIntegration.setOverallIOverSigma(XSDataFloat(float(strOverallIOverSigma)))

            strHighestResolutionIOverSigma = EDUtilsTable.getItemFromList(xsListSummary, "isigout").getValueOf_()
            xsDataMOSFLMOutputIntegration.setHighestResolutionIOverSigma(XSDataFloat(float(strHighestResolutionIOverSigma)))

            strNumberOfBadReflections = EDUtilsTable.getItemFromList(xsListSpots, "bad_spots").getValueOf_()
            xsDataMOSFLMOutputIntegration.setNumberOfBadReflections(XSDataInteger(int(strNumberOfBadReflections)))

            strNumberOfFullyRecordedReflections = EDUtilsTable.getItemFromList(xsListSpots, "full").getValueOf_()
            xsDataMOSFLMOutputIntegration.setNumberOfFullyRecordedReflections(XSDataInteger(int(strNumberOfFullyRecordedReflections)))

            strNumberOfNegativeReflections = EDUtilsTable.getItemFromList(xsListSpots, "negative").getValueOf_()
            xsDataMOSFLMOutputIntegration.setNumberOfNegativeReflections(XSDataInteger(int(strNumberOfNegativeReflections)))

            strNumberOfOverlappedReflections = EDUtilsTable.getItemFromList(xsListSpots, "overlap").getValueOf_()
            xsDataMOSFLMOutputIntegration.setNumberOfOverlappedReflections(XSDataInteger(int(strNumberOfOverlappedReflections)))

            strNumberOfPartialReflections = EDUtilsTable.getItemFromList(xsListSpots, "partial").getValueOf_()
            xsDataMOSFLMOutputIntegration.setNumberOfPartialReflections(XSDataInteger(int(strNumberOfPartialReflections)))

            # Fill in the statistics

            xsDataMOSFLMOutputIntegration.setOverallStatistics(self.getMOSFLMIntegrationStatisticsPerResolutionBin(xsDataDnaTables, "bin_0"))

            iIndex = 1
            bContinue = True
            fMinResolution = None
            while (bContinue == True):
                strBin = "bin_%d" % iIndex
                # I don't know how many intensity bins there are. Since the EDUtilsTable.getListsFromTable
                # method crashes if the list is not present, I had to wrap the calls to this method in
                # try - except:
                try:
                    xsDataMOSFLMIntegrationStatisticsPerResolutionBin = self.getMOSFLMIntegrationStatisticsPerResolutionBin(xsDataDnaTables, strBin, fMinResolution)
                    fMinResolution = xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMaxResolution().getValue()
                    xsDataMOSFLMOutputIntegration.addStatisticsPerResolutionBin(xsDataMOSFLMIntegrationStatisticsPerResolutionBin)
                    iIndex += 1
                except:
                    bContinue = False

        # Path to log file
        xsDataMOSFLMOutputIntegration.setPathToLogFile(XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))))
        return xsDataMOSFLMOutputIntegration


    def readBestFile(self, _strBestfileName):
        strBestfile = None
        try:
            strBestfile = self.readProcessFile(_strBestfileName)
        except:
            self.setFailure()
            strError = self.readProcessErrorLogFile()
            if (strError is not None) and (strError != ""):
                strErrorMessage = "EDPluginMOSFLMIntegrationv10.readBestFile : %s" % strError
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                strErrorMessage = "EDPluginMOSFLMIntegrationv10.readBestFile : Cannot read MOSFLM " + _strBestfileName + " file"
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
        return strBestfile


    def getMOSFLMIntegrationStatisticsPerResolutionBin(self, _xsDataDnaTables, _strListName, _fMinResolution=None):
        """
        This method creates an XSDataMOSFLMIntegrationStatisticsPerResolutionBin object given an XSDataDnaTables object
        and a list name, e.g. "bin_1". If _fMinResolution is provided it is used for setting the minimum resolution,
        otherwise the min and max resolution are set to the same value provided by the xsDataList object.
        """
        xsDataTableProfileFittedFull = EDUtilsTable.getTableFromTables(_xsDataDnaTables, "profile_fitted_full")
        xsDataTableProfileFittedPartial = EDUtilsTable.getTableFromTables(_xsDataDnaTables, "profile_fitted_partial")
        xsDataTableSummationFull = EDUtilsTable.getTableFromTables(_xsDataDnaTables, "summation_full")
        xsDataTableSummationPartial = EDUtilsTable.getTableFromTables(_xsDataDnaTables, "summation_partial")

        xsListProfileFittedFull = EDUtilsTable.getListsFromTable(xsDataTableProfileFittedFull, _strListName)[0]
        xsListProfileFittedPartial = EDUtilsTable.getListsFromTable(xsDataTableProfileFittedPartial, _strListName)[0]
        xsListSummationFull = EDUtilsTable.getListsFromTable(xsDataTableSummationFull, _strListName)[0]
        xsListSummationPartial = EDUtilsTable.getListsFromTable(xsDataTableSummationPartial, _strListName)[0]

        xsDataMOSFLMIntegrationDataProfileFittedFull = self.getMOSFLMIntegrationStatistics(xsListProfileFittedFull)
        xsDataMOSFLMIntegrationDataProfileFittedPartials = self.getMOSFLMIntegrationStatistics(xsListProfileFittedPartial)
        xsDataMOSFLMIntegrationSummationFull = self.getMOSFLMIntegrationStatistics(xsListSummationFull)
        xsDataMOSFLMIntegrationSummationPartial = self.getMOSFLMIntegrationStatistics(xsListSummationPartial)

        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeProfileFitted = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeProfileFitted.setFullyRecorded(xsDataMOSFLMIntegrationDataProfileFittedFull)
        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeProfileFitted.setPartials(xsDataMOSFLMIntegrationDataProfileFittedPartials)

        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeSummation = XSDataMOSFLMIntegrationStatisticsPerReflectionType()
        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeSummation.setFullyRecorded(xsDataMOSFLMIntegrationSummationFull)
        xsDataMOSFLMIntegrationStatisticsPerReflectionTypeSummation.setPartials(xsDataMOSFLMIntegrationSummationPartial)

        xsDataMOSFLMIntegrationStatisticsPerResolutionBin = XSDataMOSFLMIntegrationStatisticsPerResolutionBin()
        xsDataMOSFLMIntegrationStatisticsPerResolutionBin.setProfileFitted(xsDataMOSFLMIntegrationStatisticsPerReflectionTypeProfileFitted)
        xsDataMOSFLMIntegrationStatisticsPerResolutionBin.setSummation(xsDataMOSFLMIntegrationStatisticsPerReflectionTypeSummation)

        strMaxResolution = EDUtilsTable.getItemFromList(xsListProfileFittedFull, "resolution").getValueOf_()
        if strMaxResolution != "overall":
            xsDataMOSFLMIntegrationStatisticsPerResolutionBin.setMaxResolution(XSDataFloat(float(strMaxResolution)))
            if (_fMinResolution is not None):
                xsDataMOSFLMIntegrationStatisticsPerResolutionBin.setMinResolution(XSDataFloat(_fMinResolution))
            else:
                xsDataMOSFLMIntegrationStatisticsPerResolutionBin.setMinResolution(XSDataFloat(float(strMaxResolution)))

        return xsDataMOSFLMIntegrationStatisticsPerResolutionBin



    def getMOSFLMIntegrationStatistics(self, _xsDataList):
        """
        This method creates a new XSDataMOSFLMIntegrationStatistics object and populates it with
        values (averaged intensity, sigma, average I over sigma and number of reflections) 
        from the _xsDataList object.
        """
        xsDataMOSFLMIntegrationStatistics = XSDataMOSFLMIntegrationStatistics()

        strAverageIntensity = EDUtilsTable.getItemFromList(_xsDataList, "i").getValueOf_()
        xsDataMOSFLMIntegrationStatistics.setAverageIntensity(XSDataFloat(float(strAverageIntensity)))

        strAverageSigma = EDUtilsTable.getItemFromList(_xsDataList, "sig").getValueOf_()
        xsDataMOSFLMIntegrationStatistics.setAverageSigma(XSDataFloat(float(strAverageSigma)))

        strAverageIOverSigma = EDUtilsTable.getItemFromList(_xsDataList, "i_sig").getValueOf_()
        xsDataMOSFLMIntegrationStatistics.setAverageIOverSigma(XSDataFloat(float(strAverageIOverSigma)))

        strNumberOfReflections = EDUtilsTable.getItemFromList(_xsDataList, "count").getValueOf_()
        xsDataMOSFLMIntegrationStatistics.setNumberOfReflections(XSDataInteger(int(strNumberOfReflections)))

        return xsDataMOSFLMIntegrationStatistics


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDPluginMOSFLMv10.generateExecutiveSummary(self, _edPlugin)
        self.DEBUG("EDPluginMOSFLMIntegrationv10.createDataMOSFLMOutputIndexing")
        xsDataMOSFLMInputIntegration = self.getDataInput()
        xsDataMOSFLMOutputIntegration = self.getDataOutput()
        if xsDataMOSFLMOutputIntegration.getNumberOfFullyRecordedReflections() is not None:
            self.addExecutiveSummaryLine("Execution of MOSFLM integration successful.")
            self.addExecutiveSummaryLine("Image directory     : %s" % xsDataMOSFLMInputIntegration.getDirectory().getValue())
            self.addExecutiveSummaryLine("Image template      : %s" % xsDataMOSFLMInputIntegration.getTemplate().getValue())
            self.addExecutiveSummaryLine("Image start         : %4d" % xsDataMOSFLMInputIntegration.getImageStart().getValue())
            self.addExecutiveSummaryLine("Image end           : %4d" % xsDataMOSFLMInputIntegration.getImageEnd().getValue())
            fRotationAxisStart = xsDataMOSFLMInputIntegration.getRotationAxisStart().getValue()
            fOscillationWidth = xsDataMOSFLMInputIntegration.getOscillationWidth().getValue()
            self.addExecutiveSummaryLine("Rotation axis start : %4.1f [degrees]" % fRotationAxisStart)
            self.addExecutiveSummaryLine("Rotation axis end   : %4.1f [degrees]" % (fRotationAxisStart + fOscillationWidth))
            self.addExecutiveSummaryLine("")
            iNumberOfFullyRecordedReflections = xsDataMOSFLMOutputIntegration.getNumberOfFullyRecordedReflections().getValue()
            self.addExecutiveSummaryLine("Number of fully recorded reflections          : %5d" % iNumberOfFullyRecordedReflections)
            self.addExecutiveSummaryLine("Number of partials                            : %5d" % xsDataMOSFLMOutputIntegration.getNumberOfPartialReflections().getValue())
            self.addExecutiveSummaryLine("Number of overlapped reflections              : %5d" % xsDataMOSFLMOutputIntegration.getNumberOfOverlappedReflections().getValue())
            self.addExecutiveSummaryLine("Number of reflections with negative intensity : %5d" % xsDataMOSFLMOutputIntegration.getNumberOfNegativeReflections().getValue())
            self.addExecutiveSummaryLine("Number of bad reflections                     : %5d" % xsDataMOSFLMOutputIntegration.getNumberOfBadReflections().getValue())
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("RMS spot deviation                            : %5.3f [mm]" % xsDataMOSFLMOutputIntegration.getRMSSpotDeviation().getValue())
            self.addExecutiveSummaryLine("Average I/sigma overall                       : %5.1f" % xsDataMOSFLMOutputIntegration.getOverallIOverSigma().getValue())
            self.addExecutiveSummaryLine("Average I/sigma at highest resolution         : %5.1f" % xsDataMOSFLMOutputIntegration.getHighestResolutionIOverSigma().getValue())
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Analysis as a function of resolution:")
            strResolution = "Res (Ang) "

            strNumberProfileFittedFullyRecorded = "Number    "
            strAverageIntensityProfileFittedFullyRecorded = " <I>      "
            strAverageIOverSigmaProfileFittedFullyRecorded = " <I/sigma>"

            strNumberProfileFittedPartials = "Number    "
            strAverageIntensityProfileFittedPartials = " <I>      "
            strAverageIOverSigmaProfileFittedPartials = " <I/sigma>"

            for xsDataMOSFLMIntegrationStatisticsPerResolutionBin in xsDataMOSFLMOutputIntegration.getStatisticsPerResolutionBin():
                fMaxResolution = xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getMaxResolution().getValue()
                strResolution += "%7.2f" % fMaxResolution
                xsDataMOSFLMIntegrationStatisticsProfileFitted = xsDataMOSFLMIntegrationStatisticsPerResolutionBin.getProfileFitted()

                xsDataMOSFLMIntegrationStatisticsProfileFittedFullyRecorded = xsDataMOSFLMIntegrationStatisticsProfileFitted.getFullyRecorded()
                strNumberProfileFittedFullyRecorded += "%7d" % xsDataMOSFLMIntegrationStatisticsProfileFittedFullyRecorded.getNumberOfReflections().getValue()
                strAverageIntensityProfileFittedFullyRecorded += "%7.0f" % xsDataMOSFLMIntegrationStatisticsProfileFittedFullyRecorded.getAverageIntensity().getValue()
                strAverageIOverSigmaProfileFittedFullyRecorded += "%7.1f" % xsDataMOSFLMIntegrationStatisticsProfileFittedFullyRecorded.getAverageIOverSigma().getValue()

                xsDataMOSFLMIntegrationStatisticsProfileFittedPartials = xsDataMOSFLMIntegrationStatisticsProfileFitted.getPartials()
                strNumberProfileFittedPartials += "%7d" % xsDataMOSFLMIntegrationStatisticsProfileFittedPartials.getNumberOfReflections().getValue()
                strAverageIntensityProfileFittedPartials += "%7.0f" % xsDataMOSFLMIntegrationStatisticsProfileFittedPartials.getAverageIntensity().getValue()
                strAverageIOverSigmaProfileFittedPartials += "%7.1f" % xsDataMOSFLMIntegrationStatisticsProfileFittedPartials.getAverageIOverSigma().getValue()

            strResolution += " Overall"
            self.addExecutiveSummaryLine(strResolution)

            strNumberProfileFittedFullyRecorded += "%8d" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getFullyRecorded().getNumberOfReflections().getValue()
            strAverageIntensityProfileFittedFullyRecorded += "%8.0f" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getFullyRecorded().getAverageIntensity().getValue()
            strAverageIOverSigmaProfileFittedFullyRecorded += "%8.1f" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getFullyRecorded().getAverageIOverSigma().getValue()

            strNumberProfileFittedPartials += "%8d" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getPartials().getNumberOfReflections().getValue()
            strAverageIntensityProfileFittedPartials += "%8.0f" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getPartials().getAverageIntensity().getValue()
            strAverageIOverSigmaProfileFittedPartials += "%8.1f" % xsDataMOSFLMOutputIntegration.getOverallStatistics().getProfileFitted().getPartials().getAverageIOverSigma().getValue()

            if (iNumberOfFullyRecordedReflections > 0):
                self.addExecutiveSummaryLine("Profile fitted fully recorded:")
                self.addExecutiveSummaryLine(strNumberProfileFittedFullyRecorded)
                self.addExecutiveSummaryLine(strAverageIntensityProfileFittedFullyRecorded)
                self.addExecutiveSummaryLine(strAverageIOverSigmaProfileFittedFullyRecorded)

            self.addExecutiveSummaryLine("Profile fitted partials:")
            self.addExecutiveSummaryLine(strNumberProfileFittedPartials)
            self.addExecutiveSummaryLine(strAverageIntensityProfileFittedPartials)
            #self.addExecutiveSummaryLine( strAverageSigmaProfileFittedPartials )
            self.addExecutiveSummaryLine(strAverageIOverSigmaProfileFittedPartials)

            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Path to MTZ file : %s" % xsDataMOSFLMOutputIntegration.getGeneratedMTZFile().getPath().getValue())
