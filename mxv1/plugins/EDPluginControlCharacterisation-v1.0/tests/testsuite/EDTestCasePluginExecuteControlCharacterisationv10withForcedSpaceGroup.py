#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os


from EDTestCasePluginExecuteControlCharacterisationv10 import EDTestCasePluginExecuteControlCharacterisationv10


class EDTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup(EDTestCasePluginExecuteControlCharacterisationv10):

    def __init__(self, _oedStringTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv10.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataCollection_withForcedSpaceGroup.xml"))
        self.setNoExpectedWarningMessages(1)


    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup = EDTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup("EDTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup")
    edTestCasePluginExecuteControlCharacterisationv10withForcedSpaceGroup.execute()
