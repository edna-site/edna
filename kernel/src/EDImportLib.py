#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jerome Kieffer (kieffer@esrf.fr)
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

"""
EDImportLib is a module for importing them all

Note that the use of EDImportLib is deprecated, instead please import the 
classes directly.
"""

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDVerbose                    import EDVerbose
EDVerbose.screen("Warning! The use of EDImportLib is deprecated. Please import the classes directly.")

from EDObject                     import EDObject
from EDLogFile                    import EDLogFile
from EDAction                     import EDAction
from EDSlot                       import EDSlot
from EDActionCluster              import EDActionCluster
from EDCommandLine                import EDCommandLine

from EDCompiler                   import EDCompiler
from EDList                       import EDList
