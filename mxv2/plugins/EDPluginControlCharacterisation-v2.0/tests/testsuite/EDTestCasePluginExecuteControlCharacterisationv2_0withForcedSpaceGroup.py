#
#    Project: EDNA MXv2
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


import os

from EDTestCasePluginExecuteControlCharacterisationv2_0 import EDTestCasePluginExecuteControlCharacterisationv2_0


class EDTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup(EDTestCasePluginExecuteControlCharacterisationv2_0):

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecuteControlCharacterisationv2_0.__init__(self, "EDTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup")

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputCharacterisation_withForcedSpaceGroup.xml") , "mxv1InputCharacterisation")

        #self.setReferenceDataOutputFile( os.path.join( self.getPluginTestsDataHome(), "XSDataCharacterisationOutput_reference.xml"))



    def process(self):
        self.addTestMethod(self.testExecute)





if __name__ == '__main__':

    edTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup = EDTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup("EDTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup")
    edTestCasePluginExecuteControlCharacterisationv2_0withForcedSpaceGroup.execute()
