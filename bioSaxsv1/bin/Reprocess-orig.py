"""
=============================================
  NAME       : Reprocess (Reprocess.py)
  
  DESCRIPTION:
    
  VERSION    : 1

  REVISION   : 0

  RELEASE    : 2010/FEB/18

  PLATFORM   : None

  EMAIL      : ricardo.fernandes@esrf.fr
  
  HISTORY    :
=============================================
"""




# =============================================
#  IMPORT MODULES
# =============================================
try:
    import sys
    import os
    import subprocess
    import time
    import HDFDictionary
    import EDF
    import SPEC
    from SpecClient import SpecVariable
except ImportError:
    print "%s.py: error when importing module!" % __name__


REPROCESS_STATUS = None

REPROCESS_ABORT = None


def Reprocess(pDetector, pOperation, pDirectory, pPrefix, pRunNumber, pFrameFirst, pFrameLast, pConcentration, pComments, pCode, \
              pMaskFile, pDetectorDistance, pWaveLength, pPixelSizeX, pPixelSizeY, pBeamCenterX, pBeamCenterY, pNormalisation, pBeamStopDiode, \
              pMachineCurrent, pKeepOriginal, pTimeOut, pSPECVersion, pSPECVariableStatus, pSPECVariableAbort, pTerminal):

    if pSPECVersion is not None:
        if pSPECVariableStatus is not None:
            globals()["REPROCESS_STATUS"] = SpecVariable.SpecVariable(pSPECVariableStatus, pSPECVersion)
        if pSPECVariableAbort is not None:
            globals()["REPROCESS_ABORT"] = SpecVariable.SpecVariable(pSPECVariableAbort, pSPECVersion)

    if pDetector not in ("0", "1"):
        showMessage(4, "Invalid detector '%s'!" % pDetector)
        return

    if pOperation not in ("-2", "-1", "0", "1", "2", "3"):
        showMessage(4, "Invalid operation '%s'!" % pOperation)
        return

    if not os.path.exists(pDirectory):
        showMessage(4, "Directory '%s' not found!" % pDirectory)
        return

    if not os.path.exists(pDirectory + "/1d"):
        try:
            os.mkdir(pDirectory + "/1d")
        except Exception:
            showMessage(4, "Could not create directory '1d' in '%s'!" % pDirectory)
            return

    if not os.path.exists(pDirectory + "/2d"):
        try:
            os.mkdir(pDirectory + "/2d")
        except Exception:
            showMessage(4, "Could not create directory '2d' in '%s'!" % pDirectory)
            return

    if not os.path.exists(pDirectory + "/misc"):
        try:
            os.mkdir(pDirectory + "/misc")
        except Exception:
            showMessage(4, "Could not create directory 'misc' in '%s'!" % pDirectory)
            return


    runNumberList = []
    if pRunNumber == "":
        for filename in os.listdir(pDirectory + "/raw"):
            if os.path.isfile(pDirectory + "/raw/" + filename):
                prefix, run, frame, extra, extension = getFilenameDetails(filename)
                if prefix == pPrefix and run != "" and frame != "" and (pDetector == "0" and extension == "edf" or pDetector == "1" and extension == "gfrm"):
                    try:
                        runNumberList.index(run)
                    except Exception:
                        runNumberList.append(run)
    else:
        list = pRunNumber.split(",")
        for runNumber in list:
            runNumber = "%03d" % int(runNumber)
            try:
                runNumberList.index(runNumber)
            except Exception:
                runNumberList.append(runNumber)

    if len(runNumberList) == 0:
        showMessage(4, "There are no runs for prefix '%s'!" % pPrefix)
        return
    else:
        runNumberList.sort()


    edf = EDF.EDF()
    spec = SPEC.SPEC()
    hdfDictionary = HDFDictionary.HDFDictionary()

    if pDetector == "0":
        dictionaryEDF = "EDF_PILATUS"
    else:
        dictionaryEDF = "EDF_VANTEC"
    status, dictionary = hdfDictionary.get(os.path.join(sys.path[0], "Reprocess.xml"), dictionaryEDF)
    if status != 0:
        showMessage(3, "Could not get '%s' dictionary!" % dictionaryEDF)

    #print dictionary

    if pKeepOriginal == "0":
        directory1D_REP = ""
        directory2D_REP = ""
        directoryMISC_REP = ""
    else:
        i = 0
        while True:
            directory1D_REP = pDirectory + "/1d/reprocess" + str(i)
            if os.path.exists(directory1D_REP):
                i += 1
            else:
                try:
                    os.mkdir(directory1D_REP)
                except Exception:
                    showMessage(3, "Could not create reprocess directory '%s'!" % directory1D_REP)
                break

        i = 0
        while True:
            directory2D_REP = pDirectory + "/2d/reprocess" + str(i)
            if os.path.exists(directory2D_REP):
                i += 1
            else:
                try:
                    os.mkdir(directory2D_REP)
                except Exception:
                    showMessage(3, "Could not create reprocess directory '%s'!" % directory2D_REP)
                break

        i = 0
        while True:
            directoryMISC_REP = pDirectory + "/misc/reprocess" + str(i)
            if os.path.exists(directoryMISC_REP):
                i += 1
            else:
                try:
                    os.mkdir(directoryMISC_REP)
                except Exception:
                    showMessage(3, "Could not create reprocess directory '%s'!" % directoryMISC_REP)
                break

    print
    for runNumber in runNumberList:

        if __terminal or pSPECVersion is not None:   # reprocess was launched from terminal or from BsxCuBE while reprocessing data
            frameList = []
            for filename in os.listdir(pDirectory + "/raw"):
                if os.path.isfile(pDirectory + "/raw/" + filename):
                    prefix, run, frame, extra, extension = getFilenameDetails(filename)
                    if prefix == pPrefix and run == runNumber and frame != "":
                        if (pFrameFirst == "" or int(frame) >= int(pFrameFirst)) and (pFrameLast == "" or int(frame) <= int(pFrameLast)):
                            if pDetector == "0" and extension == "edf" or pDetector == "1" and extension == "gfrm":
                                try:
                                    frameList.index(frame)
                                except Exception:
                                    frameList.append(frame)
        else:   # reprocess was launched from BsxCuBE while collecting data
            frameList = ["%02d" % int(pFrameLast)]

        if len(frameList) == 0:
            showMessage(3, "There are no frames for run '%s'!" % runNumber)
        else:
            frameList.sort()
            for frame in frameList:

                if pDetector == "0":    # Pilatus
                    filenameRAW = "%s/raw/%s_%s_%s.edf" % (pDirectory, pPrefix, runNumber, frame)
                    sizeRAW = 4090000
                    sizeNOR = 4100000
                else:   # Vantec
                    filenameRAW = "%s/raw/%s_%s_%s.gfrm" % (pDirectory, pPrefix, runNumber, frame)
                    sizeRAW = 4200000
                    sizeNOR = 16780000

                if pKeepOriginal == "0":
                    filenameNOR = "%s/2d/%s_%s_%s.edf" % (pDirectory, pPrefix, runNumber, frame)
                    filenameLOG = "%s/misc/%s_%s_%s.log" % (pDirectory, pPrefix, runNumber, frame)
                    filenameMSK = "%s/misc/%s_%s_%s.msk" % (pDirectory, pPrefix, runNumber, frame)
                    filenameANG = "%s/misc/%s_%s_%s.ang" % (pDirectory, pPrefix, runNumber, frame)
                    filenameDAT = "%s/1d/%s_%s_%s.dat" % (pDirectory, pPrefix, runNumber, frame)
                else:
                    filenameNOR = "%s/%s_%s_%s.edf" % (directory2D_REP, pPrefix, runNumber, frame)
                    filenameLOG = "%s/%s_%s_%s.log" % (directoryMISC_REP, pPrefix, runNumber, frame)
                    filenameMSK = "%s/%s_%s_%s.msk" % (directoryMISC_REP, pPrefix, runNumber, frame)
                    filenameANG = "%s/%s_%s_%s.ang" % (directoryMISC_REP, pPrefix, runNumber, frame)
                    filenameDAT = "%s/%s_%s_%s.dat" % (directory1D_REP, pPrefix, runNumber, frame)

                if __terminal or pSPECVersion is not None:   # reprocess was launched from terminal or from BsxCuBE while reprocessing data
                    if pConcentration == "" or pComments == "" or pCode == "" or pMaskFile == "" or pDetectorDistance == "" or pWaveLength == "" or pPixelSizeX == "" or pPixelSizeY == "" or pBeamCenterX == "" or pBeamCenterY == "" or pNormalisation == "" or pBeamStopDiode == "" or pMachineCurrent == "":
                        filenameNOR_ORG = "%s/2d/%s_%s_%s.edf" % (pDirectory, pPrefix, runNumber, frame)
                        if os.path.exists(filenameNOR_ORG):
                            edf.open(filenameNOR_ORG)
                            header = edf.getHeader()

                            history0 = ""
                            history1 = ""
                            i = 0
                            while i < len(header):
                                if header[i].startswith("History-1 = "):
                                    history0 = header[i][12:]
                                    del header[i]
                                    i -= 1
                                elif header[i].startswith("History-1~1 = "):
                                    history1 = header[i][14:]
                                    del header[i]
                                    i -= 1
                                else:
                                    i += 1
                            header.append("history_combined = " + history0 + history1)
                            #print header

                            status, translate = hdfDictionary.translate(header, dictionary)
                            edf.close()
                        else:
                            translate = []
                            showMessage(3, "Trying to get values from file '%s' which doesn't exist" % filenameNOR_ORG)

                    #print translate
                else:   # reprocess was launched from BsxCuBE while collecting data
                    translate = []


                if pConcentration == "":
                    concentration = makeTranslation(translate, "concentration", "0")
                else:
                    concentration = pConcentration

                if pComments == "":
                    comments = makeTranslation(translate, "comments", "")
                else:
                    comments = pComments

                if pCode == "":
                    code = makeTranslation(translate, "code", "")
                else:
                    code = pCode

                if pMaskFile == "":
                    maskFile = makeTranslation(translate, "mask_file", "")
                else:
                    maskFile = pMaskFile

                if pDetectorDistance == "":
                    detectorDistance = makeTranslation(translate, "detector_distance", "0")
                else:
                    detectorDistance = pDetectorDistance

                if pWaveLength == "":
                    waveLength = makeTranslation(translate, "wave_length", "0")
                else:
                    waveLength = pWaveLength

                if pPixelSizeX == "":
                    pixelSizeX = makeTranslation(translate, "pixel_size_X", "0")
                else:
                    pixelSizeX = pPixelSizeX

                if pPixelSizeY == "":
                    pixelSizeY = makeTranslation(translate, "pixel_size_Y", "0")
                else:
                    pixelSizeY = pPixelSizeY

                if pBeamCenterX == "":
                    beamCenterX = makeTranslation(translate, "beam_center_X", "0")
                else:
                    beamCenterX = pBeamCenterX

                if pBeamCenterY == "":
                    beamCenterY = makeTranslation(translate, "beam_center_Y", "0")
                else:
                    beamCenterY = pBeamCenterY

                if pBeamStopDiode == "":
                    beamStopDiode = makeTranslation(translate, "diode_current", "0")
                else:
                    beamStopDiode = pBeamStopDiode

                if pMachineCurrent == "":
                    machineCurrent = makeTranslation(translate, "machine_current", "0")
                else:
                    machineCurrent = pMachineCurrent

                if pNormalisation == "":
                    normalisation = makeTranslation(translate, "normalization_factor", "0")
                else:
                    normalisation = pNormalisation


                if pOperation in ("-2", "-1", "0", "3"):
                    print "Normalising EDF frame '%s'..." % filenameNOR

                    if pKeepOriginal == "0":
                        os.system("rm -f %s %s 2>/dev/null" % (filenameNOR, filenameLOG))

                    status = waitFile(filenameRAW, sizeRAW, pTimeOut)
                    if status == 0:
                        if float(beamStopDiode) == 0:
                            showMessage(3, "The value of the beam stop diode is zero!")
                        else:
                            if pDetector == "0":    # Pilatus
                                command = "saxs_mac +var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 -otit \"DiodeCurr=%s, MachCurr=%s mA, Concentration=%s, Comments: %s, Code: %s, Mask: %s, Normalisation: %s\" -i1dis \"%s\" -i1wvl \"%s_nm\" -i1pix %s_um %s_um -i1cen %s %s -ofac %s %s %s > %s 2>/dev/null" % \
                                        (beamStopDiode, machineCurrent, concentration, comments, code, maskFile, normalisation, detectorDistance, waveLength, pixelSizeX, pixelSizeY, beamCenterX, beamCenterY, str(float(normalisation) / float(beamStopDiode)), filenameRAW, filenameNOR, filenameLOG)
                            else:           # Vantec
                                command = "saxs_mac +var +pass -omod n -i1err _i1val -i1dum -2 -i1ddum 1.1 -otit \"DiodeCurr=%s, MachCurr=%s mA, Concentration=%s, Comments: %s, Code: %s, Mask: %s, Normalisation: %s\" -odis \"%s\" -i1wvl \"%s_nm\" -i1pix %s_um %s_um -i1cen %s %s -ofac %s %s %s > %s 2>/dev/null" % \
                                        (beamStopDiode, machineCurrent, concentration, comments, code, maskFile, normalisation, detectorDistance, waveLength, pixelSizeX, pixelSizeY, beamCenterX, beamCenterY, str(float(normalisation) / float(beamStopDiode)), filenameRAW, filenameNOR, filenameLOG)
                            #print command 
                            if subprocess.call(command, shell=True) == 0:
                                showMessage(2, "The frame '%s' was normalised..." % filenameNOR, filenameNOR)
                            else:
                                showMessage(3, "Could not find 'saxs_mac' or it returned an error!")
                    elif status == 1:
                        print "Aborting data reprocess!"
                        sys.exit(0)
                    else:
                        showMessage(3, "File '%s' didn't appear on disk after '%s' seconds." % (filenameRAW, pTimeOut))


                if pOperation in ("-2", "-1", "1", "3"):
                    print "Generating 1D file '%s'..." % filenameDAT

                    if pKeepOriginal == "0":
                        os.system("rm -f %s %s %s 2>/dev/null" % (filenameDAT, filenameANG, filenameMSK))

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
                                    showMessage(2, "The 1D file '%s' was generated..." % filenameDAT, filenameDAT)
                                else:
                                    showMessage(3, "Could not find 'saxs_curves' or it returned an error!")
                            else:
                                showMessage(3, "Could not find 'saxs_angle' or it returned an error!")
                        else:
                            showMessage(3, "Could not find 'saxs_add' or it returned an error!")
                    elif status == 1:
                        print "Aborting data reprocess!"
                        sys.exit(0)
                    else:
                        showMessage(3, "File '%s' didn't appear on disk after '%s' seconds." % (filenameNOR, pTimeOut))


            if pOperation in ("-2", "1", "2", "3"):

                if pKeepOriginal == "0":
                    filenameDAT_AVE = "%s/1d/%s_%s_ave.dat" % (pDirectory, pPrefix, runNumber)
                    filenameANG_AVE = "%s/misc/%s_%s_ave.ang" % (pDirectory, pPrefix, runNumber)
                    filenameLOG_AVE = "%s/misc/%s_%s_ave.log" % (pDirectory, pPrefix, runNumber)
                    filenamePattern = "%s/misc/%s_%s_%s.ang" % (pDirectory, pPrefix, runNumber, "%%")
                else:
                    filenameDAT_AVE = "%s/%s_%s_ave.dat" % (directory1D_REP, pPrefix, runNumber)
                    filenameANG_AVE = "%s/%s_%s_ave.ang" % (directoryMISC_REP, pPrefix, runNumber)
                    filenameLOG_AVE = "%s/%s_%s_ave.log" % (directoryMISC_REP, pPrefix, runNumber)
                    filenamePattern = "%s/%s_%s_%s.ang" % (directoryMISC_REP, pPrefix, runNumber, "%%")

                print "Generating average '%s' from 1D files..." % filenameDAT_AVE

                if pKeepOriginal == "0":
                    os.system("rm -f %s %s %s 2>/dev/null" % (filenameDAT_AVE, filenameANG_AVE, filenameLOG_AVE))

                if pFrameFirst == "":
                    frameFirst = int(frameList[0])
                else:
                    frameFirst = int(pFrameFirst)

                if pFrameLast == "":
                    frameLast = int(frameList[-1])
                else:
                    frameLast = int(pFrameLast)

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
                        showMessage(2, "The average file '%s' was generated..." % filenameDAT_AVE, filenameDAT_AVE)
                    else:
                        showMessage(3, "Could not find 'saxs_curves' or it returned an error!")
                else:
                    showMessage(3, "Could not find 'saxs_mac' or it returned an error!")

    if __terminal or pSPECVersion is not None:
        showMessage(0, "The data reprocessing is done!")




