#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 ESRF
#                            INSTITUTE_LINE_2
#
#    Principal author:       Jerome KIEFFER (kieffer@esrf.fr)
#
#    Contributing author:    CONTRIBUTING_AUTHOR
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDUtilsFile                         import EDUtilsFile
from XSDataSPDv1_0                       import XSDataResultSPDCake
from EDFactoryPluginStatic               import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")

import numpy


class EDTestCasePluginExecuteSPDCakev1_1(EDTestCasePluginExecute):
    """
    """

    def __init__(self):
        """
        """
        EDTestCasePluginExecute.__init__(self, "EDPluginSPDCakev1_1", "EDPluginControlSPD-v1.1")

        self.setConfigurationFile(self.getRefConfigFile())

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                      "XSDataInputSPDCake_reference.xml"))

        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                                "XSDataResultSPDCake_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"

        edStringSplineFileName = "frelon_spline_file_to_correct_SPD.spline"
        edStringPathToSplineFile = os.path.join(self.getTestsDataImagesHome(), edStringSplineFileName)
        if (not os.path.exists(edStringPathToSplineFile)):
            EDUtilsFile.copyFile(os.path.join(self.getPluginTestsDataHome(), edStringSplineFileName), \
                                  edStringPathToSplineFile)

    def preProcess(self):
        """
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "diff6105.edf", "darks0001.edf", "flats0001.edf", "EDPluginSPDCakev1_1.chi" ])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultSPDCake.parseString(strExpectedOutput)
        outputFileName = xsDataResultReference.getCakedFile().getPath().getValue()
        EDVerbose.DEBUG(" Output file is %s" % outputFileName)
        if not os.path.isdir(os.path.dirname(outputFileName)):
            os.makedirs(os.path.dirname(outputFileName))
        if os.path.isfile(outputFileName):
            EDVerbose.DEBUG(" Output file exists %s, I will remove it" % outputFileName)
            os.remove(outputFileName)


    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

#        # Checking obtained results
        xsDataResultsSPDCake = plugin.getDataOutput()
        pathToOutput = xsDataResultsSPDCake.getCakedFile().getPath().getValue()
#        edStringDataObtained = EDUtilsFile.readFile(pathToOutput)
#        edStringDataReference = EDUtilsFile.readFile(os.path.join(self.getPluginTestsDataHome(), \
#                                                                             "EDPluginSPDCakev1_1.chi"))
#        EDAssert.strAlmostEqual(edStringDataReference, edStringDataObtained, "Comparing ChiPlot files")
        EDVerbose.DEBUG("Checking obtained result...")
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        xsDataResultReference = XSDataResultSPDCake.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same")

        # Checking obtained results
        xsDataResultsSPDCake = plugin.getDataOutput()
        strPathToChiOutput = xsDataResultsSPDCake.getCakedFile().getPath().getValue()
        strPathToChiReference = os.path.join(self.getTestsDataImagesHome(), "EDPluginSPDCakev1_1.chi")
        Xref, Yref = readChiPlot(strPathToChiReference)
        Xobt, Yobt = readChiPlot(strPathToChiOutput)
        EDVerbose.DEBUG("Output File: %s, Reference file: %s" % (strPathToChiOutput, strPathToChiReference))
        bigX = Xref + Xobt
        bigX.sort()
        bigYobt = numpy.interp(bigX, Xobt, Yobt)
        bigYref = numpy.interp(bigX, Xref, Yref)
        EDVerbose.DEBUG("ref.shape= %s, obt.shape=%s" % (bigYobt.shape, bigYref.shape))
        EDVerbose.DEBUG("Type of object ref= %s, obt=%s" % (bigYobt.__class__, bigYref.__class__))
        EDAssert.arraySimilar(bigYobt, bigYref, _fAbsMaxDelta=0.1, _fScaledMaxDelta=0.1, _strComment="Comparing ChiPlot files")



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)



##############################################################################
def readChiPlot(filename):
    """
    read a chiplot file and retruns two lists X and Y of floats
    """
    X = []
    Y = []
    if os.path.isfile(filename):
        for line in open(filename, "rb").readlines():
            words = line.split()
            if len(words) == 2:
                try:
                    x = float(words[0])
                    y = float(words[1])
                except Exception:
                    continue
                X.append(x)
                Y.append(y)
    return X, Y

if __name__ == '__main__':
    edTestCasePluginExecuteSPDv1_1 = EDTestCasePluginExecuteSPDCakev1_1("EDTestCasePluginExecuteSPDCakev1_1")
    edTestCasePluginExecuteSPDv1_1.execute()
