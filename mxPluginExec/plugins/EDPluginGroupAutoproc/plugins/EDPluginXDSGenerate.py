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


from shutil import copyfile
import os.path

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataString, XSDataFloat, XSDataBoolean

from XSDataAutoproc import XSDataMinimalXdsIn
from XSDataAutoproc import XSDataXdsGenerateInput
from XSDataAutoproc import XSDataXdsGenerateOutput
from xdscfgparser import parse_xds_file, dump_xds_file

class EDPluginXDSGenerate(EDPluginControl):
    """
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataXdsGenerateInput)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoproc.checkParameters")
        self.checkMandatoryParameters(self.dataInput.previous_run_dir,
                                      "previous run directory not specified")
        self.checkMandatoryParameters(self.dataInput.resolution,
                                      "resolution not specified")
        # Now really check what we need
        path = os.path.abspath(self.dataInput.previous_run_dir.value)
        if not os.path.isdir(path):
            EDVerbose.ERROR('path given is not a directory')
            self.setFailure()
            return

        # we do not generate a REMOVE.HKL file for now
        to_link = ['INTEGRATE.HKL', #'REMOVE.HKL',
                   'X-CORRECTIONS.cbf', 'Y-CORRECTIONS.cbf']

        # we require it but the run xds plugin copies it to its WD so
        # no need to link it
        required = to_link + ['XDS.INP']

        # we'll use it in preprocess
        self._required = [os.path.join(path, f) for f in required]
        self._to_link =  [os.path.join(path, f) for f in to_link]

        for f in self._required:
            if not os.path.isfile(f):
                EDVerbose.ERROR('missing required file {}'.format(f))
                self.setFailure()
                return


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoproc.preProcess")

        self.xds_anom = self.loadPlugin('EDPluginExecMinimalXds')
        self.xds_noanom = self.loadPlugin('EDPluginExecMinimalXds')

        path = os.path.abspath(self.dataInput.previous_run_dir.value)

        # create the data inputs now we know the files are here
        input_anom = XSDataMinimalXdsIn()
        input_anom.input_file = XSDataString(os.path.join(path, 'XDS.INP'))
        input_anom.friedels_law = XSDataBoolean(True)
        input_anom.job = XSDataString('CORRECT')
        input_anom.resolution = self.dataInput.resolution
        input_anom.resolution_range = [XSDataFloat(60), self.dataInput.resolution]
        self.xds_anom.dataInput = input_anom

        input_noanom = XSDataMinimalXdsIn()
        input_noanom.input_file = XSDataString(os.path.join(path, 'XDS.INP'))
        input_noanom.fridels_law = XSDataBoolean(False)
        input_noanom.job = XSDataString('CORRECT')
        input_noanom.resolution_range = [XSDataFloat(60), self.dataInput.resolution]
        self.xds_noanom.dataInput = input_noanom

        xds_anom_dir = os.path.abspath(self.xds_anom.getWorkingDirectory())
        xds_noanom_dir = os.path.abspath(self.xds_noanom.getWorkingDirectory())
        # let's make some links!
        for f in self._to_link:
            os.symlink(f, os.path.join(xds_anom_dir, os.path.basename(f)))
            os.symlink(f, os.path.join(xds_noanom_dir, os.path.basename(f)))
        # now this is the horrible part, we need to make symlinks to
        # the images also. for now we rely on the fact that the links
        # in the previous run are most likely the links to the
        # images. So we will make the same links and rely on the fact
        # that in the input file the path to the images is already
        # relative to the CWD
        path = os.path.abspath(self.dataInput.previous_run_dir.value)
        for f in os.listdir(path):
            fullpath = os.path.join(path, f)
            if os.path.islink(fullpath):
                # symlink the symlink...
                os.symlink(fullpath, os.path.join(xds_anom_dir, f))
                os.symlink(fullpath, os.path.join(xds_noanom_dir, f))


    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoproc.process")

        EDVerbose.DEBUG('first run w/ anom')

        self.xds_anom.executeSynchronous()
        if self.xds_anom.isFailure():
            EDVerbose.ERROR('xds failed when generating w/ anom')
            self.setFailure()
            return

        #Now backup the file
        mydir = os.path.abspath(self.getWorkingDirectory())
        xds_run_directory= self.xds_anom.getWorkingDirectory()
        xds_output = os.path.join(xds_run_directory, 'XDS_ASCII.HKL')
        output_anom = os.path.join(mydir, 'XDS_ANOM.HKL')
        copyfile(xds_output, output_anom)

        # since the original get_xds_stats uses the CORRECT.LP file we
        # need to backup it as well
        correct_lp = os.path.join(xds_run_directory, 'CORRECT.LP')
        correct_lp_anom = os.path.join(mydir, 'CORRECT_ANOM.LP')
        copyfile(correct_lp, correct_lp_anom)

        # now the second run, generate w/out anom
        EDVerbose.DEBUG('second run w/out anom')

        self.xds_noanom.executeSynchronous()

        if self.xds_noanom.isFailure():
            EDVerbose.ERROR('xds failed when generating w/out anom')
            self.setFailure()
            return

        #Now backup the file
        xds_run_directory= self.xds_anom.getWorkingDirectory()
        xds_output = os.path.join(xds_run_directory, 'XDS_ASCII.HKL')
        output_noanom = os.path.join(mydir, 'XDS_NOANOM.HKL')
        copyfile(xds_output, output_noanom)

        # since the original get_xds_stats uses the CORRECT.LP file we
        # need to backup it as well
        correct_lp = os.path.join(xds_run_directory, 'CORRECT.LP')
        correct_lp_noanom = os.path.join(mydir, 'CORRECT_NOANOM.LP')
        copyfile(correct_lp, correct_lp_noanom)

        # everything went fine
        data_output = XSDataXdsGenerateOutput()
        data_output.hkl_anom = XSDataString(output_anom)
        data_output.hkl_no_anom = XSDataString(output_noanom)
        data_output.correct_lp_no_anom = XSDataString(correct_lp_noanom)
        data_output.correct_lp_anom = XSDataString(correct_lp_anom)
        self.dataOutput = data_output

    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

#    def doSuccessExecTemplate(self,  _edPlugin = None):
#        self.DEBUG("EDPluginControlAutoproc.doSuccessExecTemplate")
#        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAutoproc.doSuccessExecTemplate")
#
#    def doFailureExecTemplate(self,  _edPlugin = None):
#        self.DEBUG("EDPluginControlAutoproc.doFailureExecTemplate")
#        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAutoproc.doFailureExecTemplate")
