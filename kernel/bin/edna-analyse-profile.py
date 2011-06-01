#!/usr/bin/env python
#-*- coding: UTF8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (Jerome.Kieffer@esrf.fr)
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

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "GPLv3"
__date__ = "2010-02-02"
__copyright__ = "ESRF"


import pstats   as PyPstats
import sys      as PySys
import os       as PyOs

print "We are currently running python %s" % PySys.version

filename = 'profile.log'
for i in PySys.argv[1:]:
    if PyOs.path.isfile(i): filename = i

if PyOs.path.isfile(filename):
    p = PyPstats.Stats(filename)
    p.sort_stats('time').print_stats(100)

