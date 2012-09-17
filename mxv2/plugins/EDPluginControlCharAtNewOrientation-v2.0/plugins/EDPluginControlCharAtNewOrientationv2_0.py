#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlCharAtNewOrientationv2_0.py 2064 2010-09-16 08:32:50Z svensson $"
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

EDFactoryPluginStatic.loadModule("XSDataMXv1")
import XSDataMXv1
import XSDataMXv2
EDFactoryPluginStatic.loadModule("XSDataSTACv2_0")
import XSDataSTACv2_0

#EDFactoryPluginStatic.loadModule("EDPluginControlCharacterisationv1_2")
#from EDPluginControlCharacterisationv1_2 import EDPluginControlCharacterisationv1_2
#EDFactoryPluginStatic.loadModule("EDPluginControlCharacterisationv1_3")
#from EDPluginControlCharacterisationv1_3 import EDPluginControlCharacterisationv1_3
EDFactoryPluginStatic.loadModule("EDHandlerXSDataMXv1v1_0")
from EDHandlerXSDataMXv1v1_0 import EDHandlerXSDataMXv1v1_0
EDFactoryPluginStatic.loadModule("EDHandlerXSDataSTACv2_0")
from EDHandlerXSDataSTACv2_0 import EDHandlerXSDataSTACv2_0


EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataInputStrategy
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation

from XSDataMXv2 import XSDataInputCharacterisationv2_0
from XSDataMXv2 import XSDataResultCharacterisationv2_0
from XSDataMXv2 import XSDataCollection
from XSDataMXv2 import kappa_alignment_response


class EDPluginControlCharAtNewOrientationv2_0(EDPluginControl):
    """
    The Plugin that controls the whole characterisation: Indexing-Integration-Strategy    
    Just like mxv1 characterisation.
    ===
    At the end we compare the statistics at this orientation to the statisticsa at the 
    reference orientation.
    If the reference is much better, we suggest to go back, or chose the next possible orientation.
    Otherwise, we suggest to continue with collecting the data following the currently calculated strategy. 
    """

    def __init__ (self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisationv2_0)
        self.setXSDataInputClass(XSDataInputCharacterisation, "mxv1InputCharacterisation")
        self.setXSDataInputClass(XSDataResultCharacterisation, "mxv1ResultCharacterisation_Reference")
        self.setXSDataInputClass(XSDataCollection, "mxv2DataCollection")
        self.setXSDataInputClass(XSDataMXv2.XSDataCollection, "mxv2DataCollection_Reference")
        self.setXSDataInputClass(kappa_alignment_response, "possibleOrientations")
        self.strPluginControlCharacterisation = "EDPluginControlCharacterisationv1_3"
        self.edPluginControlCharacterisation = None
        self.mxv1InputCharacterisation = None
        self.mxv1ResultCharacterisation_Reference = None
        self.mxv2DataCollection = None
        self.mxv2DataCollection_Reference = None
        self.strPluginStrategyName = None
        self.edPluginControlStrategy = None
        self.xsDataResultCharacterisation = None
        self.suggestedStrategy=None
        self.suggestedStrategy=None
        self.possibleOrientations=None
        self.newpossibleOrientations=None

        
    def preProcess(self, _edPlugin=None):
        EDPluginControl.preProcess(self, _edPlugin)
        # Check the input
        if self.hasDataInput():
            self.mxv1InputCharacterisation = self.getDataInput().getMxv1InputCharacterisation()
            self.mxv1ResultCharacterisation_Reference = self.getDataInput().getMxv1ResultCharacterisation_Reference()
            self.mxv2DataCollection = self.getDataInput().getMxv2DataCollection()
            self.mxv2DataCollection_Reference = self.getDataInput().getMxv2DataCollection_Reference()
            self.possibleOrientations = self.getDataInput().getPossibleOrientations()
        else:
            if self.hasDataInput("mxv1InputCharacterisation"):
                self.mxv1InputCharacterisation = self.getDataInput("mxv1InputCharacterisation")[0]
            if self.hasDataInput("mxv1ResultCharacterisation_Reference"):
                self.mxv1ResultCharacterisation_Reference = self.getDataInput("mxv1ResultCharacterisation_Reference")[0]
            if self.hasDataInput("mxv2DataCollection"):
                self.mxv2DataCollection = self.getDataInput("mxv2DataCollection")[0]
            if self.hasDataInput("mxv2DataCollection_Reference"):
                self.mxv2DataCollection_Reference = self.getDataInput("mxv2DataCollection_Reference")[0]
            if self.hasDataInput("possibleOrientations"):
                self.possibleOrientations = self.getDataInput("possibleOrientations")[0]
        # Load the plugins
        self.edPluginControlCharacterisation = self.loadPlugin(self.strPluginControlCharacterisation, "Charactersiation")
        self.edPluginControlCharacterisation.setDataInput(self.mxv1InputCharacterisation)


    def process(self, _edObject=None):
        EDPluginControl.process(self,_edObject)        
        EDVerbose.DEBUG("EDPluginControlCharAtNewOrientationv2_0.process...")
        self.edPluginControlCharacterisation.connectSUCCESS(self.doCharacterisationSuccess)
        self.edPluginControlCharacterisation.connectFAILURE(self.doCharacterisationFailure)
        self.executePluginSynchronous(self.edPluginControlCharacterisation)

        
    def doCharacterisationSuccess(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharAtNewOrientationv2_0.doCharacterisationSuccess")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doCharacterisationSuccess")
        self.xsDataResultCharacterisation = self.edPluginControlCharacterisation.getDataOutput()
        self.suggestedStrategy=None
        simple=False
        try:
            #check if there is anything to compare to
        
            #compare; for now, we only check the resolution
            resRef = 900
            for collPlan in self.mxv1ResultCharacterisation_Reference.getStrategyResult().getCollectionPlan():
                resRef = min(resRef, collPlan.getStrategySummary().getRankingResolution().getValue())
            resNew = 900
            for collPlan in self.xsDataResultCharacterisation.getStrategyResult().getCollectionPlan():
                resNew = min(resNew, collPlan.getStrategySummary().getRankingResolution().getValue())
            #now, we tolerate 15% loss of resolution
            if resNew > resRef * 1.15:
                #if there is any alternative, take the next one            
                if self.possibleOrientations is not None and self.possibleOrientations.getPossible_orientation() != []:
                    #take it
