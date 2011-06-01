##
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                        Jerome Kieffer
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

__authors__ = ["Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose import EDVerbose
from EDUtilsImage import EDUtilsImage
from EDTestCase   import EDTestCase
from EDAssert     import EDAssert


class EDTestCaseEDUtilsImage(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, _strTestName)
        self.__edConfiguration = None
        edStrDataDir = "images"
        self.__edStrDataPath = os.path.join(self.getTestsDataHome(), edStrDataDir)
        self.__strFileName = "ref-testscale_1_001.img"
        self.__strFilePath = os.path.join(self.__edStrDataPath, self.__strFileName)


    def testGetImageNumber(self):
        """
        Testing retrieving the image number from a image filename
        """
        iImageNumber = EDUtilsImage.getImageNumber(self.__strFileName)
        iReference = 1
        EDAssert.equal(iReference, iImageNumber)


    def testGetTemplateHash(self):
        """
        Testing retrieving the image number from a image filename
        """
        strSymbol = "#"
        strTemplate = EDUtilsImage.getTemplate(self.__strFileName)
        strTemplateReference = "ref-testscale_1_###.img"
        EDAssert.equal(strTemplateReference, strTemplate)


    def testGetTemplateQuestionMark(self):
        """
        Testing retrieving the image number from a image filename
        """
        strSymbol = "?"
        strTemplate = EDUtilsImage.getTemplate(self.__strFileName, strSymbol)
        strTemplateReference = "ref-testscale_1_???.img"
        EDAssert.equal(strTemplateReference, strTemplate)



##############################################################################

    def process(self):
        """
        """
        self.addTestMethod(self.testGetImageNumber)
        self.addTestMethod(self.testGetTemplateHash)
        self.addTestMethod(self.testGetTemplateQuestionMark)



##############################################################################

if __name__ == '__main__':

    edTestCaseEDUtilsImage = EDTestCaseEDUtilsImage("TestCase EDTestCaseEDUtilsImage")
    edTestCaseEDUtilsImage.execute()
