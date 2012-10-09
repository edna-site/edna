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


from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic
#import XSDataMXv2


class EDPluginSTACv2_0(EDPluginExecProcessScript):


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        EDFactoryPluginStatic.loadModule("XSDataMXv1")
        EDFactoryPluginStatic.loadModule("XSDataMXv2")
        from XSDataMXv2 import XSDataCollection
        self.setXSDataInputClass(XSDataCollection, "dataCollection")
        self.__pyStrBCMDEF = None


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginSTACv2_0.preProcess")
        self.addListCommandPreExecution("export STACDIR=%s" % self.config.get("STACDIR"))
        if (self.__pyStrBCMDEF is None):
            self.__pyStrBCMDEF = self.config.get("BCMDEF")
        self.DEBUG("EDPluginSTACv2_0.preProcess: BCMDEF set to %s" % self.__pyStrBCMDEF)
        self.addListCommandPreExecution("export BCMDEF=%s" % self.__pyStrBCMDEF)
        self.addListCommandPreExecution("export RUNDIR=%s" % self.getWorkingDirectory())
        self.setScriptCommandline("stac.core.STAC_DNA_listener %s -%s/ %s" % (self.getSTACcommand(), self.getWorkingDirectory(), self.getSTACparams()))

    def setBCMDEF(self, _pyStrBCMDEF):
        self.__pyStrBCMDEF = _pyStrBCMDEF

    def getBCMDEF(self, _pyStrBCMDEF):
        return self.__pyStrBCMDEF



    def writeBestfilePar(self, fname, content):
        '''
        Writing a bestfile.par for STAC to describe the xtal (orinetation,spacegroup,etc.)
        '''
        #version reusing a pregenerated bestfile.par
        #EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "bestfile.par" ), self.m_xsDataInput.getBestFileContentPar().getValue())
        EDUtilsFile.writeFile(fname, content)

        #version using indexing result


    def writeKappaConfig(self):
        '''
        Updating the STAC calibration settings
        '''


    def writeKappaSettings(self):
        '''
        # future version for getting motor positions related to images under processing
        # checking in order:
        # - value got as input
        # - mosflm.descr file in process subdir (if BCM (like mxcube) registered it)
        # - {imageTemplate}_kappa_settings.xml file (if BCM (like DNA) registered it)
        # - read it now (and try to register as {imageTemplate}_kappa_settings.xml)
        # - just use the datum (0,0,0)
        '''

        #code for using a predefined datum (0;0;0)
        #EDUtilsFile.writeFile( EDDiskExplorer.mergePath( self.getWorkingDirectory(), "DNA_STAC_Kappa_Settings" ), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_collect_settings><motorSettings><motorName>Omega</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>Kappa</motorName><motorValue>0.000000</motorValue></motorSettings><motorSettings><motorName>Phi</motorName><motorValue>0</motorValue></motorSettings><motorSettings><motorName>X</motorName><motorValue>0.261444</motorValue></motorSettings><motorSettings><motorName>Y</motorName><motorValue>-0.085559</motorValue></motorSettings><motorSettings><motorName>Z</motorName><motorValue>0.659333</motorValue></motorSettings><comment>BCM query performed by STAC</comment></kappa_collect_settings>")

        # gonio settings from DC descriptor object
        EDFactoryPluginStatic.loadModule("XSDataMXv2")
        #import XSDataMXv2
        #dc = XSDataMXv2.XSDataCollection()
        from XSDataMXv2 import XSDataCollection
        dc = XSDataCollection()
        dc = self.getDataInput("dataCollection")[0]
        omega = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getBaseaxissetting()
        [kappa, phi] = dc.getXSSubWedge()[0].getXSRotationalGoniostatSetting().getAxissetting()
        EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), "DNA_STAC_Kappa_Settings"), "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><kappa_collect_settings><motorSettings><motorName>Omega</motorName><motorValue>%e</motorValue></motorSettings><motorSettings><motorName>Kappa</motorName><motorValue>%e</motorValue></motorSettings><motorSettings><motorName>Phi</motorName><motorValue>%e</motorValue></motorSettings><motorSettings><motorName>X</motorName><motorValue>0.261444</motorValue></motorSettings><motorSettings><motorName>Y</motorName><motorValue>-0.085559</motorValue></motorSettings><motorSettings><motorName>Z</motorName><motorValue>0.659333</motorValue></motorSettings><comment>BCM query performed by STAC</comment></kappa_collect_settings>" % (omega.getValue(), kappa.getValue(), phi.getValue()))

        '''
        # code for the DNA version
        #
        # after indexing, the actual kappa settings must be also updated
        #
        kappa_settings=XSD.Kappa_collect_settings()
        try:
            current_fileinfo=SchedulerDNAConfig.getDna_context().getCurrent_fileinfo()
            ksettingfile=os.path.join(current_fileinfo.getDirectory(), "ref-"+current_fileinfo.getTemplate()+"_kappa_settings.xml")
            #Messenger.log_write("KappaSettings from "+ksettingfile)
            istream = open(ksettingfile , "r")
            kapSet=istream.read()
            istream.close()
            #Messenger.log_write("KappaSettings: "+kapSet)
            kappa_settings.unmarshal(kapSet)
        except:
            kappa_settings=None
            #Messenger.log_write("KappaSettings could not be updated")
        mosflm.kappaSettings = kappa_settings
        
        f=open(actWorkingDir+'DNA_STAC_Kappa_Settings','w')
        if not kappaSettings is None:
            f.write(kappaSettings.marshal())
        f.close()
        '''


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginSTACv2_0.process")
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginSTACv2_0"):
             raise ExectuteAbstractPluginError

    def getSTACcommand(self, _edObject=None):
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginSTACv2_0"):
             raise ExectuteAbstractPluginError

    def getSTACparams(self, _edObject=None):
        return ""


    def checkParameters(self):
        """
        Checks the mandatory parameters for all XDS plugins
        """
        self.DEBUG("EDPluginSTACv2_0.checkParameters")

    def postProcess(self, _edObject=None):
        """
        reading back and genericly process the output
        """
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginSTACv2_0.postProcess")
        OutputData = self.fetchOutput()

        self.DEBUG("EDPluginSTACv2_0.postProcess: " + str(OutputData))
        if (OutputData is not None):
            self.setDataOutput(OutputData)

    def fetchOutput(self):
        """
        abstract method for reading back the specific output
        """
        raise Exception("This method must be implemented by the children")