#                    tol=0.1
#                    #so we will copy the strategy of collecting the reference images inputed to here but at the new orientation
#                    #get the full strategy from the Reference
#                    self.suggestedStrategy=XSDataMXv1.XSDataResultStrategy.parseString(self.getDataInput("mxv1ResultCharacterisation_Reference")[0].getStrategyResult().marshal())
#                    #take only the first CollectionPlan
#                    self.suggestedStrategy.setCollectionPlan([self.suggestedStrategy.getCollectionPlan()[0]])
#                    #modify the DC part taking it from the input 
#                    self.suggestedStrategy.getCollectionPlan()[0].setCollectionStrategy(self.getDataInput().getDataCollection())
#                    #and modify the Orientation
                    Orients = self.possibleOrientations.getPossible_orientation()
                    omega = Orients[0].getOmega()
                    kappa = Orients[0].getKappa()
                    phi = Orients[0].getPhi()
#                    for dcplan in self.suggestedStrategy.getCollectionPlan():
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "OMEGA=", omega))
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "KAPPA=", kappa))
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "PHI=", phi))
#                    #finally take the suggested new orientation out of the list of further possible ones
#                    self.newpossibleOrientations.setPossible_orientation([])
#                    for i in range(1, Orients.__len__()):
#                        if (math.fabs(float(Orients[i].getKappa())-float(kappa))<tol and math.fabs(float(Orients[i].getPhi())-float(phi))<tol):
#                            self.newpossibleOrientations.addPossible_orientation(Orients[i])
                    self.suggestedStrategy=EDHandlerXSDataMXv1v1_0.mergeStrategyToNewOrientation(self.mxv1ResultCharacterisation_Reference.getStrategyResult(),self.mxv1InputCharacterisation.getDataCollection(),omega,kappa,phi)
                    self.newpossibleOrientations=EDHandlerXSDataSTACv2_0.removeOrientation(self.possibleOrientations,kappa,phi)
                else:
