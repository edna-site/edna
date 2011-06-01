################################################################################
# Warning: Deprecation mode 
################################################################################


#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDImportLib.py 1092 2010-02-01 13:53:18Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jerome Kieffer
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

from  EDVerbose      import  EDVerbose

def deprecated(func):
    '''This is a decorator to mark a method as deprecated and
    send a warning whenever it is called.
    '''
    def depfunc(*args, **kwargs):
        EDVerbose.WARNING("Deprecation of EDCompiler by Monday 7th June 2010, called %s" % func.__name__)
        return func(*args, **kwargs)
    depfunc.__name__ = func.__name__
    depfunc.__doc__ = func.__doc__
    depfunc.__dict__.update(func.__dict__)
    return depfunc

class EDCompiler(object):
    """
    Interface for AL Compiler.
    """
    @deprecated
    def __init__(self):
        super(self)


    @staticmethod
    @deprecated
    def accelerator():
        """
        This method accelerates the application by a JIT compiler.
        """
        pass


##############################################################################