def showMessage(pLevel, pMessage, pFilename=None):

    if globals()["REPROCESS_STATUS"] is not None:
        currentStatus = globals()["REPROCESS_STATUS"].value["reprocess"]["status"]     # must do this, since SpecClient is apparently returning a non-expected data structure
        i = currentStatus.rfind(",")
        # TB: This ,1 or ,0 suffix nonsense seems to be a hack to force Spec to signal a variable change to bsxcube
        if i == -1 or currentStatus[i + 1:] == "1":
            if pFilename is None:
                newStatus = "%s,%s,0" % (pLevel, pMessage)
            else:
                newStatus = "%s,%s,%s,0" % (pLevel, pMessage, pFilename)
        else:
            if pFilename is None:
                newStatus = "%s,%s,1" % (pLevel, pMessage)
            else:
                newStatus = "%s,%s,%s,1" % (pLevel, pMessage, pFilename)
        globals()["REPROCESS_STATUS"].setValue(newStatus)

    if globals()["REPROCESS_ABORT"] is not None:
        if globals()["REPROCESS_ABORT"].value["reprocess"]["abort"] == "1":    # must do this, since SpecClient is apparently returning a non-expected data structure
            print "Aborting data reprocess!"
            sys.exit(0)

    print pMessage




def makeTranslation(pTranslate, pKeyword, pDefaultValue):

    for keyword, value in pTranslate:
        if keyword == pKeyword:
            newValue = ""
            for i in range(0, len(value)):
                if value[i] != "\"":
                    newValue += value[i]
            return newValue

    if len(pTranslate) > 0:
        showMessage(3, "Trying to get value '%s' which doesn't exist!" % pKeyword)

    return pDefaultValue




