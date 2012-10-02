#!/usr/bin/env python
#coding: utf8
#
#    Project: Full Field XRay Absorption Spectroscopy
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012, ESRF, Grenoble
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
__copyright__ = "2012, ESRF, Grenoble"
__contact__ = "jerome.kieffer@esrf.eu"
__date__ = "20120529"
__doc__ = """
Merge and Crop HDF5 stacks of FullField Xanes/Exafs data 
"""

import sys, logging, os, time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hdf5merge")
import numpy
import h5py

class MergeFFX(object):
    """
    Merge FullField Xanes/Exafs dataset     
    """
    OFFSETS = "Offsets"
    MAX_OFFSET = "MaxOffset"
    STACK = "data"
    ENERGY = "energy"
    MAX_INT = "maxInt"
    def __init__(self, inputs, output, crop=False, check=False, normalize=False, logarithm=False):
        """
        inputs and output are /path/to/file:internal
        """
        self._h5files = []
        self.inputs = self.validateInputs(inputs) #list of HDF5 groups
        if output is None:
            raise RuntimeError("Output cannot be None")
        self.output = output
        self.crop = bool(crop)
        self.check = bool(check)
        self.normalize = bool(normalize)
        self.h5file = None
        self.h5grp = None
        self.offsets_security = None
        self.offsets = {}
        self._shape = None
        self._crop_region = None
        self.ln = logarithm

#    @classmethod
    def validateInputs(self, inputs):
        """
        @return: dict with "path:h5" -> Group object 
        """
        res = {}
        for h in inputs:
            if ":" not in h:
                logger.error("Input %s does not look like a HDF5 path: /path/to/file.h5:Aligned" % h)
            else:
                filepath, h5path = h.split(":", 1)
                if os.path.isfile(filepath):
                    h5file = h5py.File(filepath)
                    self._h5files.append(h5file)
