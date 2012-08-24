#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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


from EDVerbose            import  EDVerbose
from EDPluginExec           import  EDPluginExec
from EDMessage              import  EDMessage
from EDUtilsPath            import  EDUtilsPath
#from EDApplication          import  EDApplication
from XSDataDiffractionCTv1  import  XSDataInputWriteSinogram
from XSDataDiffractionCTv1  import  XSDataResultWriteSinogram
from XSDataCommon           import  XSDataFile, XSDataString
from CIFfile                import  CIF
from Borg2DImageWriter      import  Borg2DImageWriter
import time                 as      PyTime
import os                   as      PyOs
import random               as      PyRandom
import numpy                as      NP


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
        self.pyintSinogramSizeX = None
        self.pyintSinogramSizeY = None
        self.pydIntergratedCache = {}
        self.pyfPhotonFlux = float(cif["_synchrotron_photon-flux"])
        npaIntensities = None #NP.array([])
        for oneloop in self.cif[ "loop_" ]:
            if "_pd_meas_intensity_total" in oneloop[0]:
                self.npaIntensities = NP.array([ float(i[ "_pd_meas_intensity_total" ]) for i in oneloop[1] ])

    def integrate(self, pyfTwoThetaStart=0.0, pyfTwoThetaStop=180.0):
        """Does the integration between the 2\q min and 2\q max
        @param  pyfTwoThetaStart: angle in degrees to start integration
        @type   pyfTwoThetaStart: python float
        @param  pyfTwoThetaStop: angle in degrees to stop the integration
        @type   pyfTwoThetaStop: python float
        @return: integrated value of diffracted intensity
        @rtype:    python float
        """
        if not self.pydIntergratedCache.has_key((pyfTwoThetaStart , pyfTwoThetaStop)):
            pyintStart = max(0, int(round((pyfTwoThetaStart - self.pyfTwoThetaMin) / self.pyfTwoThetaStep)))
            pyintStop = min(self.pyintNbPoints, int(round((pyfTwoThetaStop - self.pyfTwoThetaMin) / self.pyfTwoThetaStep)))
            self.pydIntergratedCache[ (pyfTwoThetaStart , pyfTwoThetaStop) ] = self.npaIntensities [ pyintStart : pyintStop ].sum() / self.pyfTwoThetaStep
        return self.pydIntergratedCache[ (pyfTwoThetaStart , pyfTwoThetaStop) ]

    def getSinogramSize(self):
        """Retuns the size of the sinogramconsidering the data in the CIF file 
        @rtype: 2-tuple of integer
        @return: size of the sinogram image
        """
        if  self.pyintSinogramSizeX == None:
            if  self.cif["_tomo_scan_type"].lower() in ["flat", "spiral"]:
                self.pyintSinogramSizeX = 1 + int(round(abs((float(self.cif[ "_tomo_spec_displ_x_max" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"]))))
                self.pyintSinogramSizeY = 1 + int(round(abs(float(self.cif[ "_tomo_scan_ampl" ]) / float(self.cif[ "_tomo_spec_displ_rotation_inc" ]))))
            if self.cif["_tomo_scan_type"].lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
                self.pyintSinogramSizeX = 1 + int(round(abs((float(self.cif[ "_tomo_spec_displ_x_max" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"]))))
                self.pyintSinogramSizeY = 1 + int(round(abs((float(self.cif[ "_tomo_spec_displ_z_max" ]) - float (self.cif [ "_tomo_spec_displ_z_min" ])) / float(self.cif["_tomo_spec_displ_z_inc"]))))
                EDVerbose.DEBUG("Size of the sinogram generated %ix%i" % (self.pyintSinogramSizeX, self.pyintSinogramSizeY))
        return (self.pyintSinogramSizeX, self.pyintSinogramSizeY)



    def getSinogramPosition(self):
        """calculates the size of the sinogram considering the piece of informations available in the CIF file
        @rtype: 2-tuple of pyhon integers
        @return: the size in X,Y in pixels of the image of the sinogram
        """
        if   self.pyintXpos is None:
            if  self.cif["_tomo_scan_type"].lower() in ["flat", "spiral"]:
                self.pyintXpos = int(round(abs((float(self.cif[ "_tomo_spec_displ_x" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"]))))
                self.pyintYpos = int(round(abs(float(self.cif[ "_tomo_spec_displ_rotation" ]) / float(self.cif[ "_tomo_spec_displ_rotation_inc" ]))))
            if self.cif["_tomo_scan_type"].lower() == "mapping": #I agree mappings are not sinograms but the really looks like, no ? 
                self.pyintXpos = int(round(abs((float(self.cif[ "_tomo_spec_displ_x" ]) - float (self.cif [ "_tomo_spec_displ_x_min" ])) / float(self.cif["_tomo_spec_displ_x_inc"]))))
                self.pyintYpos = int(round(abs((float(self.cif[ "_tomo_spec_displ_z" ]) - float (self.cif [ "_tomo_spec_displ_z_min" ])) / float(self.cif["_tomo_spec_displ_z_inc"]))))
        return self.pyintXpos, self.pyintYpos


class EDPluginDCTWriteSinogramv1_0(EDPluginExec):
    """
    This plugin is a part of the DiffractionCT project.

    It takes as input the path to a CIF file containing integrated
    intensities as well as the necessary header information. 
    
    The CIF file could for example be the result of a 2D azimuthal 
    integration performed by the plugin 
    EDPluginControlDCTPowderIntegration-v1.0.
    
    It also takes as input the path to the directory where the 
    sinogram images are (or will be if they don't exist) stored,
    as well as a sinogram file name prefix. 

    The EDPluginDCTWriteSinogramv1_0 plugin produces one or several 
    sinogram images depending on the header information in the CIF file. 
    The XSDataResultWriteSinogram object contains a list of paths to 
    these images.
    """


    def __init__(self):
        """
        Sets the data input class to XSDataInputWriteSinogram
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputWriteSinogram)
#        self.getXSDataOutputClass( XSDataResultWriteSinogram )
        self.m_cifPowderData = None


    def checkParameters(self):
        """
        Checks the mandatory input parameter "integratedIntensities" which is
        the file path to the incoming CIF file.
        """
        EDVerbose.DEBUG("*** EDPluginDCTWriteSinogramv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getIntegratedIntensities(), "integratedIntensities")
        self.checkMandatoryParameters(self.getDataInput().getSinogramDirectory(), "sinogramDirectory")
        self.checkMandatoryParameters(self.getDataInput().getSinogramFileNamePrefix(), "sinogramFileNamePrefix")

    def preProcess(self, _edObject=None):
        """
        
        """
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("*** EDPluginDCTWriteSinogramv1_0.preProcess")
        pyStrPathToInputCIFFile = self.getDataInput().getIntegratedIntensities().getPath().getValue()
        EDVerbose.DEBUG("This is the file which will be analyzed: %s" % pyStrPathToInputCIFFile)
        self.pystrPathToSinogramsDir = self.getDataInput().getSinogramDirectory().getPath().getValue()
        if not PyOs.path.isdir(self.pystrPathToSinogramsDir):
            PyOs.makedirs(self.pystrPathToSinogramsDir)
        self.pystrSinogramPrefix = self.getDataInput().getSinogramFileNamePrefix().getValue()
        EDVerbose.DEBUG("Now generation of the SinoGrams, Path:  %s, Prefix= %s" % (self.pystrPathToSinogramsDir, self.pystrSinogramPrefix))
        if (not EDUtilsPath.existPath(pyStrPathToInputCIFFile)):
            pyStrErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", pyStrPathToInputFile)
            EDVerbose.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)
            raise RuntimeError, pyStrErrorMessage
        # File exists, try to read it with the CIF library
        try:
            self.m_cifPowderData = CIF()
            self.m_cifPowderData.loadCIF(pyStrPathToInputCIFFile)
            EDVerbose.DEBUG("Parsing of the CIF file %s successful" % pyStrPathToInputCIFFile)
        except Exception:
            pyStrErrorMessage = EDMessage.ERROR_UNEXPECTED_01 % ("EDPluginDCTWriteSinogramv1_0.preProcess: Error when trying to read CIF file : %s" % pyStrPathToInputCIFFile)
            EDVerbose.error(pyStrErrorMessage)
            self.addErrorMessage(pyStrErrorMessage)
            # Just raise the exception in order to not loose the error stack trace    
            raise
        if not self.m_cifPowderData.exists("_tomo_scan_type"):
                EDVerbose.DEBUG("How do you want to generate a Sinogram if you are lacking essential things like the scan type !!!!")
                raise
        self.pydMetaDataEDF = self.m_cifPowderData.copy() #This is a simple python dictionary
        if self.pydMetaDataEDF.has_key("loop_"):                         self.pydMetaDataEDF.pop("loop_")
        if self.pydMetaDataEDF.has_key("_synchrotron_photon-flux"):      self.pydMetaDataEDF.pop("_synchrotron_photon-flux")
        if self.pydMetaDataEDF.has_key("_synchrotron_ring-intensity"):   self.pydMetaDataEDF.pop("_synchrotron_ring-intensity")
        if self.pydMetaDataEDF.has_key("_tomo_spec_displ_rotation"):     self.pydMetaDataEDF.pop("_tomo_spec_displ_rotation")
        if self.pydMetaDataEDF.has_key("_tomo_spec_displ_x"):            self.pydMetaDataEDF.pop("_tomo_spec_displ_x")
        if self.pydMetaDataEDF.has_key("_tomo_spec_displ_z"):            self.pydMetaDataEDF.pop("_tomo_spec_displ_z")

        self.powderIntegrator = PowderIntegrator(self.m_cifPowderData)
        self.pyintXpos, self.pyintYpos = self.powderIntegrator.getSinogramPosition()
        (Xmax, Ymax) = self.powderIntegrator.getSinogramSize()
        self.pydProcessSinograms = {}
        for pystrSinogramSuffix in [ "PhotonFlux", "IntegratedRaw", "IntegratedCor"]:
                pystrSinogramFullPath = PyOs.path.join(self.pystrPathToSinogramsDir, self.pystrSinogramPrefix + "Sinogram" + pystrSinogramSuffix)
                self.pydProcessSinograms[pystrSinogramFullPath] = pystrSinogramSuffix

        if self.m_cifPowderData.exists("_pd_sum_2theta_range_min"):
                for basename in [ "Raw", "Cor" ]:
                    startregion = float(self.m_cifPowderData[ "_pd_sum_2theta_range_min" ])
                    stopregion = float(self.m_cifPowderData[ "_pd_sum_2theta_range_max" ])
                    pystrSinogramFilename = "%sSinogramROI%i-%i%s" % (self.pystrSinogramPrefix, int(round (startregion)), int(round (stopregion)), basename)
                    pystrSinogramFullPath = PyOs.path.join(self.pystrPathToSinogramsDir, pystrSinogramFilename)
                    self.pydProcessSinograms[pystrSinogramFullPath] = [ startregion, stopregion ]
        else:
                for oneloop in self.m_cifPowderData[ "loop_" ]:
                    if "_pd_sum_2theta_range_min" in oneloop[0]:
                        for i in oneloop[1] :
                            startregion = float(i[ "_pd_sum_2theta_range_min" ])
                            stopregion = float(i[ "_pd_sum_2theta_range_max" ])
                            for basename in [ "Raw", "Cor" ]:
                                pystrSinogramFilename = "%sSinogramROI%i-%i%s" % (self.pystrSinogramPrefix, int(round(startregion)), int(round(stopregion)) , basename)
                                pystrSinogramFullPath = PyOs.path.join(self.pystrPathToSinogramsDir, pystrSinogramFilename)
                                self.pydProcessSinograms[pystrSinogramFullPath] = [ startregion, stopregion ]

    def process(self, _edObject=None):
        """ 
        This method does the calculations and create / modifies the sinograms
        
        Pay attention: the xy coordinate are inverted when calling  here to have x first coordinate as horizontal, what is different from the math convention (line/column)  
        """
        EDPluginExec.process(self)


        EDVerbose.DEBUG("*** EDPluginDCTWriteSinogramv1_0.process")
        if (self.m_cifPowderData is not None):
            borg2DImageWriter = Borg2DImageWriter()
            EDVerbose.DEBUG("Now generation of the Sinograms, Path:  %s, pixel position= %i,%i" % (self.pystrPathToSinogramsDir, self.pyintXpos , self.pyintYpos))
            for pystrSinogramFullPath in self.pydProcessSinograms:
                EDVerbose.DEBUG("Writing Sinogram %s pixel (%i,%i)" % (pystrSinogramFullPath, self.pyintXpos , self.pyintYpos))
                self.xMax, self.yMax = self.powderIntegrator.getSinogramSize()
                #Change here if there is a new version of BorgDImageWriter             
                if not PyOs.path.isfile(pystrSinogramFullPath + "Size%ix%i.edf" % (self.yMax, self.xMax)):
                    EDVerbose.DEBUG("Creating Sinogram %s size (%i,%i)" % (pystrSinogramFullPath, self.xMax , self.yMax))
                    borg2DImageWriter.newFile(filename=pystrSinogramFullPath, size=(self.yMax, self.xMax))
                if isinstance(self.pydProcessSinograms[ pystrSinogramFullPath ], str) or isinstance(self.pydProcessSinograms[ pystrSinogramFullPath ], unicode) :
#                    EDVerbose.DEBUG( "Keyword= %s "%self.pydProcessSinograms[ pystrSinogramFullPath ])
                    if self.pydProcessSinograms[ pystrSinogramFullPath ] == "PhotonFlux":
                        EDVerbose.DEBUG("PhotonFlux= %s " % self.powderIntegrator.pyfPhotonFlux)
                        borg2DImageWriter.set(filename=pystrSinogramFullPath, position=(self.pyintYpos, self.pyintXpos), value=self.powderIntegrator.pyfPhotonFlux)
                    elif self.pydProcessSinograms[ pystrSinogramFullPath ] == "IntegratedRaw":
                        EDVerbose.DEBUG("IntegratedRaw= %s " % self.powderIntegrator.integrate())
                        borg2DImageWriter.set(filename=pystrSinogramFullPath, position=(self.pyintYpos, self.pyintXpos), value=self.powderIntegrator.integrate())
                    elif self.pydProcessSinograms[ pystrSinogramFullPath ] == "IntegratedCor":
                        EDVerbose.DEBUG("IntegratedCor= %s " % (self.powderIntegrator.integrate() / self.powderIntegrator.pyfPhotonFlux))
                        borg2DImageWriter.set(filename=pystrSinogramFullPath, position=(self.pyintYpos , self.pyintXpos), value=(self.powderIntegrator.integrate() / self.powderIntegrator.pyfPhotonFlux))
                elif isinstance(self.pydProcessSinograms[ pystrSinogramFullPath ], list):
                    if   pystrSinogramFullPath[-3:] == "Raw" :
                        EDVerbose.DEBUG("Raw %s - %s= %s " % (self.pydProcessSinograms[ pystrSinogramFullPath ][0], self.pydProcessSinograms[ pystrSinogramFullPath ][1], self.powderIntegrator.integrate(*tuple(self.pydProcessSinograms[ pystrSinogramFullPath ]))))
                        borg2DImageWriter.set(filename=pystrSinogramFullPath, position=(self.pyintYpos, self.pyintXpos), value=(self.powderIntegrator.integrate(*tuple(self.pydProcessSinograms[ pystrSinogramFullPath ]))))
                    elif pystrSinogramFullPath[-3:] == "Cor"  :
                        EDVerbose.DEBUG("Cor %s - %s= %s " % (self.pydProcessSinograms[ pystrSinogramFullPath ][0], self.pydProcessSinograms[ pystrSinogramFullPath ][1], self.powderIntegrator.integrate(*tuple(self.pydProcessSinograms[ pystrSinogramFullPath ])) / self.powderIntegrator.pyfPhotonFlux))
                        borg2DImageWriter.set(filename=pystrSinogramFullPath, position=(self.pyintYpos , self.pyintXpos), value=(self.powderIntegrator.integrate(*tuple(self.pydProcessSinograms[ pystrSinogramFullPath ])) / self.powderIntegrator.pyfPhotonFlux))

    def postProcess(self, _edObject=None):
        """
        """
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("*** EDPluginDCTWriteSinogramv1_0.postProcess")
        xsDataResultWriteSinogram = XSDataResultWriteSinogram()

        for pystrPathToOneSinogram in self.pydProcessSinograms:
            oneSinogram = XSDataFile()
            oneSinogram.setPath(XSDataString(pystrPathToOneSinogram + "Size%ix%i.edf" % (self.yMax, self.xMax)))
            xsDataResultWriteSinogram.addSinogramFile(oneSinogram)
            EDVerbose.DEBUG("Adding sinogram: %s" % pystrPathToOneSinogram)
        self.setDataOutput(xsDataResultWriteSinogram)
