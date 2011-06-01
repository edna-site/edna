#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) CCP4
#
#    Principal author:       Mark
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

from EDVerbose import EDVerbose

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4v0 import XSDataInputMTZDUMPUnitCellSpaceGroup
from XSDataCCP4v0 import XSDataResultMTZDUMPUnitCellSpaceGroup
from XSDataCCP4v0 import XSDataUnitCell
from XSDataCCP4v0 import XSDataSpaceGroup
from XSDataCCP4v0 import XSDataLength
from XSDataCCP4v0 import XSDataString
from XSDataCCP4v0 import XSDataAngle
from XSDataCCP4v0 import XSDataInteger

class EDPluginExecMTZDUMPUnitCellSpaceGroupv10(EDPluginExecProcessScript):
    """
    [To be replaced with a description of EDPluginExecProcessScriptTemplatev10]
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputMTZDUMPUnitCellSpaceGroup)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecMTZDUMPUnitCellSpaceGroupv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputMTZFile(), "No input MTZ file")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecMTZDUMPUnitCellSpaceGroupv10.preProcess")
        self.setRequireCCP4(True)
        self.generateMTZDUMPCommands()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecMTZDUMPUnitCellSpaceGroupv10.postProcess")
        # Create some output data
        pyStrLog = self.readProcessLogFile()
        xsDataResultMTZDUMPUnitCellSpaceGroup = self.parseMTZDUMPLog(pyStrLog)
        self.setDataOutput(xsDataResultMTZDUMPUnitCellSpaceGroup)


    def generateMTZDUMPCommands(self):
        EDVerbose.DEBUG("EDPluginExecMTZDUMPUnitCellSpaceGroupv10.generateMTZDUMPCommands")
        xsDataInputMTZDUMPUnitCellSpaceGroup = self.getDataInput()
        xsDataFileInputMTZ = xsDataInputMTZDUMPUnitCellSpaceGroup.getInputMTZFile()
        pyStrInputMTZFile = xsDataFileInputMTZ.getPath().getValue()
        self.setScriptCommandline("HKLIN %s" % pyStrInputMTZFile)
        self.addListCommandExecution("END")


    def parseMTZDUMPLog(self, _pyStrLog):
        EDVerbose.DEBUG("EDPluginExecMTZDUMPUnitCellSpaceGroupv10.parseMTZDUMPLog")
        pyListLogLines = _pyStrLog.split("\n")
        for j, pyStrLine in enumerate(pyListLogLines):
            if "* Dataset ID, project/crystal/dataset names, cell dimensions, wavelength:" in pyStrLine:
                pyTupleCell = tuple(map(float, pyListLogLines[j + 5].split()))
            if " * Space group = " in pyStrLine:
                pyStrSpaceGroupName = pyStrLine.split("'")[1].strip()
                iSpaceGroupNumber = int(pyStrLine.replace("(", " ").replace(")", " ").split()[-1])
        xsDataResultMTZDUMPUnitCellSpaceGroup = XSDataResultMTZDUMPUnitCellSpaceGroup()
        #print pyTupleCell
        xsDataUnitCell = XSDataUnitCell()
        xsDataUnitCell.setLength_a(XSDataLength(pyTupleCell[0]))
        xsDataUnitCell.setLength_b(XSDataLength(pyTupleCell[1]))
        xsDataUnitCell.setLength_c(XSDataLength(pyTupleCell[2]))
        xsDataUnitCell.setAngle_alpha(XSDataAngle(pyTupleCell[3]))
        xsDataUnitCell.setAngle_beta(XSDataAngle(pyTupleCell[4]))
        xsDataUnitCell.setAngle_gamma(XSDataAngle(pyTupleCell[5]))
        xsDataSpaceGroup = XSDataSpaceGroup()
        xsDataSpaceGroup.setName(XSDataString(pyStrSpaceGroupName))
        xsDataSpaceGroup.setITNumber(XSDataInteger(iSpaceGroupNumber))
        xsDataResultMTZDUMPUnitCellSpaceGroup.setUnitCell(xsDataUnitCell)
        xsDataResultMTZDUMPUnitCellSpaceGroup.setSpaceGroup(xsDataSpaceGroup)
        return xsDataResultMTZDUMPUnitCellSpaceGroup
