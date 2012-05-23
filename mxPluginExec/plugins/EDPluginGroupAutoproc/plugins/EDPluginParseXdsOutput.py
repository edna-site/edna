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
from XSDataCommon import XSDataBoolean, XSDataInteger, XSDataFloat
from XSDataCommon import XSDataVectorDouble, XSDataString
from XSDataAutoproc import XSDataXdsOutputFile, XSDataXdsOutput
from XSDataAutoproc import XSData2DCoordinates, XSDataXdsCompletenessEntry


# Stuff we are interested about is (extract from output file):
#
#  ******************************************************************************
#   REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES
#  ******************************************************************************
#
#
#  REFINED PARAMETERS:  DISTANCE BEAM ORIENTATION CELL AXIS
#  USING   12133 INDEXED SPOTS
#  STANDARD DEVIATION OF SPOT    POSITION (PIXELS)     1.15
#  STANDARD DEVIATION OF SPINDLE POSITION (DEGREES)    0.14
# --> CRYSTAL MOSAICITY (DEGREES)     0.216
# --> DIRECT BEAM COORDINATES (REC. ANGSTROEM)   0.000380 -0.001976  0.932599
# --> DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM    1548.74   1552.51
# --> DETECTOR ORIGIN (PIXELS) AT                     1547.73   1557.77
# --> CRYSTAL TO DETECTOR DISTANCE (mm)       254.69
#  LAB COORDINATES OF DETECTOR X-AXIS  1.000000  0.000000  0.000000
#  LAB COORDINATES OF DETECTOR Y-AXIS  0.000000  1.000000  0.000000
#  LAB COORDINATES OF ROTATION AXIS  0.999969  0.006941 -0.003829
# --> COORDINATES OF UNIT CELL A-AXIS    51.363    28.218   -24.837
#  COORDINATES OF UNIT CELL B-AXIS    -8.155    -1.394    63.110
#  COORDINATES OF UNIT CELL C-AXIS    52.606   -91.551     4.775
#  REC. CELL PARAMETERS   0.018141  0.018141  0.009461  90.000  90.000  60.000
#  UNIT CELL PARAMETERS     63.650    63.650   105.697  90.000  90.000 120.000
#  E.S.D. OF CELL PARAMETERS  1.5E-01 1.5E-01 2.0E-01 0.0E+00 0.0E+00 0.0E+00
#  SPACE GROUP NUMBER    182
#
#
#  THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
#  SPACE_GROUP_NUMBER=  182
# --> UNIT_CELL_CONSTANTS=    63.65    63.65   105.70  90.000  90.000 120.000
#
# and the second table after the line ending in 'OR EXPECTED TO BE ABSENT'

# first approach used regexpes but it was too horrible.

