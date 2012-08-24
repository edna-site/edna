#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal authors:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
#                             Olof Svensson (svensson@esrf.fr)    
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
import shutil

"""EDNA-Builder for the Scipy library"""

__contact__ = "Jerome.Kieffer@ESRF.eu"
__authors__ = ["Jerome Kieffer", "Olof Svensson"]
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, shutil
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
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller
from EDVerbose                  import EDVerbose
from EDUtilsParallel            import EDUtilsParallel



scipyLibrary = "scipy-0.7.1.tar.gz"
blasLibrary = "blas.tgz"
lapackLibrary_g77 = "lapack-lite-3.1.1.tgz"
lapackLibrary_gfortran = "lapack-3.3.0.tgz"
libblas = "libblas.a"
liblapack = "liblapack.a"
numpyDir = "20090405-Numpy-1.3"

def getFortranCompiler():
        import numpy.distutils.fcompiler
        compilerEXE = numpy.distutils.fcompiler.find_executable("g77")
        if compilerEXE is None:
            compilerEXE = numpy.distutils.fcompiler.find_executable("gfortran")
        if compilerEXE is None:
            compilerEXE = numpy.distutils.fcompiler.find_executable("g95")
        if compilerEXE is None:
            EDVerbose.ERROR("No Fortran compiler found among g77, gfortran, g95")
        return  compilerEXE


if __name__ == "__main__":
    installDir = os.path.abspath(sys.argv[0]).split(os.sep)[-2]
    EDVerbose.screen("Building %s" % scipyLibrary)
    install = EDUtilsLibraryInstaller(installDir, scipyLibrary)
    install.checkPythonVersion()
    install.getArchitecture()
    install.downloadLibrary()
    install.getArchiveName()
    install.dependency("numpy", numpyDir, _tupleVersion=(1, 3, 0), _strMethodToGetVersion="version.version")
    numpyFullPath = os.path.join(os.environ["EDNA_HOME"], "libraries", numpyDir, install.getArchitecture())
    if os.path.isdir(numpyFullPath):
        sys.path.insert(1, numpyFullPath)
        if "PYTHONPATH" in os.environ:
            os.environ["PYTHONPATH"] = numpyFullPath + os.pathsep + os.environ["PYTHONPATH"]
        else:
             os.environ["PYTHONPATH"] = numpyFullPath

    # Set the lapack library corresponding to the fortran compiler
    fortranCompiler = getFortranCompiler()
    lapackLibrary = lapackLibrary_gfortran
    if fortranCompiler.find("g77") != -1:
        lapackLibrary = lapackLibrary_g77

    # Force installation of Blas and Lapack
    installBlas = EDUtilsLibraryInstaller(installDir, blasLibrary)
    blasPath = None
    installLapack = EDUtilsLibraryInstaller(installDir, lapackLibrary)
    lapackPath = None

    if blasPath is None or lapackPath is None:
        if blasPath is None:
            EDVerbose.screen("Checking for Blas %s : not found, so I have to compile it myself" % libblas)
        else:
            EDVerbose.screen("Checking for Blas %s : Found on %s, but I don't trust it because Lapack is missing" % (libblas, blasPath))
        libblas = os.path.splitext(libblas)[0] + ".a"
        installBlas.checkPythonVersion()
        installBlas.getArchitecture()
        installBlas.downloadLibrary()
        installBlas.unZipArchive()
        originalMake = open(os.path.join(installBlas.getSourceDirectory(), "make.inc"), "rb").readlines()
        makeFile = open(os.path.join(installBlas.getSourceDirectory(), "make.inc"), "w")
        for oneline in  originalMake:
            if oneline.startswith("FORTRAN"):
                makeFile.write("FORTRAN = %s %s" % (fortranCompiler, os.linesep))
            elif oneline.startswith("OPTS"):
                makeFile.write("%s -fPIC -shared %s" % (oneline.strip(), os.linesep))
            elif oneline.startswith("NOOPT"):
                makeFile.write("%s -fPIC -shared %s" % (oneline.strip(), os.linesep))
            elif oneline.startswith("LOADER"):
                makeFile.write("LOADER = %s  %s" % (fortranCompiler, os.linesep))
