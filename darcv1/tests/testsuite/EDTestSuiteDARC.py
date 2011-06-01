#
#    Project: The EDNA Prototype
#             http://www.edna-site.org
#
#    File: "$Id: EDTestSuiteSrc.py 579 2008-11-06 08:42:48Z svensson $"
#
#    Copyright (C) 2008 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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


from EDImportLib                          import EDCompiler
from EDTestSuite                          import EDTestSuite


class EDTestSuiteDARC( EDTestSuite ):


    def process( self ):
        self.addTestCaseFromName( "EDTestCasePluginControlExecuteDLSArchiverv10" )
        self.addTestCaseFromName( "EDTestCasePluginControlUnitDLSArchiverv10" )


##############################################################################
if __name__ == '__main__':

    # JIT compiler accelerator
    EDCompiler.accelerator()

    edTestSuiteDARC = EDTestSuiteDARC( "EDTestSuiteDARC" )
    edTestSuiteDARC.execute()

##############################################################################
