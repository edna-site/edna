#!/usr/bin/env python
# coding: utf8

from __future__ import with_statement

__authors__ = [ "Jérôme Kieffer"]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110920"
__status__ = "beta"
__doc__ = """Usage: 

$ tango_client -xml=xml_file.xml  -device=DAU/edna/1 -plugin=EDPluginName -delay=0.1 *.edf


"""

import sys, os, time

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
delay = 0
if len(sys.argv) == 1:
        print __doc__
        sys.exit(1)

for arg in sys.argv[1:]:
    if arg.find("-h") in [0, 1]:
        print __doc__
        sys.exit(1)
    elif arg.find("-device=") in [0, 1]:
        device = arg.split("=", 1)[1]
    elif arg.find("-plugin=") in [0, 1]:
        plugin = arg.split("=", 1)[1]
    elif arg.find("-xml=") in [0, 1]:
        xmlfile = arg.split("=", 1)[1]
        if os.path.isfile(xmlfile):
            xml = open(xmlfile).read()
    elif arg.find("-delay=") in [0, 1]:
        delay = float(arg.split("=", 1)[1])
    elif os.path.isfile(arg):
        filenames.append(os.path.abspath(arg))

edna = PyTango.DeviceProxy(device)

edna.initPlugin(plugin)
t0 = time.time()
totaltime = 0.0
listjobs = []
if filenames:
    for fn in filenames:
        dirname, filename = os.path.split(fn)
        basename, ext = os.path.splitext(filename)
        myXML = xml.replace("${FULLNAME}", fn).replace("${FILENAME}", filename).replace("${DIRNAME}", dirname).replace("${BASENAME}", basename).replace("${EXT}", ext)
        t1 = time.time()
        pid = edna.startJob([plugin, myXML])
        deltat = time.time() - t1
        totaltime += deltat
        listjobs.append(pid)
        print "%s | Total Time:\t%.3fs /Tango %.3fs\tLast Tango:\t%.3f" % (pid, time.time() - t0, totaltime, deltat)
        time.sleep(delay)
else:
    pid = edna.startJob([plugin, xml])
    print "%s | Tango time: %.3fs" % (pid, time.time() - t0)
    listjobs.append(pid)

#for job in listjobs:
#    print edna.getJobState(job)

print edna.statistics()


