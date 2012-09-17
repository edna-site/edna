# coding: utf8
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
#                       Jérôme Kieffer (jerome.kieffer@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDPlugin import EDPlugin
from EDUtilsParallel import EDUtilsParallel
from EDVerbose import EDVerbose


class EDPluginExec(EDPlugin):
    """
    Super class for all plugins that execute something.
    For now, does nothing.
    """


    def preProcess(self, _edObject=None):
        """
        preProcess of the plugin:
        Ensure a CPU resource is available for the processing by acquiring a semaphore
        """
        EDVerbose.DEBUG("Acquire semaphore nbCPU by plugin %s, currently value: %s" % (self.getPluginName(), EDUtilsParallel.getSemaphoreValue()))
        EDUtilsParallel.semaphoreNbThreadsAcquire()
        EDPlugin.preProcess(self, _edObject)


    def finallyProcess(self, _edObject=None):
        """
        after processing of the plugin:
        Release a CPU resource by releasing the semaphore
        """
        EDVerbose.DEBUG("Release semaphore nbCPU by plugin %s, currently value: %s" % (self.getPluginName(), EDUtilsParallel.getSemaphoreValue()))
        EDUtilsParallel.semaphoreNbThreadsRelease()
        EDPlugin.finallyProcess(self, _edObject)
