#!/usr/bin/env python
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) DLS
#
#    Principal author: irakli 
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

import sys, os.path, glob

dataPattern = sys.argv[1]
dataFiles = [os.path.abspath(tmp) for tmp in filter(lambda tmp: os.path.isfile(tmp), glob.glob(dataPattern))]

if not dataFiles:
    print "No data files were found"
else:
    print '\n', "Found following data files:"
    for file in dataFiles:
        print file
    print

    for absDataFile in dataFiles:
        dataFile = os.path.split(absDataFile)[1]
        if not os.path.isdir('EDNA-'+dataFile):
            os.mkdir('EDNA-'+dataFile)
        os.chdir('./EDNA-'+dataFile)
        print "Processing data file:    ", absDataFile  
        print ' '.join(["run-sas-pipeline.py", '--data', absDataFile] + sys.argv[2:]), '\n'
        os.system(' '.join(["run-sas-pipeline.py", '--data',  absDataFile] + sys.argv[2:]))
        os.chdir('../')
