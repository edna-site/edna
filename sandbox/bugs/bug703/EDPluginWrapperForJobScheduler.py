# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDPluginExec.py 2646 2010-12-21 13:17:50Z kieffer $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

from EDPlugin import EDPlugin
from EDUtilsParallel import EDUtilsParallel
from EDVerbose import EDVerbose
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDUtilsPath import EDUtilsPath
from EDServerXMLRCP import EDServerXMLRCP


import xml.dom.minidom, time
from xml.dom.minidom import Node


class EDPluginWrapperForJobScheduler(EDPlugin):
    """
    Wrapper for executing EDPlugins through job schedulers like OAR, Condor etc.
    """
    def __init__(self, _strNameOfPlugin):
        EDPlugin.__init__(self)
        self.__strNameOfPlugin = _strNameOfPlugin
        EDFactoryPluginStatic.loadModule(_strNameOfPlugin)
        self.__dictXMLDataInput = {}
        self.__dictXMLDataOutput = {}
        self.__strPythonWrapperScriptName = "pluginWrapperForJobScheduler.py"
        self.__strPathToPythonWrapper = None
        self.__edServerXMLRCP = EDServerXMLRCP.getInstance()
        self.__edServerXMLRCP.registerPlugin(self)
        self.__bFinished = False


    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginWrapperForJobScheduler.preProcess")
        # Construct python script for executing the plugin
        strPythonWrapper = self.preparePythonWrapperScript()
        self.__strPathToPythonWrapper = os.path.join(self.getWorkingDirectory(), self.__strPythonWrapperScriptName)
        EDUtilsFile.writeFile(self.__strPathToPythonWrapper, strPythonWrapper)


    def process(self, _edObject=None):
        EDPlugin.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginWrapperForJobScheduler.process")
        #print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        EDVerbose.DEBUG("Executing: oarsub \"python %s\"" % self.__strPathToPythonWrapper)
        os.system("oarsub -l \"{cpu_vendor='INTEL'}/core=1\" \"python %s\"" % self.__strPathToPythonWrapper)
        #os.system("python %s" % self.__strPathToPythonWrapper)
