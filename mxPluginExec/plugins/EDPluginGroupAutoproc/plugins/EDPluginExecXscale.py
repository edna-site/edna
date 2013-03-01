# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
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

__author__="Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


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
            EDVerbose.ERROR('i got {0}'.format(len(self.dataInput.unit_cell_constants)))
            self.setFailure()
        # check existence of the input files
        for f in self.dataInput.xds_files:
            # check which of the anom or noanom file we have to use
            path = f.path_anom.value if self.dataInput.friedels_law.value else f.path_noanom.value
            if not os.path.isfile(path):
                EDVerbose.ERROR('missing input file {0}'.format(path))
                self.setFailure()
                break

    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXscale.preProcess")
        anomalous = self.dataInput.friedels_law.value
        merged = self.dataInput.merge.value
        self.hkl_file = 'merged' if merged else 'unmerged'
        if anomalous:
            self.hkl_file += '_anom_XSCALE.hkl'
        else:
            self.hkl_file += '_noanom_XSCALE.hkl'

        # create the input file for xscale
        with open(os.path.join(self.getWorkingDirectory(), 'XSCALE.INP'), 'w') as inputfile:
            inputfile.write("OUTPUT_FILE= {0}\n".format(self.hkl_file))
            inputfile.write("MERGE= {0}\n".format("TRUE" if merged else "FALSE"))
            for xds_file in self.dataInput.xds_files:
                if self.dataInput.friedels_law.value:
                    path = os.path.abspath(xds_file.path_anom.value)
                else:
                    path = os.path.abspath(xds_file.path_noanom.value)
                # make a symlink so we do not hit the 50char limit
                sympath = os.path.abspath(os.path.join(self.getWorkingDirectory(),
                                                       os.path.basename(path)))
                os.symlink(path, sympath)

                res = xds_file.res.value
                # os.basename(sympath) is the filename relative to our dir
                inputfile.write("INPUT_FILE= {0} XDS_ASCII 100 {1}\n".format(os.path.basename(sympath), res))

            ucellconstants = ' '.join([str(x.value) for x in self.dataInput.unit_cell_constants])
            inputfile.write("UNIT_CELL_CONSTANTS= {0}\n".format(ucellconstants))
            sg = self.dataInput.sg_number.value
            inputfile.write("SPACE_GROUP_NUMBER= {0}\n".format(sg))

            # include the RESOLUTION_SHELLS directive only if bins are
            # specified. Otherwise the whole data is used
            bins = self.dataInput.bins
            if bins is not None and len(bins) != 0:
                binstring = ' '.join([str(x.value) for x in self.dataInput.bins])
                inputfile.write("RESOLUTION_SHELLS= {0}\n".format(binstring))


    def process(self, _edObject = None):
        self.DEBUG("EDPluginXscale.process")
        EDPluginExecProcessScript.process(self)


    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginXscale.postProcess")

        data_output = XSDataXscaleOutput()
        lp_file = os.path.join(self.getWorkingDirectory(), 'XSCALE.LP')
        data_output.succeeded = XSDataBoolean(False)
        if os.path.isfile(lp_file):
            # we have the output file
            # copy it to some other name
            anomalous = self.dataInput.friedels_law.value
            merged = self.dataInput.merge.value
            new_lp_file = 'merged' if merged else 'unmerged'
            if anomalous:
                new_lp_file += '_anom_XSCALE.LP'
            else:
                new_lp_file += '_noanom_XSCALE.LP'
            new_lp_file = os.path.join(self.getWorkingDirectory(), new_lp_file)

            shutil.copy(lp_file, new_lp_file)

            data_output.lp_file = XSDataString(os.path.abspath(new_lp_file))

            # look for an error message in the output
            with open(new_lp_file, 'r') as f:
                success = True
                for line in f:
                    if line.find('!!! ERROR !!!') != -1:
                        success = False
                        break
                data_output.succeeded = XSDataBoolean(success)

        # also add the hkl file to our output
        data_output.hkl_file = XSDataString(os.path.join(self.getWorkingDirectory(),
                                                         self.hkl_file))

        self.dataOutput = data_output
