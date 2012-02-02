# -*- coding: utf8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
# 
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
__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "27/05/2011"

import os, time
from EDObject import EDObject
from EDVerbose import EDVerbose

class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()
    def __set__(self, obj, value):
        cls = type(obj)
        return self.fset.__get__(None, cls)(value)

class EDSession(EDObject):
    """
    keep track on a temporary zone writable (/buffer at ESRF, /scratch elsewhere, ...)
    """
    _sessionId = None

    @classmethod
    def getSessionId(cls):
        """getter for session ID"""
        if cls._sessionId is None:
            cls._sessionId = time.strftime("%Y%m%d-%H%M%S")
        return cls._sessionId

    @classmethod
    def setSessionId(cls, idSession):
        """setter for session ID. Only valid if not yet set !!!!"""
        if cls._sessionId is None:
            cls._sessionId = idSession
        else:
            EDVerbose.ERROR("You are not allowed to change the session ID !!!!")
    sessionId = classproperty(getSessionId, setSessionId)