#        if os.path.exists(os.path.join(self.getWorkingDirectory(), "SUCCESS.txt")):
#            #print "SUCCESS!"
#            strDataOutput = EDUtilsFile.readFile(os.path.join(self.getWorkingDirectory(), "SUCCESS.txt"))
#            for strLine in strDataOutput.split("\n"):
#                if strLine != "":
#                    strXML = EDUtilsFile.readFile(os.path.join(self.getWorkingDirectory(), "XSDataResult_" + strLine + ".xml"))
#                    if strLine == self.getDefaultOutputDataKey():
#                        self.setDataOutput(strXML)
#                    else:
#                        self.setDataOutput(strXML, strLine)
#        elif os.path.exists(os.path.join(self.getWorkingDirectory(), "FAILURE.txt")):
#            #print "FAILURE!"
#            self.setFailure()



    def finallyProcess(self, _edObject=None):
        EDPlugin.finallyProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginWrapperForJobScheduler.finallyProcess")
        while not self.__bFinished:
            time.sleep(1)



    def callSUCCESS(self, _listSuccessMessages):
        print "SUCCESS!", _listSuccessMessages
        self.__bFinished = True


    def callFAILURE(self, _listFailureMessages):
        print "FAILURE!", _listFailureMessages
        self.__bFinished = True
        self.setFailure()

    
    def setDataInput(self, _oDataInput, _strDataInputKey=None):
        """
        Sets the plugin input data.
        _oDataInput could be either an String XML or an XSData object.
        """
        EDVerbose.DEBUG("EDPluginWrapperForJobScheduler.setDataInput")
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.getDefaultInputDataKey()
        # Allow for None input
        if (_oDataInput is None):
            EDVerbose.DEBUG("EDPlugin.setDataInput: Data input is None")
            self.__dictXMLDataInput[ strDataInputKey ] = []
        else:
            # Check the type
            strXMLDataInput = None
            if isinstance(_oDataInput, (str, unicode)):
                EDVerbose.DEBUG("EDPlugin.setDataInput: Input Data is string ")
                strXMLDataInput = _oDataInput
            else:
                try:
                    strXMLDataInput = _oDataInput.marshal()
                except BaseException, e:
                    strErrorMessage = "ERROR: EDPluginWrapperForJobScheduler.setDataInput, cannot marshal data input object"
                    EDVerbose.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    raise RuntimeError, strErrorMessage
            # Add the object to a list if its key is not the default key
            if (strDataInputKey != self.getDefaultInputDataKey()) :
                # Check if there's already a list stored
                if (not strDataInputKey in self.__dictXMLDataInput.keys()):
                    self.__dictXMLDataInput[ strDataInputKey ] = []
                self.__dictXMLDataInput[ strDataInputKey ].append(strXMLDataInput)
            else:
                self.__dictXMLDataInput[ strDataInputKey ] = strXMLDataInput


    def getDataInput(self, _strDataInputKey=None):
        """
        Returns the Plugin Input Data for a particular key.
        If the key is not provided a default key is used.
        """
        oValue = None
        strDataInputKey = _strDataInputKey
        if (strDataInputKey is None):
            strDataInputKey = self.getDefaultInputDataKey()
        if (strDataInputKey in self.__dictXMLDataInput.keys()):
            oValue = self.__dictXMLDataInput[ strDataInputKey ]
        else:
            strErrorMessage = self.getPluginName() + ".getDataInput, no input data defined for key: " + strDataInputKey
            EDVerbose.warning(strErrorMessage)
            self.addWarningMessage(strErrorMessage)
        if isinstance(oValue, (str, unicode)):
            oValue = self.xsDataXmlToObject(oValue)
        return oValue


    def setDataOutput(self, _xsDataOutput, _strDataOutputKey=None):
        """
        Sets the plugin output data for a particular key.
        If the key is not provided a default key is used.

        If the key is already defined in the dictionary, the corresponding
        data object is added to a list which contains the already stored object(s).
        """
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.getDefaultOutputDataKey()
        # Add the object to a list if its key not the default key 
        if (strDataOutputKey == self.getDefaultOutputDataKey()):
            self.__dictXMLDataOutput[ strDataOutputKey ] = _xsDataOutput
        else:
            # Check if the _xsDataoutput object is already a list
            if (type(_xsDataOutput) == type ([])):
                self.__dictXMLDataOutput[ strDataOutputKey ] = _xsDataOutput
            else:
                # Check if the stored object contains already a list
                if (not strDataOutputKey in self.__dictXMLDataOutput.keys()):
                    self.__dictXMLDataOutput[ strDataOutputKey ] = []
                self.__dictXMLDataOutput[ strDataOutputKey ].append(_xsDataOutput)


    def getDataOutput(self, _strDataOutputKey=None):
        """
        Returns the Plugin Output Data
        """
        oValue = None
        strDataOutputKey = _strDataOutputKey
        if (strDataOutputKey is None):
            strDataOutputKey = self.getDefaultOutputDataKey()
        if (strDataOutputKey in self.__dictXMLDataOutput.keys()):
            oValue = self.__dictXMLDataOutput[ strDataOutputKey ]
        if isinstance(oValue, (str, unicode)):
            oValue = self.xsDataXmlToObject(oValue)
        #print oValue
        return oValue


    def xsDataXmlToObject(self, strXML):
        #print "========================================================"
        #print strXML
        #print sys.modules[self.__strNameOfPlugin]
        #print dir(sys.modules[self.__strNameOfPlugin])
        pyDom = xml.dom.minidom.parseString(strXML)
        xsDataClassName = pyDom.firstChild.nodeName
        XSDataClass = getattr(sys.modules[self.__strNameOfPlugin], xsDataClassName)
        oValue = XSDataClass.parseString(strXML)
        #print oValue
        return oValue



    def preparePythonWrapperScript(self):
        listScript = ["#!%s" % sys.executable, ""]
        listScript += ["import os, sys, xmlrpclib"]
        listScript += ["""pyXmlrcplibProxy = xmlrpclib.ServerProxy('http://%s:%d')""" % (self.__edServerXMLRCP.getHost(), self.__edServerXMLRCP.getPort())]
        listScript += ["""os.chdir("%s")""" % self.getWorkingDirectory()]
        listScript += ["""os.environ['EDNA_HOME']="%s" """ % EDUtilsPath.getEdnaHome()]
        listScript += ["""os.environ['EDNA_SITE']="%s" """ % EDUtilsPath.getEdnaSite()]
        listScript += ["""sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))"""]
        listScript += ["""from EDFactoryPluginStatic import EDFactoryPluginStatic"""]
        listScript += ["""from EDUtilsFile import EDUtilsFile"""]
        listScript += ["""edPlugin = EDFactoryPluginStatic.loadPlugin("%s")""" % self.__strNameOfPlugin]
        for strValue in self.__dictXMLDataInput:
            if strValue == self.getDefaultInputDataKey():
                listScript += ["edPlugin.setDataInput(\"\"\"%s\"\"\")""" % self.__dictXMLDataInput[strValue]]
            else:
                listScript += ["edPlugin.setDataInput(\"\"\"%s\"\"\", \"%s\")" % (self.__dictXMLDataInput[strValue], strValue)]
        listScript += ["""def actionSuccessFile(_edPlugin=None):"""]
        listScript += ["""    strSuccessMessage = "" """]
        listScript += ["""    for strKey in _edPlugin.getListOfDataOutputKeys():"""]
        listScript += ["""        if strKey == _edPlugin.getDefaultOutputDataKey():"""]
        listScript += ["""            strXMLOutput = _edPlugin.getDataOutput().marshal()"""]
        listScript += ["""            strSuccessMessage += strKey + "\\n" """]
        listScript += ["""            EDUtilsFile.writeFile(os.path.join("%s", "XSDataResult_"+strKey+".xml"), strXMLOutput)""" % self.getWorkingDirectory()]
        listScript += ["""        else:"""]
        listScript += ["""            iIndex = 1"""]
        listScript += ["""            for xsDataResult in _edPlugin.getDataOutput(strKey):"""]
        listScript += ["""                strXMLOutput = xsDataResult.marshal()"""]
        listScript += ["""                strSuccessMessage += "%s_%d\\n" % (strKey, iIndex) """]
        listScript += ["""                EDUtilsFile.writeFile(os.path.join("%s", "XSDataResult_"+strKey+"_%%d.xml") %% iIndex, strXMLOutput)""" % self.getWorkingDirectory()]
        listScript += ["""                 """]
        listScript += ["""    EDUtilsFile.writeFile(os.path.join("%s", "SUCCESS.txt"), strSuccessMessage)""" % self.getWorkingDirectory()]
        listScript += ["""def actionSuccessXMLRCP(_edPlugin=None):"""]
        listScript += ["""    pyXmlrcplibProxy.callbackSUCCESS("%d", [])""" % self.getId()]
        listScript += ["""    for strKey in _edPlugin.getListOfDataOutputKeys():"""]
        listScript += ["""        strXMLOutput = _edPlugin.getDataOutput().marshal()"""]
        listScript += ["""        pyXmlrcplibProxy.setDataOutput("%d", strXMLOutput)""" % self.getId()]
        listScript += ["""def actionFailure(_edObject=None):"""]
        listScript += ["""    pyXmlrcplibProxy.callbackFAILURE("%d", [])""" % self.getId()]
        listScript += ["""#edPlugin.connectSUCCESS(actionSuccessFile)"""]
        listScript += ["""edPlugin.connectSUCCESS(actionSuccessXMLRCP)"""]
        listScript += ["""edPlugin.connectFAILURE(actionFailure)"""]
        listScript += ["""edPlugin.executeSynchronous()"""]
        listScript += [""]
        listScript += [""]
        strPythonWrapper = ""
        for strLine in listScript:
            strPythonWrapper = strPythonWrapper + strLine + "\n"
        return strPythonWrapper
