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


from EDMessage          import EDMessage
from EDUtilsFile        import EDUtilsFile
from EDUtilsTable       import EDUtilsTable
from EDConfiguration    import EDConfiguration
from EDFactoryPluginStatic      import  EDFactoryPluginStatic

from EDPluginSTACv2_0 import EDPluginSTACv2_0

EDFactoryPluginStatic.loadModule("XSDataSTACv2_0")
from XSDataSTACv2_0 import kappa_alignment_request

from EDHandlerXSDataCommon import EDHandlerXSDataCommon


class EDPluginSTACOrientationv2_0(EDPluginSTACv2_0):
    """
    Suggests xtal orientations using a configured and calibrated STAC installation
    INPUT   : XSDataInputBest; XSDataMXv2.XSDataCollection; XSFastOrientationType
    OUTPUT  : kappa_Orientation_request
    EXECSUMM: table of orientation vectors suggested for the requested type
    Current limitations:
    """

    def __init__(self):
        """
        """
        EDPluginSTACv2_0.__init__(self)
        EDFactoryPluginStatic.loadModule("XSDataMXv1")
        EDFactoryPluginStatic.loadModule("XSDataBestv1_2")
        from XSDataMXv1 import XSDataIndexingResult
        from XSDataBestv1_2 import XSDataInputBest
        self.setXSDataInputClass(XSDataInputBest, "inputBest")
        self.setXSDataInputClass(XSDataIndexingResult, "indexingResult")
        from XSDataMXv1 import XSDataString
        self.setXSDataInputClass(XSDataString, "KappaStrategyOption")



    def getSTACcommand(self):
        return "kappa_orientation_request"

    def getSTACparams(self):
        try:
            val = None
            listOptions = self.getDataInput("KappaStrategyOption")
            for option in listOptions:
                if val is None:
                    val = option.getValue()
                else:
                    val += ' ' + option.getValue()
        except:
            self.DEBUG("ORIENTATION REQUEST COMMAND could not be found")
            val = ''

#        optstr=self.getDataInput("StrategyOption")[0].getValue()
#        opts=optstr.split()
#        for str in opts:
#            opt=str.split("KAPPA_")
#            if (opt.__len__()>1):
#                new=opt[1]
#                if (val.__len__()==0):
#                    val=new
#                else:
#                    val=' '.join([val,new])            
        return val

    def preProcess(self, _oedObject=None):
        EDPluginSTACv2_0.preProcess(self)
        self.DEBUG("EDPluginSTACOrientationv2_0.preProcess")
        #bestfile.par
        #EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.m_xsDataInput.getBestFileContentPar().getValue())
        #self.writeBestfilePar( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.getDataInput()[0].getBestFileContentPar().getValue() )
        self.writeBestfilePar(os.path.join(self.getWorkingDirectory(), "bestfile.par"), self.getDataInput("inputBest")[0].getBestFileContentPar().getValue())
        #self.writeOrientationRequest() - for now use a predefined request
        #EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), "DNA_kappa_Orientation_request"), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_Orientation_request><desired_orientation><v1>a*</v1><v2>b*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>a*</v1><v2>c*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>b*</v1><v2>a*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>b*</v1><v2>c*</v2><close>false</close><comment></comment></desired_orientation><desired_orientation><v1>c*</v1><v2>a*</v2><close>true</close><comment></comment></desired_orientation><desired_orientation><v1>c*</v1><v2>b*</v2><close>false</close><comment></comment></desired_orientation><comment>First test parameter passed</comment></kappa_Orientation_request>")
        #self.writeKappaSettings() - for now use a predefined datum (0;0;0)
        #EDUtilsFile.writeFile( os.path.join( self.getWorkingDirectory(), "DNA_STAC_Kappa_Settings" ), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_collect_settings><motorSettings><motorName>Omega</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>Kappa</motorName><motorValue>0.000000</motorValue></motorSettings><motorSettings><motorName>Phi</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>X</motorName><motorValue>0.261444</motorValue></motorSettings><motorSettings><motorName>Y</motorName><motorValue>-0.085559</motorValue></motorSettings><motorSettings><motorName>Z</motorName><motorValue>0.659333</motorValue></motorSettings><comment>BCM query performed by STAC</comment></kappa_collect_settings>")
        self.writeKappaSettings()


    def checkParameters(self):
        """
        Checks the data input object
        """
        # Checks the mandatory parameters:
        self.checkMandatoryParameters(self.getDataInput("inputBest")[0].getBestFileContentPar(), "bestfileContentPar")


    def fetchOutput(self):
        """
        method for reading back the specific output
        """
        self.xsKappaAlignmentRequest = kappa_alignment_request()
        self.xsKappaAlignmentRequest = kappa_alignment_request.parseFile(os.path.join(self.getWorkingDirectory(), "DNA_kappa_alignment_request"))
        return self.xsKappaAlignmentRequest


    def generateExecutiveSummary(self, _oedPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginSTACOrientationv2_0.generateExecutiveSummary")
        self.addExecutiveSummaryLine("<!--SUMMARY_BEGIN-->")
        if (self.getStringVersion() is not None):
            self.addExecutiveSummaryLine(self.getStringVersion() + " by Sandor Brockhauser")

        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.xsKappaAlignmentRequest.getComment())
        self.addExecutiveSummaryLine("----------------------------------------------------------------------------")
        self.addExecutiveSummaryLine("--v1-----------v2-------------Close--------------Comment--------------------")
        oxsDataKappaOrientationList = self.xsKappaAlignmentRequest.getDesired_orientation()
        for oxsDataPossible_orientation in oxsDataKappaOrientationList:
            self.addExecutiveSummaryLine("%13s %13s : %7s %45s" % \
                                          (oxsDataPossible_orientation.getV1(), \
                                            oxsDataPossible_orientation.getV2(), \
                                            oxsDataPossible_orientation.getClose(), \
                                            oxsDataPossible_orientation.getComment()))
        self.addExecutiveSummaryLine("----------------------------------------------------------------------------")
        self.addExecutiveSummaryLine("<!--SUMMARY_END-->")



