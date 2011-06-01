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

import os, time, sys, threading, tempfile, string

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
from EDParallelExecute import EDParallelExecute
sys.path.append(os.path.join(os.environ["EDNA_HOME"], "execPlugins", "plugins" , "EDPluginGroupHDF5-v1.0", "plugins"))
from EDPluginHDF5MapOfSpectrav10 import EDPluginHDF5MapOfSpectrav10


EDNAPluginName = "EDPluginHDF5MapOfSpectrav10"

def fileName2xml(filename):
    """Here we create the XML string to be passed to the EDNA plugin from the input filename
    This can / should be modified by the final user
    
    @param filename: full path of the input file
    @type filename: python string representing the path
    @rtype: XML string
    @return: python string  
    """

    basename, ext = os.path.splitext(os.path.basename(filename))
    if ext != ".azim":
        print "Not a good file: %s, Bye" % filename
        return
    basename = list(basename)
    basename.reverse()
    number = ""
    for i in basename:
        if i.isdigit():
            number = i + number
        else: break
    number = int(number)
    fastMotor = (number - 1) % 171
    slowMotor = (number - 1) / 171

    xml = "<XSDataInputHDF5MapSpectra>\
    <HDF5File><path><value>/mnt/data/bigHDF5/ID22-ODA-MapSpectra.h5</value></path></HDF5File>\
    <internalHDF5Path><value>MapSpectra</value></internalHDF5Path>\
    <inputSpectrumFile>\
        <path><value>%s</value></path>\
        <fastMotorPosition><value>%s</value></fastMotorPosition>\
        <slowMotorPosition><value>%s</value></slowMotorPosition>\
        <meshScan>\
        <fastMotorSteps><value>170</value></fastMotorSteps>\
        <slowMotorSteps><value>60</value></slowMotorSteps>\
        <fastMotorStart><value>0</value></fastMotorStart>\
        <slowMotorStart><value>0</value></slowMotorStart>\
        <fastMotorStop><value>170</value></fastMotorStop>\
        <slowMotorStop><value>60</value></slowMotorStop>\
        </meshScan>\
    </inputSpectrumFile>\
    <multiFiles><value>0</value></multiFiles>\
    </XSDataInputHDF5MapSpectra>" % (filename, fastMotor, slowMotor)
    print filename + " should be on position Slow=%4i Fast=%4i" % (slowMotor, fastMotor)
#    print xml
    return xml

def XMLerr(strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    print "Error in the processing of :"
    print strXMLin
    return None


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    ncpu = 0
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            ncpu = int(i.split("=", 1)[1])
        if os.path.exists(i):
            paths.append(os.path.abspath(i))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the HDF5 2D map of Spectra application of EDNA, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mod in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=True, _bDebug=debug, _iNbThreads=ncpu)
    edna.runEDNA(paths, mode , newerOnly)
    print "Back in main"
    EDPluginHDF5MapOfSpectrav10.closeAll()
