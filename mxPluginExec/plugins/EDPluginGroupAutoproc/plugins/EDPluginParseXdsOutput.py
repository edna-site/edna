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


from __future__ import with_statement

import os.path
import shutil

from XSDataCommon import XSDataBoolean
from XSDataAutoproc import

class EDPluginParseXdsOutput(EDPlugin):
    """
    """


    def __init__(self ):
        """
        """
        EDPlugin.__init__(self )
        self.setXSDataInputClass(XSDataMinimalXDSIn)


        self.parsing_start_re = re.compile('OR EXPECTED TO BE ABSENT')
        # yep, this is horrible
        self.table_item_re = re.compile('\s+(\d+\.\d+)\s+\S+\s+\S+\s+\S+\s+(\S+)\%\s+(\S+)\%\s+\S+\%\s+\S+\s+(\S+)\s+\S+\%\s+\S+\%\s+\S+')
        self.table_end_re = re.compile('^\s+total')



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginParseXdsOutput.checkParameters")
        self.checkMandatoryParameters(self.dataInput.correct_lp, "No XDS input file given")

        # now really check it
        path = self.dataInput.correct_lp.value
        if not os.path.isfile(path):
            self.setFailure()

    def preProcess(self, _edObject = None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.preProcess")

    def process(self, _edObject = None):
        EDPlugin.process(self)

        # we need to parse the second table after the line ending in
        # 'OR EXPECTED TO BE ABSENT'. The table ends when the first
        # column value is 'total'
        started = False
        # I'm using more or less the same variable names than Max to
        # make reviews easier
        bins = list()
        local_completeness_cutoff = float(70)


        with open(self.dataInput.correct_lp.value, 'r') as f:
            for line in f:
                # are we there yet?
                if self.parsing_start_re.match(line):
                    started = True
                if started:
                    # see if we are at a relevant line
                    match = self.table_item_re.match(line)
                    # yep? extract values
                    if match is not None:
                        outer_res = float(match.group(0))
                        outer_complete = float(match.group(1))
                        outer_rfactor = float(match.group(2))
                        outer_isig = float(match.group(3))

    def postProcess(self, _edObject = None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.postProcess")
