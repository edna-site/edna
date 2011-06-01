#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS
#
#    Principal author:       irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

import os

from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataIfeffit import XSDataInputAtoms
from XSDataIfeffit import XSDataResultAtoms
from XSDataIfeffit import XSDataAtomsSample

from XSDataIfeffit import XSDataFile, XSDataString


class EDPluginExecAtomsv0_1(EDPluginExecProcessScript):
    """
    Execution plugin for ab-initio model determination using Ifeffit
    """

    def __init__(self):
        """
        """
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputAtoms)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecAtomsv0_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecAtomsv0_1.preProcess")
        self.generateAtomsInputFile()


    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        EDVerbose.DEBUG("EDPluginExecAtomsv0_1.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecAtomsv0_1.postProcess")
        
        xsDataResult = XSDataResultAtoms()
        
        pathOutputFile = XSDataString(os.path.join(self.getWorkingDirectory(), 'feff.inp'))
        xsDataResult.setInpFile(XSDataFile(pathOutputFile))
        
        self.setDataOutput(xsDataResult)

    
    def generateInputCard(self, _dictInputData):
        _listInputCard = []
        for key, item in _dictInputData.iteritems():
            if item is not None:
                _listInputCard.append(' '.join([key,str(item.getValue())]))
            
        return ' '.join(_listInputCard)

    
    def generateAtomsCard(self, _xsDataAtomsSites):
        _listInputCard = ["atom", "! Atom.type    x    y    z    tags"]
        for site in _xsDataAtomsSites:
            _tmpList = [site.getType().getValue(), \
                        str(site.getX().getValue()), \
                        str(site.getY().getValue()), \
                        str(site.getZ().getValue())]
            if site.getTag() is not None:
                _tmpList.append(site.getTag().getValue())
                
            _listInputCard.append(' '.join(_tmpList))
            
        return _listInputCard
    
    
    def generateAtomsInputFile(self):
        EDVerbose.DEBUG("EDPluginExecAtomsv0_1.generateAtomsInput")
        
        _listInputLines = []
        
        _listInputLines.append(' '.join(['title',self.getDataInput().getTitle().getValue()]))
        
        _xsDataAtomsCrystal = self.getDataInput().getCrystal()
        _dictCrystal = {'space':    _xsDataAtomsCrystal.getSpace(), \
                        'a':        _xsDataAtomsCrystal.getA(), \
                        'b':        _xsDataAtomsCrystal.getB(), \
                        'c':        _xsDataAtomsCrystal.getC(), \
                        'alpha':    _xsDataAtomsCrystal.getAlpha(), \
                        'beta':     _xsDataAtomsCrystal.getBeta(), \
                        'gamma':    _xsDataAtomsCrystal.getGamma()}
        _listInputLines.append(self.generateInputCard(_dictCrystal))
        
        if _xsDataAtomsCrystal.getShift() is not None:
            _listInputLines.append(' '.join(['shift', \
                                          _xsDataAtomsCrystal.getShift().getDx().getValue(), \
                                          _xsDataAtomsCrystal.getShift().getDy().getValue(), \
                                          _xsDataAtomsCrystal.getShift().getDz().getValue()]))
        
        _xsDataAtomsSample = self.getDataInput().getSample()
        _dictSample = {'core':      _xsDataAtomsSample.getCore(), \
                       'edge':      _xsDataAtomsSample.getEdge(), \
                       'rmax':      _xsDataAtomsSample.getRmax(), \
                       'nitrogen':  _xsDataAtomsSample.getNitrogen(), \
                       'argon':     _xsDataAtomsSample.getArgon(), \
                       'krypton':   _xsDataAtomsSample.getKrypton()}
        _listInputLines.append(self.generateInputCard(_dictSample))
        
        if self.getDataInput().getFlags() is not None:
            _xsDataAtomsFlags = self.getDataInput().getFlags()
            _dictFlags = {'index':          _xsDataAtomsFlags.getIndex(), \
                          'ffef':           _xsDataAtomsFlags.getFeff(), \
                          'ffef8':          _xsDataAtomsFlags.getFeff8(), \
                          'corrections':    _xsDataAtomsFlags.getCorrections(), \
                          'geom':           _xsDataAtomsFlags.getGeom(), \
                          'unit':           _xsDataAtomsFlags.getUnit(), \
                          'p1':             _xsDataAtomsFlags.getP1()}
            _listInputLines.append(self.generateInputCard(_dictFlags))
            
        if self.getDataInput().getOutputFile() is not None:
            _listInputLines.append(' '.join(['out', self.getDataInput().getOutputFile().getValue()]))
            
        _listInputLines.extend(self.generateAtomsCard(self.getDataInput().getSites()))
        
        _atomsInputFileName = os.path.join(self.getWorkingDirectory(), "atoms.inp")
        EDUtilsFile.writeFile(_atomsInputFileName, '\n'.join(_listInputLines))
        

    def generateExecutiveSummary(self,__edPlugin=None):
            self.addExecutiveSummaryLine(self.readProcessLogFile())
