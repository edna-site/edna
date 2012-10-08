#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Karl Levik" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"



import os



from EDPluginMOSFLMv10 import EDPluginMOSFLMv10

from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataFile

from XSDataMOSFLMv10 import XSDataMOSFLMInputGeneratePrediction
from XSDataMOSFLMv10 import XSDataMOSFLMOutputGeneratePrediction


class EDPluginMOSFLMGeneratePredictionv10(EDPluginMOSFLMv10):


    def __init__(self):
        EDPluginMOSFLMv10.__init__(self)
        self.setXSDataInputClass(XSDataMOSFLMInputGeneratePrediction)
        self.__strPredictionImageFileName = "EDPluginMOSFLMGeneratePredictionv10.jpg"


    def preProcess(self, _edObject=None):
        EDPluginMOSFLMv10.preProcess(self)
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.preProcess")
        self.generateMOSFLMCommands()


    def postProcess(self, _edObject=None):
        EDPluginMOSFLMv10.postProcess(self)
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.postProcess")
        xsDataMOSFLMOutputGeneratePrediction = self.createDataMOSFLMOutputGeneratePrediction()
        self.setDataOutput(xsDataMOSFLMOutputGeneratePrediction)


    def configure(self):
        EDPluginMOSFLMv10.configure(self)
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.configure")
        self.createPredictionImageFileName()


    def checkParameters(self):
        """
        Checks the mandatory parameters for MOSLFM indexing
        """
        EDPluginMOSFLMv10.checkParameters(self)
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "image")


    def getPredictionImageFileName(self):
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.getPredictionImageFileName")
        return self.__strPredictionImageFileName


    def setPredictionImageFileName(self, _strFileName):
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.setPredictionImageFileName : " + _strFileName)
        self.__strPredictionImageFileName = _strFileName


    def createPredictionImageFileName(self):
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.createPredictionImagePath")
        strImageFileName = self.getBaseName() + "_image.jpg"
        self.setPredictionImageFileName(strImageFileName)


    def generateMOSFLMCommands(self):
        """
        This method creates a list of MOSFLM integration commands given a valid
        XSDataMOSFLMInputGeneratePrediction as input to the plugin.
        """
        EDPluginMOSFLMv10.generateMOSFLMCommands(self)
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.generateMOSFLMCommands")

        xsDataMOSFLMInputGeneratePrediction = self.getDataInput()

        if (xsDataMOSFLMInputGeneratePrediction is not None):

            pyStrTemplate = xsDataMOSFLMInputGeneratePrediction.getTemplate().getValue()
            xsDataMOSFLMImage = xsDataMOSFLMInputGeneratePrediction.getImage()
            iImageNumber = xsDataMOSFLMImage.getNumber().getValue()

            pyStrImageFileName = self.getImageFileNameFromTemplate(pyStrTemplate, iImageNumber)
            if (pyStrImageFileName is not None):
                self.setPredictionImageFileName(pyStrImageFileName + "_pred.jpg")

            fRotationAxisStart = xsDataMOSFLMImage.getRotationAxisStart().getValue()
            fRotationAxisEnd = xsDataMOSFLMImage.getRotationAxisEnd().getValue()
            self.addListCommandExecution("XGUI ON")
            self.addListCommandExecution("IMAGE %d PHI %f TO %f" % (iImageNumber, fRotationAxisStart, fRotationAxisEnd))
            self.addListCommandExecution("GO")
            self.addListCommandExecution("PREDICT_SPOTS")
            self.addListCommandExecution("CREATE_IMAGE PREDICTION ON BINARY TRUE FILENAME %s" % (self.getPredictionImageFileName()))
            self.addListCommandExecution("RETURN")
            self.addListCommandExecution("EXIT")

            self.addListCommandPostExecution("chmod 644 %s" % self.getPredictionImageFileName())

        # Force name of log file
        self.setScriptLogFileName(self.compactPluginName(self.getClassName())+".log")

        self.DEBUG("Finished EDPluginMOSFLMGeneratePredictionv10.generateMOSFLMCommands")


    def createDataMOSFLMOutputGeneratePrediction(self):
        self.DEBUG("EDPluginMOSFLMGeneratePredictionv10.createDataMOSFLMOutputIntegration")
        xsDataMOSFLMInputGeneratePrediction = self.getDataInput()
        xsDataMOSFLMImage = xsDataMOSFLMInputGeneratePrediction.getImage()
        iImageNumber = xsDataMOSFLMImage.getNumber().getValue()
        xsDataMOSFLMOutputGeneratePrediction = XSDataMOSFLMOutputGeneratePrediction()
        xsDataImage = XSDataImage()
        xsDataImage.setNumber(XSDataInteger(iImageNumber))
        xsDataImage.setPath(XSDataString(os.path.join(self.getWorkingDirectory(), self.getPredictionImageFileName())))
        xsDataMOSFLMOutputGeneratePrediction.setPredictionImage(xsDataImage)
         # Path to log file
        xsDataMOSFLMOutputGeneratePrediction.setPathToLogFile(XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))))
        return xsDataMOSFLMOutputGeneratePrediction


    def getImageFileNameFromTemplate(self, _strTemplate, _iImageNumber):
        bHashFound = False
        bFinished = False
        iFirstHash = None
        iNoHashes = 0
        strImageFileName = None
        try:
            for iIndex, pyChar in enumerate(_strTemplate):
                if ((not bHashFound) and (not bFinished)):
                    if (pyChar == "#"):
                        iFirstHash = iIndex
                        bHashFound = True
                else:
                    if ((pyChar != "#") and (not bFinished)):
                        bFinished = True
                if (bHashFound and (not bFinished)):
                    iNoHashes += 1
            strImageFileName = _strTemplate[ 0:iFirstHash ] + str(_iImageNumber).rjust(iNoHashes, "0")
        except:
            self.warning("EDPluginMOSFLMGeneratePredictionv10: Couldn't transform template %s to file name" % _strTemplate)
            strImageFileName = None
        return strImageFileName
