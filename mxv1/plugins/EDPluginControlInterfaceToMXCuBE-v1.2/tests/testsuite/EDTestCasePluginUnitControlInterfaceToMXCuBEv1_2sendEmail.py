#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2.py 2194 2010-10-20 10:57:11Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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
import shutil

from EDAssert                            import EDAssert
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsPath                         import EDUtilsPath
from EDConfiguration                     import EDConfiguration
from EDApplication                       import EDApplication

from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataMXCuBEv1_2 import XSDataResultCharacterisation


class EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlInterfaceToMXCuBEv1_2")
        self.strDataPath = self.getPluginTestsDataHome()


    def testSendEmail(self):
        pluginMXCuBE = self.createPlugin()
        strPathToTestConfig = os.path.join(self.getPluginTestsDataHome(),
                                                        "XSConfiguration.xml")
        edConfiguration = EDConfiguration(strPathToTestConfig)
        edConfiguration.load()
        EDApplication.setConfiguration(edConfiguration)
        pluginMXCuBE.configure()
        pluginMXCuBE.sendEmail("EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail: Test subject", "EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail: Test message")



    def process(self):
        self.addTestMethod(self.testSendEmail)




if __name__ == '__main__':

    edTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail = EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail("EDTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail")
    edTestCasePluginUnitControlInterfaceToMXCuBEv1_2sendEmail.execute()

