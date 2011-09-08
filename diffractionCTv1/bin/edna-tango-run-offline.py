#/usr/bin/env PYTHON
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

"""

"""
__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3"
__date__ = "2010-06-29"
__copyright__ = "ESRF"

import os, time, sys

os.environ[ "TANGO_HOST" ] = "mufid2:20000"
print "TANGO_HOST= %s" % os.environ[ "TANGO_HOST" ]
os.environ[ "EDNA_HOME" ] = os.path.split(os.path.split(os.path.abspath(sys.argv[0]))[0])[0]
print  "EDNA_HOME= %s" % os.environ[ "EDNA_HOME" ]
os.environ[ "EDNA_SITE" ] = "ESRF"
print  "EDNA_SITE= %s" % os.environ[ "EDNA_SITE" ]

TangoHome = "/segfs/tango/release/"
LinuxVersion = "redhate4_64"

if os.path.isfile("/etc/redhat-release"):
    f = open("/etc/redhat-release").read().strip()
    if      f.find("release 5") > 0:
        LinuxVersion = "redhate5_64"
        TangoHomeV = os.path.join(TangoHome, LinuxVersion)
        sys.path.append(os.path.join(TangoHomeV, "PyTango/lib/python2.6/site-packages"))
    elif    f.find("release 4") > 0:
        LinuxVersion = "redhate4_64"
        sys.path.append(os.path.join(TangoHome, LinuxVersion))

print "Linux Version: " + LinuxVersion

from PyTango import *
tangotest = DeviceProxy("id22/edna/1")
xml = None
tangotest.set_timeout_millis(60000)
print "Initializing EDNA: timeout = 60 secondes"
tangotest.command_inout("Start", ["EDPluginControlDiffractionCTv1_0", '<?xml version="1.0" ?>\n<XSDataInputDiffractionCT>\n</XSDataInputDiffractionCT>\n' ])


pylArv = []
for i in sys.argv[1:]:
    if os.path.isfile(i):
        if os.path.splitext(i)[1] == ".edf":
            pylArv.append(os.path.realpath(i))
    if os.path.isdir(i):
        for f in os.listdir(i):
             if os.path.splitext(f)[1] == ".edf":
                 pylArv.append(os.path.realpath(os.path.join(i, f)))

for i in pylArv:
    if os.path.isfile(i):
        print "Processing %s" % i
        fullpath = os.path.abspath(i)
        xml = '<?xml version="1.0" ?>\n<XSDataInputDiffractionCT>\n<destinationDirectory>\n<path>\n<value>%s/tmp</value>\n</path>\n</destinationDirectory>\n<image>\n<path>\n<value>%s</value>\n</path>\n</image>\n<sinogramFileNamePrefix>\n<value>Test</value>\n</sinogramFileNamePrefix>\n<powderDiffractionSubdirectory><value>test_CIF_line_</value></powderDiffractionSubdirectory></XSDataInputDiffractionCT>' % (os.getenv("HOME"), fullpath)
        result = tangotest.command_inout("Start", ["EDPluginControlDiffractionCTv1_0", xml ])
#        time.sleep(1)

