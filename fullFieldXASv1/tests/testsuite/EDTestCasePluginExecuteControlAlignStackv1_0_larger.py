#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble
#
#    Principal author:       Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble"

import os

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from XSDataFullFieldXAS         import XSDataInputAlignStack
from XSDataFullFieldXAS         import XSDataResultAlignStack

class EDTestCasePluginExecuteControlAlignStackv1_0_larger(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlAlignStackv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_AlignStack.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputAlignStack_larger.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultAlignStack_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download an EDF file from http://www.edna-site.org
        and remove any existing output file, i.e. /tmp/edna-$USER/stack.h5 
        """
        EDTestCasePluginExecute.preProcess(self)
        print
        self.loadTestImage([ "FullFieldXAS_%02i.edf" % i for i in range(11)])
        strExpectedOutput = self.readAndParseFile (self.getDataInputFile())
        xsDataResultReference = XSDataResultAlignStack.parseString(strExpectedOutput)
        self.outputFileName = xsDataResultReference.getHDF5File().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % self.outputFileName)
        if not os.path.isdir(os.path.dirname(self.outputFileName)):
            os.makedirs(os.path.dirname(self.outputFileName))
        if os.path.isfile(self.outputFileName):
            os.remove(self.outputFileName)

    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
        plugin.showData()


    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlAlignStackv1_0 = EDTestCasePluginExecuteControlAlignStackv1_0_larger("EDTestCasePluginExecuteControlAlignStackv1_0_larger")
    edTestCasePluginExecuteControlAlignStackv1_0.execute()
