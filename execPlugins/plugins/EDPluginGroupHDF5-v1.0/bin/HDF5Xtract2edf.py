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
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, h5py, fabio


def extractOneImageStack(filename, h5path=None, destPath=None):
    """
    process one HDF5 file
    """
    if destPath == None:
        destPath = "."
    if filename.find("%") > 0:
        h5file = h5py.File(filename, driver="family")
    else:
        h5file = h5py.File(filename)
    if (h5path is None) or (h5path not in h5file):
        list_of_names = []
        h5file.visit(list_of_names.append)
        print(os.linesep + "Where is your stack of images dataset (in which group) ?")
        for onePath in list_of_names:
            if isinstance(h5file[onePath], h5py.highlevel.Group):
                    print("\t" + onePath)

        h5path = raw_input("Where is your image stack ? ")
        if not h5path in  h5file:
            print("This HDF5path %s is not in the file %s" % (filename, h5path))
            sys.exit(1)
    group = h5file[h5path]
    if "data" in group:
        data = group["data"]
    else:
        maxData = None
        for obj in group:
            if isinstance(group[obj], h5py.highlevel.Dataset):
                if len(group[obj].shape) > len(maxData.shape):
                    maxData = group[obj]
                elif len(group[obj].shape) == len(maxData.shape):
                    if group[obj].shape[0] > maxData.shape[0]:
                        maxData = group[obj]
        if maxData is None:
            raise Exception("No dataset found in provided group %s from file %s" % (h5path, filename))
        else:
            data = maxData
    dsSize = data.shape[0]

    headerGrp = []
    for obj in group:
        if isinstance(group[obj], h5py.highlevel.Group):
            testHeaderGrp = group[obj]
            for headerdataset in testHeaderGrp:
                if testHeaderGrp[headerdataset].len() != dsSize:
                    break
            else:
                headerGrp = testHeaderGrp
    if "Filenames" in group:
        EdfFilenames = group["Filenames"]
    elif "filenames" in group:
        EdfFilenames = group["filenames"]
    else:
        base = os.path.splitext(filename)[0]
        grpname = h5path.replace("/", "_")
        EdfFilenames = ["%s-%s-%04i.edf" % (base, grpname, i) for i in range(dsSize) ]
    for idx, oneFile in enumerate(EdfFilenames):
        print("Extracting " + oneFile)
        headers = {}
        for key in headerGrp:
            if key == "filename":
                continue
            headers[key] = headerGrp[key][idx]
        edf = fabio.edfimage.edfimage(data=data[idx], header=headers)
        edf.write(os.path.join(destPath, oneFile))


if __name__ == "__main__":
    printHelp = False
    destPath = None
    multiFile = False
    if len(sys.argv) == 0:
        printHelp = True
    remainingArgv = []
    for key in sys.argv[1:]:
        if key.find("-h") in [0, 1]:
            printHelp = True
        elif "-M" == key:
            multiFile = True
        elif "-o" == key:
            i = sys.argv.index("-o")
            destPath = sys.argv[i + 1]
            sys.argv.pop(i)
            sys.argv.pop(i)
            if not os.path.isdir(destPath):
                print("No such output directory" + destPath)
                destPath = None
        else:
            remainingArgv.append(key)
    if len(remainingArgv) > 0:
        if os.path.isfile(remainingArgv[0]):
            fileToProcess = remainingArgv[0]
    else:
        print(os.linesep + "No HDF5 file provided on command line. Here are the files available:")
        for oneFile in os.listdir("."):
            if os.path.splitext(oneFile)[1].lower() in [".nxs", ".h5", ".hdf", ".hdf5"]:
                print("\t" + oneFile)
        fileToProcess = raw_input("Which file to process ? ")
        if not os.path.isfile(fileToProcess):
            print("No such file: " + fileToProcess)
            fileToProcess = None
    if multiFile is True:
       length = 0
       base, ext = os.path.splitext(fileToProcess)
       listBase = list(key)
       listBase.reverse()
       for key in  listBase:
           if key.isdigit():length += 1
       fileToProcess = base[:-length] + "%%0%id" % length + ext
    if len(remainingArgv) > 2:
        h5path = remainingArgv[-1]
    else:
        h5path = None
    if fileToProcess is not None:
        extractOneImageStack(fileToProcess, h5path, destPath)

    if printHelp:
        print("Usage: HDF5Xtract2edf.py Hdf5File.h5 h5path -o /tmp")
        sys.exit(0)
