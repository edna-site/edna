# coding: utf8
#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 - ESRF Grenoble
#
#    Principal author:       Jérôme Kieffer
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
List of Sinograms to write:
sinogramPhotonFlux.edf
sinogramIntgratedRaw.edf
sinogramIntegratedCor.edf
sinogramROIxx-yyRaw.edf
sinogramROIxx-yyRaw.edf
We should first calculate the sinogram in memory before creating a lock
"""


import time, random, os, sys
from CIFfile    import  CIF
import numpy    as NP
from  EdfFile   import EdfFile


def lockFile(suffix="image", path='.', basename="lock"):
    """retrurns the name of a lockfile
    @rtype: string
    @return: path for a lock file
    """
    strLockName = "%s.%s" % (basename, suffix)
    strLockPath = os.path.join(path, strLockName)
    filename = open(strLockPath, "w")
    filename.write(str(os.getpid()))
    filename.close()
    time.sleep(1.0)
    Locked = False
    for onefile in os.listdir(path):
        if onefile.find(basename) == 0 and onefile != strLockName:
            Locked = True

    while  Locked:
        os.remove(strLockFile)
        time.sleep(random.random())
        filename = open(strLockPath, "w")
        filename.write(str(os.getpid()))
        filename.close()
        Locked = False
        for onefile in os.listdir(path):
            if onefile.find(basename) == 0 and onefile != strLockName: #then we are in a trouble
                Locked = True
    return   strLockPath


class PowderIntegrator():
    """This is a class calculating the integral (sum) of the diffracted intensity   """
    def __init__(self, cif):
        """the initialisation of the class takes a CIF dictionary as input
        @param cif:  the representation of the CIF dictionary 
        @type cif:   python dictionary.
        """
        self.cif = cif
        self.pyfTwoThetaMin = float(self.cif[ "_pd_meas_2theta_range_min" ])
        self.pyfTwoThetaMax = float(self.cif[ "_pd_meas_2theta_range_max" ])
        self.pyintNbPoints = int (self.cif[  "_pd_meas_number_of_points" ])
#        self.pyfTwoThetaStep = float( self.cif[  "_pd_meas_2theta_range_inc" ] )  #This is not precise enough 
        self.pyfTwoThetaStep = (self.pyfTwoThetaMax - self.pyfTwoThetaMin) / (self.pyintNbPoints - 1.0)
        self.pyintXpos = None
        self.pyintYpos = None
        self.pyfPhotonFlux = float(cif["_synchrotron_photon-flux"])



#        npaIntensities = None #NP.array([])
        for oneloop in self.cif[ "loop_" ]:
            if "_pd_meas_intensity_total" in oneloop[0]:
                self.npaIntensities = NP.array([ float(i[ "_pd_meas_intensity_total" ]) for i in oneloop[1] ])
#        print self.npaIntensities
#        self.npaTwoThetha=NP.array(range( self.pyintNbPoints ) ) * self.pyfTwoThetaStep + self.pyfTwoThetaMin
#        print self.npaTwoThetha
#        print len(self.npaIntensities), len(self.npaTwoThetha)
#        f=open("PowderDiffraction.dat","w")
#        for i in range(self.pyintNbPoints):
#            f.write("%f\t%f\n"%(self.npaTwoThetha[i],self.npaIntensities[i]))
#        f.close()        

    def integrate(self, pyfTwoThetaStart=0.0, pyfTwoThetaStop=180.0):
        """Does the integration between the 2\q min and 2\q max
        @param  pyfTwoThetaStart: angle in degrees to start integration
        @type   pyfTwoThetaStart: python float
        @param  pyfTwoThetaStop: angle in degrees to stop the integration
        @type   pyfTwoThetaStop: python float
        @return: integrated value of diffracted intensity
        @rtype:    python float
        """
        pyintStart = max(0, int(round((pyfTwoThetaStart - self.pyfTwoThetaMin) / self.pyfTwoThetaStep)))
        pyintStop = min(self.pyintNbPoints, int(round((pyfTwoThetaStop - self.pyfTwoThetaMin) / self.pyfTwoThetaStep)))
        return self.npaIntensities [ pyintStart : pyintStop ].sum() / self.pyfTwoThetaStep

    def getEmptySinogramArray(self):
        """Generates an empty matrix of the right size considering the data 
        """
        if  cif["_tomo_scan_type"].lower() in ["flat", "spiral"]:
            pyintSinogramSizeX = 1 + int(abs((float(cif[ "_tomo_spec_displ_x_max" ]) - float (cif [ "_tomo_spec_displ_x_min" ])) / float(cif["_tomo_spec_displ_x_inc"])))
            pyintSinogramSizeY = 1 + int(abs(float(cif[ "_tomo_scan_ampl" ]) / float(cif[ "_tomo_spec_displ_rotation_inc" ])))
            self.pyintXpos = int(abs((float(cif[ "_tomo_spec_displ_x" ]) - float (cif [ "_tomo_spec_displ_x_min" ])) / float(cif["_tomo_spec_displ_x_inc"])))
            self.pyintYpos = int(abs(float(cif[ "_tomo_spec_displ_rotation" ]) / float(cif[ "_tomo_spec_displ_rotation_inc" ])))
        if cif["_tomo_scan_type"].lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
            pyintSinogramSizeX = 1 + int(abs((float(cif[ "_tomo_spec_displ_x_max" ]) - float (cif [ "_tomo_spec_displ_x_min" ])) / float(cif["_tomo_spec_displ_x_inc"])))
            pyintSinogramSizeY = 1 + int(abs((float(cif[ "_tomo_spec_displ_z_max" ]) - float (cif [ "_tomo_spec_displ_z_min" ])) / float(cif["_tomo_spec_displ_z_inc"])))
            self.pyintXpos = int(abs((float(cif[ "_tomo_spec_displ_x" ]) - float (cif [ "_tomo_spec_displ_x_min" ])) / float(cif["_tomo_spec_displ_x_inc"])))
            self.pyintYpos = int(abs((float(cif[ "_tomo_spec_displ_z" ]) - float (cif [ "_tomo_spec_displ_z_min" ])) / float(cif["_tomo_spec_displ_z_inc"])))
        return NP.zeros((pyintSinogramSizeX, pyintSinogramSizeY))



    def getSinogramPosition(self):
        """calculates the size of the sinogram considering the piece of intomations available in the CIF file
        @rtype: 2-tuple of integers
        @return: the size in X,Y in pixels of the image of the sinogram
        """
        if   self.pyintXpos is None:
            if  self.cif["_tomo_scan_type"].lower() in ["flat", "spiral"]:
                self.pyintXpos = int(abs((float(self.cif[ "_tomo_spec_displ_x" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"])))
                self.pyintYpos = int(abs(float(self.cif[ "_tomo_spec_displ_rotation" ]) / float(self.cif[ "_tomo_spec_displ_rotation_inc" ])))
            if cif["_tomo_scan_type"].lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
                self.pyintXpos = int(abs((float(self.cif[ "_tomo_spec_displ_x" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"])))
                self.pyintYpos = int(abs((float(self.cif[ "_tomo_spec_displ_z" ]) - float (self.cif [ "_tomo_spec_displ_z_min" ])) / float(self.cif["_tomo_spec_displ_z_inc"])))
        return self.pyintXpos, self.pyintYpos

############################################################################################
###################### Start of the program  ############################################### 
############################################################################################

if len(sys.argv) == 2:
    strPathToCif = sys.argv[1]
else:
    strPathToCif = "test-powder.cif"

pystSinogramFilename = "test-sinogram.edf"
cif = CIF()
cif.loadCIF(strPathToCif)
if not cif.exists("_tomo_scan_type"):
    print "How do you want to generate a Sinogram if you are lacking essential things like the scan type"
pydMetaDataEDF = cif.copy()
pydMetaDataEDF.pop("loop_")
pydMetaDataEDF.pop("_synchrotron_photon-flux")
pydMetaDataEDF.pop("_synchrotron_ring-intensity")
pydMetaDataEDF.pop("_tomo_spec_displ_rotation")
pydMetaDataEDF.pop("_tomo_spec_displ_x")
pydMetaDataEDF.pop("_tomo_spec_displ_z")

roi = PowderIntegrator(cif)
pyintXpos, pyintYpos = roi.getSinogramPosition()

strLockFile = lockFile(suffix=os.path.splitext(strPathToCif)[0], path='.', basename="lock")

startWriteTime = time.time()

for pystSinogramFilename in [ "sinogramPhotonFlux.edf", "sinogramIntegratedRaw.edf", "sinogramIntegratedCor.edf"]:
    if  os.path.isfile(pystSinogramFilename):
        edf = EdfFile(pystSinogramFilename)
        npSinogramArray = edf.GetData(0)
    else:
        npSinogramArray = roi.getEmptySinogramArray()
        edf = EdfFile(pystSinogramFilename)

    if pystSinogramFilename == "sinogramPhotonFlux.edf":
        npSinogramArray[ pyintXpos , pyintYpos ] = roi.pyfPhotonFlux
    elif pystSinogramFilename == "sinogramIntegratedRaw.edf":
        npSinogramArray[ pyintXpos , pyintYpos ] = roi.integrate()
    elif pystSinogramFilename == "sinogramIntegratedCor.edf":
        npSinogramArray[ pyintXpos , pyintYpos ] = roi.integrate() / roi.pyfPhotonFlux
    edf.WriteImage(pydMetaDataEDF, npSinogramArray, Append=0)

pylRegionsOfInterest = [ ]

if cif.exists("_pd_sum_2theta_range_min"):
    pylRegionsOfInterest.append([ float(cif["_pd_sum_2theta_range_min"]) , float(cif["_pd_sum_2theta_range_max"]) ])
else:
    for oneloop in cif[ "loop_" ]:
        if "_pd_sum_2theta_range_min" in oneloop[0]:
            for i in oneloop[1] :
                pylRegionsOfInterest.append([ float(i["_pd_sum_2theta_range_min"]) , float(i["_pd_sum_2theta_range_max"]) ])

for region in pylRegionsOfInterest:
    for basename in [ "Raw.edf", "Cor.edf" ]:
        pystSinogramFilename = "sinogramROI%i-%i%s" % (int(region[0]), int(region[1]), basename)
        if  os.path.isfile(pystSinogramFilename):
            edf = EdfFile(pystSinogramFilename)
            npSinogramArray = edf.GetData(0)
        else:
            npSinogramArray = roi.getEmptySinogramArray()
            edf = EdfFile(pystSinogramFilename)
        if basename == "Raw.edf":
            npSinogramArray[ pyintXpos , pyintYpos ] = roi.integrate(*tuple(region))
        elif basename == "Cor.edf":
            npSinogramArray[ pyintXpos , pyintYpos ] = roi.integrate(*tuple(region)) / roi.pyfPhotonFlux
        edf.WriteImage(pydMetaDataEDF, npSinogramArray, Append=0)

print time.time() - startWriteTime

os.remove(strLockFile)


