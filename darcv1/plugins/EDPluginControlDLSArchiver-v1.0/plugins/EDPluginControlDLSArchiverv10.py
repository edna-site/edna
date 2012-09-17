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
#    with changes by Ghita Kouadri Mostefaoui
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
from EDImportLib import EDActionCluster

from EDPluginControl import EDPluginControl
from EDConfiguration import EDConfiguration
from EDMessage       import EDMessage

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataControlDLSArchiverv10 import XSDataInputPluginControlDLSArchiver
from XSDataControlDLSArchiverv10 import XSDataResultPluginControlDLSArchiver

from xml.dom import minidom
import os, glob, datetime, time, stat, shutil
from time import strftime




class EDPluginControlDLSArchiverv10( EDPluginControl ):
    """
    DLS Archiver plugin
    """  
    
    def __init__( self ):
        """
        Initialise the plugin, mainly set the input class type
        """
        EDPluginControl.__init__( self )
        self.setXSDataInputClass( XSDataInputPluginControlDLSArchiver )

        self.numberOfFiles = 0  
        #self.nonExistantFiles = self.getDataInput().getNonExistantFiles().getPath().getValue()#'/dls/bl-misc/dropfiles2/icat/stats/nonexistantFiles'
                                                                        
    def configure( self ):
        """
        configure the plugin, mainly boiler plate code in here, to make sure the underlying code is being run
        """
        EDPluginControl.configure( self )
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.configure" )
        xsPluginItem = self.getConfiguration()
        if ( xsPluginItem == None ):
            EDVerbose.warning( "EDPluginControlDLSArchiverv10.configure: No DLS Archiver plugin item defined." )
            xsPluginItem = XSPluginItem()


    def preProcess( self, _edObject=None ):
        """
        This is for before the process occurs, in this case just calling the super method really, but you could add additional methods in here
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.preProcess..." )
        EDPluginControl.preProcess( self )
                 
            
    def process( self, _oalObject=None ):
        """
        This is the guts of the plugin, where all the hard work is done, in this case the plugin is a server, and is therefore repeating this process forever
        """        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.process..." )
        EDPluginControl.process( self )
        # Actually run the plugin
               
        
        #Set up the main loop to run continuously
        self.serverActive = True
        edRound = 0
        edSleeptime = self.getDataInput().getPollTime().getValue()
        
        while self.serverActive :
                        
            start = datetime.datetime.now()
                       
            self.checkDelayedFiles()
            time1 = datetime.datetime.now()
            
            self.cleanAllFiles()
            time2 = datetime.datetime.now()
            
                      
            self.processAllSRBFiles()
            time3 = datetime.datetime.now()
            
            self.processAllICATFiles()
            end = datetime.datetime.now()
            
            
            #print '=================  archiving report  ================='
            #print 'Round: ' + str( edRound )
            #print 'Total number of drop files:           ' + str( self.numberOfFiles )
            #print 'Total archiving time:                 ' + str( end - start )
            #print 'checkDelayedFiles() execution time:    ' + str( time1 - start )
            #print 'cleanAllFiles() execution time:    ' + str( time2 - time1 )
            #print 'processAllSRBFiles() execution time:  ' + str( time3 - time2 )
            #print 'processAllICATFiles() execution time: ' + str( end - time3 )
            ##print 'darc running since: ' + str( start )
            #print '======================================================'
            
            edRound += 1
            
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.Sleeping" )
            
            if( edSleeptime > 0 ):
                time.sleep( edSleeptime )
            else :
                self.serverActive = False
     

    def postProcess( self, _edObject=None ):
        """
        This method calls some super methods, and then returns the output data, in this case thats a blank object, as the plugin has no return.
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.postProcess..." )  
        # This is to make the tests pass, and it is during the postprocess step where the data is returned from the plugin. 
        xsDataResultPluginControlDLSArchiver = XSDataResultPluginControlDLSArchiver()
        self.setDataOutput( xsDataResultPluginControlDLSArchiver ) 
              

    def generateExecutiveSummary( self, _oedPlugin ):
        """
        This should probably have some extra information in here about the number of calls etc, which were made, however, as this is a server plugin, i dont think this will ever get called properly
        """
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.generateExecutiveSummary" )

    def processAllSRBFiles( self ):
        """
        This method is to run through all the .xml.clean files which need to be registered with the SRB
        """
        
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + " *** EDPluginControlDLSArchiverv10.processAllSRBFiles() : processing all '.xml.clean' files if any." ) 
        
        searchDir = self.getDataInput().getDropZonePath().getPath().getValue()
        fileList = []
        
        # process files by order of modification date (oldest first)        
        allfileList = self.sortFiles( searchDir , 'clean' ) #self.sortFiles( searchDir , 'xml' ) 
        
        # process only 100 files per round
        nbProcessableFiles = 100
        if len(allfileList) >= nbProcessableFiles:
            fileList = allfileList[0:nbProcessableFiles]
        else:
            fileList.extend(allfileList) 
             
        
        for name in fileList :      
            
            # get the full pathname of the xml file
            fullname = os.path.join( self.getDataInput().getDropZonePath().getPath().getValue(), name )               
            #edExtension = fullname.split( '.' )[-1]
            
            # # #
            # keep a copy of clean files before being registered with srb
            # # #
            #self.keepFileCopy(fullname, searchDir, 'srbinput')                                
            # # # 
            
            # get the size of the current file
            edFileStats = os.stat( fullname )
            edFileSize = edFileStats [stat.ST_SIZE]
            
            # now call the SRB register on the xml file
            if ( edFileSize > 0 ) :# ignore zero size files
                
                                                
                print ''            
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10 '%s' is being registered with the SRB" % fullname ) 
                print ''
                
                edSRBPlugin = self.loadPlugin( 'EDPluginExecSRBRegisterv10' )
                                
                from XSDataExecSRBRegisterv10 import XSDataInputPluginExecSRBRegister
                from XSDataExecSRBRegisterv10 import XSDataResultPluginExecSRBRegister
                
                # build the plugin input
                xsDataPluginExecSRBRegister = XSDataInputPluginExecSRBRegister()
                
                # create the dropfile name
                edDropfileName = XSDataFile( XSDataString( os.path.join( self.getDataInput().getSrbDropFilePath().getPath().getValue(), '%s.drop' % name ) ) )
                # edDropfileName = XSDataFile(XSDataString(self.getDataInput().getSrbDropFilePath().getPath().getValue() + name + '.drop'))
                
                xsDataPluginExecSRBRegister.setSrbDropFileName( edDropfileName )
                
                #xsDataPluginExecSRBRegister.setSrbURIPattern( self.getDataInput().getSrbURIPattern() )
                
                #xsDataPluginExecSRBRegister.setSrbURIReplacement( self.getDataInput().getSrbURIReplacement() )
                                
                xsDataPluginExecSRBRegister.setXmlIngestFileName( XSDataFile( XSDataString( fullname ) ) ) 
                
                xsDataPluginExecSRBRegister.setIgnoreList( self.getDataInput().getIgnoreList() )
                
                xsDataPluginExecSRBRegister.setIgnoreSubdirList( self.getDataInput().getIgnoreSubdirList() )
                                                                                     
                
                edSRBPlugin.setDataInput( xsDataPluginExecSRBRegister )
                
                # now run the plugin
                edSRBPlugin.connectSUCCESS( self.doSuccessSRB )
                edSRBPlugin.connectFAILURE( self.doFailureSRB )
                edSRBPlugin.executeSynchronous()
            
            else: # rename zero files so they are not processed a second time
                # this is currently already done before this step
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10 '%s' is a zero file. Renamed and ignored. " % fullname )
                #os.rename( fullname, fullname + ".zero" )
                shutil.move( fullname, fullname + ".zero" )
                

    def doSuccessSRB( self, _edPlugin=None ):
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.doSuccessSRB" )


    def doFailureSRB( self, _edPlugin=None ):
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.doFailureSRB" )


    def processAllICATFiles( self ):
        """
        This method should process all the ICAT files and then return
        """

        # Now check the directory given to see if there are any xml ingest files in there            
        print ''
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.processAllICATFiles : processing all 'icat' files if any." ) 
        print ''
                
        edICATPlugin = self.loadPlugin( 'EDPluginExecICATIngesterv10' )
               
        from XSDataExecICATIngesterv10 import XSDataInputPluginExecICATIngester
        from XSDataExecICATIngesterv10 import XSDataResultPluginExecICATIngester
                
        # build the plugin input
        xsDataPluginExecICATIngester = XSDataInputPluginExecICATIngester()                
               
        xsDataPluginExecICATIngester.setXmlArchiveDirectory( self.getDataInput().getArchiveLocation() )
                
        xsDataPluginExecICATIngester.setXmlSearchDir( self.getDataInput().getDropZonePath() )  
        #xsDataPluginExecICATIngester.setXmlFailedtoIngestDirectory( self.getDataInput().getFailedtoIngestDirectory().getPath().getValue() )    
        #xsDataPluginExecICATIngester.setXmlIngestFileName( XSDataFile( XSDataString( fullname ) ) ) 
                
        edICATPlugin.setDataInput( xsDataPluginExecICATIngester )
                
        # now run the plugin
        edICATPlugin.connectSUCCESS( self.doSuccessICAT )
        edICATPlugin.connectFAILURE( self.doFailureICAT )
        edICATPlugin.executeSynchronous()
 
        # retrieve the plugin result
        xsDataResultPluginExecICATIngester = edICATPlugin.getDataOutput()
        
        #xsDataResultPluginExecICATIngester.getSessionID().getValue()
                               
        return
    

    def doSuccessICAT( self, _edPlugin=None ):
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.doSuccessICAT" )


    def doFailureICAT( self, _edPlugin=None ):
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.doFailureICAT" )
    
    def checkDelayedFiles( self ):
        
        searchDir = self.getDataInput().getDropZonePath().getPath().getValue()
        roundDelay = self.getDataInput().getNbRoundsDelay().getValue()
        #print ''
        #print '\n delay fetched= ' + str( roundDelay )
        #print ''
        
        for filepath in glob.glob( searchDir + '/*.delayed' ):
            
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.checkDelayedFiles...processing file " + str( filepath ) )
                        
            delayedTree = minidom.parse( filepath )
            counter = 0
            
            for edElement in delayedTree.getElementsByTagName( "datafile" ) :
                
                edInternalFileName = edElement.getElementsByTagName( "location" )[0].childNodes[0].nodeValue
                
                # check if file exists
                if ( os.system( "ls " + edInternalFileName ) != 0 ): # file does not exist yet
                    
                    EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.cleanAllFiles  Failed to find file %s " % edInternalFileName )
                    #self.edTree.getElementsByTagName( "dataset" )[0].removeChild( edElement )
                    
                    # cleaning missing data file locations e.g. '/dls/b16/data/2010/sm89-89/154.dat'
                    splitfilepath = filepath.split( '/' )
                    dropfilename = splitfilepath[-1]
                    storeFolder = filepath.replace( dropfilename, '' )
                    EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.cleanAllFiles   Dropfilename %s " % str( dropfilename ) )
                    #print '\nstoreFolder= ' + str( storeFolder )
        
                    # file does not exist  
                    splitdropfilename = dropfilename.split( '-' )
                    round = int( splitdropfilename[0] )
                    #print '\nround: ' + str( round )
     
                    if round < roundDelay: 
                        newDropfilename = filepath.replace( str( round ) + '-delayed-', str( round + 1 ) + '-delayed-' )
                        #print '\nnewDropfilename= ' + str( newDropfilename )
                        #print '\nrenaming ' + str( filepath ) + ' to ' + str( newDropfilename ) 
                        shutil.copy2( filepath, newDropfilename )
                        os.remove( filepath )
                
                    else: # log the file by changing extension 
                        self.saveNonexistantFiles( edInternalFileName )
                        shutil.copy2( filepath , filepath + '.nonexistantdatafile' )
                        os.remove( filepath )
                        
                        # move the .nonexistantdatafile into the nonexistant subdir
                        # extract full filename
                        filename = filepath + '.nonexistantdatafile'
                        
                        pathSplit = os.path.split( filename )
                        
                        newFolder = os.path.join( pathSplit[0], 'nonexistant' ) # folder name should be extracted from input xml file
                        individualFile = pathSplit[1]

                        print '\nrenaming ' + str( filename ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
                        #os.rename( filename, os.path.join( newFolder, individualFile ) )                      
                        shutil.move( filename, os.path.join( newFolder, individualFile ) )    
                else:
                    # rename .delayed file to .xml file to be processed again
                    xmlfilename = filepath + '.xml'
                    shutil.copy2( filepath, xmlfilename )
                    os.remove( filepath )      
                
                counter = counter + 1
                #print '\n counter= ' + str( counter )
    
    def cleanAllFiles( self ):
        EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.cleanAllFiles..." )
        searchDir = self.getDataInput().getDropZonePath().getPath().getValue()
        allfileList = glob.glob( searchDir + '/*.xml' ) 
        self.numberOfFiles = len( allfileList )
        
        
        if self.numberOfFiles > 0 :
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.cleanAllFiles...found '%s' files." % str( self.numberOfFiles ) )
            
            fileList = []
                
            # process only 100 files per round
            nbProcessableFiles = 100
            if len(allfileList) >= nbProcessableFiles:
                fileList = allfileList[0:nbProcessableFiles]
            else:
                fileList.extend(allfileList) 
            
            for filepath in fileList:  #glob.glob( searchDir + '/*.xml' ):                
                EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.cleanAllFiles...processing '%s' " % str( filepath ) )
                                
                # # #
                # first, make a copy of xml files before being cleaned for record
                # # #
                self.keepFileCopy(filepath, searchDir, 'all')                                
                # # #  
                           
                edFileStats = os.stat( filepath )
                edFileSize = edFileStats [stat.ST_SIZE]
                
                if edFileSize > 0:
                                                
                    # check that the visitid in the header is the same as in every file location
                    # first load the tree
                    invalidFile = False
                    
                    try:
                        self.edTree = self.openXMLTree( filepath )
                        
                        headerVisitID = ( self.edTree.getElementsByTagName( "visit_id" )[0].childNodes[0].nodeValue )
                        headerInstrument = ( self.edTree.getElementsByTagName( "instrument" )[0].childNodes[0].nodeValue )
                        
                        counter = 0 # the order of the datafile element   
                        
                        # check if header consistent with data files info
                        for edElement in self.edTree.getElementsByTagName( "datafile" ) :
                            edInternalFileName = edElement.getElementsByTagName( "location" )[0].childNodes[0].nodeValue
                            list = edInternalFileName.split( '/' )                     
                        
                            
                            if len( list ) < 7:
                                invalidFile = True
                            else:
                                localInstrument = list[2]
                                localVisitID = list[5]
                                if ( ( localVisitID.lower() ).strip() != ( headerVisitID.lower() ).strip() or ( localInstrument.lower() ).strip() != ( headerInstrument.lower() ).strip() ):
                                    invalidFile = True
                                                                    
                        if invalidFile :                           
                                                    
                            filename = filepath.replace( '.xml', '.wrongContent' ) 
                            #os.rename( filepath, filename )
                            try:
                                shutil.move( filepath, filename)
                            except Exception as er:
                                print '\nerror is ='+str(er)
                                 
                            print '\nproblem with content of the file ' + filepath + ' : discarded from archiving process and renamed to ' + filename
                            
                            # move the .wrongContent file into the wrongContent subdir                                                      
                            pathSplit = os.path.split( filename )
                        
                            newFolder = os.path.join( pathSplit[0], 'wrongContent' ) # folder name should be extracted from input xml file
                            individualFile = pathSplit[1]
    
                            print '\nmoving ' + str( filename ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
                            #os.rename( filename, os.path.join( newFolder, individualFile ) )   
                            try:
                                shutil.move( filename, os.path.join( newFolder, individualFile ) ) 
                            except Exception as er:
                                print '\nerror is ='+str(er) 
                            
                        else:# xml file valid 
                            
                            # replace .xml extension with .clean for the valid file
                            shutil.move( filepath, filepath + '.clean') 
                            filepath = filepath + '.clean'
                            
                            # # #
                            # keep a copy of .clean files before being processed by SRBRegister
                            # # #
                            self.keepFileCopy(filepath, searchDir, 'clean')                                
                            # # #
                                                   
                            splitfilepath = filepath.split( '/' )
                            dropfilename = splitfilepath[-1]
                            storeFolder = filepath.replace( dropfilename, '' )
                            #print '\ndropfilename= ' + str( dropfilename )
                            #print '\nstoreFolder= ' + str( storeFolder )
                            
                            for edElement in self.edTree.getElementsByTagName( "datafile" ) : 
                                edInternalFileName = edElement.getElementsByTagName( "location" )[0].childNodes[0].nodeValue
                                #print '\nprocessing datafile file... ' + str( edInternalFileName )
                                #print '\ncounter= ' + str( counter )
                                                                      
                                # check if file exists
                                if ( os.system( "ls " + edInternalFileName ) != 0 ): # file does not exist yet
    
                                    # dealing with the drop file for the first time
                                                       
                                    # create a tmp file to hold new xml file minus missing location
                                    tmpfileName = os.path.join( storeFolder , dropfilename + '.temporary' )
                                    #print '\ntmpfile= ' + str( tmpfileName )
                                    
                                    # create a new file with the missing location
                                    delayedfileName = os.path.join( storeFolder , '0' + '-delayed-' + 'datafile-' + str( counter ) + '-' + dropfilename + '.delayed' ) # .delayed extension                                          
                                    #print '\ndelayedfileName= ' + str( delayedfileName ) 
                                    shutil.copyfile( filepath, delayedfileName ) 
                                                                                          
                                    # remove the non-existant file location from the original file
                                    self.edTree.getElementsByTagName( "dataset" )[0].removeChild( edElement )
                                    fmtp = open ( tmpfileName, 'a' ) 
                                                       
                                    
                                    self.edTree.writexml( fmtp )
                                    fmtp.close()
                                    
                                    # dealing with the delayed file
                                    delayedTree = minidom.parse( delayedfileName )
                                    
                                    delayeddatafilesList = delayedTree.getElementsByTagName( "datafile" )
                                    nbDatafiles = len( delayeddatafilesList )
                    
                                    delayedDataset = delayedTree.getElementsByTagName( "dataset" )[0]
                                               
                                    # remove all datafile childs so they can be replaced by the right ones
                                    for j in range( 0, int( nbDatafiles ) ):
                                        delayedDataset.removeChild( delayeddatafilesList[j] )
                    
                                    delayedDataset.appendChild( edElement ) 
                                    
                                    fdelayed = open( delayedfileName , "w" )
                                    #print '\n--- delayedfileTree going to delayed file ---'
                                    #print delayedTree.toxml()
                                    #print '\n--- delayedfileTree going to delayed file ---'
                                    delayedTree.writexml( fdelayed )
                                    fdelayed.close()
                                    #print '*********************'
                                    #print os.path.exists( filepath )
                                    os.remove( filepath )
                                    #print os.path.exists( filepath )
                                    #print '*********************'
                                    print '\nmoving ' + str( tmpfileName ) + ' to ' + str( filepath )
                                    shutil.move( tmpfileName, filepath )  
                                       
                                    counter = counter + 1 
                                       
                                    ############
                        
                    except Exception as er:
                        print '\ninvalid xml file, moved to invalid dir: '+ str(filepath)
                        
                    
                    
                else: # zero file
                    newfileName = filepath.replace( '.xml', '.zero' ) 
                    #os.rename( filepath, newfileName )
                    shutil.move( filepath, newfileName )
                    print '\n*** EDPluginControlDLSArchiverv10    file size = ' + str( edFileSize ) + ' detected as equal to 0.'
                    print '\n*** EDPluginControlDLSArchiverv10    file size = 0 ' + filepath + ' : discarded from archiving process and renamed to ' + newfileName
                    
                    # move the .nonexistantdatafile into the nonexistant subdir
                    # extract full filename                       
                    pathSplit = os.path.split( newfileName )
                        
                    newFolder = os.path.join( pathSplit[0], 'zero' ) # folder name should be extracted from input xml file
                    individualFile = pathSplit[1]

                    print '\nrenaming ' + str( newfileName ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
                    #os.rename( newfileName, os.path.join( newFolder, individualFile ) )
                    shutil.move( newfileName, os.path.join( newFolder, individualFile ) )       
        else:
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10 no file found to clean." )
       
        
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
                  #if fileSize > 0:
                      #date_file_list.append( date_file_tuple )
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
      
    
#    def concatenateDropfiles( self, filepath, dropDir ):
#        """
#        Concat smaller drop files into one single big file
#        """
#        print '\nconcatenating ==> ' + filepath
#         
#        # open the file in read mode
#        fileHandle = open( filepath, "r" )
#        
#        # load the xml into a tree
#        fileTree = minidom.parse( filepath )
#                    
#        dataset_name = fileTree.getElementsByTagName( "name" )[0].childNodes[0].nodeValue
#        beamline = fileTree.getElementsByTagName( "instrument" )[0].childNodes[0].nodeValue
#        
#        date = fileTree.getElementsByTagName( "datafile_create_time" )[0].childNodes[0].nodeValue
#        stripped_date = str( date ).strip()
#        year = stripped_date[0:4]  
#        visit_id = fileTree.getElementsByTagName( "visit_id" )[0].childNodes[0].nodeValue
#         
#        datafile = fileTree.getElementsByTagName( "datafile" )[0].childNodes[0].nodeValue
#        
#        # close the individual drop file
#        fileHandle.close()
#        
#        # dealing with dataset-names that contain '/' or '\'
#        dataset_name = dataset_name.replace( '/', '-' )
#        dataset_name = dataset_name.replace( '\\', '' )
#        dataset_name = dataset_name.replace( ',', '' )
#        dataset_name = dataset_name.replace( '`', '' )
#        #print dataset_name
#        
#        big_file_name = str( year ) + "-" + str( beamline ) + "-" + str( visit_id ) + "-" + str( dataset_name ) + '.concat'
#        #print ''
#        #print '1- big_file_name= ' + str( big_file_name )
#        # remove spaces in file name
#        big_file_name = big_file_name.split()
#        #print '2- big_file_name= ' + str( big_file_name )
#        big_file_name = ''.join( big_file_name )
#        #print '3- big_file_name= ' + str( big_file_name ) 
#        #print ''  
#        # check if the file exists       
#        bigfilepath = os.path.join( dropDir, big_file_name )#dropDir + '/' + big_file_name
#        
#        #print 'dropDir= ' + str( dropDir )
#        print 'big_file_name= ' + str( big_file_name )
#        #print 'bigfilepath= ' + str( bigfilepath )
#        
#        if( os.path.isfile( bigfilepath ) ):
#            #print 'file exists: ' + str( bigfilepath )
#            
#            # open the file 
#            f = open( bigfilepath, "r" )
#        
#            # load the xml into a tree
#            #print '\nparsing ' + str( bigfilepath )
#            bigfileTree = minidom.parse( bigfilepath )
#                    
#            big_dataset = bigfileTree.getElementsByTagName( "dataset" )[0]
#            
#            # adding all datafile elements to the big file dataset
#            for node in fileTree.getElementsByTagName( "datafile" ):
#                big_dataset.appendChild( node )
#            
#            # write to a tmp file
#            tmppath = bigfilepath + '.tmp'
#            ftmp = open( tmppath , "w" )
#            bigfileTree.writexml( ftmp )
#            ftmp.close()
#            
#            # copy tmp file into the big drop file
#            #print 'tmppath = ' + tmppath
#            #print 'bigfilepath = ' + bigfilepath
#            os.system ( "cp %s %s" % ( tmppath, bigfilepath ) )
#            # remove tmp file
#            os.remove( tmppath )          
#            # close big drop file
#            f.close()
#            
#            # move the individual drop file into the concatenatedDir
#            #os.system ( "cp %s %s" % ( filepath, ) )
#            
#        else:
#            try:
#                # creating the big file
#                print '\nfile does not exist. Creating it: ' + bigfilepath
#                            
#                # create the file and open it for writing
#                f = open( bigfilepath, "w" )
#                
#                os.system ( "cp %s %s" % ( filepath, bigfilepath ) )
#                
#                f.close()
#                
#                #print '\nfile created    : ' + bigfilepath
#    
#            except Exception:
#                print "\nCannot create " + bigfilepath + ': ', sys.exc_info()[0]
#                raise
#        
#        # finished with .xml file delete it to avoid processing it again
#        os.remove( filepath )
#        #print 'number of files: ' + str( count )   
 
    def openXMLTree( self, edFileName ):
        """
        Opens the xml file and places the tree in the object
        """
        # get the filename to load        
        try:
            self.localedTree = minidom.parse( edFileName )
        except Exception:
            EDVerbose.DEBUG( strftime("%Y-%m-%d %H:%M:%S") + "  *** EDPluginControlDLSArchiverv10.openXMLTree  Failed to parse file '%s' renaming it." % edFileName )
            
            edNewName = edFileName + ".invalid"
            #os.rename( edFileName, edNewName )
            shutil.move( edFileName, edNewName )
            
            pathSplit = os.path.split( edNewName )
                        
            newFolder = os.path.join( pathSplit[0], 'invalid' ) # folder name should be extracted from input xml file
            individualFile = pathSplit[1]

            print '\nmoving ' + str( edNewName ) + ' into ' + str( os.path.join( newFolder, individualFile ) )
            #os.rename( edNewName, os.path.join( newFolder, individualFile ) )
            shutil.move( edNewName, os.path.join( newFolder, individualFile ) )
                    
            #os.rename( edFileName, edFileName + '.invalid' )

        return self.localedTree  

    def saveNonexistantFiles( self, filepath ):
                
        nonExistantFiles = self.getDataInput().getNonExistantFiles().getPath().getValue()
        
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
        fileHandle = open ( nonExistantFiles  , 'a' )
        fileHandle.writelines( str( filepath ) + '\t' + str( today ) + 'T' + str( now ) + '\t' + str( statInstrument ) + '\t' + str( statVisitID ) + '\t' + str( datasetname ) + '\n' )     
        fileHandle.close() 
    
    def keepFileCopy(self, fullname, targetsubdir, destsubdir):
        # keep a copy of file to be processed by CleanAll(), SRBRegister(), ICATIngets(),...
        
        fullname = fullname.encode('ascii','ignore')
        
        nameList = fullname.split('/')
        name = nameList[-1]
        #print '\nname = '+str(name)
        dest = os.path.join(destsubdir, name)

        print '\n' + strftime("%Y-%m-%d %H:%M:%S") + ' *** EDPluginControlDLSArchiverv10...keepFileCopy() ', fullname, ' to ', os.path.join( targetsubdir,dest) 
        shutil.copy2(fullname, os.path.join( targetsubdir,dest))                             
       