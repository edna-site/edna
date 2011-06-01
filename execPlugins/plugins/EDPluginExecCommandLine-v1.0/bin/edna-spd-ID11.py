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

import os, time, sys, threading, tempfile

# Append the EDNA kernel source directory to the python path

#pyStrProgramPath = os.path.abspath(sys.argv[0])
#pyLPath = pyStrProgramPath.split(os.sep)
#if len(pyLPath) > 5:
#    pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
#else:
#    print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
#    sys.exit()
pyStrEdnaHomePath = "/sware/exp/scisoft/edna"
os.environ["EDNA_HOME"] = pyStrEdnaHomePath

#this is a workaround for bug #336
if not os.environ.has_key("EDNA_SITE"):
    os.environ["EDNA_SITE"] = "NotConfigured"

sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))

from EDParallelExecute import EDParallelExecute


EDNAPluginName = "EDPluginExecCommandLinev10"
CORRECTED_DIRNAME = "corrected"
IMAGE_AT_ONCE = 10
SPD_PATH = "/sware/exp/fable/bin/spd"
SPD_OPTIONS = "dark_const=0 inp_const=0 inp_factor=1 inp_exp=1 save_dark=2  flat_distortion=1 pass=1"
#flood_file=/mntdirect/_data_visitor/ma829/id11/F4M_Sm_July08.edf 
#xfile=/mntdirect/_data_visitor/ma829/id11/dx_mmcs.edf 
#yfile=/mntdirect/_data_visitor/ma829/id11/dy_mmcs.edf do_distortion=2 
#dark_file=/mntdirect/_data_visitor/ma829/id11/dark_1s.edf 

dictlistImageDetector = {"Frelon":[],
                         "Star1": [],
                         "Star2":  []}

dictFlatField = {        "Frelon":"/mntdirect/_data_visitor/ma829/id11/F4M_Sm_July08.edf",
                         "Star1": "/mntdirect/_data_visitor/ma829/id11/F4M_Sm_July08.edf",
                         "Star2": "/mntdirect/_data_visitor/ma829/id11/F4M_Sm_July08.edf"
                     }
dictDarkCurrent = {      "Frelon":"/mntdirect/_data_visitor/ma829/id11/dark_1s.edf",
                         "Star1": "/mntdirect/_data_visitor/ma829/id11/dark_1s.edf",
                         "Star2": "/mntdirect/_data_visitor/ma829/id11/dark_1s.edf"
                     }
dictSpline = {      "Frelon":"/mntdirect/_data_visitor/ma829/id11/dark_1s.edf",
                         "Star1": "/mntdirect/_data_visitor/ma829/id11/dark_1s.edf",
                         "Star2": "/mntdirect/_data_visitor/ma829/id11/dark_1s.edf"
                     }


def fileName2xml(filename):
    """Here we create the XML string to be passed to the EDNA plugin from the input filename
    This can / should be modified by the final user
    
    @param filename: full path of the input file
    @type filename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    if baseName.find("Frelon") > 0 :
        detector = "Frelon"
    elif baseName.find("Star1") > 0 :
        detector = "Star1"
    elif baseName.find("Star2") > 0:
        detector = "Star2"
    else:
        return "<XSDataInputExecCommandLine></XSDataInputExecCommandLine> "
    if filename.endswith(".cor"):
        return "<XSDataInputExecCommandLine></XSDataInputExecCommandLine> "
    upperDir2 = os.path.join(*[os.sep] + filename.split(os.sep)[:-2])
    upperDir1 , baseName = tuple(filename.split(os.sep)[-2:])

#    if not os.path.isdir(os.path.join(upperDir2, CORRECTED_DIRNAME)):
#           os.makedirs(os.path.join(upperDir2, CORRECTED_DIRNAME ), int("775", 8))
    destinationPath = os.path.join(upperDir2, CORRECTED_DIRNAME, upperDir1)
    if not os.path.isdir(destinationPath):
           os.makedirs(destinationPath, int("775", 8))
    dictlistImageDetector[detector].append(filename)
    if len(dictlistImageDetector[detector]) >= IMAGE_AT_ONCE:
        xml = "<XSDataInputExecCommandLine> \
            <commandLineProgram><path ><value> %s </value></path></commandLineProgram> \
            <commandLineOptions><value>%s outdir=%s flood_file=%s dark_file=%s distortion_file=</value></commandLineOptions> \
            <inputFileName><path><value>%s</value></path></inputFileName>\
            </XSDataInputExecCommandLine> "\
             % (SPD_PATH, SPD_OPTIONS, destinationPath, dictFlatField[detector], dictDarkCurrent[detector], dictSpline[detector], " ".join(dictlistImageDetector[detector]))
        dictlistImageDetector[detector] = []
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
            print "This is the zimg application of EDNA-ExecCommandLine, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=debug)
    edna.runEDNA(paths, mode , newerOnly)


