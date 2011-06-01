#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:    Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author: Marie-Francoise Incardona (incardon@esrf.fr)
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
__authors__ = ["Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

from EDFactoryPlugin import EDFactoryPlugin
from EDUtilsPath     import EDUtilsPath

class EDFactoryPluginTest(EDFactoryPlugin):
    """
    This subclass of EDFactoryPlugin provides a factory for loading test cases for the EDNA
    testing framework. The function of EDFactoryPluginTest is very similar to EDFactoryPlugin,
    the main differences are that only files starting with "EDTest" are considered as test cases
    to be loaded, and that the "src" and "plugin" directories are added to the python path from 
    two possible locations of the test case: 
        
    EDNA application, e.g. mxv1, or plugin collection e.g. mxExecPlugins::
     |
     |-datamodel
     |-src
     |-tests
     |   |-data
     |   |-testsuite
     |   |    |- EDTestSuiteXXX.py
     |
     |-plugins
     |   |-EDPlugin[name of plugin]-v1.0
     |   |   |-plugins
     |   |   |   |-EDPlugin[name of plugin]v10.py
     |   |   |   |-EDPlugin[another name of plugin]v10.py
     |   |   |-tests
     |   |   |   |-data
     |   |   |   |-testsuite
     |   |   |   |    |-EDTestSuiteYYY.py
     
    The "src" directory is searched relatively from both the EDTestSuiteXXX.py and
    EDTestSuiteYYY.py locations, i.e. "../../src" and "../../../../src".
     
    The "plugins" directory is searched only from the EDTestSuiteYYY.py location,
    i.e.  "../../plugins".
    
    """


    def isPlugin(self, _strFileName):
        """
        For the testing framework, the plugins are test cases and test suites which 
        starts with "EDTest" and ends with ".py".

        @param _strFileName: Name of the file
        @type _strFileName: python string

        @return: True or False
        @type: boolean
        """
        bValue = False
        if (_strFileName.startswith("EDTest") and \
             _strFileName.endswith(".py")):
            bValue = True
        return bValue


    def appendPath(self, _strPluginTestLocation):
        """
        For the tests, both the plugin directory and its corresponding "src" directory must
        be on the python path (see the class documentation for EDFactoryPluginTest).
        This method appends the plugin "src" directory to the system path, if it's not already present.

        @param _strModuleLocation: Path to the module location
        @type _strModuleLocation: python string
        """
        EDFactoryPlugin.appendPath(self, _strPluginTestLocation)

        strSrcDirectory = EDUtilsPath.appendListOfPaths(_strPluginTestLocation, [ "..", "..", "..", "..", "src" ])
        if os.path.exists(strSrcDirectory):
            if (not strSrcDirectory in sys.path):
                sys.path.append(strSrcDirectory)

        strSrcDirectory = EDUtilsPath.appendListOfPaths(_strPluginTestLocation, [ "..", "..", "src" ])
        if os.path.exists(strSrcDirectory):
            if (not strSrcDirectory in sys.path):
                sys.path.append(strSrcDirectory)

        strPluginDirectory = EDUtilsPath.appendListOfPaths(_strPluginTestLocation, [ "..", "..", "plugins" ])
        if os.path.exists(strPluginDirectory):
            if (not strPluginDirectory in sys.path):
                sys.path.append(strPluginDirectory)



