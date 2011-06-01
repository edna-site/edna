# -*- coding: utf8 -*-
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "2010/07/29"

DETECTORS = ["pilatus", "vantec"]
OPERATIONS = ["normalisation", "reprocess", "average", "complete"]
#RAWDIR = "raw"

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

global REPROCESS_STATUS, REPROCESS_ABORT

REPROCESS_STATUS = None
REPROCESS_ABORT = None


def Reprocess(pDetector, pOperation, pDirectory, pPrefix, pRunNumber, pFrameFirst, pFrameLast, pConcentration, pComments, pCode, \
              pMaskFile, pDetectorDistance, pWaveLength, pPixelSizeX, pPixelSizeY, pBeamCenterX, pBeamCenterY, pNormalisation, pBeamStopDiode, \
              pMachineCurrent, pKeepOriginal, pTimeOut, pSPECVersion, pSPECVariableStatus, pSPECVariableAbort, pTerminal):

    def doOneRunNumber(runNumber):
        """
        Attempt to separate the loop over the run-numbers
        """
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
                                except:
                                    frameList.append(frame)
        else:   # reprocess was launched from BsxCuBE while collecting data
            frameList = ["%02d" % int(pFrameLast)]






def showMessage(pLevel, pMessage, pFilename=None):
    """Similar to logging module of python but for udating BioSaxsCube ???
    
    @param pLevel: print level seems to be
                    4 for Errors
                    3 for Warnings
                    2 for Info
                    1
                    0
    @type pLevel: int
    @param pMessage: comment to be printed
    @type pMessage: string
    @param pFilename: the file related to the message (nothing to do with a logfile)
    @type pFilename: string or None
    """

    if REPROCESS_STATUS is not None:
        currentStatus = REPROCESS_STATUS.getValue()["reprocess"]["status"]     # must do this, since SpecClient is apparently returning a non-expected data structure
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

    if (REPROCESS_ABORT is not None) and (REPROCESS_ABORT.getValue()["reprocess"]["abort"]) == "1":
        # must do this, since SpecClient is apparently returning a non-expected data structure
        print "Aborting data reprocess!"
        sys.exit(0)

    print pMessage




def makeTranslation(pTranslate, pKeyword, pDefaultValue):
    """
    ????
    
     
    @type pTranslate: list ??
    @param pKeyword: the given keyword to be replaced
    @param pDefaultValue: default value fot the keyword
    """
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
    """
    Wait for a file to reach the given/expected size (unless timeout)
    
    @param pFilename: name of the file
    @type pFilename: string
    @param pSize: size of the file to reach
    @type pSize: scalar (int or float)
    @param pTimeOut: timeout
    @type pTimeOut: scalar (int or float) or a string representing an int
    
    @return:  0 if the file reached the good size,
             -1 if timeout is reached
              1 if there is no file and the system expects to abort
    @rtype: int  
    """
    timeOut = int(pTimeOut)
    while timeOut > 0:
        time.sleep(0.5)
        if os.path.exists(pFilename):
#            os.stat(os.path.dirname(pFilename))
            if os.path.getsize(pFilename) >= pSize:
                return 0
        else:
            if REPROCESS_ABORT is not None and REPROCESS_ABORT.getValue()["reprocess"]["abort"] == "1":
                # must do this, since SpecClient is apparently returning a non-expected data structure
                return 1
        timeOut -= 0.5

    return - 1



def getFilenameDetails(pFilename):
    """
    Split the name of the file in 4 components:
    prefix_run_frame_extra.extension
    @return: prefix, run, frame, extra, extension
    @rtype: 4-tuple of strings
    """
    pFilename = str(pFilename)
    file, extension = os.path.splitext(pFilename)

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
                    __parameters["detector"] = DETECTORS [int(input)]
                    break
                else:
                    print "Wrong option!"

            while True:
                input = raw_input("0=Normalisation; 1=Reprocess; 2=Average; 3=Complete reprocess (empty='%s'): " % __parameters["operation"])
                if input == "":
                    input = __parameters["operation"]
                if input in ("0", "1", "2", "3"):
                    __parameters["operation"] = OPERATIONS[int(input)]
                    break
                else:
                    print "Wrong option!"

            while True:
                input = raw_input("Directory (empty='%s'): " % __parameters["directory"])
                if input == "":
                    input = __parameters["directory"]
                if os.path.isdir(input):
                    __parameters["directory"] = input
                    break
                else:
                    print "Directory '%s' not found!" % input

            while True:
                input = raw_input("Prefix (empty='%s'): " % __parameters["prefix"])
                if input == "":
                    input = __parameters["prefix"]
                flag = False
                for filename in os.listdir(os.path.join(__parameters["directory"], RAWDIR)):
                    if os.path.isfile(os.path.join(__parameters["directory"], RAWDIR, filename)):
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
                    for runNumber in __parameters["runNumber"].split(","):
                        runNumber = "%03d" % int(runNumber)
                        if runNumber not in runNumberList:
                            runNumberList.append(runNumber)

                    for runNumber in runNumberList:
                        flag = False
                        for filename in os.listdir(os.path.join(__parameters["directory"], RAWDIR)):
                            if os.path.isfile(os.path.join(__parameters["directory"], RAWDIR, filename)):
                                prefix, run, frame, extra, extension = getFilenameDetails(filename)
                                if prefix == __parameters["prefix"] and run == runNumber and frame != "" and (\
                                        __parameters["detector"] == "pilatus" and extension == "edf" or \
                                        __parameters["detector"] == "vantec" and extension == "gfrm"):
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
                __parameters[""] = raw_input("New concentration (empty=from header): ")

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
                else:
                    reducedInput = input[0].lower()
                    if reducedInput in ("y" "n"):
                        __parameters["keepOriginal"] = input.lower()
                        break
                print "Wrong option!"



            handler = open(filenameREP, "w")
            handler.write(__parameters["detector"] + "\n")
            handler.write(__parameters["operation"] + "\n")
            handler.write(__parameters["directory"] + "\n")
            handler.write(__parameters["prefix"] + "\n")
            handler.write(__parameters["keepOriginal"] + "\n")
            handler.close()

#            if __parameters["keepOriginal"] in ("y", "Y"):
#                __parameters["keepOriginal"] = "1"
#            else:
#                __parameters["keepOriginal"] = "0"

            __timePerFrame = ""
            __timeOut = 20
            __SPECVersion = None
            __SPECVariableStatus = None
            __SPECVariableAbort = None
            __terminal = True
            flag = True

        elif len(sys.argv) == 26:

            if len(sys.argv[1]) == 1:
                __parameters["detector"] = DETECTORS[int(sys.argv[1])]
            else:
                __parameters["detector"] = sys.argv[1]

            if len(sys.argv[2]) < 3:
                __parameters["operation"] = OPERATIONS[int(sys.argv[2])]
            else:
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

            if sys.argv[21][0].lower() in [0, "n"]:
                __parameters["keepOriginal"] = "n"
            elif sys.argv[21][0].lower() in [1, "y"]:
                __parameters["keepOriginal"] = "y"

            __timeOut = sys.argv[22]
            __SPECVersion = sys.argv[23]
            __SPECVariableStatus = sys.argv[24]
            __SPECVariableAbort = sys.argv[25]


#this is impossible
#            if __SPECVersion == "":
#                __SPECVersion = None
#
#            if __SPECVariableStatus == "":
#                __SPECVariableStatus = None
#
#            if __SPECVariableAbort == "":
#                __SPECVariableAbort = None

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


