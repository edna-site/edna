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
from EDImportLib        import EDVerbose
from EDImportLib        import EDDiskExplorer
from EDImportLib        import EDList
from EDImportLib        import EDDict
from EDMessage          import EDMessage
from EDUtilsFile        import EDUtilsFile
from EDUtilsTable       import EDUtilsTable
from EDConfiguration    import EDConfiguration

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

from XSDataSTACv01 import kappa_alignment_response


class EDPluginSTACAlignmentv10( EDPluginSTACv10 ):
    """
    Calculates xtal reorientations using a configured and calibrated STAC installation
    INPUT   : XSDataInputBest
    OUTPUT  : kappa_alignment_response
    EXECSUMM: table of orientation vectors and the necessary Omega-Kappa-Phi Datums
    Current limitations:
    + static predefined request
    + assupmtion of collecting the original orientation at the datum (0;0;0)
    """
    

    def getSTACcommand( self ):
        return "kappa_alignment"

    def preProcess( self, _oedObject = None ):
        EDPluginSTACv10.preProcess( self )
        self.DEBUG( "EDPluginSTACalignmentv01.preProcess")
        #bestfile.par
        EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.m_xsDataInput.getBestFileContentPar().getValue())
        #self.writeAlignmentRequest() - for now use a predefined request
        EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "DNA_kappa_alignment_request" ), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_alignment_request><desired_orientation><v1>a*</v1><v2>b*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>a*</v1><v2>c*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>b*</v1><v2>a*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>b*</v1><v2>c*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>c*</v1><v2>a*</v2><close>true</close><comment></comment></desired_orientation><desired_orientation><v1>c*</v1><v2>b*</v2><close>false</close><comment></comment></desired_orientation><comment>First test parameter passed</comment></kappa_alignment_request>")
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
            self.m_xsDataInput = XSDataInputBest.parseString( _dataInput )
        elif ( isinstance( _dataInput, XSDataInputBest ) ):
            self.m_xsDataInput = _dataInput
        else:
            errorMessage = EDMessage.ERROR_WRONG_DATA_TYPE_02 % ('EDPluginSTACv10.setDataInput', "XMLString or XSDataBestv01Input expected" )
            self.error( errorMessage )
            self.addErrorMessage( errorMessage )  
            raise RuntimeError, errorMessage

    def checkParameters( self ):
        """
        Checks the data input object
        """
        # Checks the mandatory parameters:
        self.checkMandatoryParameters( self.getDataInput().getBestFileContentPar(), "bestfilePar")

    def fetchOutput( self ):
        """
        method for reading back the specific output
        """
        self.m_oxsKappaAlignmentResponse = kappa_alignment_response.parseFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "STAC_DNA_kappa_alignment_response" ) )
        return self.m_oxsKappaAlignmentResponse

    def generateExecutiveSummary( self, _oedPlugin ):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG( "EDPluginSTACv10Alignment.generateExecutiveSummary" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_BEGIN-->" )
        if ( self.getStringVersion() is not None ):
            self.addExecutiveSummaryLine( self.getStringVersion()+" by Sandor Brockhauser" )
            
        self.addExecutiveSummaryLine( "" )
        self.addExecutiveSummaryLine( EDString(self.m_oxsKappaAlignmentResponse.getComment()) )
        self.addExecutiveSummaryLine( "-------------------------------------------------------" )
        self.addExecutiveSummaryLine( "--v1-----------v2------------O---------K--------P------" )
        oxsDataKappaAlignmentList = self.m_oxsKappaAlignmentResponse.getPossible_orientation()
        for oxsDataPossible_orientation in oxsDataKappaAlignmentList:
            self.addExecutiveSummaryLine( "%13s %13s : %7s %7s %7s" % \
                                          ( EDString(oxsDataPossible_orientation.getV1()), \
                                          EDString(oxsDataPossible_orientation.getV2()),
                                          EDString(oxsDataPossible_orientation.getOmega()),
                                          EDString(oxsDataPossible_orientation.getKappa()),
                                          EDString(oxsDataPossible_orientation.getPhi()) ) )
        self.addExecutiveSummaryLine( "-------------------------------------------------------" )
        self.addExecutiveSummaryLine( "<!--SUMMARY_END-->" )



