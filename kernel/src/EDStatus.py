#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: EDNA-Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDParallelExecute.py 1990 2010-08-26 09:10:15Z svensson $"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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
this static class keeps track of plugins under execution and which have succeeded or failed
"""
__authors__ = ["Jérôme Kieffer"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDVerbose import EDVerbose
from threading import Semaphore

class EDStatus(object):
    __listRunning = []
    __listSuccess = []
    __listFailure = []
    __sem = Semaphore()


    @classmethod
    def getRunning(cls):
        return cls.__listRunning


    @classmethod
    def getSuccess(cls):
        return cls.__listSuccess


    @classmethod
    def getFailure(cls):
        return cls.__listFailure


    @classmethod
    def tellRunning(cls, strPluginId):
        """
        Tell the strPluginId has started.
        @param strPluginId:  concatenation of the plugin-name and plugin-Id
        """
        cls.__sem.acquire()
        cls.__listRunning.append(strPluginId)
        cls.__sem.release()


    @classmethod
    def tellSuccess(cls, strPluginId):
        """
        Tell the strPluginId has finished with success.
        @param strPluginId: concatenation of the plugin-name and plugin-Id
        """
        cls.__sem.acquire()
        try:
            cls.__listRunning.remove(strPluginId)
        except ValueError:
            EDVerbose.ERROR("Unable to remove %s from running plugins' list" % strPluginId)
        else:
            cls.__listSuccess.append(strPluginId)
        cls.__sem.release()


    @classmethod
    def tellFailure(cls, strPluginId):
        """
        Tell the strPluginId has finished with failure.
        @param strPluginId: concatenation of the plugin-name and plugin-Id
        """
        cls.__sem.acquire()
        try:
            cls.__listRunning.remove(strPluginId)
        except ValueError:
            EDVerbose.ERROR("Unable to remove %s from running plugins' list" % strPluginId)
        else:
            cls.__listFailure.append(strPluginId)
        cls.__sem.release()
