#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuitePluginExecuteMXv2.py 3162 2011-03-29 13:45:37Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
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



from EDTestSuite import EDTestSuite


class EDTestSuitePluginExecuteMXESRF(EDTestSuite):


    def process(self):
        # From execPlugins:
        self.addTestSuiteFromName("EDTestSuitePluginExecuteWaitFile")
        self.addTestSuiteFromName("EDTestSuitePluginExecThumbnailv10")
        # From mxPluginExec:
        self.addTestSuiteFromName("EDTestSuitePluginExecuteMXPluginExec")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteISPyBStoreImageQualityIndicatorsv1_3")
        # From mxv1:
        self.addTestSuiteFromName("EDTestSuitePluginControlPyarchThumbnailGeneratorv1_0")
        self.addTestSuiteFromName("EDTestSuitePluginExecuteMXv1")
        # From mxv2:
        self.addTestSuiteFromName("EDTestSuitePluginExecuteMXv2")



if __name__ == '__main__':


    edTestSuitePluginExecuteMXESRF = EDTestSuitePluginExecuteMXv2("EDTestSuitePluginExecuteMXESRF")
    edTestSuitePluginExecuteMXESRF.execute()

##############################################################################
