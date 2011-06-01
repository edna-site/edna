#!/bin/bash
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

#
# This python script patches the generated Python data bindings.
# See bug #394
#

import os
import sys
import tempfile
import shutil

if len(sys.argv) != 2:
    print "Usage: %s XSDataXXX.py" % sys.argv[0]
    sys.exit(1)

strXSDataFilePath = os.path.abspath(sys.argv[1])
if not os.path.exists(strXSDataFilePath):
    print "Error! Cannot find the data binding file : %s " % strXSDataFilePath
    sys.exit(1)

strXSDataFileName = os.path.basename(strXSDataFilePath)
if not strXSDataFileName.startswith("XSData") or not strXSDataFileName.endswith(".py"):
    print "Usage: %s XSDataXXX.py" % sys.argv[0]
    sys.exit(1)

print "Patching file %s (bugs #394, #657)" % strXSDataFilePath

(iFileNew, strTmpFileName) = tempfile.mkstemp(suffix=".py", prefix=strXSDataFileName[:-3] + "-")
fileNew = open(strTmpFileName, "w")

f = open(strXSDataFilePath)
listLinesXSData = f.readlines()
f.close()

#
# Go through the file line by line
#

for (iIndex, strLine) in enumerate(listLinesXSData):
    #
    # Search for XSData definition
    #
    strNewLine = strLine
    if strLine.find("class XSData:") != -1:
        # Ok, we found the definition of the class XSData
        #
        # Make XSData inherit from the Python "object" class (bug #657):
        strNewLine = "class XSData(object):\n"
        # Check if the file has already been patched
        strLine20 = listLinesXSData[iIndex + 20]
        strLine21 = listLinesXSData[iIndex + 21]
        if  strLine20.find("#") != -1 or strLine21.find("#") != -1 or \
            strLine20.find("pass") != -1 or strLine20.find("pass") != -1:
            print "The file is already patched!"
        else:
            # The file needs a patch!
            # Make sure we edit the right line
            if listLinesXSData[iIndex + 20].find("outfile.write(self.valueOf_)") != -1:
                listLinesXSData[iIndex + 20] = "        pass"
            else:
                print "Warning! File not patched."
    #
    # Write the new line to the new file
    #
    fileNew.write(strNewLine)

fileNew.close()
#
# Done! We have a patched file that we use to replace the original
#
os.remove(strXSDataFilePath)
shutil.copy(strTmpFileName, strXSDataFilePath)
