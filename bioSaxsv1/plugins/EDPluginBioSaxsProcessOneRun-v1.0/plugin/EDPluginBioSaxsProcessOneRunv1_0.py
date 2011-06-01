# coding: utf8
# 
#    Project: BioSaxs
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
from EDFactoryPluginStatic import EDFactoryPluginStatic

"""
ReImplementation of the Reprocess script: Process one Run  
( by ricardo.fernandes@esrf.fr)
"""

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, sys
from EDVerbose          import EDVerbose
from EDPluginControl    import EDPluginControl
from EDUtilsBioSaxs     import EDUtilsBioSaxs
from EDUtilsPlatform   import EDUtilsPlatform
from XSDataControlBioSaxsReprocess import XSDataInputBioSaxsReprocessv1_0
from XSDataControlBioSaxsReprocess import XSDataResultBioSaxsReprocessv1_0

architecture = EDUtilsPlatform.architecture
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "Fabio-r5080", architecture)
if  os.path.isdir(numpyPath) and (numpyPath not in sys.path):
    sys.path.insert(1, numpyPath)
if  os.path.isdir(fabioPath) and (fabioPath not in sys.path):
    sys.path.insert(1, fabioPath)

import HDFDictionary
#EDFactoryPluginStatic

from fabio.openimage import openimage

class EDPluginBioSaxsProcessOneRunv1_0(EDPlugin):
    """
    Control plugin that does what was in the Reprocess function in the original program 
    
    """
    __hdfDictionary = HDFDictionary.HDFDictionary()
    __dictTrans = None

    def __init__(self):
        """
        """
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsReprocessv1_0)
        self.xsdInputData = None
        self.strDetector = None
        self.strOperation = None
        self.strDirectory = None
        self.strRawDir = None
        self.str1dDir = None
        self.str2dDir = None
        self.strMiscDir = None
        self.strPrefix = None
        self.specStatus = None
        self.specVersion = None
        self.specAbort = None
        self.beamCenterX = None
        self.pixelSizeX = None
        self.pixelSizeY = None
        self.beamCenterY = None
        self.beamStopDiode = None
        self.strCode = None
        self.strComments = None
        self.fConcentration = None
        self.bKeepOriginal = True
        self.machineCurrent = None
        self.wavelength = None
        self.iRunNumber = None
        self.maskFile = None
        self.normalisation = None
        self.bIsOnline = False
        self.listFrames = []

    def preProcess(self):
        """
        
        """

    def process(self):
        """
        Processing of one run, i.e. a set of files differing only by their frame number. 
        """

        if len(frameList) == 0:
            EDUtilsBioSaxs.showMessage(3, "There are no frames for run '%s'!" % runNumber)
        else:
            frameList.sort()
            for frame in frameList:

                if self.strDetecor == "pilatus":
                    filenameRAW = os.path.join(self.strRawDir, "%s_%03i_%02i.edf" % (pPrefix, runNumber, frame))
                    sizeRAW = 4090000
                    sizeNOR = 4100000
                elif self.strDetecor == "vantec":
                    filenameRAW = os.path.join(self.strRawDir, "%s_%03i_%02i.gfrm" % (pPrefix, runNumber, frame))
                    sizeRAW = 4200000
                    sizeNOR = 16780000

                filenameNOR = os.path.join(self.str2dDir, "%s_%03i_%02i.edf" % (self.strPrefix, self.fRunNumber, frame))
                filenameLOG = os.path.join(self.strMiscDir, "%s_%03i_%02i.log" % (self.strPrefix, runNumber, frame))
                filenameMSK = os.path.join(self.strMiscDir, "%s_%03i_%02i.msk" % (self.strPrefix, runNumber, frame))
                filenameANG = os.path.join(self.strMiscDir, "%s_%03i_%02i.ang" % (self.strPrefix, runNumber, frame))
                filenameDAT = os.path.join(self.str1dDir, "%s_%03i_%02i.dat" % (self.strPrefix, runNumber, frame))

                if not self.bIsOnline:
