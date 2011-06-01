#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
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
from XSDataCommon import XSDataBoolean
"""
UseCase for EDPluginAccumulator:

* Keep in memory all items (accumulates them) when you feed it.
* Keep in memory queries as well. 

When one or more queries are fulfilled, then return all fulfilled queries.
There are option to keep items in memory or remove them when they are used by a query (this is an option of the query.    

There is a flush option that returns all items accumulated and remove them from the list.

There are static methods to emptyItems and emptyQueries

"""

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


import threading
from EDVerbose              import EDVerbose
from EDPlugin               import EDPlugin

from XSDataAccumulatorv1_0  import XSDataResultAccumulator, XSDataInputAccumulator, XSDataQuery, XSDataString

class EDPluginAccumulatorv1_0(EDPlugin):
    """
    Accumulate items and checks for fulfilled queries.
    
    items should be strings, queries are list of strings.
     
    EDPluginAccumulatorv1_0 is an execution plugin because it is not a control plugin (as it controls nothing) 

    """
    semaphore = threading.Semaphore()
    queries = {} #queries are stored as keys of a dictonary (as sorted tuple) where the value is the flag "Remove Item"
    items = []

    def __init__(self):
        """
        """
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataInputAccumulator)
        self.xsDataResult = XSDataResultAccumulator()
        self.flush = False


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginAccumulatorv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#        there are no mandatory parameters


    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        EDVerbose.DEBUG("EDPluginAccumulatorv1_0.preProcess")
        EDPluginAccumulatorv1_0.semaphore.acquire()
        for oneXsdItem in self.getDataInput().getItem(): #could be empty
            EDPluginAccumulatorv1_0.items.append(oneXsdItem.getValue())
        for oneXsdQuery in self.getDataInput().getQuery(): #could be an empty list
            query = []
            for  oneXsdItem in oneXsdQuery.getItem():
                query.append(oneXsdItem.getValue())

            if oneXsdQuery.getRemoveItems() is not None:
                if oneXsdQuery.getRemoveItems().getValue() in [1, True, "true"]:
                    removeItems = True
                elif oneXsdQuery.getRemoveItems().getValue() in [0, False, "false", None]:
                    removeItems = False
                else:
                    removeItems = True
            else:
                removeItems = True
            query.sort()
            EDPluginAccumulatorv1_0.queries[tuple(query)] = removeItems
        EDPluginAccumulatorv1_0.semaphore.release()

        if self.getDataInput().getFlush() is not None:
            if self.getDataInput().getFlush().getValue() in [1, True, "true"]:
                self.flush = True


    def process(self, _edObject=None):
        EDPlugin.process(self)
        EDVerbose.DEBUG("EDPluginAccumulatorv1_0.process")
        queriesToRemove = []
        listXsdQuery = []
        if not self.flush:
            EDPluginAccumulatorv1_0.semaphore.acquire()
            for query in EDPluginAccumulatorv1_0.queries:
                present = True
                for item in query:
                    if not item in EDPluginAccumulatorv1_0.items:
                        present = False
                        break
                if present is True:
                    queriesToRemove.append(query)
                    xsdQuery = XSDataQuery()
                    xsdQuery.setItem([XSDataString(item) for item in query])
                    if EDPluginAccumulatorv1_0.queries[query] is True:
                        xsdQuery.setRemoveItems(XSDataBoolean(True))
                        for item in query:
                            EDPluginAccumulatorv1_0.items.remove(item)
                    else:
                        xsdQuery.setRemoveItems(XSDataBoolean(False))
                    listXsdQuery.append(xsdQuery)

#Remove the query from the list of queries
            for query in queriesToRemove:
                EDPluginAccumulatorv1_0.queries.pop(query)
            EDPluginAccumulatorv1_0.semaphore.release()
        else:
            xsdQuery = XSDataQuery()
            EDPluginAccumulatorv1_0.semaphore.acquire()
            xsdQuery.setItem([XSDataString(item) for item in EDPluginAccumulatorv1_0.items])
            xsdQuery.setRemoveItems(XSDataBoolean(True))
            EDPluginAccumulatorv1_0.items = []
            EDPluginAccumulatorv1_0.semaphore.release()
            listXsdQuery.append(xsdQuery)
        self.xsDataResult.setQuery(listXsdQuery)

    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        EDVerbose.DEBUG("EDPluginAccumulatorv1_0.postProcess")
        # Create some output data
        self.setDataOutput(self.xsDataResult)

    @staticmethod
    def getItems():
        """
        Static methods that returns the list of items stored without changing anything.
        Made for testing, nothing else.
         
        @return: list of items accumulated.
        @rtype: list of python string 
        """
        return EDPluginAccumulatorv1_0.items

    @staticmethod
    def getQueries():
        """
        Static methods that returns the list of queries stored without changing anything.
        Made for testing, nothing else.
         
        @return: dictionary of queries accumulated.
        @rtype: list of python string 
        """
        return EDPluginAccumulatorv1_0.queries

    @staticmethod
    def emptyItems():
        """
        Static method for removing all stored items. 
        """

        EDPluginAccumulatorv1_0.semaphore.acquire()
        EDPluginAccumulatorv1_0.items = []
        EDPluginAccumulatorv1_0.semaphore.release()

    @staticmethod
    def emptyQueries():
        """
        Static method for Resetting / removing all pending queries. 
        """
        EDPluginAccumulatorv1_0.semaphore.acquire()
        EDPluginAccumulatorv1_0.queries = {}
        EDPluginAccumulatorv1_0.semaphore.release()

    @staticmethod
    def addQuery(_listItem, _removeItems=True):
        """
        Static methods to append a query to the list of queries stored without changing anything else.
        Made for testing, nothing else.
        
        @param _listItem: list to be added to the queries 
        @type _listItem: list of string
        @param _removeItems: shall items be removed after the query is fulfilled ?
        @type _removeItems: boolean
        @return: nothing
        """
        EDPluginAccumulatorv1_0.semaphore.acquire()
        EDPluginAccumulatorv1_0.queries[_listItem] = _removeItems
        EDPluginAccumulatorv1_0.semaphore.release()

    @staticmethod
    def addItem(_strItem):
        """
        Static method for appending artifically an item, without changing anything else.
        Made for testing, nothing else.
        
        @param _strItem: list to be added to the queries 
        @type _strItem: string
        @return: nothing
        """

        EDPluginAccumulatorv1_0.semaphore.acquire()
        EDPluginAccumulatorv1_0.items.append(_strItem)
        EDPluginAccumulatorv1_0.semaphore.release()

