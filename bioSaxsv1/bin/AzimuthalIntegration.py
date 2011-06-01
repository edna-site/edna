#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: BioSaxs
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

# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 3:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath


sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDVerbose          import EDVerbose
from EDParallelExecute  import EDParallelExecute


EDNAPluginName = "EDPluginBioSaxsAzimutIntv1_0"

def fileName2xml(filename):
    """Here we create the XML string to be passed to the EDNA plugin from the input filename
    This can / should be modified by the final user
    
    @param filename: full path of the input file
    @type filename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    if filename.endswith(".edf"):
        upperDir = os.path.dirname(os.path.dirname(filename))
        if not os.path.isdir(os.path.join(upperDir, "1d")):
               os.makedirs(os.path.join(upperDir, "1d"), int("775", 8))

        if not os.path.isdir(os.path.join(upperDir, "misc")):
               os.makedirs(os.path.join(upperDir, "misc"), int("775", 8))

        specfile = os.path.join(upperDir, "1d", os.path.splitext(os.path.basename(filename))[0] + ".dat")
        base = os.path.join(upperDir, "misc", os.path.splitext(os.path.basename(filename))[0])
        correctedImg = base + ".msk"
        integImg = base + ".ang"
        maskFile = os.path.join(upperDir, "Pcon_01Apr_msk.edf")
        xml = "<XSDataInput>\
<normalizedImage><path><value>%s</value></path></normalizedImage>\
<correctedImage><path><value>%s</value></path></correctedImage>\
<normalizedImageSize><value>4100000</value></normalizedImageSize>\
<integratedImage><path><value>%s</value></path></integratedImage>\
<integratedSpectrum><path><value>%s</value></path></integratedSpectrum>\
<maskFile><path><value>%s</value></path></maskFile>\
<code><value>BSAS</value></code>\
</XSDataInput>" % (filename, correctedImg, integImg, specfile, maskFile)
    return xml

def XMLerr(strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    EDVerbose.WARNING("Error in the processing of :\n%s" % strXMLin)
    return None


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        if os.path.exists(i):
            paths.append(os.path.abspath(i))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the Azimuthal Integration application of EDNA-BioSaxs, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=True, _bDebug=debug)
    edna.runEDNA(paths, mode , newerOnly)
    EDVerbose.screen("Back in main")
