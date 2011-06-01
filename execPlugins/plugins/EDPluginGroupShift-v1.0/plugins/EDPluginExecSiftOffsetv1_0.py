# coding: utf8
#
#    Project: execPlugins PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
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
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"

import os
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataShiftv1_0 import XSDataInputMeasureOffsetSift
from XSDataShiftv1_0 import XSDataResultMeasureOffsetSift
from XSDataCommon import XSDataDouble, XSDataFile, XSDataString


class EDPluginExecSiftOffsetv1_0(EDPluginExecProcessScript):
    """
    Simple implementation based on SIFT to measure the offset of two images 
    """

    OUTPUT = "output.pto"


    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputMeasureOffsetSift)
        self.inputFiles = []
        self.outFile = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecSiftOffsetv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDescriptorFile(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecSiftOffsetv1_0.preProcess")
        self.inputFiles = [ i.getPath().getValue() for i in self.getDataInput().getDescriptorFile()]
        self.outFile = os.path.join(self.getWorkingDirectory(), EDPluginExecSiftOffsetv1_0.OUTPUT)
        self.generateAutopanoCommand()

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecSiftOffsetv1_0.postProcess")
        xsDataResult = XSDataResultMeasureOffsetSift()
        if os.path.isfile(self.outFile):
            xsdStr = XSDataString(self.outFile)
            xsdFile = XSDataFile()
            xsdFile.setPath(xsdStr)
            xsDataResult.setPanoFile(xsdFile)
            dx = []
            dy = []
            for oneLine in open(self.outFile).readlines():
                if oneLine.startswith("c"):
                    x = 0
                    X = 0
                    y = 0
                    Y = 0
                    for oneWord in oneLine.strip().split(" "):
                        if oneWord.startswith("x"):
                            x = float(oneWord[1:])
                        elif oneWord.startswith("X"):
                            X = float(oneWord[1:])
                        elif oneWord.startswith("y"):
                            y = float(oneWord[1:])
                        elif oneWord.startswith("Y"):
                            Y = float(oneWord[1:])
                    if x != 0 and y != 0 and X != 0 and Y != 0 and abs(X - x) < 100 and abs(Y - y) < 100:
                        dx.append(X - x)
                        dy.append(Y - y)
                    else:
                        self.DEBUG("%s %s %s %s %s %s %s" % (oneLine, x, y, X, Y, X - x, Y - y))
            dx.sort()
            dy.sort()
            subDx = dx[int(round(0.1 * len(dx))):int(round(0.9 * len(dx)))]
            subDy = dy[int(round(0.1 * len(dy))):int(round(0.9 * len(dy)))]
            sum1 = 0.0
            sum2 = 0.0
            for i in subDx:
                sum1 += i
            for i in subDy:
                sum2 += i
            xsDataResult.setOffset([XSDataDouble(-sum2 / max(1, len(subDy))), XSDataDouble(-sum1 / max(1, len(subDx))) ])
        # Create some output data
        self.setDataOutput(xsDataResult)


    def generateAutopanoCommand(self):
        """
        This method creates the autopano command line.
        """

#        self.DEBUG("EDPluginExecSiftOffsetv1_0.generateKeysCommand")
        strMacro = ' --absolute-pathnames 1 --maxmatches 0   "%s" "%s"  "%s" ' % (self.outFile, self.inputFiles[0], self.inputFiles[1])
        self.DEBUG("EDPluginExecSiftOffsetv1_0.generateKeysCommand Autopano-sift Command line: %s%s" % (os.linesep, strMacro))
        self.setScriptCommandline(strMacro)

