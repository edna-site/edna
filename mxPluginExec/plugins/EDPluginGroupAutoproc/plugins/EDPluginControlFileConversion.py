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
import tempfile

from EDPluginControl import EDPluginControl

from XSDataCommon import XSDataStatus, XSDataBoolean, XSDataResult, XSDataString
from XSDataAutoproc import XSDataFileConversion
from XSDataAutoproc import XSDataPointless, XSDataAimless
from XSDataAutoproc import XSDataTruncate, XSDataUniqueify

class EDPluginControlFileConversion(EDPluginControl):
    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataFileConversion)

    def configure(self):
        EDPluginControl.configure(self)

    def preProcess(self):
        EDPluginControl.preProcess(self)
        self.DEBUG('FileConversion: preprocess')
        infile = self.dataInput.input_file.value
        outfile = self.dataInput.output_file.value

        self.pointless = self.loadPlugin("EDPluginExecPointless")
        self.aimless = self.loadPlugin("EDPluginExecAimless")
        self.truncate = self.loadPlugin("EDPluginExecTruncate")
        self.uniqueify = self.loadPlugin("EDPluginExecUniqueify")

        anom = "anom" if self.dataInput.anom.value else "noanom"
        self.output_basename = "unmerged_{0}_pointless".format(anom)


    def checkParameters(self):
        self.DEBUG('FileConversion: checkParameters')
        self.checkMandatoryParameters(self.dataInput.input_file, 'no input file')
        self.checkMandatoryParameters(self.dataInput.output_file, 'no output file')

        # now really check the parameters
        if self.dataInput.input_file is not None:
            path = self.dataInput.input_file.value
            if not os.path.exists(path):
                self.ERROR('input file {0} does not exist'.format(path))
                self.setFailure()
                return

    def process(self):
        self.DEBUG('FileConversion: process')
        EDPluginControl.process(self)
        # first we generate the intermediary file name
        pointless_in = XSDataPointless()
        pointless_in.input_file = self.dataInput.input_file
        pointless_out = os.path.join(os.path.dirname(self.dataInput.output_file.value),
                                     "{0}_multirecord.mtz".format(self.output_basename))
        pointless_in.output_file = XSDataString(pointless_out)
        self.pointless.dataInput = pointless_in
        self.DEBUG("Pointless")
        self.pointless.executeSynchronous()
        if self.pointless.isFailure():
            self.DEBUG("... it failed")
            self.setFailure()
            return

        # now aimless (was scala in max pipeline)
        temp_file = tempfile.NamedTemporaryFile(suffix='.mtz',
                                                prefix='tmp-',
                                                dir=self.aimless.getWorkingDirectory(),
                                                delete=False)
        aimless_out = os.path.abspath(temp_file.name)
        temp_file.close()

        aimless_in = XSDataAimless()
        aimless_in.input_file = pointless_in.output_file
        aimless_in.output_file = XSDataString(aimless_out)
        aimless_in.dataCollectionID = self.dataInput.dataCollectionID
        aimless_in.start_image = self.dataInput.start_image
        aimless_in.end_image = self.dataInput.end_image
        aimless_in.res = self.dataInput.res
        aimless_in.anom = self.dataInput.anom

        self.aimless.dataInput = aimless_in
        self.DEBUG("Aimless")
        self.aimless.executeSynchronous()
        if self.aimless.isFailure():
            self.DEBUG("...failed")
            self.setFailure()
            return

        # now truncate
        truncate_in = XSDataTruncate()
        truncate_in.input_file = self.aimless.dataInput.output_file
        temp_file = tempfile.NamedTemporaryFile(suffix='.mtz',
                                                prefix='tmp2-',
                                                dir=self.aimless.getWorkingDirectory(),
                                                delete=False)
        truncate_in.output_file = XSDataString(temp_file.name)
        temp_file.close()
        truncate_in.nres = self.dataInput.nres
        truncate_in.anom = self.dataInput.anom
        truncate_in.res = self.dataInput.res

        self.truncate.dataInput = truncate_in
        self.DEBUG("Truncate")
        self.truncate.executeSynchronous()
        if self.truncate.isFailure():
            self.DEBUG("...failed")
            self.setFailure()
            return

        # and finally uniqueify
        uniqueify_in = XSDataUniqueify()
        uniqueify_in.input_file = truncate_in.output_file
        uniqueify_out = os.path.join(os.path.dirname(self.dataInput.output_file.value),
                                     self.output_basename + ".mtz")
        uniqueify_in.output_file = XSDataString(uniqueify_out)

        self.uniqueify.dataInput = uniqueify_in

        self.DEBUG("Uniqueify")
        self.uniqueify.executeSynchronous()
        if self.uniqueify.isFailure():
            self.DEBUG("...failed")
            self.setFailure()
            return

    def postProcess(self):
        self.DEBUG('FileConversion: postProcess')
        EDPluginControl.postProcess(self)
        output_file = self.dataInput.output_file.value

        res = XSDataResult()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(os.path.exists(output_file))
        res.status = status

        self.dataOutput = res
