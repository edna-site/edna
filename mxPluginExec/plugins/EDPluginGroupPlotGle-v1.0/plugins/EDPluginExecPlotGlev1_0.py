# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
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
__date__ = "20120712"
__status__ = "production"

import os, tempfile, numpy, threading, shlex

from EDPluginExec import EDPluginExec
from EDUtilsFile import EDUtilsFile
from EDUtilsArray import EDUtilsArray
from EDUtilsPlatform import EDUtilsPlatform


from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

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
        self.listPlot = []


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
            strPlotMtvPath = xsDataInput.filePlotMtv.path.value
            if os.path.exists(strPlotMtvPath):
                strPlotMtv = EDUtilsFile.readFile(strPlotMtvPath)
                xsDataPlotSet = self.readPlotMtv(strPlotMtv)
            else:
                self.ERROR("Path to plt mtv file does not exist: %s" % strPlotMtvPath)
                self.setFailure()
                return
        else:
            xsDataPlotSet = xsDataInput.plotSet
        # Prepare input script
        iIndex = 1
        for xsDataPlot in xsDataPlotSet.plot:
            if xsDataPlot.xsize is None:
                xsDataPlot.xsize = 10
            if xsDataPlot.ysize is None:
                xsDataPlot.ysize = 10
            if iIndex in [1,5,8]:
                xsDataPlot.keypos = "tl"
            elif iIndex in [2,4,6]:
                xsDataPlot.keypos = "tr"
            elif iIndex in [3]:
                xsDataPlot.keypos = "br"
            elif iIndex in [7]:
                xsDataPlot.keypos = "bl"
            if iIndex == 4:
                xsDataPlot.xmax = 500
            strPlotFile = os.path.join(self.getWorkingDirectory(), "plot%d" % iIndex)
            strGle = self.prepareGleGraph(xsDataPlot)
            EDUtilsFile.writeFile(strPlotFile+".gle", strGle)
            self.listPlot.append(strPlotFile)
            iIndex += 1
        
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecPlotGlev1_0.process")
        for strPath in self.listPlot:
            strCommand = "gle -verbosity 0 -r 150 -d jpg %s.gle" % strPath
            # Copied from EDPluginExecProcess
            self.DEBUG(self.getBaseName() + ": Processing")
            timer = threading.Timer(float(self.getTimeOut()), self.kill)
            timer.start()
            self.__subprocess = EDUtilsPlatform.Popen(shlex.split(str(EDUtilsPlatform.escape(strCommand))),
                                                   cwd=self.getWorkingDirectory())
            self.__iPID = self.__subprocess.pid
            self.__strExecutionStatus = str(self.__subprocess.wait())
            timer.cancel()            

    def kill(self):
        self.WARNING("I will kill subprocess %s pid= %s" % (self.__subprocess, self.__iPID))
        EDUtilsPlatform.kill(self.__iPID)
        self.DEBUG("EDPluginExecProcess.process ========================================= ERROR! ================")
        errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginExecProcess.process', self.getClassName(), "Timeout ")
        self.error(errorMessage)
        self.addErrorMessage(errorMessage)
        raise RuntimeError, errorMessage

        
    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecPlotGlev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPlotGle()
        for strPath in self.listPlot:
            strPathJpg = strPath + ".jpg"
            if os.path.exists(strPathJpg):
                xsDataResult.addFileGraph(XSDataFile(XSDataString(strPathJpg)))
        self.setDataOutput(xsDataResult)
    


    def prepareGleGraph(self, _xsDataPlot):
        strGraph = ""
        if _xsDataPlot.xsize != None and _xsDataPlot.ysize != None:
            strGraph += "size %f %f\n" % (_xsDataPlot.xsize, _xsDataPlot.ysize)
        strGraph += "begin graph\n"
        strGraph += "  title \"%s\"\n" % _xsDataPlot.title
        strGraph += "  xtitle \"%s\"\n" % _xsDataPlot.xtitle
        strGraph += "  ytitle \"%s\"\n" % _xsDataPlot.ytitle
        if _xsDataPlot.xmin != None or _xsDataPlot.xmax != None:
            strGraph += "  xaxis "
            if _xsDataPlot.xmin != None:
                strGraph += "min %f " % _xsDataPlot.xmin
            if _xsDataPlot.xmax != None:
                strGraph += "max %f " % _xsDataPlot.xmax
            strGraph += "\n"
        if _xsDataPlot.ymin != None or _xsDataPlot.ymax != None:
            strGraph += "  yaxis "
            if _xsDataPlot.ymin != None:
                strGraph += "min %f " % _xsDataPlot.ymin
            if _xsDataPlot.ymax != None:
                strGraph += "max %f " % _xsDataPlot.ymax
            strGraph += "\n"
        if _xsDataPlot.keypos is None:
            strGraph += "  key pos tl hei 0.25\n"
        else:
            strGraph += "  key pos %s hei 0.25\n" % _xsDataPlot.keypos
        iIndex = 1
        for xsDataGraph in _xsDataPlot.graph:
            strTmpDataPath = tempfile.mkstemp(prefix="data_", suffix=".dat", \
                                              dir=self.getWorkingDirectory(), text=True)[1]
            numpyData = EDUtilsArray.xsDataToArray(xsDataGraph.data, _bForceNoNumpy=True)
            numpy.savetxt(strTmpDataPath, numpyData, delimiter=" ")
            #EDUtilsFile.writeFile(strTmpDataPath, strData)
            strGraph += "  data %s\n" % strTmpDataPath
            strGraph += "  d%d line " % iIndex
            if xsDataGraph.lineColor != None:
                strGraph += " color %s " % xsDataGraph.lineColor
            if xsDataGraph.lineStyle != None:
                strGraph += " lstyle %d " % xsDataGraph.lineStyle
            if xsDataGraph.lineWidth != None:
                strGraph += " lwidth %f " % xsDataGraph.lineWidth
            if xsDataGraph.markerType != None:
                strGraph += " marker %s " % xsDataGraph.markerType
            if xsDataGraph.markerColor != None:
                strGraph += " color %s " % xsDataGraph.markerColor
            if xsDataGraph.label != None:
                strGraph += " key \"%s\" " % xsDataGraph.label
            strGraph += "\n"
            iIndex+=1
        strGraph += "end graph\n"
        return strGraph


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
                xsDataPlot.title = strTopLabel
            elif strLine.find("subtitle") != -1:
                strSubTitle = strLine.split("'")[1]
                xsDataPlot.subTitle = strSubTitle
            elif strLine.find("xmin") != -1:
                strXMin = strLine.split("=")[1]
                xsDataPlot.xmin = float(strXMin) 
            elif strLine.find("ymin") != -1:
                strYMin = strLine.split("=")[1]
                xsDataPlot.ymin = float(strYMin) 
            elif strLine.find("xmax") != -1:
                strXMax = strLine.split("=")[1]
                xsDataPlot.xmax = float(strXMax) 
            elif strLine.find("ymax") != -1:
                strYMax = strLine.split("=")[1]
                xsDataPlot.ymax = float(strYMax) 
            elif strLine.find("xlabel") != -1:
                strXLabel = strLine.split("'")[1]
                xsDataPlot.xtitle = strXLabel 
            elif strLine.find("ylabel") != -1:
                if strLine.find("'") != -1:
                    strYLabel = strLine.split("'")[1]
                else:
                    strYLabel = strLine.split("=")[1]
                xsDataPlot.ytitle = strYLabel
            elif strLine.startswith("# Curve"):
                if xsDataGraph is not None:
                    xsDataGraph.data = EDUtilsArray.arrayToXSData(listData,_bForceNoNumpy=True)
                xsDataGraph = XSDataGraph()
                xsDataPlot.addGraph(xsDataGraph)
                listData = []
            elif strLine.find("linetype") != -1:
                strLineType = strLine.split("=")[1]
                xsDataGraph.lineStyle = self.lineTypePlotMtv(int(strLineType)) 
            elif strLine.find("linewidth") != -1:
                strLineWidth = strLine.split("=")[1]
                xsDataGraph.lineWidth = float(strLineWidth)*0.02 
            elif strLine.find("linecolor") != -1:
                iLineColorCode = int(strLine.split("=")[1])
                xsDataGraph.lineColor = self.colorPlotMtv(iLineColorCode)
            elif strLine.find("linelabel") != -1:
                strLineLabel = strLine.split("'")[1]
                xsDataGraph.label = strLineLabel 
            elif strLine.find("markertype") != -1:
                strMarkerType = strLine.split("=")[1]
                xsDataGraph.markerType = self.markerTypePlotMtv(int(strMarkerType)) 
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
                    self.DEBUG("Couldn't convert %s to data point" % strLine)
        # Last data
        if xsDataGraph is not None and listData != []:
            xsDataGraph.data =  EDUtilsArray.arrayToXSData(listData,_bForceNoNumpy=True)
        return xsDataPlotSet


    def colorPlotMtv(self, _iColor):
        iColor = _iColor
        if iColor > 10:
           iColor -= 10 
        strLineColor = None
        if iColor == 1:
            strLineColor = "yellow"
        if iColor == 2:
            strLineColor = "blue"
        if iColor == 3:
            strLineColor = "green"
        elif iColor == 4:
            strLineColor = "red"
        elif iColor == 5:
            strLineColor = "darkblue"
        elif iColor == 6:
            strLineColor = "orange"
        elif iColor == 7:
            strLineColor = "pink"
        elif iColor == 8:
            strLineColor = "lightpink"
        elif iColor == 9:
            strLineColor = "cyan"
        elif iColor == 10:
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
        iLineTypeGle = _iLineType
        if iLineTypeGle > 9:
            iLineTypeGle = 1
        return iLineTypeGle
    
    def markerTypePlotMtv(self, _iMarkerType):
        #0=None
        #1=Dot
        #2=Cross
        #3=X
        #4=White Square
        #5=Black Square
        #6=White Diamond
        #7=Black Diamond
        #8=White Triangle
        #9=Black Triangle
        #10=White Inverted Triangle
        #11=Black Inverted Triangle
        #12=White Circle
        #13=Black Circle
        strGleMarker = None
        if _iMarkerType == 10:
            strGleMarker = "triangle"
        return strGleMarker