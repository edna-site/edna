#
#    Project: EDNA MXv1
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Gleb Bourenkov" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCasePluginExecuteControlSubWedgeAssemblev1_1 import EDTestCasePluginExecuteControlSubWedgeAssemblev1_1

class EDTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge(EDTestCasePluginExecuteControlSubWedgeAssemblev1_1):


    def __init__(self, _edStringTestName=None):

        EDTestCasePluginExecuteControlSubWedgeAssemblev1_1.__init__(self, "EDTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputSubWedgeAssemble_nineImages.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultSubWedgeAssemble_nineImages.xml"))


    def preProcess(self):
        EDTestCasePluginExecuteControlSubWedgeAssemblev1_1.preProcess(self)
        listTestImage = []
        for iImageNumber in range(1, 10):
            listTestImage.append("testscale_1_%03d.img" % iImageNumber)
        self.loadTestImage(listTestImage)




if __name__ == '__main__':

    edTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge = EDTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge("EDTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge")
    edTestCasePluginExecuteControlSubWedgeAssemblev1_1NineImageSubWedge.execute()
