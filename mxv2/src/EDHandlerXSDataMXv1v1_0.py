#
#    Project: The EDNA Prototype
#             http://www.edna-site.org
#
#    File: "$Id: EDHandlerXSDataXDSv1_0.py 1516 2010-05-12 08:11:11Z svensson $"
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    Contributors:      Olof Svensson (svensson@esrf.fr) 


__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDHandlerXSDataMXv1v1_0:


    @staticmethod
    def mergeStrategyToNewOrientation(_xsDataResultStrategy, _xsDataCollection, _fOmega, _fKappa, _fPhi):
        '''
        _xsDataResultStrategy: reference strategy results as the template for the new strategy
        _xsDataCollection: The data collection that will be merged in
        
        result:
        suggestedStrategy(XSDataResultStrategy): the strategy resulted from the merge
        '''
#        suggestedStrategy = None
#        try:
#            newpossibleOrientations=XSDataSTACv01.kappa_alignment_response.parseString(_possible_orientation.marshal())
#        except:
#            newpossibleOrientations=None
        #so we will copy the strategy of collecting the reference images inputed to here but at the new orientation
        #get the full strategy from the Reference
        EDFactoryPluginStatic.loadModule("XSDataMXv1")
        from XSDataMXv1 import XSDataResultStrategy
        suggestedStrategy = XSDataResultStrategy.parseString(_xsDataResultStrategy.marshal())
        #take only the first CollectionPlan
        if len(suggestedStrategy.getCollectionPlan()) > 0:
            suggestedStrategy.setCollectionPlan([suggestedStrategy.getCollectionPlan()[0]])
            #modify the DC part taking it from the input 
            suggestedStrategy.getCollectionPlan()[0].setCollectionStrategy(_xsDataCollection)
            #and modify the Orientation
          #  dc = XSDataMXv2.XSDataCollection()
          #  dc = self.getDataInput("mxv2DataCollection_Reference")[0]
    #        Orients = _possible_orientation.getPossible_orientation()
    #        omega = Orients[0].getOmega()
    #        kappa = Orients[0].getKappa()
    #        phi = Orients[0].getPhi()
            suggestedStrategy = EDHandlerXSDataMXv1v1_0.copyStrategyToNewOrientation(suggestedStrategy, _fOmega, _fKappa, _fPhi, "MERGED")
    #        for dcplan in suggestedStrategy.getCollectionPlan():
    #            dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "OMEGA=", omega))
    #            dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "KAPPA=", kappa))
    #            dcplan.setComment(EDHandlerXSDataMXv1v1_0().replaceElements(dcplan.getComment(), "PHI=", phi))
            #finally take the suggested new orientation out of the list of further possible ones
    #        if newpossibleOrientations is not None:
    #            newpossibleOrientations.setPossible_orientation([])
    #            for i in range(1, Orients.__len__()):
    #                if (math.fabs(float(Orients[i].getKappa())-float(kappa))<tol and math.fabs(float(Orients[i].getPhi())-float(phi))<tol):
    #                    newpossibleOrientations.addPossible_orientation(Orients[i])
    #        return [suggestedStrategy,newpossibleOrientations]
        return suggestedStrategy


    @staticmethod
    def copyStrategyToNewOrientation(_xsDataResultStrategy, _fOmega, _fKappa, _fPhi, _strategy = "COPIED"):
        '''
        _xsDataResultStrategy: the strategy results in which the orientation should be changed
        omega,kappa,phi: the new orientation
        
        result:
        suggestedStrategy(XSDataResultStrategy): the strategy in which the orientation is changed
        '''
        #we suggest the currently calculated strategy
        EDFactoryPluginStatic.loadModule("XSDataMXv1")
        from XSDataMXv1 import XSDataResultStrategy
        suggestedStrategy = XSDataResultStrategy.parseString(_xsDataResultStrategy.marshal())
        #and we have to add the actual orientation
        EDFactoryPluginStatic.loadModule("EDHandlerXSDataCommon")
        from EDHandlerXSDataCommon import EDHandlerXSDataCommon
        for dcplan in suggestedStrategy.getCollectionPlan():
            dcplan.setComment(EDHandlerXSDataCommon.replaceElements(dcplan.getComment(), "OMEGA=", str(_fOmega)))
            dcplan.setComment(EDHandlerXSDataCommon.replaceElements(dcplan.getComment(), "KAPPA=", str(_fKappa)))
            dcplan.setComment(EDHandlerXSDataCommon.replaceElements(dcplan.getComment(), "PHI=", str(_fPhi)))
            dcplan.setComment(EDHandlerXSDataCommon.replaceElements(dcplan.getComment(), "STRATEGY=", str(_strategy)))
        return suggestedStrategy





