#!/usr/bin/env python 
#-*- coding: UTF8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:   Olof Svensson (svensson@esrf.fr)
#                        Jérôme Kieffer (kieffer@esrf.fr)
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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3"
__date__ = "2010-02-02"
__copyright__ = "ESRF"

#
# Set up PYTHON path for the EDNA kernel
#
# First locate EDNA_HOME
#
import sys, os.path
cwd = os.getcwd()
pyStrProgramPath = os.path.abspath(sys.argv[0])
pyStrBinPath = os.path.split(pyStrProgramPath)[0]
pyStrKernelPath = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrKernelPath)[0]
os.environ["EDNA_HOME"] = pyStrEdnaHomePath

#Shall we set on the profiling ?
profiling = False
verbose = False
if len(sys.argv) > 1:
    for argument in sys.argv[1:]:
        if argument.lower().find("--verbose") in [1, 0]:
            verbose = True
        elif argument.lower().find("-profile") in [1, 0]:
            profiling = True
            import cProfile
        elif argument.endswith(".py"):
            sys.argv[sys.argv.index(argument)] = argument[:-3]
else:
    print('\nThis is the EDNA testing utility.\n\nYou did not provide any test to execute, like \n    %s --test EDTestSuiteKernel\nto execute the test suite of the EDNA kernel.' % sys.argv[0])
    print('Other useful options are --profile and --DEBUG\n')

if not verbose:
    sys.argv.append("--verbose")
#
# Then add kernel/src, kernel/tests/src to PYTHONPATH
#
sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "tests", "src"))
#
# Now the EDNATestLauncher can be imported and started
#

from EDTestLauncher import EDTestLauncher
edTestLauncher = EDTestLauncher()

if profiling == True:
    print("Running in Profiling Mode")
    cProfile.run('edTestLauncher.execute()', filename=os.path.join(cwd, 'profile.log'))
else:
    edTestLauncher.execute()
    
if edTestLauncher.isFailure():
    sys.exit(1)
