# -*- coding: utf8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDUtilsPath.py 1484 2010-05-05 07:08:21Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
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
__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import math
from EDVerbose import EDVerbose
from XSDataCommon import XSDataString


class EDUtilsUnit:
    """
    This is a static utility class for handling unit (meter ... and subunit) in XSData / XML data structures.
    """

    dictLength = {("m", "meter", None): 1.0,
                ("cm", "centimeter"): 1.0e-2,
                ("mm", "millimeter"): 1.0e-3,
                ("um", "µm", "micron", "micrometer"):1.0e-6,
                ("nm", "nanometer"):1.0e-9,
                ("pm", "picometer"): 1.0e-12,
                ("A", "Angstrom", "angstrom"):1.0e-10,
                ("km", "kilometer"): 1.e3,
                }

    dictAngle = {("rad", "r", None):1.0,
                 ("deg", "°"): math.pi / 180.0,
                 ("grad", "g"): math.pi / 200.0,
                 }

    dictTime = { ("s", "sec", "second", None):1.0,
                 ("ms", "millisec", "millisecond"):1.0e-3,
                 ("mn", "min", "minute"):60.0,
                 ("h", "hour", "heure"):3600.0
                }

    @staticmethod
    def getSIValue(_object):
        """
        convert any object into the international System unit.
        @param _object: any object  
        @return: value in the international system
        @rtype: float
        """
        fValue = None

        unit = _object.getUnit()
        if unit is None:
            EDVerbose.DEBUG("No unit specified for object %s" % _object.__class__)
            fValue = _object.getValue()
        else:
            if EDUtilsUnit.getClassName(_object) in ["XSDataWavelength", "XSDataDisplacement", "XSDataLength"]:
                fValue = EDUtilsUnit.getValueLength(_object.getValue(), unit.getValue())
            elif EDUtilsUnit.getClassName(_object) in ["XSDataAngle"]:
                fValue = EDUtilsUnit.getValueAngle(_object.getValue(), unit.getValue())
            elif EDUtilsUnit.getClassName(_object) in ["XSDataTime"]:
                fValue = EDUtilsUnit.getValueTime(_object.getValue(), unit.getValue())

        return fValue


    @staticmethod
    def getValue(_object, _strUnit):
        """
        convert any object into the international System unit.
        @param _object: any object
        @param _strUnit: unit name like "um" or "deg"  
        @return: value in the international system
        @rtype: float
        """
        fValue = None
        unit = _object.getUnit()
        if unit is None:
            EDVerbose.DEBUG("No unit specified for object %s" % _object.__class__)
            fValue = _object.getValue()
        else:
            if unit.getValue() == _strUnit:
                fValue = _object.getValue()
            else:
                if EDUtilsUnit.getClassName(_object) in ["XSDataWavelength", "XSDataDisplacement", "XSDataLength"]:
                    fValue = EDUtilsUnit.getValueLength(_object.getValue(), unit.getValue()) / EDUtilsUnit.getUnitScaleLength(_strUnit)
                elif EDUtilsUnit.getClassName(_object) in ["XSDataAngle"]:
                    fValue = EDUtilsUnit.getValueAngle(_object.getValue(), unit.getValue()) / EDUtilsUnit.getUnitScaleAngle(_strUnit)
                elif EDUtilsUnit.getClassName(_object) in ["XSDataTime"]:
                    fValue = EDUtilsUnit.getValueTime(_object.getValue(), unit.getValue()) / EDUtilsUnit.getUnitScaleTime(_strUnit)
        return fValue


    @staticmethod
    def toXSD(_classXSData, _strObject,):
        """Convert a string or possibly any object to an XSD object
        
        @param _classXSData: the XSDataClass to be forced into
        @type _classXSData: class derived from XSData
        @param _strObject: the string representation of a physical object like "1.54 A" 
        @type _strObject: string (floats are accepted)
        """
        xsd = _classXSData()
        if isinstance(_strObject, (unicode, str)):
            listWords = _strObject.split(None, 1)
            if len(listWords) > 0:
                try:
                    fValue = float(listWords[0])
                except Exception:
                    EDVerbose.ERROR("Trying to create XSData object from %s; fValue not a float !" % _strObject)

                else:
                    xsd.setValue(fValue)
                    if len(listWords) == 2:
                        xsd.setUnit(XSDataString(listWords[1]))
            else:
                EDVerbose.WARNING("Trying to create XSData object from %s " % _strObject)
        elif isinstance(_strObject, (float, int)):
            xsd.setValue(_strObject)
        return xsd


    @staticmethod
    def getClassName(_object):
        """
        Retrieves the name of the class
        @return: the name of the class 
        @rtype: string 
        """
        return  str(_object.__class__).replace("<class '", "").replace("'>", "").split(".")[-1]


    @staticmethod
    def getUnitScaleLength(_unit):
        """
        Return the fScale factor of an unit versus SI unit (meter)
        @param _unit: the name of the unit
        @return : the numeric fScale factor (0.001 for mm)
        """
        fScale = None
        for oneUnit in EDUtilsUnit.dictLength:
            if  _unit in oneUnit:
                fScale = EDUtilsUnit.dictLength[oneUnit]
                break
        if  fScale is None:
            EDVerbose.WARNING("Unrecognized length unit: %s" % _unit)
            fScale = 1.0
        return fScale


    @staticmethod
    def getUnitScaleAngle(_unit):
        """
        Return the fScale factor of an unit versus SI unit (radian)
        @param _unit: the name of the unit
        @return : the numeric fScale factor (0.001 for mm)
        """
        fScale = None
        for oneUnit in EDUtilsUnit.dictAngle:
            if  _unit in oneUnit:
                fScale = EDUtilsUnit.dictAngle[oneUnit]
                break
        if  fScale is None:
            EDVerbose.WARNING("Unrecognized Angle unit: %s" % _unit)
            fScale = 1.0
        return fScale


    @staticmethod
    def getUnitScaleTime(_unit):
        """
        Return the fScale factor of an unit versus SI unit (seconds)
        @param _unit: the name of the unit
        @return : the numeric fScale factor (60 for mn)
        """
        fScale = None
        for oneUnit in EDUtilsUnit.dictTime:
            if  _unit in oneUnit:
                fScale = EDUtilsUnit.dictTime[oneUnit]
                break
        if  fScale is None:
            EDVerbose.WARNING("Unrecognized Time unit: %s" % _unit)
            fScale = 1.0
        return fScale


    @staticmethod
    def getValueLength(_value, _unit):
        """
        Convert a length like fValue to meter (SI)
        @param _value: the fValue in unit
        @type _value: float 
        @param _unit: the name of the unit
        @type _unit: string
        """
        return _value * EDUtilsUnit.getUnitScaleLength(_unit)


    @staticmethod
    def getValueAngle(_value, _unit):
        """
        Convert an angle like fValue to radian (SI)
        @param _value: the fValue in unit
        @type _value: float 
        @param _unit: the name of the unit
        @type _unit: string
        """
        return _value * EDUtilsUnit.getUnitScaleAngle(_unit)


    @staticmethod
    def getValueTime(_value, _unit):
        """
        Convert an time like fValue to seconds (SI)
        @param _value: the fValue in unit
        @type _value: float 
        @param _unit: the name of the unit
        @type _unit: string
        """
        return _value * EDUtilsUnit.getUnitScaleTime(_unit)
