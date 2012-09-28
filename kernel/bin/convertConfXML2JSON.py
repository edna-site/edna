#!/usr/bin/python
#coding:utf8
from __future__ import with_statement
import os, sys, json

__author__ = "Jérôme Kieffer"

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
from XSDataCommon import XSConfiguration

def bestType(a):
    """
    convert a string to it's typed version
    """
    if a.lower() in ["true", "on"]:
        return True
    if a.lower() in ["false", "off"]:
        return False
    if a.lower() in ["none", "nul", "null"]:
        return None
    try:
        ia = int(a)
    except:
        ia = None
    try:
        fa = float(a)
    except:
        fa = None
    if ia is not None and fa is not None:
        if ia == fa:
            return ia
        else:
            return fa
    else:
        return str(a)

def convert(infile, outfile):
    dico = {"__extend__":None}
    xml = XSConfiguration.parseFile(infile)
    xsPluginList = xml.getXSPluginList()
    for pluginItem in xsPluginList.getXSPluginItem():
        plugin_conf = {}
        plugin_name = pluginItem.name
        paramList = pluginItem.getXSParamList()
        if paramList:
            for paramItem in paramList.getXSParamItem():
                plugin_conf[paramItem.name] = bestType(paramItem.value)
        dico[plugin_name] = plugin_conf
    with open(outfile, "w") as f:
        f.write(json.dumps(dico, indent=4))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        infiles = sys.argv[1:]
    else:
        print("Usage: convert a XML configuration to a JSON one")
        sys.exit(1)
    for infile in infiles:
        outfile = os.path.splitext(infile)[0] + ".json"
        if not os.path.isfile(infile):
            print("No such input file %s" % infile)
            continue
        if os.path.isfile(outfile):
            print("Output file %s exist: skipping" % outfile)
            continue
        print("Converting %s \t-->\t%s" % (infile, outfile))
        convert(infile, outfile)
