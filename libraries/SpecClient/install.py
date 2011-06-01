#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: EDNA Libraries
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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

"""EDNA-Builder for the SpecClient library"""
__contact__ = "Jerome.Kieffer@ESRF.eu"
__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, sys
strEdnaHome = os.path.join(os.sep, *tuple(os.path.abspath(sys.argv[0]).split(os.sep)[:-3]))
if ("EDNA_HOME" in os.environ):
    if  (os.environ["EDNA_HOME"] != strEdnaHome):
        print("Warning: EDNA_HOME redefined to %s" % strEdnaHome)
        os.environ["EDNA_HOME"] = strEdnaHome
else:
    os.environ["EDNA_HOME"] = strEdnaHome

sys.path.append(os.path.join(strEdnaHome, "kernel", "src"))
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller
from EDVerbose                  import EDVerbose


strLibrary = "SpecClient.tar.bz2"


if __name__ == "__main__":
    installDir = os.path.abspath(sys.argv[0]).split(os.sep)[-2]
    EDVerbose.screen("Building %s" % strLibrary)
    install = EDUtilsLibraryInstaller(installDir, strLibrary)
    install.checkPythonVersion()
    install.getArchitecture()
    install.downloadLibrary()
    install.getArchiveName()
    install.unZipArchive()
    install.buildSources()
    install.installBuilt()
    install.cleanSources()

else:
    print("This installer program is not made to be imported, please just run it")

