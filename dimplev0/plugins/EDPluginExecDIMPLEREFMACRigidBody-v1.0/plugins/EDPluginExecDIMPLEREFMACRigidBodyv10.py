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
from EDImportLib import EDVerbose

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCCP4DIMPLE import CCP4MTZColLabels
from XSDataCCP4DIMPLE import CCP4DataInputREFMACRigidBody
from XSDataCCP4DIMPLE import CCP4DataResultREFMACRigidBody
from XSDataCCP4DIMPLE import XSDataFloat
from XSDataCCP4Factory import XYZ
from XSDataCCP4Factory import CCP4ReturnStatus

class EDPluginExecDIMPLEREFMACRigidBodyv10(EDPluginExecProcessScript):
    '''An EDNA plugin for the CCP4 program refmac5 for rigid body
    refinement.'''

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(CCP4DataInputREFMACRigidBody)

        self._hklin = None
        self._xyzin = None
        self._xyzout = None

        self._ColLabels_F = None
        self._ColLabels_SIGF = None

        return

    def checkParameters(self):
        EDVerbose.DEBUG(
            '*** EDPluginExecDIMPLEREFMACRigidBodyv10.checkParameters')
        self.checkMandatoryParameters(self.getDataInput(),'Data Input is None')

        data = self.getDataInput()

        self.checkMandatoryParameters(data.getHKLIN(),
                                      'No MTZ file specified')
        self.checkMandatoryParameters(data.getXYZIN(),
                                      'No PDB file specified')
        self.checkMandatoryParameters(data.getXYZOUT(),
                                      'No PDB file specified')
        self.checkMandatoryParameters(data.getColLabels(),
                                      'No column labels specified (input)')

        return
    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREFMACRigidBodyv10.preProcess')

        data = self.getDataInput()

        self._hklin = data.getHKLIN().getPath().getValue()
        self._xyzin = data.getXYZIN().getPath().getValue()
        self._xyzout = data.getXYZOUT().getPath().getValue()

        self._ColLabels_F = data.getColLabels().F.getValue()
        self._ColLabels_SIGF = data.getColLabels().SIGF.getValue()

        self.refmac_rigid_body_script()

        return
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREFMACRigidBodyv10.process')

        return
        
    def postProcess(self, _edObject = None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREFMACRigidBodyv10.postProcess')
        
        init_r, init_r_free, final_r, final_r_free = self.parse_refmac_log()

        xsDataResult = CCP4DataResultREFMACRigidBody(
            XYZOUT = XYZ(self._xyzout),
            initialR = XSDataFloat(init_r),
            initialRFree = XSDataFloat(init_r_free),
            finalR = XSDataFloat(final_r),
            finalRFree = XSDataFloat(final_r_free),            
            returnStatus = CCP4ReturnStatus())

        self.setDataOutput(xsDataResult)    

        if not os.path.isfile(self.getDataOutput().getXYZOUT().getPath().getValue()):
            raise RuntimeError, 'File %s does not exist' % self.getDataOutput().getXYZOUT().getPath().getValue() 

        return
    
    def refmac_rigid_body_script(self):
        '''Actually write the script to run refmac5 for rigid body
        refinement.'''
        
        self.setScriptCommandline('hklin "%s" xyzin "%s" xyzout "%s"' % 
                                  (self._hklin, self._xyzin, self._xyzout))
        self.addListCommandExecution('labin FP=%s SIGFP=%s FREE=FreeR_flag' % \
             (self._ColLabels_F, self._ColLabels_SIGF))
        self.addListCommandExecution(
            'labout FC=FC PHIC=PHIC FWT=2FOFCWT PHWT=PH2FOFCWT ' + \
            'DELFWT=FOFCWT PHDELWT=PHFOFCWT')
        self.addListCommandExecution(
            'refinement type rigidbody resolution 15 3.5')
        self.addListCommandExecution(
            'scale type simple lssc anisotropic experimental')
        self.addListCommandExecution(
            'solvent yes vdwprob 1.4 ionprob 0.8 mshrink 0.8')
        self.addListCommandExecution(
            'rigidbody ncycle 10')
        self.addListCommandExecution(
            'end')

        return

    def parse_refmac_log(self):
        '''Parse out the initial and final R and Rfree values from the
        refmac log output.'''
        EDVerbose.DEBUG('*** EDPluginExecDIMPLEREFMACRigidBodyv10.parse_refmac_log')

        init_r = None
        init_r_free = None
        final_r = None
        final_r_free = None

        for record in self.readProcessLogFile().split('\n'):
            if 'Overall R factor                     =' in record:
                final_r = float(record.split()[-1])
                if init_r is None:
                    init_r = final_r
            if 'Free R factor                        =' in record:
                final_r_free = float(record.split()[-1])
                if init_r_free is None:
                    init_r_free = final_r_free

        return init_r, init_r_free, final_r, final_r_free
                
    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        #EDPluginExecDIMPLEPDBSETv10.generateExecutiveSummary(self, _edPlugin)
        EDVerbose.DEBUG("*** EDPluginExecDIMPLEREFMACRigidBodyv10.generateExecutiveSummary")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###      REFMAC (rigid body refinement) Output Log       ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine(self.readProcessLogFile())
        self.addExecutiveSummaryLine("")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("###                End REFMAC Output Log                 ###")
        self.addExecutiveSummaryLine("############################################################")
        self.addExecutiveSummaryLine("")
        self.verboseScreenExecutiveSummary()


