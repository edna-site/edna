# coding: utf8
#
#    Project: templatev1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF Grenoble
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
__copyright__ = "2011, ESRF Grenoble"

import os, tempfile

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataEdnaSaxs")
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsSmartMergev1_0

class EDTestCasePluginExecuteBioSaxsSmartMergev1_4(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsSmartMergev1_4")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_BioSaxsSmartMerge.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsSmartMerge_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsSmartMergev1_1_reference.xml"))
        self.destFile = os.path.join(tempfile.gettempdir(), "edna-%s" % os.environ["USER"], "bioSaxsMerged.dat")

    def preProcess(self):
        """
        Download reference 1D curves
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([  "bioSaxsMerged.dat"] + ["bioSaxsIntegrated%02i.dat" % (i + 1) for i in range(10)])
        if not os.path.isdir(os.path.dirname(self.destFile)):
            os.makedirs(os.path.dirname(self.destFile))
        if os.path.isfile(self.destFile):
            os.remove(self.destFile)

    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()
        xsdRef = XSDataResultBioSaxsSmartMergev1_0.parseString(self.readAndParseFile(self.getReferenceDataOutputFile()))
        xsdRef.autoRg = None
        xsdObt = plugin.getDataOutput()
        xsdObt.status = None #Executive summary is too complicated to test
        EDAssert.strAlmostEqual(xsdRef.marshal(), xsdObt.marshal(), "XML output structures are the same", _fAbsError=0.1)
        ref = " ".join([" ".join(i.split()) for i in open(self.destFile)])
        obt = " ".join([" ".join(i.split()) for i in open(xsdObt.mergedCurve.path.value)])
        EDAssert.strAlmostEqual(ref, obt, "Files are the same", _fAbsError=0.1)

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsSmartMergev1_4 = EDTestCasePluginExecuteBioSaxsSmartMergev1_4("EDTestCasePluginExecuteBioSaxsSmartMergev1_4")
    edTestCasePluginExecuteBioSaxsSmartMergev1_4.execute()
