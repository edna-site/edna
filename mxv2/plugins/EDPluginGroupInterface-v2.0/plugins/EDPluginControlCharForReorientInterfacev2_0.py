#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginControlCharForReorientInterfacev2_0.py 1949 2010-08-23 14:51:38Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr) 
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

__authors__ = ["Olof Svensson", "Karl Levik"]
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

from EDVerbose                      import EDVerbose
from EDPluginControl                import EDPluginControl
from EDPluginControlInterfacev2_0   import EDPluginControlInterfacev2_0
from EDConfiguration                import EDConfiguration

class EDPluginControlCharForReorientInterfacev2_0(EDPluginControlInterfacev2_0):
    """
    This plugin is an extension of EDPluginControlInterfacev1_2 that uses a different characterisationPlugin
    """
        
    def configure(self):
        """
        Gets the configuration parameters (if any). Use the Python name mangling rules for storing the parameters in 
        the private variables of the parent class.
        """
        EDPluginControl.configure(self)
        EDVerbose.DEBUG("EDPluginControlCharForReorientInterfacev2_0.configure")
        pluginConfiguration = self.getConfiguration()
        strUseISPyBPlugin = "false"

        if (pluginConfiguration is None):
            EDVerbose.DEBUG("No plugin configuration found for EDPluginControlCharForReorientInterfacev2_0.")
        else:
            if (self.getControlledPluginName("subWedgeAssemblePlugin") is not None):
                self._EDPluginControlInterfacev2_0__strEDPluginControlSubWedgeAssembleName = self.getControlledPluginName("subWedgeAssemblePlugin")
            if (self.getControlledPluginName("characterisationPlugin") is not None):
                self._EDPluginControlInterfacev2_0__strEDPluginControlCharacterisationName = self.getControlledPluginName("characterisationPlugin")
            if (self.getControlledPluginName("ispybPlugin") is not None):
                self._EDPluginControlInterfacev2_0__strEDPluginControlISPyBName = self.getControlledPluginName("ispybPlugin")
            strUseISPyBPlugin = EDConfiguration.getStringParamValue(pluginConfiguration, "useISPyBPlugin")

        if (strUseISPyBPlugin.lower() != "true"):
            self._EDPluginControlInterfacev2_0__strEDPluginControlISPyBName = None

