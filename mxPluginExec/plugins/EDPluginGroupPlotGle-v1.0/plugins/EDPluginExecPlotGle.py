# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDPluginExec import EDPluginExec

from XSDataPlotGlev1_0 import XSDataInputPlotGle
from XSDataPlotGlev1_0 import XSDataResultPlotGle

class EDPluginExecPlotGle(EDPluginExec ):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__(self ):
        """
        """
        EDPluginExec.__init__(self )
        self.setXSDataInputClass(XSDataInputPlotGle)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecPlotGle.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecPlotGle.preProcess")
        
        
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecPlotGle.process")

        
    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecPlotGle.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPlotGle()
        self.setDataOutput(xsDataResult)
    