#                    #otherwise suggest to go back to the initial orientation and follow the reference DC
#                    self.suggestedStrategy=XSDataMXv1.XSDataResultStrategy.parseString(self.getDataInput("mxv1ResultCharacterisation_Reference")[0].getStrategyResult().marshal())
#                    #and we have to declare the orientation in Reference to be used
#                    dc = XSDataMXv2.XSDataCollection()
                    dc = self.mxv2DataCollection_Reference
                    omega = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getBaseaxissetting()
                    [kappa, phi] = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getAxissetting()
#                    for dcplan in self.suggestedStrategy.getCollectionPlan():
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "OMEGA=", '%.2f'%omega.getValue()))
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "KAPPA=", '%.2f'%kappa.getValue()))
#                        dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "PHI=", '%.2f'%phi.getValue()))
                    self.suggestedStrategy=EDHandlerXSDataMXv1v1_0.copyStrategyToNewOrientation(self.mxv1ResultCharacterisation_Reference.getStrategyResult(),'%.2f'%omega.getValue(),'%.2f'%kappa.getValue(),'%.2f'%phi.getValue())
            else:
                simple=True
        except:
            EDVerbose.WARNING("Problem in suggesting the strategy")
            simple=True
            raise
        
        if simple:
#            #we suggest the currently calculated strategy
#            self.suggestedStrategy=XSDataMXv1.XSDataResultStrategy.parseString(self._EDPluginControlCharacterisationv1_2__xsDataResultCharacterisation.getStrategyResult().marshal())
#            #and we have to add the actual orientation
#            dc = XSDataMXv2.XSDataCollection()
            dc = self.mxv2DataCollection
            omega = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getBaseaxissetting()
            [kappa, phi] = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getAxissetting()
#            for dcplan in self.suggestedStrategy.getCollectionPlan():
#                dcplan.setComment(EDHandlerXSDataMXv1v1_0.replaceElements(dcplan.getComment(),"OMEGA=",'%.2f'%omega.getValue()))
#                dcplan.setComment(EDHandlerXSDataMXv1v1_0.replaceElements(dcplan.getComment(),"KAPPA=",'%.2f'%kappa.getValue()))
#                dcplan.setComment(EDHandlerXSDataMXv1v1_0.replaceElements(dcplan.getComment(),"PHI=",'%.2f'%phi.getValue()))
            self.suggestedStrategy=EDHandlerXSDataMXv1v1_0.copyStrategyToNewOrientation(self.xsDataResultCharacterisation.getStrategyResult(),'%.2f'%omega.getValue(),'%.2f'%kappa.getValue(),'%.2f'%phi.getValue())
        
        #add the new outputs
        xsDataResultCharacterisationv2_0 = XSDataResultCharacterisationv2_0()
        xsDataResultCharacterisationv2_0.setMxv1ResultCharacterisation(self.xsDataResultCharacterisation)
        xsDataResultCharacterisationv2_0.setMxv1ResultCharacterisation_Reference(self.mxv1ResultCharacterisation_Reference)
        if self.suggestedStrategy is not None:
            self.setDataOutput(self.suggestedStrategy,"SuggestedStrategy")
            xsDataResultCharacterisationv2_0.setSuggestedStrategy(self.suggestedStrategy)
        if self.newpossibleOrientations is not None:
            self.setDataOutput(self.newpossibleOrientations,"possibleOrientations")
            xsDataResultCharacterisationv2_0.setPossibleOrientations(self.newpossibleOrientations)
            
        self.setDataOutput(xsDataResultCharacterisationv2_0)


    def doCharacterisationFailure(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlCharForReorientationv2_0.doCharacterisationFailure")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlCharacterisationv2_0.doFailureActionIndexing")

