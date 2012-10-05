# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
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

__author__="Thomsa Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os.path

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile, XSDataString

class EDPluginControlXdsBest( EDPluginControl ):
    """
    """

    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataMinimalXdsIn)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlXdsBest.checkParameters")


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlXdsBest.preProcess")


    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlXdsBest.process")


    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlXdsBest.postProcess")
        # XXX: maybe move the XDS output parsing there?
