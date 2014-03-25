#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal authors:  Olof Svensson (svensson@esrf.fr)     
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
__authors__ = ["Olof Svensson"]
__contact__ = "svensson@free.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, time, sys, threading, tempfile, random

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
EDFactoryPluginStatic.loadModule("EDPluginControlPyarchThumbnailGeneratorv1_0")

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from EDPluginControlPyarchThumbnailGeneratorv1_0 import EDPluginControlPyarchThumbnailGeneratorv1_0
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataInputPyarchThumbnailGenerator


if __name__ == '__main__':
    EDVerbose.setVerboseDebugOn()
    # Sleep a random time 0-2s in order to avoid problems if many instances started at the same time
    fSleepTime = random.random()*2.0
    EDVerbose.DEBUG("Sleeping for %.2f s" % fSleepTime)
    time.sleep(fSleepTime)
    # Popolate input data
    EDVerbose.screen("Starting id29_create_thumbnail")
    # If no arguments stop
    if len(sys.argv) <= 2:
        EDVerbose.screen("Usage: id29_create_thumbnail image_directory_path image1 [image2]" )
        sys.exit(1)
    EDVerbose.screen("Arguments: %r" % sys.argv)
    strPathToTempDir = tempfile.mkdtemp(prefix="id29_create_thumbnail_")
    os.chdir(strPathToTempDir)
    EDVerbose.setLogFileName(os.path.join(strPathToTempDir, "id29_create_thumbnail.log"))
    strImageDirectory = sys.argv[1]
    listImageName = sys.argv[2:]
    # Quick check if the two image names are the same. If they are launch the thumbnail generator only once
    if len(listImageName) == 2:
        if listImageName[0] == listImageName[1]:
            listImageName = [ listImageName[0] ]
    for strImageName in listImageName:
        xsDataInputPyarchThumbnailGenerator = XSDataInputPyarchThumbnailGenerator()
        xsDataInputPyarchThumbnailGenerator.setWaitForFileTimeOut(XSDataTime(1000))
        strImagePath = os.path.join(strImageDirectory, strImageName)
        xsDataInputPyarchThumbnailGenerator.setDiffractionImage(XSDataFile(XSDataString(strImagePath)))
        EDVerbose.screen("XML input for EDPluginControlPyarchThumbnailGeneratorv1_0: %s" % xsDataInputPyarchThumbnailGenerator.marshal())
        edPluginControlPyarchThumbnailGeneratorv1_0 = EDPluginControlPyarchThumbnailGeneratorv1_0()
        edPluginControlPyarchThumbnailGeneratorv1_0.setDataInput(xsDataInputPyarchThumbnailGenerator)
        edPluginControlPyarchThumbnailGeneratorv1_0.execute()
