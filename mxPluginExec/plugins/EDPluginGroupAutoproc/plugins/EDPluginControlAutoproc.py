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
import time

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString

from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataResCutoff
from XSDataAutoproc import XSDataMinimalXdsIn
from XSDataAutoproc import XSDataXdsGenerateInput
from XSDataAutoproc import XSDataXdsOutputFile
from XSDataAutoproc import XSDataXscaleInput
from XSDataAutoproc import XSDataXscaleInputFile


edFactoryPlugin.loadModule('XSDataISPyBv1_4')
# plugin input/output
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc

# what actually goes inside
from XSDataISPyBv1_4 import AutoProcContainer, AutoProc, AutoProcScalingContainer
from XSDataISPyBv1_4 import AutoProcScaling, AutoProcScalingStatistics
from XSDataISPyBv1_4 import AutoProcIntegrationContainer, AutoProcIntegration
from XSDataISPyBv1_4 import AutoProcProgramContainer, AutoProcProgram
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import Image

from xdscfgparser import parse_xds_file, dump_xds_file

class EDPluginControlAutoproc( EDPluginControl ):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataAutoprocInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoproc.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")

        # at least check for the xds input file existence before
        # trying to start anything even if the first xds run does it
        # anyway
        if not os.path.isfile(self.dataInput.input_file.path.value):
            EDVerbose.ERROR('the specified input file does not exist')
            self.setFailure()
            return

    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoproc.preProcess")

        data_in = self.dataInput
        xds_in = XSDataMinimalXdsIn()
        xds_in.input_file = data_in.input_file.path

        # we'll need the low res limit later on
        lowres = data_in.low_resolution_limit
        if lowres is not None:
            self.low_resolution_limit = lowres.value
        else:
            self.low_resolution_limit = 50

        res_override = data_in.res_override
        if res_override is not None:
            self.res_override = res_override.value
        else:
            # XXX: default to 0?
            self.res_override = None

        # modify the XDS.INP file to reflect these values, if
        # specified
        conf = parse_xds_file(data_in.input_file.path.value)
        resrange = conf.get('INCLUDE_RESOLUTION_RANGE=')

        if resrange is not None:
            if self.low_resolution_limit is not None:
                resrange[0] = self.low_resolution_limit
            if self.res_override is not None:
                resrange[1] = self.res_override
            conf['INCLUDE_RESOLUTION_RANGE='] = resrange
            dump_xds_file(data_in.input_file.path.value, conf)


        self.xds_first = self.loadPlugin("EDPluginControlRunXds")
        self.xds_first.dataInput = xds_in

        self.generate = self.loadPlugin("EDPluginXDSGenerate")

        self.first_res_cutoff = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_anom = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_noanom = self.loadPlugin("EDPluginResCutoff")

        self.parse_xds_anom = self.loadPlugin("EDPluginParseXdsOutput")
        self.parse_xds_noanom = self.loadPlugin("EDPluginParseXdsOutput")

        self.xscale_anom = self.loadPlugin("EDPluginControlXscaleGenerate")
        self.xscale_noanom = self.loadPlugin("EDPluginControlXscaleGenerate")

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoproc.process")

        # first XDS plugin run with supplied XDS file
        EDVerbose.screen("First XDS run...")
        self.xds_first.executeSynchronous()
        if self.xds_first.isFailure():
            EDVerbose.ERROR('first XDS run failed')
            self.setFailure()
            return
        EDVerbose.screen("First XDS run successfully completed")

        # apply the first res cutoff with the res extracted from the first XDS run
        EDVerbose.screen("First resolution cutoff")
        xdsresult = self.xds_first.dataOutput
        res_cutoff_in = XSDataResCutoff()
        res_cutoff_in.xds_res = xdsresult
        res_cutoff_in.completeness_entries = xdsresult.completeness_entries
        res_cutoff_in.detector_max_res = self.dataInput.detector_max_res

        #XXX: remove from the data model as it is just pass-through?
        res_cutoff_in.total_completeness = xdsresult.total_completeness
        res_cutoff_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.first_res_cutoff.dataInput = res_cutoff_in
        self.first_res_cutoff.executeSynchronous()
        if self.first_res_cutoff.isFailure():
            EDVerbose.ERROR("res cutoff failed")
            self.setFailure()
            return
        EDVerbose.screen("First resolution cutoff successfully completed")
        resolution = self.first_res_cutoff.dataOutput.res

        # for the generate w/ and w/out anom we have to specify where
        # the first XDS plugin run took place
        xds_run_directory = os.path.abspath(self.xds_first.dataOutput.xds_run_directory.value)
        EDVerbose.screen("the xds run took place in {}".format(xds_run_directory))
        generate_input = XSDataXdsGenerateInput()
        generate_input.resolution = resolution
        generate_input.previous_run_dir = XSDataString(xds_run_directory)
        self.generate.dataInput = generate_input

        self.generate.executeSynchronous()

        if self.generate.isFailure():
            EDVerbose.ERROR('generating w/ and w/out anom failed')
            self.setFailure()
            return

        # we can now use the xds output parser on the two correct.lp
        # files, w/ and w/out anom
        parse_anom_input = XSDataXdsOutputFile()
        parse_anom_input.correct_lp = XSDataFile()
        parse_anom_input.correct_lp.path = self.generate.dataOutput.correct_lp_anom

        # this one is the same as the first XDS run since they share
        # the same directory
        gxparm_file_anom = XSDataFile()
        gxparm_file_anom.path = self.generate.dataOutput.gxparm
        parse_anom_input.gxparm = gxparm_file_anom

        self.parse_xds_anom.dataInput = parse_anom_input
        self.parse_xds_anom.executeSynchronous()

        if self.parse_xds_anom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # now the other one w/out anom
        parse_noanom_input = XSDataXdsOutputFile()
        parse_noanom_input.correct_lp = XSDataFile()
        parse_noanom_input.correct_lp.path = self.generate.dataOutput.correct_lp_no_anom

        gxparm_file_noanom = XSDataFile()
        gxparm_file_noanom.path = self.generate.dataOutput.gxparm
        parse_noanom_input.gxparm = gxparm_file_noanom

        self.parse_xds_noanom.dataInput = parse_noanom_input
        self.parse_xds_noanom.executeSynchronous()

        if self.parse_xds_noanom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # we now can apply the res cutoff on the anom and no anom
        # outputs. Note that this is not done in parallel, like the
        # xds parsing

        # XXX completeness_cutoff/res_override and isig_cutoff still
        # missing
        res_cutoff_anom_in = XSDataResCutoff()
        res_cutoff_anom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_anom_in.xds_res = self.parse_xds_anom.dataOutput
        res_cutoff_anom_in.completeness_entries = self.parse_xds_anom.dataOutput.completeness_entries
        res_cutoff_anom_in.total_completeness = self.parse_xds_anom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_anom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_anom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_anom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_anom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_anom.dataInput = res_cutoff_anom_in

        self.res_cutoff_anom.executeSynchronous()
        if self.res_cutoff_anom.isFailure():
            EDVerbose.ERROR('res cutoff for anom data failed')

        # same for non anom
        res_cutoff_noanom_in = XSDataResCutoff()
        res_cutoff_noanom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_noanom_in.xds_res = self.parse_xds_noanom.dataOutput
        res_cutoff_noanom_in.completeness_entries = self.parse_xds_noanom.dataOutput.completeness_entries
        res_cutoff_noanom_in.total_completeness = self.parse_xds_noanom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_noanom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_noanom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_noanom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_noanom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_noanom.dataInput = res_cutoff_noanom_in

        self.res_cutoff_noanom.executeSynchronous()
        if self.res_cutoff_noanom.isFailure():
            EDVerbose.ERROR('res cutoff for non anom data failed')

        # now we just have to run XScale to generate w/ and w/out
        # anom, merged and unmerged

        # We use another control plugin for that to isolate the whole thing
        xscale_anom_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path = self.generate.dataOutput.hkl_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_anom_in.xds_files = [input_file]
        xscale_anom_in.unit_cell_constants = self.parse_xds_anom.dataOutput.unit_cell_constants
        xscale_anom_in.sg_number = self.parse_xds_anom.dataOutput.sg_number
        xscale_anom_in.bins = self.res_cutoff_anom.dataOutput.bins


        self.xscale_anom.dataInput = xscale_anom_in
        self.xscale_anom.executeSynchronous()

        if self.xscale_anom.isFailure():
            EDVerbose.ERROR('xscale anom/merge generation failed')

        # same for non anom code path

        xscale_noanom_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path = self.generate.dataOutput.hkl_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_noanom_in.xds_files = [input_file]
        xscale_noanom_in.unit_cell_constants = self.parse_xds_noanom.dataOutput.unit_cell_constants
        xscale_noanom_in.sg_number = self.parse_xds_noanom.dataOutput.sg_number
        xscale_noanom_in.bins = self.res_cutoff_noanom.dataOutput.bins

        self.xscale_noanom.dataInput = xscale_noanom_in
        self.xscale_noanom.executeSynchronous()

        if self.xscale_noanom.isFailure():
            EDVerbose.ERROR('xscale anom/merge generation failed')


    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

        #Now that we have executed the whole thing we need to create
        #the suitable ISPyB plugin input and serialize it to the file
        #we've been given as input
        output = AutoProcContainer()

        # AutoProc attr
        autoproc = AutoProc()

        xdsout = self.xds_first.dataOutput
        if xdsout.sg_number is not None: # and it should not
            autoproc.spaceGroup = SPACE_GROUP_NAMES[xdsout.sg_number.value]
        autoproc.refinedCell_a = xdsout.cell_a.value
        autoproc.refinedCell_b = xdsout.cell_b.value
        autoproc.refinedCell_c = xdsout.cell_c.value
        autoproc.refinedCell_alpha = xdsout.cell_alpha.value
        autoproc.refinedCell_beta = xdsout.cell_beta.value
        autoproc.refinedCell_gamm1a = xdsout.cell_gamma.value

        output.AutoProc = autoproc

        # scaling container and all the things that go in
        scaling_container = AutoProcScalingContainer()
        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        scaling_container.AutoProcScaling = scaling


        # FIXME: handle the anom path as well. It seems that max
        # generates a whole different data model for that
        xscale_stats = self.xscale_noanom.dataOutput.stats_noanom_merged
        inner_stats = xscale_stats.completeness_entries[0]
        outer_stats = xscale_stats.completeness_entries[-1]
        total_stats = xscale_stats.total_completeness

        stats = _create_scaling_stats(inner_stats, 'inner',
                                      self.low_resolution_limit, 0)
        scaling_container.AutoProcScalingStatistics.append(stats)

        stats = _create_scaling_stats(outer_stats, 'outer',
                                      self.low_resolution_limit, 0)
        scaling_container.AutoProcScalingStatistics.append(stats)
        stats = _create_scaling_stats(total_stats, 'total',
                                      self.low_resolution_limit, 0)
        scaling_container.AutoProcScalingStatistics.append(stats)


        integration_container = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.data_collection_id.value
        integration_container.Image = image

        integration = AutoProcIntegration()
        crystal_stats =  self.parse_xds_noanom.dataOutput
        integration.cell_a = crystal_stats.cell_a.value
        integration.cell_b = crystal_stats.cell_b.value
        integration.cell_c = crystal_stats.cell_c.value
        integration.cell_alpha = crystal_stats.cell_alpha.value
        integration.cell_beta = crystal_stats.cell_beta.value
        integration.cell_gamma = crystal_stats.cell_gamma.value
        integration.anomalous = 0

        # done with the integration
        integration_container.AutoProcIntegration = integration
        scaling_container.AutoProcIntegrationContainer = integration_container

        # done with the autoproc scaling container, add it to the main
        # output container
        output.AutoProcScalingContainer = scaling_container


        with open(self.dataInput.output_file.path.value, 'w') as f:
            f.write(output.marshal())


