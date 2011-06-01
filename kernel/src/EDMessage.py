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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


class EDMessage:
    ERROR_ABSTRACT_METHOD_02 = "ERROR_ABSTRACT_METHOD: %s: Method %s should be Implemented by the Final Class"
    ERROR_PLUGIN_NOT_LOADED_02 = "ERROR_PLUGIN_NOT_LOADED_02: %s: Could not load plugin %s."
    ERROR_DATA_INPUT_CLASS_NOT_DEFINED_02 = "ERROR_DATA_INPUT_CLASS_NOT_DEFINED_02: %s: %s"
    ERROR_UNEXPECTED_01 = "ERROR_UNEXPECTED_01: %s: Unexpected Error"
    ERROR_WRONG_DATA_TYPE_02 = "ERROR_WRONG_DATA_TYPE_02: %s: Wrong type for data: %s"
    ERROR_CANNOT_READ_FILE_02 = "ERROR_CANNOT_READ_FILE_02: %s: Cannot read file %s"
    ERROR_EXECUTION_03 = "ERROR_EXECUTION_03: %s: Error when executing %s: %s"
    ERROR_MANDATORY_PARAM_MISSING_02 = "ERROR_MANDATORY_PARAM_MISSING_02: %s: input parameter is missing: %s"
    ERROR_DATA_HANDLER_02 = "ERROR_DATA_HANDLER_02: %s: %s"
    ERROR_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 = "ERROR_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02: %s: No Configuration item found for: %s"

    INFO_OPTION_ENABLED_02 = "INFO_OPTION_ENABLED_02: %s: %s is Enabled"

    WARNING_RADDOSE_CONSISTENCY_PROBLEM_02 = "WARNING_RADDOSE_CONSISTENCY_PROBLEM_02: %s: %s"
    WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02 = "WARNING_NO_PLUGIN_CONFIGURATION_ITEM_FOUND_02: %s: No Configuration item found for: %s, taking default"
    WARNING_NO_PARAM_CONFIGURATION_ITEM_FOUND_03 = "WARNING_NO_PARAM_CONFIGURATION_ITEM_FOUND_03: %s: No parameter configuration %s found for: %s, taking default"
    WARNING_IMPORTANT_PARAM_MISSING_02 = "WARNING_IMPORTANT_PARAM_MISSING_02: %s: input parameter is missing: %s"
    WARNING_CANNOT_USE_PLUGIN_03 = "WARNING_CANNOT_USE_PLUGIN_03: %s: Cannot use %s: %s"






