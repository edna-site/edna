#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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


from EDTestCasePluginUnit import EDTestCasePluginUnit


class EDTestCasePluginUnitSTACAlignmentv2_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginSTACAlignmentv2_0")


    def testCreatePlugin(self):
        edPlugin = self.createPlugin()


    def process(self):
        self.addTestMethod(self.testCreatePlugin)




if __name__ == '__main__':

    edTestCasePluginUnitSTACAlignmentv2_0 = EDTestCasePluginUnitMOSFLMIndexingv10("EDTestCasePluginUnitSTACAlignmentv2_0")
    edTestCasePluginUnitSTACAlignmentv2_0.execute()
