#    coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCaseParallelExecute.py 2128 2010-10-04 16:39:42Z kieffer $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (kieffer@esrf.fr)
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

__authors__ = ["Jérôme Kieffer"]
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, math
from EDVerbose                           import EDVerbose
from EDTestCase                          import EDTestCase
from EDAssert                            import EDAssert
from EDUtilsUnit                         import EDUtilsUnit
from XSDataCommon                        import XSDataLength, XSDataString, XSDataAngle, XSDataTime



class EDTestCaseEDUtilsUnit(EDTestCase):
    """
    Unit & execution test for the EDUtilsUnit static class
    """

    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDUtilsUnit")


    def unitTestGetSIValue(self):
        """
        test the execution of unitTestGetSIValue static method
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetSIValue")
        xsd = XSDataLength(1.5)
        xsd.setUnit(XSDataString("mm"))
        EDAssert.equal(0.0015, EDUtilsUnit.getSIValue(xsd), "Conversion mm to meter")
        xsd = XSDataAngle(90)
        xsd.setUnit(XSDataString("deg"))
        EDAssert.equal(math.pi / 2, EDUtilsUnit.getSIValue(xsd), "Conversion deg to rad")


    def unitTestToXSD(self):
        """
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestToXSD")
        xsdObt = EDUtilsUnit.toXSD(XSDataLength, "1.5 mm")
        xsdExp = XSDataLength(1.5)
        xsdExp.setUnit(XSDataString("mm"))
        EDAssert.equal(xsdExp.marshal(), xsdObt.marshal(), "XML representation are the same")


    def unitTestGetValueSILength(self):
        """
        Test sub method specific to length: GetValueLength
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueSILength")
        EDAssert.equal(1.54E-10, EDUtilsUnit.getValueLength(1.54, "A"), "Length Conversion A -> m ")


    def unitTestGetValueSIAngle(self):
        """
        Test sub method specific to length: GetValueLength
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueSIAngle")
        EDAssert.equal(math.pi / 2.0, EDUtilsUnit.getValueAngle(90, "deg"), "Angle Conversion deg -> rad ")


    def unitTestGetValueSITime(self):
        """
        Test sub method specific to length: GetValueTime
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueSITime")
        EDAssert.equal(1800, EDUtilsUnit.getValueTime(30, "mn"), "Length Conversion mn -> s ")


    def unitTestGetValueLength(self):
        """
        Test conversion in length 
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueLength")
        EDAssert.equal(0.0452, EDUtilsUnit.getValue(EDUtilsUnit.toXSD(XSDataLength, "45.2 um"), "mm"), "Length Conversion um -> mm ")


    def unitTestGetValueAngle(self):
        """
        Test conversion in length 
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueAngle")
        EDAssert.equal(100.0, EDUtilsUnit.getValue(EDUtilsUnit.toXSD(XSDataAngle, "90 deg"), "grad"), "Length Conversion deg -> grad ")


    def unitTestGetValueTime(self):
        """
        Test conversion in Time 
        """
        EDVerbose.DEBUG("EDTestCaseEDUtilsUnit.unitTestGetValueTime")
        EDAssert.equal(60.0, EDUtilsUnit.getValue(EDUtilsUnit.toXSD(XSDataTime, "1 h"), "mn"), "Length Conversion h -> mn ")


    def process(self):
        self.addTestMethod(self.unitTestGetSIValue)
        self.addTestMethod(self.unitTestToXSD)
        self.addTestMethod(self.unitTestGetValueSILength)
        self.addTestMethod(self.unitTestGetValueSIAngle)
        self.addTestMethod(self.unitTestGetValueSITime)
        self.addTestMethod(self.unitTestGetValueLength)
        self.addTestMethod(self.unitTestGetValueAngle)
        self.addTestMethod(self.unitTestGetValueTime)



if __name__ == '__main__':

    edTestCaseEDUtils = EDTestCaseEDUtilsUnit("EDTestCaseEDUtilsUnit")
    edTestCaseEDUtils.execute()
