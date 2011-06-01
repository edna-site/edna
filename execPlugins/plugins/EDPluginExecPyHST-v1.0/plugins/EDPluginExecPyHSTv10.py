#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Alessandro Mirone
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

__author__ = "Alessandro Mirone"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from PyHST import PyHST

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec

from XSDataExecPyHST import XSDataInputPyHSTv10
from XSDataExecPyHST import XSDataResultPyHSTv10

class EDPluginExecPyHSTv10(EDPluginExec):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputPyHSTv10)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecPyHSTv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecPyHSTv10.postProcess")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecPyHSTv10.process")
        xsDataInputPyHST = self.getDataInput()
        pyhst = PyHST_c.PyHST(xsDataInputPyHST.getOutputFileName(),
                  Parameters.OVERSAMPLING_FACTOR,
                  Parameters.START_VOXEL_1 - 1 + 1,
                  Parameters.START_VOXEL_2 - 1 + 1,
                  Parameters.END_VOXEL_1 - Parameters.START_VOXEL_1 + 1,
                  Parameters.END_VOXEL_2 - Parameters.START_VOXEL_2 + 1,
                  Parameters.ROTATION_AXIS_POSITION,
                  Parameters.ANGLE_OFFSET * DEG2RAD,
                  Parameters.ANGLE_BETWEEN_PROJECTIONS * DEG2RAD,
                  Parameters.NO_SINOGRAM_FILTERING,
                  dim_1,
                  num_projections,
                  BIG_SINOS ,
                      axis_corrections ,
                      Parameters.BICUBIC,
                      Parameters.SUMRULE ,
                      (angles),
                              Parameters.PENTEZONE,
                      Parameters.ZEROOFFMASK,
                             Parameters.CUMSUM_INTEGRAL
                      )



    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecPyHSTv10.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPyHSTv10()
        self.setDataOutput(xsDataResult)

