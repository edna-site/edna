#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    Contributors:      Olof Svensson (svensson@esrf.fr) 


__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"


from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

import XSDataCommon

class EDHandlerXSDataCommon:


    @staticmethod
    def removeElements(_xsDataString,key):
        '''
        XSDataString key-value modification
        Eg: if key='Omega' and value='xxx'
            ...[separator]Omega=xxx[separator]...
        
        All such key elements will be removed form the string and new key-pairs will be added foreach element in th elist of newValues
        _xsDataString: the string in which we search for the key-pairs to be removed
        key: the string element that is used to identify the key-pairs
        
        result:
        a new XSDataString which does NOT contain the given key-pair elements
        '''
        if (_xsDataString is None):
            return None
        val=""
        optstr=_xsDataString.getValue()
        opts=optstr.split()
        for str in opts:
            opt=str.split(key)
            if (opt.__len__()==1):
                new=opt[0]
                if (val.__len__()==0):
                    val=new
                else:
                    val=' '.join([val,new])
        if (val.__len__()==0):
            return None
        retVal=XSDataCommon.XSDataString()
        retVal.setValue(val)            
        return retVal

    @staticmethod
    def getElements(_xsDataString,key):
        '''
        XSDataString key-value modification
        Eg: if key='Omega' and value='xxx'
            ...[separator]Omega=xxx[separator]...
        
        All such key elements will be removed form the string and new key-pairs will be added foreach element in th elist of newValues
        _xsDataString: the string in which we search for the key-pairs
        key: the string element that is used to identify the key-pairs
        
        result:
        a new XSDataString with only the requested key-pair elements
        '''
        if (_xsDataString is None):
            return None
        val=""
        optstr=_xsDataString.getValue()
        opts=optstr.split()
        for str in opts:
            opt=str.split(key)
            if (opt.__len__()>1):
                new=opt[1]
                if (val.__len__()==0):
                    val=new
                else:
                    val=' '.join([val,new])
        if (val.__len__()==0):
            return None
        retVal=XSDataCommon.XSDataString()
        retVal.setValue(val)            
        return retVal

    @staticmethod
    def replaceElements(_xsDataString,key,newValues):
        '''
        XSDataString key-value modification
        Eg: if key='Omega' and value='xxx'
            ...[separator]Omega=xxx[separator]...
        
        All such key elements will be removed form the string and new key-pairs will be added foreach element in th elist of newValues
        _xsDataString: the string in which we replace any keywords with the new values
        key: the string element that is used to identify the values
        newValues: the list of new values those will appear in the string under the settings of the key
        
        result:
        a new XSDataString with the new settings
        '''
        try:
            try:
                retVal=[EDHandlerXSDataCommon.removeElements(_xsDataString,key).getValue()]
            except:
                retVal=['']            
            val=(' '+key).join(retVal+newValues.split())
            retVal=XSDataCommon.XSDataString()
            retVal.setValue(val)
        except:
            retVal=_xsDataString            
        return retVal
        

    def __init__(self):
        a=6
        
        