#            elif oneline.startswith("ARCHFLAGS"):
#                makeFile.write("ARCHFLAGS = -shared -o %s" % (os.linesep))
#            elif oneline.startswith("ARCH"):
#                makeFile.write("ARCH = %s %s" % (fortranCompiler, os.linesep))
#            elif  oneline.startswith("RANLIB"):
#                makeFile.write("RANLIB = ls %s" % (os.linesep))
            elif  oneline.startswith("BLASLIB"):
                makeFile.write("BLASLIB = %s %s" % (libblas, os.linesep))
            else:
                makeFile.write(oneline)

        makeFile.close()
        try:
            installBlas.make("-j %i" % EDUtilsParallel.detectNumberOfCPUs())
        except Exception:
            EDVerbose.ERROR("Error for BLAS in the 'make' step")
        if not os.path.isdir(os.path.join(installBlas.getDestinationDirectory(), "lib")):
            os.makedirs(os.path.join(installBlas.getDestinationDirectory(), "lib"))
        blasPath = os.path.join(installBlas.getDestinationDirectory(), "lib")
        shutil.copyfile(os.path.join(installBlas.getSourceDirectory(), libblas), os.path.join(blasPath, libblas))

################################################################################
# END of Blas / Start of Lapack 
################################################################################
        if lapackPath is None:
            EDVerbose.screen("Checking for Lapack %s : not found, so I have to compile it myself" % liblapack)
        else:
            EDVerbose.screen("Checking for Lapack %s : Found on %s, but I don't trust it because Blas was missing" % (liblapack, lapackPath))
        liblapack = os.path.splitext(liblapack)[0] + ".a"
        installLapack.checkPythonVersion()
        installLapack.getArchitecture()
        installLapack.downloadLibrary()
        installLapack.unZipArchive()
        originalMake = open(os.path.join(installLapack.getSourceDirectory(), "make.inc.example"), "rb").readlines()
        makeFile = open(os.path.join(installLapack.getSourceDirectory(), "make.inc"), "w")
        for oneline in  originalMake:
            if oneline.startswith("FORTRAN"):
                makeFile.write("FORTRAN = %s %s" % (fortranCompiler, os.linesep))
            elif oneline.startswith("OPTS"):
                makeFile.write("%s -O3 -fPIC -shared %s" % (oneline.strip(), os.linesep))
            elif oneline.startswith("NOOPT"):
                makeFile.write("%s -fPIC -shared %s" % (oneline.strip(), os.linesep))
            elif oneline.startswith("LOADER"):
                makeFile.write("LOADER = %s %s" % (fortranCompiler, os.linesep))
#            elif oneline.startswith("ARCHFLAGS"):
#                makeFile.write("ARCHFLAGS = -shared -o %s" % (os.linesep))
#            elif oneline.startswith("ARCH"):
#                makeFile.write("ARCH = %s %s" % (fortranCompiler, os.linesep))
#            elif  oneline.startswith("RANLIB"):
#                makeFile.write("RANLIB = ls %s" % (os.linesep))
            elif  oneline.startswith("BLASLIB"):
                makeFile.write("BLASLIB = %s %s" % (os.path.join(blasPath, libblas), os.linesep))
            elif  oneline.startswith("LAPACKLIB"):
                makeFile.write("LAPACKLIB = %s %s" % (liblapack, os.linesep))

            else:
                makeFile.write(oneline)

        makeFile.close()
        try:
            installLapack.make("-j %i" % EDUtilsParallel.detectNumberOfCPUs())
        except Exception:
            EDVerbose.ERROR("Error for LAPACK in the 'make' step")
        if not os.path.isdir(os.path.join(installLapack.getDestinationDirectory(), "lib")):
            os.makedirs(os.path.join(installLapack.getDestinationDirectory(), "lib"))
        lapackPath = os.path.join(installLapack.getDestinationDirectory(), "lib")
        shutil.copyfile(os.path.join(installLapack.getSourceDirectory(), liblapack), os.path.join(lapackPath, liblapack))
    else:
        EDVerbose.screen("Checking for Blas  %s: libblas found on %s" % (liblapack, blasPath))
        EDVerbose.screen("Checking for Lapack %s: liblapack found on %s" % (libblas, lapackPath))


    install.unZipArchive()
    os.environ["BLAS"] = blasPath
    if installBlas.getSourceDirectory() is not None:
        os.environ["BLAS_SRC"] = installBlas.getSourceDirectory()

    os.environ["LAPACK"] = lapackPath
    if installLapack.getSourceDirectory() is not None:
        os.environ["LAPACK_SRC"] = installLapack.getSourceDirectory()

    install.buildSources()
    install.installBuilt()
    install.cleanSources()

else:
    EDVerbose.ERROR("This installer program is not made to be imported, please just run it")


