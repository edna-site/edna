#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from threading import Timer

from EDTestCasePluginExecuteControlImageQualityIndicatorsv1_2 import EDTestCasePluginExecuteControlImageQualityIndicatorsv1_2


class EDTestCasePluginExecuteControlImageQualityIndicatorsv1_2_testISPyB(EDTestCasePluginExecuteControlImageQualityIndicatorsv1_2):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlImageQualityIndicatorsv1_2.__init__(self, "EDPluginControlImageQualityIndicatorsv1_2")
        self.setRequiredPluginConfiguration("EDPluginDistlSignalStrengthv1_1")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputControlImageQualityIndicators_testISPyB.xml"))



