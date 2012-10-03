#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
#                            Sandor Brockhauser (brockhauser@embl-grnoble.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

__authors__ = [ "Olof Svensson", "Sandor Brockhauser", "Gleb Bourenkov" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20120712"
__status__ = "alpha"


from EDPluginExecProcessScript import EDPluginExecProcessScript



from XSDataXDSv1_1 import XSDataDouble
from XSDataXDSv1_1 import XSDataInputXDSSpotSearch
from XSDataXDSv1_1 import XSDataResultXDSSpotSearch
from XSDataXDSv1_1 import XSDataXDSSpot

class EDPluginXDSSpotSearchv1_1(EDPluginExecProcessScript):


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSSpotSearch)
        self.m_pyStrXDSInput = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginFIT2DCakev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDetector(), "inputFile is None")
        self.checkMandatoryParameters(self.getDataInput().getSubWedge(), "subWedge is None")


    def addInputLine(self, _pyStrInputLine):
        if (self.m_pyStrXDSInput is None):
            self.m_pyStrXDSInput = ""
        self.m_pyStrXDSInput += _pyStrInputLine + "\n"


    def preProcess(self, _edPlugin=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXDSSpotSearchv1_0.preProcess")
        self.createXDSInput()
        self.writeProcessFile("XDS.INP", self.m_pyStrXDSInput)


    def createXDSInput(self):
        self.m_pyStrXDSInput = ""

        xsDataInputXDSSpotSearch = self.getDataInput()

        # Jobs

        xsDataXDSJobList = xsDataInputXDSSpotSearch.getJob()

        pyStrJobLine = "JOB="
        for xsDataStringJob in xsDataXDSJobList:
            pyStrJobLine += " %s" % (xsDataStringJob.getValue())

        self.addInputLine(pyStrJobLine)

        # Detecor related input

        xsDataXDSDetector = xsDataInputXDSSpotSearch.getDetector()


        self.addInputLine("DETECTOR=%s " % \
                           (xsDataXDSDetector.getDetector_name().getValue()))

        self.addInputLine("NX=%d   NY=%d  QX=%8f  QY=%8f" % \
                           (xsDataXDSDetector.getNx().getValue(),
                             xsDataXDSDetector.getNy().getValue(),
                             xsDataXDSDetector.getQx().getValue(),
                             xsDataXDSDetector.getQy().getValue()))


        # Sub wedge related input

        xsDataXDSSubWedge = xsDataInputXDSSpotSearch.getSubWedge()

        xsDataXSDIntegerRangeBackground = xsDataXDSSubWedge.getBackground_range()
        self.addInputLine("BACKGROUND_RANGE= %4d %4d" % \
                               (xsDataXSDIntegerRangeBackground.getLower().getValue(),
                                 xsDataXSDIntegerRangeBackground.getUpper().getValue()))

        xsDataXSDIntegerRangeData = xsDataXDSSubWedge.getData_range()
        self.addInputLine("DATA_RANGE= %4d %4d" % \
                               (xsDataXSDIntegerRangeData.getLower().getValue(),
                                 xsDataXSDIntegerRangeData.getUpper().getValue()))

        pyStrTemplate = xsDataXDSSubWedge.getName_template_of_data_frames().getValue()
        pyStrImageFormat = xsDataXDSDetector.getImage_format().getValue()
        self.addInputLine("NAME_TEMPLATE_OF_DATA_FRAMES= %s %s" % (pyStrTemplate,
                                                                     pyStrImageFormat))

#    def createImageLinks( self ):
#        xsDataXDSInput = self.getDataInput()
#        xsDataXDSImageLinkList = xsDataXDSInput.getImage_link()
#        self.addListCommandPreExecution( "rm -rf %s" % ( self.m_oedStringImageLinkSubDirectory ) )
#        self.addListCommandPreExecution( "mkdir -p %s" % ( self.m_oedStringImageLinkSubDirectory ) )
#        
#        for xsDataXDSImageLink in xsDataXDSImageLinkList:
#            oedStringSourcePath = xsDataXDSImageLink.getSource().getPath().getValue()
#            oedStringTarget     = xsDataXDSImageLink.getTarget().getValue()
#            oedStringTargetPath = EDDiskExplorer.mergePath( self.m_oedStringImageLinkSubDirectory, oedStringTarget )
#            self.addListCommandPreExecution( "ln -s %s %s" % ( oedStringSourcePath, oedStringTargetPath ) )


    def postProcess(self, _edPlugin=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginXDSSpotSearchv1_0.postProcess")
        xsDataResultXDSSpotSearch = None
        pyStrSpots = self.readProcessFile("SPOT.XDS")
        if (pyStrSpots is None):
            errorMessage = "EDPluginXDSSpotSearchv01.postProcess : Cannot read file SPOT.XDS"
            self.error(errorMessage)
            self.addErrorMessage(errorMessage)
        else:
            pyListSpotLines = pyStrSpots.split("\n")
            xsDataResultXDSSpotSearch = XSDataResultXDSSpotSearch()
            for strSpotLine in pyListSpotLines:
                xsDataXDSSpot = XSDataXDSSpot()
                listFields = strSpotLine.split()
                if len(listFields) == 4:
                    xsDataXDSSpot.setCentroidX(XSDataDouble(float(listFields[0])))
                    xsDataXDSSpot.setCentroidY(XSDataDouble(float(listFields[1])))
                    xsDataXDSSpot.setCentroidFrame(XSDataDouble(float(listFields[2])))
                    xsDataXDSSpot.setIoverSigma(XSDataDouble(float(listFields[3])))
                    xsDataResultXDSSpotSearch.addSpot(xsDataXDSSpot)
        self.setDataOutput(xsDataResultXDSSpotSearch)
