#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS 2010
#
#    Principal author:       Mark Basham
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

__author__="Mark Basham"
__license__ = "GPLv3+"
__copyright__ = "DLS 2010"

import os
import time

from EDImportLib import EDVerbose

from EDPluginExecProcessScript       import EDPluginExecProcessScript

from XSDataTomo import XSDataInputTomography
from XSDataTomo import XSDataResultTomography

class EDPluginExecTomographyv10( EDPluginExecProcessScript ):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__( self ):
        """
        """
        EDPluginExecProcessScript.__init__( self )
        self.setXSDataInputClass( XSDataInputTomography )


    def checkParameters( self ):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG( "*** EDPluginExecTomographyv10.checkParameters")
        self.checkMandatoryParameters( self.getDataInput(),"Data Input is None" )

    
    def preProcess( self, _edObject = None ):
        EDPluginExecProcessScript.preProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecTomographyv10.postProcess")
        
        xsDataInputTomography = self.getDataInput()
        
        args = {}
        args["-w"] = str(xsDataInputTomography.getImageWidth().getValue())
        args["-l"] = str(xsDataInputTomography.getChunkHeight().getValue())
        args["-J"] = str(xsDataInputTomography.getJobName().getValue())
        args["-s"] = str(xsDataInputTomography.getNumberOfSegments().getValue())
        args["-p"] = str(xsDataInputTomography.getNumberOfProjectionsPerSegment().getValue())
        args["-G"] = ""
        args["-z"] = str(int(xsDataInputTomography.getTimeoutPollingInterval().getValue()))
        args["-Z"] = str(int(xsDataInputTomography.getTimeoutLength().getValue()))
        args["-b"] = str(xsDataInputTomography.getByteDepthOfImage().getValue())
        args["-U"] = str(xsDataInputTomography.getUniqueName().getValue())
        args["-v"] = ""
        args["-n"] = str(xsDataInputTomography.getNumberOfChunks().getValue())
        args["-I"] = xsDataInputTomography.getSettingsFileName().getPath().getValue()
        
        argString = " ".join(["%s %s" % (k,v) for k, v in args.items()])
        
        EDVerbose.DEBUG("Argument list is = %s" % argString)  

        self.addListCommandPreExecution("cd %s" % xsDataInputTomography.getImageDirectory().getPath().getValue() ) 
        self.setScriptCommandline(argString)
        self.addListCommandExecution("END") 
        
        # finaly get some parameters ready for when to stop the job
        strFinishFileName = "finish_r%s%s.txt" % (self.getDataInput().getJobName().getValue(), xsDataInputTomography.getUniqueName().getValue())
        self.strFinishPathName = os.path.join(self.getDataInput().getImageDirectory().getPath().getValue(),strFinishFileName)
        EDVerbose.DEBUG("finish job string name = %s" % self.strFinishPathName)   
        
        # and then in fact remove it, if this is a second go at the reconstruction for example
        # however it may not exist
        try :
            os.remove(self.strFinishPathName)
        except :
            pass   

        
    def postProcess( self, _edObject = None ):
        EDPluginExecProcessScript.postProcess( self )
        EDVerbose.DEBUG( "*** EDPluginExecTomographyv10.postProcess")
        
        #poll until the file "finish_rEDNATESTEDNATESTUNIQUE.txt" exists

        intWaitTime = 0
        fileExists = False
        while not fileExists :
            try :
                os.stat(self.strFinishPathName)
                fileExists = True
            except OSError :
                time.sleep(10)
                intWaitTime += 10
                EDVerbose.DEBUG( "Waiting for Task to complete for %d seconds" % intWaitTime)
        
        # Create some output data
        xsDataResult = XSDataResultTomography()
        
        self.setDataOutput( xsDataResult )
    
