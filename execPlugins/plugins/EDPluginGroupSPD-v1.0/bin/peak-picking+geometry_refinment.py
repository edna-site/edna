#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: Azimuthal integration 
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "18/05/2011"

import os, sys, gc
import numpy
from numpy import sin, cos, arccos, sqrt, floor, ceil, radians, degrees
import fabio
import matplotlib
import pylab
from scipy.optimize import fmin, leastsq, fmin_slsqp, anneal
from scipy.interpolate import interp2d
pi = numpy.pi
#xsDataName = "XSDataSPDv1_0"
#
#if "EDNA_HOME" not in os.environ:
#    full_path = os.path.abspath(sys.argv[0])
#    while True:
#        old_path = full_path
#        full_path = os.path.dirname(old_path)
#        if old_path == full_path:
#            print("Something weird is happening: I did not find the EDNA_ROOT !!!")
#            sys.exit(1)
#        if  os.path.isdir(os.path.join(full_path, "kernel", "datamodel")):
#            EDNA_HOME = full_path
#            os.environ["EDNA_HOME"] = full_path
#            break
#else:
#    EDNA_HOME = os.environ["EDNA_HOME"]

#sys.path.append(os.path.join(EDNA_HOME, "kernel", "src"))
#from EDFactoryPluginStatic import EDFactoryPluginStatic
#EDFactoryPluginStatic.loadModule(xsDataName)

class PeakPicker(object):
    def __init__(self, strFilename):
        """
        @param: input image filename
        """
        self.strFilename = strFilename
        self.data = fabio.open(strFilename).data.astype("float32")
        self.shape = self.data.shape
        self.points = []
        self.lXsd = []
        self.fig = None

        self.ax = None
        self.ct = None

    def gui(self, log=False):
        """
        @param log: show z in log scale
        """
        if self.fig is None:
            self.fig = pylab.plt.figure()
        self.ax = self.fig.add_subplot(111);
        if log:
            self.ax.imshow(numpy.log(self.data));
        else:
            self.ax.imshow(self.data);
        self.fig.show()
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def f(self, x):
        x0 = max(0, int(floor(x[0])))
        x1 = min(self.data.shape[0] - 1, int(ceil(x[0])))
        y0 = max(0, int(floor(x[1])))
        y1 = min(self.data.shape[0] - 1, int(ceil(x[1])))
        if x0 == x1:x1 = x0 + 1
        if y0 == y1:y1 = y0 + 1
        try:
            z = [-self.data[x0, y0], -self.data[x0, y1], -self.data[x1, y0], -self.data[x1, y1]]
        except:
            res = -self.data.min()
        else:
            function = interp2d(x=[x0, x0, x1, x1],
                                  y=[y0, y1, y0, y1],
                                  z=z)
            res = float(function(x[0], x[1]))
        return res

    def onclick(self, event):
        if event.button == 3: #right click
            x0 = event.xdata
            y0 = event.ydata
            [yopt, xopt] = fmin(self.f, (y0, x0))
            self.ax.annotate(str(len(self.points)), xy=(xopt, yopt), xytext=(x0, y0), color="white",
                arrowprops=dict(facecolor='white', edgecolor='white'),)
            self.points.append([yopt, xopt])
            self.fig.show()
            sys.stdout.flush()

    def finish(self):
        """
        Ask the 2theta values for the given points
        """
        print("Please use the GUI and Right-click on the peaks to mark them")

        c = raw_input("Please press enter when you are happy; to fill in 2theta values")
        self.lXsd = []
        last2Theta = None
        for idx, point in enumerate(self.points):
            bOk = False
            while not bOk:
                res = raw_input("Point #%i (%.1f,%.1f) [default=%s] 2Theta= " % (idx, point[1], point[0], last2Theta)).strip()
                if res == "":
                    res = last2Theta
                try:
                    tth = float(res)
                except (ValueError, TypeError):
                    print("I did not understand your 2theta value")
                else:
                    if tth > 0:
                        last2Theta = tth
                        self.lXsd.append([int(round(point[0])), int(round(point[1])), radians(tth)])
