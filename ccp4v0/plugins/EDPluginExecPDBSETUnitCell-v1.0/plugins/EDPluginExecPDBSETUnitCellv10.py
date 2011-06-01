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

import os

from EDVerbose import EDVerbose

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4v0 import XSDataInputPDBSETUnitCell
from XSDataCCP4v0 import XSDataResultPDBSETUnitCell
from XSDataCCP4v0 import XSDataFile, XSDataString


class EDPluginExecPDBSETUnitCellv10(EDPluginExecProcessScript):
    """
    [To be replaced with a description of EDPluginExecProcessScriptTemplatev10]
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputPDBSETUnitCell)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("*** EDPluginExecPDBSETUnitCellv10.checkParameters")
#        print self.getDataInput().marshal()
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputPDBFile(), "No input PDB file")
        self.checkMandatoryParameters(self.getDataInput().getUnitCell(), "No unit cell")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecPDBSETUnitCellv10.preProcess")
        self.setRequireCCP4(True)
        self.generatePDBSETCommands()


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginExecPDBSETUnitCellv10.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPDBSETUnitCell()

        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(os.path.join(self.getWorkingDirectory(), "output.pdb")))

        xsDataResult.setOutputPDBFile(xsDataFile)


        self.setDataOutput(xsDataResult)


    def generatePDBSETCommands(self):
        EDVerbose.DEBUG("*** EDPluginExecPDBSETUnitCellv10.generatePDBSETCommands")
        self.setScriptCommandline("XYZIN %s XYZOUT %s" % (self.getDataInput().getInputPDBFile().getPath().getValue(), "output.pdb"))
        uc = self.getDataInput().getUnitCell()
        self.addListCommandExecution("CELL %f %f %f %f %f %f" %
                                      (uc.getLength_a().getValue(), uc.getLength_b().getValue(), uc.getLength_c().getValue(),
                                       uc.getAngle_alpha().getValue(), uc.getAngle_beta().getValue(), uc.getAngle_gamma().getValue()))
        self.addListCommandExecution("END")
#        self.addListCommandExecution("EOF")

