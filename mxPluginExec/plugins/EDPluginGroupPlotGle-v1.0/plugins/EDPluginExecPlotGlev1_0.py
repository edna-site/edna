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
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataString

from XSDataPlotGlev1_0 import XSDataGraph
from XSDataPlotGlev1_0 import XSDataPlot
from XSDataPlotGlev1_0 import XSDataPlotSet
from XSDataPlotGlev1_0 import XSDataInputPlotGle
from XSDataPlotGlev1_0 import XSDataResultPlotGle

class EDPluginExecPlotGlev1_0(EDPluginExec ):
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
        self.DEBUG("EDPluginExecPlotGlev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecPlotGlev1_0.preProcess")
        # Check if we have a plotmtv input file
        xsDataInput = self.getDataInput()
        if xsDataInput.filePlotMtv is not None:
            strPlotMtv = EDUtilsFile.readFile(xsDataInput.filePlotMtv.path.value)
            xsDataPlotSet = self.readPlotMtv(strPlotMtv)
        else:
            xsDataPlot = xsDataInput.plotSet
        
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecPlotGlev1_0.process")

        
    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecPlotGlev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPlotGle()
        self.setDataOutput(xsDataResult)
    

    def readPlotMtv(self, _strPlotMtv):
        xsDataPlotSet = XSDataPlotSet()
        strLines = _strPlotMtv.split("\n")
        for iIndex in range(len(strLines)):
            strLine = strLines[iIndex]
            if strLine.find("$ DATA=") != -1:
                xsDataPlot = XSDataPlot()
                strType = strLine.split("$ DATA=")[1]
                xsDataPlot.plotType = strType
                xsDataPlotSet.addPlot(xsDataPlot)
            elif strLine.find("toplabel") != -1:
                strTopLabel = strLine.split("'")[1]
                xsDataPlot.topLabel = strTopLabel
            elif strLine.find("subtitle") != -1:
                strSubTitle = strLine.split("'")[1]
                xsDataPlot.subTitle = strSubTitle
            elif strLine.find("xmin") != -1:
                strXMin = strLine.split("=")[1]
                xsDataPlot.xMin = float(strXMin) 
            elif strLine.find("ymin") != -1:
                strYMin = strLine.split("=")[1]
                xsDataPlot.yMin = float(strYMin) 
            elif strLine.find("xlabel") != -1:
                strXLabel = strLine.split("'")[1]
                xsDataPlot.xLabel = strXLabel 
            elif strLine.find("ylabel") != -1:
                if strLine.find("'") != -1:
                    strYLabel = strLine.split("'")[1]
                else:
                    strYLabel = strLine.split("=")[1]
                xsDataPlot.yLabel = strYLabel
            elif strLine.startswith("# Curve"):
                xsDataGraph = XSDataGraph()
                xsDataPlot.addGraph(xsDataGraph)
            elif strLine.find("linetype") != -1:
                strLineType = strLine.split("=")[1]
                xsDataGraph.lineType = int(strLineType) 
            elif strLine.find("linewidth") != -1:
                strLineWidth = strLine.split("=")[1]
                xsDataGraph.lineWidth = int(strLineWidth) 
            elif strLine.find("linecolor") != -1:
                iLineColorCode = int(strLine.split("=")[1])
                strLineColor = None
                if iLineColorCode == 3:
                    strLineColor = "green"
                elif iLineColorCode == 4:
                    strLineColor = "red"
                elif iLineColorCode == 5:
                    strLineColor = "blue"
                elif iLineColorCode == 6:
                    strLineColor = "orange"
                elif iLineColorCode == 7:
                    strLineColor = "violet"
                elif iLineColorCode == 8:
                    strLineColor = "grey"
                elif iLineColorCode == 9:
                    strLineColor = "brown"
                elif iLineColorCode == 10:
                    strLineColor = "cyan"
                xsDataGraph.lineColor = strLineColor
        return xsDataPlotSet
        