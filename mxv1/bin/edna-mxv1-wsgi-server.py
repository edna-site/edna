#!/usr/bin/env python
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) DLS
#
#    Principal author: irakli 
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

#
# Set up PYTHON path for the EDNA kernel
#
# First locate EDNA_HOME and EDNA_SITE
#
import sys, os.path, glob, shlex

pyStrProgramPath = sys.argv[0]
pyStrBinPath = os.path.split(pyStrProgramPath)[0]
pyStrMXv1Path = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrMXv1Path)[0]
pyStrEdnaSite = 'SDANoQSubDLS'
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
os.environ["EDNA_SITE"] = pyStrEdnaSite
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA MXv1 characterisation application:"
    print "Make sure that $EDNA_SITE is set up before running edna-mxv1-characterisation."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print "Please read the INSTALL.txt file under the \"$EDNA_HOME/mxv1\" directory for more details"
    print ""
    sys.exit(1)
strConfigurationFilePath = os.path.join(pyStrEdnaHomePath, "mxv1", "conf", "XSConfiguration_" + os.environ["EDNA_SITE"] + ".xml")
#
# Then add kernel/src and mxv1/src to PYTHONPATH
#
sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "mxv1", "src"))

import bottle, cherrypy
from bottle import CherryPyServer, route, run, debug, request, send_file
from cherrypy import wsgiserver

from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile
from EDConfiguration import EDConfiguration
from EDFactoryPluginStatic import EDFactoryPluginStatic
from XSDataCommon import XSDataString
from EDApplicationMXv1Characterisation import EDApplicationMXv1Characterisation
from XSDataMXv1 import XSDataInputCharacterisation

@route('/sda', method='POST')
def runMXv1Pipeline():
    strLogFileName = os.path.join(returnWorkingDirectory(), "wsgi-server.log")
    EDVerbose.setLogFileName(strLogFileName)
    strInput = str(request['wsgi.input'].read(int(request['CONTENT_LENGTH'])))
    if strInput:
        # Take the parameters string, split off the title and run the bash script to generate the input char. XML  
        listParams = shlex.split(strInput)
        strComments = listParams[0]          # the 1st item
        strShortComments = listParams[1]     # the 2nd item
        strWorkingDir = listParams[2]        # the 3rd item
        strHTMLResultDir = listParams[3]     # the 4th item 
        
        os.chdir(strWorkingDir)
        
        strParamString = " ".join(listParams[4:])     # all but the first four items 
        edPluginMxv1ParamsToXML = EDFactoryPluginStatic.loadPlugin('EDPluginMxv1ParamsToXMLv1_0')
        edPluginMxv1ParamsToXML.setDataInput(XSDataString(strParamString), "paramString")
        edPluginMxv1ParamsToXML.executeSynchronous()
        xsDataFile = edPluginMxv1ParamsToXML.getDataOutput()

        # Read the XML and parse it into an object hierarchy        
        strXMLFile = xsDataFile.getPath().getValue()
        f = open(strXMLFile, 'r')
        xml = f.read()
        f.close()
        xsDataInputCharacterisation = XSDataInputCharacterisation.parseString(xml)

        # Run the MXv1 application pipeline
        edApplicationMXv1Characterisation = EDApplicationMXv1Characterisation(_strPluginName="EDPluginControlInterfacev1_2", \
                               _strConfigurationFileName=strConfigurationFilePath, \
                               _xsDataInputCharacterisation=xsDataInputCharacterisation, \
                               _strComments=strComments, \
                               _strShortComments=strShortComments)
        edApplicationMXv1Characterisation.execute()

        # Run the EDNA2HTML generator on the output from the MXv1 application 
        edPluginExecOutputHTML = EDFactoryPluginStatic.loadPlugin('EDPluginExecOutputHTMLv1_0')
        edPluginExecOutputHTML.setDataInput(XSDataString(strComments), "title")
        strWorkingDir = os.path.join(strWorkingDir, edApplicationMXv1Characterisation.getWorkingDir())
        edPluginExecOutputHTML.setDataInput(XSDataString(strWorkingDir), "workingDir")
        #strBaseDir = os.path.join(strHTMLResultDir, "edna")
        #edPluginExecOutputHTML.setDataInput(XSDataString(strBaseDir), "basename")
        edPluginExecOutputHTML.setDataInput(XSDataString(strHTMLResultDir), "basename")

        edPluginExecOutputHTML.executeSynchronous()
        
        strPathToHTMLFile = ""
        if (edPluginExecOutputHTML.hasDataOutput("htmlFile")):
            strPathToHTMLFile = edPluginExecOutputHTML.getDataOutput("htmlFile")[0].getPath().getValue()
        else:
            EDVerbose.ERROR("edna-mxv1-wsgi-server: edPluginExecOutputHTML has no dataOutput htmlFile!")
            
        if strPathToHTMLFile =="":
            EDVerbose.ERROR("edna-mxv1-wsgi-server: Returning empty string")
        return strPathToHTMLFile
    else:
        return strInput

    
@route('/directory')
def returnWorkingDirectory():
    return os.getcwd(); 

@route('/test')
def test():
    return 'WSGI server running!'

@route('/shutdown')
def shutdown():
    server.stop()
    # Find more graceful way to send shutdown message
    bottle.abort(200, "WSGI server is shutting down...")
    exit()


server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8081), bottle.default_app())
server.start()

