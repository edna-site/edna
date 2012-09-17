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
from EDTestSuite  import EDTestSuite
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller, installLibrary

################################################################################
# AutoBuilder for PIL
################################################################################
architecture = EDUtilsLibraryInstaller.getArchitecture()
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "Fabio-r5080", architecture)
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

try:
    import numpy
except Exception:
    if os.path.isdir(numpyPath)and (numpyPath not in sys.path):
        sys.path.insert(1, numpyPath)
    else:
        installLibrary(numpyPath)
    import numpy

if map(int, numpy.version.version.split(".")) < [1, 3, 0]:
    print "Wrong numpy: Remove old NUMPY from imported modules"
    for oneModule in sys.modules.copy():
        if oneModule not in pydictModulesBeforeNumpy:
            del sys.modules[ oneModule ]
    if os.path.isdir(numpyPath)and (numpyPath not in sys.path):
        sys.path.insert(1, numpyPath)
    else:
        installLibrary(numpyPath)
    import numpy

del pydictModulesBeforeNumpy
print "Version of Numpy Library found: %s" % numpy.version.version

################################################################################
# Import the good version of FabIO ... FABIO has not yet a version ... so it must be the good one
################################################################################
try:
    import fabio
except Exception:
    if os.path.isdir(fabioPath) and (fabioPath not in sys.path):
        sys.path.insert(1, fabioPath)
        import fabio
    else:
        installLibrary(fabioPath)


import fabio.openimage
from fabio.openimage import openimage



class EDTestSuitePluginPyarchThumbnailv10(EDTestSuite):
    """
    This is the test suite for EDNA plugin Thumbnailv10 
    It will run subsequently all unit tests and execution tests. 
    
    """

    def process(self):
        """
        """
#        self.addTestCaseFromName( "EDTestCasePluginUnitPyarchThumbnailv10" )
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_minimal")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_resize")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_keepRatio")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_png")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_gamma")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_invert")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_equalize")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_equalize_colorize")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_normalize")
        self.addTestCaseFromName("EDTestCasePluginExecutePyarchThumbnailv10_colorize")
##############################################################################
if __name__ == '__main__':
    edTestSuitePluginPyarchThumbnailv10 = EDTestSuitePluginPyarchThumbnailv10()
    edTestSuitePluginPyarchThumbnailv10.execute()

##############################################################################
