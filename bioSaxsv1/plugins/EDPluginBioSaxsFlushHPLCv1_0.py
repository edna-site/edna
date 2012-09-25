# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 ESRF
#
#    Principal author:        Jérôme Kieffer
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
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2012 ESRF"
__date__ = "20120918"
__status__ = "development"

import os, time
from EDPluginControl import EDPluginControl
from EDThreading import Semaphore
from EDUtilsParallel import EDUtilsParallel
from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("XSDataBioSaxsv1_0")
edFactoryPlugin.loadModule("XSDataEdnaSaxs")

from XSDataBioSaxsv1_0 import XSDataInputBioSaxsHPLCv1_0, XSDataResultBioSaxsHPLCv1_0, \
                            XSDataInputBioSaxsProcessOneFilev1_0
from XSDataEdnaSaxs import XSDataInputDatcmp, XSDataInputDataver, XSDataInputDatop, XSDataInputSaxsAnalysis
from XSDataCommon import XSDataFile, XSDataStatus, XSDataString, XSDataInteger, XSDataStatus
from EDPluginBioSaxsHPLCv1_0 import EDPluginBioSaxsHPLCv1_0
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab

class EDPluginBioSaxsFlushHPLCv1_0 (EDPluginControl):
    """
    plugin that just flushes the HPLC data to disk 
    """

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsHPLCv1_0)
        self.__edPluginProcessOneFile = None
        self.__edPluginSubtract = None
        self.__edPluginSaxsAnalysis = None
        self.__edPluginDatCmp = None
        self.xsDataResult = XSDataResultBioSaxsHPLCv1_0()
        self.runId = None
        self.FrameId = None
        self.hplc_run = None
        self.curve = None
        self.subtracted = None
        self.lstExecutiveSummary = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.preProcess")
        sdi = self.dataInput
        if sdi.runId is not None:
            self.runId = sdi.runId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                self.runId = path[::-1].split("_", 1)[1][::-1]
            else:
                self.runId = path

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.process")
        while EDUtilsParallel.getNbRunning() != 0:
            self.DEBUG("Waiting for all process to finish...%i remaining" % EDUtilsParallel.getNbRunning())
            time.sleep(1)
        with EDPluginBioSaxsHPLCv1_0._sem:
            if self.runId in EDPluginBioSaxsHPLCv1_0.dictHPLC:
                self.processRun(EDPluginBioSaxsHPLCv1_0.dictHPLC[self.runId])

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsFlushHPLCv1_0.postProcess")

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        executiveSummary = os.linesep.join(self.lstExecutiveSummary)
        self.xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        self.dataOutput = self.xsDataResult

    def processRun(self, run):
        run.dump_json()
        run.save_hdf5()
        fig = pylab.plt.figure()
        sp0 = fig.add_subplot(511)
        sp1 = fig.add_subplot(512)
        sp2 = fig.add_subplot(513)
        sp3 = fig.add_subplot(514)
        sp4 = fig.add_subplot(515)
        sp0.plot(run.hdf5["time"][:], run.hdf5["scattering_I"][:].sum(axis= -1), label="Total Scattering")
        sp1.errorbar(run.hdf5["time"][:], run.hdf5["Rg"][:], run.hdf5["Rg_Stdev"][:], label="Guinier_Rg")
        sp1.plot(run.hdf5["time"][:], run.hdf5["gnom"][:], label="Gnom_Rg")
        sp1.plot(run.hdf5["time"][:], run.hdf5["Dmax"][:], label="Gnom_Dmax")
        sp1.set_ylabel("Radius/Distance (nm)")
        sp2.errorbar(run.hdf5["time"][:], run.hdf5["I0"][:], run.hdf5["I0_Stdev"][:], label="I0")
        sp2.set_ylabel("Intensity")
        sp3.plot(run.hdf5["time"][:], 100 * run.hdf5["quality"][:], label="Quality")
        sp3.set_ylabel("%%")
        sp4.plot(run.hdf5["time"][:], 100 * run.hdf5["volume"][:], label="Volume")
        sp4.set_ylabel("nm³")
        sp4.set_xlabel("time (sec)")
        sp0.legend()
        sp1.legend()
        sp2.legend()
        sp3.legend()
        sp4.legend()
        fig.savefig(os.path.splitext(run.hdf5_filename)[0] + ".png")
