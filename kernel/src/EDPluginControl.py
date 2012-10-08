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

from __future__ import with_statement

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, time, gc

from EDVerbose import EDVerbose
from EDPlugin import EDPlugin
from EDSlot import EDSlot
from EDConfiguration import EDConfiguration
from EDActionCluster import EDActionCluster
from EDFactoryPluginStatic import EDFactoryPluginStatic


class EDPluginControl(EDPlugin):
    """
    An EDPluginControl is a plugin that is responsible for a EDPluginExec or EDPluginControl plugin execution:
    It is responsible for:
        - The EDPluginExec or EDPluginControl Workflow
        - The data propagation between the EDPluginExec
        - The translation between generic and specific data models via EDHandler classes
        - The error/warning propagation
        - The executive summaries propagation
        - Execution of an "action cluster": a set of plugins can be added to a so called "action cluster"
          with the method "addPluginToActionCluster". All the plugins in the cluster can then be executed
          simultaneously with the method "executeActionCluster" and synchronized with the method
          "synchronizeActionCluster". The number of threads used by the action cluster is by default the
          number of processors available on the computer, but this value can be changed either by
          calling the method "setClusterSize" or by using the configuration parameter "clusterSize".
    """

    def __init__ (self):
        """
        """
        EDPlugin.__init__(self)
        self.__strPluginToBeControlledName = None
        self.__dictControlledPlugins = {}
        self.__edActionCluster = None
        self.__iClusterSize = None
        self.__listOfLoadedPlugins = []


    def configure(self):
        """
        Gets the EDPluginControl parameters from the configuration file and stores them in class member attributes.
        """
        EDPlugin.configure(self)
        EDVerbose.DEBUG("EDPluginControl.configure")
        strControlledPlugins = self.config.get("controlledPlugins", None)
        if strControlledPlugins is not None:
            pyListControlledPlugins = strControlledPlugins.split(",")
            for strControlledPlugin in pyListControlledPlugins:
                strControlledPluginName = self.config.get(strControlledPlugin)
                if strControlledPluginName != None:
                    self.setControlledPluginName(strControlledPlugin, strControlledPluginName)
                    EDVerbose.DEBUG("EDPluginControl.configure: setting controlled plugin %s to specific plugin %s" % (strControlledPlugin, strControlledPluginName))
        strClusterSize = self.config.get("clusterSize", None)
        if strClusterSize is not None:
            self.__iClusterSize = int(strClusterSize)
            EDVerbose.DEBUG("EDPluginControl.configure: setting cluster size to %d" % self.__iClusterSize)


    def emptyListOfLoadedPlugin(self):
        """
        Reset all plugins kept in memory
        """
        self.__listOfLoadedPlugins = []
        gc.collect()

    def getListOfLoadedPlugin(self):
        """
        """
        return self.__listOfLoadedPlugins


    def removeLoadedPlugin(self, _plugin):
        """
        Remove a plugin from the list of loaded plugins to free some memory
        @param _plugin: plugin to remove
        @type _plugin: instance of the class EDPlugin
        """
        if _plugin in self.__listOfLoadedPlugins:
            with self.locked():
                self.__listOfLoadedPlugins.remove(_plugin)
            self.DEBUG("EDPluginControl.removeLoadedPlugin: Caught, removed %s unreferenced objects. currently there are %i plugins" % (gc.get_count(), len(self.__listOfLoadedPlugins)))
            gc.collect()
        else:
            self.DEBUG("EDPluginControl.removeLoadedPlugin: Missed. currently there are %i plugins" % len(self.__listOfLoadedPlugins))


    def synchronizePlugins(self):
        EDVerbose.DEBUG("EDPluginControl.synchronizePlugins")
        bSynchronized = False
        while not bSynchronized:
            listPluginOrig = self.__listOfLoadedPlugins[:]
            for edPlugin in listPluginOrig:
                if edPlugin.isStarted() and (not edPlugin.isEnded()):
                    edPlugin.synchronize()
            time.sleep(0.01)
            with self.locked():
                bSynchronized = (self.__listOfLoadedPlugins == listPluginOrig)


    def loadPlugins(self):
        """
        This method loads and returns a list of references to the plugins to be controlled.
        
        The name of the plugin to be controlled is set set before calling this method using the 
        "setControlledPluginName" method. 
        
        The base name of the plugin to be controlled is used as the working
        directory name of the plugin in question. The name of the plugin is used as 
        base name. 
        """
        EDVerbose.DEBUG("EDPluginControl.loadPlugins")
        listKeys = self.__dictControlledPlugins.keys()
        listLoadedPlugins = []
        for strKey in listKeys:
            strPluginName = self.__dictControlledPlugins[strKey]
            edPlugin = EDFactoryPluginStatic.loadPlugin(strPluginName)
            edPlugin.setBaseDirectory(self.getWorkingDirectory())
            edPlugin.setBaseName(strPluginName)
            listLoadedPlugins.append(edPlugin)
        return listLoadedPlugins


    def loadPlugin(self, _strPluginToBeControlledName=None, _strBaseName=None):
        """
        This method loads and returns a reference to the plugin to be controlled.
        
        The name of the plugin to be controlled can either be passed as an
        argument, or bet set before calling this method using the 
        "setPluginToBeControlledName". 
        
        The base name of the plugin to be controlled is used as the working
        directory name of the plugin in question. If no argument is supplied
        the name of the plugin is used as base name. In the case of creation of
        several plugins to be launched simultaneously, the base name should be
        different for each plugin and hence must be provided explicitly.
        """
        EDVerbose.DEBUG("EDPluginControl.loadPlugin")
        if (_strPluginToBeControlledName is None):
            strPluginName = self.__strPluginToBeControlledName
        else:
            strPluginName = _strPluginToBeControlledName
        edPlugin = EDFactoryPluginStatic.loadPlugin(strPluginName)
        if (edPlugin is None):
            strErrorMessage = "EDPluginControl.loadPlugin : Cannot load plugin %s" % strPluginName
            EDVerbose.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            raise RuntimeError, strErrorMessage
        else:
            self.__listOfLoadedPlugins.append(edPlugin)
        edPlugin.setBaseDirectory(self.getWorkingDirectory())
        if (_strBaseName is None):
            # Check if base name exists. OBS! Not thread safe so please set explicitly
            # _strBaseName for multi-threaded code
            strRenamedPlugin = self.compactPluginName(strPluginName)
            strNewWorkingDirectory = os.path.join(self.getWorkingDirectory(), strRenamedPlugin)
            if (os.path.exists(strNewWorkingDirectory)):
                edPlugin.setBaseName(edPlugin.createBaseName())
            else:
                edPlugin.setBaseName(strRenamedPlugin)
        else:
            edPlugin.setBaseName(_strBaseName)
        return edPlugin


    def setControlledPluginName(self, _strControlledPluginName, _strControlledPluginValue):
        """
        Adds a name-value pair to the dictionary to map the general to the specific name of a plugin to be controlled
        """
        self.__dictControlledPlugins[_strControlledPluginName] = _strControlledPluginValue


    def getControlledPluginName(self, _strControlledPluginName):
        """
        Returns the name of the plugin to be controlled.
        """
        strPluginname = None
        if self.__dictControlledPlugins.has_key(_strControlledPluginName):
            strPluginname = self.__dictControlledPlugins[_strControlledPluginName]
        return strPluginname


    def addWarningMessages(self, _listWarningMessages):
        """
        Adds a list of warning messages in the existing list of warning messages
        """
        EDVerbose.DEBUG("EDPluginControl.addWarningMessages")
        for strWarningMessage in _listWarningMessages:
            self.addWarningMessage(strWarningMessage)


    def addErrorMessages(self, _listErrorMessages):
        """
        Adds a list of error messages in the existing list of error messages
        """
        EDVerbose.DEBUG("EDPluginControl.addErrorMessages")
        for strErrorMessage in _listErrorMessages:
            self.addErrorMessage(strErrorMessage)


    def retrieveFailureMessages(self, _edPlugin, _strMethodCaller):
        """
        Propagates failure messages from a plugin including unexpected errors
        Should be called in the plugin control method invoked when a plugin exec fails (doActionFailure<>)
        """
        EDVerbose.DEBUG("EDPluginControl.retrieveFailureMessages")
        self.retrieveWarningMessages(_edPlugin)
        self.retrieveErrorMessages(_edPlugin, _strMethodCaller, True)


    def retrieveSuccessMessages(self, _edPlugin, _strMethodCaller):
        """
        Propagates success messages from a plugin
        Error messages are retrieved because a plugin could end successfully with errors (depending on the use case)
        In this case, there is no check for unexpected errors
        """
        EDVerbose.DEBUG("EDPluginControl.retrieveSuccessMessages")
        self.retrieveWarningMessages(_edPlugin)
        self.retrieveErrorMessages(_edPlugin, _strMethodCaller, False)


    def retrieveErrorMessages(self, _edPlugin, _strMethodCaller, _bFailure):
        """
        Propagates error messages from a plugin
        if _bFailure is true, this method has been called from retrieveFailureMessages
        in this case, checks for potential unexpected errors coming from the EDPluginExec
        """
        EDVerbose.DEBUG("EDPluginControl.retrieveErrorMessages")
        listErrorMessages = _edPlugin.getListOfErrorMessages()
        if (len(listErrorMessages) == 0) and (_bFailure is True):
            strErrorMessage = "%s : Adding Unexpected error" % _strMethodCaller
            EDVerbose.DEBUG(strErrorMessage)
            listErrorMessages.append(strErrorMessage)
        self.addErrorMessages(listErrorMessages)


    def retrieveWarningMessages(self, _edPlugin):
        """
        Propagates warning messages from a plugin
        """
        EDVerbose.DEBUG("EDPluginControl.retrieveWarningMessages")
        self.addWarningMessages(_edPlugin.getListOfWarningMessages())


    def appendExecutiveSummary(self, _edPlugin, _strPrefix="", _bAddSeparator=True):
        """
        Appends the executive summary from a plugin.
        """
        EDVerbose.DEBUG("EDPluginControl.appendExecutiveSummary")
        if (_bAddSeparator):
            self.addExecutiveSummarySeparator()
        for strLine in _edPlugin.getListExecutiveSummaryLines():
            if strLine == self.getExecutiveSummarySeparator() and _strPrefix != "":
                strLine = strLine[ :-len(_strPrefix) ]
            self.addExecutiveSummaryLine(_strPrefix + strLine)


    def addErrorWarningMessagesToExecutiveSummary(self, _strErrorMessage="Error messages:", _strWarningMessage="Warning messages:"):
        """
        Adds error and warning messages (if any) in the executive summary
        """
        if len(self.getListOfErrorMessages()) != 0:
            self.addExecutiveSummarySeparator()
            self.addExecutiveSummaryLine(_strErrorMessage)
            for strErrorMessage in self.getListOfErrorMessages():
                self.addExecutiveSummaryLine(strErrorMessage)
            self.addExecutiveSummarySeparator()
        if len(self.getListOfWarningMessages()) != 0:
            self.addExecutiveSummarySeparator()
            self.addExecutiveSummaryLine(_strWarningMessage)
            for warningMessage in self.getListOfWarningMessages():
                self.addExecutiveSummaryLine(warningMessage)
            self.addExecutiveSummarySeparator()


    def addPluginToActionCluster(self, _edPlugin):
        """
        This method adds a plugin instance to an action cluster.
        """
        if self.__edActionCluster == None:
            self.__edActionCluster = EDActionCluster()
        self.__edActionCluster.addAction(_edPlugin)
        self.__listOfLoadedPlugins.append(_edPlugin)


    def executeActionCluster(self):
        """
        This method executes the action cluster. The action cluster is executed
        asynchronoulsy.
        """
        if self.__iClusterSize != None:
            self.__edActionCluster.setClusterSize(self.__iClusterSize)
        self.__edActionCluster.execute()


    def synchronizeActionCluster(self):
        """
        This method synchronises the action cluster with the control plugin thread.
        """
        self.__edActionCluster.synchronize()


    def setClusterSize(self, _iClusterSize):
        """
        This method sets the size of the action cluster, i.e. the number of threads
        that will be executed simultaneously. 
        """
        self.__iClusterSize = _iClusterSize


    def executePlugin(self, _edPlugin, _bSynchronous=False):
        """
        This method is used to start executable plugins in pipeline asynchronously.
        """
        if _bSynchronous:
            self.executePluginSynchronous(_edPlugin)
        else:
            _edPlugin.execute()


    def executePluginSynchronous(self, _edPlugin):
        """
        This method is used to start executable plugins in pipeline synchronously.
        """
        _edControlSlotSUCCESS = EDSlot()
        _edControlSlotFAILURE = EDSlot()

        map(_edControlSlotSUCCESS.connect, _edPlugin.getSlotSUCCESS().getListMethod())
        map(_edControlSlotFAILURE.connect, _edPlugin.getSlotFAILURE().getListMethod())

        _edPlugin.getSlotSUCCESS().emptyListMethod()
        _edPlugin.getSlotFAILURE().emptyListMethod()

        _edPlugin.executeSynchronous()

        if (not _edPlugin.isFailure()):
            EDVerbose.DEBUG("EDControlPlugin.executeSynchronous slotSUCCESS")
            # Check that something doesn't go wrong in the success method!
            try:
                _edControlSlotSUCCESS.call(_edPlugin)

            except Exception:
                EDVerbose.DEBUG("EDControlPlugin.executeSynchronous: ERROR in slotSUCCESS!")
                EDVerbose.writeErrorTrace()
                _edPlugin.setFailure()

        if (_edPlugin.isFailure()):
            EDVerbose.DEBUG("EDControlPlugin.executeSynchronous slotFAILURE")
            # Check that something doesn't go wrong in the success method!
            try:
                _edControlSlotFAILURE.call(_edPlugin)

            except Exception:
                EDVerbose.DEBUG("EDControlPlugin.executeSynchronous: ERROR in slotFAILURE!")
                EDVerbose.writeErrorTrace()
