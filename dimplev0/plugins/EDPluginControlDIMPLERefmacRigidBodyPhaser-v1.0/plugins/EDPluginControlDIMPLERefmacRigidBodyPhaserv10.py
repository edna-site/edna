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

import os

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl

from XSDataCCP4DIMPLE import CCP4DataInputControlRefmacRigidBodyPhaser
from XSDataCCP4DIMPLE import CCP4DataResultControlRefmacRigidBodyPhaser
from XSDataCCP4DIMPLE import CCP4DataInputPhaser
from XSDataCCP4DIMPLE import CCP4DataInputREFMACRigidBody

from XSDataCCP4DIMPLE import XSDataFloat
from XSDataCCP4DIMPLE import CCP4MTZColLabels

from XSDataCCP4Factory import HKL
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginControlDIMPLERefmacRigidBodyPhaserv10( EDPluginControl ):
    """
    A control plugin that uses 2 exec plugins (RefmacRigidBody and Phaser)
    and returns a XYZ file depending on the values found in the input
    files (HKL and XYZ)
    """

    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(CCP4DataInputControlRefmacRigidBodyPhaser)

        self._refmacrigidbody_plugin = None
        self._phaser_plugin = None

        self._xyzin = None
        self._hklin = None
        self._xyzout = None
        self._hklout = ' '

        self._ColLabels = None

        return

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getHKLIN(),"No input MTZ file given")
        self.checkMandatoryParameters(self.getDataInput().getXYZIN(),"No input PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getXYZOUT(),"No output PDB file given")
        self.checkMandatoryParameters(self.getDataInput().getColLabels(),
                                      'No column labels specified (input)')

        return

    
    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.preProcess")        
        
        self._refmacrigidbody_plugin = self.loadPlugin('EDPluginExecDIMPLEREFMACRigidBodyv10')
        self._phaser_plugin = self.loadPlugin('EDPluginExecDIMPLEPHASERv10')

        self._xyzin = self.getDataInput().getXYZIN().getPath().getValue()  
        self._hklin = self.getDataInput().getHKLIN().getPath().getValue()
        self._xyzout = self.getDataInput().getXYZOUT().getPath().getValue()   

        self._ColLabels = self.getDataInput().getColLabels()

        return

        
    def process(self, _edObject = None):
        EDPluginControl.process(self)
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.process")

        self._refmacrigidbody_plugin.setDataInput(CCP4DataInputREFMACRigidBody(
            XYZIN = XYZ(self._xyzin),
            HKLIN = HKL(self._hklin),
            XYZOUT = XYZ(self._xyzout),
            ColLabels = self._ColLabels))        

        self._refmacrigidbody_plugin.connectSUCCESS(self.doSuccess_RefmacRigidBody)
        self._refmacrigidbody_plugin.connectFAILURE(self.doFailure_RefmacRigidBody)
        

        self._refmacrigidbody_plugin.executeSynchronous()        


    
    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.postProcess")
        # Create some output data
        
        xsDataResult = CCP4DataResultControlRefmacRigidBodyPhaser(
            XYZOUT = XYZ(self._xyzout),
            returnStatus = CCP4ReturnStatus())            
        self.setDataOutput(xsDataResult)
    

    def doSuccess_RefmacRigidBody(self,  _edPlugin = None):
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doSuccess_RefmacRigidBody")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doSuccess_RefmacRigidBody")

        dimple_FinalRFree = self._refmacrigidbody_plugin.getDataOutput().getFinalRFree().getValue()
 
        if dimple_FinalRFree > 0.45:
            phaser_input = CCP4DataInputPhaser(
            HKLIN = HKL(self._hklin),
            XYZIN = XYZ(self._xyzin),
            HKLOUT = HKL(self._hklout),
            XYZOUT = XYZ(self._xyzout),
            ColLabels = self._ColLabels)
            

            self._phaser_plugin.setDataInput(phaser_input)
         

            self._phaser_plugin.connectSUCCESS(self.doSuccess_Phaser)
            self._phaser_plugin.connectFAILURE(self.doFailure_Phaser)
        
            self._phaser_plugin.executeSynchronous()        

        return


    def doFailure_RefmacRigidBody(self,  _edPlugin = None):
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doFailure_RefmacRigidBody")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doFailure_RefmacRigidBody")

        raise RuntimeError, 'RefmacRigidBody failed'

        return


    def doSuccess_Phaser(self,  _edPlugin = None):
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doSuccess_Phaser")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doSuccess_Phaser")

        return


    def doFailure_Phaser(self,  _edPlugin = None):
        EDVerbose.DEBUG("EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doFailure_Phaser")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlDIMPLERefmacRigidBodyPhaserv10.doFailure_Phaser")

        raise RuntimeError, 'Phaser failed'

        return




