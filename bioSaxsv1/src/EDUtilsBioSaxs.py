#
#coding: utf8
#
#    Project: BioSaxs : ID14-3
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
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
"""
Utilities for BioSaxs, especially for logging back both to EDNA using EDVerbose and to BioSaxsCube through SpecVariable
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import sys, os, time
from EDUtilsPlatform    import EDUtilsPlatform
from EDThreading import Semaphore
from EDUtilsPath        import EDUtilsPath
architecture = EDUtilsPlatform.architecture
specClientPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "SpecClient", architecture)
if  os.path.isdir(specClientPath) and (specClientPath not in sys.path):
    sys.path.insert(1, specClientPath)


from EDVerbose          import EDVerbose
#from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDObject           import EDObject
try:
    from SpecClient         import SpecVariable
except:
    SpecVariable = None
import h5py, numpy, matplotlib, json
matplotlib.use('Agg')
from matplotlib import pylab

class EDUtilsBioSaxs(EDObject):

    DETECTORS = ["pilatus", "vantec"]
    OPERATIONS = ["normalisation", "reprocess", "average", "complete"]
    TRANSLATION = {"beamStopDiode":"DiodeCurr",
                   "machineCurrent":"MachCurr",
                   "concentration":"Concentration",
                   "comments":"Comments",
                   "code":"Code",
                   "maskFile":"Mask",
                   "normalizationFactor":"Normalization",
                   "beamCenter_1":"Center_1",
                   "beamCenter_2":"Center_2",
                   "pixelSize_1":"PSize_1",
                   "pixelSize_2":"PSize_2",
                   "detectorDistance":"SampleDistance",
                   "wavelength":"WaveLength",
                   "detector":"Detector",
                   "storageTemperature":"storageTemperature",
                   "exposureTemperature":"exposureTemperature",
                   "exposureTime":"exposureTime",
                   "frameNumber":"frameNumber",
                   "frameMax":"frameMax",
                   "timeOfFrame":"time_of_day"
                   }
    FLOAT_KEYS = ["beamStopDiode", "machineCurrent", "concentration", "normalizationFactor",
                  "beamCenter_1", "beamCenter_2", "pixelSize_1", "pixelSize_2",
                  "detectorDistance", "wavelength", "timeOfFrame",
                  "storageTemperature", "exposureTemperature", "exposureTime"]
    INT_KEYS = [ "frameNumber", "frameMax"]


    __strSpecVersion = None
    __strSpecStatus = None
    __strSpecAbort = None
    __specVarStatus = None
    __specVarAbort = None

    @staticmethod
    def initSpec(_strSpecVersion, _strSpecStatus, _strSpecAbort):
        """
        Initialization of SpecVariable  ...
        """
        if EDUtilsBioSaxs.specVersion is None:
            EDUtilsBioSaxs.__strSpecVersion = _strSpecVersion
            EDUtilsBioSaxs.__strSpecStatus = _strSpecStatus
            EDUtilsBioSaxs.__strSpecAbort = _strSpecAbort
            if SpecVariable:
                EDUtilsBioSaxs.__specVarStatus = SpecVariable.SpecVariable(_strSpecStatus)
                EDUtilsBioSaxs.__specVarAbort = SpecVariable.SpecVariable(_strSpecAbort)
        else:
            EDVerbose.DEBUG("EDUtilsBioSaxs initSpec called whereas it was already set-up")
            if EDUtilsBioSaxs.__strSpecVersion != _strSpecVersion:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specVersion %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))
            if EDUtilsBioSaxs.__strSpecStatus != _strSpecStatus:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specStatus %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))
            if EDUtilsBioSaxs.__strSpecAbort != _strSpecAbort:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specAbort %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))

    @staticmethod
    def showMessage(_iLevel, _strMessage, _strFilename=None):
        """
        Class Method:
        Similar to logging module of python but for updating BioSaxsCube

        @param _iLevel: print level seems to be
                        4 for Errors
                        3 for Warnings
                        2 for Info
                        1
                        0
        @type _iLevel: int
        @param _strMessage: comment to be printed
        @type _strMessage: string
        @param _strFilename: the file related to the message (nothing to do with a logfile)
        @type _strFilename: string or None
        """

        if _iLevel == 4:
            EDVerbose.ERROR(_strMessage)
        elif _iLevel == 3:
            EDVerbose.WARNING(_strMessage)
        else:
            EDVerbose.screen(_strMessage)
#        else:
#            EDVerbose.DEBUG(_strMessage)


        if EDUtilsBioSaxs.specStatus is not None:
            currentStatus = EDUtilsBioSaxs.specStatus.value["reprocess"]["status"]     # must do this, since SpecClient is apparently returning a non-expected data structure
            i = currentStatus.rfind(",")
            # TB: This ,1 or ,0 suffix nonsense seems to be a hack to force Spec to signal a variable change to bsxcube
            if i == -1 or currentStatus[i + 1:] == "1":
                if _strFilename is None:
                    newStatus = "%s,%s,0" % (_iLevel, _strMessage)
                else:
                    newStatus = "%s,%s,%s,0" % (_iLevel, _strMessage, _strFilename)
            else:
                if _strFilename is None:
                    newStatus = "%s,%s,1" % (_iLevel, _strMessage)
                else:
                    newStatus = "%s,%s,%s,1" % (_iLevel, _strMessage, _strFilename)
            EDUtilsBioSaxs.specStatus.setValue(newStatus)

        if (EDUtilsBioSaxs.specAbort is not None) and (EDUtilsBioSaxs.specAbort.value["reprocess"]["abort"]) == "1":
            # must do this, since SpecClient is apparently returning a non-expected data structure
            EDVerbose.ERROR("Aborting data reprocess!")
#            sys.exit(0)


    @staticmethod
    def getFilenameDetails(_strFilename):
        """
        Split the name of the file in 4 components:
        prefix_run_frame_extra.extension
        @return: prefix, run, frame, extra, extension
        @rtype: 4-tuple of strings
        """
        _strFilename = str(_strFilename)
        filei, extension = os.path.splitext(_strFilename)

        items = filei.split("_")
        prefix = items[0]
        run = ""
        frame = ""
        extra = ""

        for oneItem in items[1:]:
            if oneItem.isdigit():
                if run == "":
                    run = oneItem
                elif frame == "":
                    frame = oneItem
                elif extra == "":
                    extra = oneItem
                else:
                    extra += "_" + oneItem
            else:
                if run == "":
                    prefix += "_" + oneItem
                else:
                    extra += "_" + oneItem

        try: #remove the "." at the begining of the extension
            extension = extension[1:]
        except IndexError:
            extension = ""


        try: #remove the "_" at the begining of the extra
            extra = extra[1:]
        except IndexError:
            extra = ""

        return prefix, run, frame, extra, extension


    @staticmethod
    def makeTranslation(pTranslate, pKeyword, pDefaultValue):
        """
        Static method

        ????


        @type pTranslate: list ??
        @param pKeyword: the given keyword to be replaced
        @param pDefaultValue: default value for the keyword
        """
        for keyword, value in pTranslate:
            if keyword == pKeyword:
                newValue = ""
                for i in range(0, len(value)):
                    if value[i] != "\"":
                        newValue += value[i]
                return newValue

        if len(pTranslate) > 0:
            EDUtilsBioSaxs.showMessage(3, "Trying to get value '%s' which doesn't exist!" % pKeyword)

        return pDefaultValue

class HPLCframe(object):
    def __init__(self, runID, frameId=None):
        self.runID = runID
        self.frameId = frameId
        self.curve = None
        self.subtracted = None
        self.processing = True
        self.time = None
        self.gnom = None
        self.Dmax = None
        self.total = None
        self.volume = None
        self.Rg = None
        self.Rg_Stdev = None
        self.I0 = None
        self.I0_Stdev = None
        self.quality = None

def median_filt(input_array, width=3):
    """
    Simple 1D median filter (with reflect mode)
    """
    b = numpy.zeros(input_array.size + width, dtype=input_array.dtype)
    b[:width // 2] = input_array[width // 2 - 1::-1]
    b[-width + width // 2:] = input_array[-1:-width + width // 2 - 1:-1]
    b[width // 2:-width + width // 2] = input_array
    c = numpy.outer(b, numpy.ones(width, dtype=input_array.dtype))
    c.strides = c.strides[0], c.strides[0]
    d = numpy.median(c, axis= -1)
    return d[:-width]


def label(a):
    "Simple labaling algo for non zero regions"
    last = 0
    cnt = 1
    out = numpy.zeros_like(a)
    for i in range(a.size):
        if a[i] == 0:
            if last != 0:
                cnt += 1
            last = 0
        else:
            out[i] = cnt
            last = cnt
    return out

class HPLCrun(object):
    def __init__(self, runId, first_curve=None):
        self.id = runId
        self.buffer = None
        self.first_curve = first_curve
        self.frames = {} #key: id, value: HPLCframe instance
        self.curves = []
        self.for_buffer = []
        self.hdf5_filename = None
        self.hdf5 = None
        self.chunk_size = 250
        self.lock = Semaphore()
        if first_curve:
            self.files.append(first_curve)
        self.max_size = None
        self.time = None
        self.gnom = None
        self.Dmax = None
        self.total = None
        self.volume = None
        self.Rg = None
        self.Rg_Stdev = None
        self.I0 = None
        self.I0_Stdev = None
        self.quality = None
        self.q = None
        self.size = None

    def reset(self):
        self.frames = []
        self.curves = []
        self.for_buffer = []

    def dump_json(self, filename=None):

        dico = {}
        dico["id"] = self.id
        dico["buffer"] = self.buffer
        dico["first_curve"] = self.first_curve
        dico["frames"] = {}
        dico["curves"] = self.curves
        dico["for_buffer"] = self.for_buffer
        dico["hdf5_filename"] = self.hdf5_filename
        dico["chunk_size"] = self.chunk_size

        for i in self.frames:
            dico["frames"][i] = self.frames[i].__dict__
        if not filename and self.hdf5_filename:
            filename = os.path.splitext(self.hdf5_filename)[0] + ".json"
        json.dump(dico, open(filename, "w"), indent=1)

    def load_json(self, filename=None):
        if not filename and self.hdf5_filename:
            filename = os.path.splitext(self.hdf5_filename)[0] + ".json"
        dico = json.load(open(filename, "r"))
        for i in dico:
            if i != "frames":
                self.__setattr__(i, dico[i])
        frames = dico["frames"]
        for i in frames:
            frame = HPLCframe(self.id)
            for k, v in frames[i].items():
                frame.__setattr__(k, v)
            self.frames[int(i)] = frame

    def init_hdf5(self, filename):
        if self.hdf5_filename is None:
            with self.lock:
                if self.hdf5_filename is None:
                    self.hdf5_filename = filename

    def calc_size(self, idx):
        return (1 + (idx // self.chunk_size)) * self.chunk_size

    def extract_data(self):
        self.max_size = self.calc_size(max(self.frames.keys()) + 1)
        self.time = numpy.zeros(self.max_size, dtype=numpy.float64)
        self.gnom = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.Dmax = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.total = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.volume = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.Rg = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.Rg_Stdev = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.I0 = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.I0_Stdev = numpy.zeros(self.max_size, dtype=numpy.float32)
        self.quality = numpy.zeros(self.max_size, dtype=numpy.float32)
        data = numpy.loadtxt(self.first_curve)
        self.q = data[:, 0]
        self.size = self.q.size
#        print self.size
        self.scattering_I = numpy.zeros((self.max_size, self.size), dtype=numpy.float32)
        self.scattering_Stdev = numpy.zeros((self.max_size, self.size), dtype=numpy.float32)
        self.subtracted_I = numpy.zeros((self.max_size, self.size), dtype=numpy.float32)
        self.subtracted_Stdev = numpy.zeros((self.max_size, self.size), dtype=numpy.float32)
        for i, frame in self.frames.items():
            while frame.processing:
                time.sleep(1)
            self.time[i] = frame.time or 0
            self.gnom[i] = frame.gnom or 0
            self.Dmax[i] = frame.Dmax or 0
            self.total[i] = frame.total or 0
            self.volume[i] = frame.volume or 0
            self.Rg[i] = frame.Rg or 0
            self.Rg_Stdev[i] = frame.Rg_Stdev or 0
            self.I0[i] = frame.I0 or 0
            self.I0_Stdev[i] = frame.I0_Stdev or 0
            self.quality[i] = frame.quality or 0
            if frame.curve and os.path.exists(frame.curve):
                data = numpy.loadtxt(frame.curve)
                self.scattering_I[i, :] = data[:, 1]
                self.scattering_Stdev[i, :] = data[:, 2]
            if frame.subtracted and os.path.exists(frame.subtracted):
                data = numpy.loadtxt(frame.subtracted)
                self.subtracted_I[i, :] = data[:, 1]
                self.subtracted_Stdev[i, :] = data[:, 2]
        t = self.time > 0
        x = numpy.arange(self.max_size)
        self.time = numpy.interp(x, x[t], self.time[t])
        self.time -= self.time.min()

    def save_hdf5(self):
        if not self.size:
            self.extract_data()
        with self.lock:
            if os.path.exists(self.hdf5_filename):
                os.unlink(self.hdf5_filename)
            self.hdf5 = h5py.File(self.hdf5_filename)
            self.hdf5.create_dataset("q", shape=(self.size,), dtype=numpy.float32, data=self.q)
            self.hdf5.create_dataset(name="time", shape=(self.max_size,), dtype=numpy.float32, data=self.time, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="gnom", shape=(self.max_size,), dtype=numpy.float32, data=self.gnom, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="Dmax", shape=(self.max_size,), dtype=numpy.float32, data=self.Dmax, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="total", shape=(self.max_size,), dtype=numpy.float32, data=self.total, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="volume", shape=(self.max_size,), dtype=numpy.float32, data=self.volume, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="Rg", shape=(self.max_size,), dtype=numpy.float32, data=self.Rg, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="Rg_Stdev", shape=(self.max_size,), dtype=numpy.float32, data=self.Rg_Stdev, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="I0", shape=(self.max_size,), dtype=numpy.float32, data=self.I0, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="I0_Stdev", shape=(self.max_size,), dtype=numpy.float32, data=self.I0_Stdev, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="quality", shape=(self.max_size,), dtype=numpy.float32, data=self.quality, chunks=(self.chunk_size,))
            self.hdf5.create_dataset(name="scattering_I", shape=(self.max_size, self.size), dtype=numpy.float32, data=self.scattering_I, chunks=(self.chunk_size, self.size))
            self.hdf5.create_dataset(name="scattering_Stdev", shape=(self.max_size, self.size), dtype=numpy.float32, data=self.scattering_Stdev, chunks=(self.chunk_size, self.size))
            self.hdf5.create_dataset(name="subtracted_I", shape=(self.max_size, self.size), dtype=numpy.float32, data=self.subtracted_I, chunks=(self.chunk_size, self.size))
            self.hdf5.create_dataset(name="subtracted_Stdev", shape=(self.max_size, self.size), dtype=numpy.float32, data=self.subtracted_Stdev, chunks=(self.chunk_size, self.size))
        return self.hdf5_filename

    def make_plot(self):
        fig = pylab.plt.figure()
        fig_size = fig.get_size_inches()
        fig.set_size_inches([fig_size[0], 2 * fig_size[1]])

        sp0 = fig.add_subplot(511)
        data = self.scattering_I.sum(axis= -1)
        sp0.plot(self.time, data)#, label="Total Scattering")
        sp0.set_ylabel("Scattering")
        sp0.set_ylim((data[data > 0]).min(), data.max())
        sp0.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        sp0.legend()

        sp1 = fig.add_subplot(512)
        sp1.errorbar(self.time, self.Rg, self.Rg_Stdev, label="Rg")
        sp1.plot(self.time, self.gnom, label="Gnom")
        sp1.plot(self.time, self.Dmax, label="Dmax")
        sp1.set_ylabel("Radius nm")
        sp1.set_ylim(0, median_filt(self.Dmax, 9).max())
        sp1.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        sp1.legend()

        sp2 = fig.add_subplot(513)
        sp2.errorbar(self.time, self.I0, self.I0_Stdev)#, label="I0")
        sp2.set_ylabel("I0")
        sp2.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        sp2.legend()

        sp3 = fig.add_subplot(514)
        sp3.plot(self.time, 100 * self.quality)#, label="Quality")
        sp3.set_ylabel("Qual. %")
        sp3.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        sp3.legend()

        sp4 = fig.add_subplot(515)
        sp4.plot(self.time, self.volume)#, label="Volume")
        sp4.set_ylabel("Vol. nm^3")
        sp4.set_xlabel("time (seconds)")
        sp4.set_ylim(0, median_filt(self.volume, 9).max())
        sp4.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        sp4.legend()
        pngFile = os.path.splitext(self.hdf5_filename)[0] + ".png"
        fig.savefig(pngFile)
        fig.savefig(os.path.splitext(self.hdf5_filename)[0] + ".svg", transparent=True, bbox_inches='tight', pad_inches=0)
        return pngFile

    def analyse(self):
        """
        Look for curves to merge...
        """
        lab = label(self.I0)
        res = []
        for i in range(1, int(lab.max() + 1)):
            loc = (lab == i)
            c = loc.sum()
            if c > 10:
                idx = numpy.where(loc)[0]
                start = idx[0]
                stop = idx[-1]
                maxi = self.I0[start: stop + 1].argmax() + start
                rg0 = self.Rg[maxi]
                sg0 = self.Rg_Stdev[maxi]
                good = (abs(self.Rg - rg0) < sg0) #keep curves with same Rg within +/- 1 stdev
                good[:start] = 0
                good[stop:] = 0
                lg = label(good[start:stop + 1])
                lv = lg[maxi - start]
                res.append(numpy.where(lg == lv)[0] + start)
        return res
