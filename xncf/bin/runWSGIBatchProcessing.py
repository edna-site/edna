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
import sys, os.path, glob

pyStrProgramPath = sys.argv[0]
pyStrBinPath = os.path.split(pyStrProgramPath)[0]
pyStrXNCFPath = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrXNCFPath)[0]
pyStrEdnaSite = 'DLS_local'
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
os.environ["EDNA_SITE"] = pyStrEdnaSite
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA xncf pipeline:"
    print "Make sure that $EDNA_SITE is set up before running xncf-pipeline."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print ""
    sys.exit(1)
    
strConfigurationFilePath = os.path.join(pyStrEdnaHomePath, "xncf", "conf", "XSConfiguration_" + os.environ["EDNA_SITE"] + ".xml")
#
# Then add kernel/src, xncf/src and xncf plugins source directories to PYTHONPATH
#

sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "src"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginControlXAFSDataBatchProcessing-v0.1","plugins"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginControlXAFSDataProcessing-v0.1","plugins"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginExecIfeffit-v0.1","plugins"))
sys.path.append(os.path.join(pyStrEdnaHomePath, "xncf", "plugins", "EDPluginExecIfeffit-v0.1","plugins"))

import bottle, cherrypy
from bottle import CherryPyServer, route, run, debug, request, send_file
from cherrypy import wsgiserver

from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic

@route('/run', method='GET')
def runXAFSProcessing():
    if request.GET.get('nxs', '').strip():
        _dataPattern = request.GET.get('nxs', '').strip()
        _dataPattern = '/'.join(_dataPattern.split('\\\\'))
        print _dataPattern
        _strDatasetFileNames = [os.path.abspath(tmp) for tmp in filter(lambda tmp: os.path.isfile(tmp), glob.glob(_dataPattern))]
        if (_strDatasetFileNames is not None):
            for _tmpName in _strDatasetFileNames:
                EDVerbose.screen("Reading input data from : %s" % _tmpName)
        else:
            return edApplicationXAFSBatchProcessing.usage()
            
        edApplicationXAFSBatchProcessing.setDatasetFileNames(_strDatasetFileNames)
        
        edApplicationXAFSBatchProcessing.execute()
        #return os.path.abspath(edApplicationXAFSBatchProcessing.getXAFSPlugin().getWorkingDirectory())
        return os.path.join(os.path.abspath(edApplicationXAFSBatchProcessing.getXAFSPlugin().getWorkingDirectory()), 'results.nxs')
    else:
        return edApplicationXAFSBatchProcessing.usage()


@route('/sda', method='POST')
def runXAFSPipeline():
    xmlXSDataInput = str(request['wsgi.input'].read(int(request['CONTENT_LENGTH'])))
    if xmlXSDataInput:
        edPluginControlXAFSDataProcessing = EDFactoryPluginStatic.loadPlugin('EDPluginControlXAFSDataBatchProcessingv0_1')
        edPluginControlXAFSDataProcessing.setDataInput(xmlXSDataInput)
        edPluginControlXAFSDataProcessing.executeSynchronous()
        
        return os.path.join(edPluginControlXAFSDataProcessing.getWorkingDirectory(), \
                            edPluginControlXAFSDataProcessing.returnResultsFilename())
    else:
        return xmlXSDataInput

    
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



server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8080), bottle.default_app())
server.start()