#                if __terminal or pSPECVersion is not None:   # reprocess was launched from terminal or from BsxCuBE while reprocessing data
                    if pConcentration == "" or pComments == "" or pCode == "" or pMaskFile == "" or pDetecorDistance == "" or pWaveLength == "" or pPixelSizeX == "" or pPixelSizeY == "" or pBeamCenterX == "" or pBeamCenterY == "" or pNormalisation == "" or pBeamStopDiode == "" or pMachineCurrent == "":
                        filenameNOR_ORG = os.path.join(self.str2dDir, "%s_%03d_%02d.edf" % (pPrefix, runNumber, frame))
                        if os.path.exists(filenameNOR_ORG):
                            edf = openimage(filenameNOR_ORG)
                            if "History-1" in edf.header:
                                history0 = edf.header.pop("History-1")
                                edf.header_keys.remove("History-1")
                            else:
                                history0 = ""
                            if "History-1~1" in edf.header:
                                history1 = edf.header.pop("History-1~1")
                                edf.header_keys.remove("History-1~1")
                            else:
                                history1 = ""
                            edf.header["history_combined"] = history0 + history1
                            edf.header_keys.append("history_combined")
                            status, translate = hdfDictionary.translate(edf.header.copy(), dictionary)
                            edf.write("filenameNOR_ORG", force_type=edf.data.dtype)
                            del edf
                        else:
                            translate = []
                            EDUtilsBioSaxs.showMessage(3, "Trying to get values from file '%s' which doesn't exist" % filenameNOR_ORG)

                else:   # reprocess was launched from BsxCuBE while collecting data
                    translate = []


                if self.concentration is None:
                    concentration = EDUtilsBioSaxs.makeTranslation(translate, "concentration", "0")
                else:
                    concentration = self.concentration

                if self.strComments == "":
                    comments = EDUtilsBioSaxs.makeTranslation(translate, "comments", "")
                else:
                    comments = pComments

                if pCode == "":
                    code = EDUtilsBioSaxs.makeTranslation(translate, "code", "")
                else:
                    code = pCode

                if pMaskFile == "":
                    maskFile = EDUtilsBioSaxs.makeTranslation(translate, "mask_file", "")
                else:
                    maskFile = pMaskFile

                if pDetectorDistance == "":
                    detectorDistance = EDUtilsBioSaxs.makeTranslation(translate, "detector_distance", "0")
                else:
                    detectorDistance = pDetectorDistance

                if pWaveLength == "":
                    waveLength = EDUtilsBioSaxs.makeTranslation(translate, "wave_length", "0")
                else:
                    waveLength = pWaveLength

                if pPixelSizeX == "":
                    pixelSizeX = EDUtilsBioSaxs.makeTranslation(translate, "pixel_size_X", "0")
                else:
                    pixelSizeX = pPixelSizeX

                if pPixelSizeY == "":
                    pixelSizeY = EDUtilsBioSaxs.makeTranslation(translate, "pixel_size_Y", "0")
                else:
                    pixelSizeY = pPixelSizeY

                if pBeamCenterX == "":
                    beamCenterX = EDUtilsBioSaxs.makeTranslation(translate, "beam_center_X", "0")
                else:
                    beamCenterX = pBeamCenterX

                if pBeamCenterY == "":
                    beamCenterY = EDUtilsBioSaxs.makeTranslation(translate, "beam_center_Y", "0")
                else:
                    beamCenterY = pBeamCenterY

                if pBeamStopDiode == "":
                    beamStopDiode = EDUtilsBioSaxs.makeTranslation(translate, "diode_current", "0")
                else:
                    beamStopDiode = pBeamStopDiode

                if pMachineCurrent == "":
                    machineCurrent = EDUtilsBioSaxs.makeTranslation(translate, "machine_current", "0")
                else:
                    machineCurrent = pMachineCurrent

                if pNormalisation == "":
                    normalisation = EDUtilsBioSaxs.makeTranslation(translate, "normalization_factor", "0")
                else:
                    normalisation = pNormalisation


                if EDUtilsBioSaxs.OPERATIONS.index(self.strOperation) in (-2, -1, 0, 3):
                    EDVerbose.screen("Normalising EDF frame '%s'..." % filenameNOR)

                    if not self.bKeepOriginal:
                        for oneFile in (filenameNOR, filenameLOG):
                            if os.path.isfile(oneFile):
                                os.remove(oneFile)

                    status = waitFile(filenameRAW, sizeRAW, pTimeOut)
                    if status == 0:
                        if float(beamStopDiode) == 0:
                            EDUtilsBioSaxs.showMessage(3, "The value of the beam stop diode is zero!")
                        else:
                            if self.strDetecor == "pilatus":    # Pilatus
                                command = "saxs_mac +var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 -otit \"DiodeCurr=%s, MachCurr=%s mA, Concentration=%s, Comments: %s, Code: %s, Mask: %s, Normalisation: %s\" -i1dis \"%s\" -i1wvl \"%s_nm\" -i1pix %s_um %s_um -i1cen %s %s -ofac %s %s %s > %s 2>/dev/null" % \
                                           (beamStopDiode, machineCurrent, concentration, comments, code, maskFile, normalisation, detectorDistance, waveLength, pixelSizeX, pixelSizeY, beamCenterX, beamCenterY, str(float(normalisation) / float(beamStopDiode)), filenameRAW, filenameNOR, filenameLOG)
                            elif self.strDetecor == "vantec":   # Vantec
                                command = "saxs_mac +var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 -otit \"DiodeCurr=%s, MachCurr=%s mA, Concentration=%s, Comments: %s, Code: %s, Mask: %s, Normalisation: %s\" -odis \"%s\" -i1wvl \"%s_nm\" -i1pix %s_um %s_um -i1cen %s %s -ofac %s %s %s > %s 2>/dev/null" % \
                                        (beamStopDiode, machineCurrent, concentration, comments, code, maskFile, normalisation, detectorDistance, waveLength, pixelSizeX, pixelSizeY, beamCenterX, beamCenterY, str(float(normalisation) / float(beamStopDiode)), filenameRAW, filenameNOR, filenameLOG)
                            #print command 
                            if subprocess.call(command, shell=True) == 0:
                                EDUtilsBioSaxs.showMessage(2, "The frame '%s' was normalised..." % filenameNOR, filenameNOR)
                            else:
                                EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_mac' or it returned an error!")
                    elif status == 1:
                        print "Aborting data reprocess!"
                        sys.exit(0)
                    else:
                        EDUtilsBioSaxs.showMessage(3, "File '%s' didn't appear on disk after '%s' seconds." % (filenameRAW, pTimeOut))


                if self.strOperation in ("-2", "-1", "1", "3"):
                    print "Generating 1D file '%s'..." % filenameDAT

                    if not self.bKeepOriginal:
                        for oneFile in (filenameDAT, filenameANG, filenameMSK):
                            if os.path.isfile(oneFile):
                                os.remove(oneFile)

                    status = waitFile(filenameNOR, sizeNOR, pTimeOut)
                    if status == 0:
                        command = "saxs_add -omod n %s %s %s > /dev/null 2>/dev/null" % (filenameNOR, maskFile, filenameMSK)
                        #print command
                        if subprocess.call(command, shell=True) == 0:
                            command = "saxs_angle -omod n -rsys normal -da 360_deg -odim = 1 %s %s > /dev/null 2>/dev/null" % (filenameMSK, filenameANG)
                            #print command
                            if subprocess.call(command, shell=True) == 0:
                                #command = "saxs_curves -i1err _i1val -scf 2_pi -ext .dat -spc \"  \" -prm \"Sample c=%6.2f mg/ml,Concentration: %s,Code: %s\" %s %s" % (float(concentration), concentration, code, filenameANG, filenameDAT)
                                command = "saxs_curves -scf 2_pi -ext .dat -spc \"  \" %s %s > /dev/null 2>/dev/null" % (filenameANG, filenameDAT)
                                #print command
                                if subprocess.call(command, shell=True) == 0:
                                    spec.open(filenameDAT)
                                    header = spec.getHeader()
                                    values = spec.getValues()
                                    spec.close()
                                    header[1] = " Sample c=%6.2f mg/ml" % float(concentration)
                                    header.append("Normalisation: %s" % normalisation)
                                    header.append("Concentration: %s" % concentration)
                                    header.append("Code: %s" % code)
                                    spec.open(filenameDAT, "w")
                                    spec.write(header, values)
                                    spec.close()
                                    EDUtilsBioSaxs.showMessage(2, "The 1D file '%s' was generated..." % filenameDAT, filenameDAT)
                                else:
                                    EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_curves' or it returned an error!")
                            else:
                                EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_angle' or it returned an error!")
                        else:
                            EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_add' or it returned an error!")
                    elif status == 1:
                        print "Aborting data reprocess!"
                        sys.exit(0)
                    else:
                        EDUtilsBioSaxs.showMessage(3, "File '%s' didn't appear on disk after '%s' seconds." % (filenameNOR, pTimeOut))


