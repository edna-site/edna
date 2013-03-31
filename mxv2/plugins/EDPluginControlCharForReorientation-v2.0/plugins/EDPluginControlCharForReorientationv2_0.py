#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlCharForReorientationv2_0.py 2064 2010-09-16 08:32:50Z svensson $"
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


from EDVerbose       import EDVerbose
from EDFactoryPluginStatic   import EDFactoryPluginStatic
from EDPluginControl import EDPluginControl
from EDConfiguration import EDConfiguration
from EDMessage       import EDMessage

EDFactoryPluginStatic.loadModule("EDHandlerXSDataMXv1v1_0")
from EDHandlerXSDataMXv1v1_0 import EDHandlerXSDataMXv1v1_0
EDFactoryPluginStatic.loadModule("EDHandlerXSDataSTACv2_0")
from EDHandlerXSDataSTACv2_0 import EDHandlerXSDataSTACv2_0

from XSDataMXv1 import XSDataInputStrategy
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv2 import XSDataInputCharacterisationv2_0
from XSDataMXv2 import XSDataResultCharacterisationv2_0
from XSDataMXv2 import XSDataCollection

class EDPluginControlCharForReorientationv2_0(EDPluginControl):
    """
    The Plugin that controls the whole characterisation: Indexing-Integration-(Kappa)Strategy    
    Indexing-Integration is the same as mxv1 characterisation.
    KappaStrategy:
    Preferred Strategy is given at the initial orientation, but if KAPPA features are enabled,
    strategies are calculated to some alignments.
    ===
    In case the XSDataCollection.diffractionPlan.kappaStrategyOption contains KAPPA related keywords,
    reorientation strategy is calculated after the Integration.
    If the beam is bigger then the xtal, the result is a full strategy in a new orientation,
    otherwise it generates a strategty for collecting extra reference images at the new orientation.
    """

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisationv2_0)
        self.setXSDataInputClass(XSDataInputCharacterisation, "mxv1InputCharacterisation")
        self.setXSDataInputClass(XSDataCollection, "mxv2DataCollection")
        self.strPluginControlCharacterisation = "EDPluginControlCharacterisationv1_3"
        self.edPluginControlCharacterisation = None
        self.mxv1InputCharacterisation = None
        self.mxv2DataCollection = None
        self.strPluginStrategyName = None
        self.edPluginControlStrategy = None
        self.xsDataResultCharacterisation = None
        self.suggestedStrategy=None
        self.suggestedStrategy=None
        self.newpossibleOrientations=None

    def configure(self):
        EDPluginControl.configure(self)
        


    def preProcess(self, _edPlugin=None):
        EDPluginControl.preProcess(self, _edPlugin)
        # Check the input
        if self.hasDataInput():
            self.mxv1InputCharacterisation = self.getDataInput().getMxv1InputCharacterisation()
            self.mxv2DataCollection = self.getDataInput().getMxv2DataCollection()
        else:
            if self.hasDataInput("mxv1InputCharacterisation"):
                self.mxv1InputCharacterisation = self.getDataInput("mxv1InputCharacterisation")[0]
            if self.hasDataInput("mxv2DataCollection"):
                self.mxv2DataCollection = self.getDataInput("mxv2DataCollection")[0]
        # Load the plugins
        self.edPluginControlCharacterisation = self.loadPlugin(self.strPluginControlCharacterisation, \
                                                                   "MXv1Characterisation")
        self.edPluginControlCharacterisation.setDataInput(self.mxv1InputCharacterisation)
        xsDataListOpt=self.mxv1InputCharacterisation.getDataCollection().getDiffractionPlan().getKappaStrategyOption()
        listOpt = map(lambda xsDataOpt : xsDataOpt.getValue(), xsDataListOpt)
        # Check if kappa strategy option is specified
        if (not "NoKappa" in listOpt) and (self.mxv2DataCollection is not None):
            self.edPluginControlCharacterisation.doStrategyCalculation(False)
            #if there is specific KAPPA option request, do that and suggest a characterisation at a new orientation
            listOpt=self.mxv1InputCharacterisation.getDataCollection().getDiffractionPlan().getKappaStrategyOption()
            if listOpt == []:
                #otherwise simply do an mxv2 characterisation
                #providing mxv1 style strategy at the give orientation 
                #and standard reorientation possibilities in the Executive Summary
                self.strPluginStrategyName = "EDPluginControlKappaStrategyv2_0"        
            else:
                self.strPluginStrategyName = "EDPluginControlKappaReorientationStrategyv2_0"
        
        
    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        self.edPluginControlCharacterisation.connectSUCCESS(self.doCharacterisationSuccess)
        self.edPluginControlCharacterisation.connectFAILURE(self.doCharacterisationFailure)
        self.executePluginSynchronous(self.edPluginControlCharacterisation)


    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self,_edPlugin)
        xsDataResultCharacterisationv2_0 = XSDataResultCharacterisationv2_0()
        xsDataResultCharacterisationv2_0.setMxv1ResultCharacterisation(self.xsDataResultCharacterisation)
        xsDataResultCharacterisationv2_0.setMxv1ResultCharacterisation_Reference(self.xsDataResultCharacterisation)
        if self.suggestedStrategy is not None:
            self.setDataOutput(self.suggestedStrategy,"SuggestedStrategy")
            xsDataResultCharacterisationv2_0.setSuggestedStrategy(self.suggestedStrategy)
        if self.newpossibleOrientations is not None:
            self.setDataOutput(self.newpossibleOrientations,"possibleOrientations")
            xsDataResultCharacterisationv2_0.setPossibleOrientations(self.newpossibleOrientations)
            
        self.setDataOutput(xsDataResultCharacterisationv2_0)
        
        
    def doCharacterisationSuccess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doCharacterisationSuccess")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doCharacterisationSuccess")
        self.xsDataResultCharacterisation = self.edPluginControlCharacterisation.getDataOutput()
        # Check if kappa strategy is requested:
        if self.strPluginStrategyName is not None:
            self.edPluginControlStrategy = self.loadPlugin(self.strPluginStrategyName, \
                                                                   "MXv2KappaStrategy")
            xsDataInputStrategy = XSDataInputStrategy()
            xsDataSolutionSelected = self.xsDataResultCharacterisation.getIndexingResult().getSelectedSolution()
            xsDataInputStrategy.setCrystalRefined(xsDataSolutionSelected.getCrystal())
            xsDataInputStrategy.setSample(self.xsDataResultCharacterisation.getDataCollection().getSample())
            xsDataIntegrationSubWedgeResultList = self.xsDataResultCharacterisation.getIntegrationResult().getIntegrationSubWedgeResult()
            xsDataInputStrategy.setBestFileContentDat(xsDataIntegrationSubWedgeResultList[0].getBestfileDat())
            xsDataInputStrategy.setBestFileContentPar(xsDataIntegrationSubWedgeResultList[0].getBestfilePar())
            xsDataInputStrategy.setExperimentalCondition(xsDataIntegrationSubWedgeResultList[0].getExperimentalConditionRefined())
            xsDataInputStrategy.setXdsBackgroundImage(self.xsDataResultCharacterisation.getXdsBackgroundImage())
            for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
                xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())
            xsDataInputStrategy.setDiffractionPlan(self.xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())
            self.edPluginControlStrategy.setDataInput(xsDataInputStrategy, "mxv1InputStrategy")
            self.edPluginControlStrategy.setDataInput(self.mxv2DataCollection, "mxv2DataCollection")
            self.edPluginControlStrategy.setDataInput(self.xsDataResultCharacterisation.getIndexingResult(), "mxv1IndexingResult")
            self.edPluginControlStrategy.connectSUCCESS(self.doStrategySuccess)
            self.edPluginControlStrategy.connectFAILURE(self.doStrategyFailure)
            self.executePluginSynchronous(self.edPluginControlStrategy)
    
    def doCharacterisationFailure(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doCharacterisationFailure")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionIndexing")
        self.xsDataResultCharacterisation = self.edPluginControlCharacterisation.getDataOutput()

    
            
    def doStrategySuccess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doStrategySuccess")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doStrategySuccess")
        xsDataResultStrategy = self.edPluginControlStrategy.getDataOutput()
        self.xsDataResultCharacterisation.setStrategyResult(xsDataResultStrategy)
        self.suggestedStrategy = None
        self.newpossibleOrientations = None
        if self.edPluginControlStrategy.hasDataOutput("possibleOrientations"):
            EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doStrategySuccess: With possible orientations")
            #get the next orientation
            #create new ref data coll plan at new orirntation
            #remove the currently offered orientation from the list            
            Orients = self.edPluginControlStrategy.getDataOutput("possibleOrientations")[0].getPossible_orientation()
            if Orients != []:
                omega = Orients[0].getOmega()
                kappa = Orients[0].getKappa()
                phi = Orients[0].getPhi()
                self.suggestedStrategy=EDHandlerXSDataMXv1v1_0.mergeStrategyToNewOrientation(xsDataResultStrategy,self.mxv1InputCharacterisation.getDataCollection(),omega,kappa,phi)
                self.newpossibleOrientations=EDHandlerXSDataSTACv2_0.removeOrientation(self.edPluginControlStrategy.getDataOutput("possibleOrientations")[0],kappa,phi)
        if self.suggestedStrategy is None:
            EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doStrategySuccess: Without possible orientations")
            #set the orientation for the actual strategy
            #we suggest the currently calculated strategy
            #and we have to add the actual orientation
            dc = self.mxv2DataCollection
            omega = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getBaseaxissetting()
            [kappa, phi] = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getAxissetting()
            self.suggestedStrategy=EDHandlerXSDataMXv1v1_0.copyStrategyToNewOrientation(xsDataResultStrategy,'%.2f'%omega.getValue(),'%.2f'%kappa.getValue(),'%.2f'%phi.getValue())
    
    def doStrategyFailure(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doStrategyFailure")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionIndexing")
    
    
    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDPluginControl.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.generateExecutiveSummary")
        if (self.edPluginControlCharacterisation is not None):
            self.appendExecutiveSummary(self.edPluginControlCharacterisation, "Strategy : ")
            self.addExecutiveSummaryLine("") 
        if (self.edPluginControlStrategy is not None):
            self.appendExecutiveSummary(self.edPluginControlStrategy, "Kappa strategy : ")
            self.addExecutiveSummaryLine("")          