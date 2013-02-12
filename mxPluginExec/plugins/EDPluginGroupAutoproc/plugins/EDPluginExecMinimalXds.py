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
                EDVerbose.ERROR("resolution range must be 2 in length ({0} given)".format(resrange))
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

        file_template = parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='][0]

        # get the real directory the files are in by getting the real
        # path of the first image
        first_image_no = parsed_config['DATA_RANGE='][0]
        first_image = _template_to_image(file_template, first_image_no)
        real_data_dir = os.path.dirname(os.path.realpath(first_image))

        # create a link to this dir in our dir
        os.symlink(real_data_dir,
                   os.path.join(self.getWorkingDirectory(), 'i'))

        # and update the config to refer to this dir
        new_template = os.path.join('i', os.path.basename(file_template))
        parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='] = new_template

        # perhaps modify some params
        job = self.dataInput.job
        maxproc = self.dataInput.maxproc
        maxjobs = self.dataInput.maxjobs
        resolution_range = self.dataInput.resolution_range
        friedels_law = self.dataInput.friedels_law
        spot_range = self.dataInput.spot_range
        spacegroup = self.dataInput.spacegroup
        unit_cell = self.dataInput.unit_cell

        self.DEBUG('requested spot range is {0}'.format(spot_range))

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
        if spot_range is not None and len(spot_range) > 0:
            spot_range_list = list()
            for srange in spot_range:
                spot_range_list.append('{0} {1}'.format(srange.begin, srange.end))
            self.DEBUG('setting the spot range to {0} as requested'.format(spot_range_list))
            parsed_config['SPOT_RANGE='] = spot_range_list
        # unit cell might be an empty string or some other crazy stuff
        # we need 6 floats/ints
        if unit_cell is not None:
            ucells = unit_cell.value.split()
            if len(ucells) != 6:
                unit_cell = None
            else:
                try:
                    if any(float(x) == 0 for x in ucells):
                        unit_cell = None
                except ValueError:
                    unit_cell = None
        # both need to be specified
        if spacegroup is not None and unit_cell is not None:
            self.DEBUG('specific spacegroup requested: {0}'.format(spacegroup.value))
            self.DEBUG('specific unit cell requested: {0}'.format(unit_cell.value))
            parsed_config['SPACE_GROUP_NUMBER='] = str(spacegroup.value)
            parsed_config['UNIT_CELL_CONSTANTS='] = unit_cell.value

        # For [XY]-GEO_CORR files, link them in the cwd and fix their paths
        if 'X-GEO_CORR=' in parsed_config:
            xgeo = parsed_config['X-GEO_CORR='][0]
            os.symlink(xgeo,
                       os.path.join(self.getWorkingDirectory(), os.path.basename(xgeo)))
            parsed_config['X-GEO_CORR='] = os.path.basename(xgeo)
        if 'Y-GEO_CORR=' in parsed_config:
            ygeo = parsed_config['Y-GEO_CORR='][0]
            os.symlink(ygeo,
                       os.path.join(self.getWorkingDirectory(), os.path.basename(ygeo)))
            parsed_config['Y-GEO_CORR='] = os.path.basename(ygeo)

        # Save back the changes
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
        self.DEBUG('looking for {0}'.format(outfile))
        if not os.path.isfile(outfile):
            self.DEBUG('NOT FOUND')
            xsDataResult.succeeded = XSDataBoolean(False)
            self.setFailure()
        else:
            self.DEBUG('FOUND')
            xsDataResult.succeeded = XSDataBoolean(True)
        self.DEBUG('succeeded is {0} and succeeded.value is {1}'.format(xsDataResult.succeeded,
                                                                        xsDataResult.succeeded.value))
        self.setDataOutput(xsDataResult)



# XXX: This is the third file I copy this function to: extract it
# somewhere
def _template_to_image(fmt, num):
    # for simplicity we will assume the template to contain only one
    # sequence of '?' characters. max's code uses a regexp so this
    # further restrict the possible templates.
    start = fmt.find('?')
    end = fmt.rfind('?')
    if start == -1 or end == -1:
        # the caller test for the file existence and an empty path
        # does not exist
        return ''
    prefix = fmt[:start]
    suffix = fmt[end+1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + '{0:0' + str(length) + 'd}' + suffix

    return fmt_string.format(num)
