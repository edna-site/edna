#!/usr/bin/env python
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) DLS
#
#    Principal author: irakli 
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

#
# Set up PYTHON path for the EDNA kernel
#
# First locate EDNA_HOME and EDNA_SITE
#
import sys, os.path

pyStrProgramPath = sys.argv[0]
pyStrBinPath = os.path.split(pyStrProgramPath)[0]
pyStrSASPath = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrSASPath)[0]
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA sas pipeline:"
    print "Make sure that $EDNA_SITE is set up before running sas-pipeline."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print ""
    sys.exit(1)
strConfigurationFilePath = os.path.join(pyStrEdnaHomePath, "xncf", "conf", "XSConfiguration_" + os.environ["EDNA_SITE"] + ".xml")
#
# Then add kernel/src, xncf/src and xncf plugins source directories to PYTHONPATH
#
sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginControlXAFSDataBatchProcessing-v0.1","plugins"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginExecIfeffit-v0.1","plugins"))

from EDApplicationXAFSBatchProcessing import EDApplicationXAFSBatchProcessing

edApplicationXAFSBatchProcessing = EDApplicationXAFSBatchProcessing(_strPluginName="EDPluginControlXAFSDataBatchProcessingv0_1", \
                                                    _strConfigurationFileName=strConfigurationFilePath)
edApplicationXAFSBatchProcessing.execute()
