#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose           import EDVerbose
from XSDataDnaTables     import dna_tables

from EDUtilsTest         import EDUtilsTest
from EDUtilsFile         import EDUtilsFile
from EDUtilsTable        import EDUtilsTable
from EDAssert            import EDAssert
from EDTestCase          import EDTestCase


class EDTestCaseEDUtilsTable(EDTestCase):

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDUtilsTable")
        self.__edConfiguration = None
        strKernelDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDUtilsTable"
        self.__strDataPath = os.path.join(strKernelDataHome, strDataDir)
        self.__strFileName = "EDPluginBestv01_dnaTables.xml"
        self.__strFilePath = os.path.join(self.__strDataPath, self.__strFileName)
        self.__strFileName2 = "EDPluginBestv01_dnaTables2.xml"
        self.__strFilePath2 = os.path.join(self.__strDataPath, self.__strFileName2)


    def testTableListItem(self):
        xsItem = None
        xsItem2 = None
        strDnaTablesXML = EDUtilsFile.readFile(self.__strFilePath)
        xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
        xsTable = EDUtilsTable.getTableFromTables(xsDataDnaTables, "input")
        xsLists = EDUtilsTable.getListsFromTable(xsTable, "select_task")
        for xsList in xsLists:
            xsItem = EDUtilsTable.getItemFromList(xsList, "task")
            xsItem2 = EDUtilsTable.getItemFromList(xsList, "tata")
        EDAssert.equal("optimize", xsItem.getValueOf_())

        EDAssert.equal(None, xsItem2)

        xsLists = EDUtilsTable.getListsFromTable(xsTable, "select_tata")
        EDAssert.equal([], xsLists)

        xsTable = EDUtilsTable.getTableFromTables(xsDataDnaTables, "toto")
        EDAssert.equal(None, xsTable)

        EDVerbose.DEBUG("Test done...")


    def testListOfTables(self):
        xsItem = None
        xsItem2 = None
        strDnaTablesXML = EDUtilsFile.readFile(self.__strFilePath2)
        xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
        listTable = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "data_collection_strategy")

        EDAssert.equal(2, len(listTable))

        bFoundPlan1 = False
        bFoundPlan2 = False

        for xsTable in listTable:
            xsItem = None
            xsLists = EDUtilsTable.getListsFromTable(xsTable, "summary")
            for xsList in xsLists:
                xsItem = EDUtilsTable.getItemFromList(xsList, "resolution_reasoning")

            if(xsItem.getValueOf_() == "Low-resolution pass, no overloads"):
                bFoundPlan1 = True
            if(xsItem.getValueOf_() == "Resolution limit is set by the initial image resolution"):
                bFoundPlan2 = True

        EDAssert.equal(True, bFoundPlan1)
        EDAssert.equal(True, bFoundPlan2)



    def process(self):
        self.addTestMethod(self.testTableListItem)
        self.addTestMethod(self.testListOfTables)




if __name__ == '__main__':

    edTestCaseEDUtilsTable = EDTestCaseEDUtilsTable("TestCase EDTestCaseEDUtilsTable")
    edTestCaseEDUtilsTable.execute()
