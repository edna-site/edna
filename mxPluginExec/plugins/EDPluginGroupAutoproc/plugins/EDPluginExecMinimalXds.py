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


import os.path
import shutil

from EDPluginExecProcess import EDPluginExecProcess

from XSDataAutoproc import XSDataMinimalXDSIn, XSDataMinimalXDSOut
from xdscfgparser import parse_xds_file, dump_xds_file



class EDPluginExecMinimalXds(EDPluginExecProcess):
    """
    """


    def __init__(self ):
        """
        """
        EDPluginExecProcess.__init__(self )
        self.setXSDataInputClass(XSDataMinimalXDSIn)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExec<pluginName>.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file given")

        # really look into the mandatory arg
        xds_input = os.path.abspath(self.dataInput.input_file)
        if not (os.path.exists(xds_input) and os.path.isfile(xds_input)):
            self.setFailure()


    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginMinimalXDS.preProcess")
        xds_input = os.path.abspath(self.dataInput.input_file)
        shutil.copy(xds_input, self.getWorkingDirectory())

        # our new xds file
        xds_file = os.path.join(self.getWorkingDirectory(), 'XDS.INP')

        # perhaps modify some params
        job = self.dataInput.job
        maxproc = self.dataInput.maxproc
        maxjobs = self.dataInput.maxjobs

        # just skip the whole parsing and modif if there is nothing to
        # alter in the configuration
        if any([x is not None for x in [job, maxproc, maxjobs]]):
            parsed = parse_xds_file(xds_file)
            if job is not None:
                parsed["JOB="] = job
            if maxproc is not None:
                parsed["MAXIMUM_NUMBER_OF_PROCESSORS="] = maxproc
            if maxjobs is not None:
                parsed["MAXIMUM_NUMBER_OF_JOBS="] = maxjobs
            dump_xds_file(parsed, xds_file)


    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginMinimalXds.process")


    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginMinimalXds.postProcess")
        # Create some output data
        xsDataResult = XSDataMinimalXDSOut()


        # XDS is considered to have succeeded iff CORRECT.LP has been created
        outfile = os.path.join(self.getWorkingDirectory(), 'CORRECT.LP')
        if not os.path.isfile(outfile):
            xsDataResult.succeeded = False
            self.setFailure()
        else:
            xsDataResult.succeeded = True
        self.setDataOutput(xsDataResult)
