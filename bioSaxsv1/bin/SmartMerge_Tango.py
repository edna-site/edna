#!/usr/bin/env python
# coding: utf8

from __future__ import with_statement

__authors__ = [ "Jérôme Kieffer"]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120105"
__status__ = "beta"
__doc__ = """Usage: 

$ ${EDNA_HOME}/bioSaxsv1/bin/SmartMerge_Tango.py  -device=DAU143/edna/1 [-range=1-10] [-rdabs=1e-6] [-rdrel=1e-6] [-out=file_ave.dat] [-sub=file_sub.dat] *.dat

options:
* -device: the name of the tango device server
* -range: the range of frames to merge (by default all)  
* -rdabs: lower limit for similarity (radiation damage estimation) with first image in the serie
* -rdrel: lower limit for similarity (radiation damage estimation) with previous image in the serie
* -out:   force the name of the output file
* -sub:   force the name of the background subtracted output file (warning: this dependents on the order of processing !!!) 
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
from XSDataCommon import XSDataDouble, XSDataFile, XSDataString
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsSmartMergev1_0




def getInteger(astr):
    try:
        j = int(astr)
    except ValueError, error:
        print("%s: %s is not an integer" % (error, i))
    else:
        return j

def getRange(astr):
    """
    transforms a chain like "1,5-6" in [1,5,6]
    """
    filerange = []
    for i in arg.split("=", 1)[1].split(","):
        if "-" in i:
            lstLim = i.split("-")
            minv = getInteger(lstLim[0])
            maxv = getInteger(lstLim[1])
            if minv and maxv:
                filerange += range(minv, maxv + 1)
        else:
            j = getInteger(i)
            if j is not None:
                filerange.append(j)
    filerange.sort()
    return filerange

def getCommon(str1, str2):
    """
    return the common part of two strings
    """
    out = ""
    for i, j in zip(str1, str2):
        if i == j:
            out += i
        else:
            return out
    return out


if __name__ == "__main__":
    device = None
    filerange = None
    rdabs = None
    rdrel = None
    outFile = None
    subFile = None
    #xml = None
    listXml = []
    filenames = []
    plugin = "EDPluginBioSaxsSmartMergev1_3"
    if len(sys.argv) == 1:
            print(__doc__)
            sys.exit(1)

    for arg in sys.argv[1:]:
        if arg.find("-h") in [0, 1]:
            print(__doc__)
            sys.exit(1)
        elif arg.find("-device=") in [0, 1]:
            device = arg.split("=", 1)[1]
        elif arg.find("-range=") in [0, 1]:
            filerange = getRange(arg.split("=", 1)[1])
        elif arg.find("-plugin=") in [0, 1]:
            plugin = arg.split("=", 1)[1]
        elif arg.find("-rdabs=") in [0, 1]:
            rdabs = float(arg.split("=", 1)[1])
        elif arg.find("-rdrel=") in [0, 1]:
            rdrel = float(arg.split("=", 1)[1])
        elif arg.find("-out=") in [0, 1]:
            out = arg.split("=", 1)[1]
            if os.path.isfile(out):
                outFile = (os.path.abspath(out))
        elif arg.find("-sub=") in [0, 1]:
            out = arg.split("=", 1)[1]
            if os.path.isfile(out):
                subFile = (os.path.abspath(out))

        elif os.path.isfile(arg):
            filenames.append(os.path.abspath(arg))

    edna = PyTango.DeviceProxy(device)

#    edna.initPlugin(plugin)
    t0 = time.time()
    totaltime = 0.0
    listjobs = []
    listInFiles = []
    if filenames:
        common_base = None
        for fn in filenames:
            base = os.path.basename(os.path.splitext(fn)[0])
            if outFile is None:
                if common_base:
                    common_base = getCommon(base, common_base)
                else:
                    common_base = base
            if filerange:
                idx = getInteger(base.split("_")[-1])
                if (idx is not None) and (idx in filerange):
                    listInFiles.append(os.path.abspath(fn))
            else:
                listInFiles.append(os.path.abspath(fn))

        if not outFile:
            outFile = os.path.join(os.path.dirname(filenames[0]), common_base + "ave.dat")
        if not subFile:
            subdir = os.path.join(os.path.dirname(os.path.dirname(filenames[0])), "ednaSub")
            if not subdir:
                os.makedirs(subdir)
            subFile = os.path.join(subdir, common_base + "sub.dat")

        xsd = XSDataInputBioSaxsSmartMergev1_0(mergedCurve=XSDataFile(XSDataString(outFile)))
        xsd.subtractedCurve = XSDataFile(XSDataString(subFile))
        if rdabs:
            xsd.absoluteFidelity = XSDataDouble(rdabs)
        if rdrel:
            xsd.relativeFidelity = XSDataDouble(rdrel)
        xsd.inputCurves = [XSDataFile(XSDataString(i)) for i in listInFiles ]
        myXML = xsd.marshal()
        t1 = time.time()
        pid = edna.startJob([plugin, myXML])
        deltat = time.time() - t1
        totaltime += deltat
        listjobs.append(pid)
        print("%s | Total Time:\t%.3fs /Tango %.3fs\tLast Tango:\t%.3f" % (pid, time.time() - t0, totaltime, deltat))
    else:
        for xml in listXml:
            pid = edna.startJob([plugin, xml])
            print("%s | Tango time: %.3fs" % (pid, time.time() - t0))
            listjobs.append(pid)

    while edna.getJobState(listjobs[-1]) not in ["success", "failure"]:
        time.sleep(1)

    edna.collectStatistics()
    print(edna.getStatistics())
