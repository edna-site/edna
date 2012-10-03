# coding: utf8
#
#    Project: Python Fast Azimuthal Integration
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#
#    Principal author:       Jérôme Kieffer <jerome.kieffer@esrf.fr>
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
from __future__ import with_statement
__author__ = "Jérôme Kieffer <jerome.kieffer@esrf.fr>"
__license__ = "GPLv3+"
__copyright__ = "2012 European Synchrotron Radiation Facility"

import os
import numpy as np
from EDUtilsArray       import EDUtilsArray
from EDUtilsUnit        import EDUtilsUnit
from EDPluginExec       import EDPluginExec
from EDVerbose          import EDVerbose
from EDThreading        import Semaphore
from XSDataPyFAIv1_0    import XSDataInputPyFAI, XSDataResultPyFAI, XSDataGeometryFit2D, XSDataGeometryPyFAI
from XSDataCommon       import XSDataImageExt, XSDataString


try:
    import pyFAI
except ImportError:
    EDVerbose.ERROR("Failed to import PyFAI: download and install it from \
        https://forge.epn-campus.eu/projects/azimuthal/files")
try:
    import fabio
except ImportError:
    EDVerbose.ERROR("Failed to import Fabio: download and install it from sourceforge")


class EDPluginExecPyFAIv1_0(EDPluginExec):
    """
    This is the basic plugin of PyFAI for azimuthal integration
    """

    _dictGeo = {} #key:tuple(ai.param), value= ai
    _sem = Semaphore()
    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputPyFAI)
        self.shared = None
        self.strOutputFile = None
        self.ai = None #this is the azimuthal integrator to use
        self.data = None
        self.mask = None
        self.nbPt = None
        self.dummy = None
        self.delta_dummy = None
        self.npaOut = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecPyFAIv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
#        self.checkMandatoryParameters(self.dataInput.geometry, "No Geometry given")
#        self.checkMandatoryParameters(self.dataInput.detector, "No Detector given")
        self.checkMandatoryParameters(self.dataInput.input, "No input image given")
        self.checkMandatoryParameters(self.dataInput.nbPt, "No Number of points given for integration")

    @staticmethod
    def getDetector(xsDetector):
        detector = None
        if xsDetector.name and (xsDetector.name.value in dir(pyFAI.detectors)):
            detector = getattr(pyFAI.detectors, xsDetector.name.value)()
        else:
            pixel2 = EDUtilsUnit.getSIValue(xsDetector.pixelSizeX)
            pixel1 = EDUtilsUnit.getSIValue(xsDetector.pixelSizeY)
            if xsDetector.splineFile and os.path.isFile(xsDetector.splineFile.path.value):
                dictGeo = {"pixel1":pixel1, "pixel2":pixel2, "splineFile":xsDetector.splineFile.path.value}
            else:
                dictGeo = {"pixel1":pixel1, "pixel2":pixel2, "splineFile":None}
            detector = pyFAI.detectors.Detector()
            detector.setPyFAI(**dictGeo)
        return detector

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.preProcess")
        sdi = self.dataInput
        ai = pyFAI.AzimuthalIntegrator()
        if sdi.geometryFit2D is not None:
            xsGeometry = sdi.geometryFit2D
            detector = self.getDetector(xsGeometry.detector)
            d = {"direct": EDUtilsUnit.getSIValue(xsGeometry.distance) * 1000, #fit2D takes the distance in mm
               "centerX": xsGeometry.beamCentreInPixelsX.value ,
               "centerY":xsGeometry.beamCentreInPixelsY.value  ,
               "tilt": xsGeometry.angleOfTilt.value,
               "tiltPlanRotation": xsGeometry.tiltRotation.value}
            d.update(detector.getFit2D())
            ai.setFit2D(**d)
        elif sdi.geometryPyFAI is not None:
            xsGeometry = sdi.geometryPyFAI
            detector = self.getDetector(xsGeometry.detector)
            d = {"dist": EDUtilsUnit.getSIValue(xsGeometry.sampleDetectorDistance),
               "poni1": EDUtilsUnit.getSIValue(xsGeometry.pointOfNormalIncidence1),
               "poni2": EDUtilsUnit.getSIValue(xsGeometry.pointOfNormalIncidence2),
               "rot1": EDUtilsUnit.getSIValue(xsGeometry.rotation1),
               "rot2": EDUtilsUnit.getSIValue(xsGeometry.rotation2),
               "rot3": EDUtilsUnit.getSIValue(xsGeometry.rotation3)}
            d.update(detector.getPyFAI())
            ai.setPyFAI(**d)
        else:
            strError = "Geometry definition in %s, not recognized as a valid geometry%s %s" % (sdi, os.linesep, sdi.marshal())
            self.ERROR(strError)
            raise RuntimeError(strError)

        ########################################################################
        # Choose the azimuthal integrator
        ########################################################################

        with self.__class__._sem:
            if tuple(ai.param) in self.__class__._dictGeo:
                self.ai = self.__class__._dictGeo[tuple(ai.param)]
            else:
                self.__class__._dictGeo[tuple(ai.param)] = ai
                self.ai = ai

        self.data = EDUtilsArray.getArray(self.dataInput.input).astype(float)
        if sdi.dark is not None:
            self.data -= EDUtilsArray.getArray(sdi.dark)
        if sdi.flat is not None:
            self.data /= EDUtilsArray.getArray(sdi.flat)
        if sdi.mask is not None:
            self.mask = EDUtilsArray.getArray(sdi.mask)
        if sdi.wavelength is not None:
            self.ai.wavelength = EDUtilsUnit.getSIValue(sdi.wavelength)
        if sdi.output is not None:
            self.strOutputFile = sdi.output.path.value
        if sdi.dummy is not None:
            self.dummy = sdi.dummy.value
        if sdi.deltaDummy is not None:
            self.delta_dummy = sdi.deltaDummy.value
        if sdi.nbPt:
            self.nbPt = sdi.nbPt.value

    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.process")
        data = EDUtilsArray.getArray(self.dataInput.input)
        if self.dataInput.saxsWaxs and self.dataInput.saxsWaxs.value.lower().startswith("s"):
            out = self.ai.saxs(self.data,
                               nbPt=self.nbPt,
                               filename=self.strOutputFile,
                               mask=self.mask,
                               dummy=self.dummy,
                               delta_dummy=self.delta_dummy)
        else:
            out = self.ai.xrpd(self.data,
                               nbPt=self.nbPt,
                               filename=self.strOutputFile,
                               mask=self.mask,
                               dummy=self.dummy,
                               delta_dummy=self.delta_dummy)
        self.npaOut = np.hstack((i.reshape(-1, 1) for i in out if i is not None))


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecPyFAIv1_0.postProcess")
        # Create some output data
        if self.strOutputFile:
            output = XSDataImageExt(path=XSDataString(self.strOutputFile))
        elif self.shared:
            output = XSDataImageExt(shared=XSDataString(self.shared))
        else:
            output = XSDataImageExt(array=EDUtilsArray.arrayToXSData(self.npaOut))
        xsDataResult = XSDataResultPyFAI(output=output)

        self.setDataOutput(xsDataResult)


