#
#	Project: EDNA ExecPlugins
#			 http://www.edna-site.org
#
#	File: "$Id$"
#
#	Copyright (C) <copyright>
#
#	Principal author:	   Jerome Kieffer (Kieffer@esrf.fr)
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
An execution plugin to read the header of an EDF File and return the headers / metadata  as a dictionary
"""

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os
from EDVerbose      import EDVerbose
from EDPluginExec   import EDPluginExec
from EDMessage      import EDMessage
from XSDataEDFv1_0  import XSDataString
from XSDataEDFv1_0  import XSDataDictionary
from XSDataEDFv1_0  import XSDataKeyValuePair
from XSDataEDFv1_0  import XSDataInputEDFReadHeader
from XSDataEDFv1_0  import XSDataResultEDFReadHeader
from EdfFile        import EdfFile

class EDPluginEDFReadHeaderv1_0(EDPluginExec):
	"""
	This plugin reads the header of an EDF (ESRF Data File) and returns
	the header values as a XSDataDitcionary.
	"""

	def __init__(self):
		"""
		"""
		EDPluginExec.__init__(self)
		self.setXSDataInputClass(XSDataInputEDFReadHeader)
		self.m_edDictionaryHeader = None


	def checkParameters(self):
		"""
		Checks the mandatory parameters.
		"""
		EDVerbose.DEBUG("*** EDPluginEDFReadHeaderv1_0.checkParameters")
		self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
		self.checkMandatoryParameters(self.getDataInput().getEdfFile(), "No edfFile given as input")


	def preProcess(self, _edObject=None):
		EDPluginExec.preProcess(self)
		EDVerbose.DEBUG("*** EDPluginEDFReadHeaderv1_0.preProcess")
		# Check that the input file is present
		edStringPathToInputFile = self.getDataInput().getEdfFile().getPath().getValue()
		if (not os.path.exists(edStringPathToInputFile)):
			edStringErrorMessage = EDMessage.ERROR_CANNOT_READ_FILE_02 % (self.getPluginName() + ".preProcess", edStringPathToInputFile)
			EDVerbose.error(edStringErrorMessage)
			self.addErrorMessage(edStringErrorMessage)
			raise RuntimeError, edStringErrorMessage



	def process(self, _edObject=None):
		EDPluginExec.process(self)
		EDVerbose.DEBUG("*** EDPluginEDFReadHeaderv1_0.process")
		# Read the header contents and put it into an dictionary
		edStringPathToInputFile = self.getDataInput().getEdfFile().getPath().getValue()
		pyFileDescriptor = open(edStringPathToInputFile, "r")
		edfFile = EdfFile(pyFileDescriptor)
		pyFileDescriptor.close()
		iNumberOfImages = edfFile.GetNumImages()
		if (iNumberOfImages == 0):
			edStringErrorMessage = EDMessage.ERROR_UNEXPECTED_01 % (self.getPluginName() + ".preProcess: No images in file " + edStringPathToInputFile)
			EDVerbose.error(edStringErrorMessage)
			self.addErrorMessage(edStringErrorMessage)
			raise RuntimeError, edStringErrorMessage
		#if ( iNumberOfImages > 1 ):
		#	pass
			#EDVerbose.warning( "Warning! More than one image in file " + edStringPathToInputFile ", reading header from first image" )
		self.m_edDictionaryHeader = edfFile.GetHeader(0)




	def postProcess(self, _edObject=None):
		EDPluginExec.postProcess(self)
		EDVerbose.DEBUG("*** EDPluginEDFReadHeaderv1_0.postProcess")
		# Create some output data
		xsDataResultEDFReadHeader = XSDataResultEDFReadHeader()
		if (self.m_edDictionaryHeader is not None):
			xsDataDictionary = XSDataDictionary()
			for key in self.m_edDictionaryHeader.keys():
				xsDataKeyValuePair = XSDataKeyValuePair()
				xsDataKeyValuePair.setKey(XSDataString(key))
				xsDataKeyValuePair.setValue(XSDataString(self.m_edDictionaryHeader[ key ]))
				xsDataDictionary.addKeyValuePair(xsDataKeyValuePair)
			xsDataResultEDFReadHeader.setDictionary(xsDataDictionary)
		self.setDataOutput(xsDataResultEDFReadHeader)

