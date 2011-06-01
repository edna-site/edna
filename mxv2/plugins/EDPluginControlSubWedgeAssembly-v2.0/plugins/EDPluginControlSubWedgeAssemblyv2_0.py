#
#    Project: EDNA MXv2
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:      Olof Svensson (svensson@esrf.fr)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Gleb Bourenkov (Gleb.Bourenkov@embl-hamburg.de)
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

import os

from EDVerbose       import EDVerbose
from EDPluginControl import EDPluginControl
from EDUtilsImage    import EDUtilsImage


from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataInputSubWedgeAssemble

from XSDataMXv2 import XSDataCollection as XSDataCollection_v2
from XSDataMXv2 import XSSubWedge as XSSubWedge_v2
from XSDataMXv2 import XSDiffractionImages as XSDiffractionImages_v2
from XSDataMXv2 import XSRotationExposure as XSRotationExposure_v2
from XSDataMXv2 import XSBeamSetting as XSBeamSetting_v2
import XSDataMXv2



class EDPluginControlSubWedgeAssemblyv2_0(EDPluginControl):
    """
    This plugin takes as input a list of paths to images. 
    It calls the old assembler. The result of that will be then converted 
    to new DM and also extended by info fetched from DC (data collection)
    descriptior file created by the BCM next to the data images.
    
    For now, the OUTPUT is a LIST of 
    + the old result
    + the new DC descriptor

    Old assembler:
    It executes the 
    EDPluginReadImageHeaderv10 plugin for each image path in order to read 
    the image header data and produce a XSDataSubWedge instance for each image.
    It then executes the EDPluginSubWedgeMergev10 plugin for, if possible, 
    merging these subwedges. 
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputSubWedgeAssemble)

        self.strPluginControlSubwedgeAssembleOLDName = "EDPluginControlSubWedgeAssemblev10"
        self.strPluginConvertDataModel_1_1_to_2_0_Name = "EDPluginConvertDataModel_1_1_to_2_0_v2_0"
        self.strPluginReadDataCollectionDescriptorName = "EDPluginDataCollectionDescriptorv2_0"
        self.xsDatacollection_v2 = None
        # setXSDataOutputClass : not implemented now
        #self.setXSDataOutputClass( XSDataInputSubWedgeAssemble, "mxv1Assemble" )
        #EDFactoryPluginStatic.loadModule( "XSDataMXv2" )
        #self.setXSDataOutputClass( XSDataMXv2.XSDataCollection, "mxv2DataCollection" )

    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getFile(), "file")


    def preProcess(self, _edObject=None):
        """
        Gets the Configuration Parameters, if found, overrides default parameters
        """
        EDPluginControl.preProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.preProcess")

        self.edPluginControlSubwedgeAssembleOLD = self.loadPlugin(self.strPluginControlSubwedgeAssembleOLDName)


    def process(self, _edObject=None):
        EDPluginControl.process(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.process")
        if (self.edPluginControlSubwedgeAssembleOLD is not None):
            self.connectProcess(self.callOldSubWedgeAssembler)
            self.edPluginControlSubwedgeAssembleOLD.connectSUCCESS (self.doSuccessActionOldSubWedgeAssemble)
            self.edPluginControlSubwedgeAssembleOLD.connectFAILURE (self.doFailureActionOldSubWedgeAssemble)


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.postProcess")
        if (self.xsDataResultSubWedgeAssemble is not None):
            #copy/duplicate: YY.parseString(XX.marshal())
            #xsDataResultSubWedgeAssembly = XSDataResultSubWedgeAssemble()            
            #xsDataResultSubWedgeAssembly = self.xsDataResultSubWedgeAssemble

#            xsDataResultSubWedgeAssembly = EDList()
#            xsDataResultSubWedgeAssembly.add(self.xsDataResultSubWedgeAssemble)
#            xsDataResultSubWedgeAssembly.add(self.xsDatacollection_v2)
#            self.setDataOutput( xsDataResultSubWedgeAssembly )
            self.setDataOutput(self.xsDataResultSubWedgeAssemble , "mxv1Assemble")
            if self.xsDatacollection_v2 != None:
                self.setDataOutput(self.xsDatacollection_v2 , "mxv2DataCollection")

    def callOldSubWedgeAssembler(self, _edPlugin):
        """
        This method calls the old assembler that will be then converted to new DM and also extended 
        by info fetched from DC data collection descriptior file created by the BCM next to the data images.
        """
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.callOldSubWedgeAssembler")
        xsDataInputSubWedgeAssemble = _edPlugin.getDataInput()
        self.edPluginControlSubwedgeAssembleOLD.setDataInput(xsDataInputSubWedgeAssemble)
        self.edPluginControlSubwedgeAssembleOLD.executeSynchronous()

    def generateDataCollectionDescriptorForSubWedge(self, calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames):
        ##CONTAINER
        self.xsDC_v2 = XSDataCollection_v2()

        ##GonioCalib
        calib = XSDataMXv2.XSCalibration()
        cdate = XSDataMXv2.XSDataDate()
        cdate.setValue(XSDataMXv2.XSDataString(calibDate))
        calib.setDate(cdate)
        #OmegaCalib
        omegacal = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(omegaR[0])
        zdir.setV2(omegaR[1])
        zdir.setV3(omegaR[2])
        omegacal.setZerodirection(zdir)
        omegacal.setXSCalibration(calib)
        #KappaCalib
        kappacal = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(kappaR[0])
        zdir.setV2(kappaR[1])
        zdir.setV3(kappaR[2])
        kappacal.setZerodirection(zdir)
        kappacal.setXSCalibration(calib)
        #PhiCalib
        phical = XSDataMXv2.XSCalibratedDisplacementAxis()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(phiR[0])
        zdir.setV2(phiR[1])
        zdir.setV3(phiR[2])
        phical.setZerodirection(zdir)
        phical.setXSCalibration(calib)

        ##goni
        actgonio = XSDataMXv2.XSRotationalGoniostat()
        #omega
        omega = XSDataMXv2.XSGoniostatBaseAxis()
        omega.setName(XSDataMXv2.XSDataString('Omega'))
        omega.setIsscannable(XSDataMXv2.XSDataBoolean(1))
        omega.addXSCalibratedDisplacementAxis(omegacal)
        actgonio.setXSGoniostatBaseAxis(omega)
        #kappa
        kappa = XSDataMXv2.XSGoniostatRotatableAxis()
        kappa.setName(XSDataMXv2.XSDataString('Kappa'))
        kappa.setIsscannable(XSDataMXv2.XSDataBoolean(0))
        kappa.addXSCalibratedDisplacementAxis(kappacal)
        actgonio.addXSGoniostatRotatableAxis(kappa)
        #phi
        phi = XSDataMXv2.XSGoniostatRotatableAxis()
        phi.setName(XSDataMXv2.XSDataString('Phi'))
        phi.setIsscannable(XSDataMXv2.XSDataBoolean(0))
        phi.addXSCalibratedDisplacementAxis(phical)
        actgonio.addXSGoniostatRotatableAxis(phi)

        ##beam
        beam = XSDataMXv2.XSBeam()
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(polarisationP[0])
        zdir.setV2(polarisationP[1])
        zdir.setV3(polarisationP[2])
        beam.setPolarisatation(zdir)
        zdir = XSDataMXv2.XSDataUnitVector()
        zdir.setV1(beamD[0])
        zdir.setV2(beamD[1])
        zdir.setV3(beamD[2])
        beam.setDirection(zdir)

        ##detector
        detector = XSDataMXv2.XSDetector()
        detector.setName(XSDataMXv2.XSDataString('detector'))
        ###detector.set

        ##SUBWEDGE
        sw = XSSubWedge_v2()
        # template
        sw.setImagefilenametemplate(XSDataMXv2.XSDataString(EDUtilsImage.getTemplate(imgFnames[0], "#")))
        # images
        for imgFname in imgFnames:
            img = XSDiffractionImages_v2()
            img.setFilename(XSDataMXv2.XSDataString(imgFname))
            sw.addXSDiffractionImages(img)
        #RotationExposure
        rotexp = XSRotationExposure_v2()
        rotexp.setExposuretime(XSDataMXv2.XSDataTime(exposuretime))
        rotexp.setImagewidth(XSDataMXv2.XSDataAngle(imagewidth))
        rotexp.setNumberimages(XSDataMXv2.XSDataInteger(numberimages))
        rotexp.setXSGoniostatAxis(omega)
        sw.setXSRotationExposure(rotexp)
        #Beamsetting
        beams = XSBeamSetting_v2()
        w = XSDataMXv2.XSDataWavelength()
        w.setValue(wavelength)
        beams.setWavelength(w)
        beams.setXSBeam(beam)
        sw.setXSBeamSetting(beams)
        #RotationalGonioSetting
        rotgset = XSDataMXv2.XSRotationalGoniostatSetting()
        rotgset.setXSRotationalGoniostat(actgonio)
        oang = XSDataMXv2.XSDataAngle()
        oang.setValue(OmegaV)
        rotgset.setBaseaxissetting(oang)
        kang = XSDataMXv2.XSDataAngle()
        kang.setValue(KappaV)
        rotgset.addAxissetting(kang)
        pang = XSDataMXv2.XSDataAngle()
        pang.setValue(PhiV)
        rotgset.addAxissetting(pang)
        sw.setXSRotationalGoniostatSetting(rotgset)
        #DetectorSetting TODOTODO
        detset = XSDataMXv2.XSDetectorSetting()
        #axissetting=(XSDataMXv2.XSDataAngle().setValue(KappaV),XSDataMXv2.XSDataAngle().setValue(PhiV))
        #detset.setAxissetting(axissetting)



        self.xsDC_v2.addXSSubWedge(sw)



        imgFname = self.xsDataResultSubWedgeAssemble.getSubWedge()[0].getImage()[0].getPath().getValue()
        self.xsDC_v2.outputFile(os.path.dirname(imgFname) + '/edna_' + EDUtilsImage.getTemplate(imgFname, "#") + '_auto')

    def doSuccessActionOldSubWedgeAssemble(self, _edPlugin=None):
        """
        - gets the result from the old assembler
        - converts it to DMv2
        - reads DC descriptor file prepared by the BCM
        - merges the info together
        """
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.doSuccessActionSubWedgeMerge")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlSubWedgeAssemblyv2_0.doSuccessActionOldSubWedgeAssemble")
        if not _edPlugin.isFailure():
            # getting the result from the old assembler
            self.xsDataResultSubWedgeAssemble = _edPlugin.getDataOutput()

            # converts it to DMv2



            # reads DC descriptor file(s) prepared by the BCM
            swList = self.xsDataResultSubWedgeAssemble.getSubWedge()
            try:
                for sw in swList:
                    # get filename
                    imgFname = sw.getImage()[0].getPath().getValue()
                    strMOSFLMTemplate = os.path.dirname(imgFname) + '/edna_' + EDUtilsImage.getTemplate(imgFname, "#")
                    # print strMOSFLMTemplate

                    # read file in
                    #self.xsDatacollection_v2 = XSDataCollection_v2()
                    self.xsDatacollection_v2 = XSDataMXv2.XSDataCollection.parseFile(strMOSFLMTemplate)
            except IOError:
                # TEMP: generates the file to be read in
                ##PARAMS
                calibDate = '2009-12-10'
                omegaR = (0, 0, 1)
                kappaR = (0, 0.707106781187, 0.707106781187)
                phiR = (0, 0, 1)
                beamD = (1, 0, 0)
                polarisationP = (0, 1, 0)
                exposuretime = 1.0
                imagewidth = 1.0
                numberimages = 1
                wavelength = 1.0
                OmegaV = 0.0
                KappaV = 90.0
                PhiV = 40.0
                imgFnames = []
                imgFnames.append(self.xsDataResultSubWedgeAssemble.getSubWedge()[0].getImage()[0].getPath().getValue())

                self.generateDataCollectionDescriptorForSubWedge(calibDate, omegaR, kappaR, phiR, beamD, polarisationP, exposuretime, imagewidth, numberimages, wavelength, OmegaV, KappaV, PhiV, imgFnames)



            # merges the info together

    def doFailureActionOldSubWedgeAssemble(self, _edPlugin=None):
        EDVerbose.DEBUG("EDPluginControlSubWedgeAssemblyv2_0.doFailureActionSubWedgeMerge")
        EDVerbose.screen("Execution of " + self.strPluginControlSubwedgeAssembleOLDName + "  failed.")
        EDVerbose.screen("Please inspect the log file for further information.")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlSubWedgeAssemblyv2_0.doFailureActionOldSubWedgeAssemble")

