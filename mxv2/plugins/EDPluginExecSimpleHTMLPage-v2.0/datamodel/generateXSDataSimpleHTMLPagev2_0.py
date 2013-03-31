#
#    Project: MXv1
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:       Olof Svensson
#
#    Contributing authors:   
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

import os, sys

if not os.environ.has_key("EDNA_HOME"):
    strProgramPath = os.path.abspath(sys.argv[0])
    pyListPath = strProgramPath.split(os.sep)
    if len(pyListPath) > 5:
        strEdnaHomePath = os.sep.join(pyListPath[:-5])
    else:
        print ("Problem in the EDNA_HOME path ..." + strEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(strEdnaHomePath, "src"))
from EDFactoryPluginStatic import EDFactoryPluginStatic

strXsdFileName="XSDataSimpleHTMLPagev2_0.edml"

strPluginDir = EDFactoryPluginStatic.getModuleLocation("EDPluginExecSimpleHTMLPagev2_0")
strMXv1DatamodelHomeDir = os.path.join(strEdnaHomePath, "mxv1", "datamodel")
strXsdHomeDir  = os.path.join(os.path.dirname(strPluginDir), "datamodel")

strKernelDatamodelHomeDir = os.path.join(strEdnaHomePath, "kernel", "datamodel")


strCommand = "java -jar %s/EDGenerateDS.jar -includepaths %s,%s,%s -sourceDir %s -sourceFile %s -targetdir %s" % (\
          strKernelDatamodelHomeDir, strKernelDatamodelHomeDir, strMXv1DatamodelHomeDir, strXsdHomeDir,\
          strXsdHomeDir, strXsdFileName, strPluginDir)

print strCommand
os.system("java -version")
os.chdir(strXsdHomeDir)
os.system(strCommand)
