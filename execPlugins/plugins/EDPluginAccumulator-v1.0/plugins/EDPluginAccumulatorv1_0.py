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

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__data__ = "2011-06-07"


import threading
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
     
    EDPluginAccumulatorv1_0 is an execution plugin because it is not a control plugin (as it controls nothing) 

    """
    __semaphore = threading.Semaphore()
    __queries = {} #queries are stored as keys of a dictionary (as sorted tuple) where the value is the flag "Remove Item"
    __items = []

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
        self.DEBUG("EDPluginAccumulatorv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#        there are no mandatory parameters


    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginAccumulatorv1_0.preProcess")
        self.__semaphore.acquire()
        for oneXsdItem in self.getDataInput().getItem(): #could be empty
            self.__items.append(oneXsdItem.getValue())
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
            self.__queries[tuple(query)] = removeItems
        self.__semaphore.release()

        if self.getDataInput().getFlush() is not None:
            if self.getDataInput().getFlush().getValue() in [1, True, "true"]:
                self.flush = True


    def process(self, _edObject=None):
        EDPlugin.process(self)
        self.DEBUG("EDPluginAccumulatorv1_0.process")
        queriesToRemove = []
        listXsdQuery = []
        if not self.flush:
            self.__semaphore.acquire()
            for query in self.__queries:
                present = True
                for item in query:
                    if not item in self.__items:
                        present = False
                        break
                if present is True:
                    queriesToRemove.append(query)
                    xsdQuery = XSDataQuery()
                    xsdQuery.setItem([XSDataString(item) for item in query])
                    if self.__queries[query] is True:
                        xsdQuery.setRemoveItems(XSDataBoolean(True))
                        for item in query:
                            self.__items.remove(item)
                    else:
                        xsdQuery.setRemoveItems(XSDataBoolean(False))
                    listXsdQuery.append(xsdQuery)

#Remove the query from the list of queries
            for query in queriesToRemove:
                self.__queries.pop(query)
            self.__semaphore.release()
        else:
            xsdQuery = XSDataQuery()
            self.__semaphore.acquire()
            xsdQuery.setItem([XSDataString(item) for item in self.__items])
            xsdQuery.setRemoveItems(XSDataBoolean(True))
            self.__class__.__items = []
            self.__semaphore.release()
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
        cls.__semaphore.acquire()
        data = cls.__items
        cls.__semaphore.release()
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
        return cls.__queries
    queries = classproperty(getQueries)

    @classmethod
    def reset(cls):
        """
        classmethod to reset the whole class
        """
        cls.emptyItems()
        cls.emptyQueries()

    @classmethod
    def emptyItems(cls):
        """
        Static method for removing all stored items. 
        """
        cls.__semaphore.acquire()
        cls.__items = []
        cls.__semaphore.release()

    @classmethod
    def emptyQueries(cls):
        """
        Static method for Resetting / removing all pending queries. 
        """
        cls.__semaphore.acquire()
        cls.__queries = {}
        cls.__semaphore.release()

    @classmethod
    def addQuery(cls, _listItem, _removeItems=True):
        """
        Static methods to append a query to the list of queries stored without changing anything else.
        Made for testing, nothing else.
        
        @param _listItem: list to be added to the queries 
        @type _listItem: list of string
        @param _removeItems: shall items be removed after the query is fulfilled ?
        @type _removeItems: boolean
        @return: nothing
        """
        cls.__semaphore.acquire()
        cls.__queries[_listItem] = _removeItems
        cls.__semaphore.release()

    @classmethod
    def addItem(cls, _strItem):
        """
        Static method for appending artificially an item, without changing anything else.
        Made for testing, nothing else.
        
        @param _strItem: list to be added to the queries 
        @type _strItem: string
        @return: nothing
        """

        cls.__semaphore.acquire()
        cls.__items.append(_strItem)
        cls.__semaphore.release()

