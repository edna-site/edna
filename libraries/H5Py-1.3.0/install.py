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

"""EDNA-Builder for the h5py HDF5 library"""
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

h5pyLibrary = "h5py-1.3.0.tar.gz"
hdf5Library = "hdf5-1.8.5.tar.bz2"
laFile = "libhdf5.la"

EDVerbose.DEBUG("h5pyLibrary = " + h5pyLibrary)
EDVerbose.DEBUG("hdf5Library = " + hdf5Library)
EDVerbose.DEBUG("laFile = " + laFile)

if __name__ == "__main__":
    installDir = os.path.abspath(sys.argv[0]).split(os.sep)[-2]
    EDVerbose.screen("Building %s" % installDir)
    installHDF5 = EDUtilsLibraryInstaller(installDir, hdf5Library)
    hdfPath = installHDF5.searchCLib(laFile)
    if hdfPath is None:
        print
        installHDF5.checkPythonVersion()
        installHDF5.getArchitecture()
        installHDF5.downloadLibrary()
        installHDF5.unZipArchive()
        pthreadPath = installHDF5.searchCLib("libpthread.so")
        EDVerbose.DEBUG("Libpthread found in %s" % pthreadPath)
        if pthreadPath is None:
            try:
                installHDF5.configure("--prefix=%s" % (installHDF5.getDestinationDirectory()))
            except Exception:
                EDVerbose.ERROR("Error in the configure step, no pthread")
        else:
            try:
                installHDF5.configure("--prefix=%s --enable-threadsafe --with-pthread=%s" % (installHDF5.getDestinationDirectory(), pthreadPath))
            except Exception:
                EDVerbose.ERROR("Error in the configure step, with pthread")
        try:
            installHDF5.make("-j %i" % EDUtilsParallel.detectNumberOfCPUs())
        except Exception:
            EDVerbose.ERROR("Error in the 'make' step")

        try:
            installHDF5.make("install")
        except Exception:
            EDVerbose.ERROR("Error in the 'make install' step")
        hdfPath = installHDF5.getDestinationDirectory()
        installHDF5.cleanSources()
    else:
        hdfPath = os.path.dirname(hdfPath)
    EDVerbose.DEBUG("Building H5Py with HDF5 library from %s " % (hdfPath))
    install = EDUtilsLibraryInstaller(installDir, h5pyLibrary)
    install.checkPythonVersion()
    install.dependency("numpy", "20090405-Numpy-1.3")
    install.downloadLibrary()
    install.getArchiveName()
    install.unZipArchive()
    try:
        install.buildSources("--hdf5=%s" % hdfPath)
    except Exception:
        EDVerbose.ERROR("Error in the building of %s" % (h5pyLibrary))
        sys.exit(0)
    install.installBuilt()
    if not EDVerbose.isVerboseDebug():
        install.cleanSources()

else:
    EDVerbose.ERROR("This installer program is not made to be imported, please just run it")
