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



class EDUtilsTable:
    """
    This class allows to handle "dna_tables" objects.
    
    See http://www.edna-site.org/svn/trunk/edna/kernel/datamodel/XSDataDnaTables.xsd
    for the definition of "dna_tables".    
    """

    @staticmethod
    def getTableListFromTables(_dna_table, _strTableName):
        """
        Returns a list of "table" objects from a "dna_table" object which matches a given table name.
        """
        listTables = []
        for table in _dna_table.getTable():
            if table.getName() == _strTableName:
                listTables.append(table)
        return listTables


    @staticmethod
    def getTableFromTables(_dna_table, _strTableName):
        """
        Returns the last "table" object of name "_strTableName" from a "dna_tables" object
        """
        tableMatch = None
        for table in _dna_table.getTable():
            if table.getName() == _strTableName:
                tableMatch = table
        return tableMatch


    @staticmethod
    def getListsFromTable(_table, _strListName):
        """
        Returns a list of "list" objects which matches "_strListName" in a give "table" object
        """
        listOfListMatch = []
        # Here we use "dnalist" instead of "list" because "list" is a built-in Python keyword
        for dnaList in _table.getList():
            if dnaList.getName() == _strListName:
                listOfListMatch.append(dnaList)
        return listOfListMatch


    @staticmethod
    def getItemFromList(_list, _strItemName):
        """
        Returns the last "item" object that matches _strItemName in a given "list" object
        """
        itemMatch = None
        for item in _list.getItem():
            if item.getName() == _strItemName:
                itemMatch = item
        return itemMatch


