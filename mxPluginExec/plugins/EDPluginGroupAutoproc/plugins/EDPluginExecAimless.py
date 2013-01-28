from __future__ import with_statement

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

import re
import os.path

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataStatus, XSDataBoolean, XSDataResult
from XSDataAutoproc import XSDataAimless

class EDPluginExecAimless(EDPluginExecProcessScript):
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setRequiredToHaveConfiguration(True)
        self.setXSDataInputClass(XSDataAimless)

        self.output_file = None
        self.input_file = None

    def configure(self):
        EDPluginExecProcessScript.configure(self)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG('Aimless: preprocess')
        input_file = self.dataInput.input_file.value
        output_file = self.dataInput.output_file.value
        symdb = self.config.get('symdb_path')
        if symdb is None:
            self.ERROR('no symdb in configuration, aborting')
            self.setFailure()
            return

        # TODO: ask Max why he forces the version to 6.2.0
        options = 'HKLIN {0} HKLOUT {1} SYMINFO {2}'.format(input_file, output_file, symdb)
        self.setScriptCommandline(options)
        self.DEBUG('command line options set to {0}'.format(options))


        start_image = self.dataInput.start_image.value
        end_image = self.dataInput.end_image.value
        dcid = self.dataInput.dataCollectionID.value
        resolution = self.dataInput.res.value
        if resolution is None:
            resolution = 0
        anom = self.dataInput.anom.value

        self.addListCommandExecution('bins 15')
        self.addListCommandExecution('run 1 batch {0} to {1}'.format(start_image, end_image))
        self.addListCommandExecution('name run 1 project {0} crystal DEFAULT dataset NATIVE'.format(dcid))
        self.addListCommandExecution('scales constant')
        self.addListCommandExecution('resolution 50 {0}'.format(resolution))
        self.addListCommandExecution('cycles 100')
        anomalous = 'ON' if anom else 'OFF'
        self.addListCommandExecution('anomalous {0}'.format(anomalous))
        self.addListCommandExecution('END')

        # TODO: Max saves those parameters to a file, we'll need to
        # see where to put it. Until then, just log them
        self.DEBUG(self.getListCommandExecution())

    def checkParameters(self):
        self.DEBUG('Aimless: checkParameters')
        data_input = self.dataInput
        self.checkMandatoryParameters(data_input.input_file, 'no input file')
        self.checkMandatoryParameters(data_input.output_file, 'no output file')

        # now really check the parameters
        if data_input.input_file is not None:
            path = data_input.input_file.value
            if not os.path.exists(path):
                self.ERROR('input file {0} does not exist'.format(path))
                self.setFailure()
                return

    def process(self):
        self.DEBUG('Aimless: process')
        EDPluginExecProcessScript.process(self)

    def postProcess(self):
        self.DEBUG('Aimless: postProcess')
        EDPluginExecProcessScript.postProcess(self)
        output_file = self.dataInput.output_file.value

        res = XSDataResult()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(os.path.exists(output_file))
        res.status = status

        self.dataOutput = res
