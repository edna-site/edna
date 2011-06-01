#
#    Project: DIMPLE
#             http://www.edna-site.org
#
#    Copyright (C) 2010 Diamond Light Source and CCP4
#
#    Principal authors: Graeme Winter (graeme.winter@diamond.ac.uk)
#                       Ronan Keegan (ronan.keegan@stfc.ac.uk)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the Lesser GNU General Public License as published by
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

__author__= ['Graeme Winter', 'Ronan Keegan']
__license__ = 'LGPLv3+'
__copyright__ = '2010 Diamond Light Source, CCP4'

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4DataInputCheckValidHKL
from XSDataCCP4DIMPLE import CCP4DataResultCheckValidHKL

from XSDataCCP4DIMPLE import CCP4ReturnStatus
from XSDataCCP4DIMPLE import XSDataString
from XSDataCCP4DIMPLE import XSDataInteger


class EDPluginExecDIMPLECheckValidHKLv10(EDPluginExec ):
    """
    An EDNA plugin to check for the validity of mtz files
    """
    

    def __init__(self ):
        """
        """
        EDPluginExec.__init__(self )
        self.setXSDataInputClass(CCP4DataInputCheckValidHKL)

        self._hklin = None
        self._returnStatus = CCP4ReturnStatus()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidHKLv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),'No input MTZ file specified')
                                      
    
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidHKLv10.preProcess")
        

        self._hklin = self.getDataInput().getHKLIN().getPath().getValue()        
        
        
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidHKLv10.process")

        self.test(self._hklin)
        

    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidHKLv10.postProcess")
        # Create some output data
        xsDataResult = CCP4DataResultCheckValidHKL(returnStatus=self._returnStatus)        
        self.setDataOutput(xsDataResult)


    def test(self,filename):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLECheckValidHKLv10.test")
        f=open(filename,'r')
        mtzreadlines=f.readlines()
                
        if mtzreadlines[0][0:4] == "MTZ ":
            a=int(1) 
            b=str("The file %s is an mtz type of file") % filename
            self._returnStatus.setCode(XSDataInteger(a))
            self._returnStatus.setMessage(XSDataString(b))                                  
        else:
            a=int(0) 
            b=str("The file %s is NOT an mtz type of file") % filename
            self._returnStatus.setCode(XSDataInteger(a))
            self._returnStatus.setMessage(XSDataString(b))            

        f.close()
    
