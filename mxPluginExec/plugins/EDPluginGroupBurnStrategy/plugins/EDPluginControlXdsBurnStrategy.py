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

import os.path
import shutil

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataString, XSDataBoolean, XSDataStatus
from XSDataBurnStrategy import XSDataInputXdsBurnStrategy, XSDataOutputXdsBurnStrategy
from EDFactoryPlugin import edFactoryPlugin

edFactoryPlugin.loadPlugin('EDPluginExecMinimalXds')
from XSDataAutoproc import XSDataMinimalXdsIn

from xdscfgparser import parse_xds_file, dump_xds_file

class EDPluginControlXdsBurnStrategy(EDPluginControl):
    """
    This plugin runs XDS with the specified input file, unit cell
    constants and spacegroup
    """


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputXdsBurnStrategy)
        self.parsed_config = {}
        self.real_input_file = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlXdsBest.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")

        if not os.path.exists(self.dataInput.input_file.value):
            self.ERROR('The specified input file does not exist (path: {0})'.format(self.dataInput.input_file.value))


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlXdsBest.preProcess")
        self._xds = self.loadPlugin('EDPluginExecMinimalXds')

        # save the root path (where the initial xds.inp is) for later use
        self.root_dir = os.path.abspath(os.path.dirname(self.dataInput.input_file.value))

        # let's begin by copying the input file to avoid clobbering it
        shutil.copy(self.dataInput.input_file.value,
                    self.getWorkingDirectory())
        self.real_input_file = os.path.join(self.getWorkingDirectory(),
                                       os.path.basename(self.dataInput.input_file.value))

        # update the keywords
        self.parsed_config = parse_xds_file(self.real_input_file)
        di = self.dataInput
        unit_cell_constants = '{0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f}'.format(
            di.unit_cell_a.value,
            di.unit_cell_b.value,
            di.unit_cell_c.value,
            di.unit_cell_alpha.value,
            di.unit_cell_beta.value,
            di.unit_cell_gamma.value)
        sg = int(di.space_group.value)
        self.parsed_config['UNIT_CELL_CONSTANTS='] = unit_cell_constants
        self.parsed_config['SPACE_GROUP_NUMBER='] = sg

        # to avoid any problem let's also make the image template
        # absolute as well. The underlying XDS template will take care
        # of creating the links in its dir
        imtemplate = self.parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='][0]
        basedir = os.path.abspath(os.path.dirname(self.dataInput.input_file.value))
        newpath = os.path.join(basedir, imtemplate)
        self.parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='] = newpath
        # Make the [XY]-GEO_CORR paths absolute
        if 'X-GEO_CORR=' in self.parsed_config:
            xgeo = os.path.abspath(os.path.join(self.root_dir,
                                                self.parsed_config['X-GEO_CORR='][0]))
            if not os.path.exists(xgeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(xgeo))
                del self.parsed_config['X-GEO_CORR=']
            else:
                self.parsed_config['X-GEO_CORR='] = xgeo

        if 'Y-GEO_CORR=' in self.parsed_config:
            ygeo = os.path.abspath(os.path.join(self.root_dir,
                                                self.parsed_config['Y-GEO_CORR='][0]))
            if not os.path.exists(ygeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(ygeo))
                del self.parsed_config['Y-GEO_CORR=']
            else:
                self.parsed_config['Y-GEO_CORR='] = ygeo
        dump_xds_file(self.real_input_file, self.parsed_config)

        # create the input data model for the XDS plugin
        input_dm = XSDataMinimalXdsIn()
        input_dm.input_file = XSDataString(self.real_input_file)
        self._xds.dataInput = input_dm


    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlXdsBest.process")
        self._xds.executeSynchronous()
        expected = os.path.join(self._xds.getWorkingDirectory(), 'XDS_ASCII.HKL')
        if not os.path.exists(expected):
            # Try to re-run with JOB = DEFPIX INTEGRATE CORRECT
            self.parsed_config["JOB="] = "DEFPIX INTEGRATE CORRECT"
            self._xds2 = self.loadPlugin('EDPluginExecMinimalXds')
            self._xds2.setWorkingDirectory(self._xds.getWorkingDirectory())
            dump_xds_file(self.real_input_file, self.parsed_config)
            input_dm2 = XSDataMinimalXdsIn()
            input_dm2.input_file = XSDataString(self.real_input_file)
            self._xds2.dataInput = input_dm2
            self._xds2.executeSynchronous()
        


    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlXdsBest.postProcess")

        self.dataOutput = XSDataOutputXdsBurnStrategy()
        self.dataOutput.status = XSDataStatus()
        # check if a XDS.HKL file has been generated
        expected = os.path.join(self._xds.getWorkingDirectory(), 'XDS_ASCII.HKL')
        if os.path.exists(expected):
            self.dataOutput.status.isSuccess = XSDataBoolean(True)
            self.dataOutput.xds_hkl = XSDataString(expected)
        else:
            self.dataOutput.status.isSuccess = XSDataBoolean(False)
