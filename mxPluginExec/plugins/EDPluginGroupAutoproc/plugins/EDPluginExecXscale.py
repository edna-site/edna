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
from EDVerbose import EDVerbose

from XSDataCommon import XSDataBoolean, XSDataString
from XSDataAutoproc import XSDataXscaleInput, XSDataXscaleOutput


# XScale input files can be quite complex and our needs simple so
# instead of writing a parser them like I did for XDS I'll just
# generate the input from some data model parameters.

class EDPluginExecXscale(EDPluginExecProcessScript):
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
        # do the data binding work...
        self.checkMandatoryParameters(self.dataInput.merge,
                                      'merge param not given')
        self.checkMandatoryParameters(self.dataInput.friedels_law,
                                      'friedel\'s law not given')
        self.checkMandatoryParameters(self.dataInput.xds_files,
                                      'no xds files input')
        self.checkMandatoryParameters(self.dataInput.unit_cell_constants,
                                      'unit cell constants not defined')
        self.checkMandatoryParameters(self.dataInput.sg_number,
                                      'space group not given')
        # bins explicitely not mandatory as we may want to run xscale
        # over the whole data if the detector is complete

        # now really check that stuff
        # the unit cell constants param should be 6 floats
        if len(self.dataInput.unit_cell_constants) != 6:
            EDVerbose.ERROR('the unit cell constants list should have 6 elements')
            EDVerbose.ERROR('i got {}'.format(len(self.dataInput.unit_cell_constants)))
            self.setFailure()
        # check existence of the input files
        for f in self.dataInput.xds_files:
            path = f.path.value
            if not os.path.isfile(path):
                EDVerbose.ERROR('missing input file {}'.format(path))
                self.setFailure()
                break

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
            inputfile.write("OUTPUT_FILE= {}\n".format(outfile))
            inputfile.write("MERGE= {}\n".format("TRUE" if merged else "FALSE"))
            for xds_file in self.dataInput.xds_files:
                path = os.path.abspath(xds_file.path.value)
                # make a symlink so we do not hit the 50char limit
                sympath = os.path.abspath(os.path.join(self.getWorkingDirectory(),
                                                       os.path.basename(path)))
                os.symlink(path, sympath)

                res = xds_file.res.value
                inputfile.write("INPUT_FILE= {} XDS_ASCII 100 {}\n".format(sympath, res))

            ucellconstants = ' '.join([str(x.value) for x in self.dataInput.unit_cell_constants])
            inputfile.write("UNIT_CELL_CONSTANTS= {}\n".format(ucellconstants))
            sg = self.dataInput.sg_number.value
            inputfile.write("SPACE_GROUP_NUMBER= {}\n".format(sg))

            # include the RESOLUTION_SHELLS directive only if bins are
            # specified. Otherwise the whole data is used
            bins = self.dataInput.bins
            if bins is not None and len(bins) != 0:
                binstring = ' '.join([str(x.value) for x in self.dataInput.bins])
                inputfile.write("RESOLUTION_SHELLS= {}\n".format(binstring))


    def process(self, _edObject = None):
        self.DEBUG("EDPluginXscale.process")
        EDPluginExecProcessScript.process(self)


    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginXscale.postProcess")

        data_output = XSDataXscaleOutput()
        output_file = os.path.join(self.getWorkingDirectory(), 'XSCALE.LP')
        data_output.succeeded = XSDataBoolean(False)
        if os.path.isfile(output_file):
            # we have the output file
            data_output.output_file = XSDataString(os.path.abspath(output_file))
            # look for an error message in the output
            with open(output_file, 'r') as f:
                success = True
                for line in f:
                    if line.find('!!! ERROR !!!') != -1:
                        success = False
                        break
                data_output.succeeded = XSDataBoolean(success)

        self.dataOutput = data_output
