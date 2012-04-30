#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlKappaReorientationStrategyv2_0.py 2079 2010-09-20 13:08:27Z svensson $"
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

EDFactoryPluginStatic.loadModule("XSDataSTACv2_0")
from XSDataSTACv2_0 import kappa_strategy_request
from XSDataSTACv2_0 import kappa_strategy_response
from XSDataSTACv2_0 import strategy_request

EDFactoryPluginStatic.loadModule("EDPluginControlKappaStrategyv2_0")
from EDPluginControlKappaStrategyv2_0 import EDPluginControlKappaStrategyv2_0

class EDPluginControlKappaReorientationStrategyv2_0(EDPluginControlKappaStrategyv2_0):
    """
    The Plugin that controls the strategy step
    """

    def __init__ (self):
        EDPluginControlKappaStrategyv2_0.__init__(self)
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.__init__...")

        self.strPluginOrientationName = "EDPluginSTACOrientationv2_0"
        self.edPluginOrientation = None
#        self.edHandlerXSDataOrientation = None

        self.strPluginSimpleStrategyName = "EDPluginControlStrategyv1_2"
        self.edPluginSimpleStrategy = None
#        self.edHandlerXSDataOrientation = None


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControlKappaStrategyv2_0.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.preProcess...")

        if (self.KappaStrategy):
            #Orientation
            self.edPluginOrientation = self.loadPlugin(self.strPluginOrientationName)
            if (self.edPluginOrientation is not None):
                self.edPluginOrientation.setBaseDirectory(self.getWorkingDirectory())
                self.edPluginOrientation.setBaseName(self.strPluginOrientationName)

        self.edPluginSimpleStrategy = self.loadPlugin(self.strPluginSimpleStrategyName)
        if (self.edPluginSimpleStrategy is not None):
            self.edPluginSimpleStrategy.setBaseDirectory(self.getWorkingDirectory())
            self.edPluginSimpleStrategy.setBaseName(self.strPluginSimpleStrategyName)


    def process(self, _edObject=None):
        """
        """
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.process...")

        #call KAPPA orientation
        if self.edPluginOrientation is not None:
            self.connectProcess(self.executeOrientation)
            self.edPluginOrientation.connectFAILURE(self.doFailureActionOrientation)

        if self.edPluginAlignment is not None:
            self.connectProcess(self.doOrientationToAlignmentTransition)
            self.edPluginAlignment.connectFAILURE(self.doFailureActionAlignment)

        if self.edPluginSimpleStrategy is not None:
            self.connectProcess(self.doAlignmentToStrategyTransition)


    def executeOrientation(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.executeOrientation")

        xsDataBestInput = self.edHandlerXSDataBest.getXSDataInputBest(self.getDataInput("mxv1InputStrategy")[0])
        self.edPluginOrientation.setDataInput(xsDataBestInput, "inputBest")
        self.edPluginOrientation.setDataInput(self.getDataInput("mxv2DataCollection")[0], "dataCollection")
        self.edPluginOrientation.setDataInput(self.getDataInput("mxv1IndexingResult")[0], "indexingResult")
        listOpt = self.getDataInput("mxv1InputStrategy")[0].getDiffractionPlan().getKappaStrategyOption()
        for strOpt in listOpt:
            self.edPluginOrientation.setDataInput(strOpt, "KappaStrategyOption")

        self.edPluginOrientation.executeSynchronous()


    def doOrientationToAlignmentTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.doOrientationToAlignmentTransition")

        xsDataBestInput = self.edHandlerXSDataBest.getXSDataInputBest(self.getDataInput("mxv1InputStrategy")[0])
        self.edPluginAlignment.setDataInput(xsDataBestInput, "inputBest")
        self.edPluginAlignment.setDataInput(self.getDataInput("mxv2DataCollection")[0], "dataCollection")
        self.edPluginAlignment.setDataInput(self.getDataInput("mxv1IndexingResult")[0], "indexingResult")

        #alignment request
        OrientResult = self.edPluginOrientation.getDataOutput()
        self.edPluginAlignment.setDataInput(OrientResult, "kappa_alignment_request")

        self.edPluginAlignment.executeSynchronous()


    def doAlignmentToStrategyTransition(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.doAlignmentToStrategyTransition")

        #here we could modify bestfile.par to get the strategy (and statistics) for a prefered orientation

        #for now, we simple call strategy for the actual orientation
        self.executeSimpleStrategy(_edPlugin)


    def doFailureActionOrientation(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.doFailureActionOrientation")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlKappaReorientationStrategyv2_0.doFailureActionOrientation")
        strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlKappaReorientationStrategyv2_0.doFailureActionOrientation', self.strPluginOrientationName, "STACOrientation failure")
        EDVerbose.warning(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        self.executeSimpleStrategy(_edPlugin)


    def doFailureActionAlignment(self, _edPlugin):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.doFailureActionAlignment")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlKappaReorientationStrategyv2_0.doFailureActionAlignment")
        strWarningMessage = EDMessage.WARNING_CANNOT_USE_PLUGIN_03 % ('EDPluginControlKappaReorientationStrategyv2_0.doFailureActionAlignment', self.strPluginAlignmentName, "STACAlignment failure")
        EDVerbose.warning(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        self.executeSimpleStrategy(_edPlugin)


    def executeSimpleStrategy(self, _edPlugin):
        """
        """
        self.edPluginSimpleStrategy.setDataInput(self.getDataInput("mxv1InputStrategy")[0])

        self.edPluginSimpleStrategy.executeSynchronous()


    def postProcess(self, _edObject=None):
        """
        """
        #get reference strategy copied to new orientation if it worked

        #otherwise get full DC strategy for this orientation if reorientation does not work

        #get reference statistics from the BEST run
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.postProcess...")

        #referenceCollectionStrategyAtNewOrientation
        #for now, it is:
        #SimpleStrategy
        self.setDataOutput(self.edPluginSimpleStrategy.getDataOutput()) #,"SimpleStrategyResult")
        #possibleAlignments
        try:
            self.setDataOutput(self.edPluginAlignment.getDataOutput(), "possibleOrientations")
        except:
            EDVerbose.WARNING("Could not get the list of Possible orientations.")



    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        EDPluginControlKappaStrategyv2_0.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("EDPluginControlKappaReorientationStrategyv2_0.generateExecutiveSummary")
        if (self.edPluginOrientation is not None):
            #if ( self.edPluginAlignment.getDataOutput() is not None ):
            self.appendExecutiveSummary(self.edPluginOrientation, "STAC - Orientation : ")
            self.addExecutiveSummaryLine("")

        #Simple Strategy results
        #if (self.edPluginSimpleStrategy is not None):
        #    self.appendExecutiveSummary(self.edPluginSimpleStrategy, "Ref. Strategy : ")
        #    self.addExecutiveSummaryLine("")



