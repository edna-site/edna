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

import sys, logging, os
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
    def __init__(self, inputs, output, crop=False, check=False, normalize=False):
        """
        inputs and output are /path/to/file:internal
        """
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

    @classmethod
    def validateInputs(cls, inputs):
        """
        @return: dict with "path:h5" -> Group object 
        """
        res = {}
        for h in inputs:
            if ":" not in h:
                logger.warning("Input %s does not look like a HDF5 path" % h)
            else:
                filepath, h5path = h.split(":", 1)
                if os.path.isfile(filepath):
                    h5file = h5py.File(filepath)
                    if h5path in h5file:
                        if h5file[h5path].__class__.__name__ == "Group":
                            res[h] = h5file[h5path]
                        else:
                            res[h] = h5file[h5path].parent
                    else:
                        logger.warning("No such group %s in file: %s" % (h5path, filepath))
        return res

    def create_output(self):
        if ":" not in self.output:
            logger.warning("Input %s does not look like a HDF5 path" % h)
        else:
            filepath, h5path = self.output.split(":", 1)
            self.h5file = h5py.File(filepath)
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
        print self.crop_region
        dim1 = self.crop_region[0].stop - self.crop_region[0].start
        dim2 = self.crop_region[1].stop - self.crop_region[1].start
        if not self.ENERGY in self.h5grp:
            self.h5grp.create_dataset(self.ENERGY, (self.shape[0],), dtype="float32", data=self.get_energy())
        if not self.STACK in self.h5grp:
            self.h5grp.create_dataset(self.STACK, (self.shape[0], dim1, dim2),
                                       dtype="float32", chunks=(1, max(1, dim1 // 8), max(1, dim2 // 8)))
        ds = self.h5grp[self.STACK]
        sys.stdout.write("Averaging out frame ")
        for frn in xrange(self.shape[0]):
            sys.stdout.write("%04i" % frn)
            sys.stdout.flush()
            fr = numpy.zeros((dim1, dim2), "float64")
            i = 0
            for path, h5grp in self.inputs.items():
                if self.MAX_INT in h5grp:
                    norm_factor = h5grp[self.MAX_INT][frn]
                else:
                    norm_factor = 1.0
                if self.STACK in h5grp:
                    i += 1
                    idx = (frn,) + self.crop_region
                    fr += h5grp[self.STACK][idx] / norm_factor
                else:
                    logger.warning("no %s in %s ?????"(self.STACK, frn))
            if i == 0:
                logger.warning("Why is i=0?????")
                i = 1
            ds[frn, :, :] = fr / i

            sys.stdout.write("\b"*4)
            sys.stdout.flush()
        print("Finished !!!")



if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="h5path",
                      help="write result to HDF5 file with given path")
    parser.add_option("-c", "--crop", dest="crop",
                      help="Shall we crop the dataset to valid area", default=True)
    parser.add_option("-k", "--check", dest="recheck",
                      help="Shall we recheck the consistency of the various frames ... very time consuming !!! (not implemented", default=False)
    parser.add_option("-n", "--normalize", dest="normalize",
                      help="renormalize frames from intensity", default=True)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")


    (options, args) = parser.parse_args()
    print options
    print args
    mfx = MergeFFX(args, options.h5path, crop=options.crop, check=options.recheck, normalize=options.normalize)
    mfx.create_output()
    mfx.get_offsets()
    mfx.get_crop_region()
    mfx.merge_dataset()
