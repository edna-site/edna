#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"



from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration

from EDPluginLabelitv1_1 import EDPluginLabelitv1_1

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble

from XSDataLabelitv1_1 import XSDataImageQualityIndicators
from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength
from XSDataLabelitv1_1 import XSDataResultDistlSignalStrength


class EDPluginDistlSignalStrengthThinClientv1_1(EDPluginExecProcessScript):
    """
    This plugin runs the labelit.distl command for pre-screening reference images.
    """
    
    CONF_DISTL_SIGNAL_STRENGTH_SERVER_HOST = "distlServerHost"
    CONF_DISTL_SIGNAL_STRENGTH_SERVER_PORT = "distlServerPort"
    CONF_PATH_TO_DISTL_SIGNAL_STRENGTH_SERVER = "pathToDistlServer"
    DEFAULT_SERVER_PORT = 8125

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDistlSignalStrength)
        self.strHostName = "localhost"
        self.iPortNumber = self.DEFAULT_SERVER_PORT


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginDistlSignalStrengthThinClientv1_1.configure")
        strHostName = self.getStringConfigurationParameterValue(self.CONF_DISTL_SIGNAL_STRENGTH_SERVER_HOST)
        if strHostName is not None:
            self.strHostName = strHostName
        iPortNumber = self.getIntegerConfigurationParameterValue(self.CONF_DISTL_SIGNAL_STRENGTH_SERVER_PORT)
        if iPortNumber is not None:
            self.iPortNumber = iPortNumber
        


    def preProcess(self, _edObject=None):
        """
        Sets up the Labelit command line
        """
        EDPluginExecProcessScript.preProcess(self, _edObject)
        self.DEBUG("EDPluginDistlSignalStrengthThinClientv1_1.preProcess...")
        self.xsDataImage = self.getDataInput().getReferenceImage()
        strCommandLine = self.xsDataImage.getPath().getValue()
        strCommandLine += " %s" % self.strHostName
        strCommandLine += " %d" % self.iPortNumber
        self.setScriptCommandline(strCommandLine)
        self.addListCommandPreExecution("export PYTHONPATH=\"\" ")


    def postProcess(self, _edObject=None):
        """
        Parses the labelit.screen log file and the generated MOSFLM script
        """
        EDPluginExecProcessScript.postProcess(self, _edObject)
        self.DEBUG("EDPluginDistlSignalStrengthThinClientv1_1.postProcess")
        strLabelitDistlLog = self.readProcessLogFile()
        if (strLabelitDistlLog is None):
            strErrorMessage = "EDPluginDistlSignalStrengthThinClientv1_1.postProcess : Could not read the Labelit log file"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataImageQualityIndicators = self.parseLabelitDistlOutput(strLabelitDistlLog)
            xsDataImageQualityIndicators.setImage(self.xsDataImage)
            xsDataResultDistlSignalStrength = XSDataResultDistlSignalStrength()
            xsDataResultDistlSignalStrength.setImageQualityIndicators(xsDataImageQualityIndicators)
            self.setDataOutput(xsDataResultDistlSignalStrength)


    def parseLabelitDistlOutput(self, _strLabelitDistlLogText):
        self.DEBUG("EDPluginDistlSignalStrengthThinClientv1_1.parseLabelitDistlOutput")
        xsDataImageQualityIndicators = None
        if _strLabelitDistlLogText is not None:
            xsDataImageQualityIndicators = XSDataImageQualityIndicators()
            for strLine in _strLabelitDistlLogText.split("\n"):
                if strLine.find("Spot Total") != -1:
                    iSpotTotal = int(strLine.split()[-1])
                    xsDataImageQualityIndicators.setSpotTotal(XSDataInteger(iSpotTotal))
                elif strLine.find("Method-2 Resolution Total") != -1:
                    iInResTotal = int(strLine.split()[-1])
                    xsDataImageQualityIndicators.setInResTotal(XSDataInteger(iInResTotal))
                elif strLine.find("Good Bragg Candidates") != -1:
                    iGoodBraggCandidates = int(strLine.split()[-1])
                    xsDataImageQualityIndicators.setGoodBraggCandidates(XSDataInteger(iGoodBraggCandidates))
                elif strLine.find("Ice Rings") != -1:
                    iIceRings = int(strLine.split()[-1])
                    xsDataImageQualityIndicators.setIceRings(XSDataInteger(iIceRings))
                elif strLine.find("Method 1 Resolution") != -1:
                    fMethod1Res = float(strLine.split()[-1])
                    xsDataImageQualityIndicators.setMethod1Res(XSDataDouble(fMethod1Res))
                elif strLine.find("Method 2 Resolution") != -1:
                    if strLine.split()[4] != "None":
                        fMethod2Res = float(strLine.split()[-1])
                        xsDataImageQualityIndicators.setMethod2Res(XSDataDouble(fMethod2Res))
                elif strLine.find("Maximum unit cell") != -1:
                    if strLine.split()[4] != "None":
                        fMaxUnitCell = float(strLine.split()[-1])
                        xsDataImageQualityIndicators.setMaxUnitCell(XSDataDouble(fMaxUnitCell))
                elif strLine.find("Saturation, Top 50 Peaks") != -1:
                    fPctSaturationTop50Peaks = float(strLine.split()[-2])
                    xsDataImageQualityIndicators.setPctSaturationTop50Peaks(XSDataDouble(fPctSaturationTop50Peaks))
                elif strLine.find("In-resolution overloaded spots") != -1:
                    iInResolutionOvrlSpots = int(strLine.split()[-1])
                    xsDataImageQualityIndicators.setInResolutionOvrlSpots(XSDataInteger(iInResolutionOvrlSpots))
                elif strLine.find("Total integrated signal, pixel-ADC units above local background") != -1:
                    fTotalIntegratedSignal = float(strLine.split()[-1])
                    xsDataImageQualityIndicators.setTotalIntegratedSignal(XSDataDouble(fTotalIntegratedSignal))
        return xsDataImageQualityIndicators


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the Labelit distl thin client plugin.
        """
        self.DEBUG("EDPluginDistlSignalStrengthThinClientv1_1.generateExecutiveSummary")
        xsDataImageQualityIndicators = self.getDataOutput().getImageQualityIndicators()
        self.addExecutiveSummaryLine("Execution of Labelit distl.thin_client successful.")
        self.addExecutiveSummaryLine("Image                   : %s" % xsDataImageQualityIndicators.getImage().getPath().getValue())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("distl.signal_strength results:")
        self.addExecutiveSummaryLine("Spot Total                : %d" % xsDataImageQualityIndicators.getSpotTotal().getValue())
        self.addExecutiveSummaryLine("In-Resolution Total       : %d" % xsDataImageQualityIndicators.getInResTotal().getValue())
        self.addExecutiveSummaryLine("Good Bragg Candidates     : %d" % xsDataImageQualityIndicators.getGoodBraggCandidates().getValue())
        if xsDataImageQualityIndicators.getTotalIntegratedSignal() is not None:
            self.addExecutiveSummaryLine("Total integrated signal, pixel-ADC units above local background : %.0f" % xsDataImageQualityIndicators.getTotalIntegratedSignal().getValue())
        self.addExecutiveSummaryLine("Ice Rings                 : %d" % xsDataImageQualityIndicators.getIceRings().getValue())
        self.addExecutiveSummaryLine("Method 1 Resolution       : %.2f [A]" % xsDataImageQualityIndicators.getMethod1Res().getValue())
        if xsDataImageQualityIndicators.getMethod2Res() is None:
            self.addExecutiveSummaryLine("Method 2 Resolution       : None")
        else:
            self.addExecutiveSummaryLine("Method 2 Resolution       : %.2f [A]" % xsDataImageQualityIndicators.getMethod2Res().getValue())
        if xsDataImageQualityIndicators.getMaxUnitCell() is not None:
            self.addExecutiveSummaryLine("Maximum unit cell         : %.2f [A]" % xsDataImageQualityIndicators.getMaxUnitCell().getValue())
        if xsDataImageQualityIndicators.getPctSaturationTop50Peaks() is not None:
            self.addExecutiveSummaryLine("Saturation, Top 50 Peaks  : %.1f [%%]" % xsDataImageQualityIndicators.getPctSaturationTop50Peaks().getValue())
        self.addExecutiveSummaryLine("In-resolution Ovrld Spots : %d" % xsDataImageQualityIndicators.getInResolutionOvrlSpots().getValue())
        
