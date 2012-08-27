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
__date__ = "20120712"
__status__ = "deprecated"

import os


from EDUtilsPath                     import EDUtilsPath
from EDMessage                       import EDMessage
from EDUtilsFile                     import EDUtilsFile
from EDUtilsTable                    import EDUtilsTable
from EDConfiguration                 import EDConfiguration
from EDPluginExecProcessScript       import EDPluginExecProcessScript

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataTime

from XSDataBestv1_1 import XSDataInputBest
from XSDataBestv1_1 import XSDataResultBest

from XSDataBestv1_1 import XSDataBestCollectionPlan
from XSDataBestv1_1 import XSDataBestStatisticalPrediction
from XSDataBestv1_1 import XSDataBestCollectionRun
from XSDataBestv1_1 import XSDataBestStrategySummary
from XSDataBestv1_1 import XSDataBestResolutionBin

from XSDataDnaTablesBestv1_1 import dna_tables


class EDPluginBestv1_1(EDPluginExecProcessScript):


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)

        self.addCompatibleVersion('Version 3.1.0.d //  26.04.2007')
        self.addCompatibleVersion('Version 3.1.0.d //  16.07.2007')
        self.addCompatibleVersion('Version 3.2.0 //  03.11.2008')

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

        self.setXSDataInputClass(XSDataInputBest)


    def getComplexity(self):
        """
        """
        return self.strComplexity


    def setComplexity(self, _strComplexity):
        """
        """
        self.strComplexity = _strComplexity


    def getBestHome(self):
        """
        """
        return self.strBestHome


    def setBestHome(self, strBestHome):
        """
        """
        self.strBestHome = strBestHome


    def getCommandBestHome(self):
        """
        """
        return self.strCommandBestHome


    def setCommandBestHome(self, _strCommandBestHome):
        """
        """
        self.strCommandBestHome = _strCommandBestHome


    def getCommandBest(self):
        """
        """
        return self.strCommandBest


    def setCommandBest(self, _strCommandBest):
        """
        """
        self.strCommandBest = _strCommandBest


    def getFileBestDat(self):
        """
        """
        return self.strPathToBestDatFile


    def setFileBestDat(self, _edFileBestDat):
        """
        """
        self.strPathToBestDatFile = _edFileBestDat


    def getFileBestPar(self):
        """
        """
        return self.strPathToBestParFile


    def setFileBestPar(self, _edFileBestPar):
        """
        """
        self.strPathToBestParFile = _edFileBestPar


    def getListFileBestHKL(self):
        """
        """
        return self.listFileBestHKL


    def setListFileBestHKL(self, _listFileBestHKL):
        """
        """
        self.listFileBestHKL = _listFileBestHKL


    def configure(self):
        """
        """
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginBestv1_1.configure")
        self.setRequireCCP4(True)
        strScriptExecutable = self.getScriptExecutable()
        self.DEBUG("EDPluginBestv1_1.configure: Script Executable: " + strScriptExecutable)
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
        self.DEBUG("EDPluginBestv1_1.configure: Best Home: " + strBestHome)
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

        if(self.getDataInput().getTransmission() is not None):
            strTransmission = str(self.getDataInput().getTransmission().getValue()*100.0)
            self.strCommandBest = self.strCommandBest + "-Trans " + strTransmission + " "

        if(self.getDataInput().getAnomalousData() is not None):
            bAnomalousData = self.getDataInput().getAnomalousData().getValue()
            if (bAnomalousData):
                self.strCommandBest = self.strCommandBest + "-a "

        self.strCommandBest = self.strCommandBest + "-T " + strMaxExposureTime + " " + \
                                     "-dna " + self.getScriptBaseName() + "_dnaTables.xml" + " " + \
                                     "-o " + self.getScriptBaseName() + "_plots.mtv " + \
                                     "-e " + self.getComplexity() + " " + \
                                     "-mos " + self.getFileBestDat() + " " + self.getFileBestPar() + " " + listFileBestHKLCommand

        self.setScriptCommandline(self.strCommandBest)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)

        strError = self.readProcessErrorLogFile()
        if((strError is not None) and (strError != "")):
            pyStrErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginBestv1_1.postProcess', 'EDPluginBestv1_1', strError)
            self.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)
            raise RuntimeError, pyStrErrorMessage

        outputData = self.getOutputDataFromDNATableFile(os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_dnaTables.xml"))
        self.setDataOutput(outputData)


    def getOutputDataFromDNATableFile(self, _strFileName):
        xsDataResultBest = XSDataResultBest()
        strDnaTablesXML = self.readProcessFile(_strFileName)
        xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
        # Loop through all the tables and fill in the relevant parts of xsDataResultBest

        # SubWedges
        xsTablesCollectionStrategy = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "data_collection_strategy")

        iCollectionPlanNumber = 1
        for xsTableCollectionStrategy in xsTablesCollectionStrategy:

            xsDataBestCollectionPlan = XSDataBestCollectionPlan()
            xsCollectionRunList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "collection_run")

            iCollectionRunNumber = 1
            for xsCollectionRunItemList in xsCollectionRunList:
                xsDataCollectionRun = self.collectionRunItemListToCollectionRun(xsCollectionRunItemList)
                xsDataCollectionRun.setCollectionRunNumber(XSDataInteger(iCollectionRunNumber))
                xsDataBestCollectionPlan.addCollectionRun(xsDataCollectionRun)
                iCollectionRunNumber = iCollectionRunNumber + 1


            # Strategy Summary
            xsStrategySummaryItemList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "summary")
            xsDataStrategySummary = self.strategySummaryItemListToStrategySummary(xsStrategySummaryItemList[0])
            # Ranking Resolution
            # Not part of strategySummaryItemListToStrategySummary method since it is in the general_form part
            xsTableGeneralInform = EDUtilsTable.getTableFromTables(xsDataDnaTables, "general_inform")
            xsRankingResolutionItemList = EDUtilsTable.getListsFromTable(xsTableGeneralInform, "ranking_resolution")
            xsItemRankingResolution = EDUtilsTable.getItemFromList(xsRankingResolutionItemList[0], "dmin")
            fRankingResolution = float(xsItemRankingResolution.getValueOf_())
            xsDataStrategySummary.setRankingResolution(XSDataDouble(fRankingResolution))

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

            xsDataBestCollectionPlan.setCollectionPlanNumber(XSDataInteger(iCollectionPlanNumber))
            xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)
            iCollectionPlanNumber = iCollectionPlanNumber + 1

        # Fix the order of the collection plans - then low resolution pass should be the first one
        listCollectionPlan = xsDataResultBest.getCollectionPlan()
        if (len(listCollectionPlan) > 1):
            bIsModified = False
            for xsDataCollectionPlan in listCollectionPlan:
                xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                strReasoning = xsDataStrategySummary.getResolutionReasoning().getValue()
                if (strReasoning.find("Low-resolution") != -1) and (xsDataCollectionPlan.getCollectionPlanNumber().getValue() != 1):
                    listCollectionPlan.remove(xsDataCollectionPlan)
                    listCollectionPlan.insert(0, xsDataCollectionPlan)
                    bIsModified = True
            if (bIsModified):
                iCollectionPlanNumber = 1
                for xsDataCollectionPlan in listCollectionPlan:
                    xsDataCollectionPlan.setCollectionPlanNumber(XSDataInteger(iCollectionPlanNumber))
                    iCollectionPlanNumber = iCollectionPlanNumber + 1



        return xsDataResultBest


    def collectionRunItemListToCollectionRun(self, _xsCollectionRunItemList):
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
        xsDataStrategySummary.setAttenuation(XSDataDouble(fAttenuation))

        pyStrItemCompleteness = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "completeness")
        # For homegeneity concerns, EDNA data model should store all the completeness value in fraction
        # ( DNA table xml file stores the summary strategy completeness in percentage whereas
        # the resolution bin completeness are in fraction )
        fCompleteness = float(pyStrItemCompleteness.getValueOf_()) / 100
        xsDataStrategySummary.setCompleteness(XSDataDouble(fCompleteness))

        pyStrItemISigma = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "i_sigma")
        fISigma = float(pyStrItemISigma.getValueOf_())
        xsDataStrategySummary.setISigma(XSDataDouble(fISigma))

        pyStrItemRedundancy = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "redundancy")
        fRedundancy = float(pyStrItemRedundancy.getValueOf_())
        xsDataStrategySummary.setRedundancy(XSDataDouble(fRedundancy))

        pyStrItemResolution = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "resolution")
        fResolution = float(pyStrItemResolution.getValueOf_())
        xsDataStrategySummary.setResolution(XSDataDouble(fResolution))

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
        """
        """
        xsDataResolutionBin = XSDataBestResolutionBin()

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "min_resolution")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setMinResolution(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "max_resolution")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setMaxResolution(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "completeness")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setCompleteness(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "redundancy")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setRedundancy(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_intensity")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setAverageIntensity(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_error")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setAverageSigma(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setIOverSigma(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "R_factor")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setRFactor(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "Chi**2")
        if (pyStrItem is not None):
            fItem = float(pyStrItem.getValueOf_())
            xsDataResolutionBin.setChi2(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma_Chi**2")
        if (pyStrItem is not None):
            fItem = float(pyStrItem.getValueOf_())
            xsDataResolutionBin.setIOverSigmaChi(XSDataDouble(fItem))

        pyStrItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "fract_overload")
        fItem = float(pyStrItem.getValueOf_())
        xsDataResolutionBin.setPercentageOverload(XSDataDouble(fItem))

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
        self.DEBUG("EDPluginBestv1_1.generateExecutiveSummary")
        if (self.getStringVersion() is not None):
            self.addExecutiveSummaryLine(self.getStringVersion())

        xsDataInputBest = self.getDataInput()
        xsDataResultBest = self.getDataOutput()
        listCollectionPlan = xsDataResultBest.getCollectionPlan()
        self.addExecutiveSummaryLine("Input parameters:")
        self.addExecutiveSummaryLine("=================")
        # Aimed completeness
        if (xsDataInputBest.getAimedCompleteness() is not None):
            self.addExecutiveSummaryLine("Aimed completeness            : %6.1f [%%]" % (xsDataInputBest.getAimedCompleteness().getValue()*100.0))
        # Aimed I over Sigma
        if (xsDataInputBest.getAimedIOverSigma() is not None):
            self.addExecutiveSummaryLine("Aimed I over Sigma            : %6.1f" % xsDataInputBest.getAimedIOverSigma().getValue())
        # Aimed Redundancy
        if (xsDataInputBest.getAimedRedundancy() is not None):
            self.addExecutiveSummaryLine("Aimed Redundancy              : %6.1f" % xsDataInputBest.getAimedRedundancy().getValue())
        # Aimed Resolution
        if (xsDataInputBest.getAimedResolution() is not None):
            self.addExecutiveSummaryLine("Aimed Resolution              : %6.1f [A]" % xsDataInputBest.getAimedResolution().getValue())
        # Anomalous Data
        if (xsDataInputBest.getAnomalousData() is not None):
            if (xsDataInputBest.getAnomalousData().getValue()):
                self.addExecutiveSummaryLine("Anomalous data                :   True")
            else:
                self.addExecutiveSummaryLine("Anomalous data                :  False")
        else:
            self.addExecutiveSummaryLine("Anomalous data                :  False")
        # Beam exposure time
        if (xsDataInputBest.getBeamExposureTime() is not None):
            self.addExecutiveSummaryLine("Beam exposure time            : %6.1f [s]" % xsDataInputBest.getBeamExposureTime().getValue())
        # Beam max exposure time
        if (xsDataInputBest.getBeamMaxExposureTime() is not None):
            self.addExecutiveSummaryLine("Beam max exposure time        : %6.1f [s]" % xsDataInputBest.getBeamMaxExposureTime().getValue())
        # Beam min exposure time
        if (xsDataInputBest.getBeamMinExposureTime() is not None):
            self.addExecutiveSummaryLine("Beam min exposure time        : %6.1f [s]" % xsDataInputBest.getBeamMinExposureTime().getValue())
        # Transmission
        if (xsDataInputBest.getTransmission() is not None):
            self.addExecutiveSummaryLine("Transmission                  : %6.1f [%%]" % (xsDataInputBest.getTransmission().getValue()*100.0))
        # Strategy complexity
        if self.getComplexity() == "none":
            self.addExecutiveSummaryLine("Best strategy complexity      : Single sub wedge")
        elif self.getComplexity() == "min":
            self.addExecutiveSummaryLine("Best strategy complexity      : Few sub wedges")
        elif self.getComplexity() == "full":
            self.addExecutiveSummaryLine("Best strategy complexity      : Many sub wedge")
        else:
            self.addExecutiveSummaryLine("Unknown best strategy complexity! : %s" % self.getComplexity())
        # Crystal absorbed dose rate
        if (xsDataInputBest.getCrystalAbsorbedDoseRate() is not None):
            self.addExecutiveSummaryLine("Crystal absorbed dose rate    : %6.1f" % xsDataInputBest.getCrystalAbsorbedDoseRate().getValue())
        # Crystal shape
        if (xsDataInputBest.getCrystalShape() is not None):
            self.addExecutiveSummaryLine("Crystal shape                 : %6.1f" % xsDataInputBest.getCrystalShape().getValue())
        # Crystal susceptibilty
        if (xsDataInputBest.getCrystalSusceptibility() is not None):
            self.addExecutiveSummaryLine("Crystal susceptibilty         : %6.1f" % xsDataInputBest.getCrystalSusceptibility().getValue())
        # Detector type
        if (xsDataInputBest.getDetectorType() is not None):
            self.addExecutiveSummaryLine("Detector type                 : %6s" % xsDataInputBest.getDetectorType().getValue())
        # Goniostat max rotation speed
        if (xsDataInputBest.getGoniostatMaxRotationSpeed() is not None):
            self.addExecutiveSummaryLine("Goniostat max rotation speed  : %6.1f [degree/s]" % xsDataInputBest.getGoniostatMaxRotationSpeed().getValue())
        # Goniostat min rotation width
        if (xsDataInputBest.getGoniostatMinRotationWidth() is not None):
            self.addExecutiveSummaryLine("Goniostat min rotation width  : %6.1f [degree]" % xsDataInputBest.getGoniostatMinRotationWidth().getValue())

        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("Results:")
        self.addExecutiveSummaryLine("========")

        if(len(listCollectionPlan) > 1):
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("MULTI-SWEEP COLLECTION PLAN STRATEGY:")
            self.addExecutiveSummaryLine("------------------------------------")
            self.addExecutiveSummaryLine("")

        for xsDataCollectionPlan in listCollectionPlan:

            if(len(listCollectionPlan) > 1):

                self.addExecutiveSummaryLine("SWEEP %d:" % xsDataCollectionPlan.getCollectionPlanNumber().getValue())
                self.addExecutiveSummaryLine("---------------------------------------------------------------------------------------")

            xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
            self.addExecutiveSummaryLine("Resolution reasoning          : %s" % xsDataStrategySummary.getResolutionReasoning().getValue())
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Plan for data collection:")
            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine(" N |  Phi_start |  N.of.images | Rot.width |  Exposure | Distance |  Overlap |")
            iTotalImages = 0
            fTotalRotationRange = 0.0
            for xsDataCollectionRun in xsDataCollectionPlan.getCollectionRun():
                iCollectionRunNumber = xsDataCollectionRun.getCollectionRunNumber().getValue()
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
                iTotalImages += iNumberOfImages
                fTotalRotationRange += fPhiWidth * iNumberOfImages


            self.addExecutiveSummaryLine("")
            self.addExecutiveSummaryLine("Transmission                  : %6.3f" % xsDataStrategySummary.getAttenuation().getValue())
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


