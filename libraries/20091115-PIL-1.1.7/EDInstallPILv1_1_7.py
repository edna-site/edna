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

"""EDNA installer for PIL v1.1.7"""

__authors__ = ["Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

from EDVerbose                  import EDVerbose
from EDUtilsPlatform            import EDUtilsPlatform
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller, installLibrary
from EDFactoryPluginStatic      import EDFactoryPluginStatic

moduleName = "Image"
modulePath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", EDUtilsPlatform.architecture)
moduleVersion = "1.1.7"
###############################################################################
# Import the right version of PIL
###############################################################################

oModule = EDFactoryPluginStatic.preImport(moduleName, _strMethodVersion="VERSION")
if not oModule:
    oModule = EDFactoryPluginStatic.preImport(moduleName, modulePath, _strMethodVersion="VERSION")
    if oModule is None:
        installLibrary(modulePath)
        oModule = EDFactoryPluginStatic.preImport(moduleName, modulePath, _strMethodVersion="VERSION")
try:
    version = oModule.VERSION
except AttributeError:
    version = "0.0.0"

if version.split(".") < moduleVersion.split("."):
    EDVerbose.screen("Wrong %s library:  %s " % (moduleName, version))
    EDFactoryPluginStatic.unImport(moduleName)
    oModule = EDFactoryPluginStatic.preImport(moduleName, modulePath, moduleVersion, _strMethodVersion="VERSION")

EDVerbose.screen("Version of %s: %s from %s" % (moduleName, version, oModule.__file__))

