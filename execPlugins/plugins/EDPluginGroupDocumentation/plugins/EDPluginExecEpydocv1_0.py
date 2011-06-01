# coding: utf8
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF
#
#    Principal author:       Jérôme Kieffer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF"

import os
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataDocumentation import XSDataInputEpydoc, XSDataResultEpydoc, XSDataFile, XSDataString

class EDPluginExecEpydocv1_0(EDPluginExecProcessScript):
    """
    EDPluginExecEpydocv1_0 is a plugin running Epydoc, an automatic API documentation generator  
    """


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputEpydoc)
        self.sources = []
        self.strDestpath = None
        self.iVerbosity = 0
        self.strOutputType = "html"
        self.strProjectName = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecEpydocv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDocPath(), "No output documentation path provided")
        self.checkMandatoryParameters(self.getDataInput().getSources(), "No Source files provided ")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecEpydocv1_0.preProcess")
        self.sources = [ oneSrc.getPath().getValue() for oneSrc in self.getDataInput().getSources() ]
        self.strDestpath = self.getDataInput().getDocPath().getPath().getValue()
        if self.getDataInput().getVerbosity() is not None:
            self.iVerbosity = self.getDataInput().getVerbosity().getValue()
        if self.getDataInput().getDocType() is not None:
            self.strOutputType = self.getDataInput().getDocType().getValue().strip().lower()
            if self.strOutputType == "latex":
                self.strOutputType = "tex"
        if self.getDataInput().getProjectName() is not None:
            self.strProjectName = self.getDataInput().getProjectName().getValue()
        self.generateEpydocCommand()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecEpydocv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultEpydoc()
        if self.strProjectName is None:
            strName = "api." + self.strOutputType
        else:
            strName = self.strProjectName + "." + self.strOutputType
        dest = os.path.join(self.strDestpath, strName)
        if os.path.isfile(dest):
            xsDataResult.setDocPath(XSDataFile(XSDataString(dest)))
        else:
            xsDataResult.setDocPath(self.getDataInput().getDocPath())
        self.setDataOutput(xsDataResult)

    def generateEpydocCommand(self):
        lstCommandLineOption = ["--simple-term"]
        if self.iVerbosity < 0:
            lstCommandLineOption.append("-q")
        elif self.iVerbosity == 1:
            lstCommandLineOption.append("-v")
        elif self.iVerbosity > 1:
            lstCommandLineOption.append("-vv")

        if self.strOutputType == "pdf":
            lstCommandLineOption.append("--pdf")
        elif self.strOutputType == "html":
            lstCommandLineOption.append("--html")
        elif self.strOutputType == "text":
            lstCommandLineOption.append("--text")
        elif self.strOutputType == "dvi":
            lstCommandLineOption.append("--dvi")
        elif self.strOutputType == "ps":
            lstCommandLineOption.append("--ps")
        elif self.strOutputType in ["tex"]:
            lstCommandLineOption.append("--latex")


        if self.strProjectName is not None:
            lstCommandLineOption.append("-n %s" % self.strProjectName)

        lstCommandLineOption.append("-o '%s'" % self.strDestpath)
        lstCommandLineOption += ["'%s'" % i for i in self.sources]

        self.setScriptCommandline(" ".join(lstCommandLineOption))
        self.DEBUG("epydoc " + " ".join(lstCommandLineOption))
