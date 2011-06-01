#!usr/bin/env PYTHON
#
#    Project: DiffractCTv1
#             http://www.edna-site.org
#
#    File: "$Id: $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Olof Svensson (svensson@esrf.fr)
#                      Jerome Kieffer (kieffer@estf.fr)
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

import os       as PyOs
import sys      as PySys
import time     as PyTime
#import ctypes   as PyCtypes


PyOs.environ[ "TANGO_HOST" ] = "mufid6:20000" 
print "TANGO_HOST= %s"%PyOs.environ[ "TANGO_HOST" ]
PyOs.environ[ "EDNA_HOME" ] = PyOs.path.split( PyOs.path.split( PyOs.path.split( PyOs.path.abspath(PySys.argv[0]) )[0] )[0] )[0]
print  "EDNA_HOME= %s"%PyOs.environ[ "EDNA_HOME" ] 
PyOs.environ[ "EDNA_SITE" ] = "ESRF"
print  "EDNA_SITE= %s"%PyOs.environ[ "EDNA_SITE" ]

TangoHome="/segfs/tango/release/"
LinuxVersion="redhate4_64"

if PyOs.path.isfile("/etc/redhat-release"):
    f=open("/etc/redhat-release").read().strip()
    if      f.find( "release 5" ) > 0: 
        LinuxVersion="redhate5_64"
        TangoHomeV = PyOs.path.join(TangoHome,LinuxVersion)
        PySys.path.append( PyOs.path.join(TangoHomeV,"PyTango/lib/python2.6/site-packages" ) )
    elif    f.find( "release 4" ) > 0: 
        LinuxVersion="redhate4_64"
        PySys.path.append( PyOs.path.join(TangoHome,LinuxVersion ) )

print "Linux Version: "+LinuxVersion

from PyTango import *
tangotest = DeviceProxy("id22/edna/1")
xml=None
tangotest.set_timeout_millis(60000)
print "Initializing EDNA: timeout = 60 secondes"
tangotest.command_inout("Start", ["EDPluginDCTWriteSinogramv1_0", '<?xml version="1.0" ?>\n<XSDataInputDiffractionCT>\n</XSDataInputDiffractionCT>\n' ] )

for i in PySys.argv[1:]:
    if PyOs.path.isfile( i ):
        print "Processing %s"%i
        fullpath=PyOs.path.abspath(i)
        print fullpath
#        xml= '<?xml version="1.0" ?>\n<XSDataInputDiffractionCT>\n<destinationDirectory>\n<path>\n<value>%s/tmp</value>\n</path>\n</destinationDirectory>\n<image>\n<path>\n<value>%s</value>\n</path>\n</image>\n<sinogramFileNamePrefix>\n<value>Test</value>\n</sinogramFileNamePrefix>\n</XSDataInputDiffractionCT>'%(PyOs.getenv("HOME"),fullpath)
        xml= '<XSDataInputWriteSinogram><integratedIntensities><path><value>%s</value></path></integratedIntensities><sinogramDirectory><path><value>%s</value></path></sinogramDirectory><sinogramFileNamePrefix><value>Only</value></sinogramFileNamePrefix></XSDataInputWriteSinogram>'%(fullpath, PyOs.path.join(PyOs.getenv("HOME"),"tmp/SinogramOnly") )
        result= tangotest.command_inout("Start", ["EDPluginDCTWriteSinogramv1_0", xml ] )
 #       PyTime.sleep(0.1)
 