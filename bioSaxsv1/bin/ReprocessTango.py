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

$ ${EDNA_HOME}/bioSaxsv1/bin/ReprocessTango.py  -device=DAU143/edna/1 -plugin=EDPluginName -mask=myMask/Pcon.edf -delay=0.1 *.xml


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
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsProcessOneFilev1_0
device = None
xml = None
listXml = []
filenames = []
plugin = None
delay = 0
mask = None
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
    elif arg.find("-mask=") in [0, 1]:
        mask = os.path.abspath(arg.split("=", 1)[1])
    elif arg.find("-xml=") in [0, 1]:
        xmlfile = arg.split("=", 1)[1]
        if os.path.isfile(xmlfile):
            if xml is None:
                xml = open(xmlfile).read()
                listXml.append(xml)
            else:
                listXml.append(open(xmlfile).read())
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
    reprocessDirname = "reprocess-%s" % time.strftime("%Y%m%d-%Hh%M", time.localtime())
    for fn in filenames:
        if fn.endswith(".xml"):
            dirname, xmlbase = os.path.split(fn)
            xsd = XSDataInputBioSaxsProcessOneFilev1_0.parseFile(fn)
            if xsd.experimentSetup is None:
                print("XML file %s is not a good XSD file")
                continue
            xsd.experimentSetup.maskFile.path.value = mask
            oldRawdir, rawfile = os.path.split(xsd.rawImage.path.value)
            newraw = os.path.join(dirname, rawfile)
            if not os.path.isfile(newraw):
                print("new raw %s does dot exist: skipping !!!" % newraw)
                continue
            xsd.rawImage.path.value = newraw
            oldbase = os.path.dirname(oldRawdir)
            newbase = os.path.join(os.path.dirname(dirname), reprocessDirname)
            xmldir = os.path.join(newbase, "raw")
            if not os.path.isdir(newbase):
                os.makedirs(xmldir)

            xsd.logFile.path.value = xsd.logFile.path.value.replace(oldbase, newbase)
            xsd.normalizedImage.path.value = xsd.normalizedImage.path.value.replace(oldbase, newbase)
            xsd.integratedImage.path.value = xsd.integratedImage.path.value.replace(oldbase, newbase)
            xsd.integratedCurve.path.value = xsd.integratedCurve.path.value.replace(oldbase, newbase)
            xsd.exportToFile(os.path.join(xmldir, xmlbase))
            myXML = xsd.marshal()
            t1 = time.time()
            pid = edna.startJob([plugin, myXML])
            deltat = time.time() - t1
            totaltime += deltat
            listjobs.append(pid)
            print "%s | Total Time:\t%.3fs /Tango %.3fs\tLast Tango:\t%.3f" % (pid, time.time() - t0, totaltime, deltat)
            time.sleep(delay)
        else:
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
    for xml in listXml:
        pid = edna.startJob([plugin, xml])
        print "%s | Tango time: %.3fs" % (pid, time.time() - t0)
        listjobs.append(pid)

while edna.getJobState(listjobs[-1]) not in ["success", "failure"]:
    time.sleep(1)
#for job in listjobs:
#    print edna.getJobState(job)

edna.collectStatistics()
print edna.getStatistics()
