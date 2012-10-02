#
#    Project: EDNA MXv2
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

import math, os

from EDVerbose                         import EDVerbose
from EDPluginControl                   import EDPluginControl
from EDMessage                         import EDMessage
from EDConfiguration                   import EDConfiguration
from EDUtilsSymmetry                   import EDUtilsSymmetry
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon                      import XSDataString
from XSDataCommon                      import XSDataFloat

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1                        import XSDataInputStrategy
from XSDataMXv1                        import XSDataSampleCrystalMM
from XSDataMXv1                        import XSDataAtom
from XSDataMXv1                        import XSDataAtomicComposition
from XSDataMXv1                        import XSDataChain
from XSDataMXv1                        import XSDataStructure
from XSDataMXv1                        import XSDataSolvent
from XSDataMXv1                        import XSDataChemicalCompositionMM
from XSDataMXv1                        import XSDataInputStrategy

EDFactoryPluginStatic.loadModule("XSDataSTACv2_0")
from XSDataSTACv2_0 import kappa_strategy_request
from XSDataSTACv2_0 import kappa_strategy_response
from XSDataSTACv2_0 import strategy_request


class EDPluginControlKappaStrategyv2_0(EDPluginControl):
    """
    The Plugin that controls the strategy step
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        #self.setXSDataInputClass(EDList)

        self.setRequiredToHaveConfiguration(True)

        self.strPluginRaddoseName = "EDPluginRaddosev10"
        self.edPluginRaddose = None
        self.edHandlerXSDataRaddose = None

        self.strPluginBestName = "EDPluginBestv1_2"
        self.edPluginBest = None
        from EDHandlerXSDataBestv1_2    import EDHandlerXSDataBestv1_2
        self.edHandlerXSDataBest = EDHandlerXSDataBestv1_2()

        self.strPluginAlignmentName = "EDPluginSTACAlignmentv2_0"
        self.edPluginAlignment = None
        self.edHandlerXSDataAlignment = None

        self.strPluginKappaStrategyName = "EDPluginSTACStrategyv2_0"
        self.edPluginKappaStrategy = None
        self.edHandlerXSDataKappaStrategy = None

        self.setXSDataInputClass(XSDataInputStrategy, "mxv1InputStrategy")
        EDFactoryPluginStatic.loadModule("XSDataMXv2")
        import XSDataMXv2
        self.setXSDataInputClass(XSDataMXv2.XSDataCollection, "mxv2DataCollection")
        import XSDataMXv1
        self.setXSDataInputClass(XSDataMXv1.XSDataIndexingResult, "mxv1IndexingResult")

        #disable kappa by default
        self.KappaStrategy = 0

        self.strCONF_SYMOP_HOME = "symopHome"
        # Default value for the location of the symop table
        self.strSymopHome = os.path.normpath("/opt/pxsoft/ccp4-6.0.2/lib/data")

        self.xsDataSampleCopy = None

        # For default chemical composition
        self.fAverageAminoAcidVolume = 135.49
        self.fAverageCrystalSolventContent = 0.47
        self.fAverageSulfurContentPerAminoacid = 0.05
        self.fAverageSulfurConcentration = 314


    def setSymopHome(self, _strSymopHome):
        self.strSymopHome = _strSymopHome


    def getSymopHome(self):
        return self.strSymopHome


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.preProcess...")
        self.edPluginRaddose = None

        xsDataSampleCrystalMM = self.getDataInput("mxv1InputStrategy")[0].getSample()

        if(xsDataSampleCrystalMM is None):
            self.xsDataSampleCopy = XSDataSampleCrystalMM()

        else:
            strXmlStringDataSample = xsDataSampleCrystalMM.marshal()
            self.xsDataSampleCopy = XSDataSampleCrystalMM.parseString(strXmlStringDataSample)

        xsDataCrystal = self.getDataInput("mxv1InputStrategy")[0].getCrystalRefined()
        if(xsDataCrystal is not None):
            self.xsDataSampleCopy.setCrystal(xsDataCrystal)

        # Raddose is enabled only if the beam flux is set
        if(self.getDataInput("mxv1InputStrategy")[0].getExperimentalCondition().getBeam().getFlux() is None):
            strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginRaddoseName, "Beam Flux not set")
            EDVerbose.warning(strWarningMessage)
            self.addWarningMessage(strWarningMessage)

        else:
            self.edPluginRaddose = self.loadPlugin(self.strPluginRaddoseName)

            if (self.edPluginRaddose is not None):
                EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.preProcess: " + self.strPluginRaddoseName + " Found... setting Data Input")

                strFileSymop = os.path.join(self.getSymopHome(), "symop.lib")

                xsDataStringSpaceGroup = self.getDataInput("mxv1InputStrategy")[0].getDiffractionPlan().getForcedSpaceGroup()
                # Space Group has been forced
                # Prepare chemical composition calculation with the forced Space Group (Space Group Name)
                strNumOperators = None
                strSpaceGroup = None
                if(xsDataStringSpaceGroup is not None):
                    strSpaceGroup = xsDataStringSpaceGroup.getValue()
                    EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.preProcess: Forced Space Group Found: " + strSpaceGroup)
                    try:
                        strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroup, strFileSymop)
                    except Exception, detail:
                        strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', "Problem to calculate Number of symmetry operators", detail)
                        EDVerbose.error(strErrorMessage)
                        self.addErrorMessage(strErrorMessage)
                        raise RuntimeError, strErrorMessage
                # Space Group has NOT been forced
                else:
                    xsDataStringSpaceGroup = self.xsDataSampleCopy.getCrystal().getSpaceGroup().getName()
                    if (xsDataStringSpaceGroup is not None):
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group Name)
                        strSpaceGroup = self.xsDataSampleCopy.getCrystal().getSpaceGroup().getName().getValue()
                        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.preProcess: Space Group IT Name found by indexing: " + strSpaceGroup)
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupName(strSpaceGroup, strFileSymop)
                        except Exception, detail:
                            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(strErrorMessage)
                            self.addErrorMessage(strErrorMessage)
                            raise RuntimeError, strErrorMessage
                    else:
                        # Prepare chemical composition calculation with the Space Group calculated by indexing (Space Group IT number)
                        dSpaceGroupITNumber = self.xsDataSampleCopy.getCrystal().getSpaceGroup().getITNumber().getValue()
                        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.preProcess: Space Group IT Number Found by indexing: %d" % dSpaceGroupITNumber)
                        try:
                            strNumOperators = EDUtilsSymmetry.getNumberOfSymmetryOperatorsFromSpaceGroupITNumber(str(dSpaceGroupITNumber), strFileSymop)
                        except Exception, detail:
                            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', "Problem to calculate Number of symmetry operators", detail)
                            EDVerbose.error(strErrorMessage)
                            self.addErrorMessage(strErrorMessage)
                            raise RuntimeError, strErrorMessage

                if(strNumOperators is not None):
                    iNumOperators = int(strNumOperators)
                else:
                    strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', "No symmetry operators found for Space Group: ", strSpaceGroup)
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    raise RuntimeError, strErrorMessage

                xsDataChemicalComposition = self.xsDataSampleCopy.getChemicalComposition()

                if(xsDataChemicalComposition is None):
                    # create a default chemical composition and assign it to the sample
                    xsDataDefaultChemicalComposition = self.getDefaultChemicalComposition(self.xsDataSampleCopy, iNumOperators)
                    self.xsDataSampleCopy.setChemicalComposition(xsDataDefaultChemicalComposition)
                else:
                    # Check for Sulfur atoms, if none, add native sulfur atoms
                    xsDataUpdatedChemicalComposition = self.updateChemicalComposition(xsDataChemicalComposition)
                    self.xsDataSampleCopy.setChemicalComposition(xsDataUpdatedChemicalComposition)

                # create Data Input for Raddose
                from EDHandlerXSDataRaddosev10 import EDHandlerXSDataRaddosev10
                self.edHandlerXSDataRaddose = EDHandlerXSDataRaddosev10()
                xsDataBeam = self.getDataInput("mxv1InputStrategy")[0].getExperimentalCondition().getBeam()

                xsDataRaddoseInput = None

                try:
                    xsDataRaddoseInput = self.edHandlerXSDataRaddose.getXSDataRaddoseInput(xsDataBeam, self.xsDataSampleCopy, iNumOperators)

                except Exception, detail:
                    strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginRaddoseName, "EDHandlerXSDataRaddose : " + detail)
                    EDVerbose.warning(strWarningMessage)
                    self.addWarningMessage(strWarningMessage)

                if(xsDataRaddoseInput is not None):
                    self.edPluginRaddose.setDataInput(xsDataRaddoseInput)
                    self.edPluginRaddose.setBaseDirectory(self.getWorkingDirectory())
                    self.edPluginRaddose.setBaseName(self.strPluginRaddoseName)

                    # More checks?
#                    try:
#                        self.edPluginRaddose.setDataInput( xsDataRaddoseInput )
#                        self.edPluginRaddose.setBaseDirectory( self.getWorkingDirectory() )
#                        self.edPluginRaddose.setBaseName( self.strPluginRaddoseName )
#                        
#                    except Exception, detail:
#                        strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlStrategyv1_1.preProcess', self.strPluginRaddoseName,  detail ) )
#                        EDVerbose.warning( strWarningMessage )
#                        self.addWarningMessage( strWarningMessage )

            else:
                strErrorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginRaddoseName)
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage

        self.edPluginBest = self.loadPlugin(self.strPluginBestName)
        if (self.edPluginBest is None):
            strErrorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginBestName)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        else:
            self.edPluginBest.setBaseDirectory(self.getWorkingDirectory())
            self.edPluginBest.setBaseName(self.strPluginBestName)

        if (self.KappaStrategy):
            #Alignment
            self.edPluginAlignment = self.loadPlugin(self.strPluginAlignmentName)
            if (self.edPluginAlignment is None):
                errorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginAlignmentName)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                #do not kill the application just because this feature is not available
                #raise RuntimeError, errorMessage
            else:
                self.edPluginAlignment.setBaseDirectory(self.getWorkingDirectory())
                self.edPluginAlignment.setBaseName(self.strPluginAlignmentName)

            #KappaStaregy
            self.edPluginKappaStrategy = self.loadPlugin(self.strPluginKappaStrategyName)
            if (self.edPluginKappaStrategy is None):
                errorMessage = EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDPluginControlKappaStrategyv2_0.preProcess', self.strPluginKappaStrategyName)
                EDVerbose.error(errorMessage)
                self.addErrorMessage(errorMessage)
                #raise RuntimeError, errorMessage
            else:
                self.edPluginKappaStrategy.setBaseDirectory(self.getWorkingDirectory())
                self.edPluginKappaStrategy.setBaseName(self.strPluginKappaStrategyName)


    def configure(self):
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.configure")
        pluginConfiguration = self.getConfiguration()

        if pluginConfiguration != None:
            strSymopHome = EDConfiguration.getStringParamValue(pluginConfiguration, self.strCONF_SYMOP_HOME)
            if(strSymopHome == None):
                strWarningMessage = EDMessage.WARNING_NO_PARAM_CONFIGURATION_ITEM_FOUND_03 % ('EDPluginControlKappaStrategyv2_0.configure', self.strCONF_SYMOP_HOME, self.getPluginName())
                EDVerbose.warning(strWarningMessage)
                self.addWarningMessage(strWarningMessage)
            else:
                strSymopHomeNorm = os.path.normpath(strSymopHome)
                self.setSymopHome(strSymopHomeNorm)

            strKappaOn = EDConfiguration.getStringParamValue(pluginConfiguration, "KAPPA")
            if(strKappaOn == None or strKappaOn != "True"):
                #self.strPluginStrategyName = "EDPluginControlStrategyv10"
                #self.strPluginStrategyName = "EDPluginControlStrategyv2_0"
                self.KappaStrategy = 0
            else:
                self.KappaStrategy = 1


    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.process...")

        # In case Beam Flux has not been set, The plugin Raddose has not been created, so it could be None
        # and it won't be launched in this case
        if(self.edPluginRaddose is not None):
            self.connectProcess(self.edPluginRaddose.executeSynchronous)
            self.edPluginRaddose.connectSUCCESS(self.doRaddoseToBestTransition)
            self.edPluginRaddose.connectFAILURE(self.doFailureActionRaddose)
        else:
            # The plugin Best should not be None as this has been checked in the preProcess method... Double check it anyway
            if(self.edPluginBest is not None):
                self.connectProcess(self.executeBest)

        # Launches Best anyway whether Raddose has been launched or not
        # The plugin Best should not be None as this has been checked in the preProcess method... Double check it anyway
        if(self.edPluginBest is not None):
            self.edPluginBest.connectSUCCESS(self.doSuccessActionBest)
            self.edPluginBest.connectFAILURE(self.doFailureActionBest)

        # Kappa strategy calculation
        if self.hasDataInput("mxv2DataCollection"):
            if self.edPluginAlignment is not None:
                self.connectProcess(self.doBestToAlignmentTransition)
#                self.edPluginAlignment.connectSUCCESS( self.doAlignmentToKappaStrategyTransition )
#                self.edPluginAlignment.connectFAILURE( self.doFailureActionAlignment )
#                self.edPluginKappaStrategy.connectSUCCESS( self.doKappaStrategyMerge )
#                self.edPluginKappaStrategy.connectFAILURE( self.doFailureActionKappaStrategy )

            # Kappa strategy calculation
            if self.edPluginKappaStrategy is not None:
                self.connectProcess(self.doAlignmentToStrategyTransition)
#                self.edPluginKappaStrategy.connectSUCCESS( self.doKappaStrategyMerge )
#                self.edPluginKappaStrategy.connectFAILURE( self.doFailureActionKappaStrategy )


    def postProcess(self, _edObject=None):
        """
        """
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.postProcess...")

        xsDataResultBest = self.edPluginBest.getDataOutput()
        xsDataResultStrategy = None

        if(xsDataResultBest is not None):
            xsDataResultStrategy = self.edHandlerXSDataBest.getXSDataResultStrategy(xsDataResultBest, self.getDataInput("mxv1InputStrategy")[0].getExperimentalCondition(), self.xsDataSampleCopy)

        self.setDataOutput(xsDataResultStrategy)

        #possibleAlignments
        try:
            self.setDataOutput(self.edPluginAlignment.getDataOutput(), "possibleOrientations")
        except:
            EDVerbose.WARNING("Could not get the list of Possible orientations.")


    def doRaddoseToBestTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doRaddoseToBestTransition")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlKappaStrategyv2_0.doRaddoseToBestTransition")

        xsDataRaddoseOutput = self.edPluginRaddose.getDataOutput()

        # update the strategy data with the data coming from Raddose
        self.xsDataSampleCopy.setAbsorbedDoseRate(xsDataRaddoseOutput.getAbsorbedDoseRate())

        # Call the Best Translator layer

        xsDataInputStrategyCopy = XSDataInputStrategy.parseString(self.getDataInput("mxv1InputStrategy")[0].marshal())
        xsDataInputStrategyCopy.setSample(self.xsDataSampleCopy)

        xsDataInputBest = self.edHandlerXSDataBest.getXSDataInputBest(xsDataInputStrategyCopy)

        self.edPluginBest.setDataInput(xsDataInputBest)
        self.edPluginBest.executeSynchronous()

    def doBestToAlignmentTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doBestToAlignmentTransition")
        #self.retrieveSuccessMessages( _edPlugin, "EDPluginControlStrategyv01.doRaddoseToBestTransition" )


        xsDataInputStrategyCopy = XSDataInputStrategy.parseString(self.getDataInput("mxv1InputStrategy")[0].marshal())
        xsDataInputStrategyCopy.setSample(self.xsDataSampleCopy)

        xsDataInputBest = self.edHandlerXSDataBest.getXSDataInputBest(xsDataInputStrategyCopy)

        #xsDataAlignmentInput=EDList()
        #xsDataAlignmentInput.add(xsDataBestInput)
        ##data collection descriptor
        #xsDataAlignmentInput.add(self.getDataInput("mxv2DataCollection")[0])
        ##indexing result
        #xsDataAlignmentInput.add(self.getDataInput("mxv1Indexingresult")[0])
        #self.edPluginAlignment.setDataInput( xsDataAlignmentInput )
        self.edPluginAlignment.setDataInput(xsDataInputBest, "inputBest")
        self.edPluginAlignment.setDataInput(self.getDataInput("mxv2DataCollection")[0], "dataCollection")
        self.edPluginAlignment.setDataInput(self.getDataInput("mxv1IndexingResult")[0], "indexingResult")


        self.edPluginAlignment.executeSynchronous()


    def doAlignmentToStrategyTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doAlignmentToStrategy")
        #self.retrieveSuccessMessages( _edPlugin, "EDPluginControlStrategyv01.doRaddoseToBestTransition" )

        # Call the Best Translator layer
        #from XSDataSTACv01 import kappa_alignment_response
        #from XSDataSTACv01 import kappa_strategy_request
        #from XSDataSTACv01 import strategy_request

        self.xsKappaStrategyRequest = kappa_strategy_request()
        #self.xsKappaStrategyRequest.build(???)      

        KappaAlignmentResponse = self.edPluginAlignment.getDataOutput()
        xsDataKappaAlignmentList = KappaAlignmentResponse.getPossible_orientation()
        self.xsKappaStrategyRequest.setDesired_datum(xsDataKappaAlignmentList)

        self.xsksreq = strategy_request()
        self.xsKappaStrategyRequest.setStandard_request(self.xsksreq)

        #xsDataKappaStrategyInput=EDList()
        #xsDataKappaStrategyInput.add(self.xsKappaStrategyRequest)
        ##data collection descriptor
        #xsDataKappaStrategyInput.add(self.getDataInput("mxv2DataCollection")[0])
        ##indexing result
        #xsDataKappaStrategyInput.add(self.getDataInput("mxv1IndexingResult")[0])
        ##bestfile
        #xsDataKappaStrategyInput.add(self.getDataInput("mxv1InputStrategy")[0])
        #self.edPluginKappaStrategy.setDataInput( xsDataKappaStrategyInput )
        self.edPluginKappaStrategy.setDataInput(self.xsKappaStrategyRequest, "kappa_strategy_request")
        self.edPluginKappaStrategy.setDataInput(self.getDataInput("mxv2DataCollection")[0], "dataCollection")
        self.edPluginKappaStrategy.setDataInput(self.getDataInput("mxv1InputStrategy")[0], "inputBest")

        #self.edPluginKappaStrategy.m_xsDataBestFileContentPar=self.getDataInput()[0].getBestFileContentPar()
        self.edPluginKappaStrategy.executeSynchronous()


    def doFailureActionRaddose(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doFailureActionRaddose")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlKappaStrategyv2_0.doFailureActionRaddose")
        strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlKappaStrategyv2_0.doFailureActionRaddose', self.strPluginRaddoseName, "Raddose failure")
        EDVerbose.warning(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        self.executeBest(self)


    def executeBest(self, _edPlugin):
        xsDataInputBest = None
        # Call the Best Translator layer

        from EDHandlerXSDataBestv1_2    import EDHandlerXSDataBestv1_2
        self.__edHandlerXSDataBest = EDHandlerXSDataBestv1_2()
        xsDataInputStrategyCopy = XSDataInputStrategy.parseString(self.getDataInput("mxv1InputStrategy")[0].marshal())
        xsDataInputStrategyCopy.setSample(self.xsDataSampleCopy)
        xsDataInputBest = self.__edHandlerXSDataBest.getXSDataInputBest(xsDataInputStrategyCopy)
        self.edPluginBest.setDataInput(xsDataInputBest)
        self.edPluginBest.executeSynchronous()


    def doSuccessActionBest(self, _edPlugin):
        """
        retrieve the potential warning messages
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doSuccessActionBest")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlKappaStrategyv2_0.doSuccessActionBest")


    def doFailureActionBest(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.doFailureActionBest")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlKappaStrategyv2_0.doFailureActionBest")


    def getDefaultChemicalComposition(self, _xsDataSample, _inumOperators):
        """
        """
        xsDataCell = _xsDataSample.getCrystal().getCell()
        a = xsDataCell.getLength_a().getValue()
        b = xsDataCell.getLength_b().getValue()
        c = xsDataCell.getLength_c().getValue()
        alpha = math.radians(xsDataCell.getAngle_alpha().getValue())
        beta = math.radians(xsDataCell.getAngle_beta().getValue())
        gamma = math.radians(xsDataCell.getAngle_gamma().getValue())

        fUnitCellVolume = a * b * c * (math.sqrt(1 - math.cos(alpha) * math.cos(alpha) - math.cos(beta) * math.cos(beta) - math.cos(gamma) * math.cos(gamma) + 2 * math.cos(alpha) * math.cos(beta) * math.cos(gamma)))
        fPolymerVolume = fUnitCellVolume * (1 - self.fAverageCrystalSolventContent)
        fNumberOfMonomersPerUnitCell = fPolymerVolume / self.fAverageAminoAcidVolume
        fNumberOfMonomersPerAsymmetricUnit = fNumberOfMonomersPerUnitCell / _inumOperators
        iNumberOfSulfurAtom = int(round(fNumberOfMonomersPerAsymmetricUnit * self.fAverageSulfurContentPerAminoacid))

        xsDataAtom = XSDataAtom()
        xsDataAtom.setSymbol(XSDataString("S"))
        xsDataAtom.setNumberOf(XSDataFloat(iNumberOfSulfurAtom))
        xsDataAtomicComposition = XSDataAtomicComposition()
        xsDataAtomicComposition.addAtom(xsDataAtom)

        xsDataChain = XSDataChain()
        xsDataChain.setType(XSDataString("protein"))
        xsDataChain.setNumberOfMonomers(XSDataFloat(round(fNumberOfMonomersPerAsymmetricUnit)))
        xsDataChain.setNumberOfCopies(XSDataFloat(1))
        xsDataChain.setHeavyAtoms(xsDataAtomicComposition)

        xsDataStructure = XSDataStructure()
        xsDataStructure.addChain(xsDataChain)
        xsDataStructure.setNumberOfCopiesInAsymmetricUnit(XSDataFloat(1))

        xsDataAtomSolvent = XSDataAtom()
        xsDataAtomSolvent.setSymbol(XSDataString("S"))
        xsDataAtomSolvent.setConcentration(XSDataFloat(self.fAverageSulfurConcentration))
        xsDataAtomicCompositionSolvent = XSDataAtomicComposition()
        xsDataAtomicCompositionSolvent.addAtom(xsDataAtomSolvent)
        xsDataSolvent = XSDataSolvent()
        xsDataSolvent.setAtoms(xsDataAtomicCompositionSolvent)

        xsDataChemicalCompositionMM = XSDataChemicalCompositionMM()
        xsDataChemicalCompositionMM.setSolvent(xsDataSolvent)
        xsDataChemicalCompositionMM.setStructure(xsDataStructure)

        return xsDataChemicalCompositionMM

    def updateChemicalComposition(self, _xsDataChemicalComposition):
        """
        """
        xsDataChemicalComposition = _xsDataChemicalComposition

        for chain in xsDataChemicalComposition.getStructure().getChain():
            if(chain.getType().getValue() == "protein"):
                bSulfurExists = False
                xsDataAtomicCompositionHeavyAtoms = chain.getHeavyAtoms()
                if(xsDataAtomicCompositionHeavyAtoms is None):
                    xsDataAtomicCompositionHeavyAtoms = XSDataAtomicComposition()
                else:
                    for heavyAtom in xsDataAtomicCompositionHeavyAtoms.getAtom():
                        if(heavyAtom.getSymbol().getValue() == "S" or heavyAtom.getSymbol().getValue() == "s"):
                            bSulfurExists = True

                # all protein chains should contain sulfur atom as a percentage of the number
                # of amino acids. Add them if the user did not input them.
                if(bSulfurExists == False):
                    iNumberOfSulfurAtom = int(round(chain.getNumberOfMonomers().getValue() * 0.05))
                    xsDataSulfurAtom = XSDataAtom()
                    xsDataSulfurAtom.setSymbol(XSDataString("S"))
                    xsDataSulfurAtom.setNumberOf(XSDataFloat(iNumberOfSulfurAtom))
                    xsDataAtomicCompositionHeavyAtoms.addAtom(xsDataSulfurAtom)
                    chain.setHeavyAtoms(xsDataAtomicCompositionHeavyAtoms)

        return xsDataChemicalComposition


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDVerbose.DEBUG("EDPluginControlKappaStrategyv2_0.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of Strategy:")
        self.addErrorWarningMessagesToExecutiveSummary()

        xsDataResultStrategy = self.getDataOutput()

        if (self.edPluginRaddose is not None):
            if (self.edPluginRaddose.getDataOutput() is not None):
                self.appendExecutiveSummary(self.edPluginRaddose, "Raddose : ")
                self.addExecutiveSummaryLine("")
                self.addExecutiveSummaryLine("Calculations assuming polymer crystal with:")
                self.addExecutiveSummaryLine("------------------------------------------")
                self.addExecutiveSummaryLine("")

                xsDataStructure = xsDataResultStrategy.getCollectionPlan()[0].getCollectionStrategy().getSample().getChemicalComposition().getStructure()

                self.addExecutiveSummaryLine("Number of structure copies in asymmetric unit: %.2f" % xsDataStructure.getNumberOfCopiesInAsymmetricUnit().getValue())
                self.addExecutiveSummaryLine("")

                chains = xsDataStructure.getChain()
                self.addExecutiveSummaryLine("Chains:")
                for chain in chains:
                    strChainType = chain.getType().getValue()
                    self.addExecutiveSummaryLine("    Type                           : %s" % strChainType)
                    if(strChainType == "protein"):
                        self.addExecutiveSummaryLine("    Number of residues             : %.2f" % chain.getNumberOfMonomers().getValue())
                    elif(strChainType == "dna" or strChainType == "rna"):
                        self.addExecutiveSummaryLine("    Number of nucleotides          : %.2f" % chain.getNumberOfMonomers().getValue())
                    strHeavyAtomsChain = "    Number of heavy atoms          :"
                    if(chain.getHeavyAtoms() is not None):
                        heavyAtomsChain = chain.getHeavyAtoms().getAtom()
                        for heavyAtomChain in heavyAtomsChain:
                            strHeavyAtomsChain = strHeavyAtomsChain + " %s=%d" % (heavyAtomChain.getSymbol().getValue(), heavyAtomChain.getNumberOf().getValue())
                    else:
                        strHeavyAtomsChain = strHeavyAtomsChain + " No heavy atoms"
                    self.addExecutiveSummaryLine(strHeavyAtomsChain)

                    self.addExecutiveSummaryLine("    Number of copies in structure  : %.2f" % chain.getNumberOfCopies().getValue())
                    self.addExecutiveSummaryLine("")

                ligands = xsDataStructure.getLigand()
                if(len(ligands) != 0):
                    self.addExecutiveSummaryLine("Ligands:")

                for ligand in ligands:
                    self.addExecutiveSummaryLine("    Number of light atoms          : %.2f" % ligand.getNumberOfLightAtoms().getValue())
                    strHeavyAtomsLigand = "    Number of heavy atoms          :"
                    if(ligand.getHeavyAtoms() is not None):
                        heavyAtomsLigand = ligand.getHeavyAtoms().getAtom()
                        for heavyAtomLigand in heavyAtomsLigand:
                            strHeavyAtomsLigand = strHeavyAtomsLigand + " %s=%d" % (heavyAtomLigand.getSymbol().getValue(), heavyAtomLigand.getNumberOf().getValue())
                    else:
                        strHeavyAtomsChain = strHeavyAtomsChain + " No heavy atoms"
                    self.addExecutiveSummaryLine(strHeavyAtomsLigand)
                    self.addExecutiveSummaryLine("    Number of copies in structure  : %.2f" % chain.getNumberOfCopies().getValue())
                    self.addExecutiveSummaryLine("")


        if (self.edPluginBest is not None):
            if (self.edPluginBest.getDataOutput() is not None):
                self.appendExecutiveSummary(self.edPluginBest, "Best : ")
                self.addExecutiveSummaryLine("")

        if (self.edPluginAlignment is not None):
            #if ( self.edPluginAlignment.getDataOutput() is not None ):
            self.appendExecutiveSummary(self.edPluginAlignment, "STAC - Alignment : ")
            self.addExecutiveSummaryLine("")

        if (self.edPluginKappaStrategy is not None):
            #if ( self.edPluginAlignment.getDataOutput() is not None ):
            self.appendExecutiveSummary(self.edPluginKappaStrategy, "STAC - Strategy : ")
            self.addExecutiveSummaryLine("")

