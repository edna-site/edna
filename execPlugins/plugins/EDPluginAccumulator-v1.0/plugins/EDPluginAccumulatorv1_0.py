# coding: utf8
#
#    Project: General purpose plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jérôme Kieffer
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

"""
UseCase for EDPluginAccumulator:

* Keep in memory all items (accumulates them) when you feed it.
* Keep in memory queries as well. 

When one or more queries are fulfilled, then return all fulfilled queries.
There are option to keep items in memory or remove them when they are used by a query (this is an option of the query.    

There is a flush option that returns all items accumulated and remove them from the list.

There are static methods to emptyItems and emptyQueries

"""
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__data__ = "2012-03-13"

from EDThreading            import Semaphore
from EDPlugin               import EDPlugin
from XSDataCommon           import XSDataBoolean, XSDataString
from XSDataAccumulatorv1_0  import XSDataResultAccumulator, XSDataInputAccumulator, XSDataQuery

class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()
    def __set__(self, obj, value):
        cls = type(obj)
        return self.fset.__get__(None, cls)(value)


class EDPluginAccumulatorv1_0(EDPlugin):
    """
    Accumulate items and checks for fulfilled queries.
    
    items should be strings, queries are list of strings.
     
    EDPluginAccumulatorv1_0 is an simple plugin because:
    * it is not a control plugin (as it controls nothing)
    * it is not an execution plugin as it does not need to take a CPU (via SemaphoreNbCPU)    

    """
    _semaphore = Semaphore()
    _queries = {} #queries are stored as keys of a dictionary (as sorted tuple) where the value is the flag "Remove Item"
    _items = []

    def __init__(self):
        """
        Constructor of the plugin
        """
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataInputAccumulator)
        self.xsDataResult = XSDataResultAccumulator()
        self.flush = False


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginAccumulatorv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
#        there are no mandatory parameters


    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginAccumulatorv1_0.preProcess")
        with self.__class__._semaphore:
            for oneXsdItem in self.dataInput.item: #could be empty
                self._items.append(oneXsdItem.value)
            for oneXsdQuery in self.dataInput.query: #could be an empty list
                query = []
                for  oneXsdItem in oneXsdQuery.item:
                    query.append(oneXsdItem.value)

                if oneXsdQuery.removeItems is not None:
                    if oneXsdQuery.removeItems.value in [1, True, "true"]:
                        removeItems = True
                    elif oneXsdQuery.removeItems.value in [0, False, "false", None]:
                        removeItems = False
                    else:
                        removeItems = True
                else:
                    removeItems = True
                query.sort()
                self._queries[tuple(query)] = removeItems

        if self.dataInput.flush is not None:
            if self.dataInput.flush.value in [1, True, "true"]:
                self.flush = True


    def process(self, _edObject=None):
        EDPlugin.process(self)
        self.DEBUG("EDPluginAccumulatorv1_0.process")
        queriesToRemove = []
        listXsdQuery = []
        if not self.flush:
            with self.__class__._semaphore:
                for query in self._queries:
                    present = True
                    for item in query:
                        if not item in self._items:
                            present = False
                            break
                    if present is True:
                        queriesToRemove.append(query)
                        xsdQuery = XSDataQuery()
                        xsdQuery.setItem([XSDataString(item) for item in query])
                        if self._queries[query] is True:
                            xsdQuery.setRemoveItems(XSDataBoolean(True))
                            for item in query:
                                self._items.remove(item)
                        else:
                            xsdQuery.setRemoveItems(XSDataBoolean(False))
                        listXsdQuery.append(xsdQuery)

    #Remove the query from the list of queries
                for query in queriesToRemove:
                    self._queries.pop(query)
        else:
            xsdQuery = XSDataQuery()
            with self.__class__._semaphore:
                xsdQuery.setItem([XSDataString(item) for item in self._items])
                xsdQuery.setRemoveItems(XSDataBoolean(True))
                self.__class__._items = []
            listXsdQuery.append(xsdQuery)
        self.xsDataResult.setQuery(listXsdQuery)


    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginAccumulatorv1_0.postProcess")
        # Create some output data
        self.setDataOutput(self.xsDataResult)


    @classmethod
    def getItems(cls):
        """
        Static methods that returns the list of items stored without changing anything.
        Made for testing, nothing else.
         
        @return: list of items accumulated.
        @rtype: list of python string 
        """
        with cls._semaphore:
            data = cls._items
        return data
    items = classproperty(getItems)

    @classmethod
    def getQueries(cls):
        """
        Class methods that returns the list of queries stored without changing anything.
        Made for testing, nothing else.
         
        @return: dictionary of queries accumulated.
        @rtype: list of python string 
        """
        return cls._queries
    queries = classproperty(getQueries)

    @classmethod
    def reset(cls):
        """
        Class method to reset the whole class
        """
        cls.emptyItems()
        cls.emptyQueries()

    @classmethod
    def emptyItems(cls):
        """
        Class method for removing all stored items. 
        """
        cls._semaphore.acquire()
        cls._items = []
        cls._semaphore.release()

    @classmethod
    def emptyQueries(cls):
        """
        Class method for Resetting / removing all pending queries. 
        """
        with cls._semaphore:
            cls._queries = {}


    @classmethod
    def addQuery(cls, _listItem, _removeItems=True):
        """
        Class methods to append a query to the list of queries stored without changing anything else.
        Made for testing, nothing else.
        
        @param _listItem: list to be added to the queries 
        @type _listItem: list of string
        @param _removeItems: shall items be removed after the query is fulfilled ?
        @type _removeItems: boolean
        @return: nothing
        """
        with cls._semaphore:
            cls._queries[_listItem] = _removeItems


    @classmethod
    def addItem(cls, _strItem):
        """
        Class method for appending artificially an item, without changing anything else.
        Made for testing, nothing else.
        
        @param _strItem: list to be added to the queries 
        @type _strItem: string
        @return: nothing
        """
        with cls._semaphore:
            cls._items.append(_strItem)

