#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@esrf.eu)
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys
from EDTestSuite                import EDTestSuite
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller, installLibrary

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsLibraryInstaller.getArchitecture()
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "Fabio-r5080", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)


###############################################################################
# Import the right version of PIL
###############################################################################
pydictModulesBeforePIL = sys.modules.copy()

try:
    import Image
except Exception:
    if  os.path.isdir(imagingPath) and (imagingPath not in sys.path):
        sys.path.insert(1, imagingPath)
    else:
        installLibrary(imagingPath)
    import Image

if map(int, Image.VERSION.split(".")) < [1, 1, 6]:
    print "Wrong PIL: Remove old PIL from imported modules"
    for oneModule in sys.modules.copy():
        if oneModule not in pydictModulesBeforePIL:
            del sys.modules[ oneModule ]
    if  os.path.isdir(imagingPath) and (imagingPath not in sys.path):
        sys.path.insert(1, imagingPath)
    else:
        installLibrary(imagingPath)
    import Image

print "Version of Python Imaging Library found: %s" % Image.VERSION
del pydictModulesBeforePIL

################################################################################
# Import the right version of numpy 
################################################################################
pydictModulesBeforeNumpy = sys.modules.copy()

def installNumpy():
    """runs the Numpy Installer"""
    print "Building Numpy"
    cwd = os.getcwd()
    if numpyPath in sys.path: sys.path.remove(numpyPath)
    os.chdir(os.path.dirname(numpyPath))
    os.system("%s install.py" % sys.executable)
    os.chdir(cwd)
    sys.path = [".", numpyPath] + sys.path[1:]

try:
    import numpy
except Exception:
    if os.path.isdir(numpyPath)and (numpyPath not in sys.path):
        sys.path = [".", numpyPath] + sys.path[1:]
    else:
        installNumpy()
    import numpy

if map(int, numpy.version.version.split(".")) < [1, 3, 0]:
    print "Wrong numpy: Remove old NUMPY from imported modules"
    for oneModule in sys.modules.copy():
        if oneModule not in pydictModulesBeforeNumpy:
            del sys.modules[ oneModule ]
    if os.path.isdir(numpyPath)and (numpyPath not in sys.path):
        sys.path = [".", numpyPath] + sys.path[1:]
    else:
        installNumpy()
    import numpy

del pydictModulesBeforeNumpy
print "Version of Numpy Library found: %s" % numpy.version.version

################################################################################
# Import the good version of FabIO ... FABIO has not yet a version ... so it must be the good one
################################################################################

def installFabio():
    """Runs the Fabio Installer"""
    print "Building Fabio"
    cwd = os.getcwd()
    if fabioPath in sys.path: sys.path.remove(fabioPath)
    os.chdir(os.path.dirname(fabioPath))
    os.system("%s install.py" % sys.executable)
    os.chdir(cwd)
    sys.path = [".", fabioPath] + sys.path[1:]

try:
    import fabio
except Exception:
    if os.path.isdir(fabioPath) and (fabioPath not in sys.path):
        sys.path = [".", fabioPath] + sys.path[1:]
        import fabio
    else:
        installFabio()


import fabio.openimage
from fabio.openimage import openimage

################################################################################
# EDNA_SITE is not needed for this plugin so why bother !
################################################################################
if not  os.environ.has_key("EDNA_SITE"):
    os.environ["EDNA_SITE"] = "edna"



class EDTestSuitePluginThumbnailv10(EDTestSuite):
    """
    This is the test suite for EDNA plugin Thumbnailv10 
    It will run subsequently all unit tests and execution tests. 
    
    """

    def process(self):
        """
        """
        self.addTestCaseFromName("EDTestCasePluginUnitPyarchThumbnailv10")
        self.addTestSuiteFromName("EDTestSuitePluginPyarchThumbnailv10")
##############################################################################
if __name__ == '__main__':
    edTestSuitePluginThumbnailv10 = EDTestSuitePluginThumbnailv10()
    edTestSuitePluginThumbnailv10.execute()

##############################################################################
