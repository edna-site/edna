#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, tempfile, threading

def usage():
    print """This program calculates the image quality indicators for a given image and stores the results in ISPyB.
    
Usage: %s path_to_image_directory

Optional arguments:

--verbose        : Turn on verbose output
--debug          : Turn on debugging mode in EDNA

""" % os.path.basename(sys.argv[0])

# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 5:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
        print pyStrEdnaHomePath
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath

# Force config to ESRF_ID29 in order to avoid problems with timeout for the waitfile plugin
os.environ["EDNA_SITE"] = "ESRF_ID29"

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDVerbose import EDVerbose
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataBoolean

EDFactoryPluginStatic.loadModule("XSDataGridScreeningv1_0")
from XSDataGridScreeningv1_0 import XSDataInputGridScreening


if __name__ == '__main__':
    strPathToTempDir = tempfile.mkdtemp(prefix="edna-image-quality-indicators_")
    os.chdir(strPathToTempDir)
    EDVerbose.setLogFileName(os.path.join(strPathToTempDir, "edna.log"))
    # Popolate input data
    EDVerbose.screen("Starting EDNA image quality indicators processing")
    EDVerbose.screen("Arguments: %r" % sys.argv)
    bVerbose = False
    bDebug = False
    listPaths = []
    for iIndex, strArg in enumerate(sys.argv[1:]):
        strarg = strArg.lower()
        if strarg == "--verbose":
            EDVerbose.setVerboseOn()
        elif strarg == "--debug":
            EDVerbose.setVerboseDebugOn()
        if os.path.exists(strArg):
            listPaths.append(os.path.abspath(strArg))
    for strPath in listPaths:
        xsDataInputGridScreening = XSDataInputGridScreening()
        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(strPath))
        xsDataInputGridScreening.setImageFile(xsDataFile)
        xsDataInputGridScreening.setDoOnlyImageQualityIndicators(XSDataBoolean(True))
        xsDataInputGridScreening.setStoreImageQualityIndicatorsInISPyB(XSDataBoolean(True))
        edPluginGridScreening = EDFactoryPluginStatic.loadPlugin("EDPluginControlGridScreeningv1_0")
        edPluginGridScreening.setDataInput(xsDataInputGridScreening)
        edPluginGridScreening.executeSynchronous()