#
#coding: utf8
#
#    Project: BioSaxs : ID14-3
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Jérôme Kieffer
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

"""
Utilities for BioSaxs, especially for logging back both to EDNA using EDVerbose and to BioSaxsCube through SpecVariable  
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import sys, os
from EDUtilsPlatform    import EDUtilsPlatform
from EDUtilsPath        import EDUtilsPath
architecture = EDUtilsPlatform.architecture
specClientPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "SpecClient", architecture)
if  os.path.isdir(specClientPath) and (specClientPath not in sys.path):
    sys.path.insert(1, specClientPath)


from EDVerbose          import EDVerbose
#from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDObject           import EDObject
#try:
#    from SpecClient         import SpecVariable
#except:
#    SpecClient = None


class EDUtilsBioSaxs(EDObject):

    DETECTORS = ["pilatus", "vantec"]
    OPERATIONS = ["normalisation", "reprocess", "average", "complete"]
    TRANSLATION = {"beamStopDiode":"DiodeCurr",
                   "machineCurrent":"MachCurr",
                   "concentration":"Concentration",
                   "comments":"Comments",
                   "code":"Code",
                   "maskFile":"Mask",
                   "normalizationFactor":"Normalization",
                   "beamCenter_1":"Center_1",
                   "beamCenter_2":"Center_2",
                   "pixelSize_1":"PSize_1",
                   "pixelSize_2":"PSize_2",
                   "detectorDistance":"SampleDistance",
                   "wavelength":"WaveLength",
                   "detector":"Detector",
                   "storageTemperature":"storageTemperature",
                   "exposureTemperature":"exposureTemperature",
                   "exposureTime":"exposureTime",
                   "frameNumber":"frameNumber",
                   "frameMax":"frameMax",
                   "timeOfFrame":"time_of_day"
                   }
    FLOAT_KEYS = ["beamStopDiode", "machineCurrent", "concentration", "normalizationFactor",
                  "beamCenter_1", "beamCenter_2", "pixelSize_1", "pixelSize_2",
                  "detectorDistance", "wavelength", "timeOfFrame",
                  "storageTemperature", "exposureTemperature", "exposureTime"]
    INT_KEYS = [ "frameNumber", "frameMax"]


    __strSpecVersion = None
    __strSpecStatus = None
    __strSpecAbort = None
    __specVarStatus = None
    __specVarAbort = None

    @staticmethod
    def initSpec(_strSpecVersion, _strSpecStatus, _strSpecAbort):
        """
        Initialization of SpecVariable  ...
        """
        if EDUtilsBioSaxs.specVersion is None:
            EDUtilsBioSaxs.__strSpecVersion = _strSpecVersion
            EDUtilsBioSaxs.__strSpecStatus = _strSpecStatus
            EDUtilsBioSaxs.__strSpecAbort = _strSpecAbort
            EDUtilsBioSaxs.__specVarStatus = SpecVariable.SpecVariable(_strSpecStatus)
            EDUtilsBioSaxs.__specVarAbort = SpecVariable.SpecVariable(_strSpecAbort)
        else:
            EDVerbose.DEBUG("EDUtilsBioSaxs initSpec called whereas it was already set-up")
            if EDUtilsBioSaxs.__strSpecVersion != _strSpecVersion:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specVersion %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))
            if EDUtilsBioSaxs.__strSpecStatus != _strSpecStatus:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specStatus %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))
            if EDUtilsBioSaxs.__strSpecAbort != _strSpecAbort:
                EDVerbose.WARNING("EDUtilsBioSaxs initSpec specAbort %s whereas configured with %s"
                                  % (_strSpecVersion, EDUtilsBioSaxs.__strSpecVersion))

    @staticmethod
    def showMessage(_iLevel, _strMessage, _strFilename=None):
        """
        Class Method: 
        Similar to logging module of python but for updating BioSaxsCube
        
        @param _iLevel: print level seems to be
                        4 for Errors
                        3 for Warnings
                        2 for Info
                        1
                        0
        @type _iLevel: int
        @param _strMessage: comment to be printed
        @type _strMessage: string
        @param _strFilename: the file related to the message (nothing to do with a logfile)
        @type _strFilename: string or None
        """

        if _iLevel == 4:
            EDVerbose.ERROR(_strMessage)
        elif _iLevel == 3:
            EDVerbose.WARNING(_strMessage)
        else:
            EDVerbose.screen(_strMessage)
#        else:
#            EDVerbose.DEBUG(_strMessage)


        if EDUtilsBioSaxs.specStatus is not None:
            currentStatus = EDUtilsBioSaxs.specStatus.value["reprocess"]["status"]     # must do this, since SpecClient is apparently returning a non-expected data structure
            i = currentStatus.rfind(",")
            # TB: This ,1 or ,0 suffix nonsense seems to be a hack to force Spec to signal a variable change to bsxcube
            if i == -1 or currentStatus[i + 1:] == "1":
                if _strFilename is None:
                    newStatus = "%s,%s,0" % (_iLevel, _strMessage)
                else:
                    newStatus = "%s,%s,%s,0" % (_iLevel, _strMessage, _strFilename)
            else:
                if _strFilename is None:
                    newStatus = "%s,%s,1" % (_iLevel, _strMessage)
                else:
                    newStatus = "%s,%s,%s,1" % (_iLevel, _strMessage, _strFilename)
            EDUtilsBioSaxs.specStatus.setValue(newStatus)

        if (EDUtilsBioSaxs.specAbort is not None) and (EDUtilsBioSaxs.specAbort.value["reprocess"]["abort"]) == "1":
            # must do this, since SpecClient is apparently returning a non-expected data structure
            EDVerbose.ERROR("Aborting data reprocess!")
#            sys.exit(0)


    @staticmethod
    def getFilenameDetails(_strFilename):
        """
        Split the name of the file in 4 components:
        prefix_run_frame_extra.extension
        @return: prefix, run, frame, extra, extension
        @rtype: 4-tuple of strings
        """
        _strFilename = str(_strFilename)
        file, extension = os.path.splitext(_strFilename)

        items = file.split("_")
        prefix = items[0]
        run = ""
        frame = ""
        extra = ""

        for oneItem in items[1:]:
            if oneItem.isdigit():
                if run == "":
                    run = oneItem
                elif frame == "":
                    frame = oneItem
                elif extra == "":
                    extra = oneItem
                else:
                    extra += "_" + oneItem
            else:
                if run == "":
                    prefix += "_" + oneItem
                else:
                    extra += "_" + oneItem

        try: #remove the "." at the begining of the extension
            extension = extension[1:]
        except IndexError:
            extension = ""


        try: #remove the "_" at the begining of the extra
            extra = extra[1:]
        except IndexError:
            extra = ""

        return prefix, run, frame, extra, extension


    @staticmethod
    def makeTranslation(pTranslate, pKeyword, pDefaultValue):
        """
        Static method
        
        ????
        
         
        @type pTranslate: list ??
        @param pKeyword: the given keyword to be replaced
        @param pDefaultValue: default value for the keyword
        """
        for keyword, value in pTranslate:
            if keyword == pKeyword:
                newValue = ""
                for i in range(0, len(value)):
                    if value[i] != "\"":
                        newValue += value[i]
                return newValue

        if len(pTranslate) > 0:
            EDUtilsBioSaxs.showMessage(3, "Trying to get value '%s' which doesn't exist!" % pKeyword)

        return pDefaultValue
