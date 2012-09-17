#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id: EDParallelExecute.py 1990 2010-08-26 09:10:15Z svensson $"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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

from __future__ import with_statement
"""
Program that does the statistics on a log file given as argument    
"""

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20111103"

import os, sys, logging
logger = logging.getLogger(__file__)

def parseLogFile(filename):
    """
    @param filename: name of a log file
    @return: interesting lines as a dict:{pluginName: {id: execTime}} 
    """
    ret = {}
    for line in open(filename):
        words = line.split()
        if len(words) < 6:
            continue
        if words[0].isdigit():
            if  "-" in words[2]:
                pluginName, id = words[2].split("-", 1)
            else:
                 continue
            if pluginName not in ret:
                ret[pluginName] = {}
            if id.isdigit():
                id = int(id)
            else:
                continue
            try:
                time = float(words[6])
            except Exception:
                continue
            ret[pluginName][id] = time
    return ret

if __name__ == "__main__":
    logFile = None
    if len(sys.argv) == 2:
        logFile = sys.argv[1]
        if not os.path.isfile(logFile):
            logFile = None
    if logFile is None:
        logger.warning(__doc__)
        sys.exit(1)
    data = parseLogFile(logFile)
    for fn in data:
        with open(fn + ".dat", "w") as f:
            id = data[fn].keys()
            id.sort()
            for i in id:
                f.write("%s\t%s%s" % (i, data[fn][i], os.linesep))
        logger.info("Written file for %s" % fn)
