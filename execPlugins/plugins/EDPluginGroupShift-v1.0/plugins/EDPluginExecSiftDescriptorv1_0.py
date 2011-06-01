# coding: utf8
#
#    Project: execPlugins PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jérôme Kieffer"
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"

import os
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataShiftv1_0 import XSDataInputSiftDescriptor
from XSDataShiftv1_0 import XSDataResultSiftDescriptor
from XSDataCommon import XSDataString, XSDataFile

class EDPluginExecSiftDescriptorv1_0(EDPluginExecProcessScript):
    """
    Runs "autopano-sift" to retrive the SIFT descriptor of the image
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputSiftDescriptor)
        self.strImage = None
        self.strKeys = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecSiftDescriptorv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "No image provided")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecSiftDescriptorv1_0.preProcess")
        self.strImage = self.getDataInput().getImage().getPath().getValue()
        if not os.path.isfile(self.strImage):
            strError = "Input image file does not exist: %s" % self.strImage
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)
        self.strKeys = os.path.join(self.getWorkingDirectory(), os.path.basename(self.strImage + ".keys.gz"))
        self.generateKeysCommand()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecSiftDescriptorv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultSiftDescriptor()
        if os.path.isfile(self.strKeys):
            xsdFile = XSDataFile()
            xsdFile.setPath(XSDataString(self.strKeys))
            xsDataResult.setDescriptorFile(xsdFile)
        self.setDataOutput(xsDataResult)

    def generateKeysCommand(self):
        """
        This method creates the generatekeys command line for Sift.
        """

        self.DEBUG("EDPluginExecSiftDescriptorv1_0.generateKeysCommand")
        strMacro = ' "%s"  "%s" ' % (self.strImage, self.strKeys)
        self.DEBUG("Sift generateKeys Command line:\n" + strMacro)
        self.setScriptCommandline(strMacro)

#    def 
#/mnt/data/ID21-FullFieldXanes$ mono /usr/lib/autopano-sift/generatekeys.exe Thumbnail/FullFieldXAS_02.png toto.key.gz
