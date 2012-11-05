# coding: utf8
#
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
#
#    Principal author:       Jérôme Kieffer
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"
__date__ = "20120112"
__doc__ = "This is a python module to measure image offsets using pyfftw3 or fftpack"
import os, threading, time, gc
try:
    import fftw3
except ImportError:
    fftw3 = None
try:
    import pycuda
    import pycuda.autoinit
    import pycuda.elementwise
    import pycuda.gpuarray as gpuarray
    import scikits.cuda.fft as cu_fft
except ImportError:
    cu_fft = None

import numpy
from math import ceil, floor
sem = threading.Semaphore()
masks = {}
def shift(input, shift):
    """
    Shift an array like  scipy.ndimage.interpolation.shift(input, shift, mode="wrap", order=0) but faster
    @param input: 2d numpy array
    @param shift: 2-tuple of integers
    @return: shifted image
    """
    re = numpy.zeros_like(input)
    s0, s1 = input.shape
    d0 = shift[0] % s0
    d1 = shift[1] % s1
    r0 = (-d0) % s0
    r1 = (-d1) % s1
    re[d0:, d1:] = input[:r0, :r1]
    re[:d0, d1:] = input[r0:, :r1]
    re[d0:, :d1] = input[:r0, r1:]
    re[:d0, :d1] = input[r0:, r1:]
    return re