class EDPluginParseXdsOutput(EDPlugin):
    """
    """


    def __init__(self ):
        """
        """
        EDPlugin.__init__(self )
        self.setXSDataInputClass(XSDataXdsOutputFile)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginParseXdsOutput.checkParameters")
        self.checkMandatoryParameters(self.dataInput.correct_lp, "No XDS input file given")

        # now really check it
        path = self.dataInput.correct_lp.path.value
        if not os.path.isfile(path):
            self.setFailure()

    def preProcess(self, _edObject = None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.preProcess")

    def process(self, _edObject = None):
        EDPlugin.process(self)

        output = XSDataXdsOutput()

        # get all the file's contents, find where the info is and then
        # use helper functions to retrieve stuff and put it in the
        # data model
        try:
            f = open(self.dataInput.correct_lp.path.value, 'r')
            lines = f.readlines()
        except IOError:
            EDVerbose.ERROR('Could not open the specified XDS output file for reading')
            self.setFailure()
            return

        # look for the "big piece of information"
        info_begin = None
        info_end = None
        for lineno, line in enumerate(lines):
            if info_begin is None:
                if line.find('REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES') != -1:
                    info_begin = lineno
            else:
                if line.find('MEAN INTENSITY AS FUNCTION OF SPINDLE POSITION WITHIN DATA IMAGE') != -1:
                    info_end = lineno
                    break

        if info_begin is None or info_end is None:
            EDVerbose.ERROR('could not find the refined parameters')
            self.setFailure()
            return

        _extract_infos(lines[info_begin:info_end], output)

        # second pass, look for the interesting table
        info_begin = None
        info_end = None
        started = False
        for line_no, line in enumerate(lines):
            if line.find('REFLECTIONS OF TYPE H,0,0  0,K,0  0,0,L OR EXPECTED TO BE ABSENT (*)') != -1:
                # the table will start shortly after
                started = True
                continue
            if started:
                # look if we are at the table yet
                if line.find('LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected') != -1:
                    # there's an empty line after the header
                    info_begin = line_no + 2
                if info_begin is not None and line.find('total') != -1:
                    # we're at the last table line
                    info_end = line_no
        if info_begin is None or info_end is None:
            EDVerbose.ERROR('could not find the completeness table')
            self.setFailure()
            return

        _extract_completeness_entries(lines[info_begin:info_end+1], output)


        # now for the last bit: check if we were given a path to the
        # gxparm file and if it exists get the space group and unit
        # cell constants from it
        if self.dataInput.gxparm is not None:
            gxparm_path = self.dataInput.gxparm.path.value
            if os.path.exists(gxparm_path):
                with open(gxparm_path, 'r') as f:
                    lines = f.readlines()
                for line in lines:
                    # the one we want has 7 floats
                    chunks = line.split()
                    if len(chunks) == 7:
                        output.sg_number = XSDataInteger(int(chunks[0]))
                        output.unit_cell_constants = [XSDataFloat(float(x)) for x in chunks[1:]]


        input_file = self.dataInput.correct_lp.path.value
        output.xds_run_directory = XSDataString(os.path.dirname(input_file))
        self.dataOutput = output

    def postProcess(self, _edObject = None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.postProcess")


def _extract_infos(lines, output):
    # extract values into the output obj modified in place
    # stuff we want:
    tmp_params = [
        'CRYSTAL MOSAICITY (DEGREES)',
        'DIRECT BEAM COORDINATES (REC. ANGSTROEM)',
        'DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM',
        'DETECTOR ORIGIN (PIXELS) AT',
        'CRYSTAL TO DETECTOR DISTANCE (mm)',
        'COORDINATES OF UNIT CELL A-AXIS',
        'COORDINATES OF UNIT CELL B-AXIS',
        'COORDINATES OF UNIT CELL C-AXIS',
        'UNIT_CELL_CONSTANTS=',
        ]

    params = [(item, len(item.split())) for item in tmp_params]

    parsed = dict()

    for line in lines:
        for param, param_len in params:
            if line.find(param) != -1:
                values = [float(x) for x in line.split()[param_len:]]
                parsed[param] = values

    # now fill in the data model with the values we got (and stop if
    # any of them is missing)
    try:
        output.crystal_mosaicity = XSDataFloat(parsed['CRYSTAL MOSAICITY (DEGREES)'][0])

        output.direct_beam_coordinates = XSDataVectorDouble()
        output.direct_beam_coordinates.v1 = parsed['DIRECT BEAM COORDINATES (REC. ANGSTROEM)'][0]
        output.direct_beam_coordinates.v2 = parsed['DIRECT BEAM COORDINATES (REC. ANGSTROEM)'][1]
        output.direct_beam_coordinates.v3 = parsed['DIRECT BEAM COORDINATES (REC. ANGSTROEM)'][2]

        output.direct_beam_detector_coordinates = XSData2DCoordinates()
        output.direct_beam_detector_coordinates.x = XSDataFloat(parsed['DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM'][0])
        output.direct_beam_detector_coordinates.y = XSDataFloat(parsed['DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM'][1])

        output.detector_origin = XSData2DCoordinates()
        output.detector_origin.x = XSDataFloat(parsed['DETECTOR ORIGIN (PIXELS) AT'][0])
        output.detector_origin.y = XSDataFloat(parsed['DETECTOR ORIGIN (PIXELS) AT'][1])

        output.crystal_to_detector_distance = XSDataFloat(parsed['CRYSTAL TO DETECTOR DISTANCE (mm)'][0])

        output.coordinates_of_unit_cell_a_axis = XSDataVectorDouble()
        output.coordinates_of_unit_cell_a_axis.v1 = parsed['COORDINATES OF UNIT CELL A-AXIS'][0]
        output.coordinates_of_unit_cell_a_axis.v2 = parsed['COORDINATES OF UNIT CELL A-AXIS'][1]
        output.coordinates_of_unit_cell_a_axis.v3 = parsed['COORDINATES OF UNIT CELL A-AXIS'][2]

        output.coordinates_of_unit_cell_b_axis = XSDataVectorDouble()
        output.coordinates_of_unit_cell_b_axis.v1 = parsed['COORDINATES OF UNIT CELL B-AXIS'][0]
        output.coordinates_of_unit_cell_b_axis.v2 = parsed['COORDINATES OF UNIT CELL B-AXIS'][1]
        output.coordinates_of_unit_cell_b_axis.v3 = parsed['COORDINATES OF UNIT CELL B-AXIS'][2]

        output.coordinates_of_unit_cell_c_axis = XSDataVectorDouble()
        output.coordinates_of_unit_cell_c_axis.v1 = parsed['COORDINATES OF UNIT CELL C-AXIS'][0]
        output.coordinates_of_unit_cell_c_axis.v2 = parsed['COORDINATES OF UNIT CELL C-AXIS'][1]
        output.coordinates_of_unit_cell_c_axis.v3 = parsed['COORDINATES OF UNIT CELL C-AXIS'][2]

        parsed['UNIT_CELL_CONSTANTS='] = [XSDataFloat(x) for x in parsed['UNIT_CELL_CONSTANTS='] ]

        # there may be trailing information after the 6 floats (the
        # string "as used by INTEGRATE")
        unit_cells = parsed['UNIT_CELL_CONSTANTS='][:6]
        output.cell_a, output.cell_b, output.cell_c, \
        output.cell_alpha, output.cell_beta, output.cell_gamma = unit_cells

    except KeyError, ke:
        EDVerbose.ERROR('Some parameters could not be found!')
        EDVerbose.DEBUG('Those found were: %s' % parsed)
        raise ValueError('Some parameters missing')

def _extract_completeness_entries(lines, output):
    for line in lines:
        if line.find('total') != -1:
            # special case for the last table line which contains the
            # totals
            infos = [float(x.replace('%', '').replace('*','')) for x in line.split()[1:]]
            output.total_completeness = XSDataXdsCompletenessEntry()
            output.total_completeness.outer_complete = XSDataFloat(infos[3])
            output.total_completeness.outer_rfactor = XSDataFloat(infos[4])
            output.total_completeness.outer_isig = XSDataFloat(infos[7])
            output.total_completeness.half_dataset_correlation = XSDataFloat(infos[10])
        else:
            # regular line, do not strip the first elem and bump the
            # indices by 1
            infos = [float(x.replace('%', '').replace('*','')) for x in line.split()]
            res = XSDataXdsCompletenessEntry()
            res.outer_res = XSDataFloat(infos[0])
            res.outer_complete = XSDataFloat(infos[4])
            res.outer_rfactor = XSDataFloat(infos[5])
            res.outer_isig = XSDataFloat(infos[8])
            res.half_dataset_correlation = XSDataFloat(infos[10])
            output.completeness_entries.append(res)
