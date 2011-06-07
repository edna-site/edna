#coding: utf8
#
#    Project: BioSaxs Downstream processing
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Jérôme Kieffer (Kieffer@esrf.fr
#
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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


from EDTestSuite           import EDTestSuite


class EDTestSuiteSas(EDTestSuite):


    def process(self):

       self.addTestSuiteFromName("EDTestSuiteUnitSasv1_0")
       self.addTestSuiteFromName("EDTestSuiteExecuteSasv1_0")



##############################################################################
if __name__ == '__main__':


    edTestSuite = EDTestSuiteSas("EDTestSuiteSas")
    edTestSuite.execute()

##############################################################################
