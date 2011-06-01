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

from XSDataCCP4DIMPLE import CCP4DataInputCheckValidXYZ
from XSDataCCP4DIMPLE import CCP4DataResultCheckValidXYZ

from XSDataCCP4DIMPLE import CCP4ReturnStatus
from XSDataCCP4DIMPLE import XSDataString
from XSDataCCP4DIMPLE import XSDataInteger

class EDPluginExecDIMPLECheckValidXYZv10(EDPluginExec):
    """
    [To be replaced with a description of EDPluginExecTemplatev10]
    """
    

    def __init__(self ):
        """
        """
        EDPluginExec.__init__(self )
        self.setXSDataInputClass(CCP4DataInputCheckValidXYZ)

        self._xyzin = None
        self._returnStatus = CCP4ReturnStatus()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidXYZv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(),"Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidXYZv10.preProcess")

        self._xyzin = self.getDataInput().getXYZIN().getPath().getValue()  
        
        
    def process(self, _edObject = None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidXYZv10.process")

        self.test(self._xyzin)

        
    def postProcess(self, _edObject = None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecDIMPLECheckValidXYZv10.postProcess")
        # Create some output data
        xsDataResult = CCP4DataResultCheckValidXYZ(returnStatus=self._returnStatus)        
        self.setDataOutput(xsDataResult)


    def test(self,filename):
        EDVerbose.DEBUG("*** EDPluginExecDIMPLECheckValidXYZv10.test")        
        CRYST1Found=False
        ATOMFound=False
        FileIsPDB=False
        f=open(filename,'r')
        pdbreadlines=f.readlines()
        for pdbline in pdbreadlines:

            pdblistofitemsincurrentline=pdbline.split()
            
            if pdblistofitemsincurrentline[0]=="CRYST1":    
                CRYST1Found=True
        
            if pdblistofitemsincurrentline[0]=="ATOM":    
                ATOMFound=True

            if CRYST1Found==True and ATOMFound==True :    
                FileIsPDB=True
                break

        if FileIsPDB == True:
            a=int(1) 
            b=str("The file %s is an pdb type of file") % filename
            self._returnStatus.setCode(XSDataInteger(a))
            self._returnStatus.setMessage(XSDataString(b))                                  
        else:
            a=int(0) 
            b=str("The file %s is NOT an pdb type of file") % filename
            self._returnStatus.setCode(XSDataInteger(a))
            self._returnStatus.setMessage(XSDataString(b))  



        f.close()

    
