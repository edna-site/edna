#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT ID11
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

if sys.version_info < (2, 5):
    raise RuntimeError("EDNA work only with Python >= 2.5")

if not "EDNA_SITE" in os.environ:
    os.environ["EDNA_SITE"] = "ESRF"

# Append the EDNA kernel source directory to the python path
if not "EDNA_HOME" in os.environ:
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 5:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath



sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "tests", "src"))
from EDVerbose import EDVerbose
from EDParallelExecute import EDParallelExecute
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataID11v1_0")
edPluginSPD = EDFactoryPluginStatic.loadPlugin("EDPluginSPDCakev1_5")

from XSDataID11v1_0 import XSDataInputID11, XSDataFile, XSDataString, XSDataBoolean
EDNAPluginName = "EDPluginControlID11v1_0"
xsdParam = XSDataFile()
xsdOutputDir = None
xsdCorrectMask = None

def fileName2xml(filename):
    """Here we create the XML string to be passed to the EDNA plugin from the input filename
    This can / should be modified by the final user
    
    @param filename: full path of the input file
    @type filename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    if not filename.endswith(".edf"):
        return
    xsdIn = XSDataInputID11()
    xsdFile = XSDataFile()
    xsdFile.setPath(XSDataString(filename))
    xsdIn.setDataFile([xsdFile])
    xsdIn.setParameterFile(xsdParam)
    xsdIn.setCorrectMask(xsdCorrectMask)
    if xsdOutputDir is not None:
        xsdIn.setOutputdir(xsdOutputDir)
    return xsdIn.marshal()

def XMLerr(strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    EDVerbose.ERROR("Error in the processing of : %s%s" % (os.linesep, strXMLin))


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    strParamFile = None
    iNbCPU = None
    for oneArg in sys.argv[1:]:
        one_arg = oneArg.lower()
        if one_arg.find("-online") in [0, 1]:
            mode = "dirwatch"
        elif one_arg.find("-all") in [0, 1]:
            newerOnly = False
        elif one_arg.find("-debug") in [0, 1]:
            debug = True
        elif one_arg.find("-ncpu") in [0, 1]:
            iNbCPU = int(oneArg.split("=", 1)[1])
        elif one_arg.find("-o=") in [0, 1]:
            strOutDir = os.path.abspath(oneArg.split("=", 1)[1])

            if not os.path.isdir(strOutDir):
                os.makedirs(strOutDir)
            xsdOutputDir = XSDataFile()
            xsdOutputDir.setPath(XSDataString(strOutDir))
        elif one_arg.find("-p=") in [0, 1]:
            strParamFile = oneArg.split("=", 1)[1]
            if os.path.isfile(strParamFile):
                xsdParam.setPath(XSDataString(os.path.abspath(strParamFile)))
            else:
                EDVerbose.ERROR("The parameter file you provided %s is not valid !!!" % strParamFile)
        elif one_arg.find("-nocorrectmask") in [0, 1]:
            xsdCorrectMask = XSDataBoolean(0)
        elif os.path.exists(oneArg):
            paths.append(os.path.abspath(oneArg))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the ID11 application of EDNA, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mod in EDNA\n\
            -p=ParameterFile.param (MANDATORY)\n\
            -o=outputDir"

            sys.exit()
        else:
            paths = [os.getcwd()]
    if strParamFile is None:
        EDVerbose.ERROR("No parameter file: Use ''-p=file.param''")
        sys.exit(1)
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(paths, mode , newerOnly)
    EDVerbose.screen("Back in main .... close to finish")
    edPluginSPD.killAllWorkers()
