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


from EDImportLib import EDVerbose
from EDImportLib import EDString
from EDImportLib import EDList
from EDImportLib import EDDiskExplorer

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration


class EDPluginSTACv10(EDPluginExecProcessScript):


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginSTACv10.preProcess")
        xsPluginItem = self.getConfiguration()
        self.addListCommandPreExecution("export STACDIR=%s" % EDConfiguration.getStringParamValue(xsPluginItem, "STACDIR"))
        self.addListCommandPreExecution("export BCMDEF=%s" % EDConfiguration.getStringParamValue(xsPluginItem, "BCMDEF"))
        self.addListCommandPreExecution("export RUNDIR=%s" % self.getWorkingDirectory())
        self.setScriptCommandline("stac.core.STAC_DNA_listener %s -%s/" % (self.getSTACcommand(), self.getWorkingDirectory()))


    def writeKappaSettings(self):
        # future version for getting motor positions related to images under processing
        # checking in order:
        # - value got as input
        # - mosflm.descr file in process subdir (if BCM (like mxcube) registered it)
        # - {imageTemplate}_kappa_settings.xml file (if BCM (like DNA) registered it)
        # - read it now (and try to register as {imageTemplate}_kappa_settings.xml)
        # - just use the datum (0,0,0)

        # code for the DNA version
        #
        # after indexing, the actual kappa settings must be also updated
        #
        kappa_settings = XSD.Kappa_collect_settings()
        try:
            current_fileinfo = SchedulerDNAConfig.getDna_context().getCurrent_fileinfo()
            ksettingfile = os.path.join(current_fileinfo.getDirectory(), "ref-" + current_fileinfo.getTemplate() + "_kappa_settings.xml")
            #Messenger.log_write("KappaSettings from "+ksettingfile)
            istream = open(ksettingfile , "r")
            kapSet = istream.read()
            istream.close()
            #Messenger.log_write("KappaSettings: "+kapSet)
            kappa_settings.unmarshal(kapSet)
        except:
            kappa_settings = None
            #Messenger.log_write("KappaSettings could not be updated")
        mosflm.kappaSettings = kappa_settings

        f = open(actWorkingDir + 'DNA_STAC_Kappa_Settings', 'w')
        if not kappaSettings is None:
            f.write(kappaSettings.marshal())
        f.close()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginSTACv10.process")
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginSTACv10"):
             raise ExectuteAbstractPluginError

    def getSTACcommand(self, _edObject=None):
        # It should not be possible to execute this abstract plugin
        if (self.getPluginName() == "EDPluginSTACv10"):
             raise ExectuteAbstractPluginError


    def checkParameters(self):
        """
        Checks the mandatory parameters for all XDS plugins
        """
        self.DEBUG("EDPluginSTACv10.checkParameters")

    def postProcess(self, _edObject=None):
        """
        reading back and genericly process the output
        """
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginSTACv10.postProcess")
        OutputData = self.fetchOutput()

        self.DEBUG("EDPluginSTACv10.postProcess: " + EDString(OutputData))
        if (OutputData is not None):
            self.setDataOutput(OutputData)

    def fetchOutput(self):
        """
        abstract method for reading back the specific output
        """
        raise Exception("This method must be implemented by the children")

