#
#    Project: execPlugin / Saxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 - EDNA Default Copyright
#
#    Principal author:       Jerome Kieffer
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

"""
Wrapper for Saxs Angle:

calls azimuthal integration program of the suite

"""

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2008-2009 - ESRF"

import os
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataSaxsv1_0 import XSDataInputSaxsAnglev1_0, XSDataImage
from XSDataSaxsv1_0 import XSDataResultSaxsAnglev1_0 , XSDataString

class EDPluginExecSaxsAnglev1_0(EDPluginExecProcessScript):
    """
    
    Execution plugins running the saxs_angle program 
    
    """


    def __init__(self):
        """
        Constructor of the Plugin
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsAnglev1_0)
        self.inputDataFile = None
        self.regroupedDataFile = None
        self.beamCenterX = None
        self.beamCenterY = None
        self.innerRadius = None
        self.stepRadius = None
        self.sizeRadial = None
        self.startAzimuth = None
        self.stepAzimuth = None
        self.sizeAzimuth = None
        self.firstImage = None
        self.lastImage = None
        self.options = None
        self.dummy = None
        self.increment = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        #No parameters are mandatory !!!!!

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0.preProcess")
        xsdIn = self.getDataInput()
        if xsdIn.getInputDataFile() is not None:
            self.inputDataFile = xsdIn.getInputDataFile().getPath().getValue()
            if not os.path.isfile(self.inputDataFile):
                EDVerbose.WARNING("Input file %s does not exist ... try to go on anyway" % self.inputDataFile)
                self.inputDataFile = None
        if xsdIn.getRegroupedDataFile() is not None:
            self.regroupedDataFile = xsdIn.getRegroupedDataFile().getPath().getValue()
        if xsdIn.getBeamCenterX() is not None:
            self.beamCenterX = xsdIn.getBeamCenterX().getValue()
        if xsdIn.getBeamCenterY() is not None:
            self.beamCenterY = xsdIn.getBeamCenterY().getValue()
        if xsdIn.getInnerRadius() is not None:
            self.innerRadius = xsdIn.getInnerRadius().getValue()
        if xsdIn.getStepRadius() is not None:
            self.stepRadius = xsdIn.getStepRadius().getValue()
        if xsdIn.getSizeRadial() is not None:
            self.sizeRadial = xsdIn.getSizeRadial().getValue()
        if xsdIn.getStartAzimuth() is not None:
            self.startAzimuth = xsdIn.getStartAzimuth().getValue()
        if xsdIn.getStepAzimuth() is not None:
            self.stepAzimuth = xsdIn.getStepAzimuth().getValue()
        if xsdIn.getSizeAzimuth() is not None:
            self.sizeAzimuth = xsdIn.getSizeAzimuth().getValue()
        if xsdIn.getFirstImage() is not None:
            self.firstImage = xsdIn.getFirstImage().getValue()
        if xsdIn.getLastImage() is not None:
            self.lastImage = xsdIn.getLastImage().getValue()
        if xsdIn.getOptions() is not None:
            self.options = xsdIn.getOptions().getValue()
        if xsdIn.getDummy() is not None:
            self.dummy = xsdIn.getDummy().getValue()
        if xsdIn.getIncrement() is not None:
            self.increment = xsdIn.getIncrement().getValue()
        #Create the command line to run the program
        self.generateSaxsAngleCommand()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSaxsAnglev1_0()
        if self.regroupedDataFile is None:
            self.regroupedDataFile = "output.edf"
        if os.path.isfile(self.regroupedDataFile):
            xsdFile = XSDataImage()
            xsdFile.setPath(XSDataString(os.path.abspath(self.regroupedDataFile)))
#            EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0 xsDataFile: \n%s" % xsdFile.marshal())
            xsDataResult.setRegroupedDataFile(xsdFile)
#            EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0 xsDataResult: \n%s" % xsDataResult.marshal())
        self.setDataOutput(xsDataResult)

    def generateSaxsAngleCommand(self):

        EDVerbose.DEBUG("EDPluginExecSaxsAnglev1_0.generateSaxsAngleCommand")
        if self.options is not None:
            strOptions = self.options
        else:
            strOptions = ""

        if self.firstImage is not None:
            strOptions += " -firstimage %s" % self.firstImage
        if self.lastImage is not None:
            strOptions += " -lastimage %s" % self.lastImage
        if self.increment is not None:
            strOptions += " -increment %s" % self.increment
        if self.dummy is not None:
            strOptions += " -dummy %s" % self.dummy

        if (self.beamCenterX is not None) and (self.beamCenterY is not None):
            strOptions += " -i1cen %s %s" % (self.beamCenterY, self.beamCenterX)

        if self.innerRadius is not  None:
            strOptions += " -r0 %s" % self.innerRadius
        if self.stepRadius  is not None:
            strOptions += " -dr %s" % self.stepRadius
        if self.sizeRadial  is not None:
            strOptions += " -odim_1 %s" % self.sizeAzimuth
        if self.startAzimuth  is not None:
            strOptions += " -a0 %s" % self.startAzimuth
        if self.stepAzimuth  is not None:
            strOptions += " -da %s" % self.stepAzimuth
        if self.sizeAzimuth  is not None:
            strOptions += " -odim_2 %s" % self.sizeAzimuth



        if (self.inputDataFile is not None) and (self.regroupedDataFile is not None):
            strOptions += " " + self.inputDataFile + " " + self.regroupedDataFile
        elif (self.inputDataFile is None) and (self.regroupedDataFile is not None):
            strOptions += " = " + self.regroupedDataFile
        elif (self.inputDataFile is not None) and (self.regroupedDataFile is None):
            strOptions += " " + self.inputDataFile
#        command = "saxs_angle -omod n -rsys normal -da 360_deg -odim = 1 %s %s > /dev/null 2>/dev/null" % (filenameMSK, filenameANG)
        EDVerbose.DEBUG("saxs_angle " + strOptions)
        self.setScriptCommandline(strOptions)
