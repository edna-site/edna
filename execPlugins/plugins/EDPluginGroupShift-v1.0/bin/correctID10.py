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
__date__ = "20/05/2011"

import os, sys
import numpy
import fabio
#import matplotlib
#from pylab import *

def correctImageID10(strImage, strDark, strFlat, strMask, dummy= -1):
    """
    @param strImage: name of the file containing the raw, uncorrected image
    @param strDark: name of the file containing the dark current image
    @param strFlat: name of the file containing the flat field correction (TO BE MULTIPLIED FOR ID10)
    @param strMask: name of the file containing the mask (bad pixel at 0, good ones at 1)
    @param dummy: value of the dumy pixels 
    """
    img = fabio.open(strImage).data.astype("float")
    dark = fabio.open(strDark).data
    flat = fabio.open(strFlat).data
    mask = 1 - fabio.open(strMask).data.astype("bool")
    shape = img.shape
    workMArray = numpy.ma.MaskedArray(img, mask)
    workMArray = numpy.maximum(workMArray - dark, numpy.zeros(shape)) * flat
    edfOut = fabio.edfimage.edfimage(header={"Dummy":str(dummy)}, data=workMArray.filled(dummy))
    outFile = os.path.splitext(strImage)[0] + ".cor"
    print("Output--> " + outFile)
    edfOut.write(outFile)

if __name__ == "__main__":
    listFile = []
    extraDict = {}
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            listFile.append(i)
        elif i.isdigit():
            extraDict["dummy"] = float(i)
    correctImageID10(*listFile, **extraDict)
