# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       <author>
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

__author__="thomas boeglin"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"


import os
import os.path
import shutil
import fnmatch

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataBoolean
from XSDataAutoproc import XSDataXscaleInput


# XScale input files can be quite complex and our needs simple so
# instead of writing a parser them like I did for XDS I'll just
# generate the input from some data model parameters.

class EDPluginXscale(EDPluginExecProcessScript):
    """
    """


    def __init__(self ):
        """
        """
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataXscaleInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginXscale.checkParameters")
        # TODO do the job of the data model thingie by hand

    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXscale.preProcess")
        anomalous = self.dataInput.friedels_law.value
        merged = self.dataInput.merge.value
        outfile = 'merged' if merged else unmerged
        if anomalous:
            outfile += '_anom.hkl'
        else:
            outfile += '_noanom.hkl'

        # create the input file for xscale
        with open(os.path.join(self.getWorkingDirectory(), 'XSCALE.INP'), 'w') as inputfile:
            inputfile.write("OUTPUT_FILE= {}".format(outfile))
            inputfile.write("MERGE= {}".format("TRUE" if merge else "FALSE"))
            for xds_file in self.dataInput.xds_files:
                path = xds_file.path.value
                res = xds_file.res.value
                inputfile.write("INPUT_FILE= {} XDS_ASCII 100 {}".format(path, res))
            ucellconstants = ' '.join([str(x.value) for x in self.dataInput.unit_cell_constants])
            inputfile.write("UNIT_CELL_CONSTANTS= {}".format(ucellconstants))
            sg = self.dataInput.sg_number.value
            inputfile.write("SPACE_GROUP_NUMBER= {}".format(sg))
            binstring = ' '.join([str(x.value) for x in self.dataInput.bins])
            inputfile.write("RESOLUTION_SHELLS= {}".format(binstring))


    def process(self, _edObject = None):
        self.DEBUG("EDPluginXscale.process")
        EDPluginExecProcessScript.process(self)


    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginXscale.postProcess")

        data_output = XSDataXscaleOutput()
        output_file = os.path.join(self.getWorkingDirectory(), 'XSCALE.LP')
        if os.path.isfile(output_file):
            data_output.succeeded = True
            data_output.output_file = os.path.abspath(output_file)
        else:
            data_output.succeeded = False

        self.dataOutput = data_output
