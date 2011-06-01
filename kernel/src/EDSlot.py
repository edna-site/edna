#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

"""
This class is used for connecting one instance of a class to another.
"""


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDObject import EDObject
from EDVerbose import EDVerbose

class EDSlot(EDObject):
    """
    This class is used for connecting one instance of a class to another.
    """

    def __init__(self):
        """
        """
        EDObject.__init__(self)
        self.__listMethod = []


    def connect(self, _pyClassMethod):
        """
        Connects a signal between an object and a method in an other object.
        """
        if (_pyClassMethod == None):
            EDVerbose.error("EDSlot.connect: None class method")
            return
        self.synchronizeOn()    # Block the thread
        self.__listMethod.append(_pyClassMethod)
        self.synchronizeOff()   # Release the thread


    def call(self, _tupleArguments=None):
        """
        Calls a slot with a list of arguments.
        @param _tupleArguments: arguments to be passed to the slot method 
        @type _tupleArguments: tuple
        """
        self.synchronizeOn()    # Block the thread
        for pyMethod in self.__listMethod:
            if (pyMethod is not None):
                self.executeMethod(pyMethod, _tupleArguments)
        self.synchronizeOff()   # Release the thread


    def executeMethod(self, _pyMethod, _tupleArguments=None):
        if (_tupleArguments is None):
            _pyMethod()
        else:
            _pyMethod(_tupleArguments)
            
            
    def getListMethod(self):
        return self.__listMethod
    
    
    def emptyListMethod(self):
        self.__listMethod = []
