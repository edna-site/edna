# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:        <author>
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

__author__="<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"


import os.path

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString

from XSDataAutoproc import XSDataAutoprocInput
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc

from xdscfgparser import parse_xds_file, dump_xds_file

class EDPluginControlAutoprocMaster(EDPluginControl):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataAutoprocInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        input_file = self.dataInput.input_file
        if input_file is None:
            EDVerbose.ERROR('no xds input file given, giving up')
            self.setFailure()
            return

        input_file = input_file.value
        if not os.path.exists(input_file):
            EDVerbose.ERROR('the specified input file does not seem to exist,'
                            ' giving up')
            self.setFailure()
            return

        # we need to "fix" the input file so the SPOT_RANGE gets set
        # to a sensible value
        cfg = parse_xds_file(input_file)
        spot_range = _spot_range(cfg)
        if len(spot_range) != 0:
            cfg['SPOT_RANGE='] = spot_range

        #SECONDS is also set to 20
        cfg['SECONDS='] = 20
        dump_xds_file(input_file, cfg)

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoprocMaster.preProcess")

        # instantiate the plugins
        self.wait_intput_files = self.loadPlugin("EDPluginWaitFile")
        self.ispyb_upload = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4")


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoprocMaster.process")


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoprocMaster.postProcess")


# for the original see xdsproc.pl::spot_range(). Determine a suitable
# value for the SPOT_RANGE XDS input file
def _spot_range(cfg):
    """straight port of max's code. we will return a list of strings
    in the format "START END" or an empty list in case anything goes
    wrong."""

    template = cfg['NAMED_TEMPLATE_OF_DATA_FILES=']
    osc_range = cfg['OSCILLATION_RANGE=']
    data_range = cfg['DATA_RANGE=']

    startimage = data_range[0]

    # reuse more or less the same variable names
    eranges = [[90, 85, 80 ,75 ,70 ,65 ,60],
               [45, 40, 35, 30, 25, 20, 15]]
    res=list()
    for range_ in eranges:
        for angle in range_:
            imnumber = startimage+(angle//osc_range)
            filename = _template_to_image(template, imnumber)
            if os.path.exists(filename):
                startno = imnumber-10
                if startno < 0:
                    continue #try the next angle
                else:
                    res.append("{0} {1}".format(startno, imnumber))
                    break # next erange
            else:
                EDVerbose.DEBUG('file {0} does not exist'.format(filename))
    return res

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
