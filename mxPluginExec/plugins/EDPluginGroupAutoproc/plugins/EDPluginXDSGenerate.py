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


from EDPluginControl import EDPluginControl
from XSDataAutoProc import XSDataXdsGenerateInput
from XSDataAutoProc import XSDataResCutoff
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

        # Now really check what we need
        path = os.path.abspath(self.dataInput.previous_run_dir.value)
        if not os.path.isdir(path):
            EDVerbose.ERROR('path given is not a directory')
            self.setFailure(True)
            return

        files = ['XDS.INP', 'INTEGRATE.HKL', 'REMOVE.HKL',
                 'X-CORRECTIONS.cbf', 'Y-CORRECTIONS.cbf']

        # we'll use it in preprocess
        self._required = [os.path.join(path, f) for f in files]

        for f in self._required:
            if not os.path.isfile(f):
                EDVerbose.ERROR('missing required file {}'.format(f))
                self.setFailure(True)
                return


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoproc.preProcess")

        self.xds = self.loadPlugin('EDPluginExecMinimalXDS')

        xds_dir = os.path.abspath(self.xds.getWorkingDirectory())
        # let's make some links!
        for f in self._required:
            os.symlink(f, os.path.join(xds_dir, os.path.basename(f)))

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
                os.symlink(fullpath, f)

        # now that this ugly stuff is dealt with, ensure that JOB=
        # CORRECT in XDS.INP
        cfg_path = os.path.join(xds_dir, 'XDS.INP')
        config = parse_xds_file(cfg_path)
        if config['JOB='] != 'CORRECT':
            config['JOB'] = 'CORRECT'
            dump_xds_file(config, cfg_path)


    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoproc.process")

        self.xds.executeSynchronous()

    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

    def doSuccessExecTemplate(self,  _edPlugin = None):
        self.DEBUG("EDPluginControlAutoproc.doSuccessExecTemplate")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlAutoproc.doSuccessExecTemplate")

    def doFailureExecTemplate(self,  _edPlugin = None):
        self.DEBUG("EDPluginControlAutoproc.doFailureExecTemplate")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlAutoproc.doFailureExecTemplate")