def shiftFFT(inp, shift, method="fftw"):
    """
    Do shift using FFTs
    Shift an array like  scipy.ndimage.interpolation.shift(input, shift, mode="wrap", order="infinity") but faster
    @param input: 2d numpy array
    @param shift: 2-tuple of float
    @return: shifted image

    """
    d0, d1 = inp.shape
    v0, v1 = shift
    f0 = numpy.fft.ifftshift(numpy.arange(-d0 // 2, d0 // 2))
    f1 = numpy.fft.ifftshift(numpy.arange(-d1 // 2, d1 // 2))
    m1, m0 = numpy.meshgrid(f1, f0)
    e0 = numpy.exp(-2j * numpy.pi * v0 * m0 / float(d0))
    e1 = numpy.exp(-2j * numpy.pi * v1 * m1 / float(d1))
    e = e0 * e1
    if method.startswith("fftw") and (fftw3 is not None):

        input = numpy.zeros((d0, d1), dtype=complex)
        output = numpy.zeros((d0, d1), dtype=complex)
        with sem:
                fft = fftw3.Plan(input, output, direction='forward', flags=['estimate'])
                ifft = fftw3.Plan(output, input, direction='backward', flags=['estimate'])
        input[:, :] = inp.astype(complex)
        fft()
        output *= e
        ifft()
        out = input / input.size
    else:
        out = numpy.fft.ifft2(numpy.fft.fft2(inp) * e)
    return abs(out)

def maximum_position(img):
    """
    Same as scipy.ndimage.measurements.maximum_position:
    Find the position of the maximum of the values of the array.

    @param img: 2-D image
    @return: 2-tuple of int with the position of the maximum
    """
    maxarg = numpy.argmax(img)
    s0, s1 = img.shape
    return (maxarg // s1, maxarg % s1)

def center_of_mass(img):
    """
    Calculate the center of mass of of the array.
    Like scipy.ndimage.measurements.center_of_mass
    @param img: 2-D array
    @return: 2-tuple of float with the center of mass
    """
    d0, d1 = img.shape
    a0, a1 = numpy.ogrid[:d0, :d1]
    img = img.astype("float64")
    img /= img.sum()
    return ((a0 * img).sum(), (a1 * img).sum())




class CudaCorrelate(object):
    plans = {}
    data1_gpus = {}
    data2_gpus = {}
    multconj = None
    ctx = None
#    pycuda.autoinit.context.pop()
#    ctx.pop()
    sem = threading.Semaphore()
    initsem = threading.Semaphore()

    def __init__(self, shape):
        self.shape = tuple(shape)

    def init(self):
        if self.ctx is None:
            with self.__class__.initsem:
                if self.ctx is None:
                    self.__class__.ctx = pycuda.autoinit.context
        if not self.shape in self.plans:
            with self.__class__.initsem:
                if not self.shape in self.plans:
                    self.ctx.push()
                    if not self.__class__.multconj:
                        self.__class__.multconj = pycuda.elementwise.ElementwiseKernel("pycuda::complex<double> *a, pycuda::complex<double> *b", "a[i]*=conj(b[i])")
                    if self.shape not in self.__class__.data1_gpus:
                        self.__class__.data1_gpus[self.shape] = gpuarray.empty(self.shape, numpy.complex128)
                    if self.shape not in self.__class__.data2_gpus:
                        self.__class__.data2_gpus[self.shape] = gpuarray.empty(self.shape, numpy.complex128)
                    if self.shape not in self.__class__.plans:
                        self.__class__.plans[self.shape] = cu_fft.Plan(self.shape, numpy.complex128, numpy.complex128)
                    self.ctx.synchronize()
                    self.ctx.pop()
    @classmethod
    def clean(cls):
        with initsem:
            with sem:
                if self.ctx:
                    cls.ctx.push()
                    for plan_name in list(cls.plans.keys()):
                        plan = cls.plans.pop(plan_name)
                        del plan
                    for plan_name in list(cls.data1_gpus.keys()):
                        data = cls.data1_gpus.pop(plan_name)
                        data.gpudata.free()
                        del data
                    for plan_name in cls.data2_gpus.copy():
                        data = cls.data2_gpus.pop(plan_name)
                        data.gpudata.free()
                        del data
                    cls.ctx.pop()
                    cls.ctx = None

    def correlate(self, data1, data2):
        self.init()
        with self.__class__.sem:
            self.ctx.push()
            plan = self.__class__.plans[self.shape]
            data1_gpu = self.__class__.data1_gpus[self.shape]
            data2_gpu = self.__class__.data2_gpus[self.shape]
            data1_gpu.set(data1.astype(numpy.complex128))
            cu_fft.fft(data1_gpu, data1_gpu, plan)
            data2_gpu.set(data2.astype(numpy.complex128))
            cu_fft.fft(data2_gpu, data2_gpu, plan)
    #            data1_gpu *= data2_gpu.conj()
            self.multconj(data1_gpu, data2_gpu)
            cu_fft.ifft(data1_gpu, data1_gpu, plan, True)
#            self.ctx.synchronize()
            res = data1_gpu.get().real
            self.ctx.pop()
        return res

def measure_offset(img1, img2, method="fftw", withLog=False, withCorr=False):
    """
    Measure the actual offset between 2 images
    @param img1: ndarray, first image
    @param img2: ndarray, second image, same shape as img1
    @param withLog: shall we return logs as well ? boolean
    @param _shared: DO NOT USE !!!
    @return: tuple of floats with the offsets
    """
    method = str(method)
    ################################################################################
    # Start convolutions
    ################################################################################
    shape = img1.shape
    logs = []
    assert img2.shape == shape
    t0 = time.time()
    if method[:4] == "fftw" and (fftw3 is not None):
        input = numpy.zeros(shape, dtype=complex)
        output = numpy.zeros(shape, dtype=complex)
        with sem:
                fft = fftw3.Plan(input, output, direction='forward', flags=['measure'])
                ifft = fftw3.Plan(output, input, direction='backward', flags=['measure'])
        input[:, :] = img2.astype(complex)
        fft()
        temp = output.conjugate()
        input[:, :] = img1.astype(complex)
        fft()
        output *= temp
        ifft()
        res = input.real / input.size
    if method[:4] == "cuda" and (cu_fft is not None):
        with sem:
            cuda_correlate = CudaCorrelate(shape)
            res = cuda_correlate.correlate(img1, img2)
    else:#use numpy fftpack
        i1f = numpy.fft.fft2(img1)
        i2f = numpy.fft.fft2(img2)
        res = numpy.fft.ifft2(i1f * i2f.conjugate()).real
    t1 = time.time()
    ################################################################################
    # END of convolutions
    ################################################################################
    offset1 = maximum_position(res)
    res = shift(res, (shape[0] // 2 , shape[1] // 2))
    mean = res.mean(dtype="float64")
    maxi = res.max()
    std = res.std(dtype="float64")
    SN = (maxi - mean) / std
    new = numpy.maximum(numpy.zeros(shape), res - numpy.ones(shape) * (mean + std * SN * 0.9))
    com2 = center_of_mass(new)
    logs.append("MeasureOffset: fine result of the centered image: %s %s " % com2)
    offset2 = ((com2[0] - shape[0] // 2) % shape[0] , (com2[1] - shape[1] // 2) % shape[1])
    delta0 = (offset2[0] - offset1[0]) % shape[0]
    delta1 = (offset2[1] - offset1[1]) % shape[1]
    if delta0 > shape[0] // 2:
        delta0 -= shape[0]
    if delta1 > shape[1] // 2:
        delta1 -= shape[1]
    if (abs(delta0) > 2) or (abs(delta1) > 2):
        logs.append("MeasureOffset: Raw offset is %s and refined is %s. Please investigate !" % (offset1, offset2))
    listOffset = list(offset2)
    if listOffset[0] > shape[0] // 2:
        listOffset[0] -= shape[0]
    if listOffset[1] > shape[1] // 2:
        listOffset[1] -= shape[1]
    offset = tuple(listOffset)
    t2 = time.time()
    logs.append("MeasureOffset: fine result: %s %s" % offset)
    logs.append("MeasureOffset: execution time: %.3fs with %.3fs for FFTs" % (t2 - t0, t1 - t0))
    if withLog:
        if withCorr:
            return offset, logs, new
        else:
            return offset, logs
    else:
        if withCorr:
            return offset, new
        else:
            return offset

def merge3(a, b, c, ROI=None):
    """
    @param: a, b, c: 3 2D-datasets
    @param ROI: tuple of slices, i.e. (slice(1,513),slice(700,700+512))
    """
    from scipy import ndimage
    out = numpy.zeros(a.shape, dtype="float32")
    out += a
    if ROI is not None:
        ac = a[ROI]
        bc = b[ROI]
        cc = c[ROI]
    else:
        ac = a
        bc = b
        cc = c
    shab = measure_offset(ac, bc)
    out += ndimage.shift(b, shab, order=1, cval=b.mean(dtype=float))
    shac = measure_offset(ac, cc)
    out += ndimage.shift(c, shac, order=1, cval=c.mean(dtype=float))
    print(shab, shac)
    return out / 3.0

def patch(*arrays):
    """
    Will try to merge n-ndarray's representing images.
    @param arrays: list of 2D images
    @return: one image (ndarray)
    """
    n = len(arrays)
    assert n > 0
    #ensure all arrays have the same size
    shape = arrays[0].shape
    for i in arrays:
        assert i.shape == shape
    deltas = numpy.zeros((n, 2))
    for i in range(1, n):
         deltas[i] = measure_offset(arrays[0], arrays[i])
    d0min = int(floor(deltas[:, 0].min()))
    d1min = int(floor(deltas[:, 1].min()))
    d0max = int(ceil(deltas[:, 0].max()))
    d1max = int(ceil(deltas[:, 1].max()))
    big_shape = (shape[0] + d0max - d0min, shape[1] + d1max - d1min)
    print shape, big_shape
    idx = numpy.zeros(big_shape, dtype=int)
    patched = numpy.zeros(big_shape, dtype="float64")
    print deltas
    for i in range(n):
        data = numpy.zeros(big_shape, dtype="float64")
        pos = data.copy()
        data[:shape[0], :shape[1]] = arrays[i]
        pos[:shape[0], :shape[1]] = 1.0
        patched += shiftFFT(data, deltas[i] - [d0min, d1min])
        idx += shiftFFT(pos, deltas[i] - [d0min, d1min]).round().astype(int)
    out = patched / idx.clip(1, n)
    out[idx == 0] = 0
    return out

def gaussian(M, std, sym=True):
    """Return a Gaussian window of length M with standard-deviation std.

    """
    if M < 1:
        return numpy.array([])
    if M == 1:
        return numpy.ones(1, 'd')
    odd = M % 2
    if not sym and not odd:
        M = M + 1
    n = numpy.arange(0, M) - (M - 1.0) / 2.0
    sig2 = 2 * std * std
    w = numpy.exp(-n ** 2 / sig2)
    if not sym and not odd:
        w = w[:-1]
    return w

def make_mask(shape, width):
    """
    Create a 2D mask with 1 in the center and fades-out to 0 on the border.
    """
    assert len(shape) == 2
    s0, s1 = shape
    try:
        if len(width) == 2:
            w0, w1 = width
        else:
            w0 = w1 = width
    except TypeError:
        w0 = w1 = width
    key = ((s0, s1), (w0, w1))
    if key not in masks:
        g0 = gaussian(s0, w0)
        g1 = gaussian(s1, w1)
        h0 = numpy.empty_like(g0)
        h1 = numpy.empty_like(g1)
        h0[:s0 // 2] = g0[s0 - s0 // 2:]
        h0[s0 // 2:] = g0[:s0 - s0 // 2]
        h1[:s1 // 2] = g1[s1 - s1 // 2:]
        h1[s1 // 2:] = g1[:s1 - s1 // 2]
        mask = numpy.outer(1 - h0, 1 - h1)
        masks[key] = mask
    return masks[key]