#                        self.lXsd.append(XSDataPeakPosition(
#                                        positon1=XSDataDouble(point[0]),
#                                        positon2=XSDataDouble(point[1]),
#                                        twoTheta=XSDataDouble(tth)
#                                        ))
                        bOk = True
        return self.lXsd

    def contour(self, data):
        if self.fig is None:
            print("No diffraction image available => not showing the contour")
        else:
            self.ct = self.fig.add_subplot(111);
            try:
                self.ct.contour(data)
            except MemoryError:
                print("Sorry but your computer does NOT have enough memory to display the 2-theta contour plot")
            self.fig.show()

    def closeGUI(self):
        if self.fig is not None:
            self.fig.clear()
            self.fig = None
            gc.collect()

class Refinement(object):
    def __init__(self, data, dist=1, poni1=0, poni2=0, rot1=0, rot2=0, rot3=0, pixel1=1, pixel2=1):
        self.data = numpy.array(data, dtype="float64")
        self.dist = dist
        self.dist_min = 0
        self.dist_max = 10
        self.poni1 = poni1
        self.poni1_min = -10000 * pixel1
        self.poni1_max = 15000 * pixel1
        self.poni2 = poni2
        self.poni2_min = -10000 * pixel2
        self.poni2_max = 15000 * pixel2
        self.rot1 = rot1
        self.rot1_min = -pi
        self.rot1_max = pi
        self.rot2 = rot2
        self.rot2_min = -pi
        self.rot2_max = pi
        self.rot3 = rot3
        self.rot3_min = -pi
        self.rot3_max = pi
        self.pixel1 = pixel1
        self.pixel2 = pixel2
        self.param = [self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3]
        self._ttha = None
        self._dssa = None
        self._nbPixCache = {} #key=shape, value: array

    def __repr__(self):
        self.param = [self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3]
        return "SampleDetDist= %.6fm\tPONI= %.6f, %.6fm\trot1=%.6f  rot2= %.6f  rot3= %.6f\t" % tuple(self.param)

    def tth(self, d1, d2, param=None):
        if param == None:
            param = self.param
#        tmp = arccos((param[0] * cos(param[3]) * cos(param[4]) - ((self.pixel2 * d2) - param[2]) * cos(param[4]) * sin(param[3]) + ((self.pixel1 * d1) - param[1]) * sin(param[4])) / (sqrt(abs(-param[0] * cos(param[3]) * cos(param[4]) + ((self.pixel2 * d2) - param[2]) * cos(param[4]) * sin(param[3]) - ((self.pixel1 * d1) - param[1]) * sin(param[4])) ** 2 + abs(((self.pixel1 * d1) - param[1]) * cos(param[4]) * cos(param[5]) + ((self.pixel2 * d2) - param[2]) * (cos(param[5]) * sin(param[3]) * sin(param[4]) - cos(param[3]) * sin(param[5])) - param[0] * (cos(param[3]) * cos(param[5]) * sin(param[4]) + sin(param[3]) * sin(param[5]))) ** 2 + abs(((self.pixel1 * d1) - param[1]) * cos(param[4]) * sin(param[5]) - param[0] * (-cos(param[5]) * sin(param[3]) + cos(param[3]) * sin(param[4]) * sin(param[5])) + ((self.pixel2 * d2) - param[2]) * (cos(param[3]) * cos(param[5]) + sin(param[3]) * sin(param[4]) * sin(param[5]))) ** 2)))
        cosRot1 = cos(param[3])
        cosRot2 = cos(param[4])
        cosRot3 = cos(param[5])
        sinRot1 = sin(param[3])
        sinRot2 = sin(param[4])
        sinRot3 = sin(param[5])
        p1 = (self.pixel1 * (d1 + 0.5)) - param[1]
        p2 = (self.pixel2 * (d2 + 0.5)) - param[2]
        tmp = arccos((param[0] * cosRot1 * cosRot2 - p2 * cosRot2 * sinRot1 + p1 * sinRot2) / (sqrt((-param[0] * cosRot1 * cosRot2 + p2 * cosRot2 * sinRot1 - p1 * sinRot2) ** 2 + (p1 * cosRot2 * cosRot3 + p2 * (cosRot3 * sinRot1 * sinRot2 - cosRot1 * sinRot3) - param[0] * (cosRot1 * cosRot3 * sinRot2 + sinRot1 * sinRot3)) ** 2 + (p1 * cosRot2 * sinRot3 - param[0] * (-cosRot3 * sinRot1 + cosRot1 * sinRot2 * sinRot3) + p2 * (cosRot1 * cosRot3 + sinRot1 * sinRot2 * sinRot3)) ** 2)))
