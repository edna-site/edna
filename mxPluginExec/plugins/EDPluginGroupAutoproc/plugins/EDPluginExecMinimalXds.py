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

from XSDataCommon import XSDataBoolean
from XSDataAutoproc import XSDataMinimalXdsIn, XSDataMinimalXdsOut
from xdscfgparser import parse_xds_file, dump_xds_file



class EDPluginExecMinimalXds(EDPluginExecProcessScript):
    """
    """


    def __init__(self ):
        """
        """
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataMinimalXdsIn)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMinimalXds.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file given")

        # really look into the mandatory arg
        xds_input = os.path.abspath(self.dataInput.input_file.value)
        if not (os.path.exists(xds_input) and os.path.isfile(xds_input)):
            self.setFailure()

        # if we have a resolution it has to be a list of 2 XSDataFloat
        resrange = self.dataInput.resolution_range
        if resrange is not None and len(resrange) != 0:
            # a non specified list input parameter has a default value
            # of [], seriously???
            if len(resrange) != 2:
                EDVerbose.ERROR("resolution range must be 2 in length ({} given)".format(resrange))
                self.setFailure()
                return


    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginMinimalXDS.preProcess")
        xds_input = os.path.abspath(self.dataInput.input_file.value)
        shutil.copy(xds_input, self.getWorkingDirectory())

        # our new xds file
        xds_file = os.path.join(self.getWorkingDirectory(), 'XDS.INP')

        parsed_config = parse_xds_file(xds_file)

        # try to make some symlinks to work around the path length
        # limitation of xds
        # TODO: don't even try if not on Unix

        # XXX: why did i make this config item a list instead of a
        # regular string?
        file_template = os.path.abspath(parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='][0])

        directory = os.path.dirname(file_template)
        filename = os.path.basename(file_template)

        matches = fnmatch.filter(os.listdir(directory), filename)
        our_dir = self.getWorkingDirectory()
        for f in matches:
            os.symlink(os.path.join(directory, f),
                       os.path.join(our_dir, f))
        # patch the template in the config by stripping the whole prefix
        parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='] = filename

        # perhaps modify some params
        job = self.dataInput.job
        maxproc = self.dataInput.maxproc
        maxjobs = self.dataInput.maxjobs
        resolution_range = self.dataInput.resolution_range
        friedels_law = self.dataInput.friedels_law

        if job is not None:
            parsed_config["JOB="] = job.value
        if maxproc is not None:
            parsed_config["MAXIMUM_NUMBER_OF_PROCESSORS="] = maxproc.value
        if maxjobs is not None:
            parsed_config["MAXIMUM_NUMBER_OF_JOBS="] = maxjobs.value
        if resolution_range is not None and len(resolution_range) != 0:
            parsed_config["INCLUDE_RESOLUTION_RANGE="] = [x.value for x in resolution_range]
        if friedels_law is not None:
            if friedels_law:
                parsed_config["FRIEDEL'S_LAW="] = "TRUE"
            else:
                parsed_config["FRIEDEL'S_LAW="] = "FALSE"
        dump_xds_file(xds_file, parsed_config)


    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginMinimalXds.process")


    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginMinimalXds.postProcess")
        # Create some output data
        xsDataResult = XSDataMinimalXdsOut()


        # XDS is considered to have succeeded iff CORRECT.LP has been created
        outfile = os.path.join(self.getWorkingDirectory(), 'CORRECT.LP')
        if not os.path.isfile(outfile):
            xsDataResult.succeeded = XSDataBoolean(False)
            self.setFailure()
        else:
            xsDataResult.succeeded = XSDataBoolean(True)
        self.setDataOutput(xsDataResult)
