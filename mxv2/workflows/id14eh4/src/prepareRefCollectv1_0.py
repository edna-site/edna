# Script for preparing data collection

import os, time

def createPyArchFilePath(_strFileDirectoryPath):
    """
    This method translates from a "visitor" path to a "pyarch" path:
    /data/visitor/mx415/id14eh1/20100209 -> /data/pyarch/id14eh1/mx415/20100209
    """
    strPyarchDNAFilePath = None
    listOfDirectories = _strFileDirectoryPath.split(os.sep)
    listBeamlines = ["bm14", "id14eh1", "id14eh2", "id14eh3", "id14eh4", "id23eh1", "id23eh2", "id29"]
    # Check that we have at least four levels of directories:
    if (len(listOfDirectories) > 4):
        strDataDirectory = listOfDirectories[ 1 ]
        strSecondDirectory = listOfDirectories[ 2 ]
        strProposal = None
        strBeamline = None
        if ((strDataDirectory == "data") and (strSecondDirectory == "visitor")):
            strProposal = listOfDirectories[ 3 ]
            strBeamline = listOfDirectories[ 4 ]
        elif ((strDataDirectory == "data") and (strSecondDirectory in listBeamlines)):
            strBeamline = strSecondDirectory
            strProposal = listOfDirectories[ 4 ]
        if (strProposal != None) and (strBeamline != None):
            strPyarchDNAFilePath = os.path.join(os.sep, "data")
            strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, "pyarch")
            strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strBeamline)
            strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strProposal)
            for strDirectory in listOfDirectories[ 5: ]:
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strDirectory)
    if (strPyarchDNAFilePath is None):
        EDVerbose.WARNING("EDPluginControlInterfaceToMXCuBEv1_3.createPyArchDNAFilePath: path not converted for pyarch: %s " % _strFileDirectoryPath)
    return strPyarchDNAFilePath

archive_dir = createPyArchFilePath(directory)
collection_message = "Starting a reference image data collection..."
collection_start_time = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime( time.time() ) )
comment = "Image created for EDNA characterisation"