#        if isinstance(tmp1, float):
#            print tmp1 - tmp2
#        else:
#            print abs(tmp1 - tmp2).max()
        return tmp

    def residu1(self, param, d1, d2, tth):
        return self.tth(d1, d2, param) - tth

    def residu2(self, param, d1, d2, tth):
        return (self.residu1(param, d1, d2, tth) ** 2).sum()

    def refine1(self):
        self.param = [self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3]
        newParam, rc = leastsq(self.residu1, self.param, args=(self.data[:, 0], self.data[:, 1], radians(self.data[:, 2])))
        print "Least square", rc, self.chi2(), "--> ", self.chi2(newParam)
        if self.chi2(tuple(newParam)) < self.chi2(tuple(self.param)):
            self.param = newParam
            self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3 = tuple(newParam)

    def refine2(self, maxiter=1000000):
        self.param = [self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3]
        newParam = fmin_slsqp(self.residu2, self.param, iter=maxiter, args=(self.data[:, 0], self.data[:, 1], self.data[:, 2]),
                              bounds=[(self.dist_min, self.dist_max),
                                      (self.poni1_min, self.poni1_max),
                                      (self.poni2_min, self.poni2_max),
                                      (self.rot1_min, self.rot1_max),
                                      (self.rot2_min, self.rot2_max),
                                      (self.rot3_min, self.rot3_max)],
                              acc=1.0e-12)
        print "Constrained Lest square", self.chi2(), "--> ", self.chi2(newParam)
        if self.chi2(newParam) < self.chi2():
            self.param = newParam
            self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3 = tuple(newParam)

    def anneal(self, maxiter=1000000):
        self.param = [self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3]
        result = anneal(self.residu2, self.param, args=(self.data[:, 0], self.data[:, 1], self.data[:, 2]),
                        lower=[self.dist_min, self.poni1_min, self.poni2_min, self.rot1_min , self.rot2_min, self.rot3_min],
                        upper=[self.dist_max, self.poni1_max, self.poni2_max, self.rot1_max , self.rot2_max, self.rot3_max],
                        maxiter=maxiter)
        newParam = result[0]
        print "Anneal", self.chi2(), "--> ", self.chi2(newParam)
        if self.chi2(tuple(newParam)) < self.chi2(tuple(self.param)):
            self.param = newParam
            self.dist, self.poni1, self.poni2, self.rot1, self.rot2, self.rot3 = tuple(newParam)

    def chi2(self, param=None):
        if param == None:
            param = self.param
        return  self.residu2(param, self.data[:, 0], self.data[:, 1], self.data[:, 2])


    def twoThetaArray(self, shape):
        """
        Generate an array of the given shape with two-theta(i,j) for all elements.  
        """
        if self._ttha is None:
            self._ttha = numpy.fromfunction(self.tth, shape, dtype="float32")
        return self._ttha

    def diffSolidAngle(self, d1, d2):
        p1 = (0.5 + d1) * self.pixel1 - self.poni1
        p2 = (0.5 + d2) * self.pixel2 - self.poni2
        dsa = self.pixel1 * self.pixel2 / sqrt(self.dist ** 2 + p1 ** 2 + p2 ** 2)
        return dsa

    def solidAngleArray(self, shape):
        """
        Generate an array of the given shape with the solid angle of the current element two-theta(i,j) for all elements.  
        """
        if self._dssa is None:
            self._dssa = numpy.fromfunction(self.diffSolidAngle, shape, dtype="float32")
        return self._dssa

    def xrpd(self, data, nbPt, filename=None):
        """
        Calculate the powder diffraction pattern from a set of data, an image
        @param data: 2D array from the CCD camera
        @type data: ndarray
        @param nbPt: number of points in the output pattern
        @type nbPt: integer
        @param filename: file to save data in
        @type filename: string
        """
        tth = self.twoThetaArray(data.shape)
        if nbPt in self._nbPixCache:
            ref = self._nbPixCache[nbPt]
        else:
            ref, b = numpy.histogram(tth, nbPt)
            self._nbPixCache[nbPt] = ref
        val, b = numpy.histogram(tth, nbPt, weights=data / self.solidAngleArray(data.shape))
        tthAxis = degrees(b[1:] + b[:-1]) / 2.0
        I = val / ref
        if filename:
            open(filename, "w").writelines(["%s\t%s%s" % (t, i, os.linesep) for t, i in zip(tthAxis, I)])
        return tthAxis, I

    def rotArray(self):
        raise NotImplementedError("TODO")

    def save(self, filename):
        """
        Save the refined parameters.
        @param filename: name of the file where to save the parameters
        @type filename: string
        """
        f = open(filename, "w")
        f.write("PixelSize1: %s%s" % (self.pixel1, os.linesep))
        f.write("PixelSize2: %s%s" % (self.pixel2, os.linesep))
        f.write("Distance: %s%s" % (self.dist, os.linesep))
        f.write("Poni1: %s%s" % (self.poni1, os.linesep))
        f.write("Poni2: %s%s" % (self.poni2, os.linesep))
        f.write("Rot1: %s%s" % (self.rot1, os.linesep))
        f.write("Rot2: %s%s" % (self.rot2, os.linesep))
        f.write("Rot3: %s%s" % (self.rot3, os.linesep))
        f.close()

    def load(self, filename):
        """
        Load the refined parameters from a file.
        @param filename: name of the file to load
        @type filename: string
        """
        for line in open(filename):
            words = line.split(":", 1)
            key = words[0].strip().lower()
            value = words[1].strip()
            if key == "pixelsize1":
                self.pixel1 = float(value)
            elif key == "pixelsize2":
                self.pixel2 = float(value)
            elif key == "distance":
                self.dist = float(value)
            elif key == "poni1":
                self.poni1 = float(value)
            elif key == "poni2":
                self.poni2 = float(value)
            elif key == "rot1":
                self.rot1 = float(value)
            elif key == "rot2":
                self.rot2 = float(value)
            elif key == "rot3":
                self.rot3 = float(value)


