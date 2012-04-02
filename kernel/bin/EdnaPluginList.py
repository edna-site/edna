#!/usr/bin/env python
#-*- coding: UTF8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EdnaPluginList.py $"
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
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
This is a generator retrieving all plugin (by their name) and retrieve some basic statisitcs   
"""

__authors__ = ["Jérôme Kieffer", "Régis Perdreau"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3"
__date__ = "2011-05-20"
__copyright__ = "ESRF"

import os, sys, shutil, stat, time


if "EDNA_HOME" not in os.environ:
    strEdnaHome = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ["EDNA_HOME"] = strEdnaHome
else:
    strEdnaHome = os.environ["EDNA_HOME"]

def getPlugins(strPath, htmlpath=None):
    """
    @return: a dict with key=plugin and value=path
    """
    dictPlugins = {}
    dictProject = {}
    iControlPl = 0
    iExecPl = 0
    iOtherPl = 0
    ilen = len(strPath) + 1
    for root, dirs, files in os.walk(strPath, topdown=False):
        for name in files:
            if name.startswith("EDPlugin") and name.endswith(".py"):
                strPlugin = name[:-3]
                plugin = EdnaPlugin(os.path.join(root, name)[ilen:])
                dictPlugins[strPlugin] = plugin
                plugin.analyse()
                project = plugin.project
                strType = plugin.type
                if htmlpath is not None:
                    html = plugin.getHtml()
                    open(os.path.join(htmlpath, strPlugin + ".html"), "w").write(html)

                if strType == "Control Plugins":
                    iControlPl += 1
                elif strType == "Execution Plugins":
                    iExecPl += 1
                else:
                    iOtherPl += 1
                if project in dictProject:
                    if strType in dictProject[project]:
                        dictProject[project][strType][strPlugin] = plugin
                    else:
                        dictProject[project][strType] = {strPlugin:plugin}
                else:
                    dictProject[project] = {strType:{strPlugin:plugin}}
    return dictProject, {"Control":iControlPl, "Execution":iExecPl, "Others": iOtherPl}


def prettyPrint(dictProjects, dictNumbers):
    """
    @type dictProjects:  dict
    @type dictNumbers: dict
    @return: a string
    """
    lstStr = []
    for i in dictNumbers:
        lstStr += ["Number of %s Plugins:\t%d" % (i, dictNumbers[i])]
    lstProjects = dictProjects.keys()
    lstProjects.sort()
    for project in lstProjects:
        lstStr.append(project)
        lstType = dictProjects[project].keys()
        lstType.sort()
        for strType in  lstType:
            lstStr.append("\t%s" % strType)
            lstPlugins = dictProjects[project][strType].keys()
            lstPlugins.sort()
            for strPlugin in lstPlugins:
                lstStr.append("\t\t%s:\t%s" % (strPlugin, os.linesep.join(dictProjects[project][strType][strPlugin].classDoc)))
        lstStr.append("")
    return os.linesep.join(lstStr)


def prettyHtml(dictProjects, dictNumbers):
    """
    @return: a string
    """
    lstStr = ["<html>", "<head>", "<title>List of EDNA Plugins</title>", "</head>", \
               "<body>", "<center><h1>List of EDNA Plugins</h1></center>", "<table>", \
               "<tr><td>Generated on:</td><td>%s</td></tr>" % (time.asctime())]
    for i in dictNumbers:
        lstStr += ["<tr><td>Number of %s Plugins:</td><td>%d</td></tr>" % (i, dictNumbers[i])]
    lstStr += ["</table><hr>"]
    lstProjects = dictProjects.keys()
    lstProjects.sort()
    for project in lstProjects:
        lstStr.append("<h2>%s<h2>" % project)
        lstType = dictProjects[project].keys()
        lstType.sort()
        for strType in  lstType:
            lstStr.append("<h3>%s<h3>" % strType)
            lstPlugins = dictProjects[project][strType].keys()
            lstPlugins.sort()
            lstStr.append("<table>")
            for strPlugin in lstPlugins:
                plugin = dictProjects[project][strType][strPlugin]
                for datamodel in plugin.datamodel:
                    for datamodelImg in plugin.dictXSD:
                        if (plugin.datamodel[datamodel] is not None) and \
                                datamodelImg.startswith(plugin.datamodel[datamodel]) and \
                                plugin.dictXSD[datamodelImg].endswith(".png"):
                            destDatamodel = os.path.join(strDest, datamodelImg + ".png")
                            if os.path.isfile(destDatamodel) and os.path.isfile(plugin.dictXSD[datamodelImg]):
                                os.remove(destDatamodel)
                            try:
                                shutil.copy(plugin.dictXSD[datamodelImg], destDatamodel)
                            except shutil.Error:
                                print("Unable to copy %s to %s" % (plugin.dictXSD[plugin.datamodel], destDatamodel))
                            except IOError:
                                print("Unable to find Datamodel Image  %s" % (plugin.dictXSD[datamodelImg]))
                lstStr.append("<tr><td><a href='%s'>%s</a></td><td>%s</td></tr>" %
                              (os.path.join(os.path.basename(strDest), strPlugin + ".html"), strPlugin,
                               "<br>".join([unicode2html(i) for i in plugin.classDoc])))

            lstStr.append("</table>")
        lstStr.append("<hr>")
    lstStr.append("</body></html>")
    return os.linesep.join(lstStr)

def unicode2html(_unicodeIn):
    """
    Converts an unicode input into a "html" like string
    
    @param _unicodeIn: input unicode
    @return: html string
    """
    dico = {u'\u0022': '&quot;', u'\u0026': '&amp;', u'\u0027': '&apos;', u'\u003C': '&lt;', u'\u003E': '&gt;', u'\u00A0': '&nbsp;', u'\u00A1': '&iexcl;', u'\u00A2': '&cent;',
u'\u00A3': '&pound;', u'\u00A4': '&curren;', u'\u00A5': '&yen;', u'\u00A6': '&brvbar;', u'\u00A7': '&sect;', u'\u00A8': '&uml;', u'\u00A9': '&copy;', u'\u00AA': '&ordf;',
u'\u00AB': '&laquo;', u'\u00AC': '&not;', u'\u00AD': '&shy;', u'\u00AE': '&reg;', u'\u00AF': '&macr;', u'\u00B0': '&deg;', u'\u00B1': '&plusmn;', u'\u00B2': '&sup2;',
u'\u00B3': '&sup3;', u'\u00B4': '&acute;', u'\u00B5': '&micro;', u'\u00B6': '&para;', u'\u00B7': '&middot;', u'\u00B8': '&cedil;', u'\u00B9': '&sup1;', u'\u00BA': '&ordm;',
u'\u00BB': '&raquo;', u'\u00BC': '&frac14;', u'\u00BD': '&frac12;', u'\u00BE': '&frac34;', u'\u00BF': '&iquest;', u'\u00C0': '&Agrave;', u'\u00C1': '&Aacute;', u'\u00C2': '&Acirc;',
u'\u00C3': '&Atilde;', u'\u00C4': '&Auml;', u'\u00C5': '&Aring;', u'\u00C6': '&AElig;', u'\u00C7': '&Ccedil;', u'\u00C8': '&Egrave;', u'\u00C9': '&Eacute;', u'\u00CA': '&Ecirc;',
u'\u00CB': '&Euml;', u'\u00CC': '&Igrave;', u'\u00CD': '&Iacute;', u'\u00CE': '&Icirc;', u'\u00CF': '&Iuml;', u'\u00D0': '&ETH;', u'\u00D1': '&Ntilde;', u'\u00D2': '&Ograve;',
u'\u00D3': '&Oacute;', u'\u00D4': '&Ocirc;', u'\u00D5': '&Otilde;', u'\u00D6': '&Ouml;', u'\u00D7': '&times;', u'\u00D8': '&Oslash;', u'\u00D9': '&Ugrave;', u'\u00DA': '&Uacute;',
u'\u00DB': '&Ucirc;', u'\u00DC': '&Uuml;', u'\u00DD': '&Yacute;', u'\u00DE': '&THORN;', u'\u00DF': '&szlig;', u'\u00E0': '&agrave;', u'\u00E1': '&aacute;', u'\u00E2': '&acirc;',
u'\u00E3': '&atilde;', u'\u00E4': '&auml;', u'\u00E5': '&aring;', u'\u00E6': '&aelig;', u'\u00E7': '&ccedil;', u'\u00E8': '&egrave;', u'\u00E9': '&eacute;', u'\u00EA': '&ecirc;',
u'\u00EB': '&euml;', u'\u00EC': '&igrave;', u'\u00ED': '&iacute;', u'\u00EE': '&icirc;', u'\u00EF': '&iuml;', u'\u00F0': '&eth;', u'\u00F1': '&ntilde;', u'\u00F2': '&ograve;',
u'\u00F3': '&oacute;', u'\u00F4': '&ocirc;', u'\u00F5': '&otilde;', u'\u00F6': '&ouml;', u'\u00F7': '&divide;', u'\u00F8': '&oslash;', u'\u00F9': '&ugrave;', u'\u00FA': '&uacute;',
u'\u00FB': '&ucirc;', u'\u00FC': '&uuml;', u'\u00FD': '&yacute;', u'\u00FE': '&thorn;', u'\u00FF': '&yuml;', u'\u0152': '&OElig;', u'\u0153': '&oelig;',
u'\u0160': '&Scaron;', u'\u0161': '&scaron;', u'\u0178': '&Yuml;', u'\u0192': '&fnof;', u'\u02C6': '&circ;', u'\u02DC': '&tilde;',
u'\u0391': '&Alpha;', u'\u0392': '&Beta;', u'\u0393': '&Gamma;', u'\u0394': '&Delta;', u'\u0395': '&Epsilon;',
u'\u0396': '&Zeta;', u'\u0397': '&Eta;', u'\u0398': '&Theta;', u'\u0399': '&Iota;', u'\u039A': '&Kappa;',
u'\u039B': '&Lambda;', u'\u039C': '&Mu;', u'\u039D': '&Nu;', u'\u039E': '&Xi;', u'\u039F': '&Omicron;', u'\u03A0': '&Pi;', u'\u03A1': '&Rho;', u'\u03A3': '&Sigma;',
u'\u03A4': '&Tau;', u'\u03A5': '&Upsilon;', u'\u03A6': '&Phi;', u'\u03A7': '&Chi;', u'\u03A8': '&Psi;', u'\u03A9': '&Omega;', u'\u03B1': '&alpha;', u'\u03B2': '&beta;',
u'\u03B3': '&gamma;', u'\u03B4': '&delta;', u'\u03B5': '&epsilon;', u'\u03B6': '&zeta;', u'\u03B7': '&eta;', u'\u03B8': '&theta;',
u'\u03B9': '&iota;', u'\u03BA': '&kappa;', u'\u03BB': '&lambda;', u'\u03BC': '&mu;', u'\u03BD': '&nu;', u'\u03BE': '&xi;',
u'\u03BF': '&omicron;', u'\u03C0': '&pi;', u'\u03C1': '&rho;', u'\u03C2': '&sigmaf;', u'\u03C3': '&sigma;', u'\u03C4': '&tau;', u'\u03C5': '&upsilon;',
u'\u03C6': '&phi;', u'\u03C7': '&chi;', u'\u03C8': '&psi;', u'\u03C9': '&omega;', u'\u03D1': '&thetasym;', u'\u03D2': '&upsih;', u'\u03D6': '&piv;', u'\u2002': '&ensp;',
u'\u2003': '&emsp;', u'\u2009': '&thinsp;', u'\u200C': '&zwnj;', u'\u200D': '&zwj;', u'\u200E': '&lrm;', u'\u200F': '&rlm;', u'\u2013': '&ndash;', u'\u2014': '&mdash;', u'\u2018': '&lsquo;',
u'\u2019': '&rsquo;', u'\u201A': '&sbquo;', u'\u201C': '&ldquo;', u'\u201D': '&rdquo;', u'\u201E': '&bdquo;', u'\u2020': '&dagger;', u'\u2021': '&Dagger;', u'\u2022': '&bull;',
u'\u2026': '&hellip;', u'\u2030': '&permil;', u'\u2032': '&prime;', u'\u2033': '&Prime;', u'\u2039': '&lsaquo;', u'\u203A': '&rsaquo;', u'\u203E': '&oline;', u'\u2044': '&frasl;',
u'\u20AC': '&euro;', u'\u2111': '&image;', u'\u2118': '&weierp;', u'\u211C': '&real;', u'\u2122': '&trade;', u'\u2135': '&alefsym;', u'\u2190': '&larr;', u'\u2191': '&uarr;',
u'\u2192': '&rarr;', u'\u2193': '&darr;', u'\u2194': '&harr;', u'\u21B5': '&crarr;', u'\u21D0': '&lArr;', u'\u21D1': '&uArr;', u'\u21D2': '&rArr;', u'\u21D3': '&dArr;', u'\u21D4': '&hArr;',
u'\u2200': '&forall;', u'\u2202': '&part;', u'\u2203': '&exist;', u'\u2205': '&empty;', u'\u2207': '&nabla;', u'\u2208': '&isin;', u'\u2209': '&notin;', u'\u220B': '&ni;',
u'\u220F': '&prod;', u'\u2211': '&sum;', u'\u2212': '&minus;', u'\u2217': '&lowast;', u'\u221A': '&radic;', u'\u221D': '&prop;', u'\u221E': '&infin;', u'\u2220': '&ang;', u'\u2227': '&and;',
u'\u2228': '&or;', u'\u2229': '&cap;', u'\u222A': '&cup;', u'\u222B': '&int;', u'\u2234': '&there4;', u'\u223C': '&sim;', u'\u2245': '&cong;', u'\u2248': '&asymp;', u'\u2260': '&ne;',
u'\u2261': '&equiv;', u'\u2264': '&le;', u'\u2265': '&ge;', u'\u2282': '&sub;', u'\u2283': '&sup;', u'\u2284': '&nsub;', u'\u2286': '&sube;', u'\u2287': '&supe;', u'\u2295': '&oplus;',
u'\u2297': '&otimes;', u'\u22A5': '&perp;', u'\u22C5': '&sdot;', u'\u2308': '&lceil;', u'\u2309': '&rceil;', u'\u230A': '&lfloor;', u'\u230B': '&rfloor;', u'\u27E8': '&lang;',
u'\u27E9': '&rang;', u'\u25CA': '&loz;', u'\u2660': '&spades;', u'\u2663': '&clubs;', u'\u2665': '&hearts;', u'\u2666': '&diams;'}

    strOut = ""
    if _unicodeIn is not None:
        for i in _unicodeIn:
            if i in dico:
                strOut += dico[i]
            else:
                strOut += str(i)
    return strOut

class EdnaPlugin(object):
    """
    represents an EDNA Plugin: authore, date, doc, datamodel, ...
    """
    strEdnaHome = strEdnaHome
    dictXSD = {} #key= XSDataTruc value=path to XSD image/edml
    def __init__(self, _strPath):
        self.dirname, self.basename = os.path.split(_strPath)
        self.path = _strPath
        if not(self.basename.startswith("EDPlugin") and self.basename.endswith(".py")):
            self.isaPlugin = False
            raise RuntimeError("Not an EDNA Plugin: %s" % _strPath)
        self.name = self.basename[:-3]
        self.project = _strPath.split(os.sep)[0]
        if len(self.project) == 0:
            self.project = _strPath.split(os.sep)[1]
        self.abspath = os.path.abspath(os.path.join(self.strEdnaHome, _strPath))
        self.date = None
        self.author = None
        self.license = None
        self.copyright = None
        self.type = None
        self.moduleDoc = []
        self.classDoc = []
        self.type = "Plugins (other)"
        self.isaPlugin = True
        self.__coding = None
        self.datamodel = {}
        if self.dictXSD == {}:
            self.loadXSD()


    def analyse(self):
        """
        Parse the source code to analyse the plugin 
        """
        print("Analysing: %s" % self.name)
        lines = open(os.path.join(self.strEdnaHome, self.path)).readlines()
        classline = None
#        moduledoc = None
        starter = None
        coding = None
        lstmoduledoc = []
        for line in lines:
            if ("coding:" in line) and (coding is None):
                coding = line[line.index("coding:") + 7:].split()[0].strip()
            if "#" in line:
                doc = line[:line.index("#")].rstrip()
            if line.startswith("__author__") and "=" in line:
                if coding is not None:
                    self.author = eval(line.split("=")[1]).decode(coding)
                else:
                    self.author = eval(line.split("=")[1])
            if line.startswith("__authors__") and "=" in line:
                if coding is not None:
                    self.author = ", ".join(eval(line.split("=")[1])).decode(coding)
                else:
                    self.author = ", ".join(eval(line.split("=")[1]))
            if line.startswith("__copyright__") and "=" in line:
                if coding is not None:
                    self.copyright = eval(line.split("=")[1]).decode(coding)
                else:
                    self.copyright = eval(line.split("=")[1])
            if line.startswith("__date__") and "=" in line:
                if coding is not None:
                    self.date = eval(line.split("=")[1]).decode(coding)
                else:
                    self.date = eval(line.split("=")[1])

            if line.startswith("__license__") and "=" in line:
                if coding is not None:
                    self.license = eval(line.split("=")[1]).decode(coding)
                else:
                    self.license = eval(line.split("=")[1])
            if (line.startswith("class") and line.split()[1].startswith(self.name)):
                classline = line
            if line.strip().startswith("self.setXSDataInputClass("):
                self.datamodel[(line.split("(", 1)[1].split(")", 1)[0].split(",")[0].split(".")[0]).strip()] = None

            if (self.moduleDoc == []) and (starter is not None) and (lstmoduledoc != []):
                if starter in line:
                    lstmoduledoc.append(line[:line.index(starter)])
                    self.moduleDoc = lstmoduledoc
                else:
                    lstmoduledoc.append(line)

            if (self.moduleDoc == []) and (starter is None):
                if line.startswith("'''"):
                    starter = "'''"
                elif line.startswith('"""'):
                    starter = '"""'
                elif line.startswith("'"):
                    starter = "'"
                elif line.startswith('"'):
                    starter = '"'
                else:
                    starter = None
                if starter is not None:
                    if line.strip().endswith(starter) and (len(line) > (2 * len(starter))):
                        self.moduleDoc = [line[len(starter):-len(starter)]]
                    else:
                        lstmoduledoc.append(line[len(starter):])

        for xsdIn in self.datamodel:
            for line in lines:
                if line.startswith("from") and ("import" in line) and (xsdIn in line):
                    self.datamodel[xsdIn] = line.split()[1]
                    break

        starter = None
        if classline is not None:
            lstclasstypes = classline.split("(", 1)
            if len(lstclasstypes) == 1:
                self.isaPlugin = False
                print("ERROR: Does not inherit from EDPlugin: %s" % self.name)
                return
            classtypes = lstclasstypes[1].strip()
            if classtypes.startswith("EDPluginControl"):
                self.type = "Control Plugins"
            elif classtypes.startswith("EDPluginExec"):
                self.type = "Execution Plugins"
        else:
            self.isaPlugin = False
            raise RuntimeError("Does not look like an EDNA Plugin: %s" % self.path)
            return
        idx = lines.index(classline) + 1
        lstclassdoc = []
        doc = lines[idx ].strip()
        if "#" in doc:
            doc = doc[:doc.index["#"]].strip()
        if doc.startswith("'''"):
            starter = "'''"
        elif doc.startswith('"""'):
            starter = '"""'
        elif doc.startswith("'"):
            starter = "'"
        elif doc.startswith('"'):
            starter = '"'
        else:
            starter = None
        if starter is not None:
            if doc.endswith(starter) and (len(doc) > (2 * len(starter))):
                lstclassdoc.append(doc[len(starter):-len(starter)])
            else:
                lstclassdoc.append(doc[len(starter):])
                bFinished = False
                while not bFinished:
                    idx += 1
                    doc = lines[idx ].strip()
                    if "#" in doc:
                        doc = doc[:doc.index("#")].strip()
                    if starter in doc:
                        lstclassdoc.append(doc[:doc.index(starter)])
                        bFinished = True
                    else:
                        lstclassdoc.append(doc)

            self.classDoc = lstclassdoc
        self.moduleDoc = [i for i in self.moduleDoc if i.strip() != "" ]
        self.classDoc = [i for i in self.classDoc if i.strip() != "" ]
        if coding is not None:
            newModuleDoc = []
            newClassDoc = []
            for line in self.moduleDoc:
                try:
                    dec = line.decode(coding)
                except Exception:
                    dec = line
                    print("Unable to decode %s with %s" % (line, coding))
                else:
                    newModuleDoc.append(dec)
            self.moduleDoc = newModuleDoc
            for line in self.classDoc:
                try:
                    dec = line.decode(coding)
                except Exception:
                    dec = line
                    print("Unable to decode %s with %s" % (line, coding))
                else:
                    newClassDoc.append(dec)
            self.classDoc = newClassDoc
        self.isaPlugin = True
        self.__coding = coding


    def getHtml(self, coding=None):
        """
        Generate a web page with the documentation for the plugin
        """
        if coding is None:
            coding = self.__coding
        if coding is None:
            try:
                import locale
            except ImportError:
                coding = "ascii"
            else:
                coding = locale.getdefaultlocale()[1]
                if coding is None:
                    coding = "ascii"

        lstStr = ["<html>", "<head>", "<title>EDNA Plugin: %s</title>" % self.name, "</head>", "<body>", "<center><h1>EDNA Plugin: %s</h1></center>" % self.name, "<table>"]
        lstStr.append("<tr><td>Name:</td><td>%s</td</tr>" % self.name)
        lstStr.append("<tr><td>Project:</td><td>%s</td</tr>" % self.project)
        lstStr.append("<tr><td>Path:</td><td>%s</td</tr>" % self.path)
        lstStr.append("<tr><td>Author:</td><td>%s</td</tr>" % unicode2html(self.author))
        lstStr.append("<tr><td>Date:</td><td>%s</td</tr>" % unicode2html(self.date))
        lstStr.append("<tr><td>Copyright:</td><td>%s</td</tr>" % unicode2html(self.copyright))
        lstStr.append("<tr><td>License:</td><td>%s</td</tr>" % unicode2html(self.license))
        lstStr.append("<tr><td>Module doc:</td><td>%s</td</tr>" % "<br>".join([unicode2html(i) for i in self.moduleDoc]))
        lstStr.append("<tr><td>Class doc:</td><td>%s</td</tr>" % "<br>".join([unicode2html(i) for i in self.classDoc]))
        lstStr += ["</table><hr>"]

        onpage = {}
        for datamodel in self.datamodel:
            if self.datamodel[datamodel] is None:
                continue
            for datamodelImg in self.dictXSD:
                if datamodelImg.startswith(self.datamodel[datamodel]):
                    if datamodelImg in onpage:
                        onpage[datamodelImg].append(datamodel)
                    else:
                        onpage[datamodelImg] = [datamodel]

        for img in onpage:
            lstStr.append("Datamodels: %s <br \ >" % ", ".join(onpage[img]))
            if self.dictXSD[img].endswith(".png"):
                lstStr.append("<img src='%s.png'><hr>" % img)
            elif self.dictXSD[img].endswith(".edml"):
                lstStr += [edml2html(open(self.dictXSD[img]).read()), "<hr>"]
        lstStr.append("</body></html>")

        return os.linesep.join(lstStr)

    @classmethod
    def loadXSD(cls):
        """
        look for all datamodel images.
        """
        fullPath = ""
        if cls.dictXSD == {}:
            for root, dirs, files in os.walk(strEdnaHome, topdown=False):
                for name in files:
                    base, ext = os.path.splitext(name)
                    if name.startswith("XSData") and (ext in [".edml", ".png"]):
                        fullPath = os.path.join(root, name)
                        if fullPath.startswith(strDest):
                            try:
                                os.remove(fullPath)
                            except IOError:
                                print("Unable to remove %s" % fullPath)
                        elif base in cls.dictXSD :
                            if os.stat(fullPath)[stat.ST_MTIME] > os.stat(cls.dictXSD[base])[stat.ST_MTIME]:
                                cls.dictXSD[base] = fullPath
                        else:
                                cls.dictXSD[base] = fullPath


