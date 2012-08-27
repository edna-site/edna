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
from suds.wsse import *
from suds.client import Client

from EDImportLib import EDVerbose
from EDImportLib import EDString
from EDImportLib import EDList

from EDPluginExec import EDPluginExec
from EDConfiguration            import EDConfiguration
from EDMessage                  import EDMessage

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString

from XSDataExecICATIngesterv10 import XSDataInputPluginExecICATIngester
from XSDataExecICATIngesterv10 import XSDataResultPluginExecICATIngester

import os, glob, stat, time
import datetime
import math, shutil

from xml.dom import minidom
from time import strftime


class EDPluginExecICATIngesterv10( EDPluginExec ):
    """
    DLS Archiver plugin
    """
    
    def __init__( self ):
        EDPluginExec.__init__( self )
        self.setXSDataInputClass( XSDataInputPluginExecICATIngester )
    
        self.sessionID = 'sid';
        

    def configure( self ):
        EDPluginExec.configure( self )
        EDVerbose.DEBUG( "*** EDPluginExecICATIngesterv10.configure" )
        xsPluginItem = self.getConfiguration()
        if ( xsPluginItem == None ):
            EDVerbose.warning( "EDPluginExecICATIngesterv10.configure: No DLS Archiver plugin item defined." )
            xsPluginItem = XSPluginItem()


    def preProcess( self, _edObject=None ):
        """
        Pre-process
        """
        EDVerbose.DEBUG( "*** EDPluginExecICATIngesterv10.preProcess..." )

    def process( self, _oalObject=None ):
               
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process..." )
        # Actually run the plugin
        xsDataInputPluginExecICATIngester = self.getDataInput()
               
        #edXMLFilePath = xsDataInputPluginExecICATIngester.getXmlIngestFileName().getPath().getValue()
        
        # Now check the directory given to see if there are any xml ingest files in there       
        searchDir = xsDataInputPluginExecICATIngester.getXmlSearchDir().getPath().getValue()
        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process    searchDir=  " + str( searchDir ) )    
        
        fileList = self.sortFiles( searchDir, 'icat' )    
        nbFiles = len( fileList )
                                
        for name in fileList:            
            # statistics variables
            # should be fetched from xml input file
            self.csvFile = '/dls/bl-misc/dropfiles2/icat/stats/stats-icat.csv'
            #self.csvFile = self.getDataInput().getIcatCsvFile().getPath().getValue() #'/dls/bl-misc/dropfiles2/icat/stats/stats-icat.csv' # should be fetched from xml file
            self.statNbFiles = 0
            self.statSize = 0
            self.statInstrument = ''
            self.statVisitID = ''
            self.stats = {} # create an empty dict
                               
            edXMLFilePath = os.path.join( searchDir , name )
            #print 'edXMLFilePath= ' + str( edXMLFilePath )
            
            # # #
            # keep a copy of input icat files before being ingested
            # # #
            self.keepFileCopy(edXMLFilePath, searchDir, 'icatinput')                                
            # # #  
            
            xmlFile = open( edXMLFilePath, "r" )
            xmlString = xmlFile.read()

            try:   
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** Ingesting " + str( edXMLFilePath ) )
                # to be used in split if needed
                fileTree = minidom.parse( edXMLFilePath )
                nbDatafiles = len( fileTree.getElementsByTagName( "datafile" ) )
                
                if nbDatafiles > 0 :

                   self.ingestXML( xmlString )
                   
                   EDVerbose.DEBUG( "" ) #some space to make the following debug visible
                   EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** File " + str( edXMLFilePath ) + " has been successfully ingested." )
                   EDVerbose.DEBUG( "" )
                   
                   # # #
                   # keep a copy of input icat files before being ingested
                   # # #
                   self.keepFileCopy(edXMLFilePath, searchDir, 'icatsuccess')                                
                   # # #
                   
                   ### begin record statistics ### 
                   #fi = fileTree.getElementsByTagName( "datafile" )
                   
                   #fi is the list of filenames
                   #for i in fi:
                       #edInternalFileName = str( i.getElementsByTagName( "location" )[0].childNodes[0].nodeValue )
                                            
                       ##print '\nrecordStats ==== ' + str( edInternalFileName )
                       #self.statNbFiles += 1
                       #statFileSize = '%.5f' % ( ( os.path.getsize( edInternalFileName.rstrip() ) ) / ( 1024 * 1024.0 * 1024.0 ) )
                       ##statFileSize = os.path.getsize( edInternalFileName.rstrip() )
                       #self.statSize = self.statSize + float( statFileSize )

                       #list = edInternalFileName.split( '/' )                     
                       #self.statInstrument = list[2]
                       #self.statVisitID = list[5]
                       
                       ## save file locations 
                       #self.saveSuccessICAT( edInternalFileName )
                       
                   ##fi.close()
            
                   ##print '\nrecordStats...' + str( statInstrument ) + ' - ' + str( statVisitID ) + ' - ' + str( self.statNbFiles ) + ' - ' + str( self.statSize )
            
                   #self.recordStats( self.statInstrument, self.statVisitID, self.statNbFiles, self.statSize )
                   ## write stats from dict to file
                   #fileHandle = open ( self.csvFile , 'a' ) 
                   #for key in self.stats:
                       #contents = self.stats[key]
                       ##print str( str( contents[0] ) + '    ' + str( contents[1] ) + '    ' + str( contents[2] ) + '        ' + str( contents[3] ) + '\n' )
                       #fileHandle.writelines( str( contents[0] ) + ',    ' + str( contents[1] ) + ',    ' + str( contents[2] ) + ',        ' + str( contents[3] ) + '\n' )     
        
                   #fileHandle.close()
                   #### end record statistics ###
                   
                   
                   # all went well, so move the file to the archive location
                   edSplitFilePath = edXMLFilePath.split( '/' )
                   edFileName = '/' + edSplitFilePath[len( edSplitFilePath ) - 1]
                
                   edArchiveDir = xsDataInputPluginExecICATIngester.getXmlArchiveDirectory().getPath().getValue() 
                   edTree = minidom.parse( edXMLFilePath )
                
                   #extract the visit_id from the .icat file
                   edVisitId = ( edTree.getElementsByTagName( "visit_id" )[0].childNodes[0].nodeValue ) 
                
                   #edCurrentYear = now.year
                   edArchiveLocation = edArchiveDir + edVisitId + '/'

                   #check if the directory exists, if not create it labelled with the visit_id
                   if ( not os.path.isdir( edArchiveLocation ) ):
                       print 'folder ' + edArchiveLocation + ' does not exist. Creating it ...'
                       os.mkdir( edArchiveLocation )
                   #else:
                       #print 'folder %s exists.' % edArchiveLocation
                   
                   
                   # move the .xml.icat file into its corresponding archive location
                   EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process. about to go into os.path.join" )
                   edDestination = os.path.join( edArchiveLocation, edFileName )

                   EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process. removing file, instead of moving it to the archive location" )
                   #os.rename( edXMLFilePath, edDestination )
                   #shutil.move( edXMLFilePath, edDestination )
                   os.remove( edXMLFilePath )
                   EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " ***  EDPluginExecICATIngesterv10.process. removed" + edXMLFilePath )
                                      
                   EDVerbose.DEBUG( "" ) #some space to make the following debug visible
                   #EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process. Ingested file moved from " + edXMLFilePath + ' to ' + edDestination )
                   EDVerbose.DEBUG( "" ) #some space to make the following debug visible
                      
                   
                else:# nbDatafiles == 0 :
                    #edNewName = edXMLFilePath + ".nodatafile"
                    EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.process. Contain no datafile element, deleting..." + edXMLFilePath )
                    os.remove( edXMLFilePath )
                    #os.rename( edXMLFilePath, edNewName )
                    
            except Exception as er:              
                
                #if nbDatafiles == 1:
                    #i = fileTree.getElementsByTagName( "datafile" )[0]
                    #edInternalFileName = str( i.getElementsByTagName( "location" )[0].childNodes[0].nodeValue )
                    
                    #self.saveFailedICAT( edInternalFileName )
                            
                    ###
                    # add ingest error tag and rename into .failedtoingest file
                    ###
                    
                    edDatasetElement = fileTree.getElementsByTagName( "dataset" )[0]
                    # creating a new xml tag <ingest_error>
                    edIngestError_element = fileTree.createElement( "ingest_error" ) 
                    txt = fileTree.createTextNode( str( er ) )  # creates ingest error
                    edIngestError_element.appendChild( txt )  # results in <ingest_error> Failed to ingest </ingest_error>
                    #will be appended as the last child of </dataset> element
                    edDatasetElement.appendChild( edIngestError_element ) 
                    
                    # saving the new tree in the xml file
                    edNewName = edXMLFilePath + ".failedtoingest"
        
                    edXMLTempFile = open( edNewName, "w" )
                    fileTree.writexml( edXMLTempFile )
                    edXMLTempFile.close()
                    
                    # delete the original .icat file 
                    os.remove(edXMLFilePath)
                    #shutil.rmtree(edXMLFilePath, ignore_errors, onerror)
                    
                    # move the .failedtoingest into the failedtoingest subdir
                    # extract full filename                       
                    pathSplit = os.path.split( edNewName )
                        
                    newFolder = os.path.join( pathSplit[0], 'failedtoingest' ) # folder name should be extracted from input xml file
                    individualFile = pathSplit[1]
                    
                    ###
                    
                    print '\nmoving ' + str( edNewName ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
                    #os.rename( edNewName, os.path.join( newFolder, individualFile ) )       
                    shutil.move( edNewName, os.path.join( newFolder, individualFile ) )
                    
                    # 
                    EDVerbose.DEBUG( "" ) #some space to make the following debug visible  
                    EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** problem ingesting " + edXMLFilePath + " file moved to " + str( edNewName ) )
                    EDVerbose.DEBUG( "" ) #some space to make the following debug visible                
                #else:# nbDatafiles > 1:
                    # split into 2 halves                   
                    #print 'process -- nbDatafiles= ' + str( nbDatafiles )
                    #commented out below one to stop splitting.
                    #self.splitBigFiles( edXMLFilePath, math.trunc( nbDatafiles / 2 ) )
                                
        #logout from the webservice session              


    def postProcess( self, _edObject=None ):
        """
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.postProcess..." )  
        # This is to make the tests pass, and it is during the postprocess step where the data is returned from the plugin. 
        xsDataResultPluginExecICATIngester = XSDataResultPluginExecICATIngester()
        
        #xsDataResultPluginExecICATIngester.setSessionID( XSDataString( self.sessionID ) )
        self.setDataOutput( xsDataResultPluginExecICATIngester ) 
  


    def generateExecutiveSummary( self, _oedPlugin ):
        """
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATRegisterv10.generateExecutiveSummary" )

    def refreshSessionID( self ) :
        """
        Connect to the ICAT and return the new sessionID
        """ 
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATRegisterv10.refreshSessionID..." )
        
        url = "https://facilities02.esc.rl.ac.uk:8181/ICATAdminService/ICATAdmin?wsdl"
        client = Client( url )
        client.options.username = "DLS-admin"
        client.options.password = "TaunWuOd5"

        self.sessionID = client.service.loginAdmin( "GUARDIAN" )
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATRegisterv10.refreshSessionID : New sessionID = " + str( self.sessionID ) )
        
    def ingestXMLBackup( self, xml ) :   
        
        print ''
        print '\n===========> simulating ingest...'
        print ''
        
    def ingestXML( self, xml ) :
        """
        Connect to the ICAT and ingest an XML string using the existing sessionID
        if the sessionID is invalid or has expired get a new one using refreshSessionID()
        """ 
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATRegisterv10.ingestXML..." )
        icat = Client( "https://facilities02.esc.rl.ac.uk:8181/ICATService/ICAT?wsdl" )
                        
        try:
           icat.service.ingestMetadata( self.sessionID, xml )
        except Exception as e:
           
           EDVerbose.DEBUG( 'An error occurred: %s\n' % e.message )
           
           # record the error and the info about the file being ingested, i.e. visit_id,  
           #self.recordFailedIngest( self.sessionID, xml, e.message )
           
           if e.message.lower().find( 'session' ) == -1:
               print 'Not a sessionId issue!'
               #return
               raise e
           
           self.refreshSessionID()
           try:
              
               icat.service.ingestMetadata( self.sessionID, xml )
             
           except Exception as ee:
               EDVerbose.DEBUG( 'An error occurred: %s\n' % ee.message )
               raise ee
    
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
            
    def saveSuccessICAT( self, filepath ):
        # should be fetched from xml input file
        icatProcessedFile = self.getDataInput().getIcatProcessedFiles().getPath().getValue()#'/dls/bl-misc/dropfiles2/icat/stats/icat-success'
        
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
        fileHandle = open ( icatProcessedFile , 'a' )
        fileHandle.writelines( str( filepath ) + '\t' + str( today ) + 'T' + str( now ) + '\t' + str( statInstrument ) + '\t' + str( statVisitID ) + '\t' + str( datasetname ) + '\n' )     
        fileHandle.close() 
            
    def saveFailedICAT( self, filepath ):
        # should be fetched from xml input file
        icatFailedFile = '/dls/bl-misc/dropfiles2/icat/stats/icat-failed'
        failedFolder = 'dls/bl-misc/dropfiles2/icat/stats/failed/'
        #icatFailedFile = self.getDataInput().getIcatFailedFiles().getPath().getValue()#'/dls/bl-misc/dropfiles2/icat/stats/icat-failed'
        #failedFolder = self.getDataInput().getIcatFailedFolder().getPath().getValue()#'/dls/bl-misc/dropfiles2/icat/stats/failed/'
        
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
        fileHandle = open ( icatFailedFile , 'a' )
        fileHandle.writelines( str( filepath ) + '\t' + str( today ) + 'T' + str( now ) + '\t' + str( statInstrument ) + '\t' + str( statVisitID ) + '\t' + str( datasetname ) + '\n' )     
        fileHandle.close()          


    #def recordFailedIngest( self, sessionID, xml, e ):
        #"""
        #this method record in a file information about the failing to ingest
        #as well as the error information
        #"""
        #failedIngestFile = '' # should be fetched from xml input file
        
        #now = time.strftime( "%H:%M:%S", time.localtime() )
        #today = datetime.date.today()
        
        #line = str( today ) + 'T' + str( now ) + '\t' + str( sessionID ) + '\t' + str( visit_id ) + '\t' + str( filename ) + '\t' + str( e )        
        

    def sortFiles( self, root, extension ):
          """
          sort files in a file list by order of modification date (oldest first) ignoring 0 size files
          """
          date_file_list = []
          files = []
          for folder in glob.glob( root ):
              #print "folder =", folder
              
              # sort only files with the given extension. '*' for all files
              for file in glob.glob( folder + '/*.' + extension ):
                  
                  # retrieves the stats for the current file as a tuple
                  # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
                  # the tuple element mtime at index 8 is the last-modified-date
                  stats = os.stat( file )
                  # create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
                  # weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
                  # note:  this tuple can be sorted properly by date and time
                  lastmod_date = time.localtime( stats[8] )
                  # create list of tuples ready for sorting by date
                  date_file_tuple = lastmod_date, file
                  
                  # do not include zero size files
                  fileSize = stats [stat.ST_SIZE]
                  if fileSize > 0:
                      date_file_list.append( date_file_tuple )
                  
          date_file_list.sort() #oldest modification date first
          #date_file_list.reverse()  # newest mod date now first

          #print "%-40s %s" % ( "filename:", "last modified:" )
          for file in date_file_list:
              #
              # extract just the filename
              #
              folder, file_name = os.path.split( file[1] )
              #
              # convert date tuple to MM/DD/YYYY HH:MM:SS format
              #
              #file_date = time.strftime( "%m/%d/%y %H:%M:%S", file[0] )
              files.append( file_name )

          return files
                
    
    def splitBigFiles( self, filepath, bulkSize ):
        """
        Splits a xml file into smaller files with <= 'bulksize'  number of datafile elements each 
        """
        try:
            fileTree = minidom.parse( filepath )
        
            # get the number of actual datafile elements in the .concat file
            datafilesList = fileTree.getElementsByTagName( "datafile" )
            nbDatafiles = len( datafilesList )
            
            #print str( nbDatafiles ) + ' datafile elements in : ' + filepath
            #print str( bulkSize ) + ' bulksize'
                   
            if ( int( nbDatafiles ) <= int ( bulkSize ) ):
                
                print '\nNumber of datafile elements in ' + filepath + ' is less than bulksize: ' + str( bulkSize ) + ', no split possible.'
                
            else:
                try:
                    # 
                    #split the big drop file into smaller files with number of datafile elements =< bulkSize
                    #
                    print '\nsplitting ==> ' + filepath
                    # counting the number smaller files needed
                    # check the use of divmod( nbDatafiles , bulkSize )
                    #print '\nsplitBigFiles -- nbDatafiles= ' + str( nbDatafiles )
                    #print '\nsplitBigFiles -- bulkSize= ' + str( bulkSize )
                    
                    ( quotient, remainder ) = divmod( int( nbDatafiles ) , int( bulkSize ) )
                    
                    if( remainder == 0 ):
                        nbFiles = quotient
                    else:
                        nbFiles = quotient + 1 
                    
                    #print '\nsplitting ' + filepath + ' into ' + str( nbFiles ) + ' files.'
                    #print '\n'
                    
                    #print 'nbFiles= ' + str( nbFiles )       
                    
                    # constructing the individual files
                    for i in range( 0, int( nbFiles ) ):
                        #print '\nProcessing file  ' + str( i ) + ' ...'
                        #create the small file
                                       
                        dropDirOrArchiveFile = filepath
                        if ( os.path.isfile( dropDirOrArchiveFile ) ):
                            #print 'dropDirOrArchiveFile: ' + dropDirOrArchiveFile
                            #print 'local filepath: ' + filepath
                            #filename = filepath.replace( dropDirOrArchiveFile, '' )
                            #print 'local filename: ' + filename 
                            
                            # remove .concat extension before renaming the file
                            
                            # remove '.concat' extension
                            dropDirOrArchiveFile = dropDirOrArchiveFile.replace( '.icat', '' )
                            
                            # rename the file into *.srb
                            newFilename = dropDirOrArchiveFile + '-' + str( 0 ) + str( i ) + '-split' + '.icat'
                            #print 'newFilename= ' + newFilename
                            filenamePath = newFilename
                            #print 'filenamePath= ' + str( filenamePath )
                            
                            
                        f = open( filenamePath , 'w' )
                                    
                        #print '\nPopulating the dataset...'
                        #
                        # read/get the dataset header first
                        #
                        
                        # load the xml into a tree. This load is not redundant as for some obscure reason the fileList 
                        # is loosing one of its datafile element during the process???           
                        fileTree = minidom.parse( filepath )
                        datafilesList = fileTree.getElementsByTagName( "datafile" )
                        
                        dataset = fileTree.getElementsByTagName( "dataset" )[0]
                        #print '--- dataset header ---'
                        #print dataset.toxml()
                        
                        # remove all datafiles childs so they can be replaced by the right ones
                        for j in range( 0, int( nbDatafiles ) ):
                            dataset.removeChild( datafilesList[j] )
                        
                        
                        ( q, r ) = divmod( int( nbDatafiles ), int( bulkSize ) )
                        # add only bulkSize number of datafile elements           
                        if ( i < nbFiles - 1 ):
                            for l in range( 0, int( bulkSize ) ):
                                #print 'i= ' + str( i ) + ' --- l= ' + str( l )
                                #print 'datafilesList[' + str( int( l ) + int( i ) * int( bulkSize ) ) + ']= ' + datafilesList[int( l ) + int( i ) * int( bulkSize )].toxml()  
                                dataset.appendChild( datafilesList[int( l ) + int( i ) * int( bulkSize )] )
                                
                                
                        else:#( i == ( nbFiles - 1 ) ):
                            for l in range( 0, r ):
                                #print 'i= ' + str( i ) + ' --- l= ' + str( l )
                                #print 'datafilesList[' + str( int( l ) ) + ']= ' + datafilesList[int( l ) + int( i ) * int( bulkSize )].toxml()
                                dataset.appendChild( datafilesList[int( l ) + int( i ) * int( bulkSize )] ) 
                         
                                
                        #print dataset.toxml()
                        # 
                        # write into the small file the corresponding datafile elements
                        # 
                        nb = len( fileTree.getElementsByTagName( 'datafile' ) )
                        #print filenamePath + ' contains ' + str( nb ) + ' nbDatafiles' 
                        fileTree.writexml( f )
                        f.close()
                
                except Exception:
                    #
                    #os.rename( filepath, filepath + '.nosplit' )
                    shutil.move( filepath, filepath + '.nosplit' )
                    #print 'reporting error in ' + str( errorFile )
                    pass
        
        
        
        except Exception:
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginExecICATIngesterv10.splitBigFiles  Failed to parse file '%s' renaming it." % filepath )
            #os.rename( filepath, filepath + '.invalid' )
            shutil.move( filepath, filepath + '.invalid' )
            
            # move the .invalid file into the invalid subdir
            # extract full filename                       
            newfileName = filepath + '.invalid'
            pathSplit = os.path.split( newfileName )
                        
            newFolder = os.path.join( pathSplit[0], 'invalid' ) # folder name should be extracted from input xml file
            individualFile = pathSplit[1]

            print '\nrenaming ' + str( newfileName ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
            #os.rename( newfileName, os.path.join( newFolder, individualFile ) )       
            shutil.move( newfileName, os.path.join( newFolder, individualFile ) ) 
        
            
    def openXMLTree( self, edFileName ):
        """
        Opens the xml file and places the tree in the object
        """
        # get the filename to load        
        try:
            edTree = minidom.parse( edFileName )
        except Exception:
            # is performed by the archiver already
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginControlDLSArchiverv10.openXMLTree  Failed to parse file '%s' renaming it." % edFileName )
            #os.rename( edFileName, edFileName + '.invalid' )
            shutil.move( edFileName, edFileName + '.invalid' )
            
        return edTree                
        
    def keepFileCopy(self, fullname, targetsubdir, destsubdir):
        # keep a copy of file to be processed by CleanAll(), SRBRegister(), ICATIngets(),...
        
        fullname = fullname.encode('ascii','ignore')
        
        nameList = fullname.split('/')
        name = nameList[-1]
        #print '\nname = '+str(name)
        dest = os.path.join(destsubdir, name)

        print '\n' + strftime("%Y-%m-%d %H:%M:%S") + ' *** EDPluginExecICATIngesterv10...keepFileCopy() ', fullname, ' to ', os.path.join( targetsubdir,dest) 
        shutil.copy2(fullname, os.path.join( targetsubdir,dest)) 
    
    