def test():
    """
    simple tests
    """
    data = [
[1585.9999996029055, 2893.9999991192408, 0.53005649383067788],
[1853.9999932086102, 2873.0000001637909, 0.53005649383067788],
[2163.9999987531855, 2854.9999987738884, 0.53005649383067788],
[2699.9999977914931, 2893.9999985831755, 0.53005649383067788],
[3186.9999966428777, 3028.9999985930604, 0.53005649383067788],
[3595.0000039534661, 3167.0000022967461, 0.53005649383067788],
[3835.0000007197755, 3300.0000002536408, 0.53005649383067788],
[1252.0000026881371, 2984.0000056421914, 0.53005649383067788],
[576.99992486352289, 3220.0000014469815, 0.53005649383067788],
[52.999989546760531, 3531.9999975314959, 0.53005649383067788],
[520.99999862452842, 2424.0000005943775, 0.65327673902147754],
[1108.0000045189499, 2239.9999793751085, 0.65327673902147754],
[2022.0000098770186, 2136.9999921020726, 0.65327673902147754],
[2436.000002384907, 2137.0000034435734, 0.65327673902147754],
[2797.9999973906524, 2169.9999849019205, 0.65327673902147754],
[3516.0000041508365, 2354.0000059814265, 0.65327673902147754],
[3870.9999995625412, 2464.9999964079757, 0.65327673902147754],
[3735.9999952703465, 2417.9999888223151, 0.65327673902147754],
[3374.0001428680412, 2289.9999885080188, 0.65327673902147754],
[1709.99999872134, 2165.0000006693272, 0.65327673902147754],
[2004.0000081015958, 1471.0000012076148, 0.7592182246175333],
[2213.0000015244159, 1464.0000243454842, 0.7592182246175333],
[2115.9999952456633, 1475.0000015176133, 0.7592182246175333],
[2242.0000023736206, 1477.0000046142911, 0.7592182246175333],
[2463.9999967564663, 1464.0000011704756, 0.7592182246175333],
[2986.000011249705, 1540.9999994523619, 0.7592182246175333],
[2760.0000031761901, 1514.0000002442944, 0.7592182246175333],
[3372.0000025298395, 1617.9999995345927, 0.7592182246175333],
[3187.0000005152106, 1564.9999952212884, 0.7592182246175333],
[3952.0000062252166, 1765.0000234029771, 0.7592182246175333],
[200.99999875941003, 1190.0000046393075, 0.85451320177642376],
[463.00000674257342, 1121.9999956648539, 0.85451320177642376],
[1455.0000001416358, 936.99999830341949, 0.85451320177642376],
[1673.9999958962637, 927.99999934328309, 0.85451320177642376],
[2492.0000021823594, 922.00000383122256, 0.85451320177642376],
[2639.9999948599761, 936.00000247819059, 0.85451320177642376],
[3476.9999490636446, 1027.9999838362451, 0.85451320177642376],
[3638.9999965727247, 1088.0000258143732, 0.85451320177642376],
[4002.0000051610787, 1149.9999925115812, 0.85451320177642376],
[2296.9999822277705, 908.00000939182382, 0.85451320177642376],
[266.00000015817864, 576.00000049157074, 0.94195419730133967],
[364.00001493127616, 564.00000136247968, 0.94195419730133967],
[752.99999958240187, 496.9999948653093, 0.94195419730133967],
[845.99999758606646, 479.00000730401808, 0.94195419730133967],
[1152.0000082161678, 421.9999937722655, 0.94195419730133967],
[1215.0000019951258, 431.00019867504369, 0.94195419730133967],
[1728.0000096657914, 368.00000247754218, 0.94195419730133967],
[2095.9999932673395, 365.99999862304219, 0.94195419730133967],
[2194.0000006543587, 356.99999967534075, 0.94195419730133967],
[2598.0000021676074, 386.99999979901884, 0.94195419730133967],
[2959.9998766657627, 410.00000323183838, 0.94195419730133967],
]
    r = Refinement(data, dist=0.1, poni1=0.00, poni2=0.00, pixel1=pixelSize[0], pixel2=pixelSize[1])
    print r
    r.refine2(10000000)
    print r
    ref = numpy.array([0.089652, 0.030970, 0.027668, -0.699407 , 0.010067  , 0.000001])
    assert abs(numpy.array(r.param) - ref).max() < 1e-3
    print("test succeeded")