def waitFile(pFilename, pSize, pTimeOut):

    timeOut = int(pTimeOut)
    while timeOut > 0:
        time.sleep(0.5)
        if os.path.exists(pFilename):
            os.system("stat $(dirname %s) > /dev/null" % pFilename)
            if os.path.getsize(pFilename) >= pSize:
                return 0
        else:
            if globals()["REPROCESS_ABORT"] is not None and globals()["REPROCESS_ABORT"].value["reprocess"]["abort"] == "1":   # must do this, since SpecClient is apparently returning a non-expected data structure
                return 1
        timeOut -= 0.5

    return - 1



def getFilenameDetails(pFilename):
    pFilename = str(pFilename)
    i = pFilename.rfind(".")
    if i == -1:
        file = pFilename
        extension = ""
    else:
        file = pFilename[:i]
        extension = pFilename[i + 1:]
    items = file.split("_")
    prefix = items[0]
    run = ""
    frame = ""
    extra = ""
    i = len(items)
    j = 1
    while j < i:
        if items[j].isdigit():
            run = items[j]
            j += 1
            break
        else:
            prefix.join("_".join(items[j]))
            j += 1
    if j < i:
        if items[j].isdigit():
            frame = items[j]
            j += 1
        while j < i:
            if extra == "":
                extra = items[j]
            else:
                extra.join("_".join(items[j]))
            j += 1

    return prefix, run, frame, extra, extension



