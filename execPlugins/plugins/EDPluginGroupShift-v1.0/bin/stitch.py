#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: execPlugin: program for stitching images 
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

EDNAPluginName = "EDPluginControlStitchImagev1_0"


# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 5:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDJob                  import EDJob
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataImage, XSDataString, XSDataDouble, \
    XSDataBoolean, XSDataInteger
EDFactoryPluginStatic.loadModule("XSDataShiftv1_0")
from XSDataShiftv1_0        import XSDataInputStitchImage
from EDVerbose import EDVerbose

def process(_listInputFile, _output, dummy=0, autoscale=False, center=None, width=None, blending=None, mask=None):
    """
    call EDNA with this options:
    @param _listInputFile: list of input files as strings
    @param _output: output file name
    @param dummy: value for dummy pixels
    @param autoscale: shall image intensity be scaled (boolean)
    @param center: 2-list of int representing the center of the ROI
    @param width:  2-list of int representing the width of the ROI
    @param blending: blending method: max, mean or min 
    @param mask: name of the file containing the mask
    """
    xsd = XSDataInputStitchImage()
    xsd.dummyValue = XSDataDouble(dummy)
    xsd.autoscale = XSDataBoolean(autoscale)
    if blending:
        xsd.blending = XSDataString(blending)
    if mask:
        xsd.mask = XSDataImage(XSDataString(mask))
    xsd.outputImage = XSDataImage(XSDataString(_output))
    xsd.inputImages = [XSDataImage(XSDataString(i)) for i in _listInputFile]
    if isinstance(width, list):
        xsd.widthROI = [XSDataInteger(i) for i in width ]
    if isinstance(center, list):
        xsd.centerROI = [XSDataInteger(i) for i in center ]
    job = EDJob(EDNAPluginName)
    job.setDataInput(xsd)
    job.execute()

if __name__ == "__main__":
    inputlist = []
    outputFile = None
    dummy = 0
    autoscale = False
    center = None
    width = None
    blending = None
    mask = None
    for arg in sys.argv[1:]:
        if arg.startswith("-d="):
            dummy = float(arg.split("=")[1])
        elif arg.startswith("-o="):
            outputFile = arg.split("=")[1]
        elif arg.startswith("-a"):
            autoscale = True
        elif arg.startswith("-w="):
            width = [int(i) for i in arg.split("=")[1].split(",")]
        elif arg.startswith("-c="):
            center = [int(i) for i in arg.split("=")[1].split(",")]
        elif arg.startswith("-mask="):
            tmp = arg.split("=")[1]
            if os.path.isfile(tmp):
                mask = tmp
        elif arg.startswith("-max"):
            blending = "max"
        elif arg.startswith("-mean"):
            blending = "mean"
        elif arg.startswith("-min"):
            blending = "min"
        elif arg.startswith("-naive"):
            blending = "naive"
        elif arg.startswith("--debug"):
            EDVerbose.setVerboseDebugOn()
        elif os.path.isfile(arg):
            inputlist.append(arg)
        else:
            print("Unknown option: %s" % arg)
    if inputlist == [] or outputFile is None:
        print("Usage:\n\tstitch.py -o=output.edf [-d=0] [-a] [-c=256,256] [-w=256,256] [-mask=mask.edf] [-max] [-mean] [-min] [-naive] file1.edf file2.edf [file3 .... ]")
        print(" for output, dummy, autoscale, center and full width of ROI, mask file and blending methods")
    else:

        process(inputlist, outputFile, dummy, autoscale, width=width, center=center, blending=blending, mask=mask)
