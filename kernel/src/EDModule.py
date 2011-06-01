# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDModule.py 2539 2010-11-29 09:37:11Z kieffer $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:    Jérôme Kieffer (jerome.kieffer@esrf.eu)
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

__authors__ = ["Jérôme Kieffer" ]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import sys, os
from EDLogging import  EDLogging


class EDModule(EDLogging):
    """
    This class is a container for a module, it contains its name, it's path and the dict of modules
    """

    def __init__(self, _strModuleName):
        EDLogging.__init__(self)
        self.DEBUG("EDModule.__init__ on %s" % _strModuleName)
        self.__name = _strModuleName
        self.__module = None
        self.__path = None
        self.__dictSubModules = {}
        self.__version = ""


    def preImport(self, _strPath=None, _strMethodVersion="version"):
        """
        Load the module in memory
        @param _strPath: Path to the module to import
        @param _strMethodVersion: property or method to get the version number (should return a string)
        @return: reference to the module loaded
        """
        self.DEBUG("EDModule.preImport on %s from %s" % (self.__name, _strPath))

        if (self.__module is None):
            if _strPath and os.path.isdir(_strPath):
                self.__path = _strPath
                if _strPath in sys.path:
                    sys.path.remove(_strPath)
                sys.path.insert(1, _strPath)
            self.synchronizeOn()
            dictModulesPreImport = sys.modules.copy()
            try:
                self.__module = __import__(self.__name)
                self.DEBUG("preImport of %s from %s" % (self.__name, _strPath))
            except ImportError:
                self.__module = None
                self.ERROR("Import error while preImporting %s from %s" % (self.__name, _strPath))
                self.writeErrorTrace()
            dictModulesPostImport = sys.modules.copy()
            for module in dictModulesPreImport:
                if module in dictModulesPostImport:
                    dictModulesPostImport.pop(module)
            self.__dictSubModules = dictModulesPostImport
            self.synchronizeOff()
            if _strMethodVersion in dir(self.__module):
                try:
                    self.__version = eval(self.__module._strMethodVersion)
                except:
                    pass
                if not isinstance(self.__version, (str, unicode)):
                    try:
                        self.__version = eval(self.__module._strMethodVersion())
                    except:
                        pass
                if not isinstance(self.__version, (str, unicode)):
                    self.__version = ""
            try:
                self.__path = self.module.__file__
            except:
                pass
        return self.__module


    def unImport(self):
        """
        Method that unload a module from the system memory.
        """
        self.DEBUG("EDModule.unImport on %s" % self.__name)
        self.synchronizeOn()
        if self.__module is not None:
            for module in sys.modules.copy():
                if module in self.__dictSubModules:
                    sys.modules.pop(module)
        self.__dictSubModules = {}
        self.__module = None
        self.synchronizeOff()


    def getName(self):
        return self.__name
    name = property(getName)

    def getVersion(self):
        return self.__version
    version = property(getVersion)

    def getModule(self):
        return self.__module
    module = property(getModule)

    def getPath(self):
        return self.__path
    path = property(getPath)

    def getDictSubModules(self):
        return self.__dictSubModules
    dictSubModules = property(getDictSubModules)
