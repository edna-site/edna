#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDActionCluster.py 1498 2010-05-06 15:47:43Z kieffer $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import threading, time, socket

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from EDObject import EDObject
from EDVerbose import EDVerbose



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class EDServerXMLRCP(EDObject, threading.Thread):

    __edServerXMLRCP = None
    __semaphore = threading.Semaphore()
    __server = None

    def __init__(self):
        EDObject.__init__(self)
        threading.Thread.__init__(self)
        self.__dictPlugin = {}
        #self.__strHost = socket.get
        self.__strHost = socket.gethostbyname_ex(socket.gethostname())[2][0]
        self.__iPort = 8000


    @staticmethod
    def getInstance():
        EDServerXMLRCP.__semaphore.acquire()
        if EDServerXMLRCP.__edServerXMLRCP == None:
            EDServerXMLRCP.__edServerXMLRCP = EDServerXMLRCP()
            EDServerXMLRCP.__edServerXMLRCP.start()
            time.sleep(1)
        EDServerXMLRCP.__semaphore.release()
        return EDServerXMLRCP.__edServerXMLRCP


    def callbackSUCCESS(self, _strPluginId, _listSUCCESSMessages):
        EDVerbose.DEBUG("EDServerXMLRCP.callbackSUCCESS: %s" % _strPluginId)
        if _strPluginId in self.__dictPlugin.keys():
            edPluginWrapper = self.__dictPlugin[_strPluginId]
            edPluginWrapper.callSUCCESS(_listSUCCESSMessages)


    def callbackFAILURE(self, _strPluginId, _listFAILUREMessages):
        EDVerbose.DEBUG("EDServerXMLRCP.callbackFAILURE: %s" % _strPluginId)
        if _strPluginId in self.__dictPlugin.keys():
            edPluginWrapper = self.__dictPlugin[_strPluginId]
            edPluginWrapper.callFAILURE(_listFAILUREMessages)


    def setDataOutput(self, _strPluginId, _strXML, _strKey=None):
        EDVerbose.DEBUG("EDServerXMLRCP.setDataOutput: %s" % _strPluginId)
        if _strPluginId in self.__dictPlugin.keys():
            edPluginWrapper = self.__dictPlugin[_strPluginId]
            edPluginWrapper.setDataOutput(_strXML, _strKey)


    def registerPlugin(self, _edPlugin):
        EDVerbose.DEBUG("EDServerXMLRCP.registerPlugin: %s" % _edPlugin.getId())
        EDServerXMLRCP.__semaphore.acquire()
        strPluginId = str(_edPlugin.getId())
        self.__dictPlugin[strPluginId] = _edPlugin
        EDServerXMLRCP.__semaphore.release()


    def unRegisterPlugin(self, _edPlugin):
        EDVerbose.DEBUG("EDServerXMLRCP.registerPlugin: %s" % _edPlugin.getId())
        EDServerXMLRCP.__semaphore.acquire()
        strPluginId = str(_edPlugin.getId())
        if strPluginId in self.__dictPlugin.keys():
            del self.__dictPlugin[strPluginId]
        EDServerXMLRCP.__semaphore.release()


    def getRegisteredPlugin(self, _strPluginId):
        EDVerbose.DEBUG("EDServerXMLRCP.registerPlugin: %s" % _strPluginId)
        EDServerXMLRCP.__semaphore.acquire()
        oValue = None
        if _strPluginId in self.__dictPlugin.keys():
            oValue = self.__dictPlugin[_strPluginId]
        EDServerXMLRCP.__semaphore.release()
        return oValue


    def shutdown(self):
        EDVerbose.DEBUG("EDServerXMLRCP.shutdown")
        EDServerXMLRCP.__semaphore.acquire()
        EDServerXMLRCP.__server.shutdown()
        EDServerXMLRCP.__semaphore.release()


    def run(self):
        # Create server
        EDVerbose.DEBUG("EDServerXMLRCP.run, host = %s, port = %d" % (self.__strHost, self.__iPort))
        EDServerXMLRCP.__server = SimpleXMLRPCServer((self.__strHost, self.__iPort),
                                    requestHandler=RequestHandler, allow_none=1)
        EDServerXMLRCP.__server.register_introspection_functions()
        EDServerXMLRCP.__server.register_function(pow)
        EDServerXMLRCP.__server.register_function(self.callbackSUCCESS, 'callbackSUCCESS')
        EDServerXMLRCP.__server.register_function(self.callbackFAILURE, 'callbackFAILURE')
        EDServerXMLRCP.__server.register_function(self.setDataOutput, 'setDataOutput')
        # Run the server's main loop
        EDServerXMLRCP.__server.serve_forever()


    def getHost(self):
        return self.__strHost

    def getPort(self):
        return self.__iPort

        