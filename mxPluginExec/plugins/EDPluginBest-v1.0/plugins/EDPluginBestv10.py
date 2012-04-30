#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose import EDVerbose
from EDUtilsPath                     import EDUtilsPath
from EDMessage                       import EDMessage
from EDUtilsFile                     import EDUtilsFile
from EDUtilsTable                    import EDUtilsTable
from EDConfiguration                 import EDConfiguration
from EDPluginExecProcessScript       import EDPluginExecProcessScript

from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataTime

from XSDataBestv10 import XSDataBestInput
from XSDataBestv10 import XSDataBestOutput

from XSDataBestv10 import XSDataBestCollectionPlan
from XSDataBestv10 import XSDataBestStatisticalPrediction
from XSDataBestv10 import XSDataBestCollectionRun
from XSDataBestv10 import XSDataBestStrategySummary
from XSDataBestv10 import XSDataBestResolutionBin

from XSDataDnaTablesBest          import dna_tables


class EDPluginBestv10(EDPluginExecProcessScript):


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.addCompatibleVersion("Version 3.1.0.d //  16.07.2007")
        self.addCompatibleVersion("Version 3.2.0 //  03.11.2008")

        self.strCONF_BEST_HOME_LABEL = "besthome"

        # Default value of strategy complexity
        self.strComplexity = "none"

        self.strBestHome = None
        self.strCommandBestHome = None
        self.strCommandBest = None

        self.strExposureTime = None
        self.strDoseRate = None
        self.strDetectorType = None

        self.strPathToBestDatFile = None
        self.strPathToBestParFile = None
        self.listFileBestHKL = []

        self.setXSDataInputClass(XSDataBestInput)


    def getComplexity(self):
        return self.strComplexity


    def setComplexity(self, _strComplexity):
        self.strComplexity = _strComplexity


    def getBestHome(self):
        return self.strBestHome


    def setBestHome(self, strBestHome):
        self.strBestHome = strBestHome


    def getCommandBestHome(self):
        return self.strCommandBestHome


    def setCommandBestHome(self, _strCommandBestHome):
        self.strCommandBestHome = _strCommandBestHome


    def getCommandBest(self):
        return self.strCommandBest


    def setCommandBest(self, _strCommandBest):
        self.strCommandBest = _strCommandBest


    def getFileBestDat(self):
        return self.strPathToBestDatFile


    def setFileBestDat(self, _edFileBestDat):
        self.strPathToBestDatFile = _edFileBestDat


    def getFileBestPar(self):
        return self.strPathToBestParFile


    def setFileBestPar(self, _edFileBestPar):
        self.strPathToBestParFile = _edFileBestPar


    def getListFileBestHKL(self):
        return self.listFileBestHKL


    def setListFileBestHKL(self, _listFileBestHKL):
        self.listFileBestHKL = _listFileBestHKL


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        EDVerbose.DEBUG("EDPluginBestv10.configure")
        self.setRequireCCP4(True)
        strScriptExecutable = self.getScriptExecutable()
        EDVerbose.DEBUG("EDPluginBestv10.configure: Script Executable: " + strScriptExecutable)
        strBestScriptHome = os.path.dirname(strScriptExecutable)
        strBestHome = None

        pluginConfiguration = self.getConfiguration()

        if(pluginConfiguration == None):
            strBestHome = strBestScriptHome
        else:
            strBestHome = EDConfiguration.getStringParamValue(pluginConfiguration, self.strCONF_BEST_HOME_LABEL)
            if(strBestHome == None):
                strBestHome = strBestScriptHome

        self.setBestHome(strBestHome)
        EDVerbose.DEBUG("EDPluginBestv10.configure: Best Home: " + strBestHome)
        self.setCommandBestHome("export besthome=" + self.getBestHome())


    def preProcess(self, _edObject=None):
        """
        """
        EDPluginExecProcessScript.preProcess(self)

        self.setFileBestDat(os.path.join(self.getWorkingDirectory(), "bestfile.dat"))
        self.setFileBestPar(os.path.join(self.getWorkingDirectory(), "bestfile.par"))

        EDUtilsFile.writeFile(self.getFileBestDat(), self.getDataInput().getBestFileContentDat().getValue())
        EDUtilsFile.writeFile(self.getFileBestPar(), self.getDataInput().getBestFileContentPar().getValue())

        listBestFileContentHKL = self.getDataInput().getBestFileContentHKL()

        iterator = 0
        for bestFileContentHKL in listBestFileContentHKL:
            iterator = iterator + 1
            bestFileHKL = os.path.join(self.getWorkingDirectory(), "bestfile" + str(iterator) + ".hkl")
            self.listFileBestHKL.append(bestFileHKL)
            EDUtilsFile.writeFile(bestFileHKL, bestFileContentHKL.getValue())


        if(self.getDataInput().getComplexity() is not None):
            self.setComplexity(self.getDataInput().getComplexity().getValue())

        self.initializeCommands()


    def initializeCommands(self):
        self.addListCommandPreExecution(self.strCommandBestHome)

        listFileBestHKL = self.getListFileBestHKL()
        listFileBestHKLCommand = ""

        for fileBestHKL in listFileBestHKL:
            listFileBestHKLCommand = listFileBestHKLCommand + fileBestHKL + " "

        strDetectorName = self.getDataInput().getDetectorType().getValue()
        strExposureTime = str(self.getDataInput().getBeamExposureTime().getValue())
        strMaxExposureTime = str(self.getDataInput().getBeamMaxExposureTime().getValue())

        self.strCommandBest = "-f " + strDetectorName + " " + \
                                   "-t " + strExposureTime + " "

        if(self.getDataInput().getBeamMinExposureTime() is not None):
            strBeamMinExposureTime = str(self.getDataInput().getBeamMinExposureTime().getValue())
            self.strCommandBest = self.strCommandBest + "-M " + strBeamMinExposureTime + " "

        if(self.getDataInput().getGoniostatMaxRotationSpeed() is not None):
            strGoniostatMaxRotationSpeed = str(self.getDataInput().getGoniostatMaxRotationSpeed().getValue())
            self.strCommandBest = self.strCommandBest + "-S " + strGoniostatMaxRotationSpeed + " "

        if(self.getDataInput().getGoniostatMinRotationWidth() is not None):
            strGoniostatMinRotationWidth = str(self.getDataInput().getGoniostatMinRotationWidth().getValue())
            self.strCommandBest = self.strCommandBest + "-w " + strGoniostatMinRotationWidth + " "

        if(self.getDataInput().getAimedResolution() is not None):
            strAimedResolution = str(self.getDataInput().getAimedResolution().getValue())
            self.strCommandBest = self.strCommandBest + "-r " + strAimedResolution + " "

        if(self.getDataInput().getAimedRedundancy() is not None):
            strAimedRedundancy = str(self.getDataInput().getAimedRedundancy().getValue())
            self.strCommandBest = self.strCommandBest + "-R " + strAimedRedundancy + " "

        if(self.getDataInput().getAimedCompleteness() is not None):
            strAimedCompleteness = str(self.getDataInput().getAimedCompleteness().getValue())
            self.strCommandBest = self.strCommandBest + "-C " + strAimedCompleteness + " "

        if(self.getDataInput().getAimedIOverSigma() is not None):
            strAimedIOverSigma = str(self.getDataInput().getAimedIOverSigma().getValue())
            self.strCommandBest = self.strCommandBest + "-i2s " + strAimedIOverSigma + " "

        if(self.getDataInput().getCrystalAbsorbedDoseRate() is not None):
            strCrystalAbsorbedDoseRate = str(self.getDataInput().getCrystalAbsorbedDoseRate().getValue())
            self.strCommandBest = self.strCommandBest + "-GpS " + strCrystalAbsorbedDoseRate + " "

        if(self.getDataInput().getCrystalShape() is not None):
            strCrystalShape = str(self.getDataInput().getCrystalShape().getValue())
            self.strCommandBest = self.strCommandBest + "-sh " + strCrystalShape + " "

        if(self.getDataInput().getCrystalSusceptibility() is not None):
            strCrystalSusceptibility = str(self.getDataInput().getCrystalSusceptibility().getValue())
            self.strCommandBest = self.strCommandBest + "-su " + strCrystalSusceptibility + " "


        self.strCommandBest = self.strCommandBest + "-T " + strMaxExposureTime + " " + \
                                     "-dna " + self.getScriptBaseName() + "_dnaTables.xml" + " " + \
                                     "-o " + self.getScriptBaseName() + "_plots.mtv " + \
                                     "-e " + self.getComplexity() + " " + \
                                     "-mos " + self.getFileBestDat() + " " + self.getFileBestPar() + " " + listFileBestHKLCommand

        self.setScriptCommandline(self.strCommandBest)


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExecProcessScript.postProcess(self)

        strError = self.readProcessErrorLogFile()
        if (strError is not None) and (strError != ""):
            errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginBestv10.postProcess', 'EDPluginBestv10', strError)
            EDVerbose.error(errorMessage)
            self.addErrorMessage(errorMessage)
            raise RuntimeError, errorMessage

        outputData = self.getOutputDataFromDNATableFile(os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_dnaTables.xml"))
        self.setDataOutput(outputData)


    def getOutputDataFromDNATableFile(self, _strFileName):
        """
        """

        xsDataBestOutput = XSDataBestOutput()
        strDnaTablesXML = self.readProcessFile(_strFileName)
        xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
        # Loop through all the tables and fill in the relevant parts of xsDataBestOutput

        # SubWedges
        xsTablesCollectionStrategy = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "data_collection_strategy")

        for xsTableCollectionStrategy in xsTablesCollectionStrategy:

            xsDataBestCollectionPlan = XSDataBestCollectionPlan()
            xsCollectionRunList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "collection_run")

            for xsCollectionRunItemList in xsCollectionRunList:
                xsDataCollectionRun = self.collectionRunItemListToCollectionRun(xsCollectionRunItemList)
                xsDataBestCollectionPlan.addCollectionRun(xsDataCollectionRun)

            # Strategy Summary
            xsStrategySummaryItemList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "summary")
            xsDataStrategySummary = self.strategySummaryItemListToStrategySummary(xsStrategySummaryItemList[0])
            # Ranking Resolution
            # Not part of strategySummaryItemListToStrategySummary method since it is in the general_form part
            xsTableGeneralInform = EDUtilsTable.getTableFromTables(xsDataDnaTables, "general_inform")
            xsRankingResolutionItemList = EDUtilsTable.getListsFromTable(xsTableGeneralInform, "ranking_resolution")
            xsItemRankingResolution = EDUtilsTable.getItemFromList(xsRankingResolutionItemList[0], "dmin")
            fRankingResolution = float(xsItemRankingResolution.getValueOf_())
            xsDataStrategySummary.setRankingResolution(XSDataFloat(fRankingResolution))

            xsDataBestCollectionPlan.setStrategySummary(xsDataStrategySummary)

            # Satistics
            xsTablesStatisticalPrediction = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "statistical_prediction")
            for xsTableStatisticalPrediction in xsTablesStatisticalPrediction:
                if(xsTableStatisticalPrediction.getIndex() == xsTableCollectionStrategy.getIndex()):
                    xsResolutionBinList = EDUtilsTable.getListsFromTable(xsTableStatisticalPrediction, "resolution_bin")
                    xsDataStatisticalPrediction = XSDataBestStatisticalPrediction()
                    for xsResolutionBinItemList in xsResolutionBinList:
                        xsDataResolutionBin = self.resolutionBinItemListToResolutionBin(xsResolutionBinItemList)
                        xsDataStatisticalPrediction.addResolutionBin(xsDataResolutionBin)

                    xsDataBestCollectionPlan.setStatisticalPrediction(xsDataStatisticalPrediction)

            xsDataBestOutput.addCollectionPlan(xsDataBestCollectionPlan)

        return xsDataBestOutput


    def collectionRunItemListToCollectionRun(self, _xsCollectionRunItemList):
        """
        """
        xsDataCollectionRun = XSDataBestCollectionRun()

        xsItemExposureTime = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "exposure_time")
        fExposureTime = float(xsItemExposureTime.getValueOf_())
        xsDataCollectionRun.setExposureTime(XSDataTime(fExposureTime))

        xsItemDistance = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "distance")
        fDistance = float(xsItemDistance.getValueOf_())
        xsDataCollectionRun.setDistance(XSDataLength(fDistance))

        xsItemRotationAxisStart = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "phi_start")
        fRotationAxisStart = float(xsItemRotationAxisStart.getValueOf_())
        xsDataCollectionRun.setPhiStart(XSDataAngle(fRotationAxisStart))

        xsNumberOfImages = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "number_of_images")
        iNumberOfImages = int(xsNumberOfImages.getValueOf_())
        xsDataCollectionRun.setNumberOfImages(XSDataInteger(iNumberOfImages))

        xsItemPhiWidth = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "phi_width")
        fPhiWidth = float(xsItemPhiWidth.getValueOf_())
        xsDataCollectionRun.setPhiWidth(XSDataAngle(fPhiWidth))

        xsItemOverlaps = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "overlaps")
        strOverlaps = xsItemOverlaps.getValueOf_()
        xsDataCollectionRun.setOverlaps(XSDataString(strOverlaps))

        return xsDataCollectionRun


    def strategySummaryItemListToStrategySummary(self, _xsStrategySummaryItemList):
        xsDataStrategySummary = XSDataBestStrategySummary()
        pyStrItemAttenuation = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "attenuation")
        fAttenuation = float(pyStrItemAttenuation.getValueOf_())
        xsDataStrategySummary.setAttenuation(XSDataFloat(fAttenuation))

        pyStrItemCompleteness = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "completeness")
        # For homegeneity concerns, EDNA data model should store all the completeness value in fraction
        # ( DNA table xml file stores the summary strategy completeness in percentage whereas
        # the resolution bin completeness are in fraction )
        fCompleteness = float(pyStrItemCompleteness.getValueOf_()) / 100
        xsDataStrategySummary.setCompleteness(XSDataFloat(fCompleteness))

        pyStrItemISigma = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "i_sigma")
        fISigma = float(pyStrItemISigma.getValueOf_())
        xsDataStrategySummary.setISigma(XSDataFloat(fISigma))

        pyStrItemRedundancy = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "redundancy")
        fRedundancy = float(pyStrItemRedundancy.getValueOf_())
        xsDataStrategySummary.setRedundancy(XSDataFloat(fRedundancy))

        pyStrItemResolution = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "resolution")
        fResolution = float(pyStrItemResolution.getValueOf_())
        xsDataStrategySummary.setResolution(XSDataFloat(fResolution))

        pyStrItemResolutionReasoning = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "resolution_reasoning")
        strResolutionReasoning = pyStrItemResolutionReasoning.getValueOf_()
        xsDataStrategySummary.setResolutionReasoning(XSDataString(strResolutionReasoning))

        pyStrItemTotalDataCollectionTime = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "total_data_collection_time")
        fTotalDataCollectionTime = float(pyStrItemTotalDataCollectionTime.getValueOf_())
        xsDataStrategySummary.setTotalDataCollectionTime(XSDataTime(fTotalDataCollectionTime))

        pyStrItemTotalExposureTime = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "total_exposure_time")
        fTotalExposureTime = float(pyStrItemTotalExposureTime.getValueOf_())
        xsDataStrategySummary.setTotalExposureTime(XSDataTime(fTotalExposureTime))

        return xsDataStrategySummary


    def resolutionBinItemListToResolutionBin(self, _xsResolutionBinItemList):
        xsDataResolutionBin = XSDataBestResolutionBin()

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "min_resolution")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setMinResolution(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "max_resolution")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setMaxResolution(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "completeness")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setCompleteness(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "redundancy")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setRedundancy(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_intensity")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setAverageIntensity(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_error")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setAverageSigma(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setIOverSigma(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "R_factor")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setRFactor(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "Chi**2")
        if (pyStrItem is not None):
            fItem = float(pyStrItem.getValueOf_())
            xsDataResolutionBin.setChi2(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma_Chi**2")
        if (pyStrItem is not None):
            fItem = float(pyStrItem.getValueOf_())
            xsDataResolutionBin.setIOverSigmaChi(XSDataFloat(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "fract_overload")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setPercentageOverload(XSDataFloat(fItem))

        return xsDataResolutionBin


    def checkParameters(self):
        """
        Checks the data input object
        """
        # Checks the mandatory parameters:
        self.checkMandatoryParameters(self.getDataInput().getBeamExposureTime(), "beamExposureTime")
        self.checkMandatoryParameters(self.getDataInput().getBeamMaxExposureTime(), "beamMaxExposureTime")
        self.checkMandatoryParameters(self.getDataInput().getDetectorType(), "detectorType")

        self.checkImportantParameters(self.getDataInput().getCrystalAbsorbedDoseRate(), "crystalDoseRate")
        self.checkImportantParameters(self.getDataInput().getCrystalShape(), "crystalShape")


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginBestv10.generateExecutiveSummary")
        if (self.getStringVersion() is not None):
            self.addExecutiveSummaryLine(self.getStringVersion())

        xsDataBestv10Output = self.getDataOutput()
        listCollectionPlan = xsDataBestv10Output.getCollectionPlan()

        if(len(listCollectionPlan) > 1):
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("MULTI-SWEEP COLLECTION PLAN STRATEGY:")
            self.addExecutiveSummaryLine("------------------------------------")
            self.addExecutiveSummaryLine("")
            for xsDataCollectionPlan in listCollectionPlan:
                xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                strReasoning = xsDataStrategySummary.getResolutionReasoning().getValue()
                if (strReasoning.find("Low-resolution") != -1) and (listCollectionPlan.index(xsDataCollectionPlan) != 0):
                    listCollectionPlan.remove(xsDataCollectionPlan)
                    listCollectionPlan.insert(0, xsDataCollectionPlan)

        iSweepNumber = 1
        for xsDataCollectionPlan in listCollectionPlan:

            if(len(listCollectionPlan) > 1):

                self.addExecutiveSummaryLine("SWEEP %d:" % iSweepNumber)
                self.addExecutiveSummaryLine("---------------------------------------------------------------------------------------")
                iSweepNumber = iSweepNumber + 1

            xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
            self.addExecutiveSummaryLine("Resolution reasoning          : %s" % xsDataStrategySummary.getResolutionReasoning().getValue())
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Plan for data collection:")
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine(" N |  Phi_start |  N.of.images | Rot.width |  Exposure | Distance |  Overlap |")
            iCollectionRunNumber = 1
            iTotalImages = 0
            fTotalRotationRange = 0.0
            for xsDataCollectionRun in xsDataCollectionPlan.getCollectionRun():
                fDistance = xsDataCollectionRun.getDistance().getValue()
                fExposureTime = xsDataCollectionRun.getExposureTime().getValue()
                iNumberOfImages = xsDataCollectionRun.getNumberOfImages().getValue()
                strOverlaps = ""
                if (xsDataCollectionRun.getOverlaps() is not None):
                    strOverlaps = xsDataCollectionRun.getOverlaps().getValue()
                fPhiStart = xsDataCollectionRun.getPhiStart().getValue()
                fPhiWidth = xsDataCollectionRun.getPhiWidth().getValue()
                self.addExecutiveSummaryLine("%2d | %8.2f   | %7d      |%9.2f  | %9.2f | %7.1f  | %7s  |" % \
                                              (iCollectionRunNumber, fPhiStart, iNumberOfImages, \
                                                fPhiWidth, fExposureTime, fDistance, strOverlaps))
                iCollectionRunNumber += 1
                iTotalImages += iNumberOfImages
                fTotalRotationRange += fPhiWidth * iNumberOfImages


            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Attenuation                   : %6.1f" % xsDataStrategySummary.getAttenuation().getValue())
            self.addExecutiveSummaryLine("Total rotation range          : %6.1f [degrees]" % fTotalRotationRange)
            self.addExecutiveSummaryLine("Total number of images        : %6d" % iTotalImages)
            self.addExecutiveSummaryLine("Total exposure time           : %6.2f [s]" % xsDataStrategySummary.getTotalExposureTime().getValue())
            self.addExecutiveSummaryLine("Total data collection time    : %6.2f [s]" % xsDataStrategySummary.getTotalDataCollectionTime().getValue())
            self.addExecutiveSummaryLine("Resolution                    : %6.2f [A]" % xsDataStrategySummary.getResolution().getValue())
            self.addExecutiveSummaryLine("Ranking resolution            : %6.2f [A]" % xsDataStrategySummary.getRankingResolution().getValue())
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Predicted statistics:")
            self.addExecutiveSummaryLine("Completeness                  : %6.1f [%%]" % (xsDataStrategySummary.getCompleteness().getValue() * 100))
            self.addExecutiveSummaryLine("I/sigma at highest resolution : %6.1f" % xsDataStrategySummary.getISigma().getValue())
            self.addExecutiveSummaryLine("Multiplicity                  : %6.1f" % xsDataStrategySummary.getRedundancy().getValue())

            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Statistics according to the plan:")

            # Retrieve first resolution bin to check if Chi2 is present
            # Could arrive if Radiation damage is not estimated or double sweep strategy
            bChi2Present = False
            xsDataResolutionBin = xsDataCollectionPlan.getStatisticalPrediction().getResolutionBin()[0]
            if(xsDataResolutionBin.getChi2() is not None):
                bChi2Present = True

            if(bChi2Present == True):
                self.addExecutiveSummaryLine(" Resolution  Compl.       Average     I/Sigma  I/Sigma Chi**2  R-fact  Overload")
                self.addExecutiveSummaryLine("Lower Upper     %   Intensity  Sigma            /Chi             %        %")
                self.addExecutiveSummaryLine("-------------------------------------------------------------------------------")
            else:
                self.addExecutiveSummaryLine(" Resolution  Compl.       Average     I/Sigma   R-fact  Overload")
                self.addExecutiveSummaryLine("Lower Upper     %   Intensity  Sigma               %        %")
                self.addExecutiveSummaryLine("-----------------------------------------------------------------")

            for xsDataResolutionBin in xsDataCollectionPlan.getStatisticalPrediction().getResolutionBin():
                fMinResolution = xsDataResolutionBin.getMinResolution().getValue()
                fMaxResolution = xsDataResolutionBin.getMaxResolution().getValue()
                fCompleteness = xsDataResolutionBin.getCompleteness().getValue()
                fAverageIntensity = xsDataResolutionBin.getAverageIntensity().getValue()
                fAverageSigma = xsDataResolutionBin.getAverageSigma().getValue()
                fIOverSigma = xsDataResolutionBin.getIOverSigma().getValue()
                if(xsDataResolutionBin.getIOverSigmaChi() is not None):
                    fIOverSigmaChi = xsDataResolutionBin.getIOverSigmaChi().getValue()
                if(xsDataResolutionBin.getChi2() is not None):
                    fChi2 = xsDataResolutionBin.getChi2().getValue()
                fRFactor = xsDataResolutionBin.getRFactor().getValue()
                fPercentageOverload = xsDataResolutionBin.getPercentageOverload().getValue()

                if(bChi2Present == True):
                    self.addExecutiveSummaryLine("%5.2f %5.2f %6.1f %7.1f %9.1f %7.1f %7.1f %7.2f %7.1f %7.2f" % \
                                                (fMinResolution, fMaxResolution, (fCompleteness * 100), fAverageIntensity, fAverageSigma, fIOverSigma, \
                                                  fIOverSigmaChi, fChi2, \
                                                  fRFactor, fPercentageOverload))
                else:
                    self.addExecutiveSummaryLine("%5.2f %5.2f %6.1f %7.1f %9.1f %7.1f %9.1f %9.2f" % \
                                                (fMinResolution, fMaxResolution, (fCompleteness * 100), fAverageIntensity, fAverageSigma, fIOverSigma, \
                                                  fRFactor, fPercentageOverload))

            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("")


