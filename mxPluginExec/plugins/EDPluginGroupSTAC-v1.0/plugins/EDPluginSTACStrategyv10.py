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

from EDImportLib        import EDVerbose
from EDImportLib        import EDString
from EDImportLib                     import EDVerbose
from EDImportLib                     import EDString
from EDImportLib                     import EDDiskExplorer
from EDImportLib                     import EDList
from EDImportLib                     import EDDict
from EDMessage                     import EDMessage
from EDUtilsFile                     import EDUtilsFile
from EDUtilsTable                     import EDUtilsTable
from EDConfiguration                     import EDConfiguration

from EDPluginSTACv10 import EDPluginSTACv10

from XSDataBestv1_1 import XSDataResultBest 
from XSDataBestv1_1 import XSDataBestCollectionPlan 


from XSDataCommon import XSDataFloat 
from XSDataMXv1 import XSDataBeam 
from XSDataCommon import XSDataTime 
from XSDataMXv1 import XSDataDetector 
from XSDataCommon import XSDataLength 
from XSDataCommon import XSDataAngle 
from XSDataCommon import XSDataInteger 
from XSDataCommon import XSDataString 
from XSDataCommon import XSDataTime 

from XSDataBestv1_1 import XSDataBestStatisticalPrediction 
from XSDataBestv1_1 import XSDataBestCollectionRun 
from XSDataBestv1_1 import XSDataBestStrategySummary 
from XSDataBestv1_1 import XSDataBestResolutionBin 
from XSDataBestv1_1 import XSDataInputBest

from XSDataSTACv01 import kappa_strategy_request
from XSDataSTACv01 import kappa_strategy_response


class EDPluginSTACStrategyv10( EDPluginSTACv10 ):
    """
    Calculates multi-sweep data collection strategy for different orientations 
    using a configured and calibrated STAC installation
    INPUT   : kappa_strategy_request
    OUTPUT  : kappa_strategy_response
    EXECSUMM: table of Omega scan strategies with different Kappa-Phi Datums
    Current limitations:
    + assupmtion of collecting the original orientation at the datum (0;0;0)
    + do not print exposure time and resolution to be used
    """



    def getSTACcommand( self ):
        return "kappa_strategy"

    def preProcess( self, _oedObject = None ):
        EDPluginSTACv10.preProcess( self )
        self.DEBUG( "EDPluginSTACalignmentv01.preProcess")
        #bestfile.par
        EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.m_oxsDataBestFileContentPar.getValue())
        #self.writeStrategyRequest()
        EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "DNA_kappa_strategy_request" ), self.m_xsDataInput.marshal() )
        #self.writeKappaSettings() - for now use a predefined datum (0;0;0)
        EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "DNA_STAC_Kappa_Settings" ), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_collect_settings><motorSettings><motorName>Omega</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>Kappa</motorName><motorValue>0.000000</motorValue></motorSettings><motorSettings><motorName>Phi</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>X</motorName><motorValue>0.261444</motorValue></motorSettings><motorSettings><motorName>Y</motorName><motorValue>-0.085559</motorValue></motorSettings><motorSettings><motorName>Z</motorName><motorValue>0.659333</motorValue></motorSettings><comment>BCM query performed by STAC</comment></kappa_collect_settings>")

    def setDataInput( self, _dataInput ):
        """
        Sets the Plugin Input Data
        _dataInput could be either an String XML or an XSData
        The XML String should be parsed as an Output Object by the final Plugin
        """
        self.DEBUG( "EDPluginSTACv10Alignment.setDataInput" )
        # Check the type
        if( isinstance( _dataInput, EDString ) ):
            self.DEBUG( "EDPluginSTACv10.setDataInput: Input Data is of EDString " )
            self.m_xsDataInput = kappa_strategy_request.parseString( _dataInput )
        elif ( isinstance( _dataInput, kappa_strategy_request ) ):
            self.m_xsDataInput = _dataInput
        else:
            errorMessage = EDMessage.ERROR_WRONG_DATA_TYPE_02 % ('EDPluginSTACv10.setDataInput', "XMLString or kappa_strategy_request expected" )
            self.error( errorMessage )
            self.addErrorMessage( errorMessage )  
            raise RuntimeError, errorMessage

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
        self.m_oxsKappaResponse = kappa_strategy_response.parseFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "STAC_DNA_kappa_strategy_response" ) )
        return self.m_oxsKappaResponse

    def generateExecutiveSummary( self, _oedPlugin ):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG( "EDPluginSTACv10Strategy.generateExecutiveSummary" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_BEGIN-->" )
        if ( self.getStringVersion() is not None ):
            self.addExecutiveSummaryLine( self.getStringVersion()+" by Sandor Brockhauser" )
            
        import math
            
        self.addExecutiveSummaryLine( "" )
        #also STAC credit string
        self.addExecutiveSummaryLine( EDString(self.m_oxsKappaResponse.getComment()) )
        self.addExecutiveSummaryLine( "----------------------------------------------------------------" )
        self.addExecutiveSummaryLine( "--ID------OStart----OEnd------K--------P----#Img-----Compl%-----" )
        oxsDataList = self.m_oxsKappaResponse.getGenerated_sweep()
        for oxsDataSweep in oxsDataList:
            self.addExecutiveSummaryLine( "%5s : %7s <-> %7s %7s %7s %4s %7s" % \
                                          ( EDString(oxsDataSweep.getStrategyID()), \
                                          EDString(oxsDataSweep.getOmegaStart()),
                                          EDString(oxsDataSweep.getOmegaEnd()),
                                          EDString(oxsDataSweep.getKappa()),
                                          EDString(oxsDataSweep.getPhi()),
                                          #exposure,
                                          #resolution,
                                          EDString(1+int(math.fabs(float(oxsDataSweep.getOmegaEnd())-float(oxsDataSweep.getOmegaStart())))),
                                          EDString(oxsDataSweep.getCompleteness())   ) )
        self.addExecutiveSummaryLine( "----------------------------------------------------------------" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_END-->" )

