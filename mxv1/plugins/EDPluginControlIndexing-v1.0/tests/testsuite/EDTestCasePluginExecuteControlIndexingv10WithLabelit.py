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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlIndexingv10WithLabelit(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlIndexingLabelitv10")
        self.setRequiredPluginConfiguration("EDPluginLabelitIndexingv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataIndexingInput_reference.xml"))
        self.strReferenceDataOutputFile = os.path.join(self.getPluginTestsDataHome(), "XSDataIndexingResult_reference.xml")



    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img", "ref-testscale_1_002.img" ])


    def testExecute(self):
        self.run()



if __name__ == '__main__':

    edTestCasePluginExecuteControlIndexingv10WithLabelit = EDTestCasePluginExecuteControlIndexingv10WithLabelit("EDTestCasePluginExecuteControlIndexingv10WithLabelit")
    edTestCasePluginExecuteControlIndexingv10WithLabelit.execute()
