# coding: utf8
#
#    Project: MX Plugin Exec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsTable              import EDUtilsTable

from XSDataCommon import XSDataDouble

from XSDataDnaTables import dna_tables

from XSDataRdfitv1_0 import XSDataInputRdfit
from XSDataRdfitv1_0 import XSDataResultRdfit

class EDPluginRdfitv1_0(EDPluginExecProcessScript ):
    """
    This plugin runs the rdfit program written by Sasha Popov:

    There is the help for  RDFIT
    rdfit --help
    
    RDFIT can read xml file after BEST burn strategy and also write results in xml format and create  GLE files.
    
    For EDNA one can run rdfit as:
    rdfit -d best_htm.file  -glr rdfit_graph.gle   -xml out_xml.file [ xds.HKL files]
    
    For GLE It will make 3 data files with fixed names : B2D.dat, I2D.dat, S2D.dat.
    
    To run RDFIT need to set (like for BEST)
    setenv rdfithome  rdfit_directory  - can be used the BEST directory where must be file - symop.lib 
    """
    

    def __init__(self ):
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputRdfit)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")
        self.checkMandatoryParameters(self.dataInput.getBestXmlFile(),"Best XML file path is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.preProcess")
        xsDataInputRdfit = self.getDataInput()
        self.setScriptCommandline(self.generateCommands(xsDataInputRdfit))

        
        
    def process(self, _edObject = None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.process")

        
    def finallyProcess(self, _edObject = None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginExecMtz2Variousv1_0.finallyProcess")
        xsDataResult = self.getOutputDataFromDNATableFile("rdfit.xml")
        self.setDataOutput(xsDataResult)
    
    def generateCommands(self, _xsDataInputRdfit):
        """
        This method creates a list of commands for mtz2various
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.generateCommands")

        if _xsDataInputRdfit is not None:
            
            strScriptCommandLine = " -d " + _xsDataInputRdfit.bestXmlFile.path.value
            
            if _xsDataInputRdfit.dmin is not None:
                strScriptCommandLine += " -dmin %f" % _xsDataInputRdfit.dmin.value
                
            if _xsDataInputRdfit.defaultBeta is not None:
                strScriptCommandLine += " -beta %f" % _xsDataInputRdfit.defaultBeta.value
            
            if _xsDataInputRdfit.defaultGama is not None:
                strScriptCommandLine += " -gama %f" % _xsDataInputRdfit.defaultGama.value
            
            if _xsDataInputRdfit.bFactorMtvplotFile is not None:
                strScriptCommandLine += " -gb " + _xsDataInputRdfit.bFactorMtvplotFile.path.value
            
            if _xsDataInputRdfit.bFactorGlePlotFile is not None:
                strScriptCommandLine += " -gr " + _xsDataInputRdfit.bFactorGlePlotFile.path.value
            
            if _xsDataInputRdfit.bScaleIntensityMtvPlotFile is not None:
                strScriptCommandLine += " -glb " + _xsDataInputRdfit.bScaleIntensityMtvPlotFile.path.value
            
            if _xsDataInputRdfit.bScaleIntensityGleFile is not None:
                strScriptCommandLine += " -glr " + _xsDataInputRdfit.bScaleIntensityGleFile.path.value
            
            if _xsDataInputRdfit.resultsFile is not None:
                strScriptCommandLine += " -result " + _xsDataInputRdfit.resultsFile.path.value
            
            if _xsDataInputRdfit.resultsXmlFile is None:
                strScriptCommandLine += " -xml rdfit.xml"
            else:
                strScriptCommandLine += " -xml " + _xsDataInputRdfit.resultsXmlFile.path.value
                
            for xsDataFile in _xsDataInputRdfit.xdsHklFile:
                strScriptCommandLine += " " + xsDataFile.path.value
            
            return strScriptCommandLine

    
    def getOutputDataFromDNATableFile(self, _strFileName):
        """Parses the result 'DNA'-type XML file"""
        xsDataResultRdfit = XSDataResultRdfit()
        strDnaTablesXML = self.readProcessFile(_strFileName)
        xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
        # Loop through all the tables and fill in the relevant parts of xsDataResultBest
        xsDataRDFIT_Results = EDUtilsTable.getTableListFromTables(xsDataDnaTables, "RDFIT_Results")[0]
        xsDataListGeneral = EDUtilsTable.getListsFromTable(xsDataRDFIT_Results, "general")[0]
        xsDataItemBeta = EDUtilsTable.getItemFromList(xsDataListGeneral, "beta")
        if xsDataItemBeta is not None:
            beta = xsDataItemBeta.getValueOf_()
            xsDataResultRdfit.setBeta(XSDataDouble(beta))
        xsDataItemGama = EDUtilsTable.getItemFromList(xsDataListGeneral, "gama")
        if xsDataItemGama is not None:
            gama = xsDataItemGama.getValueOf_()
            xsDataResultRdfit.setGama(XSDataDouble(gama))
        xsDataItemDose_half_th = EDUtilsTable.getItemFromList(xsDataListGeneral, "Dose_1/2_th")
        if xsDataItemDose_half_th is not None:
            dose_half_th = xsDataItemDose_half_th.getValueOf_()
            xsDataResultRdfit.setDose_half_th(XSDataDouble(dose_half_th))
        xsDataItemDose_half = EDUtilsTable.getItemFromList(xsDataListGeneral, "Dose_1/2")
        if xsDataItemDose_half is not None:
            dose_half = xsDataItemDose_half.getValueOf_()
            xsDataResultRdfit.setDose_half(XSDataDouble(dose_half))
        xsDataItemRelative_radiation_sensitivity = EDUtilsTable.getItemFromList(xsDataListGeneral, "Relative_Radiation_Sensitivity")
        if xsDataItemRelative_radiation_sensitivity is not None:
            relative_radiation_sensitivity = xsDataItemRelative_radiation_sensitivity.getValueOf_()
            xsDataResultRdfit.setRelative_radiation_sensitivity(XSDataDouble(relative_radiation_sensitivity))
        return xsDataResultRdfit
