#
#    Project: Photo v1 Demo
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

import os, pyexiv2

from EDVerbose      import EDVerbose
from EDPluginExec   import EDPluginExec
from EDMessage      import EDMessage
from XSDataPhotov1  import XSDataInputCopyExifv1
from XSDataPhotov1  import XSDataResultCopyExifv1

class EDPluginCopyExifv1_0(EDPluginExec):
    """
    Copy the Exif metadata from input file to output file
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputCopyExifv1)
        self.strInfile = None
        self.strOutfile = None
        self.exifInfile = None
        self.exifOutfile = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginCopyExifv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImagePath(), "No Input Image Provided")
        self.checkMandatoryParameters(self.getDataInput().getOutputImagePath(), "No Output Image Provided")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginCopyExifv1_0.preProcess")
        self.strInfile = self.getDataInput().getInputImagePath().getPath().getValue()
        self.strOutfile = self.getDataInput().getOutputImagePath().getPath().getValue()
        for oneFile in [self.strInfile, self.strOutfile]:
            if not os.path.isfile(oneFile):
                strErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", oneFile)
                EDVerbose.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                raise RuntimeError, strErrorMessage


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginCopyExifv1_0.process")

        self.exifInfile = pyexiv2.Image(self.strInfile)
        self.exifOutfile = pyexiv2.Image(self.strOutfile)
        self.exifInfile.readMetadata()
        self.exifOutfile.readMetadata()
        for metadata in [ 'Exif.Image.Make', 'Exif.Image.Model', 'Exif.Photo.DateTimeOriginal', 'Exif.Photo.ExposureTime', 'Exif.Photo.FNumber', 'Exif.Photo.ExposureBiasValue', 'Exif.Photo.Flash', 'Exif.Photo.FocalLength', 'Exif.Photo.ISOSpeedRatings']:
        #for metadata in self.exifInfile.exifKeys():
            try:
                self.exifOutfile[metadata] = self.exifInfile[metadata]
            except ValueError:
                EDVerbose.WARNING("ValueError in copying metadata %s in file %s, value: %s" % (metadata, self.strInfile, self.exifInfile[metadata]))

        #dcraw sets automatically the good orientation
        self.exifOutfile['Exif.Image.Orientation'] = 1
        # save the name of the raw image
        self.exifOutfile["Exif.Photo.UserComment"] = self.strInfile

        self.exifOutfile.writeMetadata()


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginCopyExifv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultCopyExifv1()
        xsDataResult.setOutputImagePath(self.getDataInput().getOutputImagePath())
        self.setDataOutput(xsDataResult)
################################################################################
# By unallocating those ... we save memory
################################################################################
        self.exifInfile = None
        self.exifOutfile = None

