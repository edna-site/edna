#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: EDNA Libraries
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal authors:   Olof Svensson (svensson@esrf.fr)
#                         Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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
#
#

"""EDNA installer for Fabio r5080"""

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110722"
import os, sys
if "EDNA_HOME" not in os.environ:
    EDNA_HOME = os.path.dirname(os.path.dirname(__file__))
    os.environ["EDNA_HOME"] = EDNA_HOME
else:
    EDNA_HOME = os.environ["EDNA_HOME"]
kernel_src = os.path.join(EDNA_HOME, "kernel", "src")
if kernel_src not in sys.path:
    sys.path.append(kernel_src)

from EDVerbose import EDVerbose
from EDUtilsPlatform import EDUtilsPlatform
from EDUtilsLibraryInstaller             import EDUtilsLibraryInstaller, installLibrary

fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "Fabio-r5080", EDUtilsPlatform.architecture)

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