#                    cls.set_cache(h5file, policy=0.0)
                    if h5path in h5file:
                        if h5file[h5path].__class__.__name__ == "Group":
                            res[h] = h5file[h5path]
                        else:
                            res[h] = h5file[h5path].parent
                    else:
                        logger.warning("No such group %s in file: %s" % (h5path, filepath))
        return res

    @classmethod
    def set_cache(cls, f, size=None, policy=None):
        if hasattr(f.id, 'get_access_plist'):
            p = f.id.get_access_plist()
            # create a copy of the current settings
            cache_settings = list(p.get_cache())
            # multiply current cache by 10
            if not size:
                cache_settings[2] = int(10 * cache_settings[2])
            else:
                cache_settings[2] = int(size)
            # if we are not going to use the read or written chunks, set the 
            # preemption policy to 0
            if policy is not None:
                cache_settings[3] = float(policy)
            p.set_cache(*cache_settings)



    def create_output(self):
        if ":" not in self.output:
            logger.error("Input %s does not look like a HDF5 path: /path/to/file.h5:Aligned" % self.output)
        else:
            filepath, h5path = self.output.split(":", 1)
            self.h5file = h5py.File(filepath)
            self.set_cache(self.h5file, size=100e6, policy=0.0)
            if h5path in self.h5file:
                self.h5grp = self.h5file[h5path]
            else:
                self.h5grp = self.h5file.create_group(h5path)

    def get_offsets(self):
        if self.crop:
            for path, h5grp in self.inputs.items():
                if self.OFFSETS in h5grp:
                    offsets = h5grp[self.OFFSETS]
                    if (self.offsets_security is None) and (self.MAX_OFFSET in offsets.attrs):
                        self.offsets_security = offsets.attrs[self.MAX_OFFSET]
                    npa = offsets[:]
                    self.offsets[path] = npa
                    print path, npa.min(axis=0), npa.max(axis=0)

    def get_crop_region(self):
        if not self._crop_region:
            if self.crop:
                shape = numpy.array(self.shape[1:])
                secu = self.offsets_security
                start = numpy.ceil(numpy.array([npa.max(axis=0) for npa in self.offsets.values()]).max(axis=0) + secu).astype(int)
                stop = numpy.floor(numpy.array([npa.min(axis=0) for npa in self.offsets.values()]).min(axis=0) - secu + shape).astype(int)
                self._crop_region = (slice(start[0], stop[0]), slice(start[1], stop[1]))
                print start, stop
            else:
                self._crop_region = tuple([slice(i) for i in numpy.array(self.shape[1:])])
        return self._crop_region
    crop_region = property(get_crop_region)


    def get_shape(self):
        if self._shape is None :
            for path, h5grp in self.inputs.items():
                if self.STACK in h5grp:
                    self._shape = h5grp[self.STACK].shape
                    break
                else:
                     logger.warning("No dataset %s in %s" % (self.STACK, path))
        return self._shape
    shape = property(get_shape)

    def get_energy(self):
        for path, h5grp in self.inputs.items():
            if self.ENERGY in h5grp:
                return  h5grp[self.ENERGY][:]
            else:
                 logger.warning("No dataset %s in %s" % (self.ENERGY, path))


    def merge_dataset(self):
        print('Crop region: %s %s'% self.crop_region)
        dim1 = self.crop_region[0].stop - self.crop_region[0].start
        dim2 = self.crop_region[1].stop - self.crop_region[1].start
        if not self.ENERGY in self.h5grp:
            nrj = self.get_energy()
            self.h5grp.create_dataset(self.ENERGY, (nrj.size,), dtype="float32", data=nrj)
        if not self.STACK in self.h5grp:
            self.h5grp.create_dataset(self.STACK, (self.shape[0], dim1, dim2),
                                       dtype="float32", chunks=(1, max(1, dim1 // 8), max(1, dim2 // 8)))
        ds = self.h5grp[self.STACK]
        sys.stdout.write("Averaging out frame ")
        readt = []
        writet = []
        for frn in xrange(self.shape[0]):
            sys.stdout.write("%04i" % frn)
            fr = numpy.zeros((dim1, dim2), "float64")
            i = 0
            tr0 = time.time()
            for path, h5grp in self.inputs.items():
                if self.normalize and (self.MAX_INT in h5grp):
                    norm_factor = h5grp[self.MAX_INT][frn]
                else:
                    norm_factor = 1.0
                if self.STACK in h5grp:
                    idx = (frn,) + self.crop_region
                    cropped = h5grp[self.STACK][idx]
                    if abs(cropped).max() < 1e-10:
                        continue
                    i += 1
                    fr += h5grp[self.STACK][idx] / norm_factor
                else:
                    logger.warning("no %s in %s ?????"(self.STACK, frn))
            tr = time.time() - tr0
            sys.stdout.write("  r=%5.3fs" % tr)
            readt.append(tr)
            if i == 0:
                logger.warning("Why is i=0?????")
                i = 1
            tw0 = time.time()
            if self.ln:
                ds[frn] = -numpy.log(fr / i)
            else:
                ds[frn] = fr / i
            tw = time.time() - tw0
            sys.stdout.write("  w=%5.3fs" % tw)
            writet.append(tw)
            sys.stdout.flush()
            sys.stdout.write("\b"*24)

        print("Finished !!!")
        return readt, writet



if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="h5path",
                      help="write result to HDF5 file with given path: path/to/file.h5:Aligned")
    parser.add_option("-c", "--crop", dest="crop",
                      help="Shall we crop the dataset to valid area", default=True)
    parser.add_option("-k", "--check", dest="recheck",
                      help="Shall we recheck the consistency of the various frames ... very time consuming !!! (not implemented", default=False)
    parser.add_option("-n", "--normalize", dest="normalize",
                      help="renormalize frames from intensity", default=True)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")
    parser.add_option("-l", "--ln",
                      dest="ln", default=False,
                      help="write data as -logarithm of merged input")



    (options, args) = parser.parse_args()
    print("")
    print("Options:")
    print('========')
    for k,v in options.__dict__.items():
        print("    %s: %s"%(k,v))
    print("")
    print("Input files and HDF5 path:")
    print("==========================")
    for f in list(args): 
        print("    %s"%f)
    print(" ")
    mfx = MergeFFX(args, options.h5path, crop=options.crop, check=options.recheck, normalize=options.normalize, logarithm=options.ln)
    mfx.create_output()
    mfx.get_offsets()
    mfx.get_crop_region()
    r, w = mfx.merge_dataset()
    from pylab import *
    plot(r, 'b')
    plot(w, 'r')
    show()
