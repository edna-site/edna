#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
from EDVerbose                  import EDVerbose
from EDPluginExecProcessScript  import EDPluginExecProcessScript
from EDMessage                  import EDMessage
from XSDataSaxsv1_0             import XSDataInputSaxsDelMetadatav1_0
from XSDataSaxsv1_0             import XSDataResultSaxsDelMetadatav1_0

class EDPluginExecSaxsDelMetadatav1_0(EDPluginExecProcessScript):
    """
    Wrapper for program /sware/exp/saxs/bin/edfheaderdelkey
    
/sware/exp/saxs/edf/ubuntu1004/edfheaderdelkey <level> <verbose> <block> <chain> <key> [<filename>]

  EXAMPLE: Delete header key SampleConcentration 
          (level=0|1|2|..., verbose=0|1|2, block and chain are usually 1, key="string")
          edfheaderdelkey 0 1 1 1 SampleConcentration *ccd

    Remove a metadata called key.
    verbose is set to 2 if EDVerbose.isVerboseDebug 


    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsDelMetadatav1_0)
        self.strImage = None
        self.strKey = None
#        self.strValue = None



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsDelMetadatav1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImage(), "Input image is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsDelMetadatav1_0.preProcess")
        self.strImage = self.getDataInput().getInputImage().getPath().getValue()
        if not os.path.isfile(self.strImage):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", self.strImage)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        if self.getDataInput().getKey() is not None:
            self.strKey = self.getDataInput().getKey().getValue()
        else:
            return #Nothing to delete
#        if self.getDataInput().getValue() is not None:
#            self.strKey = self.getDataInput().getValue().getValue()

        self.generateEdfheaderdelkey2DCommands()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsDelMetadatav1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSaxsDelMetadatav1_0()
        xsDataResult.setOutputImage(self.getDataInput().getInputImage())
        self.setDataOutput(xsDataResult)


    def generateEdfheaderdelkey2DCommands(self):
        """
        Generate the command line
        """
        EDVerbose.DEBUG("*** EDPluginExecSaxsDelMetadatav1_0.generateEdfheaderdelkeyCommands")
        if EDVerbose.isVerboseDebug():
            strOptions = "0 2 1 1 '%s' '%s'" % (self.strKey, self.strImage)
        else:
            strOptions = "0 0 1 1 '%s' '%s'" % (self.strKey, self.strImage)

        EDVerbose.DEBUG("edfheaderdelkey " + strOptions)
        self.setScriptCommandline(strOptions)