if __name__ == "__main__":
    pixelSize = [1.5e-5, 1.5e-5]
    if len(sys.argv) < 2:
        print("Please provide the name of a file !!!")
        sys.exit(1)
    elif sys.argv[1] == "-test":
        test()
        sys.exit(0)


    px = raw_input("Please enter the pixel size (in meter, C order, i.e. %.2e %.2e ): " % tuple(pixelSize)).split()
    if px != []:
        try:
            pixelSize = [float(i) for i in px[0:2]]
        except:
            print("error in reading pixel size")
            sys.exit(1)
    inputFile = sys.argv[1]
    basename = os.path.splitext(inputFile)[0]
    pp = PeakPicker(inputFile)
    pp.gui(True)
    data = pp.finish()
    for i in data:
        print i
    if os.name == "nt":
        print("We are under windows, matplotlib is not able to display too many images without crashing, this is why the window showing the diffraction image is closed")
        pp.closeGUI()
    r = Refinement(data, dist=0.1, poni1=0.00, poni2=0.00, pixel1=pixelSize[0], pixel2=pixelSize[1])
    print r
    previous = sys.maxint
    while previous > r.chi2():
        previous = r.chi2()
        r.refine2(1000000)
        print r

    r.refine1()
    print r
    r.save(basename + ".poni")
    import time
    t0 = time.time()
    tth = r.twoThetaArray(pp.shape)
    t1 = time.time()
    dsa = r.solidAngleArray(pp.shape)
    t2 = time.time()

    if os.name == "nt":
        print("We are under windows, matplotlib is not able to display too many images without crashing, this is why little information is displayed")
    else:
        pp.contour(tth)
        fig2 = pylab.plt.figure()
        sp = fig2.add_subplot(111)
        sp.imshow(dsa)
        fig2.show()

    fig3 = pylab.plt.figure()
    xrpd = fig3.add_subplot(111)
    t3 = time.time()
    a, b = r.xrpd(pp.data, 1024, basename + ".xy")
    t4 = time.time()
    print ("Timings:\n two theta array generation %.3fs\n diff Solid Angle  %.3fs\n Azimuthal integration: %.3fs" % (t1 - t0, t2 - t1, t4 - t3))
    xrpd.plot(a, b)
    fig3.show()



    raw_input("Press enter to quit")
