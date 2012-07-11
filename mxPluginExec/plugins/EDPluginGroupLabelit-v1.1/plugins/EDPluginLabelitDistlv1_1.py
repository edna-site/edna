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



from EDPluginLabelitv1_1 import EDPluginLabelitv1_1

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger

from XSDataLabelitv1_1 import XSDataImageQualityIndicators


class EDPluginLabelitDistlv1_1(EDPluginLabelitv1_1):
    """
    This plugin runs the labelit.distl command for pre-screening reference images.
    """


    def preProcess(self, _edObject=None):
        """
        Sets up the Labelit command line
        """
        EDPluginLabelitv1_1.preProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitDistlv1_1.preProcess...")
        self.setScriptExecutable("labelit.distl")
        self.initaliseLabelitCommandLine()
        self.addListCommandPreExecution("export PYTHONPATH=\"\" ")
        self.addListCommandPreExecution(". %s" % self.getPathToLabelitSetpathScript())


    def postProcess(self, _edObject=None):
        """
        Parses the labelit.screen log file and the generated MOSFLM script
        """
        EDPluginLabelitv1_1.postProcess(self, _edObject)
        self.DEBUG("EDPluginLabelitDistlv1_1.postProcess")
        strLabelitDistlLog = self.readProcessLogFile()
        if (strLabelitDistlLog is None):
            strErrorMessage = "EDPluginLabelitDistlv1_1.postProcess : Could not read the Labelit log file"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataImageQualityIndicators = self.parseLabelitDistlOutput(strLabelitDistlLog)
            xsDataImage = self.getDataInput("referenceImage")[0]
            xsDataImageQualityIndicators.setImage(xsDataImage)
            self.setDataOutput(xsDataImageQualityIndicators, "imageQualityIndicators")


    def parseLabelitDistlOutput(self, _strLabelitDistlLogText):
        self.DEBUG("EDPluginLabelitDistlv1_1.parseLabelitDistlOutput")
        xsDataImageQualityIndicators = None
        if _strLabelitDistlLogText is not None:
            xsDataImageQualityIndicators = XSDataImageQualityIndicators()
            for strLine in _strLabelitDistlLogText.split("\n"):
                if strLine.find("Spot Total") != -1:
                    iSpotTotal = int(strLine.split()[3])
                    xsDataImageQualityIndicators.setSpotTotal(XSDataInteger(iSpotTotal))
                elif strLine.find("In-Resolution Total") != -1:
                    iInResTotal = int(strLine.split()[3])
                    xsDataImageQualityIndicators.setInResTotal(XSDataInteger(iInResTotal))
                elif strLine.find("Good Bragg Candidates") != -1:
                    iGoodBraggCandidates = int(strLine.split()[4])
                    xsDataImageQualityIndicators.setGoodBraggCandidates(XSDataInteger(iGoodBraggCandidates))
                elif strLine.find("Ice Rings") != -1:
                    iIceRings = int(strLine.split()[3])
                    xsDataImageQualityIndicators.setIceRings(XSDataInteger(iIceRings))
                elif strLine.find("Method 1 Resolution") != -1:
                    fMethod1Res = float(strLine.split()[4])
                    xsDataImageQualityIndicators.setMethod1Res(XSDataDouble(fMethod1Res))
                elif strLine.find("Method 2 Resolution") != -1:
                    if strLine.split()[4] != "None":
                        fMethod2Res = float(strLine.split()[4])
                        xsDataImageQualityIndicators.setMethod2Res(XSDataDouble(fMethod2Res))
                elif strLine.find("Maximum unit cell") != -1:
                    if strLine.split()[4] != "None":
                        fMaxUnitCell = float(strLine.split()[4])
                        xsDataImageQualityIndicators.setMaxUnitCell(XSDataDouble(fMaxUnitCell))
                elif strLine.find("%Saturation, Top 50 Peaks") != -1:
                    fPctSaturationTop50Peaks = float(strLine.split()[5])
                    xsDataImageQualityIndicators.setPctSaturationTop50Peaks(XSDataDouble(fPctSaturationTop50Peaks))
                elif strLine.find("In-Resolution Ovrld Spots") != -1:
                    iInResolutionOvrlSpots = int(strLine.split()[4])
                    xsDataImageQualityIndicators.setInResolutionOvrlSpots(XSDataInteger(iInResolutionOvrlSpots))
                elif strLine.find("Bin population cutoff for method 2 resolution") != -1:
                    fBinPopCutOffMethod2Res = float(strLine.split()[7][:-1])
                    xsDataImageQualityIndicators.setBinPopCutOffMethod2Res(XSDataDouble(fBinPopCutOffMethod2Res))
        return xsDataImageQualityIndicators


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the Labelit distl plugin.
        """
        self.DEBUG("EDPluginLabelitDistlv1_1.generateExecutiveSummary")
        xsDataImageQualityIndicators = self.getDataOutput("imageQualityIndicators")[0]
        self.addExecutiveSummaryLine("Execution of Labelit distl successful.")
        self.addExecutiveSummaryLine("Image                   : %s" % xsDataImageQualityIndicators.getImage().getPath().getValue())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("Labelit.distl results:")
        self.addExecutiveSummaryLine("Spot Total                : %d" % xsDataImageQualityIndicators.getSpotTotal().getValue())
        self.addExecutiveSummaryLine("In-Resolution Total       : %d" % xsDataImageQualityIndicators.getInResTotal().getValue())
        self.addExecutiveSummaryLine("Good Bragg Candidates     : %d" % xsDataImageQualityIndicators.getGoodBraggCandidates().getValue())
        self.addExecutiveSummaryLine("Ice Rings                 : %d" % xsDataImageQualityIndicators.getIceRings().getValue())
        self.addExecutiveSummaryLine("Method 1 Resolution       : %.2f [A]" % xsDataImageQualityIndicators.getMethod1Res().getValue())
        if xsDataImageQualityIndicators.getMethod2Res() is None:
            self.addExecutiveSummaryLine("Method 2 Resolution       : None")
        else:
            self.addExecutiveSummaryLine("Method 2 Resolution       : %.2f [A]" % xsDataImageQualityIndicators.getMethod2Res().getValue())
        if xsDataImageQualityIndicators.getMaxUnitCell() is not None:
            self.addExecutiveSummaryLine("Maximum unit cell         : %.2f [A]" % xsDataImageQualityIndicators.getMaxUnitCell().getValue())
        if xsDataImageQualityIndicators.getPctSaturationTop50Peaks() is not None:
            self.addExecutiveSummaryLine("Saturation, Top 50 Peaks  : %f [%%]" % xsDataImageQualityIndicators.getPctSaturationTop50Peaks().getValue())
        self.addExecutiveSummaryLine("In-Resolution Ovrld Spots : %d" % xsDataImageQualityIndicators.getInResolutionOvrlSpots().getValue())
        self.addExecutiveSummaryLine("Bin population cutoff for method 2 resolution : %d [%%]" % xsDataImageQualityIndicators.getBinPopCutOffMethod2Res().getValue())
