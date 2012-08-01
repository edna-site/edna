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

        self.outfile = None
        self.infile = None

    def configure(self):
        EDPluginExecProcessScript.configure(self)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG('Aimless: preprocess')
        infile = self.dataInput.infile.value
        outfile = self.dataInput.outfile.value
        symdb = self.getStringConfigurationParamValue('symdb_path')
        if symdb is None:
            self.ERROR('no symdb in configuration, aborting')
            self.setFailure()
            return

        # TODO: ask Max why he forces the version to 6.2.0
        options = 'HKLIN {0} HKLOUT {1} SYMINFO {3}'.format(infile, outfile, symdb)
        self.setScriptCommandLine(options)
        self.DEBUG('command line options set to {0}'.format(options))


        start_image = self.dataInput.start_image.value
        end_image = self.dataInput.end_image.value
        dcid = self.dataInput.datacollectionID.value
        resolution = self.dataInput.res.value
        anom = self.dataInput.anom.value

        self.addListCommandExecution('bins 15')
        self.addListCommandExecution('run 1 batch {0} to {1}'.format(start_image, end_image))
        self.addListCommandExecution('name run 1 project {0} crystal DEFAULT dataset NATIVE'.format(dcid))
        self.addListCommandExecution('scales constant')
        self.addListCommandExecution('resolution 50 {0}'.format(resolution))
        self.addListCommandExecution('cycles 100')
        self.addListCommandExecution('anomalous {0}'.format(anom))
        self.addListCommandExecution('END')

        # TODO: Max saves those parameters to a file, we'll need to
        # see where to put it. Until then, just log them
        self.DEBUG(self.getListCommandExecution())

    def checkParameters(self):
        self.DEBUG('Aimless: checkParameters')
        data_input = self.dataInput
        self.checkMandatoryParameters(data_input.infile, 'no input file')
        self.checkMandatoryParameters(data_input.outfile, 'no output file')

        # now really check the parameters
        if data_input.infile is not None:
            path = data_input.infile.value
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
        output_file = self.dataInput.outfile.value

        res = XSDataResult()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(os.path.exists(output_file))
        res.status = status

        self.dataOutput = res