#            if self.strOperation in ("-2", "1", "2", "3"):
            if EDUtilsBioSaxs.OPERATIONS.index(self.strOperation) in (1, 2, 3):
                filenameDAT_AVE = os.pathjoin(self.str1dDir, "%s_%s_ave.dat" % (pDirectory, pPrefix, runNumber))
                filenameANG_AVE = os.pathjoin(self.strMiscDir, "%s_%s_ave.ang" % (pDirectory, pPrefix, runNumber))
                filenameLOG_AVE = os.pathjoin(self.strMiscDir, "%s_%s_ave.log" % (pDirectory, pPrefix, runNumber))
                filenamePattern = os.pathjoin(self.strMiscDir, "%s_%s_%s.ang" % (pDirectory, pPrefix, runNumber, "%%"))

                EDVerbose.screen("Generating average '%s' from 1D files..." % filenameDAT_AVE)

                if not sel.bKeepOriginal :
                    for oneFile in (filenameDAT_AVE, filenameANG_AVE, filenameLOG_AVE):
                        if os.path.isfile(oneFile):
                            os.remove(oneFile)


                frameFirst = frameList[0]
                frameLast = frameList[-1]

                #command = "saxs_mac -omod n -i1err _i1val -var -add %d -ofac %f %s,%d,%d %s > %s" % (frameLast - frameFirst + 1, 1 / float(frameLast - frameFirst + 1), filenamePattern, frameFirst, frameLast, filenameANG_AVE, filenameLOG_AVE)
                command = "saxs_mac -omod n +var -add %d -ofac %s %s,%d,%d %s > %s 2>/dev/null" % (frameLast - frameFirst + 1, str(1 / float(frameLast - frameFirst + 1)), filenamePattern, frameFirst, frameLast, filenameANG_AVE, filenameLOG_AVE)
                #print command
                if subprocess.call(command, shell=True) == 0:
                    #command = "saxs_curves -i1err _i1val -scf 2_pi -ext .dat -spc \"  \" -prm \"Sample c=%6.2f mg/ml,Concentration: %s,Code: %s\" %s %s" % (float(concentration), concentration, code, filenameANG_AVE, filenameDAT_AVE)
                    command = "saxs_curves -scf 2_pi -ext .dat -spc \"  \" %s %s > /dev/null 2>/dev/null" % (filenameANG_AVE, filenameDAT_AVE)
                    #print command
                    if subprocess.call(command, shell=True) == 0:
                        spec.open(filenameDAT_AVE)
                        header = spec.getHeader()
                        values = spec.getValues()
                        spec.close()
                        header[1] = " Sample c=%6.2f mg/ml" % float(concentration)
                        header.append("Normalisation: %s" % normalisation)
                        header.append("Concentration: %s" % concentration)
                        header.append("Code: %s" % code)
                        spec.open(filenameDAT_AVE, "w")
                        spec.write(header, values)
                        spec.close()
                        EDUtilsBioSaxs.showMessage(2, "The average file '%s' was generated..." % filenameDAT_AVE, filenameDAT_AVE)
                    else:
                        EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_curves' or it returned an error!")
                else:
                    EDUtilsBioSaxs.showMessage(3, "Could not find 'saxs_mac' or it returned an error!")
################################################################################
# END ONE RUNNUMBER
################################################################################

    def setupDict(self):
        """This is to setup the HDFdictionary (even if i don't know hot it works)"""
        if EDPluginBioSaxsProcessOneRunv1_0.__dictTrans is None:
            dictionaryEDF = "EDF_" + self.strDetector.upper()
            strConfDir = EDFactoryPluginStatic.getConfigurationHome("EDPluginBioSaxsProcessOneRunv1_0.py")
            EDVerbose.DEBUG("Configuration directory is %s" % strConfDir)
            status, dictionary = hdfDictionary.get(os.path.join(strConfDir, "Reprocess.xml"), dictionaryEDF)
            if status != 0:
                self.EDUtilsBioSaxs.showMessage(3, "Could not get '%s' dictionary!" % dictionaryEDF)

EDFactoryPluginStatic.getProjectPluginConfiguration(self.getPluginName())
