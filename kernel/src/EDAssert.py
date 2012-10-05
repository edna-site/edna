# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (kieffer@esrf.fr)
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
This static class is used for comparing two objects.
"""


__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, tempfile, types
from difflib import SequenceMatcher
from EDVerbose import EDVerbose


class EDAssert:
    """
    This static class is used for comparing two objects.
    """


    @staticmethod
    def equal(_oExpected, _oObtained, _strComment="Equal", _fMaxDelta=1e-6):
        """
        Fail if the two objects are unequal as determined by the '==' operator.
        Saves the two objects to the current working directory using an unique identifier
        appended with "_obtained.txt" and "_expected.txt".
        @param _oExpected: any python object used as reference
        @param _oObtained: any python object to be compared with the reference
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        @param _fMaxDelta: epsilon to check equivalence for float
        @param _fMaxDelta: float 
        """
        bAlmostEqual = True

        if  (_oExpected != _oObtained):
            if isinstance(_oExpected, float):
                if abs(_oExpected - _oObtained) > _fMaxDelta:
                    bAlmostEqual = False
            elif isinstance(_oExpected, dict) and isinstance(_oObtained, dict):
                listExpKeys = list(_oExpected.keys())
                listExpKeys.sort()
                listObtKeys = list(_oObtained.keys())
                listObtKeys.sort()
                if listObtKeys == listExpKeys:
                    for key in listObtKeys:
                        oExpectedValue = _oExpected[key]
                        oObtainedValue = _oObtained[key]
                        if oExpectedValue != oObtainedValue:
                            if isinstance(oExpectedValue, float) and isinstance(oObtainedValue, float):
                                if abs(oExpectedValue - oObtainedValue) > _fMaxDelta:
                                    bAlmostEqual = False
                                    break
                            else:
                                bAlmostEqual = False
                                break
                else:
                    bAlmostEqual = False
            else:
                bAlmostEqual = False
        if bAlmostEqual:
            EDVerbose.ASSERT("OK " + _strComment)
        else:
            strExpectedFileName = tempfile.mktemp(suffix="_expected.txt", dir=os.getcwd())
            strUniqueIndentifier = strExpectedFileName.split("_expected.txt")[0]
            f = open(strExpectedFileName , "w")
            if isinstance(_oExpected, dict):
                f.write("#Dict:" + os.linesep)
                keys = _oExpected.keys()
                keys.sort()
                f.write(os.linesep.join(["%s:%s" % (i, _oExpected[i]) for i in keys ]))
            else:
                f. write(str(_oExpected))

            f.close()
            strObtainedFileName = strUniqueIndentifier + "_obtained.txt"
            f = open(strObtainedFileName, "w")
            if isinstance(_oObtained, dict):
                f.write("#Dict:" + os.linesep)
                keys = _oObtained.keys()
                keys.sort()
                print
                f.write(os.linesep.join(["%s:%s" % (i, _oObtained[i]) for i in keys ]))
            else:
                f. write(str(_oObtained))
            f.close()
            EQUAL_ERROR_ASSERT_MESSAGE = _strComment + " FAILURE: Expected different from obtained - identifier %s" % strUniqueIndentifier
            EDVerbose.ASSERT(EQUAL_ERROR_ASSERT_MESSAGE)
            raise AssertionError, EQUAL_ERROR_ASSERT_MESSAGE


    @staticmethod
    def strAlmostEqual(_oExpected, _oObtained, _strComment="Strings are similar", _fRelError=1e-2, _fAbsError=1e-4, _fStrSimilar=1.0, _strExcluded=None, _lstExcluded=[]):
        """
        Check if two strings (or XML strings) are almost equal, which means that: 
        - all pure text part are equal
        - floats do not differ more than 1% by default or 0.0001 in absolute difference

        Saves the two objects to the current working directory using an unique identifier
        appended with "_obtained.txt" and "_expected.txt".
        @param _oExpected: any python object used as reference, probably a string or an unicode string
        @param _oObtained: any python object to be compared with the reference, probably a string or an unicode string
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        @param _fRelError: maximum relative error defined as a float
        @param _fAbsError: maximum absolute error defined as a float
        @param _strExcluded: if a "word" contains this string, it is not taken into account for the comparison
        @type _strExcluded: string 
        @param _lstExcluded: list of words to be excluded for the comparison
        @type _lstExcluded:  list of strings

        """
        bAlmostEqual = True
        ERROR_ASSERT_MESSAGE = _strComment + ". "
        if  _oExpected != _oObtained:
            if _oExpected.__class__ != _oObtained.__class__:
                EDVerbose.WARNING("Expected is type %s and Obtained is type: %s" % (_oExpected.__class__, _oObtained.__class__))
                _oExpected = str(_oExpected)
                _oObtained = str(_oObtained)
            lstDataReference = _oExpected.replace(">", " ").replace("<", " ").split()
            lstDataObtained = _oObtained.replace(">", " ").replace("<", " ").split()
            if len(lstDataReference) == len(lstDataObtained):
                EDVerbose.DEBUG("Checking for small numerical error...Relative:%s Absolute: %s and similarity in strings >= %s%%" % (_fRelError, _fAbsError, _fStrSimilar * 100))
                for i in xrange(len(lstDataReference)):
                    dataReference = lstDataReference[i]
                    dataObtained = lstDataObtained[i]
                    if dataReference != dataObtained:
                        if (_strExcluded is not None) and (_strExcluded  in dataReference or _strExcluded in dataObtained):
                            continue
                        if len(_lstExcluded) > 0:
                            bFound = False
                            for key in _lstExcluded:
                                if (key  in dataReference) or (key in dataObtained):
                                    bFound = True
                                    break
                            if bFound:
                                continue
                        try:
                            fRefValue = float(dataReference)
                            fObtValue = float(dataObtained)
                        except ValueError:
                            fSimilarity = SequenceMatcher(None, dataReference, dataObtained).quick_ratio()
                            if fSimilarity < _fStrSimilar:
                                if max(len(dataReference), len(dataObtained)) < 100:
                                    ERROR_ASSERT_MESSAGE += "\nMismatch on %ith word, between ref: %s, and obt: %s." % (i, dataReference, dataObtained)
                                else:
                                    ERROR_ASSERT_MESSAGE += "\nMismatch on %ith word, Similarity of BIG string is %s < %s" % (i, fSimilarity, _fStrSimilar)
                                bAlmostEqual = False
                                break
                            else:
                                EDVerbose.DEBUG("Checking for similarity on %i th word: obtained %.4f%% >= %.4f%%" % (i, fSimilarity * 100.0, _fStrSimilar * 100.0))
                            continue
                        if  (fObtValue != fRefValue) and \
                            (2 * abs(fRefValue - fObtValue) / (fObtValue + fRefValue) > _fRelError) and \
                            abs(fRefValue - fObtValue) > _fAbsError:

                            ERROR_ASSERT_MESSAGE += "\nMismatch on word %i between ref: %s, and obt: %s." % (i, fRefValue, fObtValue)
                            bAlmostEqual = False
                            break
            else:
                ERROR_ASSERT_MESSAGE += "\nStrings do not have the same number of words."
                bAlmostEqual = False

        if not bAlmostEqual:
            strExpectedFileName = tempfile.mktemp(suffix="_expected.txt", dir=os.getcwd())
            strUniqueIndentifier = strExpectedFileName.split("_expected.txt")[0]
            f = open(strExpectedFileName , "w")
            f. write(str(_oExpected))
            f.close()
            strObtainedFileName = strUniqueIndentifier + "_obtained.txt"
            f = open(strObtainedFileName, "w")
            f. write(str(_oObtained))
            f.close()
            EQUAL_ERROR_ASSERT_MESSAGE = "FAILURE: %s \nIdentifier %s" % (ERROR_ASSERT_MESSAGE, strUniqueIndentifier)
            EDVerbose.ASSERT(EQUAL_ERROR_ASSERT_MESSAGE)
            raise AssertionError, EQUAL_ERROR_ASSERT_MESSAGE
        else:
            EDVerbose.ASSERT("OK " + _strComment)


    @staticmethod
    def isFile(_strFilename, _strComment=""):
        """
        Fail if the filename does not exist.
        @param _strFilename: any python string representing a file that shoul exist
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        """
        if not os.path.isfile(_strFilename):
            EQUAL_ERROR_ASSERT_MESSAGE = "FAILURE: " + _strComment + "\n Filename does not exist " + _strFilename
            EDVerbose.ASSERT(EQUAL_ERROR_ASSERT_MESSAGE)
            raise AssertionError, EQUAL_ERROR_ASSERT_MESSAGE
        else:
            EDVerbose.ASSERT("OK " + _strComment)


    @staticmethod
    def lowerThan(_fValue, _fReference=1.0, _strComment="Lower than"):
        """
        Fails if the _fValue is greater (or equal) than the reference.
        @param _fValue: any python object that can be compared ...
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        """
        if _fValue >= _fReference:
            EQUAL_ERROR_ASSERT_MESSAGE = "FAILURE: %s\n Obtained value %s should be lower than %s !!" % (_strComment, _fValue, _fReference)
            EDVerbose.ASSERT(EQUAL_ERROR_ASSERT_MESSAGE)
            raise AssertionError, EQUAL_ERROR_ASSERT_MESSAGE
        else:
            EDVerbose.ASSERT("OK " + _strComment)


    @staticmethod
    def greaterThan(_fValue, _fReference=1.0, _strComment="Greater than"):
        """
        Fails if the _fValue is greater (or equal) than the reference.
        @param _fValue: any python object that can be compared ...
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        """
        if _fValue <= _fReference:
            EQUAL_ERROR_ASSERT_MESSAGE = "FAILURE: %s\n Obtained value %s should be greater than %s !!" % (_strComment, _fValue, _fReference)
            EDVerbose.ASSERT(EQUAL_ERROR_ASSERT_MESSAGE)
            raise AssertionError, EQUAL_ERROR_ASSERT_MESSAGE
        else:
            EDVerbose.ASSERT("OK " + _strComment)


    @staticmethod
    def arraySimilar(_npaValue, _npaRef, _strComment="Arrays are similar", _fAbsMaxDelta=None, _fRelMaxDelta=None, _fRfactor=None, _fScaledMaxDelta=None):
        """
        Tests if two arrays are similar. 
        Two arrays (vectors, matrices, tensors, ...) if the have :  
        * same shape (always tested),
        * max(abs(Value - Ref)) < _fAbsMaxDelta if _fAbsMaxDelta is defined
        * max(abs(Value - Ref)/max(abs(Value),abs(Ref)) < _fRelMaxDelta if _fRelMaxDelta is defined 
        * Sigma(abs(Value - Ref)/max(abs(Value),abs(Ref)) < _fRfactor1 if _fRfactor1 is defined 
        
        
        @param _npaRef: reference array
        @type _npaRef: Numpy like array
        @param _npaValue: array to be compared with the reference
        @param _strComment: a comment to make your assertion more understandable to the user
        @type _strComment: python string or unicode string. 
        @type _fAbsMaxDelta: Float
        @type _fRelMaxDelta: Float
        @type _fRfactor1: Float
        """
        bAlmostEqual = True
        try:
            refShape = _npaRef.shape
            valShape = _npaValue.shape
        except Exception:
            bAlmostEqual = False
            ERROR_ASSERT_MESSAGE = "Objects passed have no shape attribute"

        if bAlmostEqual and not (refShape == valShape):
            bAlmostEqual = False
            ERROR_ASSERT_MESSAGE = "Arrays have different shapes Ref: %s, Obt: %s" % (refShape, valShape)

        if bAlmostEqual and _fAbsMaxDelta is not None:
            fval = (abs(_npaRef - _npaValue)).max()
            EDVerbose.DEBUG("Obtained Absolute Max Delta: %.4f" % fval)
            if fval > _fAbsMaxDelta:
                ERROR_ASSERT_MESSAGE = "Max delta obtained: %s larger than allowed: %s" % (fval, _fAbsMaxDelta)
                bAlmostEqual = False

        if bAlmostEqual and _fRelMaxDelta is not None:
            fval = (abs(_npaRef - _npaValue) / abs(_npaRef)).max()
            EDVerbose.DEBUG("Obtained Relative Max Delta: %.4f" % fval)
            if fval > _fRelMaxDelta:
                ERROR_ASSERT_MESSAGE = "Max relative delta obtained: %s larger than allowed: %s" % (fval, _fRelMaxDelta)
                bAlmostEqual = False

        if bAlmostEqual and _fRfactor is not None:
            fval = (abs(_npaRef - _npaValue) / abs(_npaRef)).sum() / len(_npaRef)
            EDVerbose.DEBUG("Obtained R-factor: %.4f" % fval)
            if fval > _fRfactor:
                ERROR_ASSERT_MESSAGE = "R factor obtained: %s larger than allowed: %s" % (fval, _fRfactor)
                bAlmostEqual = False

        if bAlmostEqual and _fScaledMaxDelta is not None:
            fval = (abs(_npaRef - _npaValue).max()) / (_npaRef.max() - _npaRef.min())
            EDVerbose.DEBUG("Obtained Scaled Max Delta: %.4f" % fval)
            if fval > _fScaledMaxDelta:
                ERROR_ASSERT_MESSAGE = "Scaled delta obtained: %s larger than allowed: %s" % (fval, _fScaledMaxDelta)
                bAlmostEqual = False


        if not bAlmostEqual:
            EDVerbose.ASSERT("FAILURE: %s, %s " % (_strComment, ERROR_ASSERT_MESSAGE))
            raise AssertionError, ERROR_ASSERT_MESSAGE
        else:
            EDVerbose.ASSERT("OK " + _strComment)

