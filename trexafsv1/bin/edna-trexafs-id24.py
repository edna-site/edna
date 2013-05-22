import os, sys

strProgramPath = os.path.abspath(sys.argv[0])
pyListPath = strProgramPath.split(os.sep)
if len(pyListPath) > 3:
    strEdnaHomePath = os.sep.join(pyListPath[:-3])
else:
    print ("Problem in the EDNA_HOME path ..." + strEdnaHomePath)
    sys.exit()
os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("XSDataTRExafsv1_0")
EDFactoryPluginStatic.loadModule("XSDataReadDataID24v1_0")

from XSDataReadDataID24v1_0 import XSDataInputReadDataID24
from XSDataTRExafsv1_0 import XSDataInputTRExafs

if __name__ == '__main__':
    strDataPath = None
    fEnergyCalibA = 0
    fEnergyCalibB = 0
    for iIndex, strArg in enumerate(sys.argv[1:]):
        strarg = strArg.lower()
        if strarg == "--data":
            strDataPath = sys.argv[iIndex + 2]
        elif strarg == "--a":
            fEnergyCalibA = float(sys.argv[iIndex + 2])
        elif strarg == "--b":
            fEnergyCalibB = float(sys.argv[iIndex + 2])
    print strDataPath, fEnergyCalibA, fEnergyCalibB
    XSDataInputReadDataID24 = XSDataInputReadDataID24()
    XSDataInputReadDataID24.inputFile = None