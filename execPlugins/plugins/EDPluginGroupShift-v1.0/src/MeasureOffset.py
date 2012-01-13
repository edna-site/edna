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
import os, threading, time
try:
    import fftw3
except ImportError:
    fftw3 = None
import numpy
sem = threading.Semaphore()

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


def shiftFFT(input, shift):
    """
    Do shift using FFTs
    Shift an array like  scipy.ndimage.interpolation.shift(input, shift, mode="wrap", order="infinity") but faster
    @param input: 2d numpy array
    @param shift: 2-tuple of float 
    @return: shifted image
    """
    d0, d1 = input.shape
    v0, v1 = shift
    m0, m1 = np.ogrid[:d0, :d1]
    e0 = np.exp(-2j * pi * v[0] * m0 / d0)
    e1 = np.exp(-2j * pi * v[1] * m1 / d1)
    e = e0 * e1
    return abs(np.fft.ifft2(np.fft.fft2(input) * e))


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




def measure_offset(img1, img2, method="fftw", withLog=False):
    """
    Measure the actual offset between 2 images
    @param img1: ndarray, first image 
    @param img2: ndarray, second image, same shape as img1
    @return: tuple of floats with the offsets
    """
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

    else:#use numpy fftpack
        i1f = numpy.fft.fft2(self.npaIm1)
        i2f = numpy.fft.fft2(self.npaIm2)
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
        return offset, logs
    else:
        return offset

