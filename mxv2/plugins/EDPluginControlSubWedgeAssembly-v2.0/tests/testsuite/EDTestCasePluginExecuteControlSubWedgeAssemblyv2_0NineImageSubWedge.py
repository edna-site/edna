#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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


from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0NineImageSubWedge(EDTestCasePluginExecute):

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlSubWedgeAssemblyv2_0")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeAssemble_nineImages.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultSubWedgeAssemble_nineImages.xml"), "mxv1Assemble")


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        listTestImage = []
        for iImageNumber in range(1, 10):
            strImageName = "testscale_1_%03d.img" % iImageNumber
            listTestImage.append(strImageName)
        self.loadTestImage(listTestImage)




if __name__ == '__main__':

    edTestCasePluginExecuteControlSubWedgeAssemblyv2_0NineImageSubWedge = EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0NineImageSubWedge("EDTestCasePluginExecuteControlSubWedgeAssemblyv2_0NineImageSubWedge")
    edTestCasePluginExecuteControlSubWedgeAssemblyv2_0NineImageSubWedge.execute()
