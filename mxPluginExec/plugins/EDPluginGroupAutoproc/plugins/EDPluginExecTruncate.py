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
from XSDataAutoproc import XSDataTruncate

class EDPluginExecTruncate(EDPluginExecProcessScript):
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setRequiredToHaveConfiguration(True)
        self.setXSDataInputClass(XSDataTruncate)


    def configure(self):
        EDPluginExecProcessScript.configure(self)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG('Truncate: preprocess')
        input_file = self.dataInput.input_file.value
        output_file = self.dataInput.output_file.value
        options = 'hklin {0} hklout {1}'.format(input_file, output_file)
        self.setScriptCommandline(options)
        self.DEBUG('command line options set to {0}'.format(options))

        nres = self.dataInput.nres.value
        anom = self.dataInput.anom.value
        res = self.dataInput.res.value
        if res is None:
            res = 0

        self.addListCommandExecution('nres {0}'.format(nres))
        self.addListCommandExecution('truncate YES')
        self.addListCommandExecution('anomalous {0}'.format(anom))
        self.addListCommandExecution('plot OFF')
        self.addListCommandExecution('labout F=F_xdsproc SIGF=SIGF_xdsproc')
        self.addListCommandExecution('falloff YES')
        self.addListCommandExecution('resolution 50 {0}'.format(res))
        self.addListCommandExecution('PNAME foo')
        self.addListCommandExecution('DNAME foo')
        self.addListCommandExecution('end')

    def checkParameters(self):
        self.DEBUG('Truncate: checkParameters')
        data_input = self.getDataInput()
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
        self.DEBUG('Truncate: process')
        EDPluginExecProcessScript.process(self)

    def postProcess(self):
        self.DEBUG('Truncate: postProcess')
        EDPluginExecProcessScript.postProcess(self)
        output_file = self.dataInput.output_file.value

        res = XSDataResult()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(os.path.exists(output_file))
        res.status = status

        self.dataOutput = res
