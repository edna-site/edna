# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Jérome Kieffer (kieffer@esrf.fr)
#                        
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the Lesser General Public License as published by
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

__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120213"

import os, traceback, time
from EDVerbose import EDVerbose

def deprecated(func):
    def wrapper(*arg, **kw):
        """
        decorator that deprecates the use of a function  
        """
        EDVerbose.WARNING("%s is Deprecated !!! %s" % (func.func_name, os.linesep.join([""] + traceback.format_stack()[:-1])))
        return func(*arg, **kw)
    return wrapper


def timeit(func):
    def wrapper(*arg, **kw):
        '''This is the docstring from timeit: 
        a decorator that prints the execution time'''
        t1 = time.time()
        res = func(*arg, **kw)
        EDVerbose.WARNING("%s took %.3fs" % (func.func_name, time.time() - t1))
        return res
    return wrapper
