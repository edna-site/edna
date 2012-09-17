#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
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

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20120712"
__status__ = "alpha"


import os



from EDPluginXDSv1_0 import EDPluginXDSv1_0

from XSDataXDSv1_0 import XSDataInputXDSIndexing


class EDPluginXDSIndexingv1_0(EDPluginXDSv1_0):


    def __init__(self):
        EDPluginXDSv1_0.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSIndexing)


    def configure(self):
        EDPluginXDSv1_0.configure(self)
        self.DEBUG("EDPluginXDSIndexingv1_0.configure")
        self.addJob("XYCORR")
        self.addJob("INIT")
        self.addJob("COLSPOT")
        self.addJob("IDXREF")



