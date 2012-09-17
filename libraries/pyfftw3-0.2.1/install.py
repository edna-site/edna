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

"""EDNA-Builder for the FFTw3 library"""
__contact__ = "Jerome.Kieffer@ESRF.eu"
__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys
#to be compatible with windows
#strEdnaHome = os.path.join(os.sep, *tuple(os.path.abspath(sys.argv[0]).split(os.sep)[:-3]))
from os.path  import dirname
strEdnaHome = dirname(dirname(dirname(os.path.abspath(sys.argv[0]))))
if ("EDNA_HOME" in os.environ):
    if  (os.environ["EDNA_HOME"] != strEdnaHome):
        print("Warning: EDNA_HOME redefined to %s" % strEdnaHome)
        os.environ["EDNA_HOME"] = strEdnaHome
else:
    os.environ["EDNA_HOME"] = strEdnaHome

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDVerbose                  import EDVerbose
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller
from EDUtilsParallel            import  EDUtilsParallel


strLibrary = "PyFFTW3-0.2.1.tar.gz"


if __name__ == "__main__":
    installDir = os.path.abspath(sys.argv[0]).split(os.sep)[-2]
    EDVerbose.screen("Building %s" % strLibrary)
    install = EDUtilsLibraryInstaller(installDir, strLibrary)
    install.checkPythonVersion()
    install.downloadLibrary()
    install.getArchiveName()
    install.unZipArchive()
    install.buildSources()
    install.installBuilt()
    install.cleanSources()

#if os.name == "nt":
#    fftw - 3.2.2.pl1 - dll32.zip
#elif os.name == "posix":
#    fftwLibrary = "hdf5-1.8.5.tar.bz2"
#else:
#    fftwLibrary = None
#laFile = "libfftw3.so"

#if __name__ == "__main__":
#    installDir = os.path.abspath(sys.argv[0]).split(os.sep)[-2]
#    EDVerbose.screen("Building %s" % installDir)
#    installer = EDUtilsLibraryInstaller(installDir, pyfftwLibrary)
#    pathClib = installer.searchCLib(laFile)
#    if pathClib is None:
#        installer.checkPythonVersion()
#        installer.getArchitecture()
#        installer.downloadLibrary()
#        installer.unZipArchive()
#        pthreadPath = installer.searchCLib("libpthread.so")
#        EDVerbose.DEBUG("Libpthread found in %s" % pthreadPath)
#        if pthreadPath is None:
#            try:
#                installer.configure("--prefix=%s" % (installer.getDestinationDirectory()))
#            except Exception:
#                EDVerbose.ERROR("Error in the configure step, no pthread")
#        else:
#            try:
#                installer.configure("--prefix=%s --enable-threadsafe --with-pthread=%s" % (installer.getDestinationDirectory(), pthreadPath))
#            except Exception:
#                EDVerbose.ERROR("Error in the configure step, with pthread")
#        try:
#            installer.make("-j %i" % EDUtilsParallel.detectNumberOfCPUs())
#        except Exception:
#            EDVerbose.ERROR("Error in the 'make' step")
#
#        try:
#            installer.make("install")
#        except Exception:
#            EDVerbose.ERROR("Error in the 'make install' step")
#        pathClib = installer.getDestinationDirectory()
#        installer.cleanSources()
#    else:
#        pathClib = os.path.dirname(pathClib)
#    EDVerbose.DEBUG("Building H5Py with HDF5 library from %s " % (pathClib))
#    install = EDUtilsLibraryInstaller(installDir, h5pyLibrary)
#    install.checkPythonVersion()
#    install.dependency("numpy", "20090405-Numpy-1.3")
#    install.downloadLibrary()
#    install.getArchiveName()
#    install.unZipArchive()
#    try:
#        install.buildSources("--hdf5=%s" % pathClib)
#    except Exception:
#        EDVerbose.ERROR("Error in the building of %s" % (h5pyLibrary))
#        sys.exit(0)
#    install.installBuilt()
#    if not EDVerbose.isVerboseDebug():
#        install.cleanSources()
#
#else:
#    EDVerbose.ERROR("This installer program is not made to be imported, please just run it")
