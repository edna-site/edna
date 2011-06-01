#
#    Project: EDNA ExecPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, re
from EDVerbose      import EDVerbose
from EDPluginExec   import EDPluginExec
from EDMessage      import EDMessage
from XSDataEDFv1_0  import XSDataFile
from XSDataEDFv1_0  import XSDataString
from XSDataEDFv1_0  import XSDataKeyValuePair
from XSDataEDFv1_0  import XSDataInputChiToEDF
from XSDataEDFv1_0  import XSDataResultChiToEDF
from EdfFile        import EdfFile
import numpy

class EDPluginChiToEDFv1_0(EDPluginExec):
    """
    This plugin reads the header of an EDF (ESRF Data File) and returns
    the header values as a python Dictionary.
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputChiToEDF)
        self._strEDFFile = None
        self.m_edDictionaryHeader = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginChiToEDFv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getChiFile(), "No chiFile given as input")


    def preProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginChiToEDFv1_0.postProcess")
        # Check that the input file is present
        strPathToInputFile = self.getDataInput().getChiFile().getPath().getValue()
        if (not os.path.exists(strPathToInputFile)):
            strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", strPathToInputFile)
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage



    def process(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginChiToEDFv1_0.process")
        # Read the Chi file
        pyStrPathToChiFile = self.getDataInput().getChiFile().getPath().getValue()
        pyNumpyArray = numpy.loadtxt(pyStrPathToChiFile, skiprows=4)
        # Prepare the header dictionary
        self.m_edDictionaryHeader = {}
        for xsDataKeyValuePair in self.getDataInput().getHeader().getKeyValuePair():
            key = xsDataKeyValuePair.getKey().getValue()
            value = xsDataKeyValuePair.getValue().getValue()
            self.m_edDictionaryHeader[ str(key) ] = str(value)
        # Save it as an EDF file
        if self.getDataInput().getOutputPathEDF() is not None:
            strOutputPath = self.getDataInput().getOutputPathEDF().getPath().getValue()
        else:
            strOutputPath = self.getWorkingDirectory()
        if strOutputPath is None:
            strOutputPath = os.getcwd()
        if os.path.exists(strOutputPath):
            if os.path.isfile(strOutputPath):
                self._strEDFFile = strOutputPath
            else: #it is a directory, I guess
                self._strEDFFile = os.path.join(strOutputPath, os.path.splitext(os.path.basename(self.getDataInput().getChiFile().getPath().getValue()))[0] + ".edf")
        else: #strOutputPath does not exist
            if strOutputPath.endswith("/"):
                try:
                    os.makedirs(strOutputPath, int("777", 8))
                except IOError:
                    raise IOError, "Unable to create directory named %s, please chech the rights or the input parameters." % strOutputPath
                self._strEDFFile = os.path.join(strOutputPath, os.path.splitext(os.path.basename(self.getDataInput().getChiFile().getPath().getValue()))[0] + ".edf")
            else: #it will be a file, the create the upper directory if needed
                upperDir = os.path.dirname(strOutputPath)
                if not os.path.isdir(upperDir):
                    try:
                        os.makedirs(upperDir, int("777", 8))
                    except IOError:
                        raise IOError, "Unable to create directory named %s, please chech the rights or the input parameters." % upperDir
                self._strEDFFile = strOutputPath
        print self._strEDFFile
        edfFile = EdfFile(self._strEDFFile)
        edfFile.WriteImage(self.m_edDictionaryHeader, pyNumpyArray)



    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginChiToEDFv1_0.postProcess")
        if (self._strEDFFile is not None):
            xsDataResultChiToEDF = XSDataResultChiToEDF()
            xsDataResultChiToEDF.setEdfFile(XSDataFile(XSDataString(self._strEDFFile)))
            self.setDataOutput(xsDataResultChiToEDF)
