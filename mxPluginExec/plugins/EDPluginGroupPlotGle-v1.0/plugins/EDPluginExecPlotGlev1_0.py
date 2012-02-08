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
from EDUtilsArray import EDUtilsArray

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
        xsDataGraph = None
        xsDataPlot = None
        listData = []
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
            elif strLine.find("xmax") != -1:
                strXMax = strLine.split("=")[1]
                xsDataPlot.xMax = float(strXMax) 
            elif strLine.find("ymax") != -1:
                strYMax = strLine.split("=")[1]
                xsDataPlot.yMax = float(strYMax) 
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
                if xsDataGraph is not None:
                    xsDataGraph.data = EDUtilsArray.arrayToXSData(listData,_bForceNoNumpy=True)
                xsDataGraph = XSDataGraph()
                xsDataPlot.addGraph(xsDataGraph)
                listData = []
            elif strLine.find("linetype") != -1:
                strLineType = strLine.split("=")[1]
                xsDataGraph.lineType = int(strLineType) 
            elif strLine.find("linewidth") != -1:
                strLineWidth = strLine.split("=")[1]
                xsDataGraph.lineWidth = int(strLineWidth) 
            elif strLine.find("linecolor") != -1:
                iLineColorCode = int(strLine.split("=")[1])
                xsDataGraph.lineColor = self.colorPlotMtv(iLineColorCode)
            elif strLine.find("linelabel") != -1:
                strLineLabel = strLine.split("'")[1]
                xsDataGraph.lineLabel = strLineLabel 
            elif strLine.find("markertype") != -1:
                strMarkerType = strLine.split("=")[1]
                xsDataGraph.markerType = int(strMarkerType) 
            elif strLine.find("markercolor") != -1:
                iMarkerColor = int(strLine.split("=")[1])
                xsDataGraph.markerColor = self.colorPlotMtv(iMarkerColor) 
            else:
                # Try to convert data points
                try:
                    strListLine = strLine.split()
                    fXValue = float(strListLine[-2])
                    fYValue = float(strListLine[-1])
                    listData.append([fXValue, fYValue])
                except:
                    self.warning("Couldn't convert %s to data point" % strLine)
        # Last data
        if xsDataGraph is not None and listData != []:
            xsDataGraph.data =  EDUtilsArray.arrayToXSData(listData,_bForceNoNumpy=True)
        return xsDataPlotSet


    def colorPlotMtv(self, _iColor):
        strLineColor = None
        if _iColor == 1:
            strLineColor = "yellow"
        if _iColor == 2:
            strLineColor = "blue"
        if _iColor == 3:
            strLineColor = "green"
        elif _iColor == 4:
            strLineColor = "red"
        elif _iColor == 5:
            strLineColor = "darkblue"
        elif _iColor == 6:
            strLineColor = "orange"
        elif _iColor == 7:
            strLineColor = "pink"
        elif _iColor == 8:
            strLineColor = "lightpink"
        elif _iColor == 9:
            strLineColor = "cyan"
        elif _iColor == 10:
            strLineColor = "brown"
        return strLineColor
    
    def lineTypePlotMtv(self, _iLineType):
        # 0=None
        # 1=Solid
        # 2=Dashed
        # 3=Dotted
        # 4=Dot-Dash
        # 5=Long-Dots
        # 6=Double-Dot
        # 7=Long-Dash
        # 8=Sparse Dot-Dash
        # 9=Triple-Dot
        #10=Dot-Dot-Dash
        return None