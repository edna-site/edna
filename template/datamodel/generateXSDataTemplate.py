#!/usr/bin/env python
# coding: utf8 
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       <author>
#
#    Contributing authors:   
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
from __future__ import with_statement
import os, sys, subprocess, tempfile

xsDataName = "<xsDataName>"
xsdHomeDir = os.path.dirname(os.path.abspath(sys.argv[0]))
destDir = os.path.join(os.path.dirname(xsdHomeDir), "plugins")
outputModule = os.path.join(destDir, os.path.splitext(xsDataName)[0] + ".py")


def patchFile(filename):
    """
    correct "XSDataCommon": "workspace/edna/kernel/datamodel", \
    in      "XSDataCommon": "kernel/datamodel", \
    """
    print("patching file %s" % filename)
    outfile = []
    last = None
    edna_idx = None
    for i in open(filename):
        if i.lstrip().startswith('"XSData') and (":" in i):
            mod, loc = i.split(":", 1)
            if edna_idx is None:
                edna_idx = loc.find("kernel")
            if len(loc) > edna_idx:
                i = mod + ': "' + loc[edna_idx:]
        if i != last:
            outfile.append(i)
        last = i
    with  open(filename, "w") as f:
        f.writelines(outfile)

if "EDNA_HOME" not in os.environ:
    full_path = os.path.abspath(sys.argv[0])
    while True:
        old_path = full_path
        full_path = os.path.dirname(old_path)
        if old_path == full_path:
            print("Something weird is happening: I did not find the EDNA_ROOT !!!")
            sys.exit(1)
        if  os.path.isdir(os.path.join(full_path, "kernel", "datamodel")):
            EDNA_HOME = full_path
            os.environ["EDNA_HOME"] = full_path
            break
else:
    EDNA_HOME = os.environ["EDNA_HOME"]

cmdLine = ["java", "-jar"]
cmdLine.append(os.path.join(EDNA_HOME, "kernel", "datamodel", "EDGenerateDS.jar"))
cmdLine.append("-includepaths")
cmdLine.append(os.path.join(EDNA_HOME, "kernel", "datamodel"))
cmdLine.append("-sourceDir")
cmdLine.append(xsdHomeDir)
cmdLine.append("-sourceFile")
cmdLine.append(xsDataName)
cmdLine.append("-targetdir")
cmdLine.append(os.path.join(os.path.dirname(xsdHomeDir), "plugins"))
sub = subprocess.Popen(cmdLine, cwd=tempfile.gettempdir())
print("Java code for data-binding finished with exit code %s" % sub.wait())
patchFile(outputModule)
