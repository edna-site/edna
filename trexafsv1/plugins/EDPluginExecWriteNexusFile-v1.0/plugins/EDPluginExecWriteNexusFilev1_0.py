# coding: utf8
#
#    Project: Time-Resolved EXAFS
#             http://www.edna-site.org
#
#    Copyright (C)      2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, h5py

from EDPluginExec import EDPluginExec
from EDUtilsArray import EDUtilsArray

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataWriteNexusFilev1_0 import XSDataInputWriteNexusFile
from XSDataWriteNexusFilev1_0 import XSDataResultWriteNexusFile

class EDPluginExecWriteNexusFilev1_0( EDPluginExec ):
    """
    This plugin reads an ascii file of DEXAFS data produced by the ID24 beamline at the ESRF.
    The energy calibration coefficients must be given as input. 
    """

    def __init__( self ):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputWriteNexusFile)   

    
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecWriteNexusFilev1_0.process")
        xsDataInput = self.getDataInput()
#        print xsDataInput.marshal()
        fileName = str(xsDataInput.outputFileName.value)
        if xsDataInput.outputFileDirectory is None:
            fileDir = self.getWorkingDirectory()
        else:
            fileDir = str(xsDataInput.outputFileDirectory.value)
        timestamp = "2010-10-18T17:17:04-0500"
        instrument = str(xsDataInput.instrument.value)
        # Create nexus file
        nexusFile = self.makeFile(os.path.join(fileDir, fileName), file_name=fileName,
            file_time=timestamp,
            instrument=instrument,
            creator="EDPluginExecWriteNexusFilev1_0",
            NeXus_version="4.3.0",
            HDF5_Version=h5py.version.hdf5_version,
            h5py_version=h5py.version.version) 
        # Write main data
        nxentry = self.makeGroup(nexusFile, "Result", "NXentryResult")
        for nexusGroup in xsDataInput.nexusGroup:
            groupTitle = str(nexusGroup.title.value)
            long_name = str(nexusGroup.long_name.value)
            nxdata = self.makeGroup(nxentry, groupTitle, "NXdata", long_name=long_name)
            # First add the axes - if any...
            listAxisNames = []
            for xsDataNexusAxis in nexusGroup.axis:
                numpyAxisArray = EDUtilsArray.xsDataToArray(xsDataNexusAxis.axisData)
                self.makeDataset(nxdata, 
                                 str(xsDataNexusAxis.title.value), 
                                 numpyAxisArray, 
                                 axis=xsDataNexusAxis.axis.value,
                                 primary=xsDataNexusAxis.primary.value, 
                                 units=str(xsDataNexusAxis.units.value), 
                                 long_name=str(xsDataNexusAxis.long_name.value))
                listAxisNames.append(str(xsDataNexusAxis.title.value))
            numpyDataArray = EDUtilsArray.xsDataToArray(nexusGroup.data)
            strAxisNames = ""
            bFirst = True
            for strAxisName in listAxisNames:
                if bFirst:
                    strAxisNames += strAxisName
                    bFirst = False
                else:
                    strAxisNames += ":"+strAxisName
            self.makeDataset(nxdata, groupTitle, numpyDataArray.transpose(), 
                signal='1', # Y axis of default plot
                axes=strAxisNames, # name of X and Y axes
                long_name=long_name)
            pass
        xsDataResult = XSDataResultWriteNexusFile()
        xsDataResult.outputFilePath = XSDataFile(XSDataString(os.path.join(fileDir, fileName)))
        self.setDataOutput(xsDataResult)
    
    def makeFile(self, filename, **attr):
        f = h5py.File(filename, "w")
        self.add_attributes(f, attr)
        return f
    
    def add_attributes(self, parent, attr):
        """
        add attributes to an h5py data item
        
        :param obj parent: h5py parent object
        :param dict attr: dictionary of attributes
        """
        if attr and type(attr) == type({}):
            # attr is a dictionary of attributes
            for k, v in attr.items():
                parent.attrs[k] = v
    
    def makeDataset(self, parent, name, data = None, **attr):
        if data == None:
            obj = parent.create_dataset(name)
        else:
            obj = parent.create_dataset(name, data=data)
        self.add_attributes(obj, attr)
        return obj 
    
    def makeGroup(self, parent, name, nxclass, **attr):
        group = parent.create_group(name)
        group.attrs["NX_class"] = nxclass
        self.add_attributes(group, attr)
        return group
