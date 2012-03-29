from __future__ import with_statement

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

from EDPlugin import EDPlugin
from EDVerbose import EDVerbose
from XSDataCommon import XSDataBoolean, XSDataFloat, XSDataVectorDouble
from XSDataAutoproc import XSDataResCutoff, XSDataResCutoffResult
from XSDataAutoproc import XSData2DCoordinates, XSDataXdsCompletenessEntry


class EDPluginResCutoff(EDPlugin):
    """
    """


    def __init__(self ):
        """
        """
        EDPlugin.__init__(self )
        self.setXSDataInputClass(XSDataResCutoff)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginParseXdsOutput.checkParameters")

        data_input = self.dataInput
        self.checkMandatoryParameters(data_input.completeness_entries,
                                      "no completeness entries in input")

    def preProcess(self, _edObject = None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.preProcess")

    def process(self, _edObject = None):
        EDPlugin.process(self)
        completeness_cutoff_param = self.dataInput.completeness_cutoff
        if completeness_cutoff_param is None:
            completeness_cutoff = 80
        else:
            completeness_cutoff = completeness_cutoff_param.value

        isig_cutoff_param = self.dataInput.isig_cutoff
        if isig_cutoff_param is None:
            isig_cutoff = 3
        else:
            isig_cutoff = isig_cutoff_param.value

        res_override = self.dataInput.res_override

        bins = list()

        # for the first iteration
        # comment from max's code: "less stringent at low res"
        local_completeness_cutoff = 70
        # declared but not initialized in the perl code
        prev_isig = prev_res = 0

        # XXX: if res is still not defined at the end it is set to
        # detector_max_res, which we should somehow defined (in the
        # data model?) and used as the default value before we start
        # the processing

        for entry in self.dataInput.completeness_entries:
            outer_res = entry.outer_res.value
            outer_complete = entry.outer_complete.value
            outer_rfactor = entry.outer_rfactor.value
            outer_isig = entry.outer_isig.value

            if outer_complete < local_completeness_cutoff or outer_isig < isig_cutoff or \
                    (res_override is not None and outer_res < res_override.value):
                if outer_complete < completeness_cutoff:
                    EDVerbose.DEBUG('incomplete data (%s) in this shell' % outer_complete)
                    res = prev_res
                else:
                    res = _calculate_res_from_bins(prev_isig, prev_res,
                                                   outer_isig, outer_res)
                bins.append(outer_res)

                #NOTE: get out of the loop, see the value of `skip` in
                #max's code
                break
            else:
                bins.append(outer_res)
            prev_res, prev_isig = outer_res, outer_isig

        # Now the implementation of what max does when he encouters
        # the total values, which are conveniently already parsed in
        # our case
        if len(bins) < 2:
            EDVerbose.DEBUG("No bins with I/sigma greater than %s" % isig_cutoff)
            EDVerbose.DEBUG("""something could be wrong, or the completeness could be too low!
bravais lattice/SG could be incorrect or something more insidious like
incorrect parameters in XDS.INP like distance, X beam, Y beam, etc.
Stopping""")
            self.setFailure()
            return
        if res_override is not None:
            res = res_override.value
        # remove last bin (see why w/ max)
        retbins = [XSDataFloat(x) for x in bins[:-1]]


        data_output = XSDataResCutoffResult()
        data_output.res = XSDataFloat(res)
        data_output.bins = retbins
        totals = self.dataInput.total_completeness
        data_output.total_complete = totals.outer_complete
        data_output.total_rfactor = totals.outer_rfactor
        data_output.total_isig = totals.outer_isig

        self.dataOutput = data_output

    def postProcess(self, _edObject = None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.postProcess")


# straight port of max's code, reusing the same var names (pythonized)
def _calculate_res_from_bins(prev_isig, prev_res, outer_isig, outer_res):
    diff_i = prev_isig - outer_isig
    diff_d = prev_res - outer_res

    hyp = math.sqrt((diff_i ** 2) + (diff_d ** 2))
    alpha = math.atan(diff_i / diff_d)

    res_id = isig_cutoff - outer_isig
    res_offset = res_id / math.tan(alpha)

    return res_offset + outer_res