if __name__ == "__main__":

    try:

        __parameters = {}

        if len(sys.argv) == 1:

            filenameREP = os.path.join(sys.path[0], "Reprocess.txt")

            if os.path.exists(filenameREP):
                handler = open(filenameREP, "r")
                __parameters["detector"] = handler.readline()[:-1]
                __parameters["operation"] = handler.readline()[:-1]
                __parameters["directory"] = handler.readline()[:-1]
                __parameters["prefix"] = handler.readline()[:-1]
                __parameters["keepOriginal"] = handler.readline()[:-1]
                handler.close()
            else:
                __parameters["detector"] = ""
                __parameters["operation"] = ""
                __parameters["directory"] = ""
                __parameters["prefix"] = ""
                __parameters["keepOriginal"] = ""

            __parameters["concentration"] = ""
            __parameters["comments"] = ""
            __parameters["code"] = ""
            __parameters["maskFile"] = ""
            __parameters["detectorDistance"] = ""
            __parameters["waveLength"] = ""
            __parameters["pixelSizeX"] = ""
            __parameters["pixelSizeY"] = ""
            __parameters["beamCenterX"] = ""
            __parameters["beamCenterY"] = ""
            __parameters["normalisation"] = ""
            __parameters["beamStopDiode"] = ""
            __parameters["machineCurrent"] = ""


            print

            while True:
                input = raw_input("0=Pilatus; 1=Vantec (empty='%s'): " % __parameters["detector"])
                if input == "":
                    input = __parameters["detector"]
                if input in ("0", "1"):
                    __parameters["detector"] = input
                    break
                else:
                    print "Wrong option!"

            while True:
                input = raw_input("0=Normalisation; 1=Reprocess; 2=Average; 3=Complete reprocess (empty='%s'): " % __parameters["operation"])
                if input == "":
                    input = __parameters["operation"]
                if input in ("0", "1", "2", "3"):
                    __parameters["operation"] = input
                    break
                else:
                    print "Wrong option!"

            while True:
                input = raw_input("Directory (empty='%s'): " % __parameters["directory"])
                if input == "":
                    input = __parameters["directory"]
                if os.path.exists(input) and not os.path.isfile(input):
                    __parameters["directory"] = input
                    break
                else:
                    print "Directory '%s' not found!" % input

            while True:
                input = raw_input("Prefix (empty='%s'): " % __parameters["prefix"])
                if input == "":
                    input = __parameters["prefix"]
                flag = False
                for filename in os.listdir(__parameters["directory"] + "/raw"):
                    if os.path.isfile(__parameters["directory"] + "/raw/" + filename):
                        prefix, run, frame, extra, extension = getFilenameDetails(filename)
                        if prefix == input and run != "" and frame != "" and (__parameters["detector"] == "0" and extension == "edf" or __parameters["detector"] == "1" and extension == "gfrm"):
                            flag = True
                            break
                if flag:
                    __parameters["prefix"] = input
                    break
                else:
                    print "Prefix '%s' not found!" % input

            while True:
                __parameters["runNumber"] = raw_input("Run # (empty=all): ")
                if __parameters["runNumber"] == "":
                    break
                else:
                    runNumberList = []
                    list = __parameters["runNumber"].split(",")
                    for runNumber in list:
                        runNumber = "%03d" % int(runNumber)
                        try:
                            runNumberList.index(runNumber)
                        except Exception:
                            runNumberList.append(runNumber)

                    for runNumber in runNumberList:
                        flag = False
                        for filename in os.listdir(__parameters["directory"] + "/raw"):
                            if os.path.isfile(__parameters["directory"] + "/raw/" + filename):
                                prefix, run, frame, extra, extension = getFilenameDetails(filename)
                                if prefix == __parameters["prefix"] and run == runNumber and frame != "" and (__parameters["detector"] == "0" and extension == "edf" or __parameters["detector"] == "1" and extension == "gfrm"):
                                    flag = True
                                    break
                        if not flag:
                            break
                    if flag:
                        break
                    else:
                        print "Run '%s' not found!" % runNumber

            if __parameters["runNumber"] == "" or len(__parameters["runNumber"].split(",")) > 1:
                __parameters["frameFirst"] = ""
                __parameters["frameLast"] = ""
            else:
                __parameters["frameFirst"] = raw_input("First frame (empty=first): ")
                while True:
                    __parameters["frameLast"] = raw_input("Last frame (empty=last): ")
                    if __parameters["frameFirst"] == "" or __parameters["frameLast"] == "" or int(__parameters["frameFirst"]) <= int(__parameters["frameLast"]):
                        break
                    else:
                        print "Last frame is lower than first frame!"


            if __parameters["operation"] in ("1", "3"):
                __parameters["concentration"] = raw_input("New concentration (empty=from header): ")

                __parameters["comments"] = raw_input("New comments (empty=from header): ")

                __parameters["code"] = raw_input("New code (empty=from header): ")

                while True:
                    __parameters["maskFile"] = raw_input("New mask file (empty=from header): ")
                    if __parameters["maskFile"] == "" or os.path.isfile(__parameters["maskFile"]):
                        break
                    else:
                        print "Mask file '%s' not found!" % __parameters["maskFile"]

                __parameters["detectorDistance"] = raw_input("New detector distance (empty=from header): ")

                __parameters["waveLength"] = raw_input("New wave length (empty=from header): ")

                __parameters["pixelSizeX"] = raw_input("New pixel size X (empty=from header): ")

                __parameters["pixelSizeY"] = raw_input("New pixel size Y (empty=from header): ")

                __parameters["beamCenterX"] = raw_input("New beam center X (empty=from header): ")

                __parameters["beamCenterY"] = raw_input("New beam center Y (empty=from header): ")

            if __parameters["operation"] in ("0", "3"):
                __parameters["normalisation"] = raw_input("New normalisation (empty=from header): ")

                __parameters["beamStopDiode"] = raw_input("New beam stop diode (empty=from header): ")

            if __parameters["operation"] in ("1", "3"):
                __parameters["machineCurrent"] = raw_input("New machine current (empty=from header): ")

            while True:
                input = raw_input("Keep original files (empty='%s'): " % __parameters["keepOriginal"])
                if input == "":
                    input = __parameters["keepOriginal"]
                if input in ("y", "Y", "n", "N"):
                    __parameters["keepOriginal"] = input
                    break
                else:
                    print "Wrong option!"



            handler = open(filenameREP, "w")
            handler.write(__parameters["detector"] + "\n")
            handler.write(__parameters["operation"] + "\n")
            handler.write(__parameters["directory"] + "\n")
            handler.write(__parameters["prefix"] + "\n")
            handler.write(__parameters["keepOriginal"] + "\n")
            handler.close()

            if __parameters["keepOriginal"] in ("y", "Y"):
                __parameters["keepOriginal"] = "1"
            else:
                __parameters["keepOriginal"] = "0"

            __timePerFrame = ""
            __timeOut = 20
            __SPECVersion = None
            __SPECVariableStatus = None
            __SPECVariableAbort = None
            __terminal = True
            flag = True

        elif len(sys.argv) == 26:
            __parameters["detector"] = sys.argv[1]
            __parameters["operation"] = sys.argv[2]
            __parameters["directory"] = sys.argv[3]
            __parameters["prefix"] = sys.argv[4]
            __parameters["runNumber"] = sys.argv[5]
            __parameters["frameFirst"] = sys.argv[6]
            __parameters["frameLast"] = sys.argv[7]
            __parameters["concentration"] = sys.argv[8]
            __parameters["comments"] = sys.argv[9]
            __parameters["code"] = sys.argv[10]
            __parameters["maskFile"] = sys.argv[11]
            __parameters["detectorDistance"] = sys.argv[12]
            __parameters["waveLength"] = sys.argv[13]
            __parameters["pixelSizeX"] = sys.argv[14]
            __parameters["pixelSizeY"] = sys.argv[15]
            __parameters["beamCenterX"] = sys.argv[16]
            __parameters["beamCenterY"] = sys.argv[17]
            __parameters["normalisation"] = sys.argv[18]
            __parameters["beamStopDiode"] = sys.argv[19]
            __parameters["machineCurrent"] = sys.argv[20]
            __parameters["keepOriginal"] = sys.argv[21]

            __timeOut = sys.argv[22]
            __SPECVersion = sys.argv[23]
            __SPECVariableStatus = sys.argv[24]
            __SPECVariableAbort = sys.argv[25]

            if __SPECVersion == "":
                __SPECVersion = None

            if __SPECVariableStatus == "":
                __SPECVariableStatus = None

            if __SPECVariableAbort == "":
                __SPECVariableAbort = None

            __terminal = False

            flag = True
        else:
            print
            print "Number of parameters is not correct. Need 25 parameters and %s were provided!" % (len(sys.argv) - 1)
            flag = False

        #print __parameters

        if flag:
            Reprocess(__parameters["detector"], __parameters["operation"], __parameters["directory"], __parameters["prefix"], __parameters["runNumber"], __parameters["frameFirst"], \
                      __parameters["frameLast"], __parameters["concentration"], __parameters["comments"], __parameters["code"], __parameters["maskFile"], __parameters["detectorDistance"], \
                      __parameters["waveLength"], __parameters["pixelSizeX"], __parameters["pixelSizeY"], __parameters["beamCenterX"], __parameters["beamCenterY"], \
                      __parameters["normalisation"], __parameters["beamStopDiode"], __parameters["machineCurrent"], __parameters["keepOriginal"], __timeOut, __SPECVersion, __SPECVariableStatus, __SPECVariableAbort, __terminal)

    except KeyboardInterrupt:
        print
        print "Exiting..."
        print
    except SystemExit:
        pass


