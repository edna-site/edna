#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       
#
#    

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os


from EDMessage import EDMessage
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import  EDFactoryPluginStatic

from EDPluginSTACv2_0 import EDPluginSTACv2_0

EDFactoryPluginStatic.loadModule( "XSDataSTACv2_0" )
from XSDataSTACv2_0 import kappa_strategy_request
from XSDataSTACv2_0 import kappa_strategy_response

import math

class EDPluginSTACStrategyv2_0( EDPluginSTACv2_0 ):
    """
    Calculates multi-sweep data collection strategy for different orientations 
    using a configured and calibrated STAC installation
    INPUT   : kappa_strategy_request; XSDataMXv2.XSDataCollection; XSDataInputStrategy
    OUTPUT  : kappa_strategy_response
    EXECSUMM: table of Omega scan strategies with different Kappa-Phi Datums
    Current limitations:
    + do not print exposure time, osc. width and resolution to be used
    """

    def __init__( self ):
        """
        """
        EDPluginSTACv2_0.__init__( self )
        EDFactoryPluginStatic.loadModule( "XSDataMXv1" )
        EDFactoryPluginStatic.loadModule( "XSDataMXv2" )
        EDFactoryPluginStatic.loadModule( "XSDataSTACv2_0" )
        EDFactoryPluginStatic.loadModule( "XSDataBestv1_1" )
        from XSDataMXv1 import XSDataIndexingResult
        from XSDataMXv1 import XSDataInputStrategy
        from XSDataBestv1_1 import XSDataInputBest
        self.setXSDataInputClass( kappa_strategy_request, "kappa_strategy_request" )
        import XSDataMXv2
        self.setXSDataInputClass( XSDataMXv2.XSDataCollection, "mxv2DataCollection" )
        # not used: self.setXSDataInputClass( XSDataIndexingResult, "indexingResult" )
        self.setXSDataInputClass( XSDataInputStrategy, "inputBest" )
        #self.setXSDataInputClass( XSDataInputBest, "inputBest" )


    def getSTACcommand( self ):
        return "kappa_strategy"


    def preProcess( self, _oedObject=None ):
        EDPluginSTACv2_0.preProcess( self )
        self.DEBUG( "EDPluginSTACStrategyv2_0.preProcess" )
        #bestfile.par
        #EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.m_oxsDataBestFileContentPar.getValue())
        #self.writeBestfilePar( os.path.join( self.getWorkingDirectory(), "bestfile.par" ), self.m_oxsDataBestFileContentPar.getValue() )
        self.writeBestfilePar( os.path.join( self.getWorkingDirectory(), "bestfile.par" ), self.getDataInput( "inputBest" )[0].getBestFileContentPar().getValue() )
        self.writeStrategyRequest()
        self.writeKappaSettings()


    def writeStrategyRequest( self ):
        #EDUtilsFile.writeFile( os.path.join( self.getWorkingDirectory(), "DNA_kappa_strategy_request" ), self.getDataInput( "kappa_strategy_request" )[0].marshal() )
        
        #pass any requests only just once
        request=kappa_strategy_request.parseString(self.getDataInput( "kappa_strategy_request" )[0].marshal())
        list=self.getDataInput( "kappa_strategy_request" )[0].getDesired_datum()
        request.setDesired_datum([])
        fnd=False
        tol=0.1
        for i in range(0, list.__len__()):
            fnd=False
            for j in range(0,i):
                if (math.fabs(float(list[i].getKappa())-float(list[j].getKappa()))<tol and math.fabs(float(list[i].getPhi())-float(list[j].getPhi()))<tol):
                    fnd=True
            if not fnd:       
                request.addDesired_datum(list[i])
        EDUtilsFile.writeFile( os.path.join( self.getWorkingDirectory(), "DNA_kappa_strategy_request" ), request.marshal() )
    

    def checkParameters( self ):
        """
        Checks the data input object
        """
        # Checks the mandatory parameters:
        #self.checkMandatoryParameters( self.getDataInput().getclass(), "kappa_strategy_request")


    def fetchOutput( self ):
        """
        method for reading back the specific output
        """
        # Then read the XML file
        self.m_oxsKappaResponse = kappa_strategy_response.parseFile( os.path.join( self.getWorkingDirectory(), "STAC_DNA_kappa_strategy_response" ) )
        return self.m_oxsKappaResponse


    def generateExecutiveSummary( self, _oedPlugin ):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG( "EDPluginSTACStrategyv2_0.generateExecutiveSummary" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_BEGIN-->" )
        if ( self.getStringVersion() is not None ):
            self.addExecutiveSummaryLine( self.getStringVersion() + " by Sandor Brockhauser" )

        import math

        self.addExecutiveSummaryLine( "" )
        #also STAC credit string
        self.addExecutiveSummaryLine( self.m_oxsKappaResponse.getComment() )
        self.addExecutiveSummaryLine( "----------------------------------------------------------------" )
        self.addExecutiveSummaryLine( "--ID------OStart----OEnd------K--------P----#Img-----Compl%-----" )
        oxsDataList = self.m_oxsKappaResponse.getGenerated_sweep()
        for oxsDataSweep in oxsDataList:
            self.addExecutiveSummaryLine( "%5s : %7s <-> %7s %7s %7s %4s %7s" % \
                                          ( oxsDataSweep.getStrategyID(), \
                                          oxsDataSweep.getOmegaStart(),
                                          oxsDataSweep.getOmegaEnd(),
                                          oxsDataSweep.getKappa(),
                                          oxsDataSweep.getPhi(),
                                          #exposure,
                                          #resolution,
                                          1 + int( math.fabs( float( oxsDataSweep.getOmegaEnd() ) - float( oxsDataSweep.getOmegaStart() ) ) ),
                                          oxsDataSweep.getCompleteness() ) )
        self.addExecutiveSummaryLine( "----------------------------------------------------------------" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_END-->" )

