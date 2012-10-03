#
#    Project: The EDNA Archive Project
#             http://www.edna-site.org
#
#    File: "$Id:$"
#
#    Copyright (C) 2008-2009 Diamond Light Source
#                            Chilton, Didcot, UK
#
#    Principal author:       Mark Basham (mark.basham@diamond.ac.uk)
#    
#    with changes from Ghita Kouadri Mostefaoui
#
#    Contributing authors:   Olof Svensson (svensson@esrf.fr) 
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

from EDImportLib import EDVerbose
from EDImportLib import EDString
from EDImportLib import EDList

from EDPluginExec               import EDPluginExec
from EDConfiguration            import EDConfiguration
from EDMessage                  import EDMessage

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataExecSRBRegisterv10 import XSDataInputPluginExecSRBRegister
from XSDataExecSRBRegisterv10 import XSDataResultPluginExecSRBRegister

import os, glob, stat, sys
import re
import fnmatch
import shutil
from xml.dom import minidom
from time import strftime

import fileinput
from time import localtime
import time, datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

class EDPluginExecSRBRegisterv10( EDPluginExec ):
    """
    DLS Archiver plugin
    """

    def __init__( self ):
        """
        Initialise the plugin, mainly set the input class type
        """
        EDPluginExec.__init__( self )
        self.setXSDataInputClass( XSDataInputPluginExecSRBRegister )
        
        self.forArchiving = True
        # statistics variables
        self.statNbFiles = 0
        self.statSize = 0
        self.statInstrument = ''
        self.statVisitID = ''
        self.stats = {} # create an empty dict
        

    def configure( self ):
        """
        Configure the plugin, mainly boiler plate code to get things going
        """
        EDPluginExec.configure( self )
        EDVerbose.DEBUG( "*** EDPluginExecSRBRegisterv10.configure" )
        xsPluginItem = self.getConfiguration()
        if ( xsPluginItem == None ):
            EDVerbose.warning( "EDPluginExecSRBRegisterv10.configure: No DLS Archiver plugin item defined." )
            xsPluginItem = XSPluginItem()


    def preProcess( self, _edObject=None ):
        """
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.preProcess..." )
        self.edXMLFileName = None 
        self.edXMLFileSize = None
        self.edXMLFileValid = True
        

    def process( self, _oalObject=None ):
        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.process..." )
        # Actually run the plugin
        
        # checking for zero size files
        self.getFileSize()
                
        # continue processing if the file size is > 0                
        if ( self.edXMLFileSize > 0 ):
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.process About to create dropfile" )

            # create the dropfile and generate the new XML
            self.createDropFile()
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.process  created dropfile" )
            
            # move the 2 files to there final locations
            self.moveGeneratedFiles()
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.process  files all moved" )
            
        else:
            # this is performed by the Control plugin already, is kept in case the SRBRegister plugin is run alone
            newfileName = self.edXMLFileName.replace( '.clean', '.zero' ) 
            #os.rename( self.edXMLFileName, newfileName )
            shutil.move( self.edXMLFileName, newfileName )
            print strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.process Found zero file " + filepath + '  Renamed to ' + newfileName


    def postProcess( self, _edObject=None ):
        """
        """
        if ( self.edXMLFileSize > 0 ):
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.postProcess..." )  
            # This is to make the tests pass, and it is during the postprocess step where the data is returned from the plugin. 
            xsDataResultPluginExecSRBRegister = XSDataResultPluginExecSRBRegister()
            edOutput = XSDataFile( XSDataString( self.edXMLFileName ) )
            xsDataResultPluginExecSRBRegister.setXmlIngestFileName( edOutput )
            self.setDataOutput( xsDataResultPluginExecSRBRegister ) 


    def generateExecutiveSummary( self, _oedPlugin ):
        """
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.generateExecutiveSummary" )


    def openXMLTree( self ):
        """
        Opens the xml file and places the tree in the object
        """
        # get the filename to load
        # get the data from the plugin
        xsDataInputPluginExecSRBRegister = self.getDataInput()
        # get the string of the path
        xsDataInputPluginExecSRBRegister.getXmlIngestFileName().getPath().getValue() 
        
        edFileName = EDString( xsDataInputPluginExecSRBRegister.getXmlIngestFileName().getPath().getValue() )
        #print '\nedFileName= ' + str( edFileName )
        
        try:
            self.edTree = minidom.parse( edFileName )
        except Exception:
            # This is to make the tests pass, and it is during the postprocess step where the data is returned from the plugin.
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.openXMLTree  Failed to parse file '%s' renaming it." % edFileName )
            #os.rename( edFileName, edFileName + '.invalid' )
            shutil.move( edFileName, edFileName + '.invalid' )


    def processFileList( self ):
        """
        Function that gets a list of all the files out of the input XML, also generates a 
        new XML which will eventually be copied to the output position
        This function will ignore files in sub-directories specified by the subDir ignore filelist
        """

        edReturnList = []                
        
        #print '\nfilepath= ' + str( self.getDataInput().getXmlIngestFileName().getPath().getValue() )
        filepath = str( self.getDataInput().getXmlIngestFileName().getPath().getValue() ) # edFileName
              
        for edElement in self.edTree.getElementsByTagName( "datafile" ) : 
            edInternalFileName = edElement.getElementsByTagName( "location" )[0].childNodes[0].nodeValue
            #print '\nprocessing datafile file... ' + str( edInternalFileName )
                                         
            # checking the validity of the data filename before adding it to the list of files to be processed
            edValidFile = self.validFileName( edInternalFileName )

            if ( edValidFile ):
                #EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.processFileList  Valid: " + str( edValidFile ) )
                edReturnList += [edInternalFileName + '\n']
                            
                #edURI = re.sub( self.getDataInput().getSrbURIPattern().getValue() , self.getDataInput().getSrbURIReplacement().getValue(), edInternalFileName )
                #edElement.getElementsByTagName( "location" )[0].childNodes[0].nodeValue = edURI
                
                # add size information if not present
                sizeElementList = edElement.getElementsByTagName( "file_size" )
                nbSizeElements = len( sizeElementList )
                
                if  nbSizeElements == 0:    
                    # getting the size of the actual data file and append it in a new <file_size> tag in the xml file          
                    # size is computed in 'bytes' as recommended by the ICAT 3.3 data dict. documentation
                    edFileStats = os.stat( edInternalFileName )
                    edFileSize = edFileStats [stat.ST_SIZE]           
                    
                    # creating a new xml tag <file_size>
                    edFileSize_element = self.edTree.createElement( "file_size" ) 
                    txt = self.edTree.createTextNode( str( edFileSize ) )  # creates "file size"
                    edFileSize_element.appendChild( txt )  # results in <file_size>44</file_size>
                    #will be appended as the last child of </datafile> element
                    edElement.appendChild( edFileSize_element )
                     
                else:
                    print 'size file info already present in datafile element file.'
        
                # new XML file temporary creation filename
                #self.edTempXMLFileName = self.getDataInput().getXmlIngestFileName().getPath().getValue() + ".tempxmlingest"
        
                #edXMLTempFile = open( self.edTempXMLFileName, "w" )
                #self.edTree.writexml( edXMLTempFile )
                #edXMLTempFile.close()     
            else:
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.processFileList  Removing the datafile element " + str( edInternalFileName ) ) 
                self.edTree.getElementsByTagName( "dataset" )[0].removeChild( edElement )
                   
                                    
        # new XML file temporary creation filename
        #self.edTempXMLFileName = self.getDataInput().getXmlIngestFileName().getPath().getValue() + ".tempxmlingest"
        self.edTempXMLFileName = filepath + ".tempxmlingest"
        
        edXMLTempFile = open( self.edTempXMLFileName, "w" )
        self.edTree.writexml( edXMLTempFile )
        edXMLTempFile.close()              
                                    
        return edReturnList


    def createDropFile( self ):
        """
        Function to generate the dropfile in the location specified by the input, this 
        should generate a file which has .drop on the end, as the final file will be moved from this 
        location as an atomic operation.
        """
        
        # first load the tree
        self.openXMLTree()
        
        self.checkAgainstIgnoreList()
               
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.createDropFile Archiving tag set to :" + str( self.forArchiving ) ) 
        # then check to see if this is to be archived or not
        if( self.forArchiving ):
            
            # first generate the list of files which are to be put into the file
            edFileList = self.processFileList()
            
            # drop file temporary creation filename
            self.edTempDropFileName = self.getDataInput().getXmlIngestFileName().getPath().getValue() + ".drop"
            
            
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.createDropFile temp dropfile named " + str( self.edTempDropFileName ) )   
            
            # now write the file into a temporary location 
            edTempFile = open( self.edTempDropFileName, "w" )
            edTempFile.writelines( edFileList )
            edTempFile.close()
            
            # # #
            # keep a copy of clean files before being registered with srb
            # # #
            dirList = str(self.edTempDropFileName).split('/')
            name = dirList[-1]
            targetsubdir = str(self.edTempDropFileName).replace(name, '')
            self.keepFileCopy(self.edTempDropFileName, targetsubdir, 'srboutput')                                
            # # #
            
            # now write the list of file locations into the trace file
            self.saveProcessedStoraged( edFileList )
                     
            # 
            # recording
            #
            fi = fileinput.FileInput( self.edTempDropFileName )
            for edInternalFileName in fi: 
                ## recording the stats
                #print str( edInternalFileName )
                self.statNbFiles += 1
                statFileSize = ' % .5f' % ( ( os.path.getsize( edInternalFileName.rstrip() ) ) / ( 1024 * 1024.0 * 1024.0 ) )
                #statFileSize = os.path.getsize( edInternalFileName.rstrip() )
                self.statSize = self.statSize + float( statFileSize )

                list = edInternalFileName.split( '/' )                     
                self.statInstrument = list[2]
                self.statVisitID = list[5]
                ##self.statNbFiles =
                #print 'statInstrument = ' + str( statInstrument )
                #print 'statVisitID = ' + str( statVisitID )
            fi.close()
            
            #print '\nrecordStats...' + str( statInstrument ) + ' - ' + str( statVisitID ) + ' - ' + str( self.statNbFiles ) + ' - ' + str( self.statSize )
            
            self.recordStats( self.statInstrument, self.statVisitID, self.statNbFiles, self.statSize )
            # write stats from dict to file
            csvFile = '/dls/bl-misc/dropfiles2/icat/stats/stats-storaged.csv' # should be fetched from xml file
            #csvFile = self.getDataInput().getStoragedCsvFile().getPath().getValue()
            fileHandle = open ( csvFile , 'a' ) 
            for key in self.stats:
                contents = self.stats[key]
                #print str( str( contents[0] ) + '    ' + str( contents[1] ) + '    ' + str( contents[2] ) + '        ' + str( contents[3] ) + '\n' )
                fileHandle.writelines( str( contents[0] ) + ', ' + str( contents[1] ) + ', ' + str( contents[2] ) + ', ' + str( contents[3] ) + '\n' )     
        
            fileHandle.close()


    def checkAgainstIgnoreList( self ):
        """
        This function sets the self.forArchiving tag to false, if the archiving is not required
        """
        
        self.forArchiving = True;
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.checkAgainstIgnoreList setting archiving tag to :" + str( self.forArchiving ) ) 
        
        try:
            edVisitId = ( self.edTree.getElementsByTagName( "visit_id" )[0].childNodes[0].nodeValue )
            #print '\nedVisitId = ' + str( edVisitId )
        except Exception:
            print "Unexpected error:", sys.exc_info()[0]
            raise    
                      
        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.checkAgainstIgnoreList tag for comparison :" + str( edVisitId ) ) 
        
        for edElement in self.getDataInput().getIgnoreList() :
            
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.checkAgainstIgnoreList ignore list parameter :" + edElement.getValue() ) 
            # will also ignore visit-ids with no dash
            if ( fnmatch.fnmatch( edVisitId.upper(), edElement.getValue().upper() ) or ( str( edVisitId.upper() ).find( '-' ) == -1 ) ):
                self.forArchiving = False
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.checkAgainstIgnoreList setting archiving tag to :" + str( self.forArchiving ) ) 
        

    def moveGeneratedFiles( self ):
        """
        Function to move the files automatically to their new locations
        """
        
        # check to see if these files have been created
        if ( self.forArchiving ) :
            # generate the icat Filename
            self.edXMLFileName = self.getDataInput().getXmlIngestFileName().getPath().getValue() + ".icat"
            
            dropfileStats = os.stat( self.edTempDropFileName )
            dropfileSize = dropfileStats [stat.ST_SIZE]
            
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.movegeneratedFiles is moving '" + self.edTempDropFileName + "' to '" + self.getDataInput().getSrbDropFileName().getPath().getValue() )      
            # make the dropfile writable by all
            os.chmod( self.edTempDropFileName, 0777 )
            
            # move the .drop file into the dropfiles zone
            #os.rename( self.edTempDropFileName, self.getDataInput().getSrbDropFileName().getPath().getValue() )
            shutil.move( self.edTempDropFileName, self.getDataInput().getSrbDropFileName().getPath().getValue() )
                        
            # first rename the tmp dropfile into *.icat for the ICAT ingester to find it
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.movegeneratedFiles is moving '" + self.edTempXMLFileName + "' to '" + self.edXMLFileName ) 
            #os.rename( self.edTempXMLFileName, self.edXMLFileName )
            shutil.move( self.edTempXMLFileName, self.edXMLFileName )
                        
               
        # Whatever happens remove the original file
        os.remove( self.getDataInput().getXmlIngestFileName().getPath().getValue() )

    def getFileSize( self ):
        """
        Function to compute the file size
        """      
        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.getFileSize..." )
        # get the filename to load
        # get the data from the plugin
        xsDataInputPluginExecSRBRegister = self.getDataInput()
        # get the string of the path
        xsDataInputPluginExecSRBRegister.getXmlIngestFileName().getPath().getValue() 
        
        edFileName = EDString( xsDataInputPluginExecSRBRegister.getXmlIngestFileName().getPath().getValue() )
        
        # get the size of the current file
        edFileStats = os.stat( edFileName )
        self.edXMLFileSize = edFileStats [stat.ST_SIZE]
                
        #return
            

    def recordStats( self, instr, visitid, nbFiles, size ):
        
        if  self.stats.has_key( visitid ):
            #print 'visitID already exists ', visitid
            # update nbFiles and size
            content = self.stats[visitid]
            nNbFiles = int( content[2] ) + nbFiles
            nSize = int( content[3] ) + size
            
            # update the hashmap
            self.stats[visitid] = instr, visitid, nNbFiles, nSize
        else:
            #print 'does not exist: ', visitid 
            # create new record with new visitid
            self.stats[visitid] = instr, visitid, nbFiles, size     

    
    def validFileName( self, filenamepath ):
        """
        check the validity of the filename
        (a) against invalid characters, e.g. '(' 
        (b) against invalid sub-directories in their path, e.g. processing, spool
        """
                
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.validFileName..." + str( filenamepath ) )
        
        validFileName = True
        validFilePath = True
            
        #String illegal = "\"M\"\\a/ry/ h**ad:>> a\\/:*?\"| li*tt|le|| la\"mb.?";
        illegal = "()\\";#"()\\,'\ / :*? <>| ()"    
        for letter in str( filenamepath ):
            if ( letter in illegal ):
                validFileName = False
                print 'filenamepath ' + str( filenamepath )
                #EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.validFileName  ( 1 )validFileName:" + str( validFileName ) )        
    
        if validFileName :
            for edElement in self.getDataInput().getIgnoreSubdirList() :
                #EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.validFileName subdir ignore list parameter :" + edElement.getValue() ) 
                # correct --> ignore only if in subdir after visit-dir
                list = ( str( filenamepath ) ).split( '/' )
                # extract subdir just underneath the visit directory
                subdir = list[6] 
                #print '\nsubdir= ' + str( subdir )
                
                if ( edElement.getValue().upper() in subdir.upper() ):#fnmatch.fnmatch( filenamepath(), edElement.getValue().upper() ) :
                    validFilePath = False
                    print strftime("%Y-%m-%d %H:%M:%S") + ' filenamepath discared as in ignored subdirectory ' + str( filenamepath )
                    #EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecSRBRegisterv10.validFileName  ( 2 )validFilePath:" + str( validFilePath ) ) 

        return ( validFileName and validFilePath )
    
    
    def saveProcessedStoraged( self, edfilelist ):
        """
        record the list of files given to storaged
        """
        #processedStoraged = self.getDataInput().getStoragedProcessedFiles().getPath().getValue()#'/dls/bl-misc/dropfiles2/icat/stats/storaged-processed'
        processedStoraged = '/dls/bl-misc/dropfiles2/icat/stats/storaged-processed'
        print '\n-----' + str( processedStoraged )
        
        for filepath in edfilelist:
            
            filepath = filepath.strip( '\n' )         
            aList = filepath.split( '/' )                     
            statInstrument = aList[2]
            statVisitID = aList[5]
            
            #get dataset_name
            if len( aList ) == 7:
                datasetname = 'topdir'
    
            if len( aList ) > 7:
                datasetname = aList[6]
                                
            for i in range( 7, len( aList ) - 1 ):
                datasetname = datasetname + '/' + str( aList[i] )
            
            now = time.strftime( "%H:%M:%S", time.localtime() )
            today = datetime.date.today()
            
            fileHandle = open ( processedStoraged , 'a' )
            fileHandle.writelines( str( filepath ) + '\t' + str( today ) + 'T' + str( now ) + '\t' + str( statInstrument ) + '\t' + str( statVisitID ) + '\t' + str( datasetname ) + '\n' )     
            fileHandle.close()  
        
    
    def keepFileCopy(self, fullname, targetsubdir, destsubdir):
        # keep a copy of file to be processed by CleanAll(), SRBRegister(), ICATIngets(),...

        fullname = fullname.encode('ascii','ignore')

        nameList = fullname.split('/')
        name = nameList[-1]
        #print '\nname = '+str(name)
        dest = os.path.join(destsubdir, name)

        print '\n' +strftime("%Y-%m-%d %H:%M:%S") + ' *** EDPluginExecSRBRegisterv10...keepFileCopy() ', fullname, ' to ', os.path.join( targetsubdir,dest) 
        shutil.copy2(fullname, os.path.join( targetsubdir,dest))         
    
    