def edml2html(chaine):
    """
    Convert an EDML file to a piece of HTML string
    @param chaine: input string (EDML format)
    @type chaine: string 
    """
    COLORS = {'red':'FF0000', 'orange':'FF4500', 'yellow':'FFFF00', 'green':'00EE00', 'magenta':'FF00FF', 'cyan':'00FFFF', 'blue':'0000FF',
    'violet':'D02090', 'black':'000000', 'gray':'BEBEBE'}
    dictInst = {'targetNamespace':    'red',
              'complex':            'blue',
              'type':               'blue',
              'COMMENT':            'green',
              'package':            'orange',
              "optional":           "orange",
              "[":                  "orange",
              "]":                  "orange",
              ":":                  "violet",
              "{":                  "blue",
             "}":                  "blue",
              }

    listStruct = []
    for idx, subchain in enumerate(chaine.split('"')):
        if idx % 2 == 0:
            listLines = []
            for line in subchain.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;").replace(" ", "&nbsp;").split("\n"):
                for key in dictInst:
                    pos = line.find(key)
                    if pos >= 0:
                         line = '%s<FONT COLOR="%s">%s</FONT>%s' % (line[:pos], COLORS[dictInst[key]], line[pos:pos + len(key)], line[pos + len(key):])
                listLines.append(line)
            listStruct.append("<BR>\n".join(listLines))
        else:
             listStruct.append('<FONT COLOR="%s">"%s"</FONT>' % (COLORS[dictInst['COMMENT']], subchain.replace("\n", "<BR>\n")))
    return "".join(listStruct)


if __name__ == "__main__":
    strDest = os.path.join(os.getcwd() , "edna")
    if len(sys.argv) > 1:
        strDest = os.path.abspath(sys.argv[1])
    if not os.path.isdir(strDest):
        os.makedirs(strDest)
    datas = getPlugins(strEdnaHome, strDest)
    txt = prettyHtml(*datas)
    open(strDest + ".html", "w").write(txt)
