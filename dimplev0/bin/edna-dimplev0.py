#!/usr/bin/env cctbx.python
#
#    Project: EDNA Dimplev0
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2011 Diamond Light Source
#                       Chilton, Didcot, UK
#
#    Pipeline authors:   Ronan Keegan (ronan.keegan@stfc.ac.uk)  
#                        Graeme Winter (graeme.winter@diamond.ac.uk)
#
#    This file:          Karl Levik (karl.levik@diamond.ac.uk)
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

__author__ = "Karl Levik"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

#
# Set up PYTHON path for the EDNA kernel
#
# First locate EDNA_HOME and EDNA_SITE
#
import sys, os.path
strProgramPath = sys.argv[0]
strBinPath = os.path.split(strProgramPath)[0]
strDimplev0Path = os.path.split(strBinPath)[0]
strEdnaHomePath = os.path.split(strDimplev0Path)[0]
os.environ["EDNA_HOME"] = strEdnaHomePath
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA Dimplev0 application:"
    print "Make sure that $EDNA_SITE is set up before running edna-dimplev0."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print "Please read the INSTALL.txt file under the \"$EDNA_HOME/dimplev0\" directory for more details"
    print ""
    sys.exit(1)
strConfigurationFilePath = os.path.join(strEdnaHomePath, "dimplev0", "conf", "XSConfiguration_" + os.environ["EDNA_SITE"] + ".xml")
#
# Then add kernel/src and dimplev0/src to PYTHONPATH
#
sys.path.append(os.path.join(strEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(strEdnaHomePath, "dimplev0", "src"))

#
# Now the edApplicationMXv1Characterisation can be imported and started
#
from EDApplicationDimplev0 import EDApplicationDimplev0
edApplicationDimplev0 = EDApplicationDimplev0(_strPluginName="EDPluginControlDIMPLEPipelineCalcDiffMapv10", \
                               _strConfigurationFileName=strConfigurationFilePath)
edApplicationDimplev0.execute()
