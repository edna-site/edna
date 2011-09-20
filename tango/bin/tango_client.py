#!/usr/bin/env python
# coding: utf8

from __future__ import with_statement

__authors__ = [ "Jérôme Kieffer"]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110919"
__status__ = "development"
__doc__ = """Usage: 

$ tango_client -xml=xml_file.xml  -d=DAU/edna/1 -p=EDPluginName *.edf


"""

import sys, os, threading, time

import os
if "TANGO_HOST" not in os.environ:
    raise RuntimeError("No TANGO_HOST defined")
import PyTango

# Append the EDNA kernel source directory to the python path

if not os.environ.has_key("EDNA_HOME"):
    strProgramPath = os.path.abspath(sys.argv[0])
    lPath = strProgramPath.split(os.sep)
    if len(lPath) > 3:
        strEdnaHomePath = os.sep.join(lPath[:-3])
    else:
        raise RuntimeError("Problem in the EDNA_HOME path ... %s" % strEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

device = None
xml = None
filenames = []
plugin = None
if len(sys.argv) == 1:
        print __doc__
        sys.exit(1)

for arg in sys.argv[1:]:
    if arg.find("-h") in [0, 1]:
        print __doc__
        sys.exit(1)
    elif arg.find("-d=") in [0, 1]:
        device = arg.split("=", 1)[1]
    elif arg.find("-p=") in [0, 1]:
        plugin = arg.split("=", 1)[1]
    elif arg.find("-xml=") in [0, 1]:
        xmlfile = arg.split("=", 1)[1]
        if os.path.isfile(xmlfile):
            xml = open(xmlfile).read()
    elif os.path.isfile(arg):
        filenames.append(os.path.abspath(arg))

edna = PyTango.DeviceProxy(device)

edna.initPlugin(plugin)
t0 = time.time()
t1 = t0
for fn in filenames:
    dirname, filename = os.path.split(fn)
    basename, ext = os.path.splitext(filename)
    myXML = xml.replace("${FULLNAME}", fn).replace("${FILENAME}", filename).replace("${DIRNAME}", dirname).replace("${BASENAME}", basename).replace("${EXT}", ext)
    pid = edna.startJob([plugin, myXML])
    print "%s | Total:\t%.3f\tLast:\t%.3f" % (pid, time.time() - t0, time.time() - t1)
    t1 = time.time()
