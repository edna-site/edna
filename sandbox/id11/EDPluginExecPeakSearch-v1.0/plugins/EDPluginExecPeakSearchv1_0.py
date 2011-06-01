# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       jerome Kieffer
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

__authors__ = [ "Jérôme Kieffer", "Olof Svensson" ]
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataPeakSearchv1_0 import XSDataInputPeakSearch
from XSDataPeakSearchv1_0 import XSDataResultPeakSearch
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString


class EDPluginExecPeakSearchv1_0(EDPluginExecProcessScript):
    """
    Execution plugin for running the Fable program peaksearch.py
    """
    

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputPeakSearch)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecProcessScriptPeakSearchv1_0.checkParameters")
        xsdIn = self.getDataInput()
        self.checkMandatoryParameters(xsdIn, "Data Input is None")
        self.checkMandatoryParameters(xsdIn.getStem(), "No Stem in input")
        self.checkMandatoryParameters(xsdIn.getIndexMin(), "No Min index")
        self.checkMandatoryParameters(xsdIn.getIndexMax(), "no max index")
        self.checkMandatoryParameters(xsdIn.getThreshold(), "no threshold")

    
    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecPeakSearchv1_0.preProcess")
        self.generateCommandLine()
        
        
    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecPeakSearchv1_0.postProcess")
        # Create some output data
        xsDataResult = self.findOutputFiles()
        self.setDataOutput(xsDataResult)

    
    def generateCommandLine(self):
        """
        generate the options command line for the peak search program
        """
        xsDataInput = self.getDataInput()
        strCmd = ""
        strCmd += "-n %s" % xsDataInput.getStem().getValue()
        strCmd += " -f %i" % xsDataInput.getIndexMin().getValue()
        strCmd += " -l %i" % xsDataInput.getIndexMax().getValue()
        for xsDataDoubleThreshold in xsDataInput.getThreshold():
            strCmd += " -t %f" % xsDataDoubleThreshold.getValue()
        if xsDataInput.getImageFormat() != None:
            strCmd += " -F %s" % xsDataInput.getImageFormat().getValue()
        if xsDataInput.getNumberOfDigits() != None:
            strCmd += " --ndigits %d" % xsDataInput.getNumberOfDigits().getValue()
        if xsDataInput.getOutputStem() != None:
            strCmd += " -o %s" % xsDataInput.getOutputStem().getValue()
        self.setScriptCommandline(strCmd)
        
    
    def findOutputFiles(self):
        strWorkingDir = self.getWorkingDirectory()
        xsDataInput = self.getDataInput()
        if xsDataInput.getOutputStem() != None:
            strOutputStem = xsDataInput.getOutputStem().getValue()
        else:
            strOutputStem = "peaks"
        xsDataResult = XSDataResultPeakSearch()
        for xsDataDoubleThreshold in xsDataInput.getThreshold():
            strFileName2D = os.path.join(strWorkingDir, "%s_t%d.spt" % (strOutputStem, int(xsDataDoubleThreshold.getValue())))
            strFileName3D = os.path.join(strWorkingDir, "%s_t%d.flt" % (strOutputStem, int(xsDataDoubleThreshold.getValue())))
            if os.path.exists(strFileName2D):
                xsDataResult.addPeakFile2D(XSDataFile(path=XSDataString(value=strFileName2D)))
            else:
                self.ERROR("Cannot find output file %s!" % strFileName2D)
                self.setFailure()
            if os.path.exists(strFileName3D):
                xsDataResult.addPeakFile3D(XSDataFile(path=XSDataString(value=strFileName3D)))
            else:
                self.ERROR("Cannot find output file %s!" % strFileName3D)
                self.setFailure()
        return xsDataResult
                                
