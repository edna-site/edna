#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: mxPluginExec
#             http://www.edna-site.org
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
__date__ = "20120712"
__status__ = "deprecated"

import os, time, sys, threading, tempfile

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

# Force config to ESRF_ISPyB
os.environ["EDNA_SITE"] = "ESRF_ISPyB"

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDVerbose import EDVerbose

from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDPluginISPyBStoreAutoProcv1_3")

from XSDataISPyBv1_3 import XSDataInputStoreAutoProc
from XSDataISPyBv1_3 import AutoProcContainer


def successAction(self, _edObject=None):
    EDVerbose.screen("XML data sucessfully stored in ISPyB")

def failureAction(self, _edObject=None):
    EDVerbose.ERROR("XML data not stored in ISPyB")

if __name__ == '__main__':
    strCwd = os.getcwd()
    strPathToTempDir = tempfile.mkdtemp(prefix="edna-autoproc2ispyb_")
    os.chdir(strPathToTempDir)
    EDVerbose.setVerboseOn()
    EDVerbose.setLogFileName(os.path.join(strPathToTempDir, "edna.log"))
    # Populate input data
    EDVerbose.DEBUG("Arguments: %r" % sys.argv)
    bVerbose = False
    bDebug = False
    listPaths = []
    for iIndex, strArg in enumerate(sys.argv[1:]):
        strarg = strArg.lower()
        if strarg == "--verbose":
            EDVerbose.setVerboseOn()
        elif strarg == "--debug":
            EDVerbose.setVerboseDebugOn()
        strArgPath = strArg
        if os.path.dirname(strArgPath) == "":
            strArgPath = os.path.join(strCwd, strArg)
        strArgPathAbsolute = os.path.abspath(strArgPath)
        if os.path.exists(strArgPathAbsolute):
            listPaths.append(strArgPathAbsolute)
    if listPaths == []:
        EDVerbose.ERROR("No valid XML file given as input!")
        EDVerbose.ERROR("Arguments: %r" % sys.argv)
        EDVerbose.ERROR("Usage: edna-autoproc2ispyb path_to_xml_file [--debug]")
        sys.exit(1)
    for strPath in listPaths:
        EDVerbose.screen("Starting EDNA AutoProc -> ISPyB for file %s" % strPath)
        xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
        strXMLAutoProcContainer = EDUtilsFile.readFile(strPath)
        xsDataAutoProcContainer = AutoProcContainer.parseString(strXMLAutoProcContainer)
        if xsDataAutoProcContainer is None:
            EDVerbose.WARNING("Couldn't parse file %s" % strPath)
        else:
            xsDataInputStoreAutoProc.setAutoProcContainer(xsDataAutoProcContainer)
            edPluginISPyBStoreAutoProc = EDFactoryPluginStatic.loadPlugin("EDPluginISPyBStoreAutoProcv1_3")
            edPluginISPyBStoreAutoProc.setDataInput(xsDataInputStoreAutoProc)
            edPluginISPyBStoreAutoProc.connectSUCCESS(successAction)
            edPluginISPyBStoreAutoProc.connectFAILURE(failureAction)
            edPluginISPyBStoreAutoProc.executeSynchronous()