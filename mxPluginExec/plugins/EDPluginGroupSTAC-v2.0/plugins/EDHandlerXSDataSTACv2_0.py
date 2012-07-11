#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    Contributors:      Olof Svensson (svensson@esrf.fr) 


__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"


from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

EDFactoryPluginStatic.loadModule("XSDataMXv1")

from XSDataMXv1 import XSDataCell
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataDetector
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataVectorDouble

import XSDataMXv1
EDFactoryPluginStatic.loadModule("XSDataSTACv2_0")
import XSDataSTACv2_0

EDFactoryPluginStatic.loadModule("EDHandlerXSDataCommon")
from EDHandlerXSDataCommon import EDHandlerXSDataCommon

import math

class EDHandlerXSDataSTACv2_0:


    @staticmethod
    def removeOrientation(_possible_orientation, kappa, phi):
        '''
        _possible_orientation: the list of orientation 
        
        result:
        newpossibleOrientations(XSDataSTACv2_0.kappa_alignment_response): the list of orientations filtered not to contain the orientation used
        '''
        tol = 0.1

        try:
            newpossibleOrientations = XSDataSTACv2_0.kappa_alignment_response.parseString(_possible_orientation.marshal())
        except:
            newpossibleOrientations = None
        if newpossibleOrientations is not None:
            Orients = _possible_orientation.getPossible_orientation()
            newpossibleOrientations.setPossible_orientation([])
            for i in range(0, Orients.__len__()):
                if not (math.fabs(float(Orients[i].getKappa()) - float(kappa)) < tol and math.fabs(float(Orients[i].getPhi()) - float(phi)) < tol):
                    newpossibleOrientations.addPossible_orientation(Orients[i])
        return newpossibleOrientations