def _create_scaling_stats(xscale_stats, stats_type, lowres, anom):
    stats = AutoProcScalingStatistics()
    stats.scalingStatisticsType = stats_type
    stats.resolutionLimitLow = lowres
    if stats_type != 'total':
        stats.resolutionLimitHigh = xscale_stats.outer_res.value
    stats.meanIOverSigI = xscale_stats.outer_isig.value
    stats.completeness = xscale_stats.outer_complete.value
    stats.multiplicity = xscale_stats.multiplicity.value
    stats.nTotalObservations = xscale_stats.outer_observed.value
    stats.rMerge = xscale_stats.outer_rfactor.value
    stats.anomalous = anom

    return stats


# taken straight from max's code
SPACE_GROUP_NAMES = {
    1: ' P 1 ',
    2: ' P -1 ',
    3: ' P 1 2 1 ',
    4: ' P 1 21 1 ',
    5: ' C 1 2 1 ',
    6: ' P 1 m 1 ',
    7: ' P 1 c 1 ',
    8: ' C 1 m 1 ',
    9: ' C 1 c 1 ',
    10: ' P 1 2/m 1 ',
    11: ' P 1 21/m 1 ',
    12: ' C 1 2/m 1 ',
    13: ' P 1 2/c 1 ',
    14: ' P 1 21/c 1 ',
    15: ' C 1 2/c 1 ',
    16: ' P 2 2 2 ',
    17: ' P 2 2 21 ',
    18: ' P 21 21 2 ',
    19: ' P 21 21 21 ',
    20: ' C 2 2 21 ',
    21: ' C 2 2 2 ',
    22: ' F 2 2 2 ',
    23: ' I 2 2 2 ',
    24: ' I 21 21 21 ',
    25: ' P m m 2 ',
    26: ' P m c 21 ',
    27: ' P c c 2 ',
    28: ' P m a 2 ',
    29: ' P c a 21 ',
    30: ' P n c 2 ',
    31: ' P m n 21 ',
    32: ' P b a 2 ',
    33: ' P n a 21 ',
    34: ' P n n 2 ',
    35: ' C m m 2 ',
    36: ' C m c 21 ',
    37: ' C c c 2 ',
    38: ' A m m 2 ',
    39: ' A b m 2 ',
    40: ' A m a 2 ',
    41: ' A b a 2 ',
    42: ' F m m 2 ',
    43: ' F d d 2 ',
    44: ' I m m 2 ',
    45: ' I b a 2 ',
    46: ' I m a 2 ',
    47: ' P m m m ',
    48: ' P n n n ',
    49: ' P c c m ',
    50: ' P b a n ',
    51: ' P m m a1 ',
    52: ' P n n a1 ',
    53: ' P m n a1 ',
    54: ' P c c a1 ',
    55: ' P b a m1 ',
    56: ' P c c n1 ',
    57: ' P b c m1 ',
    58: ' P n n m1 ',
    59: ' P m m n1 ',
    60: ' P b c n1 ',
    61: ' P b c a1 ',
    62: ' P n m a1 ',
    63: ' C m c m1 ',
    64: ' C m c a1 ',
    65: ' C m m m ',
    66: ' C c c m ',
    67: ' C m m a ',
    68: ' C c c a ',
    69: ' F m m m ',
    70: ' F d d d ',
    71: ' I m m m ',
    72: ' I b a m ',
    73: ' I b c a1 ',
    74: ' I m m a1 ',
    75: ' P 4 ',
    76: ' P 41 ',
    77: ' P 42 ',
    78: ' P 43 ',
    79: ' I 4 ',
    80: ' I 41 ',
    81: ' P -4 ',
    82: ' I -4 ',
    83: ' P 4/m ',
    84: ' P 42/m ',
    85: ' P 4/n ',
    86: ' P 42/n ',
    87: ' I 4/m ',
    88: ' I 41/a ',
    89: ' P 4 2 2 ',
    90: ' P 4 21 2 ',
    91: ' P 41 2 2 ',
    92: ' P 41 21 2 ',
    93: ' P 42 2 2 ',
    94: ' P 42 21 2 ',
    95: ' P 43 2 2 ',
    96: ' P 43 21 2 ',
    97: ' I 4 2 2 ',
    98: ' I 41 2 2 ',
    99: ' P 4 m m ',
    100: ' P 4 b m ',
    101: ' P 42 c m ',
    102: ' P 42 n m ',
    103: ' P 4 c c ',
    104: ' P 4 n c ',
    105: ' P 42 m c ',
    106: ' P 42 b c ',
    107: ' I 4 m m ',
    108: ' I 4 c m ',
    109: ' I 41 m d ',
    110: ' I 41 c d ',
    111: ' P -4 2 m ',
    112: ' P -4 2 c ',
    113: ' P -4 21 m ',
    114: ' P -4 21 c ',
    115: ' P -4 m 2 ',
    116: ' P -4 c 2 ',
    117: ' P -4 b 2 ',
    118: ' P -4 n 2 ',
    119: ' I -4 m 2 ',
    120: ' I -4 c 2 ',
    121: ' I -4 2 m ',
    122: ' I -4 2 d ',
    123: ' P 4/m m m ',
    124: ' P 4/m c c ',
    125: ' P 4/n b m ',
    126: ' P 4/n n c ',
    127: ' P 4/m b m1 ',
    128: ' P 4/m n c1 ',
    129: ' P 4/n m m1 ',
    130: ' P 4/n c c1 ',
    131: ' P 42/m m c ',
    132: ' P 42/m c m ',
    133: ' P 42/n b c ',
    134: ' P 42/n n m ',
    135: ' P 42/m b c ',
    136: ' P 42/m n m ',
    137: ' P 42/n m c ',
    138: ' P 42/n c m ',
    139: ' I 4/m m m ',
    140: ' I 4/m c m ',
    141: ' I 41/a m d ',
    142: ' I 41/a c d ',
    143: ' P 3 ',
    144: ' P 31 ',
    145: ' P 32 ',
    146: ' H 3 ',
    147: ' P -3 ',
    148: ' H -3 ',
    149: ' P 3 1 2 ',
    150: ' P 3 2 1 ',
    151: ' P 31 1 2 ',
    152: ' P 31 2 1 ',
    153: ' P 32 1 2 ',
    154: ' P 32 2 1 ',
    155: ' H 3 2 ',
    156: ' P 3 m 1 ',
    157: ' P 3 1 m ',
    158: ' P 3 c 1 ',
    159: ' P 3 1 c ',
    160: ' H 3 m ',
    161: ' H 3 c ',
    162: ' P -3 1 m ',
    163: ' P -3 1 c ',
    164: ' P -3 m 1 ',
    165: ' P -3 c 1 ',
    166: ' H -3 m ',
    167: ' H -3 c ',
    168: ' P 6 ',
    169: ' P 61 ',
    170: ' P 65 ',
    171: ' P 62 ',
    172: ' P 64 ',
    173: ' P 63 ',
    174: ' P -6 ',
    175: ' P 6/m ',
    176: ' P 63/m ',
    177: ' P 6 2 2 ',
    178: ' P 61 2 2 ',
    179: ' P 65 2 2 ',
    180: ' P 62 2 2 ',
    181: ' P 64 2 2 ',
    182: ' P 63 2 2 ',
    183: ' P 6 m m ',
    184: ' P 6 c c ',
    185: ' P 63 c m ',
    186: ' P 63 m c ',
    187: ' P -6 m 2 ',
    188: ' P -6 c 2 ',
    189: ' P -6 2 m ',
    190: ' P -6 2 c ',
    191: ' P 6/m m m ',
    192: ' P 6/m c c ',
    193: ' P 63/m c m ',
    194: ' P 63/m m c ',
    195: ' P 2 3 ',
    196: ' F 2 3 ',
    197: ' I 2 3 ',
    198: ' P 21 3 ',
    199: ' I 21 3 ',
    200: ' P m -3 ',
    201: ' P n -3 ',
    202: ' F m -3 ',
    203: ' F d -3 ',
    204: ' I m -3 ',
    205: ' P a -31 ',
    206: ' I a -31 ',
    207: ' P 4 3 2 ',
    208: ' P 42 3 2 ',
    209: ' F 4 3 2 ',
    210: ' F 41 3 2 ',
    211: ' I 4 3 2 ',
    212: ' P 43 3 2 ',
    213: ' P 41 3 2 ',
    214: ' I 41 3 2 ',
    215: ' P -4 3 m ',
    216: ' F -4 3 m ',
    217: ' I -4 3 m ',
    218: ' P -4 3 n ',
    219: ' F -4 3 c ',
    220: ' I -4 3 d ',
    221: ' P m -3 m ',
    222: ' P n -3 n ',
    223: ' P m -3 n1 ',
    224: ' P n -3 m1 ',
    225: ' F m -3 m ',
    226: ' F m -3 c ',
    227: ' F d -3 m1 ',
    228: ' F d -3 c1 ',
    229: ' I m -3 m ',
    230: ' I a -3 d1 ',
}
