#!/usr/bin/env python
#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Olof Svensson (svensson@esrf.fr) 
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
pyStrMXv2Path = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrMXv2Path)[0]
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA MXv2 characterisation application:"
    print "Make sure that $EDNA_SITE is set up before running edna-MXv2-characterisation."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print "Please read the INSTALL.txt file under the \"$EDNA_HOME/MXv2\" directory for more details"
    print ""
    sys.exit(1)
#
# Then add kernel/src and MXv2/src to PYTHONPATH
#
sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "mxv2", "src"))

#
# Now the edApplicationMXv2Characterisation can be imported and started
#
from EDApplicationMXv2Characterisation import EDApplicationMXv2Characterisation

# Check if we want to run a different plugin than EDPluginControlInterfacev2_0
strPluginName = "EDPluginControlInterfacev2_0"
for x in range(1, len(sys.argv)):
    arg = sys.argv[x]
    if arg == "-p" or arg == "--plugin":
        strPluginName = sys.argv[x+1]
        break
    elif arg.startswith("--plugin="):
	   strPluginName = arg[9:]
	   break

edApplicationMXv2Characterisation = EDApplicationMXv2Characterisation(_strPluginName = strPluginName)
edApplicationMXv2Characterisation.execute()
