#!/usr/bin/env python

#
# Generated Mon Dec 3 11:21::01 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataMXv1": "mxv1/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataRotation
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataVectorDouble
    from XSDataCommon import XSDataDate
    from XSDataCommon import XSDataUnitVector
    from XSDataMXv1 import XSDataInputCharacterisation
    from XSDataMXv1 import XSDataResultStrategy
    from XSDataMXv1 import XSDataResultCharacterisation
    from XSDataCommon import XSDataDisplacement
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
    from XSDataCommon import XSDataWavelength
    from XSDataCommon import XSDataAngle
except ImportError as error:
    if strEdnaHome is not None:
        for strXsdName in dictLocation:
            strXsdModule = strXsdName + ".py"
            strRootdir = os.path.dirname(os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName])))
            for strRoot, listDirs, listFiles in os.walk(strRootdir):
                if strXsdModule in listFiles:
                    sys.path.append(strRoot)
    else:
        raise error
from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataRotation
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataDate
from XSDataCommon import XSDataUnitVector
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataCommon import XSDataDisplacement
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataAngle




#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith('3'):
    unicode = str
    from io import StringIO
else:
    from StringIO import StringIO


def showIndent(outfile, level):
    for idx in range(level):
        outfile.write(unicode('    '))


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    #if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
    #    print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer(object):
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:     # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write(unicode('<%s>%s</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write(unicode('<%s>%d</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write(unicode('<%s>%f</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write(unicode('<%s>%g</%s>' % (self.name, self.value, self.name)))

#
# Data representation classes.
#



class possible_orientation(object):
    def __init__(self, rank=None, trans=None, phi=None, kappa=None, omega=None, v2=None, v1=None):
        self._v1 = str(v1)
        self._v2 = str(v2)
        if omega is None:
            self._omega = None
        else:
            self._omega = float(omega)
        if kappa is None:
            self._kappa = None
        else:
            self._kappa = float(kappa)
        if phi is None:
            self._phi = None
        else:
            self._phi = float(phi)
        self._trans = str(trans)
        if rank is None:
            self._rank = None
        else:
            self._rank = float(rank)
    # Methods and properties for the 'v1' attribute
    def getV1(self): return self._v1
    def setV1(self, v1):
        self._v1 = str(v1)
    def delV1(self): self._v1 = None
    v1 = property(getV1, setV1, delV1, "Property for v1")
    # Methods and properties for the 'v2' attribute
    def getV2(self): return self._v2
    def setV2(self, v2):
        self._v2 = str(v2)
    def delV2(self): self._v2 = None
    v2 = property(getV2, setV2, delV2, "Property for v2")
    # Methods and properties for the 'omega' attribute
    def getOmega(self): return self._omega
    def setOmega(self, omega):
        if omega is None:
            self._omega = None
        else:
            self._omega = float(omega)
    def delOmega(self): self._omega = None
    omega = property(getOmega, setOmega, delOmega, "Property for omega")
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        else:
            self._kappa = float(kappa)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        else:
            self._phi = float(phi)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    # Methods and properties for the 'trans' attribute
    def getTrans(self): return self._trans
    def setTrans(self, trans):
        self._trans = str(trans)
    def delTrans(self): self._trans = None
    trans = property(getTrans, setTrans, delTrans, "Property for trans")
    # Methods and properties for the 'rank' attribute
    def getRank(self): return self._rank
    def setRank(self, rank):
        if rank is None:
            self._rank = None
        else:
            self._rank = float(rank)
    def delRank(self): self._rank = None
    rank = property(getRank, setRank, delRank, "Property for rank")
    def export(self, outfile, level, name_='possible_orientation'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='possible_orientation'):
        pass
        if self._v1 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<v1>%s</v1>\n' % self._v1))
        else:
            warnEmptyAttribute("v1", "string")
        if self._v2 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<v2>%s</v2>\n' % self._v2))
        else:
            warnEmptyAttribute("v2", "string")
        if self._omega is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<omega>%e</omega>\n' % self._omega))
        else:
            warnEmptyAttribute("omega", "double")
        if self._kappa is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<kappa>%e</kappa>\n' % self._kappa))
        else:
            warnEmptyAttribute("kappa", "double")
        if self._phi is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<phi>%e</phi>\n' % self._phi))
        else:
            warnEmptyAttribute("phi", "double")
        if self._trans is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<trans>%s</trans>\n' % self._trans))
        else:
            warnEmptyAttribute("trans", "string")
        if self._rank is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rank>%e</rank>\n' % self._rank))
        else:
            warnEmptyAttribute("rank", "double")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._v1 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._v2 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omega':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._omega = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._kappa = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._phi = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trans':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._trans = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rank':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._rank = fval_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="possible_orientation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='possible_orientation' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class possible_orientation is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return possible_orientation.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = possible_orientation()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="possible_orientation" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = possible_orientation()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class possible_orientation


class status(object):
    def __init__(self, message=None, code=None):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "status_code":
            self._code = code
        else:
            strMessage = "ERROR! status constructor argument 'code' is not status_code but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
        self._message = str(message)
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "status_code":
            self._code = code
        else:
            strMessage = "ERROR! status.setCode argument is not status_code but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    # Methods and properties for the 'message' attribute
    def getMessage(self): return self._message
    def setMessage(self, message):
        self._message = str(message)
    def delMessage(self): self._message = None
    message = property(getMessage, setMessage, delMessage, "Property for message")
    def export(self, outfile, level, name_='status'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='status'):
        pass
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
        else:
            warnEmptyAttribute("code", "status_code")
        if self._message is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<message>%s</message>\n' % self._message))
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = status_code()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._message = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="status" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='status' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class status is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return status.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = status()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="status" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = status()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class status


class kappa_alignment_response(object):
    def __init__(self, possible_orientation=None, comment=None, status=None):
        if status is None:
            self._status = None
        elif status.__class__.__name__ == "status":
            self._status = status
        else:
            strMessage = "ERROR! kappa_alignment_response constructor argument 'status' is not status but %s" % self._status.__class__.__name__
            raise BaseException(strMessage)
        self._comment = str(comment)
        if possible_orientation is None:
            self._possible_orientation = []
        elif possible_orientation.__class__.__name__ == "list":
            self._possible_orientation = possible_orientation
        else:
            strMessage = "ERROR! kappa_alignment_response constructor argument 'possible_orientation' is not list but %s" % self._possible_orientation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'status' attribute
    def getStatus(self): return self._status
    def setStatus(self, status):
        if status is None:
            self._status = None
        elif status.__class__.__name__ == "status":
            self._status = status
        else:
            strMessage = "ERROR! kappa_alignment_response.setStatus argument is not status but %s" % status.__class__.__name__
            raise BaseException(strMessage)
    def delStatus(self): self._status = None
    status = property(getStatus, setStatus, delStatus, "Property for status")
    # Methods and properties for the 'comment' attribute
    def getComment(self): return self._comment
    def setComment(self, comment):
        self._comment = str(comment)
    def delComment(self): self._comment = None
    comment = property(getComment, setComment, delComment, "Property for comment")
    # Methods and properties for the 'possible_orientation' attribute
    def getPossible_orientation(self): return self._possible_orientation
    def setPossible_orientation(self, possible_orientation):
        if possible_orientation is None:
            self._possible_orientation = []
        elif possible_orientation.__class__.__name__ == "list":
            self._possible_orientation = possible_orientation
        else:
            strMessage = "ERROR! kappa_alignment_response.setPossible_orientation argument is not list but %s" % possible_orientation.__class__.__name__
            raise BaseException(strMessage)
    def delPossible_orientation(self): self._possible_orientation = None
    possible_orientation = property(getPossible_orientation, setPossible_orientation, delPossible_orientation, "Property for possible_orientation")
    def addPossible_orientation(self, value):
        if value is None:
            strMessage = "ERROR! kappa_alignment_response.addPossible_orientation argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "possible_orientation":
            self._possible_orientation.append(value)
        else:
            strMessage = "ERROR! kappa_alignment_response.addPossible_orientation argument is not possible_orientation but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPossible_orientation(self, index, value):
        if index is None:
            strMessage = "ERROR! kappa_alignment_response.insertPossible_orientation argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! kappa_alignment_response.insertPossible_orientation argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "possible_orientation":
            self._possible_orientation[index] = value
        else:
            strMessage = "ERROR! kappa_alignment_response.addPossible_orientation argument is not possible_orientation but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='kappa_alignment_response'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='kappa_alignment_response'):
        pass
        if self._status is not None:
            self.status.export(outfile, level, name_='status')
        else:
            warnEmptyAttribute("status", "status")
        if self._comment is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<comment>%s</comment>\n' % self._comment))
        else:
            warnEmptyAttribute("comment", "string")
        for possible_orientation_ in self.getPossible_orientation():
            possible_orientation_.export(outfile, level, name_='possible_orientation')
        if self.getPossible_orientation() == []:
            warnEmptyAttribute("possible_orientation", "possible_orientation")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'status':
            obj_ = status()
            obj_.build(child_)
            self.setStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._comment = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possible_orientation':
            obj_ = possible_orientation()
            obj_.build(child_)
            self.possible_orientation.append(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="kappa_alignment_response" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='kappa_alignment_response' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class kappa_alignment_response is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return kappa_alignment_response.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_response()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="kappa_alignment_response" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_response()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class kappa_alignment_response


class status_code(object):
    def __init__(self, code=None):
        self._code = str(code)
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        self._code = str(code)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='status_code'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='status_code'):
        pass
        if self._code is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<code>%s</code>\n' % self._code))
        else:
            warnEmptyAttribute("code", "string")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._code = value_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="status_code" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='status_code' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class status_code is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return status_code.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = status_code()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="status_code" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = status_code()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class status_code


class XSBeam(XSData):
    def __init__(self, direction=None, polarisatation=None):
        XSData.__init__(self, )
        if polarisatation is None:
            self._polarisatation = None
        elif polarisatation.__class__.__name__ == "XSDataUnitVector":
            self._polarisatation = polarisatation
        else:
            strMessage = "ERROR! XSBeam constructor argument 'polarisatation' is not XSDataUnitVector but %s" % self._polarisatation.__class__.__name__
            raise BaseException(strMessage)
        if direction is None:
            self._direction = None
        elif direction.__class__.__name__ == "XSDataUnitVector":
            self._direction = direction
        else:
            strMessage = "ERROR! XSBeam constructor argument 'direction' is not XSDataUnitVector but %s" % self._direction.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'polarisatation' attribute
    def getPolarisatation(self): return self._polarisatation
    def setPolarisatation(self, polarisatation):
        if polarisatation is None:
            self._polarisatation = None
        elif polarisatation.__class__.__name__ == "XSDataUnitVector":
            self._polarisatation = polarisatation
        else:
            strMessage = "ERROR! XSBeam.setPolarisatation argument is not XSDataUnitVector but %s" % polarisatation.__class__.__name__
            raise BaseException(strMessage)
    def delPolarisatation(self): self._polarisatation = None
    polarisatation = property(getPolarisatation, setPolarisatation, delPolarisatation, "Property for polarisatation")
    # Methods and properties for the 'direction' attribute
    def getDirection(self): return self._direction
    def setDirection(self, direction):
        if direction is None:
            self._direction = None
        elif direction.__class__.__name__ == "XSDataUnitVector":
            self._direction = direction
        else:
            strMessage = "ERROR! XSBeam.setDirection argument is not XSDataUnitVector but %s" % direction.__class__.__name__
            raise BaseException(strMessage)
    def delDirection(self): self._direction = None
    direction = property(getDirection, setDirection, delDirection, "Property for direction")
    def export(self, outfile, level, name_='XSBeam'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSBeam'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._polarisatation is not None:
            self.polarisatation.export(outfile, level, name_='polarisatation')
        else:
            warnEmptyAttribute("polarisatation", "XSDataUnitVector")
        if self._direction is not None:
            self.direction.export(outfile, level, name_='direction')
        else:
            warnEmptyAttribute("direction", "XSDataUnitVector")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'polarisatation':
            obj_ = XSDataUnitVector()
            obj_.build(child_)
            self.setPolarisatation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direction':
            obj_ = XSDataUnitVector()
            obj_.build(child_)
            self.setDirection(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSBeam" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSBeam' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSBeam is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSBeam.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSBeam()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSBeam" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSBeam()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSBeam


class XSBeamSetting(XSData):
    def __init__(self, XSBeam=None, wavelength=None):
        XSData.__init__(self, )
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSBeamSetting constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if XSBeam is None:
            self._XSBeam = None
        elif XSBeam.__class__.__name__ == "XSBeam":
            self._XSBeam = XSBeam
        else:
            strMessage = "ERROR! XSBeamSetting constructor argument 'XSBeam' is not XSBeam but %s" % self._XSBeam.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSBeamSetting.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'XSBeam' attribute
    def getXSBeam(self): return self._XSBeam
    def setXSBeam(self, XSBeam):
        if XSBeam is None:
            self._XSBeam = None
        elif XSBeam.__class__.__name__ == "XSBeam":
            self._XSBeam = XSBeam
        else:
            strMessage = "ERROR! XSBeamSetting.setXSBeam argument is not XSBeam but %s" % XSBeam.__class__.__name__
            raise BaseException(strMessage)
    def delXSBeam(self): self._XSBeam = None
    XSBeam = property(getXSBeam, setXSBeam, delXSBeam, "Property for XSBeam")
    def export(self, outfile, level, name_='XSBeamSetting'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSBeamSetting'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        else:
            warnEmptyAttribute("wavelength", "XSDataWavelength")
        if self._XSBeam is not None:
            self.XSBeam.export(outfile, level, name_='XSBeam')
        else:
            warnEmptyAttribute("XSBeam", "XSBeam")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSBeam':
            obj_ = XSBeam()
            obj_.build(child_)
            self.setXSBeam(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSBeamSetting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSBeamSetting' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSBeamSetting is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSBeamSetting.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSBeamSetting()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSBeamSetting" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSBeamSetting()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSBeamSetting


class XSCalibration(XSData):
    def __init__(self, date=None):
        XSData.__init__(self, )
        if date is None:
            self._date = None
        elif date.__class__.__name__ == "XSDataDate":
            self._date = date
        else:
            strMessage = "ERROR! XSCalibration constructor argument 'date' is not XSDataDate but %s" % self._date.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'date' attribute
    def getDate(self): return self._date
    def setDate(self, date):
        if date is None:
            self._date = None
        elif date.__class__.__name__ == "XSDataDate":
            self._date = date
        else:
            strMessage = "ERROR! XSCalibration.setDate argument is not XSDataDate but %s" % date.__class__.__name__
            raise BaseException(strMessage)
    def delDate(self): self._date = None
    date = property(getDate, setDate, delDate, "Property for date")
    def export(self, outfile, level, name_='XSCalibration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSCalibration'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._date is not None:
            self.date.export(outfile, level, name_='date')
        else:
            warnEmptyAttribute("date", "XSDataDate")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'date':
            obj_ = XSDataDate()
            obj_.build(child_)
            self.setDate(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSCalibration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSCalibration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSCalibration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSCalibration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSCalibration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSCalibration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSCalibration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSCalibration


class XSCalibratedDisplacementAxis(XSData):
    def __init__(self, XSCalibration=None, zerodirection=None):
        XSData.__init__(self, )
        if zerodirection is None:
            self._zerodirection = None
        elif zerodirection.__class__.__name__ == "XSDataUnitVector":
            self._zerodirection = zerodirection
        else:
            strMessage = "ERROR! XSCalibratedDisplacementAxis constructor argument 'zerodirection' is not XSDataUnitVector but %s" % self._zerodirection.__class__.__name__
            raise BaseException(strMessage)
        if XSCalibration is None:
            self._XSCalibration = None
        elif XSCalibration.__class__.__name__ == "XSCalibration":
            self._XSCalibration = XSCalibration
        else:
            strMessage = "ERROR! XSCalibratedDisplacementAxis constructor argument 'XSCalibration' is not XSCalibration but %s" % self._XSCalibration.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'zerodirection' attribute
    def getZerodirection(self): return self._zerodirection
    def setZerodirection(self, zerodirection):
        if zerodirection is None:
            self._zerodirection = None
        elif zerodirection.__class__.__name__ == "XSDataUnitVector":
            self._zerodirection = zerodirection
        else:
            strMessage = "ERROR! XSCalibratedDisplacementAxis.setZerodirection argument is not XSDataUnitVector but %s" % zerodirection.__class__.__name__
            raise BaseException(strMessage)
    def delZerodirection(self): self._zerodirection = None
    zerodirection = property(getZerodirection, setZerodirection, delZerodirection, "Property for zerodirection")
    # Methods and properties for the 'XSCalibration' attribute
    def getXSCalibration(self): return self._XSCalibration
    def setXSCalibration(self, XSCalibration):
        if XSCalibration is None:
            self._XSCalibration = None
        elif XSCalibration.__class__.__name__ == "XSCalibration":
            self._XSCalibration = XSCalibration
        else:
            strMessage = "ERROR! XSCalibratedDisplacementAxis.setXSCalibration argument is not XSCalibration but %s" % XSCalibration.__class__.__name__
            raise BaseException(strMessage)
    def delXSCalibration(self): self._XSCalibration = None
    XSCalibration = property(getXSCalibration, setXSCalibration, delXSCalibration, "Property for XSCalibration")
    def export(self, outfile, level, name_='XSCalibratedDisplacementAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSCalibratedDisplacementAxis'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._zerodirection is not None:
            self.zerodirection.export(outfile, level, name_='zerodirection')
        else:
            warnEmptyAttribute("zerodirection", "XSDataUnitVector")
        if self._XSCalibration is not None:
            self.XSCalibration.export(outfile, level, name_='XSCalibration')
        else:
            warnEmptyAttribute("XSCalibration", "XSCalibration")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'zerodirection':
            obj_ = XSDataUnitVector()
            obj_.build(child_)
            self.setZerodirection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSCalibration':
            obj_ = XSCalibration()
            obj_.build(child_)
            self.setXSCalibration(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSCalibratedDisplacementAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSCalibratedDisplacementAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSCalibratedDisplacementAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSCalibratedDisplacementAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSCalibratedDisplacementAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSCalibratedDisplacementAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSCalibratedDisplacementAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSCalibratedDisplacementAxis


class XSDataCollection(XSData):
    def __init__(self, XSSubWedge=None, imagelocation=None):
        XSData.__init__(self, )
        if imagelocation is None:
            self._imagelocation = None
        elif imagelocation.__class__.__name__ == "XSDataString":
            self._imagelocation = imagelocation
        else:
            strMessage = "ERROR! XSDataCollection constructor argument 'imagelocation' is not XSDataString but %s" % self._imagelocation.__class__.__name__
            raise BaseException(strMessage)
        if XSSubWedge is None:
            self._XSSubWedge = []
        elif XSSubWedge.__class__.__name__ == "list":
            self._XSSubWedge = XSSubWedge
        else:
            strMessage = "ERROR! XSDataCollection constructor argument 'XSSubWedge' is not list but %s" % self._XSSubWedge.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imagelocation' attribute
    def getImagelocation(self): return self._imagelocation
    def setImagelocation(self, imagelocation):
        if imagelocation is None:
            self._imagelocation = None
        elif imagelocation.__class__.__name__ == "XSDataString":
            self._imagelocation = imagelocation
        else:
            strMessage = "ERROR! XSDataCollection.setImagelocation argument is not XSDataString but %s" % imagelocation.__class__.__name__
            raise BaseException(strMessage)
    def delImagelocation(self): self._imagelocation = None
    imagelocation = property(getImagelocation, setImagelocation, delImagelocation, "Property for imagelocation")
    # Methods and properties for the 'XSSubWedge' attribute
    def getXSSubWedge(self): return self._XSSubWedge
    def setXSSubWedge(self, XSSubWedge):
        if XSSubWedge is None:
            self._XSSubWedge = []
        elif XSSubWedge.__class__.__name__ == "list":
            self._XSSubWedge = XSSubWedge
        else:
            strMessage = "ERROR! XSDataCollection.setXSSubWedge argument is not list but %s" % XSSubWedge.__class__.__name__
            raise BaseException(strMessage)
    def delXSSubWedge(self): self._XSSubWedge = None
    XSSubWedge = property(getXSSubWedge, setXSSubWedge, delXSSubWedge, "Property for XSSubWedge")
    def addXSSubWedge(self, value):
        if value is None:
            strMessage = "ERROR! XSDataCollection.addXSSubWedge argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSSubWedge":
            self._XSSubWedge.append(value)
        else:
            strMessage = "ERROR! XSDataCollection.addXSSubWedge argument is not XSSubWedge but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSSubWedge(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataCollection.insertXSSubWedge argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataCollection.insertXSSubWedge argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSSubWedge":
            self._XSSubWedge[index] = value
        else:
            strMessage = "ERROR! XSDataCollection.addXSSubWedge argument is not XSSubWedge but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataCollection'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._imagelocation is not None:
            self.imagelocation.export(outfile, level, name_='imagelocation')
        else:
            warnEmptyAttribute("imagelocation", "XSDataString")
        for XSSubWedge_ in self.getXSSubWedge():
            XSSubWedge_.export(outfile, level, name_='XSSubWedge')
        if self.getXSSubWedge() == []:
            warnEmptyAttribute("XSSubWedge", "XSSubWedge")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagelocation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImagelocation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSSubWedge':
            obj_ = XSSubWedge()
            obj_.build(child_)
            self.XSSubWedge.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataCollection


class XSDataSpaceGroupType(XSData):
    def __init__(self, iucrstandardsymbol=None, iucrnumber=None):
        XSData.__init__(self, )
        if iucrnumber is None:
            self._iucrnumber = None
        elif iucrnumber.__class__.__name__ == "XSDataInteger":
            self._iucrnumber = iucrnumber
        else:
            strMessage = "ERROR! XSDataSpaceGroupType constructor argument 'iucrnumber' is not XSDataInteger but %s" % self._iucrnumber.__class__.__name__
            raise BaseException(strMessage)
        if iucrstandardsymbol is None:
            self._iucrstandardsymbol = None
        elif iucrstandardsymbol.__class__.__name__ == "XSDataString":
            self._iucrstandardsymbol = iucrstandardsymbol
        else:
            strMessage = "ERROR! XSDataSpaceGroupType constructor argument 'iucrstandardsymbol' is not XSDataString but %s" % self._iucrstandardsymbol.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'iucrnumber' attribute
    def getIucrnumber(self): return self._iucrnumber
    def setIucrnumber(self, iucrnumber):
        if iucrnumber is None:
            self._iucrnumber = None
        elif iucrnumber.__class__.__name__ == "XSDataInteger":
            self._iucrnumber = iucrnumber
        else:
            strMessage = "ERROR! XSDataSpaceGroupType.setIucrnumber argument is not XSDataInteger but %s" % iucrnumber.__class__.__name__
            raise BaseException(strMessage)
    def delIucrnumber(self): self._iucrnumber = None
    iucrnumber = property(getIucrnumber, setIucrnumber, delIucrnumber, "Property for iucrnumber")
    # Methods and properties for the 'iucrstandardsymbol' attribute
    def getIucrstandardsymbol(self): return self._iucrstandardsymbol
    def setIucrstandardsymbol(self, iucrstandardsymbol):
        if iucrstandardsymbol is None:
            self._iucrstandardsymbol = None
        elif iucrstandardsymbol.__class__.__name__ == "XSDataString":
            self._iucrstandardsymbol = iucrstandardsymbol
        else:
            strMessage = "ERROR! XSDataSpaceGroupType.setIucrstandardsymbol argument is not XSDataString but %s" % iucrstandardsymbol.__class__.__name__
            raise BaseException(strMessage)
    def delIucrstandardsymbol(self): self._iucrstandardsymbol = None
    iucrstandardsymbol = property(getIucrstandardsymbol, setIucrstandardsymbol, delIucrstandardsymbol, "Property for iucrstandardsymbol")
    def export(self, outfile, level, name_='XSDataSpaceGroupType'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSpaceGroupType'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._iucrnumber is not None:
            self.iucrnumber.export(outfile, level, name_='iucrnumber')
        else:
            warnEmptyAttribute("iucrnumber", "XSDataInteger")
        if self._iucrstandardsymbol is not None:
            self.iucrstandardsymbol.export(outfile, level, name_='iucrstandardsymbol')
        else:
            warnEmptyAttribute("iucrstandardsymbol", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iucrnumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIucrnumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iucrstandardsymbol':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIucrstandardsymbol(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSpaceGroupType" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSpaceGroupType' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSpaceGroupType is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSpaceGroupType.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSpaceGroupType()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSpaceGroupType" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSpaceGroupType()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSpaceGroupType


class XSDataUnitCell(XSData):
    def __init__(self, edgelengths=None, angles=None):
        XSData.__init__(self, )
        if angles is None:
            self._angles = []
        elif angles.__class__.__name__ == "list":
            self._angles = angles
        else:
            strMessage = "ERROR! XSDataUnitCell constructor argument 'angles' is not list but %s" % self._angles.__class__.__name__
            raise BaseException(strMessage)
        if edgelengths is None:
            self._edgelengths = []
        elif edgelengths.__class__.__name__ == "list":
            self._edgelengths = edgelengths
        else:
            strMessage = "ERROR! XSDataUnitCell constructor argument 'edgelengths' is not list but %s" % self._edgelengths.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angles' attribute
    def getAngles(self): return self._angles
    def setAngles(self, angles):
        if angles is None:
            self._angles = []
        elif angles.__class__.__name__ == "list":
            self._angles = angles
        else:
            strMessage = "ERROR! XSDataUnitCell.setAngles argument is not list but %s" % angles.__class__.__name__
            raise BaseException(strMessage)
    def delAngles(self): self._angles = None
    angles = property(getAngles, setAngles, delAngles, "Property for angles")
    def addAngles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataUnitCell.addAngles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAngle":
            self._angles.append(value)
        else:
            strMessage = "ERROR! XSDataUnitCell.addAngles argument is not XSDataAngle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAngles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataUnitCell.insertAngles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataUnitCell.insertAngles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAngle":
            self._angles[index] = value
        else:
            strMessage = "ERROR! XSDataUnitCell.addAngles argument is not XSDataAngle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'edgelengths' attribute
    def getEdgelengths(self): return self._edgelengths
    def setEdgelengths(self, edgelengths):
        if edgelengths is None:
            self._edgelengths = []
        elif edgelengths.__class__.__name__ == "list":
            self._edgelengths = edgelengths
        else:
            strMessage = "ERROR! XSDataUnitCell.setEdgelengths argument is not list but %s" % edgelengths.__class__.__name__
            raise BaseException(strMessage)
    def delEdgelengths(self): self._edgelengths = None
    edgelengths = property(getEdgelengths, setEdgelengths, delEdgelengths, "Property for edgelengths")
    def addEdgelengths(self, value):
        if value is None:
            strMessage = "ERROR! XSDataUnitCell.addEdgelengths argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataLength":
            self._edgelengths.append(value)
        else:
            strMessage = "ERROR! XSDataUnitCell.addEdgelengths argument is not XSDataLength but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertEdgelengths(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataUnitCell.insertEdgelengths argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataUnitCell.insertEdgelengths argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataLength":
            self._edgelengths[index] = value
        else:
            strMessage = "ERROR! XSDataUnitCell.addEdgelengths argument is not XSDataLength but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataUnitCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataUnitCell'):
        XSData.exportChildren(self, outfile, level, name_)
        for angles_ in self.getAngles():
            angles_.export(outfile, level, name_='angles')
        if self.getAngles() == []:
            warnEmptyAttribute("angles", "XSDataAngle")
        for edgelengths_ in self.getEdgelengths():
            edgelengths_.export(outfile, level, name_='edgelengths')
        if self.getEdgelengths() == []:
            warnEmptyAttribute("edgelengths", "XSDataLength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angles':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.angles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'edgelengths':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.edgelengths.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataUnitCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataUnitCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataUnitCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataUnitCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataUnitCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataUnitCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataUnitCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataUnitCell


class XSDataLattice(XSData):
    def __init__(self, representativespacegroup=None, unitcell=None):
        XSData.__init__(self, )
        if unitcell is None:
            self._unitcell = None
        elif unitcell.__class__.__name__ == "XSDataUnitCell":
            self._unitcell = unitcell
        else:
            strMessage = "ERROR! XSDataLattice constructor argument 'unitcell' is not XSDataUnitCell but %s" % self._unitcell.__class__.__name__
            raise BaseException(strMessage)
        if representativespacegroup is None:
            self._representativespacegroup = None
        elif representativespacegroup.__class__.__name__ == "XSDataSpaceGroupType":
            self._representativespacegroup = representativespacegroup
        else:
            strMessage = "ERROR! XSDataLattice constructor argument 'representativespacegroup' is not XSDataSpaceGroupType but %s" % self._representativespacegroup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'unitcell' attribute
    def getUnitcell(self): return self._unitcell
    def setUnitcell(self, unitcell):
        if unitcell is None:
            self._unitcell = None
        elif unitcell.__class__.__name__ == "XSDataUnitCell":
            self._unitcell = unitcell
        else:
            strMessage = "ERROR! XSDataLattice.setUnitcell argument is not XSDataUnitCell but %s" % unitcell.__class__.__name__
            raise BaseException(strMessage)
    def delUnitcell(self): self._unitcell = None
    unitcell = property(getUnitcell, setUnitcell, delUnitcell, "Property for unitcell")
    # Methods and properties for the 'representativespacegroup' attribute
    def getRepresentativespacegroup(self): return self._representativespacegroup
    def setRepresentativespacegroup(self, representativespacegroup):
        if representativespacegroup is None:
            self._representativespacegroup = None
        elif representativespacegroup.__class__.__name__ == "XSDataSpaceGroupType":
            self._representativespacegroup = representativespacegroup
        else:
            strMessage = "ERROR! XSDataLattice.setRepresentativespacegroup argument is not XSDataSpaceGroupType but %s" % representativespacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delRepresentativespacegroup(self): self._representativespacegroup = None
    representativespacegroup = property(getRepresentativespacegroup, setRepresentativespacegroup, delRepresentativespacegroup, "Property for representativespacegroup")
    def export(self, outfile, level, name_='XSDataLattice'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataLattice'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._unitcell is not None:
            self.unitcell.export(outfile, level, name_='unitcell')
        else:
            warnEmptyAttribute("unitcell", "XSDataUnitCell")
        if self._representativespacegroup is not None:
            self.representativespacegroup.export(outfile, level, name_='representativespacegroup')
        else:
            warnEmptyAttribute("representativespacegroup", "XSDataSpaceGroupType")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitcell':
            obj_ = XSDataUnitCell()
            obj_.build(child_)
            self.setUnitcell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'representativespacegroup':
            obj_ = XSDataSpaceGroupType()
            obj_.build(child_)
            self.setRepresentativespacegroup(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataLattice" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataLattice' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataLattice is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataLattice.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLattice()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataLattice" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLattice()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataLattice


class XSDetectorFaceAxisDirection(XSData):
    def __init__(self, direction=None):
        XSData.__init__(self, )
        if direction is None:
            self._direction = None
        elif direction.__class__.__name__ == "XSDataUnitVector":
            self._direction = direction
        else:
            strMessage = "ERROR! XSDetectorFaceAxisDirection constructor argument 'direction' is not XSDataUnitVector but %s" % self._direction.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'direction' attribute
    def getDirection(self): return self._direction
    def setDirection(self, direction):
        if direction is None:
            self._direction = None
        elif direction.__class__.__name__ == "XSDataUnitVector":
            self._direction = direction
        else:
            strMessage = "ERROR! XSDetectorFaceAxisDirection.setDirection argument is not XSDataUnitVector but %s" % direction.__class__.__name__
            raise BaseException(strMessage)
    def delDirection(self): self._direction = None
    direction = property(getDirection, setDirection, delDirection, "Property for direction")
    def export(self, outfile, level, name_='XSDetectorFaceAxisDirection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorFaceAxisDirection'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._direction is not None:
            self.direction.export(outfile, level, name_='direction')
        else:
            warnEmptyAttribute("direction", "XSDataUnitVector")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direction':
            obj_ = XSDataUnitVector()
            obj_.build(child_)
            self.setDirection(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorFaceAxisDirection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorFaceAxisDirection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorFaceAxisDirection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorFaceAxisDirection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceAxisDirection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorFaceAxisDirection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceAxisDirection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorFaceAxisDirection


class XSDetectorFaceAxis(XSData):
    def __init__(self, XSDetectorFaceAxisDirection=None, numberofpixels=None, pixelsize=None, name=None):
        XSData.__init__(self, )
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDetectorFaceAxis constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
        if pixelsize is None:
            self._pixelsize = None
        elif pixelsize.__class__.__name__ == "XSDataDouble":
            self._pixelsize = pixelsize
        else:
            strMessage = "ERROR! XSDetectorFaceAxis constructor argument 'pixelsize' is not XSDataDouble but %s" % self._pixelsize.__class__.__name__
            raise BaseException(strMessage)
        if numberofpixels is None:
            self._numberofpixels = None
        elif numberofpixels.__class__.__name__ == "XSDataInteger":
            self._numberofpixels = numberofpixels
        else:
            strMessage = "ERROR! XSDetectorFaceAxis constructor argument 'numberofpixels' is not XSDataInteger but %s" % self._numberofpixels.__class__.__name__
            raise BaseException(strMessage)
        if XSDetectorFaceAxisDirection is None:
            self._XSDetectorFaceAxisDirection = []
        elif XSDetectorFaceAxisDirection.__class__.__name__ == "list":
            self._XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
        else:
            strMessage = "ERROR! XSDetectorFaceAxis constructor argument 'XSDetectorFaceAxisDirection' is not list but %s" % self._XSDetectorFaceAxisDirection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    # Methods and properties for the 'pixelsize' attribute
    def getPixelsize(self): return self._pixelsize
    def setPixelsize(self, pixelsize):
        if pixelsize is None:
            self._pixelsize = None
        elif pixelsize.__class__.__name__ == "XSDataDouble":
            self._pixelsize = pixelsize
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.setPixelsize argument is not XSDataDouble but %s" % pixelsize.__class__.__name__
            raise BaseException(strMessage)
    def delPixelsize(self): self._pixelsize = None
    pixelsize = property(getPixelsize, setPixelsize, delPixelsize, "Property for pixelsize")
    # Methods and properties for the 'numberofpixels' attribute
    def getNumberofpixels(self): return self._numberofpixels
    def setNumberofpixels(self, numberofpixels):
        if numberofpixels is None:
            self._numberofpixels = None
        elif numberofpixels.__class__.__name__ == "XSDataInteger":
            self._numberofpixels = numberofpixels
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.setNumberofpixels argument is not XSDataInteger but %s" % numberofpixels.__class__.__name__
            raise BaseException(strMessage)
    def delNumberofpixels(self): self._numberofpixels = None
    numberofpixels = property(getNumberofpixels, setNumberofpixels, delNumberofpixels, "Property for numberofpixels")
    # Methods and properties for the 'XSDetectorFaceAxisDirection' attribute
    def getXSDetectorFaceAxisDirection(self): return self._XSDetectorFaceAxisDirection
    def setXSDetectorFaceAxisDirection(self, XSDetectorFaceAxisDirection):
        if XSDetectorFaceAxisDirection is None:
            self._XSDetectorFaceAxisDirection = []
        elif XSDetectorFaceAxisDirection.__class__.__name__ == "list":
            self._XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.setXSDetectorFaceAxisDirection argument is not list but %s" % XSDetectorFaceAxisDirection.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetectorFaceAxisDirection(self): self._XSDetectorFaceAxisDirection = None
    XSDetectorFaceAxisDirection = property(getXSDetectorFaceAxisDirection, setXSDetectorFaceAxisDirection, delXSDetectorFaceAxisDirection, "Property for XSDetectorFaceAxisDirection")
    def addXSDetectorFaceAxisDirection(self, value):
        if value is None:
            strMessage = "ERROR! XSDetectorFaceAxis.addXSDetectorFaceAxisDirection argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxisDirection":
            self._XSDetectorFaceAxisDirection.append(value)
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.addXSDetectorFaceAxisDirection argument is not XSDetectorFaceAxisDirection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDetectorFaceAxisDirection(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDetectorFaceAxis.insertXSDetectorFaceAxisDirection argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDetectorFaceAxis.insertXSDetectorFaceAxisDirection argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxisDirection":
            self._XSDetectorFaceAxisDirection[index] = value
        else:
            strMessage = "ERROR! XSDetectorFaceAxis.addXSDetectorFaceAxisDirection argument is not XSDetectorFaceAxisDirection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDetectorFaceAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorFaceAxis'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        else:
            warnEmptyAttribute("name", "XSDataString")
        if self._pixelsize is not None:
            self.pixelsize.export(outfile, level, name_='pixelsize')
        else:
            warnEmptyAttribute("pixelsize", "XSDataDouble")
        if self._numberofpixels is not None:
            self.numberofpixels.export(outfile, level, name_='numberofpixels')
        else:
            warnEmptyAttribute("numberofpixels", "XSDataInteger")
        for XSDetectorFaceAxisDirection_ in self.getXSDetectorFaceAxisDirection():
            XSDetectorFaceAxisDirection_.export(outfile, level, name_='XSDetectorFaceAxisDirection')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelsize':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPixelsize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberofpixels':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberofpixels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetectorFaceAxisDirection':
            obj_ = XSDetectorFaceAxisDirection()
            obj_.build(child_)
            self.XSDetectorFaceAxisDirection.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorFaceAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorFaceAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorFaceAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorFaceAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorFaceAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorFaceAxis


class XSDetectorFaceSetting(XSData):
    def __init__(self, XSDetectorFaceAxisDirection=None, detectoraxesorigin=None):
        XSData.__init__(self, )
        if detectoraxesorigin is None:
            self._detectoraxesorigin = None
        elif detectoraxesorigin.__class__.__name__ == "XSDataVectorDouble":
            self._detectoraxesorigin = detectoraxesorigin
        else:
            strMessage = "ERROR! XSDetectorFaceSetting constructor argument 'detectoraxesorigin' is not XSDataVectorDouble but %s" % self._detectoraxesorigin.__class__.__name__
            raise BaseException(strMessage)
        if XSDetectorFaceAxisDirection is None:
            self._XSDetectorFaceAxisDirection = []
        elif XSDetectorFaceAxisDirection.__class__.__name__ == "list":
            self._XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
        else:
            strMessage = "ERROR! XSDetectorFaceSetting constructor argument 'XSDetectorFaceAxisDirection' is not list but %s" % self._XSDetectorFaceAxisDirection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detectoraxesorigin' attribute
    def getDetectoraxesorigin(self): return self._detectoraxesorigin
    def setDetectoraxesorigin(self, detectoraxesorigin):
        if detectoraxesorigin is None:
            self._detectoraxesorigin = None
        elif detectoraxesorigin.__class__.__name__ == "XSDataVectorDouble":
            self._detectoraxesorigin = detectoraxesorigin
        else:
            strMessage = "ERROR! XSDetectorFaceSetting.setDetectoraxesorigin argument is not XSDataVectorDouble but %s" % detectoraxesorigin.__class__.__name__
            raise BaseException(strMessage)
    def delDetectoraxesorigin(self): self._detectoraxesorigin = None
    detectoraxesorigin = property(getDetectoraxesorigin, setDetectoraxesorigin, delDetectoraxesorigin, "Property for detectoraxesorigin")
    # Methods and properties for the 'XSDetectorFaceAxisDirection' attribute
    def getXSDetectorFaceAxisDirection(self): return self._XSDetectorFaceAxisDirection
    def setXSDetectorFaceAxisDirection(self, XSDetectorFaceAxisDirection):
        if XSDetectorFaceAxisDirection is None:
            self._XSDetectorFaceAxisDirection = []
        elif XSDetectorFaceAxisDirection.__class__.__name__ == "list":
            self._XSDetectorFaceAxisDirection = XSDetectorFaceAxisDirection
        else:
            strMessage = "ERROR! XSDetectorFaceSetting.setXSDetectorFaceAxisDirection argument is not list but %s" % XSDetectorFaceAxisDirection.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetectorFaceAxisDirection(self): self._XSDetectorFaceAxisDirection = None
    XSDetectorFaceAxisDirection = property(getXSDetectorFaceAxisDirection, setXSDetectorFaceAxisDirection, delXSDetectorFaceAxisDirection, "Property for XSDetectorFaceAxisDirection")
    def addXSDetectorFaceAxisDirection(self, value):
        if value is None:
            strMessage = "ERROR! XSDetectorFaceSetting.addXSDetectorFaceAxisDirection argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxisDirection":
            self._XSDetectorFaceAxisDirection.append(value)
        else:
            strMessage = "ERROR! XSDetectorFaceSetting.addXSDetectorFaceAxisDirection argument is not XSDetectorFaceAxisDirection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDetectorFaceAxisDirection(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDetectorFaceSetting.insertXSDetectorFaceAxisDirection argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDetectorFaceSetting.insertXSDetectorFaceAxisDirection argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxisDirection":
            self._XSDetectorFaceAxisDirection[index] = value
        else:
            strMessage = "ERROR! XSDetectorFaceSetting.addXSDetectorFaceAxisDirection argument is not XSDetectorFaceAxisDirection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDetectorFaceSetting'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorFaceSetting'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._detectoraxesorigin is not None:
            self.detectoraxesorigin.export(outfile, level, name_='detectoraxesorigin')
        else:
            warnEmptyAttribute("detectoraxesorigin", "XSDataVectorDouble")
        for XSDetectorFaceAxisDirection_ in self.getXSDetectorFaceAxisDirection():
            XSDetectorFaceAxisDirection_.export(outfile, level, name_='XSDetectorFaceAxisDirection')
        if self.getXSDetectorFaceAxisDirection() == []:
            warnEmptyAttribute("XSDetectorFaceAxisDirection", "XSDetectorFaceAxisDirection")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectoraxesorigin':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDetectoraxesorigin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetectorFaceAxisDirection':
            obj_ = XSDetectorFaceAxisDirection()
            obj_.build(child_)
            self.XSDetectorFaceAxisDirection.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorFaceSetting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorFaceSetting' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorFaceSetting is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorFaceSetting.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceSetting()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorFaceSetting" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorFaceSetting()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorFaceSetting


class XSDetectorImageProperties(XSData):
    def __init__(self, format=None, headersizevariable=None, headersize=None, mode=None):
        XSData.__init__(self, )
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDetectorImageProperties constructor argument 'mode' is not XSDataString but %s" % self._mode.__class__.__name__
            raise BaseException(strMessage)
        if headersize is None:
            self._headersize = None
        elif headersize.__class__.__name__ == "XSDataInteger":
            self._headersize = headersize
        else:
            strMessage = "ERROR! XSDetectorImageProperties constructor argument 'headersize' is not XSDataInteger but %s" % self._headersize.__class__.__name__
            raise BaseException(strMessage)
        if headersizevariable is None:
            self._headersizevariable = None
        elif headersizevariable.__class__.__name__ == "XSDataBoolean":
            self._headersizevariable = headersizevariable
        else:
            strMessage = "ERROR! XSDetectorImageProperties constructor argument 'headersizevariable' is not XSDataBoolean but %s" % self._headersizevariable.__class__.__name__
            raise BaseException(strMessage)
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDetectorImageProperties constructor argument 'format' is not XSDataString but %s" % self._format.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mode' attribute
    def getMode(self): return self._mode
    def setMode(self, mode):
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDetectorImageProperties.setMode argument is not XSDataString but %s" % mode.__class__.__name__
            raise BaseException(strMessage)
    def delMode(self): self._mode = None
    mode = property(getMode, setMode, delMode, "Property for mode")
    # Methods and properties for the 'headersize' attribute
    def getHeadersize(self): return self._headersize
    def setHeadersize(self, headersize):
        if headersize is None:
            self._headersize = None
        elif headersize.__class__.__name__ == "XSDataInteger":
            self._headersize = headersize
        else:
            strMessage = "ERROR! XSDetectorImageProperties.setHeadersize argument is not XSDataInteger but %s" % headersize.__class__.__name__
            raise BaseException(strMessage)
    def delHeadersize(self): self._headersize = None
    headersize = property(getHeadersize, setHeadersize, delHeadersize, "Property for headersize")
    # Methods and properties for the 'headersizevariable' attribute
    def getHeadersizevariable(self): return self._headersizevariable
    def setHeadersizevariable(self, headersizevariable):
        if headersizevariable is None:
            self._headersizevariable = None
        elif headersizevariable.__class__.__name__ == "XSDataBoolean":
            self._headersizevariable = headersizevariable
        else:
            strMessage = "ERROR! XSDetectorImageProperties.setHeadersizevariable argument is not XSDataBoolean but %s" % headersizevariable.__class__.__name__
            raise BaseException(strMessage)
    def delHeadersizevariable(self): self._headersizevariable = None
    headersizevariable = property(getHeadersizevariable, setHeadersizevariable, delHeadersizevariable, "Property for headersizevariable")
    # Methods and properties for the 'format' attribute
    def getFormat(self): return self._format
    def setFormat(self, format):
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDetectorImageProperties.setFormat argument is not XSDataString but %s" % format.__class__.__name__
            raise BaseException(strMessage)
    def delFormat(self): self._format = None
    format = property(getFormat, setFormat, delFormat, "Property for format")
    def export(self, outfile, level, name_='XSDetectorImageProperties'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorImageProperties'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
        else:
            warnEmptyAttribute("mode", "XSDataString")
        if self._headersize is not None:
            self.headersize.export(outfile, level, name_='headersize')
        else:
            warnEmptyAttribute("headersize", "XSDataInteger")
        if self._headersizevariable is not None:
            self.headersizevariable.export(outfile, level, name_='headersizevariable')
        else:
            warnEmptyAttribute("headersizevariable", "XSDataBoolean")
        if self._format is not None:
            self.format.export(outfile, level, name_='format')
        else:
            warnEmptyAttribute("format", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'headersize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setHeadersize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'headersizevariable':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setHeadersizevariable(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'format':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFormat(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorImageProperties" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorImageProperties' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorImageProperties is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorImageProperties.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorImageProperties()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorImageProperties" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorImageProperties()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorImageProperties


class XSDiffractionImages(XSData):
    def __init__(self, filename=None):
        XSData.__init__(self, )
        if filename is None:
            self._filename = None
        elif filename.__class__.__name__ == "XSDataString":
            self._filename = filename
        else:
            strMessage = "ERROR! XSDiffractionImages constructor argument 'filename' is not XSDataString but %s" % self._filename.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'filename' attribute
    def getFilename(self): return self._filename
    def setFilename(self, filename):
        if filename is None:
            self._filename = None
        elif filename.__class__.__name__ == "XSDataString":
            self._filename = filename
        else:
            strMessage = "ERROR! XSDiffractionImages.setFilename argument is not XSDataString but %s" % filename.__class__.__name__
            raise BaseException(strMessage)
    def delFilename(self): self._filename = None
    filename = property(getFilename, setFilename, delFilename, "Property for filename")
    def export(self, outfile, level, name_='XSDiffractionImages'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDiffractionImages'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._filename is not None:
            self.filename.export(outfile, level, name_='filename')
        else:
            warnEmptyAttribute("filename", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filename':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFilename(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDiffractionImages" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDiffractionImages' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDiffractionImages is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDiffractionImages.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDiffractionImages()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDiffractionImages" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDiffractionImages()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDiffractionImages


class XSDisplacementAxis(XSData):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
        XSData.__init__(self, )
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDisplacementAxis constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
        if XSCalibratedDisplacementAxis is None:
            self._XSCalibratedDisplacementAxis = []
        elif XSCalibratedDisplacementAxis.__class__.__name__ == "list":
            self._XSCalibratedDisplacementAxis = XSCalibratedDisplacementAxis
        else:
            strMessage = "ERROR! XSDisplacementAxis constructor argument 'XSCalibratedDisplacementAxis' is not list but %s" % self._XSCalibratedDisplacementAxis.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDisplacementAxis.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    # Methods and properties for the 'XSCalibratedDisplacementAxis' attribute
    def getXSCalibratedDisplacementAxis(self): return self._XSCalibratedDisplacementAxis
    def setXSCalibratedDisplacementAxis(self, XSCalibratedDisplacementAxis):
        if XSCalibratedDisplacementAxis is None:
            self._XSCalibratedDisplacementAxis = []
        elif XSCalibratedDisplacementAxis.__class__.__name__ == "list":
            self._XSCalibratedDisplacementAxis = XSCalibratedDisplacementAxis
        else:
            strMessage = "ERROR! XSDisplacementAxis.setXSCalibratedDisplacementAxis argument is not list but %s" % XSCalibratedDisplacementAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSCalibratedDisplacementAxis(self): self._XSCalibratedDisplacementAxis = None
    XSCalibratedDisplacementAxis = property(getXSCalibratedDisplacementAxis, setXSCalibratedDisplacementAxis, delXSCalibratedDisplacementAxis, "Property for XSCalibratedDisplacementAxis")
    def addXSCalibratedDisplacementAxis(self, value):
        if value is None:
            strMessage = "ERROR! XSDisplacementAxis.addXSCalibratedDisplacementAxis argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSCalibratedDisplacementAxis":
            self._XSCalibratedDisplacementAxis.append(value)
        else:
            strMessage = "ERROR! XSDisplacementAxis.addXSCalibratedDisplacementAxis argument is not XSCalibratedDisplacementAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSCalibratedDisplacementAxis(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDisplacementAxis.insertXSCalibratedDisplacementAxis argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDisplacementAxis.insertXSCalibratedDisplacementAxis argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSCalibratedDisplacementAxis":
            self._XSCalibratedDisplacementAxis[index] = value
        else:
            strMessage = "ERROR! XSDisplacementAxis.addXSCalibratedDisplacementAxis argument is not XSCalibratedDisplacementAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDisplacementAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDisplacementAxis'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        else:
            warnEmptyAttribute("name", "XSDataString")
        for XSCalibratedDisplacementAxis_ in self.getXSCalibratedDisplacementAxis():
            XSCalibratedDisplacementAxis_.export(outfile, level, name_='XSCalibratedDisplacementAxis')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSCalibratedDisplacementAxis':
            obj_ = XSCalibratedDisplacementAxis()
            obj_.build(child_)
            self.XSCalibratedDisplacementAxis.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDisplacementAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDisplacementAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDisplacementAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDisplacementAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDisplacementAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDisplacementAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDisplacementAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDisplacementAxis


class XSDisplacementList(XSData):
    def __init__(self, ):
        XSData.__init__(self, )
    def export(self, outfile, level, name_='XSDisplacementList'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDisplacementList'):
        XSData.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDisplacementList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDisplacementList' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDisplacementList is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDisplacementList.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDisplacementList()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDisplacementList" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDisplacementList()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDisplacementList


class XSDisplacementListSetting(XSData):
    def __init__(self, ):
        XSData.__init__(self, )
    def export(self, outfile, level, name_='XSDisplacementListSetting'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDisplacementListSetting'):
        XSData.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDisplacementListSetting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDisplacementListSetting' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDisplacementListSetting is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDisplacementListSetting.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDisplacementListSetting()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDisplacementListSetting" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDisplacementListSetting()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDisplacementListSetting


class XSFoundSpot(XSData):
    def __init__(self, intensityesu=None, intensity=None, omega=None, detectorposition=None):
        XSData.__init__(self, )
        if detectorposition is None:
            self._detectorposition = []
        elif detectorposition.__class__.__name__ == "list":
            self._detectorposition = detectorposition
        else:
            strMessage = "ERROR! XSFoundSpot constructor argument 'detectorposition' is not list but %s" % self._detectorposition.__class__.__name__
            raise BaseException(strMessage)
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSFoundSpot constructor argument 'omega' is not XSDataAngle but %s" % self._omega.__class__.__name__
            raise BaseException(strMessage)
        if intensity is None:
            self._intensity = None
        elif intensity.__class__.__name__ == "XSDataDouble":
            self._intensity = intensity
        else:
            strMessage = "ERROR! XSFoundSpot constructor argument 'intensity' is not XSDataDouble but %s" % self._intensity.__class__.__name__
            raise BaseException(strMessage)
        if intensityesu is None:
            self._intensityesu = None
        elif intensityesu.__class__.__name__ == "XSDataDouble":
            self._intensityesu = intensityesu
        else:
            strMessage = "ERROR! XSFoundSpot constructor argument 'intensityesu' is not XSDataDouble but %s" % self._intensityesu.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detectorposition' attribute
    def getDetectorposition(self): return self._detectorposition
    def setDetectorposition(self, detectorposition):
        if detectorposition is None:
            self._detectorposition = []
        elif detectorposition.__class__.__name__ == "list":
            self._detectorposition = detectorposition
        else:
            strMessage = "ERROR! XSFoundSpot.setDetectorposition argument is not list but %s" % detectorposition.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorposition(self): self._detectorposition = None
    detectorposition = property(getDetectorposition, setDetectorposition, delDetectorposition, "Property for detectorposition")
    def addDetectorposition(self, value):
        if value is None:
            strMessage = "ERROR! XSFoundSpot.addDetectorposition argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._detectorposition.append(value)
        else:
            strMessage = "ERROR! XSFoundSpot.addDetectorposition argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDetectorposition(self, index, value):
        if index is None:
            strMessage = "ERROR! XSFoundSpot.insertDetectorposition argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSFoundSpot.insertDetectorposition argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._detectorposition[index] = value
        else:
            strMessage = "ERROR! XSFoundSpot.addDetectorposition argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'omega' attribute
    def getOmega(self): return self._omega
    def setOmega(self, omega):
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSFoundSpot.setOmega argument is not XSDataAngle but %s" % omega.__class__.__name__
            raise BaseException(strMessage)
    def delOmega(self): self._omega = None
    omega = property(getOmega, setOmega, delOmega, "Property for omega")
    # Methods and properties for the 'intensity' attribute
    def getIntensity(self): return self._intensity
    def setIntensity(self, intensity):
        if intensity is None:
            self._intensity = None
        elif intensity.__class__.__name__ == "XSDataDouble":
            self._intensity = intensity
        else:
            strMessage = "ERROR! XSFoundSpot.setIntensity argument is not XSDataDouble but %s" % intensity.__class__.__name__
            raise BaseException(strMessage)
    def delIntensity(self): self._intensity = None
    intensity = property(getIntensity, setIntensity, delIntensity, "Property for intensity")
    # Methods and properties for the 'intensityesu' attribute
    def getIntensityesu(self): return self._intensityesu
    def setIntensityesu(self, intensityesu):
        if intensityesu is None:
            self._intensityesu = None
        elif intensityesu.__class__.__name__ == "XSDataDouble":
            self._intensityesu = intensityesu
        else:
            strMessage = "ERROR! XSFoundSpot.setIntensityesu argument is not XSDataDouble but %s" % intensityesu.__class__.__name__
            raise BaseException(strMessage)
    def delIntensityesu(self): self._intensityesu = None
    intensityesu = property(getIntensityesu, setIntensityesu, delIntensityesu, "Property for intensityesu")
    def export(self, outfile, level, name_='XSFoundSpot'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSFoundSpot'):
        XSData.exportChildren(self, outfile, level, name_)
        for detectorposition_ in self.getDetectorposition():
            detectorposition_.export(outfile, level, name_='detectorposition')
        if self.getDetectorposition() == []:
            warnEmptyAttribute("detectorposition", "XSDataDouble")
        if self._omega is not None:
            self.omega.export(outfile, level, name_='omega')
        else:
            warnEmptyAttribute("omega", "XSDataAngle")
        if self._intensity is not None:
            self.intensity.export(outfile, level, name_='intensity')
        else:
            warnEmptyAttribute("intensity", "XSDataDouble")
        if self._intensityesu is not None:
            self.intensityesu.export(outfile, level, name_='intensityesu')
        else:
            warnEmptyAttribute("intensityesu", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorposition':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.detectorposition.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omega':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOmega(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'intensity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'intensityesu':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIntensityesu(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSFoundSpot" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSFoundSpot' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSFoundSpot is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSFoundSpot.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSFoundSpot()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSFoundSpot" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSFoundSpot()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSFoundSpot


class XSImageRange(XSData):
    def __init__(self, XSProcessingWedge=None, endimage=None, startimage=None):
        XSData.__init__(self, )
        if startimage is None:
            self._startimage = None
        elif startimage.__class__.__name__ == "XSDataInteger":
            self._startimage = startimage
        else:
            strMessage = "ERROR! XSImageRange constructor argument 'startimage' is not XSDataInteger but %s" % self._startimage.__class__.__name__
            raise BaseException(strMessage)
        if endimage is None:
            self._endimage = None
        elif endimage.__class__.__name__ == "XSDataInteger":
            self._endimage = endimage
        else:
            strMessage = "ERROR! XSImageRange constructor argument 'endimage' is not XSDataInteger but %s" % self._endimage.__class__.__name__
            raise BaseException(strMessage)
        if XSProcessingWedge is None:
            self._XSProcessingWedge = None
        elif XSProcessingWedge.__class__.__name__ == "XSProcessingWedge":
            self._XSProcessingWedge = XSProcessingWedge
        else:
            strMessage = "ERROR! XSImageRange constructor argument 'XSProcessingWedge' is not XSProcessingWedge but %s" % self._XSProcessingWedge.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'startimage' attribute
    def getStartimage(self): return self._startimage
    def setStartimage(self, startimage):
        if startimage is None:
            self._startimage = None
        elif startimage.__class__.__name__ == "XSDataInteger":
            self._startimage = startimage
        else:
            strMessage = "ERROR! XSImageRange.setStartimage argument is not XSDataInteger but %s" % startimage.__class__.__name__
            raise BaseException(strMessage)
    def delStartimage(self): self._startimage = None
    startimage = property(getStartimage, setStartimage, delStartimage, "Property for startimage")
    # Methods and properties for the 'endimage' attribute
    def getEndimage(self): return self._endimage
    def setEndimage(self, endimage):
        if endimage is None:
            self._endimage = None
        elif endimage.__class__.__name__ == "XSDataInteger":
            self._endimage = endimage
        else:
            strMessage = "ERROR! XSImageRange.setEndimage argument is not XSDataInteger but %s" % endimage.__class__.__name__
            raise BaseException(strMessage)
    def delEndimage(self): self._endimage = None
    endimage = property(getEndimage, setEndimage, delEndimage, "Property for endimage")
    # Methods and properties for the 'XSProcessingWedge' attribute
    def getXSProcessingWedge(self): return self._XSProcessingWedge
    def setXSProcessingWedge(self, XSProcessingWedge):
        if XSProcessingWedge is None:
            self._XSProcessingWedge = None
        elif XSProcessingWedge.__class__.__name__ == "XSProcessingWedge":
            self._XSProcessingWedge = XSProcessingWedge
        else:
            strMessage = "ERROR! XSImageRange.setXSProcessingWedge argument is not XSProcessingWedge but %s" % XSProcessingWedge.__class__.__name__
            raise BaseException(strMessage)
    def delXSProcessingWedge(self): self._XSProcessingWedge = None
    XSProcessingWedge = property(getXSProcessingWedge, setXSProcessingWedge, delXSProcessingWedge, "Property for XSProcessingWedge")
    def export(self, outfile, level, name_='XSImageRange'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSImageRange'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._startimage is not None:
            self.startimage.export(outfile, level, name_='startimage')
        else:
            warnEmptyAttribute("startimage", "XSDataInteger")
        if self._endimage is not None:
            self.endimage.export(outfile, level, name_='endimage')
        else:
            warnEmptyAttribute("endimage", "XSDataInteger")
        if self._XSProcessingWedge is not None:
            self.XSProcessingWedge.export(outfile, level, name_='XSProcessingWedge')
        else:
            warnEmptyAttribute("XSProcessingWedge", "XSProcessingWedge")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startimage':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStartimage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endimage':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEndimage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSProcessingWedge':
            obj_ = XSProcessingWedge()
            obj_.build(child_)
            self.setXSProcessingWedge(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSImageRange" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSImageRange' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSImageRange is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSImageRange.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSImageRange()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSImageRange" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSImageRange()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSImageRange


class XSIndexingResult(XSData):
    def __init__(self, XSIndexingSolution=None, XSIndexingOutput=None, selectedsolution=None):
        XSData.__init__(self, )
        if selectedsolution is None:
            self._selectedsolution = None
        elif selectedsolution.__class__.__name__ == "XSDataInteger":
            self._selectedsolution = selectedsolution
        else:
            strMessage = "ERROR! XSIndexingResult constructor argument 'selectedsolution' is not XSDataInteger but %s" % self._selectedsolution.__class__.__name__
            raise BaseException(strMessage)
        if XSIndexingOutput is None:
            self._XSIndexingOutput = []
        elif XSIndexingOutput.__class__.__name__ == "list":
            self._XSIndexingOutput = XSIndexingOutput
        else:
            strMessage = "ERROR! XSIndexingResult constructor argument 'XSIndexingOutput' is not list but %s" % self._XSIndexingOutput.__class__.__name__
            raise BaseException(strMessage)
        if XSIndexingSolution is None:
            self._XSIndexingSolution = []
        elif XSIndexingSolution.__class__.__name__ == "list":
            self._XSIndexingSolution = XSIndexingSolution
        else:
            strMessage = "ERROR! XSIndexingResult constructor argument 'XSIndexingSolution' is not list but %s" % self._XSIndexingSolution.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'selectedsolution' attribute
    def getSelectedsolution(self): return self._selectedsolution
    def setSelectedsolution(self, selectedsolution):
        if selectedsolution is None:
            self._selectedsolution = None
        elif selectedsolution.__class__.__name__ == "XSDataInteger":
            self._selectedsolution = selectedsolution
        else:
            strMessage = "ERROR! XSIndexingResult.setSelectedsolution argument is not XSDataInteger but %s" % selectedsolution.__class__.__name__
            raise BaseException(strMessage)
    def delSelectedsolution(self): self._selectedsolution = None
    selectedsolution = property(getSelectedsolution, setSelectedsolution, delSelectedsolution, "Property for selectedsolution")
    # Methods and properties for the 'XSIndexingOutput' attribute
    def getXSIndexingOutput(self): return self._XSIndexingOutput
    def setXSIndexingOutput(self, XSIndexingOutput):
        if XSIndexingOutput is None:
            self._XSIndexingOutput = []
        elif XSIndexingOutput.__class__.__name__ == "list":
            self._XSIndexingOutput = XSIndexingOutput
        else:
            strMessage = "ERROR! XSIndexingResult.setXSIndexingOutput argument is not list but %s" % XSIndexingOutput.__class__.__name__
            raise BaseException(strMessage)
    def delXSIndexingOutput(self): self._XSIndexingOutput = None
    XSIndexingOutput = property(getXSIndexingOutput, setXSIndexingOutput, delXSIndexingOutput, "Property for XSIndexingOutput")
    def addXSIndexingOutput(self, value):
        if value is None:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingOutput argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingOutput":
            self._XSIndexingOutput.append(value)
        else:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingOutput argument is not XSIndexingOutput but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSIndexingOutput(self, index, value):
        if index is None:
            strMessage = "ERROR! XSIndexingResult.insertXSIndexingOutput argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSIndexingResult.insertXSIndexingOutput argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingOutput":
            self._XSIndexingOutput[index] = value
        else:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingOutput argument is not XSIndexingOutput but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSIndexingSolution' attribute
    def getXSIndexingSolution(self): return self._XSIndexingSolution
    def setXSIndexingSolution(self, XSIndexingSolution):
        if XSIndexingSolution is None:
            self._XSIndexingSolution = []
        elif XSIndexingSolution.__class__.__name__ == "list":
            self._XSIndexingSolution = XSIndexingSolution
        else:
            strMessage = "ERROR! XSIndexingResult.setXSIndexingSolution argument is not list but %s" % XSIndexingSolution.__class__.__name__
            raise BaseException(strMessage)
    def delXSIndexingSolution(self): self._XSIndexingSolution = None
    XSIndexingSolution = property(getXSIndexingSolution, setXSIndexingSolution, delXSIndexingSolution, "Property for XSIndexingSolution")
    def addXSIndexingSolution(self, value):
        if value is None:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingSolution argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingSolution":
            self._XSIndexingSolution.append(value)
        else:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingSolution argument is not XSIndexingSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSIndexingSolution(self, index, value):
        if index is None:
            strMessage = "ERROR! XSIndexingResult.insertXSIndexingSolution argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSIndexingResult.insertXSIndexingSolution argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingSolution":
            self._XSIndexingSolution[index] = value
        else:
            strMessage = "ERROR! XSIndexingResult.addXSIndexingSolution argument is not XSIndexingSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSIndexingResult'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSIndexingResult'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._selectedsolution is not None:
            self.selectedsolution.export(outfile, level, name_='selectedsolution')
        else:
            warnEmptyAttribute("selectedsolution", "XSDataInteger")
        for XSIndexingOutput_ in self.getXSIndexingOutput():
            XSIndexingOutput_.export(outfile, level, name_='XSIndexingOutput')
        if self.getXSIndexingOutput() == []:
            warnEmptyAttribute("XSIndexingOutput", "XSIndexingOutput")
        for XSIndexingSolution_ in self.getXSIndexingSolution():
            XSIndexingSolution_.export(outfile, level, name_='XSIndexingSolution')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedsolution':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSelectedsolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSIndexingOutput':
            obj_ = XSIndexingOutput()
            obj_.build(child_)
            self.XSIndexingOutput.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSIndexingSolution':
            obj_ = XSIndexingSolution()
            obj_.build(child_)
            self.XSIndexingSolution.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSIndexingResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSIndexingResult' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSIndexingResult is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSIndexingResult.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSIndexingResult()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSIndexingResult" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSIndexingResult()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSIndexingResult


class XSIndexingInput(XSData):
    def __init__(self, XSIndexingResult=None, XSSpotSearchOutput=None):
        XSData.__init__(self, )
        if XSSpotSearchOutput is None:
            self._XSSpotSearchOutput = []
        elif XSSpotSearchOutput.__class__.__name__ == "list":
            self._XSSpotSearchOutput = XSSpotSearchOutput
        else:
            strMessage = "ERROR! XSIndexingInput constructor argument 'XSSpotSearchOutput' is not list but %s" % self._XSSpotSearchOutput.__class__.__name__
            raise BaseException(strMessage)
        if XSIndexingResult is None:
            self._XSIndexingResult = []
        elif XSIndexingResult.__class__.__name__ == "list":
            self._XSIndexingResult = XSIndexingResult
        else:
            strMessage = "ERROR! XSIndexingInput constructor argument 'XSIndexingResult' is not list but %s" % self._XSIndexingResult.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSSpotSearchOutput' attribute
    def getXSSpotSearchOutput(self): return self._XSSpotSearchOutput
    def setXSSpotSearchOutput(self, XSSpotSearchOutput):
        if XSSpotSearchOutput is None:
            self._XSSpotSearchOutput = []
        elif XSSpotSearchOutput.__class__.__name__ == "list":
            self._XSSpotSearchOutput = XSSpotSearchOutput
        else:
            strMessage = "ERROR! XSIndexingInput.setXSSpotSearchOutput argument is not list but %s" % XSSpotSearchOutput.__class__.__name__
            raise BaseException(strMessage)
    def delXSSpotSearchOutput(self): self._XSSpotSearchOutput = None
    XSSpotSearchOutput = property(getXSSpotSearchOutput, setXSSpotSearchOutput, delXSSpotSearchOutput, "Property for XSSpotSearchOutput")
    def addXSSpotSearchOutput(self, value):
        if value is None:
            strMessage = "ERROR! XSIndexingInput.addXSSpotSearchOutput argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSSpotSearchOutput":
            self._XSSpotSearchOutput.append(value)
        else:
            strMessage = "ERROR! XSIndexingInput.addXSSpotSearchOutput argument is not XSSpotSearchOutput but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSSpotSearchOutput(self, index, value):
        if index is None:
            strMessage = "ERROR! XSIndexingInput.insertXSSpotSearchOutput argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSIndexingInput.insertXSSpotSearchOutput argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSSpotSearchOutput":
            self._XSSpotSearchOutput[index] = value
        else:
            strMessage = "ERROR! XSIndexingInput.addXSSpotSearchOutput argument is not XSSpotSearchOutput but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSIndexingResult' attribute
    def getXSIndexingResult(self): return self._XSIndexingResult
    def setXSIndexingResult(self, XSIndexingResult):
        if XSIndexingResult is None:
            self._XSIndexingResult = []
        elif XSIndexingResult.__class__.__name__ == "list":
            self._XSIndexingResult = XSIndexingResult
        else:
            strMessage = "ERROR! XSIndexingInput.setXSIndexingResult argument is not list but %s" % XSIndexingResult.__class__.__name__
            raise BaseException(strMessage)
    def delXSIndexingResult(self): self._XSIndexingResult = None
    XSIndexingResult = property(getXSIndexingResult, setXSIndexingResult, delXSIndexingResult, "Property for XSIndexingResult")
    def addXSIndexingResult(self, value):
        if value is None:
            strMessage = "ERROR! XSIndexingInput.addXSIndexingResult argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingResult":
            self._XSIndexingResult.append(value)
        else:
            strMessage = "ERROR! XSIndexingInput.addXSIndexingResult argument is not XSIndexingResult but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSIndexingResult(self, index, value):
        if index is None:
            strMessage = "ERROR! XSIndexingInput.insertXSIndexingResult argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSIndexingInput.insertXSIndexingResult argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSIndexingResult":
            self._XSIndexingResult[index] = value
        else:
            strMessage = "ERROR! XSIndexingInput.addXSIndexingResult argument is not XSIndexingResult but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSIndexingInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSIndexingInput'):
        XSData.exportChildren(self, outfile, level, name_)
        for XSSpotSearchOutput_ in self.getXSSpotSearchOutput():
            XSSpotSearchOutput_.export(outfile, level, name_='XSSpotSearchOutput')
        if self.getXSSpotSearchOutput() == []:
            warnEmptyAttribute("XSSpotSearchOutput", "XSSpotSearchOutput")
        for XSIndexingResult_ in self.getXSIndexingResult():
            XSIndexingResult_.export(outfile, level, name_='XSIndexingResult')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSSpotSearchOutput':
            obj_ = XSSpotSearchOutput()
            obj_.build(child_)
            self.XSSpotSearchOutput.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSIndexingResult':
            obj_ = XSIndexingResult()
            obj_.build(child_)
            self.XSIndexingResult.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSIndexingInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSIndexingInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSIndexingInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSIndexingInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSIndexingInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSIndexingInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSIndexingInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSIndexingInput


class XSIndexingSolution(XSData):
    def __init__(self, penalty=None, lattice=None):
        XSData.__init__(self, )
        if lattice is None:
            self._lattice = None
        elif lattice.__class__.__name__ == "XSDataLattice":
            self._lattice = lattice
        else:
            strMessage = "ERROR! XSIndexingSolution constructor argument 'lattice' is not XSDataLattice but %s" % self._lattice.__class__.__name__
            raise BaseException(strMessage)
        if penalty is None:
            self._penalty = None
        elif penalty.__class__.__name__ == "XSDataDouble":
            self._penalty = penalty
        else:
            strMessage = "ERROR! XSIndexingSolution constructor argument 'penalty' is not XSDataDouble but %s" % self._penalty.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lattice' attribute
    def getLattice(self): return self._lattice
    def setLattice(self, lattice):
        if lattice is None:
            self._lattice = None
        elif lattice.__class__.__name__ == "XSDataLattice":
            self._lattice = lattice
        else:
            strMessage = "ERROR! XSIndexingSolution.setLattice argument is not XSDataLattice but %s" % lattice.__class__.__name__
            raise BaseException(strMessage)
    def delLattice(self): self._lattice = None
    lattice = property(getLattice, setLattice, delLattice, "Property for lattice")
    # Methods and properties for the 'penalty' attribute
    def getPenalty(self): return self._penalty
    def setPenalty(self, penalty):
        if penalty is None:
            self._penalty = None
        elif penalty.__class__.__name__ == "XSDataDouble":
            self._penalty = penalty
        else:
            strMessage = "ERROR! XSIndexingSolution.setPenalty argument is not XSDataDouble but %s" % penalty.__class__.__name__
            raise BaseException(strMessage)
    def delPenalty(self): self._penalty = None
    penalty = property(getPenalty, setPenalty, delPenalty, "Property for penalty")
    def export(self, outfile, level, name_='XSIndexingSolution'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSIndexingSolution'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._lattice is not None:
            self.lattice.export(outfile, level, name_='lattice')
        else:
            warnEmptyAttribute("lattice", "XSDataLattice")
        if self._penalty is not None:
            self.penalty.export(outfile, level, name_='penalty')
        else:
            warnEmptyAttribute("penalty", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lattice':
            obj_ = XSDataLattice()
            obj_.build(child_)
            self.setLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'penalty':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPenalty(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSIndexingSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSIndexingSolution' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSIndexingSolution is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSIndexingSolution.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSIndexingSolution()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSIndexingSolution" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSIndexingSolution()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSIndexingSolution


class XSRotationExposure(XSData):
    def __init__(self, XSGoniostatAxis=None, exposuretime=None, numberimages=None, imagewidth=None):
        XSData.__init__(self, )
        if imagewidth is None:
            self._imagewidth = None
        elif imagewidth.__class__.__name__ == "XSDataAngle":
            self._imagewidth = imagewidth
        else:
            strMessage = "ERROR! XSRotationExposure constructor argument 'imagewidth' is not XSDataAngle but %s" % self._imagewidth.__class__.__name__
            raise BaseException(strMessage)
        if numberimages is None:
            self._numberimages = None
        elif numberimages.__class__.__name__ == "XSDataInteger":
            self._numberimages = numberimages
        else:
            strMessage = "ERROR! XSRotationExposure constructor argument 'numberimages' is not XSDataInteger but %s" % self._numberimages.__class__.__name__
            raise BaseException(strMessage)
        if exposuretime is None:
            self._exposuretime = None
        elif exposuretime.__class__.__name__ == "XSDataTime":
            self._exposuretime = exposuretime
        else:
            strMessage = "ERROR! XSRotationExposure constructor argument 'exposuretime' is not XSDataTime but %s" % self._exposuretime.__class__.__name__
            raise BaseException(strMessage)
        if XSGoniostatAxis is None:
            self._XSGoniostatAxis = None
        elif XSGoniostatAxis.__class__.__name__ == "XSGoniostatAxis":
            self._XSGoniostatAxis = XSGoniostatAxis
        else:
            strMessage = "ERROR! XSRotationExposure constructor argument 'XSGoniostatAxis' is not XSGoniostatAxis but %s" % self._XSGoniostatAxis.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imagewidth' attribute
    def getImagewidth(self): return self._imagewidth
    def setImagewidth(self, imagewidth):
        if imagewidth is None:
            self._imagewidth = None
        elif imagewidth.__class__.__name__ == "XSDataAngle":
            self._imagewidth = imagewidth
        else:
            strMessage = "ERROR! XSRotationExposure.setImagewidth argument is not XSDataAngle but %s" % imagewidth.__class__.__name__
            raise BaseException(strMessage)
    def delImagewidth(self): self._imagewidth = None
    imagewidth = property(getImagewidth, setImagewidth, delImagewidth, "Property for imagewidth")
    # Methods and properties for the 'numberimages' attribute
    def getNumberimages(self): return self._numberimages
    def setNumberimages(self, numberimages):
        if numberimages is None:
            self._numberimages = None
        elif numberimages.__class__.__name__ == "XSDataInteger":
            self._numberimages = numberimages
        else:
            strMessage = "ERROR! XSRotationExposure.setNumberimages argument is not XSDataInteger but %s" % numberimages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberimages(self): self._numberimages = None
    numberimages = property(getNumberimages, setNumberimages, delNumberimages, "Property for numberimages")
    # Methods and properties for the 'exposuretime' attribute
    def getExposuretime(self): return self._exposuretime
    def setExposuretime(self, exposuretime):
        if exposuretime is None:
            self._exposuretime = None
        elif exposuretime.__class__.__name__ == "XSDataTime":
            self._exposuretime = exposuretime
        else:
            strMessage = "ERROR! XSRotationExposure.setExposuretime argument is not XSDataTime but %s" % exposuretime.__class__.__name__
            raise BaseException(strMessage)
    def delExposuretime(self): self._exposuretime = None
    exposuretime = property(getExposuretime, setExposuretime, delExposuretime, "Property for exposuretime")
    # Methods and properties for the 'XSGoniostatAxis' attribute
    def getXSGoniostatAxis(self): return self._XSGoniostatAxis
    def setXSGoniostatAxis(self, XSGoniostatAxis):
        if XSGoniostatAxis is None:
            self._XSGoniostatAxis = None
        elif XSGoniostatAxis.__class__.__name__ == "XSGoniostatAxis":
            self._XSGoniostatAxis = XSGoniostatAxis
        else:
            strMessage = "ERROR! XSRotationExposure.setXSGoniostatAxis argument is not XSGoniostatAxis but %s" % XSGoniostatAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSGoniostatAxis(self): self._XSGoniostatAxis = None
    XSGoniostatAxis = property(getXSGoniostatAxis, setXSGoniostatAxis, delXSGoniostatAxis, "Property for XSGoniostatAxis")
    def export(self, outfile, level, name_='XSRotationExposure'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSRotationExposure'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._imagewidth is not None:
            self.imagewidth.export(outfile, level, name_='imagewidth')
        else:
            warnEmptyAttribute("imagewidth", "XSDataAngle")
        if self._numberimages is not None:
            self.numberimages.export(outfile, level, name_='numberimages')
        else:
            warnEmptyAttribute("numberimages", "XSDataInteger")
        if self._exposuretime is not None:
            self.exposuretime.export(outfile, level, name_='exposuretime')
        else:
            warnEmptyAttribute("exposuretime", "XSDataTime")
        if self._XSGoniostatAxis is not None:
            self.XSGoniostatAxis.export(outfile, level, name_='XSGoniostatAxis')
        else:
            warnEmptyAttribute("XSGoniostatAxis", "XSGoniostatAxis")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagewidth':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setImagewidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberimages':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNumberimages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposuretime':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposuretime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSGoniostatAxis':
            obj_ = XSGoniostatAxis()
            obj_.build(child_)
            self.setXSGoniostatAxis(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSRotationExposure" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSRotationExposure' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSRotationExposure is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSRotationExposure.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSRotationExposure()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSRotationExposure" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSRotationExposure()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSRotationExposure


class XSSample(XSData):
    def __init__(self, XSDataCollection=None, identifier=None):
        XSData.__init__(self, )
        if identifier is None:
            self._identifier = None
        elif identifier.__class__.__name__ == "XSDataString":
            self._identifier = identifier
        else:
            strMessage = "ERROR! XSSample constructor argument 'identifier' is not XSDataString but %s" % self._identifier.__class__.__name__
            raise BaseException(strMessage)
        if XSDataCollection is None:
            self._XSDataCollection = []
        elif XSDataCollection.__class__.__name__ == "list":
            self._XSDataCollection = XSDataCollection
        else:
            strMessage = "ERROR! XSSample constructor argument 'XSDataCollection' is not list but %s" % self._XSDataCollection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'identifier' attribute
    def getIdentifier(self): return self._identifier
    def setIdentifier(self, identifier):
        if identifier is None:
            self._identifier = None
        elif identifier.__class__.__name__ == "XSDataString":
            self._identifier = identifier
        else:
            strMessage = "ERROR! XSSample.setIdentifier argument is not XSDataString but %s" % identifier.__class__.__name__
            raise BaseException(strMessage)
    def delIdentifier(self): self._identifier = None
    identifier = property(getIdentifier, setIdentifier, delIdentifier, "Property for identifier")
    # Methods and properties for the 'XSDataCollection' attribute
    def getXSDataCollection(self): return self._XSDataCollection
    def setXSDataCollection(self, XSDataCollection):
        if XSDataCollection is None:
            self._XSDataCollection = []
        elif XSDataCollection.__class__.__name__ == "list":
            self._XSDataCollection = XSDataCollection
        else:
            strMessage = "ERROR! XSSample.setXSDataCollection argument is not list but %s" % XSDataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delXSDataCollection(self): self._XSDataCollection = None
    XSDataCollection = property(getXSDataCollection, setXSDataCollection, delXSDataCollection, "Property for XSDataCollection")
    def addXSDataCollection(self, value):
        if value is None:
            strMessage = "ERROR! XSSample.addXSDataCollection argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataCollection":
            self._XSDataCollection.append(value)
        else:
            strMessage = "ERROR! XSSample.addXSDataCollection argument is not XSDataCollection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDataCollection(self, index, value):
        if index is None:
            strMessage = "ERROR! XSSample.insertXSDataCollection argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSSample.insertXSDataCollection argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataCollection":
            self._XSDataCollection[index] = value
        else:
            strMessage = "ERROR! XSSample.addXSDataCollection argument is not XSDataCollection but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSSample'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._identifier is not None:
            self.identifier.export(outfile, level, name_='identifier')
        else:
            warnEmptyAttribute("identifier", "XSDataString")
        for XSDataCollection_ in self.getXSDataCollection():
            XSDataCollection_.export(outfile, level, name_='XSDataCollection')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'identifier':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIdentifier(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDataCollection':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.XSDataCollection.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSSample


class XSSpotSearchOutput(XSData):
    def __init__(self, XSWedge=None, spots=None):
        XSData.__init__(self, )
        if spots is None:
            self._spots = []
        elif spots.__class__.__name__ == "list":
            self._spots = spots
        else:
            strMessage = "ERROR! XSSpotSearchOutput constructor argument 'spots' is not list but %s" % self._spots.__class__.__name__
            raise BaseException(strMessage)
        if XSWedge is None:
            self._XSWedge = None
        elif XSWedge.__class__.__name__ == "XSWedge":
            self._XSWedge = XSWedge
        else:
            strMessage = "ERROR! XSSpotSearchOutput constructor argument 'XSWedge' is not XSWedge but %s" % self._XSWedge.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spots' attribute
    def getSpots(self): return self._spots
    def setSpots(self, spots):
        if spots is None:
            self._spots = []
        elif spots.__class__.__name__ == "list":
            self._spots = spots
        else:
            strMessage = "ERROR! XSSpotSearchOutput.setSpots argument is not list but %s" % spots.__class__.__name__
            raise BaseException(strMessage)
    def delSpots(self): self._spots = None
    spots = property(getSpots, setSpots, delSpots, "Property for spots")
    def addSpots(self, value):
        if value is None:
            strMessage = "ERROR! XSSpotSearchOutput.addSpots argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSFoundSpot":
            self._spots.append(value)
        else:
            strMessage = "ERROR! XSSpotSearchOutput.addSpots argument is not XSFoundSpot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSpots(self, index, value):
        if index is None:
            strMessage = "ERROR! XSSpotSearchOutput.insertSpots argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSSpotSearchOutput.insertSpots argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSFoundSpot":
            self._spots[index] = value
        else:
            strMessage = "ERROR! XSSpotSearchOutput.addSpots argument is not XSFoundSpot but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSWedge' attribute
    def getXSWedge(self): return self._XSWedge
    def setXSWedge(self, XSWedge):
        if XSWedge is None:
            self._XSWedge = None
        elif XSWedge.__class__.__name__ == "XSWedge":
            self._XSWedge = XSWedge
        else:
            strMessage = "ERROR! XSSpotSearchOutput.setXSWedge argument is not XSWedge but %s" % XSWedge.__class__.__name__
            raise BaseException(strMessage)
    def delXSWedge(self): self._XSWedge = None
    XSWedge = property(getXSWedge, setXSWedge, delXSWedge, "Property for XSWedge")
    def export(self, outfile, level, name_='XSSpotSearchOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSSpotSearchOutput'):
        XSData.exportChildren(self, outfile, level, name_)
        for spots_ in self.getSpots():
            spots_.export(outfile, level, name_='spots')
        if self._XSWedge is not None:
            self.XSWedge.export(outfile, level, name_='XSWedge')
        else:
            warnEmptyAttribute("XSWedge", "XSWedge")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spots':
            obj_ = XSFoundSpot()
            obj_.build(child_)
            self.spots.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSWedge':
            obj_ = XSWedge()
            obj_.build(child_)
            self.setXSWedge(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSSpotSearchOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSSpotSearchOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSSpotSearchOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSSpotSearchOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSSpotSearchOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSSpotSearchOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSSpotSearchOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSSpotSearchOutput


class XSStatisticsIndexing(XSData):
    def __init__(self, spotsused=None, spotstotal=None, spotdeviationpositional=None, spotdeviationangular=None):
        XSData.__init__(self, )
        if spotdeviationangular is None:
            self._spotdeviationangular = None
        elif spotdeviationangular.__class__.__name__ == "XSDataAngle":
            self._spotdeviationangular = spotdeviationangular
        else:
            strMessage = "ERROR! XSStatisticsIndexing constructor argument 'spotdeviationangular' is not XSDataAngle but %s" % self._spotdeviationangular.__class__.__name__
            raise BaseException(strMessage)
        if spotdeviationpositional is None:
            self._spotdeviationpositional = None
        elif spotdeviationpositional.__class__.__name__ == "XSDataLength":
            self._spotdeviationpositional = spotdeviationpositional
        else:
            strMessage = "ERROR! XSStatisticsIndexing constructor argument 'spotdeviationpositional' is not XSDataLength but %s" % self._spotdeviationpositional.__class__.__name__
            raise BaseException(strMessage)
        if spotstotal is None:
            self._spotstotal = None
        elif spotstotal.__class__.__name__ == "XSDataInteger":
            self._spotstotal = spotstotal
        else:
            strMessage = "ERROR! XSStatisticsIndexing constructor argument 'spotstotal' is not XSDataInteger but %s" % self._spotstotal.__class__.__name__
            raise BaseException(strMessage)
        if spotsused is None:
            self._spotsused = None
        elif spotsused.__class__.__name__ == "XSDataInteger":
            self._spotsused = spotsused
        else:
            strMessage = "ERROR! XSStatisticsIndexing constructor argument 'spotsused' is not XSDataInteger but %s" % self._spotsused.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spotdeviationangular' attribute
    def getSpotdeviationangular(self): return self._spotdeviationangular
    def setSpotdeviationangular(self, spotdeviationangular):
        if spotdeviationangular is None:
            self._spotdeviationangular = None
        elif spotdeviationangular.__class__.__name__ == "XSDataAngle":
            self._spotdeviationangular = spotdeviationangular
        else:
            strMessage = "ERROR! XSStatisticsIndexing.setSpotdeviationangular argument is not XSDataAngle but %s" % spotdeviationangular.__class__.__name__
            raise BaseException(strMessage)
    def delSpotdeviationangular(self): self._spotdeviationangular = None
    spotdeviationangular = property(getSpotdeviationangular, setSpotdeviationangular, delSpotdeviationangular, "Property for spotdeviationangular")
    # Methods and properties for the 'spotdeviationpositional' attribute
    def getSpotdeviationpositional(self): return self._spotdeviationpositional
    def setSpotdeviationpositional(self, spotdeviationpositional):
        if spotdeviationpositional is None:
            self._spotdeviationpositional = None
        elif spotdeviationpositional.__class__.__name__ == "XSDataLength":
            self._spotdeviationpositional = spotdeviationpositional
        else:
            strMessage = "ERROR! XSStatisticsIndexing.setSpotdeviationpositional argument is not XSDataLength but %s" % spotdeviationpositional.__class__.__name__
            raise BaseException(strMessage)
    def delSpotdeviationpositional(self): self._spotdeviationpositional = None
    spotdeviationpositional = property(getSpotdeviationpositional, setSpotdeviationpositional, delSpotdeviationpositional, "Property for spotdeviationpositional")
    # Methods and properties for the 'spotstotal' attribute
    def getSpotstotal(self): return self._spotstotal
    def setSpotstotal(self, spotstotal):
        if spotstotal is None:
            self._spotstotal = None
        elif spotstotal.__class__.__name__ == "XSDataInteger":
            self._spotstotal = spotstotal
        else:
            strMessage = "ERROR! XSStatisticsIndexing.setSpotstotal argument is not XSDataInteger but %s" % spotstotal.__class__.__name__
            raise BaseException(strMessage)
    def delSpotstotal(self): self._spotstotal = None
    spotstotal = property(getSpotstotal, setSpotstotal, delSpotstotal, "Property for spotstotal")
    # Methods and properties for the 'spotsused' attribute
    def getSpotsused(self): return self._spotsused
    def setSpotsused(self, spotsused):
        if spotsused is None:
            self._spotsused = None
        elif spotsused.__class__.__name__ == "XSDataInteger":
            self._spotsused = spotsused
        else:
            strMessage = "ERROR! XSStatisticsIndexing.setSpotsused argument is not XSDataInteger but %s" % spotsused.__class__.__name__
            raise BaseException(strMessage)
    def delSpotsused(self): self._spotsused = None
    spotsused = property(getSpotsused, setSpotsused, delSpotsused, "Property for spotsused")
    def export(self, outfile, level, name_='XSStatisticsIndexing'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSStatisticsIndexing'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._spotdeviationangular is not None:
            self.spotdeviationangular.export(outfile, level, name_='spotdeviationangular')
        else:
            warnEmptyAttribute("spotdeviationangular", "XSDataAngle")
        if self._spotdeviationpositional is not None:
            self.spotdeviationpositional.export(outfile, level, name_='spotdeviationpositional')
        else:
            warnEmptyAttribute("spotdeviationpositional", "XSDataLength")
        if self._spotstotal is not None:
            self.spotstotal.export(outfile, level, name_='spotstotal')
        else:
            warnEmptyAttribute("spotstotal", "XSDataInteger")
        if self._spotsused is not None:
            self.spotsused.export(outfile, level, name_='spotsused')
        else:
            warnEmptyAttribute("spotsused", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotdeviationangular':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setSpotdeviationangular(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotdeviationpositional':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setSpotdeviationpositional(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotstotal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpotstotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotsused':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpotsused(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSStatisticsIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSStatisticsIndexing' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSStatisticsIndexing is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSStatisticsIndexing.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSStatisticsIndexing()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSStatisticsIndexing" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSStatisticsIndexing()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSStatisticsIndexing


class XSSubWedge(XSData):
    def __init__(self, XSRotationExposure=None, XSRotationalGoniostatSetting=None, XSImageRange=None, XSDiffractionImages=None, XSDetectorSetting=None, XSCollectionWedge=None, XSBeamSetting=None, imagefilenametemplate=None):
        XSData.__init__(self, )
        if imagefilenametemplate is None:
            self._imagefilenametemplate = None
        elif imagefilenametemplate.__class__.__name__ == "XSDataString":
            self._imagefilenametemplate = imagefilenametemplate
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'imagefilenametemplate' is not XSDataString but %s" % self._imagefilenametemplate.__class__.__name__
            raise BaseException(strMessage)
        if XSBeamSetting is None:
            self._XSBeamSetting = None
        elif XSBeamSetting.__class__.__name__ == "XSBeamSetting":
            self._XSBeamSetting = XSBeamSetting
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSBeamSetting' is not XSBeamSetting but %s" % self._XSBeamSetting.__class__.__name__
            raise BaseException(strMessage)
        if XSCollectionWedge is None:
            self._XSCollectionWedge = None
        elif XSCollectionWedge.__class__.__name__ == "XSCollectionWedge":
            self._XSCollectionWedge = XSCollectionWedge
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSCollectionWedge' is not XSCollectionWedge but %s" % self._XSCollectionWedge.__class__.__name__
            raise BaseException(strMessage)
        if XSDetectorSetting is None:
            self._XSDetectorSetting = None
        elif XSDetectorSetting.__class__.__name__ == "XSDetectorSetting":
            self._XSDetectorSetting = XSDetectorSetting
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSDetectorSetting' is not XSDetectorSetting but %s" % self._XSDetectorSetting.__class__.__name__
            raise BaseException(strMessage)
        if XSDiffractionImages is None:
            self._XSDiffractionImages = []
        elif XSDiffractionImages.__class__.__name__ == "list":
            self._XSDiffractionImages = XSDiffractionImages
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSDiffractionImages' is not list but %s" % self._XSDiffractionImages.__class__.__name__
            raise BaseException(strMessage)
        if XSImageRange is None:
            self._XSImageRange = []
        elif XSImageRange.__class__.__name__ == "list":
            self._XSImageRange = XSImageRange
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSImageRange' is not list but %s" % self._XSImageRange.__class__.__name__
            raise BaseException(strMessage)
        if XSRotationalGoniostatSetting is None:
            self._XSRotationalGoniostatSetting = None
        elif XSRotationalGoniostatSetting.__class__.__name__ == "XSRotationalGoniostatSetting":
            self._XSRotationalGoniostatSetting = XSRotationalGoniostatSetting
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSRotationalGoniostatSetting' is not XSRotationalGoniostatSetting but %s" % self._XSRotationalGoniostatSetting.__class__.__name__
            raise BaseException(strMessage)
        if XSRotationExposure is None:
            self._XSRotationExposure = None
        elif XSRotationExposure.__class__.__name__ == "XSRotationExposure":
            self._XSRotationExposure = XSRotationExposure
        else:
            strMessage = "ERROR! XSSubWedge constructor argument 'XSRotationExposure' is not XSRotationExposure but %s" % self._XSRotationExposure.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imagefilenametemplate' attribute
    def getImagefilenametemplate(self): return self._imagefilenametemplate
    def setImagefilenametemplate(self, imagefilenametemplate):
        if imagefilenametemplate is None:
            self._imagefilenametemplate = None
        elif imagefilenametemplate.__class__.__name__ == "XSDataString":
            self._imagefilenametemplate = imagefilenametemplate
        else:
            strMessage = "ERROR! XSSubWedge.setImagefilenametemplate argument is not XSDataString but %s" % imagefilenametemplate.__class__.__name__
            raise BaseException(strMessage)
    def delImagefilenametemplate(self): self._imagefilenametemplate = None
    imagefilenametemplate = property(getImagefilenametemplate, setImagefilenametemplate, delImagefilenametemplate, "Property for imagefilenametemplate")
    # Methods and properties for the 'XSBeamSetting' attribute
    def getXSBeamSetting(self): return self._XSBeamSetting
    def setXSBeamSetting(self, XSBeamSetting):
        if XSBeamSetting is None:
            self._XSBeamSetting = None
        elif XSBeamSetting.__class__.__name__ == "XSBeamSetting":
            self._XSBeamSetting = XSBeamSetting
        else:
            strMessage = "ERROR! XSSubWedge.setXSBeamSetting argument is not XSBeamSetting but %s" % XSBeamSetting.__class__.__name__
            raise BaseException(strMessage)
    def delXSBeamSetting(self): self._XSBeamSetting = None
    XSBeamSetting = property(getXSBeamSetting, setXSBeamSetting, delXSBeamSetting, "Property for XSBeamSetting")
    # Methods and properties for the 'XSCollectionWedge' attribute
    def getXSCollectionWedge(self): return self._XSCollectionWedge
    def setXSCollectionWedge(self, XSCollectionWedge):
        if XSCollectionWedge is None:
            self._XSCollectionWedge = None
        elif XSCollectionWedge.__class__.__name__ == "XSCollectionWedge":
            self._XSCollectionWedge = XSCollectionWedge
        else:
            strMessage = "ERROR! XSSubWedge.setXSCollectionWedge argument is not XSCollectionWedge but %s" % XSCollectionWedge.__class__.__name__
            raise BaseException(strMessage)
    def delXSCollectionWedge(self): self._XSCollectionWedge = None
    XSCollectionWedge = property(getXSCollectionWedge, setXSCollectionWedge, delXSCollectionWedge, "Property for XSCollectionWedge")
    # Methods and properties for the 'XSDetectorSetting' attribute
    def getXSDetectorSetting(self): return self._XSDetectorSetting
    def setXSDetectorSetting(self, XSDetectorSetting):
        if XSDetectorSetting is None:
            self._XSDetectorSetting = None
        elif XSDetectorSetting.__class__.__name__ == "XSDetectorSetting":
            self._XSDetectorSetting = XSDetectorSetting
        else:
            strMessage = "ERROR! XSSubWedge.setXSDetectorSetting argument is not XSDetectorSetting but %s" % XSDetectorSetting.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetectorSetting(self): self._XSDetectorSetting = None
    XSDetectorSetting = property(getXSDetectorSetting, setXSDetectorSetting, delXSDetectorSetting, "Property for XSDetectorSetting")
    # Methods and properties for the 'XSDiffractionImages' attribute
    def getXSDiffractionImages(self): return self._XSDiffractionImages
    def setXSDiffractionImages(self, XSDiffractionImages):
        if XSDiffractionImages is None:
            self._XSDiffractionImages = []
        elif XSDiffractionImages.__class__.__name__ == "list":
            self._XSDiffractionImages = XSDiffractionImages
        else:
            strMessage = "ERROR! XSSubWedge.setXSDiffractionImages argument is not list but %s" % XSDiffractionImages.__class__.__name__
            raise BaseException(strMessage)
    def delXSDiffractionImages(self): self._XSDiffractionImages = None
    XSDiffractionImages = property(getXSDiffractionImages, setXSDiffractionImages, delXSDiffractionImages, "Property for XSDiffractionImages")
    def addXSDiffractionImages(self, value):
        if value is None:
            strMessage = "ERROR! XSSubWedge.addXSDiffractionImages argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDiffractionImages":
            self._XSDiffractionImages.append(value)
        else:
            strMessage = "ERROR! XSSubWedge.addXSDiffractionImages argument is not XSDiffractionImages but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDiffractionImages(self, index, value):
        if index is None:
            strMessage = "ERROR! XSSubWedge.insertXSDiffractionImages argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSSubWedge.insertXSDiffractionImages argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDiffractionImages":
            self._XSDiffractionImages[index] = value
        else:
            strMessage = "ERROR! XSSubWedge.addXSDiffractionImages argument is not XSDiffractionImages but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSImageRange' attribute
    def getXSImageRange(self): return self._XSImageRange
    def setXSImageRange(self, XSImageRange):
        if XSImageRange is None:
            self._XSImageRange = []
        elif XSImageRange.__class__.__name__ == "list":
            self._XSImageRange = XSImageRange
        else:
            strMessage = "ERROR! XSSubWedge.setXSImageRange argument is not list but %s" % XSImageRange.__class__.__name__
            raise BaseException(strMessage)
    def delXSImageRange(self): self._XSImageRange = None
    XSImageRange = property(getXSImageRange, setXSImageRange, delXSImageRange, "Property for XSImageRange")
    def addXSImageRange(self, value):
        if value is None:
            strMessage = "ERROR! XSSubWedge.addXSImageRange argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSImageRange":
            self._XSImageRange.append(value)
        else:
            strMessage = "ERROR! XSSubWedge.addXSImageRange argument is not XSImageRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSImageRange(self, index, value):
        if index is None:
            strMessage = "ERROR! XSSubWedge.insertXSImageRange argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSSubWedge.insertXSImageRange argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSImageRange":
            self._XSImageRange[index] = value
        else:
            strMessage = "ERROR! XSSubWedge.addXSImageRange argument is not XSImageRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSRotationalGoniostatSetting' attribute
    def getXSRotationalGoniostatSetting(self): return self._XSRotationalGoniostatSetting
    def setXSRotationalGoniostatSetting(self, XSRotationalGoniostatSetting):
        if XSRotationalGoniostatSetting is None:
            self._XSRotationalGoniostatSetting = None
        elif XSRotationalGoniostatSetting.__class__.__name__ == "XSRotationalGoniostatSetting":
            self._XSRotationalGoniostatSetting = XSRotationalGoniostatSetting
        else:
            strMessage = "ERROR! XSSubWedge.setXSRotationalGoniostatSetting argument is not XSRotationalGoniostatSetting but %s" % XSRotationalGoniostatSetting.__class__.__name__
            raise BaseException(strMessage)
    def delXSRotationalGoniostatSetting(self): self._XSRotationalGoniostatSetting = None
    XSRotationalGoniostatSetting = property(getXSRotationalGoniostatSetting, setXSRotationalGoniostatSetting, delXSRotationalGoniostatSetting, "Property for XSRotationalGoniostatSetting")
    # Methods and properties for the 'XSRotationExposure' attribute
    def getXSRotationExposure(self): return self._XSRotationExposure
    def setXSRotationExposure(self, XSRotationExposure):
        if XSRotationExposure is None:
            self._XSRotationExposure = None
        elif XSRotationExposure.__class__.__name__ == "XSRotationExposure":
            self._XSRotationExposure = XSRotationExposure
        else:
            strMessage = "ERROR! XSSubWedge.setXSRotationExposure argument is not XSRotationExposure but %s" % XSRotationExposure.__class__.__name__
            raise BaseException(strMessage)
    def delXSRotationExposure(self): self._XSRotationExposure = None
    XSRotationExposure = property(getXSRotationExposure, setXSRotationExposure, delXSRotationExposure, "Property for XSRotationExposure")
    def export(self, outfile, level, name_='XSSubWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSSubWedge'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._imagefilenametemplate is not None:
            self.imagefilenametemplate.export(outfile, level, name_='imagefilenametemplate')
        else:
            warnEmptyAttribute("imagefilenametemplate", "XSDataString")
        if self._XSBeamSetting is not None:
            self.XSBeamSetting.export(outfile, level, name_='XSBeamSetting')
        else:
            warnEmptyAttribute("XSBeamSetting", "XSBeamSetting")
        if self._XSCollectionWedge is not None:
            self.XSCollectionWedge.export(outfile, level, name_='XSCollectionWedge')
        else:
            warnEmptyAttribute("XSCollectionWedge", "XSCollectionWedge")
        if self._XSDetectorSetting is not None:
            self.XSDetectorSetting.export(outfile, level, name_='XSDetectorSetting')
        else:
            warnEmptyAttribute("XSDetectorSetting", "XSDetectorSetting")
        for XSDiffractionImages_ in self.getXSDiffractionImages():
            XSDiffractionImages_.export(outfile, level, name_='XSDiffractionImages')
        for XSImageRange_ in self.getXSImageRange():
            XSImageRange_.export(outfile, level, name_='XSImageRange')
        if self._XSRotationalGoniostatSetting is not None:
            self.XSRotationalGoniostatSetting.export(outfile, level, name_='XSRotationalGoniostatSetting')
        else:
            warnEmptyAttribute("XSRotationalGoniostatSetting", "XSRotationalGoniostatSetting")
        if self._XSRotationExposure is not None:
            self.XSRotationExposure.export(outfile, level, name_='XSRotationExposure')
        else:
            warnEmptyAttribute("XSRotationExposure", "XSRotationExposure")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagefilenametemplate':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImagefilenametemplate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSBeamSetting':
            obj_ = XSBeamSetting()
            obj_.build(child_)
            self.setXSBeamSetting(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSCollectionWedge':
            obj_ = XSCollectionWedge()
            obj_.build(child_)
            self.setXSCollectionWedge(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetectorSetting':
            obj_ = XSDetectorSetting()
            obj_.build(child_)
            self.setXSDetectorSetting(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDiffractionImages':
            obj_ = XSDiffractionImages()
            obj_.build(child_)
            self.XSDiffractionImages.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSImageRange':
            obj_ = XSImageRange()
            obj_.build(child_)
            self.XSImageRange.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSRotationalGoniostatSetting':
            obj_ = XSRotationalGoniostatSetting()
            obj_.build(child_)
            self.setXSRotationalGoniostatSetting(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSRotationExposure':
            obj_ = XSRotationExposure()
            obj_.build(child_)
            self.setXSRotationExposure(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSSubWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSSubWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSSubWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSSubWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSSubWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSSubWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSSubWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSSubWedge


class XSWedge(XSData):
    def __init__(self, ednaid=None):
        XSData.__init__(self, )
        if ednaid is None:
            self._ednaid = None
        elif ednaid.__class__.__name__ == "XSDataString":
            self._ednaid = ednaid
        else:
            strMessage = "ERROR! XSWedge constructor argument 'ednaid' is not XSDataString but %s" % self._ednaid.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'ednaid' attribute
    def getEdnaid(self): return self._ednaid
    def setEdnaid(self, ednaid):
        if ednaid is None:
            self._ednaid = None
        elif ednaid.__class__.__name__ == "XSDataString":
            self._ednaid = ednaid
        else:
            strMessage = "ERROR! XSWedge.setEdnaid argument is not XSDataString but %s" % ednaid.__class__.__name__
            raise BaseException(strMessage)
    def delEdnaid(self): self._ednaid = None
    ednaid = property(getEdnaid, setEdnaid, delEdnaid, "Property for ednaid")
    def export(self, outfile, level, name_='XSWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSWedge'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._ednaid is not None:
            self.ednaid.export(outfile, level, name_='ednaid')
        else:
            warnEmptyAttribute("ednaid", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ednaid':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setEdnaid(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSWedge


class XSIndexingOutput(XSData):
    def __init__(self, XSWedge=None, refinedaxisdirection=None, statistics=None):
        XSData.__init__(self, )
        if statistics is None:
            self._statistics = None
        elif statistics.__class__.__name__ == "XSStatisticsIndexing":
            self._statistics = statistics
        else:
            strMessage = "ERROR! XSIndexingOutput constructor argument 'statistics' is not XSStatisticsIndexing but %s" % self._statistics.__class__.__name__
            raise BaseException(strMessage)
        if refinedaxisdirection is None:
            self._refinedaxisdirection = None
        elif refinedaxisdirection.__class__.__name__ == "XSDataUnitVector":
            self._refinedaxisdirection = refinedaxisdirection
        else:
            strMessage = "ERROR! XSIndexingOutput constructor argument 'refinedaxisdirection' is not XSDataUnitVector but %s" % self._refinedaxisdirection.__class__.__name__
            raise BaseException(strMessage)
        if XSWedge is None:
            self._XSWedge = None
        elif XSWedge.__class__.__name__ == "XSWedge":
            self._XSWedge = XSWedge
        else:
            strMessage = "ERROR! XSIndexingOutput constructor argument 'XSWedge' is not XSWedge but %s" % self._XSWedge.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'statistics' attribute
    def getStatistics(self): return self._statistics
    def setStatistics(self, statistics):
        if statistics is None:
            self._statistics = None
        elif statistics.__class__.__name__ == "XSStatisticsIndexing":
            self._statistics = statistics
        else:
            strMessage = "ERROR! XSIndexingOutput.setStatistics argument is not XSStatisticsIndexing but %s" % statistics.__class__.__name__
            raise BaseException(strMessage)
    def delStatistics(self): self._statistics = None
    statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
    # Methods and properties for the 'refinedaxisdirection' attribute
    def getRefinedaxisdirection(self): return self._refinedaxisdirection
    def setRefinedaxisdirection(self, refinedaxisdirection):
        if refinedaxisdirection is None:
            self._refinedaxisdirection = None
        elif refinedaxisdirection.__class__.__name__ == "XSDataUnitVector":
            self._refinedaxisdirection = refinedaxisdirection
        else:
            strMessage = "ERROR! XSIndexingOutput.setRefinedaxisdirection argument is not XSDataUnitVector but %s" % refinedaxisdirection.__class__.__name__
            raise BaseException(strMessage)
    def delRefinedaxisdirection(self): self._refinedaxisdirection = None
    refinedaxisdirection = property(getRefinedaxisdirection, setRefinedaxisdirection, delRefinedaxisdirection, "Property for refinedaxisdirection")
    # Methods and properties for the 'XSWedge' attribute
    def getXSWedge(self): return self._XSWedge
    def setXSWedge(self, XSWedge):
        if XSWedge is None:
            self._XSWedge = None
        elif XSWedge.__class__.__name__ == "XSWedge":
            self._XSWedge = XSWedge
        else:
            strMessage = "ERROR! XSIndexingOutput.setXSWedge argument is not XSWedge but %s" % XSWedge.__class__.__name__
            raise BaseException(strMessage)
    def delXSWedge(self): self._XSWedge = None
    XSWedge = property(getXSWedge, setXSWedge, delXSWedge, "Property for XSWedge")
    def export(self, outfile, level, name_='XSIndexingOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSIndexingOutput'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._statistics is not None:
            self.statistics.export(outfile, level, name_='statistics')
        if self._refinedaxisdirection is not None:
            self.refinedaxisdirection.export(outfile, level, name_='refinedaxisdirection')
        if self._XSWedge is not None:
            self.XSWedge.export(outfile, level, name_='XSWedge')
        else:
            warnEmptyAttribute("XSWedge", "XSWedge")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statistics':
            obj_ = XSStatisticsIndexing()
            obj_.build(child_)
            self.setStatistics(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refinedaxisdirection':
            obj_ = XSDataUnitVector()
            obj_.build(child_)
            self.setRefinedaxisdirection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSWedge':
            obj_ = XSWedge()
            obj_.build(child_)
            self.setXSWedge(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSIndexingOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSIndexingOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSIndexingOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSIndexingOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSIndexingOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSIndexingOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSIndexingOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSIndexingOutput


class XSCollectionWedge(XSWedge):
    def __init__(self, ednaid=None):
        XSWedge.__init__(self, ednaid)
    def export(self, outfile, level, name_='XSCollectionWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSCollectionWedge'):
        XSWedge.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSWedge.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSCollectionWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSCollectionWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSCollectionWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSCollectionWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSCollectionWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSCollectionWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSCollectionWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSCollectionWedge


class XSDataInputCharacterisationv2_0(XSDataInput):
    def __init__(self, configuration=None, possibleOrientations=None, mxv2DataCollection_Reference=None, mxv2DataCollection=None, mxv1ResultCharacterisation_Reference=None, mxv1InputCharacterisation=None):
        XSDataInput.__init__(self, configuration)
        if mxv1InputCharacterisation is None:
            self._mxv1InputCharacterisation = None
        elif mxv1InputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._mxv1InputCharacterisation = mxv1InputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0 constructor argument 'mxv1InputCharacterisation' is not XSDataInputCharacterisation but %s" % self._mxv1InputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0 constructor argument 'mxv1ResultCharacterisation_Reference' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0 constructor argument 'mxv2DataCollection' is not XSDataCollection but %s" % self._mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0 constructor argument 'mxv2DataCollection_Reference' is not XSDataCollection but %s" % self._mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0 constructor argument 'possibleOrientations' is not kappa_alignment_response but %s" % self._possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mxv1InputCharacterisation' attribute
    def getMxv1InputCharacterisation(self): return self._mxv1InputCharacterisation
    def setMxv1InputCharacterisation(self, mxv1InputCharacterisation):
        if mxv1InputCharacterisation is None:
            self._mxv1InputCharacterisation = None
        elif mxv1InputCharacterisation.__class__.__name__ == "XSDataInputCharacterisation":
            self._mxv1InputCharacterisation = mxv1InputCharacterisation
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0.setMxv1InputCharacterisation argument is not XSDataInputCharacterisation but %s" % mxv1InputCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1InputCharacterisation(self): self._mxv1InputCharacterisation = None
    mxv1InputCharacterisation = property(getMxv1InputCharacterisation, setMxv1InputCharacterisation, delMxv1InputCharacterisation, "Property for mxv1InputCharacterisation")
    # Methods and properties for the 'mxv1ResultCharacterisation_Reference' attribute
    def getMxv1ResultCharacterisation_Reference(self): return self._mxv1ResultCharacterisation_Reference
    def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0.setMxv1ResultCharacterisation_Reference argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation_Reference(self): self._mxv1ResultCharacterisation_Reference = None
    mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
    # Methods and properties for the 'mxv2DataCollection' attribute
    def getMxv2DataCollection(self): return self._mxv2DataCollection
    def setMxv2DataCollection(self, mxv2DataCollection):
        if mxv2DataCollection is None:
            self._mxv2DataCollection = None
        elif mxv2DataCollection.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection = mxv2DataCollection
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0.setMxv2DataCollection argument is not XSDataCollection but %s" % mxv2DataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection(self): self._mxv2DataCollection = None
    mxv2DataCollection = property(getMxv2DataCollection, setMxv2DataCollection, delMxv2DataCollection, "Property for mxv2DataCollection")
    # Methods and properties for the 'mxv2DataCollection_Reference' attribute
    def getMxv2DataCollection_Reference(self): return self._mxv2DataCollection_Reference
    def setMxv2DataCollection_Reference(self, mxv2DataCollection_Reference):
        if mxv2DataCollection_Reference is None:
            self._mxv2DataCollection_Reference = None
        elif mxv2DataCollection_Reference.__class__.__name__ == "XSDataCollection":
            self._mxv2DataCollection_Reference = mxv2DataCollection_Reference
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0.setMxv2DataCollection_Reference argument is not XSDataCollection but %s" % mxv2DataCollection_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv2DataCollection_Reference(self): self._mxv2DataCollection_Reference = None
    mxv2DataCollection_Reference = property(getMxv2DataCollection_Reference, setMxv2DataCollection_Reference, delMxv2DataCollection_Reference, "Property for mxv2DataCollection_Reference")
    # Methods and properties for the 'possibleOrientations' attribute
    def getPossibleOrientations(self): return self._possibleOrientations
    def setPossibleOrientations(self, possibleOrientations):
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataInputCharacterisationv2_0.setPossibleOrientations argument is not kappa_alignment_response but %s" % possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    def delPossibleOrientations(self): self._possibleOrientations = None
    possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
    def export(self, outfile, level, name_='XSDataInputCharacterisationv2_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputCharacterisationv2_0'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._mxv1InputCharacterisation is not None:
            self.mxv1InputCharacterisation.export(outfile, level, name_='mxv1InputCharacterisation')
        else:
            warnEmptyAttribute("mxv1InputCharacterisation", "XSDataInputCharacterisation")
        if self._mxv1ResultCharacterisation_Reference is not None:
            self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
        if self._mxv2DataCollection is not None:
            self.mxv2DataCollection.export(outfile, level, name_='mxv2DataCollection')
        if self._mxv2DataCollection_Reference is not None:
            self.mxv2DataCollection_Reference.export(outfile, level, name_='mxv2DataCollection_Reference')
        if self._possibleOrientations is not None:
            self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1InputCharacterisation':
            obj_ = XSDataInputCharacterisation()
            obj_.build(child_)
            self.setMxv1InputCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation_Reference':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv2DataCollection_Reference':
            obj_ = XSDataCollection()
            obj_.build(child_)
            self.setMxv2DataCollection_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possibleOrientations':
            obj_ = kappa_alignment_response()
            obj_.build(child_)
            self.setPossibleOrientations(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputCharacterisationv2_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputCharacterisationv2_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputCharacterisationv2_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputCharacterisationv2_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputCharacterisationv2_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputCharacterisationv2_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputCharacterisationv2_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputCharacterisationv2_0


class XSDataResultCharacterisationv2_0(XSDataResult):
    def __init__(self, status=None, possibleOrientations=None, suggestedStrategy=None, mxv1ResultCharacterisation_Reference=None, mxv1ResultCharacterisation=None):
        XSDataResult.__init__(self, status)
        if mxv1ResultCharacterisation is None:
            self._mxv1ResultCharacterisation = None
        elif mxv1ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation = mxv1ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0 constructor argument 'mxv1ResultCharacterisation' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0 constructor argument 'mxv1ResultCharacterisation_Reference' is not XSDataResultCharacterisation but %s" % self._mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
        if suggestedStrategy is None:
            self._suggestedStrategy = None
        elif suggestedStrategy.__class__.__name__ == "XSDataResultStrategy":
            self._suggestedStrategy = suggestedStrategy
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0 constructor argument 'suggestedStrategy' is not XSDataResultStrategy but %s" % self._suggestedStrategy.__class__.__name__
            raise BaseException(strMessage)
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0 constructor argument 'possibleOrientations' is not kappa_alignment_response but %s" % self._possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mxv1ResultCharacterisation' attribute
    def getMxv1ResultCharacterisation(self): return self._mxv1ResultCharacterisation
    def setMxv1ResultCharacterisation(self, mxv1ResultCharacterisation):
        if mxv1ResultCharacterisation is None:
            self._mxv1ResultCharacterisation = None
        elif mxv1ResultCharacterisation.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation = mxv1ResultCharacterisation
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0.setMxv1ResultCharacterisation argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation(self): self._mxv1ResultCharacterisation = None
    mxv1ResultCharacterisation = property(getMxv1ResultCharacterisation, setMxv1ResultCharacterisation, delMxv1ResultCharacterisation, "Property for mxv1ResultCharacterisation")
    # Methods and properties for the 'mxv1ResultCharacterisation_Reference' attribute
    def getMxv1ResultCharacterisation_Reference(self): return self._mxv1ResultCharacterisation_Reference
    def setMxv1ResultCharacterisation_Reference(self, mxv1ResultCharacterisation_Reference):
        if mxv1ResultCharacterisation_Reference is None:
            self._mxv1ResultCharacterisation_Reference = None
        elif mxv1ResultCharacterisation_Reference.__class__.__name__ == "XSDataResultCharacterisation":
            self._mxv1ResultCharacterisation_Reference = mxv1ResultCharacterisation_Reference
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0.setMxv1ResultCharacterisation_Reference argument is not XSDataResultCharacterisation but %s" % mxv1ResultCharacterisation_Reference.__class__.__name__
            raise BaseException(strMessage)
    def delMxv1ResultCharacterisation_Reference(self): self._mxv1ResultCharacterisation_Reference = None
    mxv1ResultCharacterisation_Reference = property(getMxv1ResultCharacterisation_Reference, setMxv1ResultCharacterisation_Reference, delMxv1ResultCharacterisation_Reference, "Property for mxv1ResultCharacterisation_Reference")
    # Methods and properties for the 'suggestedStrategy' attribute
    def getSuggestedStrategy(self): return self._suggestedStrategy
    def setSuggestedStrategy(self, suggestedStrategy):
        if suggestedStrategy is None:
            self._suggestedStrategy = None
        elif suggestedStrategy.__class__.__name__ == "XSDataResultStrategy":
            self._suggestedStrategy = suggestedStrategy
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0.setSuggestedStrategy argument is not XSDataResultStrategy but %s" % suggestedStrategy.__class__.__name__
            raise BaseException(strMessage)
    def delSuggestedStrategy(self): self._suggestedStrategy = None
    suggestedStrategy = property(getSuggestedStrategy, setSuggestedStrategy, delSuggestedStrategy, "Property for suggestedStrategy")
    # Methods and properties for the 'possibleOrientations' attribute
    def getPossibleOrientations(self): return self._possibleOrientations
    def setPossibleOrientations(self, possibleOrientations):
        if possibleOrientations is None:
            self._possibleOrientations = None
        elif possibleOrientations.__class__.__name__ == "kappa_alignment_response":
            self._possibleOrientations = possibleOrientations
        else:
            strMessage = "ERROR! XSDataResultCharacterisationv2_0.setPossibleOrientations argument is not kappa_alignment_response but %s" % possibleOrientations.__class__.__name__
            raise BaseException(strMessage)
    def delPossibleOrientations(self): self._possibleOrientations = None
    possibleOrientations = property(getPossibleOrientations, setPossibleOrientations, delPossibleOrientations, "Property for possibleOrientations")
    def export(self, outfile, level, name_='XSDataResultCharacterisationv2_0'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultCharacterisationv2_0'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._mxv1ResultCharacterisation is not None:
            self.mxv1ResultCharacterisation.export(outfile, level, name_='mxv1ResultCharacterisation')
        else:
            warnEmptyAttribute("mxv1ResultCharacterisation", "XSDataResultCharacterisation")
        if self._mxv1ResultCharacterisation_Reference is not None:
            self.mxv1ResultCharacterisation_Reference.export(outfile, level, name_='mxv1ResultCharacterisation_Reference')
        if self._suggestedStrategy is not None:
            self.suggestedStrategy.export(outfile, level, name_='suggestedStrategy')
        if self._possibleOrientations is not None:
            self.possibleOrientations.export(outfile, level, name_='possibleOrientations')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mxv1ResultCharacterisation_Reference':
            obj_ = XSDataResultCharacterisation()
            obj_.build(child_)
            self.setMxv1ResultCharacterisation_Reference(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'suggestedStrategy':
            obj_ = XSDataResultStrategy()
            obj_.build(child_)
            self.setSuggestedStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possibleOrientations':
            obj_ = kappa_alignment_response()
            obj_.build(child_)
            self.setPossibleOrientations(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultCharacterisationv2_0" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultCharacterisationv2_0' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultCharacterisationv2_0 is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultCharacterisationv2_0.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultCharacterisationv2_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultCharacterisationv2_0" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultCharacterisationv2_0()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultCharacterisationv2_0


class XSDetectorAxis(XSDisplacementAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
        XSDisplacementAxis.__init__(self, XSCalibratedDisplacementAxis, name)
    def export(self, outfile, level, name_='XSDetectorAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorAxis'):
        XSDisplacementAxis.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDisplacementAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorAxis


class XSDetector(XSDisplacementList):
    def __init__(self, XSDetectorAxis=None, XSDetectorFaceAxis=None, profileerror=None, background=None, darkcurrent=None, switchingplatetime=None, readouttime=None, radius=None, shape=None, name=None):
        XSDisplacementList.__init__(self, )
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDetector constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
        if shape is None:
            self._shape = None
        elif shape.__class__.__name__ == "XSDataString":
            self._shape = shape
        else:
            strMessage = "ERROR! XSDetector constructor argument 'shape' is not XSDataString but %s" % self._shape.__class__.__name__
            raise BaseException(strMessage)
        if radius is None:
            self._radius = None
        elif radius.__class__.__name__ == "XSDataDouble":
            self._radius = radius
        else:
            strMessage = "ERROR! XSDetector constructor argument 'radius' is not XSDataDouble but %s" % self._radius.__class__.__name__
            raise BaseException(strMessage)
        if readouttime is None:
            self._readouttime = None
        elif readouttime.__class__.__name__ == "XSDataDouble":
            self._readouttime = readouttime
        else:
            strMessage = "ERROR! XSDetector constructor argument 'readouttime' is not XSDataDouble but %s" % self._readouttime.__class__.__name__
            raise BaseException(strMessage)
        if switchingplatetime is None:
            self._switchingplatetime = None
        elif switchingplatetime.__class__.__name__ == "XSDataDouble":
            self._switchingplatetime = switchingplatetime
        else:
            strMessage = "ERROR! XSDetector constructor argument 'switchingplatetime' is not XSDataDouble but %s" % self._switchingplatetime.__class__.__name__
            raise BaseException(strMessage)
        if darkcurrent is None:
            self._darkcurrent = None
        elif darkcurrent.__class__.__name__ == "XSDataVectorDouble":
            self._darkcurrent = darkcurrent
        else:
            strMessage = "ERROR! XSDetector constructor argument 'darkcurrent' is not XSDataVectorDouble but %s" % self._darkcurrent.__class__.__name__
            raise BaseException(strMessage)
        if background is None:
            self._background = None
        elif background.__class__.__name__ == "XSDataDouble":
            self._background = background
        else:
            strMessage = "ERROR! XSDetector constructor argument 'background' is not XSDataDouble but %s" % self._background.__class__.__name__
            raise BaseException(strMessage)
        if profileerror is None:
            self._profileerror = None
        elif profileerror.__class__.__name__ == "XSDataDouble":
            self._profileerror = profileerror
        else:
            strMessage = "ERROR! XSDetector constructor argument 'profileerror' is not XSDataDouble but %s" % self._profileerror.__class__.__name__
            raise BaseException(strMessage)
        if XSDetectorFaceAxis is None:
            self._XSDetectorFaceAxis = []
        elif XSDetectorFaceAxis.__class__.__name__ == "list":
            self._XSDetectorFaceAxis = XSDetectorFaceAxis
        else:
            strMessage = "ERROR! XSDetector constructor argument 'XSDetectorFaceAxis' is not list but %s" % self._XSDetectorFaceAxis.__class__.__name__
            raise BaseException(strMessage)
        if XSDetectorAxis is None:
            self._XSDetectorAxis = []
        elif XSDetectorAxis.__class__.__name__ == "list":
            self._XSDetectorAxis = XSDetectorAxis
        else:
            strMessage = "ERROR! XSDetector constructor argument 'XSDetectorAxis' is not list but %s" % self._XSDetectorAxis.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDetector.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    # Methods and properties for the 'shape' attribute
    def getShape(self): return self._shape
    def setShape(self, shape):
        if shape is None:
            self._shape = None
        elif shape.__class__.__name__ == "XSDataString":
            self._shape = shape
        else:
            strMessage = "ERROR! XSDetector.setShape argument is not XSDataString but %s" % shape.__class__.__name__
            raise BaseException(strMessage)
    def delShape(self): self._shape = None
    shape = property(getShape, setShape, delShape, "Property for shape")
    # Methods and properties for the 'radius' attribute
    def getRadius(self): return self._radius
    def setRadius(self, radius):
        if radius is None:
            self._radius = None
        elif radius.__class__.__name__ == "XSDataDouble":
            self._radius = radius
        else:
            strMessage = "ERROR! XSDetector.setRadius argument is not XSDataDouble but %s" % radius.__class__.__name__
            raise BaseException(strMessage)
    def delRadius(self): self._radius = None
    radius = property(getRadius, setRadius, delRadius, "Property for radius")
    # Methods and properties for the 'readouttime' attribute
    def getReadouttime(self): return self._readouttime
    def setReadouttime(self, readouttime):
        if readouttime is None:
            self._readouttime = None
        elif readouttime.__class__.__name__ == "XSDataDouble":
            self._readouttime = readouttime
        else:
            strMessage = "ERROR! XSDetector.setReadouttime argument is not XSDataDouble but %s" % readouttime.__class__.__name__
            raise BaseException(strMessage)
    def delReadouttime(self): self._readouttime = None
    readouttime = property(getReadouttime, setReadouttime, delReadouttime, "Property for readouttime")
    # Methods and properties for the 'switchingplatetime' attribute
    def getSwitchingplatetime(self): return self._switchingplatetime
    def setSwitchingplatetime(self, switchingplatetime):
        if switchingplatetime is None:
            self._switchingplatetime = None
        elif switchingplatetime.__class__.__name__ == "XSDataDouble":
            self._switchingplatetime = switchingplatetime
        else:
            strMessage = "ERROR! XSDetector.setSwitchingplatetime argument is not XSDataDouble but %s" % switchingplatetime.__class__.__name__
            raise BaseException(strMessage)
    def delSwitchingplatetime(self): self._switchingplatetime = None
    switchingplatetime = property(getSwitchingplatetime, setSwitchingplatetime, delSwitchingplatetime, "Property for switchingplatetime")
    # Methods and properties for the 'darkcurrent' attribute
    def getDarkcurrent(self): return self._darkcurrent
    def setDarkcurrent(self, darkcurrent):
        if darkcurrent is None:
            self._darkcurrent = None
        elif darkcurrent.__class__.__name__ == "XSDataVectorDouble":
            self._darkcurrent = darkcurrent
        else:
            strMessage = "ERROR! XSDetector.setDarkcurrent argument is not XSDataVectorDouble but %s" % darkcurrent.__class__.__name__
            raise BaseException(strMessage)
    def delDarkcurrent(self): self._darkcurrent = None
    darkcurrent = property(getDarkcurrent, setDarkcurrent, delDarkcurrent, "Property for darkcurrent")
    # Methods and properties for the 'background' attribute
    def getBackground(self): return self._background
    def setBackground(self, background):
        if background is None:
            self._background = None
        elif background.__class__.__name__ == "XSDataDouble":
            self._background = background
        else:
            strMessage = "ERROR! XSDetector.setBackground argument is not XSDataDouble but %s" % background.__class__.__name__
            raise BaseException(strMessage)
    def delBackground(self): self._background = None
    background = property(getBackground, setBackground, delBackground, "Property for background")
    # Methods and properties for the 'profileerror' attribute
    def getProfileerror(self): return self._profileerror
    def setProfileerror(self, profileerror):
        if profileerror is None:
            self._profileerror = None
        elif profileerror.__class__.__name__ == "XSDataDouble":
            self._profileerror = profileerror
        else:
            strMessage = "ERROR! XSDetector.setProfileerror argument is not XSDataDouble but %s" % profileerror.__class__.__name__
            raise BaseException(strMessage)
    def delProfileerror(self): self._profileerror = None
    profileerror = property(getProfileerror, setProfileerror, delProfileerror, "Property for profileerror")
    # Methods and properties for the 'XSDetectorFaceAxis' attribute
    def getXSDetectorFaceAxis(self): return self._XSDetectorFaceAxis
    def setXSDetectorFaceAxis(self, XSDetectorFaceAxis):
        if XSDetectorFaceAxis is None:
            self._XSDetectorFaceAxis = []
        elif XSDetectorFaceAxis.__class__.__name__ == "list":
            self._XSDetectorFaceAxis = XSDetectorFaceAxis
        else:
            strMessage = "ERROR! XSDetector.setXSDetectorFaceAxis argument is not list but %s" % XSDetectorFaceAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetectorFaceAxis(self): self._XSDetectorFaceAxis = None
    XSDetectorFaceAxis = property(getXSDetectorFaceAxis, setXSDetectorFaceAxis, delXSDetectorFaceAxis, "Property for XSDetectorFaceAxis")
    def addXSDetectorFaceAxis(self, value):
        if value is None:
            strMessage = "ERROR! XSDetector.addXSDetectorFaceAxis argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxis":
            self._XSDetectorFaceAxis.append(value)
        else:
            strMessage = "ERROR! XSDetector.addXSDetectorFaceAxis argument is not XSDetectorFaceAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDetectorFaceAxis(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDetector.insertXSDetectorFaceAxis argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDetector.insertXSDetectorFaceAxis argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorFaceAxis":
            self._XSDetectorFaceAxis[index] = value
        else:
            strMessage = "ERROR! XSDetector.addXSDetectorFaceAxis argument is not XSDetectorFaceAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSDetectorAxis' attribute
    def getXSDetectorAxis(self): return self._XSDetectorAxis
    def setXSDetectorAxis(self, XSDetectorAxis):
        if XSDetectorAxis is None:
            self._XSDetectorAxis = []
        elif XSDetectorAxis.__class__.__name__ == "list":
            self._XSDetectorAxis = XSDetectorAxis
        else:
            strMessage = "ERROR! XSDetector.setXSDetectorAxis argument is not list but %s" % XSDetectorAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetectorAxis(self): self._XSDetectorAxis = None
    XSDetectorAxis = property(getXSDetectorAxis, setXSDetectorAxis, delXSDetectorAxis, "Property for XSDetectorAxis")
    def addXSDetectorAxis(self, value):
        if value is None:
            strMessage = "ERROR! XSDetector.addXSDetectorAxis argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorAxis":
            self._XSDetectorAxis.append(value)
        else:
            strMessage = "ERROR! XSDetector.addXSDetectorAxis argument is not XSDetectorAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSDetectorAxis(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDetector.insertXSDetectorAxis argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDetector.insertXSDetectorAxis argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDetectorAxis":
            self._XSDetectorAxis[index] = value
        else:
            strMessage = "ERROR! XSDetector.addXSDetectorAxis argument is not XSDetectorAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDetector'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetector'):
        XSDisplacementList.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        else:
            warnEmptyAttribute("name", "XSDataString")
        if self._shape is not None:
            self.shape.export(outfile, level, name_='shape')
        else:
            warnEmptyAttribute("shape", "XSDataString")
        if self._radius is not None:
            self.radius.export(outfile, level, name_='radius')
        else:
            warnEmptyAttribute("radius", "XSDataDouble")
        if self._readouttime is not None:
            self.readouttime.export(outfile, level, name_='readouttime')
        else:
            warnEmptyAttribute("readouttime", "XSDataDouble")
        if self._switchingplatetime is not None:
            self.switchingplatetime.export(outfile, level, name_='switchingplatetime')
        else:
            warnEmptyAttribute("switchingplatetime", "XSDataDouble")
        if self._darkcurrent is not None:
            self.darkcurrent.export(outfile, level, name_='darkcurrent')
        else:
            warnEmptyAttribute("darkcurrent", "XSDataVectorDouble")
        if self._background is not None:
            self.background.export(outfile, level, name_='background')
        else:
            warnEmptyAttribute("background", "XSDataDouble")
        if self._profileerror is not None:
            self.profileerror.export(outfile, level, name_='profileerror')
        else:
            warnEmptyAttribute("profileerror", "XSDataDouble")
        for XSDetectorFaceAxis_ in self.getXSDetectorFaceAxis():
            XSDetectorFaceAxis_.export(outfile, level, name_='XSDetectorFaceAxis')
        if self.getXSDetectorFaceAxis() == []:
            warnEmptyAttribute("XSDetectorFaceAxis", "XSDetectorFaceAxis")
        for XSDetectorAxis_ in self.getXSDetectorAxis():
            XSDetectorAxis_.export(outfile, level, name_='XSDetectorAxis')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shape':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radius':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadius(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'readouttime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setReadouttime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'switchingplatetime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSwitchingplatetime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'darkcurrent':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDarkcurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'background':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBackground(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'profileerror':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setProfileerror(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetectorFaceAxis':
            obj_ = XSDetectorFaceAxis()
            obj_.build(child_)
            self.XSDetectorFaceAxis.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetectorAxis':
            obj_ = XSDetectorAxis()
            obj_.build(child_)
            self.XSDetectorAxis.append(obj_)
        XSDisplacementList.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetector' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetector is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetector.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetector()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetector" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetector()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetector


class XSDetectorSetting(XSDisplacementListSetting):
    def __init__(self, XSDetector=None, axissetting=None):
        XSDisplacementListSetting.__init__(self, )
        if axissetting is None:
            self._axissetting = []
        elif axissetting.__class__.__name__ == "list":
            self._axissetting = axissetting
        else:
            strMessage = "ERROR! XSDetectorSetting constructor argument 'axissetting' is not list but %s" % self._axissetting.__class__.__name__
            raise BaseException(strMessage)
        if XSDetector is None:
            self._XSDetector = None
        elif XSDetector.__class__.__name__ == "XSDetector":
            self._XSDetector = XSDetector
        else:
            strMessage = "ERROR! XSDetectorSetting constructor argument 'XSDetector' is not XSDetector but %s" % self._XSDetector.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'axissetting' attribute
    def getAxissetting(self): return self._axissetting
    def setAxissetting(self, axissetting):
        if axissetting is None:
            self._axissetting = []
        elif axissetting.__class__.__name__ == "list":
            self._axissetting = axissetting
        else:
            strMessage = "ERROR! XSDetectorSetting.setAxissetting argument is not list but %s" % axissetting.__class__.__name__
            raise BaseException(strMessage)
    def delAxissetting(self): self._axissetting = None
    axissetting = property(getAxissetting, setAxissetting, delAxissetting, "Property for axissetting")
    def addAxissetting(self, value):
        if value is None:
            strMessage = "ERROR! XSDetectorSetting.addAxissetting argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDisplacement":
            self._axissetting.append(value)
        else:
            strMessage = "ERROR! XSDetectorSetting.addAxissetting argument is not XSDataDisplacement but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAxissetting(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDetectorSetting.insertAxissetting argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDetectorSetting.insertAxissetting argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDisplacement":
            self._axissetting[index] = value
        else:
            strMessage = "ERROR! XSDetectorSetting.addAxissetting argument is not XSDataDisplacement but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSDetector' attribute
    def getXSDetector(self): return self._XSDetector
    def setXSDetector(self, XSDetector):
        if XSDetector is None:
            self._XSDetector = None
        elif XSDetector.__class__.__name__ == "XSDetector":
            self._XSDetector = XSDetector
        else:
            strMessage = "ERROR! XSDetectorSetting.setXSDetector argument is not XSDetector but %s" % XSDetector.__class__.__name__
            raise BaseException(strMessage)
    def delXSDetector(self): self._XSDetector = None
    XSDetector = property(getXSDetector, setXSDetector, delXSDetector, "Property for XSDetector")
    def export(self, outfile, level, name_='XSDetectorSetting'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorSetting'):
        XSDisplacementListSetting.exportChildren(self, outfile, level, name_)
        for axissetting_ in self.getAxissetting():
            axissetting_.export(outfile, level, name_='axissetting')
        if self.getAxissetting() == []:
            warnEmptyAttribute("axissetting", "XSDataDisplacement")
        if self._XSDetector is not None:
            self.XSDetector.export(outfile, level, name_='XSDetector')
        else:
            warnEmptyAttribute("XSDetector", "XSDetector")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axissetting':
            obj_ = XSDataDisplacement()
            obj_.build(child_)
            self.axissetting.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSDetector':
            obj_ = XSDetector()
            obj_.build(child_)
            self.setXSDetector(obj_)
        XSDisplacementListSetting.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorSetting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorSetting' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorSetting is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorSetting.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorSetting()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorSetting" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorSetting()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorSetting


class XSGoniostatAxis(XSDisplacementAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
        XSDisplacementAxis.__init__(self, XSCalibratedDisplacementAxis, name)
        if isscannable is None:
            self._isscannable = None
        elif isscannable.__class__.__name__ == "XSDataBoolean":
            self._isscannable = isscannable
        else:
            strMessage = "ERROR! XSGoniostatAxis constructor argument 'isscannable' is not XSDataBoolean but %s" % self._isscannable.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'isscannable' attribute
    def getIsscannable(self): return self._isscannable
    def setIsscannable(self, isscannable):
        if isscannable is None:
            self._isscannable = None
        elif isscannable.__class__.__name__ == "XSDataBoolean":
            self._isscannable = isscannable
        else:
            strMessage = "ERROR! XSGoniostatAxis.setIsscannable argument is not XSDataBoolean but %s" % isscannable.__class__.__name__
            raise BaseException(strMessage)
    def delIsscannable(self): self._isscannable = None
    isscannable = property(getIsscannable, setIsscannable, delIsscannable, "Property for isscannable")
    def export(self, outfile, level, name_='XSGoniostatAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSGoniostatAxis'):
        XSDisplacementAxis.exportChildren(self, outfile, level, name_)
        if self._isscannable is not None:
            self.isscannable.export(outfile, level, name_='isscannable')
        else:
            warnEmptyAttribute("isscannable", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isscannable':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setIsscannable(obj_)
        XSDisplacementAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSGoniostatAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSGoniostatAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSGoniostatAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSGoniostatAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSGoniostatAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSGoniostatAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSGoniostatAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSGoniostatAxis


class XSIndexingSolutionSelected(XSIndexingSolution):
    def __init__(self, penalty=None, lattice=None, orientation=None, statistics=None, mosaicityestimated=None, refineddetectorsetting=None):
        XSIndexingSolution.__init__(self, penalty, lattice)
        if refineddetectorsetting is None:
            self._refineddetectorsetting = None
        elif refineddetectorsetting.__class__.__name__ == "XSDetectorFaceSetting":
            self._refineddetectorsetting = refineddetectorsetting
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected constructor argument 'refineddetectorsetting' is not XSDetectorFaceSetting but %s" % self._refineddetectorsetting.__class__.__name__
            raise BaseException(strMessage)
        if mosaicityestimated is None:
            self._mosaicityestimated = None
        elif mosaicityestimated.__class__.__name__ == "XSDataDouble":
            self._mosaicityestimated = mosaicityestimated
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected constructor argument 'mosaicityestimated' is not XSDataDouble but %s" % self._mosaicityestimated.__class__.__name__
            raise BaseException(strMessage)
        if statistics is None:
            self._statistics = None
        elif statistics.__class__.__name__ == "XSStatisticsIndexing":
            self._statistics = statistics
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected constructor argument 'statistics' is not XSStatisticsIndexing but %s" % self._statistics.__class__.__name__
            raise BaseException(strMessage)
        if orientation is None:
            self._orientation = None
        elif orientation.__class__.__name__ == "XSDataRotation":
            self._orientation = orientation
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected constructor argument 'orientation' is not XSDataRotation but %s" % self._orientation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'refineddetectorsetting' attribute
    def getRefineddetectorsetting(self): return self._refineddetectorsetting
    def setRefineddetectorsetting(self, refineddetectorsetting):
        if refineddetectorsetting is None:
            self._refineddetectorsetting = None
        elif refineddetectorsetting.__class__.__name__ == "XSDetectorFaceSetting":
            self._refineddetectorsetting = refineddetectorsetting
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected.setRefineddetectorsetting argument is not XSDetectorFaceSetting but %s" % refineddetectorsetting.__class__.__name__
            raise BaseException(strMessage)
    def delRefineddetectorsetting(self): self._refineddetectorsetting = None
    refineddetectorsetting = property(getRefineddetectorsetting, setRefineddetectorsetting, delRefineddetectorsetting, "Property for refineddetectorsetting")
    # Methods and properties for the 'mosaicityestimated' attribute
    def getMosaicityestimated(self): return self._mosaicityestimated
    def setMosaicityestimated(self, mosaicityestimated):
        if mosaicityestimated is None:
            self._mosaicityestimated = None
        elif mosaicityestimated.__class__.__name__ == "XSDataDouble":
            self._mosaicityestimated = mosaicityestimated
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected.setMosaicityestimated argument is not XSDataDouble but %s" % mosaicityestimated.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicityestimated(self): self._mosaicityestimated = None
    mosaicityestimated = property(getMosaicityestimated, setMosaicityestimated, delMosaicityestimated, "Property for mosaicityestimated")
    # Methods and properties for the 'statistics' attribute
    def getStatistics(self): return self._statistics
    def setStatistics(self, statistics):
        if statistics is None:
            self._statistics = None
        elif statistics.__class__.__name__ == "XSStatisticsIndexing":
            self._statistics = statistics
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected.setStatistics argument is not XSStatisticsIndexing but %s" % statistics.__class__.__name__
            raise BaseException(strMessage)
    def delStatistics(self): self._statistics = None
    statistics = property(getStatistics, setStatistics, delStatistics, "Property for statistics")
    # Methods and properties for the 'orientation' attribute
    def getOrientation(self): return self._orientation
    def setOrientation(self, orientation):
        if orientation is None:
            self._orientation = None
        elif orientation.__class__.__name__ == "XSDataRotation":
            self._orientation = orientation
        else:
            strMessage = "ERROR! XSIndexingSolutionSelected.setOrientation argument is not XSDataRotation but %s" % orientation.__class__.__name__
            raise BaseException(strMessage)
    def delOrientation(self): self._orientation = None
    orientation = property(getOrientation, setOrientation, delOrientation, "Property for orientation")
    def export(self, outfile, level, name_='XSIndexingSolutionSelected'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSIndexingSolutionSelected'):
        XSIndexingSolution.exportChildren(self, outfile, level, name_)
        if self._refineddetectorsetting is not None:
            self.refineddetectorsetting.export(outfile, level, name_='refineddetectorsetting')
        else:
            warnEmptyAttribute("refineddetectorsetting", "XSDetectorFaceSetting")
        if self._mosaicityestimated is not None:
            self.mosaicityestimated.export(outfile, level, name_='mosaicityestimated')
        else:
            warnEmptyAttribute("mosaicityestimated", "XSDataDouble")
        if self._statistics is not None:
            self.statistics.export(outfile, level, name_='statistics')
        else:
            warnEmptyAttribute("statistics", "XSStatisticsIndexing")
        if self._orientation is not None:
            self.orientation.export(outfile, level, name_='orientation')
        else:
            warnEmptyAttribute("orientation", "XSDataRotation")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refineddetectorsetting':
            obj_ = XSDetectorFaceSetting()
            obj_.build(child_)
            self.setRefineddetectorsetting(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityestimated':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMosaicityestimated(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statistics':
            obj_ = XSStatisticsIndexing()
            obj_.build(child_)
            self.setStatistics(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orientation':
            obj_ = XSDataRotation()
            obj_.build(child_)
            self.setOrientation(obj_)
        XSIndexingSolution.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSIndexingSolutionSelected" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSIndexingSolutionSelected' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSIndexingSolutionSelected is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSIndexingSolutionSelected.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSIndexingSolutionSelected()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSIndexingSolutionSelected" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSIndexingSolutionSelected()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSIndexingSolutionSelected


class XSProcessingWedge(XSWedge):
    def __init__(self, ednaid=None):
        XSWedge.__init__(self, ednaid)
    def export(self, outfile, level, name_='XSProcessingWedge'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSProcessingWedge'):
        XSWedge.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSWedge.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSProcessingWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSProcessingWedge' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSProcessingWedge is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSProcessingWedge.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSProcessingWedge()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSProcessingWedge" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSProcessingWedge()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSProcessingWedge


class XSRotationalGoniostat(XSDisplacementList):
    def __init__(self, XSGoniostatRotatableAxis=None, XSGoniostatBaseAxis=None):
        XSDisplacementList.__init__(self, )
        if XSGoniostatBaseAxis is None:
            self._XSGoniostatBaseAxis = None
        elif XSGoniostatBaseAxis.__class__.__name__ == "XSGoniostatBaseAxis":
            self._XSGoniostatBaseAxis = XSGoniostatBaseAxis
        else:
            strMessage = "ERROR! XSRotationalGoniostat constructor argument 'XSGoniostatBaseAxis' is not XSGoniostatBaseAxis but %s" % self._XSGoniostatBaseAxis.__class__.__name__
            raise BaseException(strMessage)
        if XSGoniostatRotatableAxis is None:
            self._XSGoniostatRotatableAxis = []
        elif XSGoniostatRotatableAxis.__class__.__name__ == "list":
            self._XSGoniostatRotatableAxis = XSGoniostatRotatableAxis
        else:
            strMessage = "ERROR! XSRotationalGoniostat constructor argument 'XSGoniostatRotatableAxis' is not list but %s" % self._XSGoniostatRotatableAxis.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSGoniostatBaseAxis' attribute
    def getXSGoniostatBaseAxis(self): return self._XSGoniostatBaseAxis
    def setXSGoniostatBaseAxis(self, XSGoniostatBaseAxis):
        if XSGoniostatBaseAxis is None:
            self._XSGoniostatBaseAxis = None
        elif XSGoniostatBaseAxis.__class__.__name__ == "XSGoniostatBaseAxis":
            self._XSGoniostatBaseAxis = XSGoniostatBaseAxis
        else:
            strMessage = "ERROR! XSRotationalGoniostat.setXSGoniostatBaseAxis argument is not XSGoniostatBaseAxis but %s" % XSGoniostatBaseAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSGoniostatBaseAxis(self): self._XSGoniostatBaseAxis = None
    XSGoniostatBaseAxis = property(getXSGoniostatBaseAxis, setXSGoniostatBaseAxis, delXSGoniostatBaseAxis, "Property for XSGoniostatBaseAxis")
    # Methods and properties for the 'XSGoniostatRotatableAxis' attribute
    def getXSGoniostatRotatableAxis(self): return self._XSGoniostatRotatableAxis
    def setXSGoniostatRotatableAxis(self, XSGoniostatRotatableAxis):
        if XSGoniostatRotatableAxis is None:
            self._XSGoniostatRotatableAxis = []
        elif XSGoniostatRotatableAxis.__class__.__name__ == "list":
            self._XSGoniostatRotatableAxis = XSGoniostatRotatableAxis
        else:
            strMessage = "ERROR! XSRotationalGoniostat.setXSGoniostatRotatableAxis argument is not list but %s" % XSGoniostatRotatableAxis.__class__.__name__
            raise BaseException(strMessage)
    def delXSGoniostatRotatableAxis(self): self._XSGoniostatRotatableAxis = None
    XSGoniostatRotatableAxis = property(getXSGoniostatRotatableAxis, setXSGoniostatRotatableAxis, delXSGoniostatRotatableAxis, "Property for XSGoniostatRotatableAxis")
    def addXSGoniostatRotatableAxis(self, value):
        if value is None:
            strMessage = "ERROR! XSRotationalGoniostat.addXSGoniostatRotatableAxis argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSGoniostatRotatableAxis":
            self._XSGoniostatRotatableAxis.append(value)
        else:
            strMessage = "ERROR! XSRotationalGoniostat.addXSGoniostatRotatableAxis argument is not XSGoniostatRotatableAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXSGoniostatRotatableAxis(self, index, value):
        if index is None:
            strMessage = "ERROR! XSRotationalGoniostat.insertXSGoniostatRotatableAxis argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSRotationalGoniostat.insertXSGoniostatRotatableAxis argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSGoniostatRotatableAxis":
            self._XSGoniostatRotatableAxis[index] = value
        else:
            strMessage = "ERROR! XSRotationalGoniostat.addXSGoniostatRotatableAxis argument is not XSGoniostatRotatableAxis but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSRotationalGoniostat'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSRotationalGoniostat'):
        XSDisplacementList.exportChildren(self, outfile, level, name_)
        if self._XSGoniostatBaseAxis is not None:
            self.XSGoniostatBaseAxis.export(outfile, level, name_='XSGoniostatBaseAxis')
        else:
            warnEmptyAttribute("XSGoniostatBaseAxis", "XSGoniostatBaseAxis")
        for XSGoniostatRotatableAxis_ in self.getXSGoniostatRotatableAxis():
            XSGoniostatRotatableAxis_.export(outfile, level, name_='XSGoniostatRotatableAxis')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSGoniostatBaseAxis':
            obj_ = XSGoniostatBaseAxis()
            obj_.build(child_)
            self.setXSGoniostatBaseAxis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSGoniostatRotatableAxis':
            obj_ = XSGoniostatRotatableAxis()
            obj_.build(child_)
            self.XSGoniostatRotatableAxis.append(obj_)
        XSDisplacementList.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSRotationalGoniostat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSRotationalGoniostat' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSRotationalGoniostat is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSRotationalGoniostat.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSRotationalGoniostat()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSRotationalGoniostat" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSRotationalGoniostat()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSRotationalGoniostat


class XSRotationalGoniostatSetting(XSDisplacementListSetting):
    def __init__(self, XSRotationalGoniostat=None, axissetting=None, baseaxissetting=None):
        XSDisplacementListSetting.__init__(self, )
        if baseaxissetting is None:
            self._baseaxissetting = None
        elif baseaxissetting.__class__.__name__ == "XSDataAngle":
            self._baseaxissetting = baseaxissetting
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting constructor argument 'baseaxissetting' is not XSDataAngle but %s" % self._baseaxissetting.__class__.__name__
            raise BaseException(strMessage)
        if axissetting is None:
            self._axissetting = []
        elif axissetting.__class__.__name__ == "list":
            self._axissetting = axissetting
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting constructor argument 'axissetting' is not list but %s" % self._axissetting.__class__.__name__
            raise BaseException(strMessage)
        if XSRotationalGoniostat is None:
            self._XSRotationalGoniostat = None
        elif XSRotationalGoniostat.__class__.__name__ == "XSRotationalGoniostat":
            self._XSRotationalGoniostat = XSRotationalGoniostat
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting constructor argument 'XSRotationalGoniostat' is not XSRotationalGoniostat but %s" % self._XSRotationalGoniostat.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'baseaxissetting' attribute
    def getBaseaxissetting(self): return self._baseaxissetting
    def setBaseaxissetting(self, baseaxissetting):
        if baseaxissetting is None:
            self._baseaxissetting = None
        elif baseaxissetting.__class__.__name__ == "XSDataAngle":
            self._baseaxissetting = baseaxissetting
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting.setBaseaxissetting argument is not XSDataAngle but %s" % baseaxissetting.__class__.__name__
            raise BaseException(strMessage)
    def delBaseaxissetting(self): self._baseaxissetting = None
    baseaxissetting = property(getBaseaxissetting, setBaseaxissetting, delBaseaxissetting, "Property for baseaxissetting")
    # Methods and properties for the 'axissetting' attribute
    def getAxissetting(self): return self._axissetting
    def setAxissetting(self, axissetting):
        if axissetting is None:
            self._axissetting = []
        elif axissetting.__class__.__name__ == "list":
            self._axissetting = axissetting
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting.setAxissetting argument is not list but %s" % axissetting.__class__.__name__
            raise BaseException(strMessage)
    def delAxissetting(self): self._axissetting = None
    axissetting = property(getAxissetting, setAxissetting, delAxissetting, "Property for axissetting")
    def addAxissetting(self, value):
        if value is None:
            strMessage = "ERROR! XSRotationalGoniostatSetting.addAxissetting argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAngle":
            self._axissetting.append(value)
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting.addAxissetting argument is not XSDataAngle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAxissetting(self, index, value):
        if index is None:
            strMessage = "ERROR! XSRotationalGoniostatSetting.insertAxissetting argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSRotationalGoniostatSetting.insertAxissetting argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAngle":
            self._axissetting[index] = value
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting.addAxissetting argument is not XSDataAngle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'XSRotationalGoniostat' attribute
    def getXSRotationalGoniostat(self): return self._XSRotationalGoniostat
    def setXSRotationalGoniostat(self, XSRotationalGoniostat):
        if XSRotationalGoniostat is None:
            self._XSRotationalGoniostat = None
        elif XSRotationalGoniostat.__class__.__name__ == "XSRotationalGoniostat":
            self._XSRotationalGoniostat = XSRotationalGoniostat
        else:
            strMessage = "ERROR! XSRotationalGoniostatSetting.setXSRotationalGoniostat argument is not XSRotationalGoniostat but %s" % XSRotationalGoniostat.__class__.__name__
            raise BaseException(strMessage)
    def delXSRotationalGoniostat(self): self._XSRotationalGoniostat = None
    XSRotationalGoniostat = property(getXSRotationalGoniostat, setXSRotationalGoniostat, delXSRotationalGoniostat, "Property for XSRotationalGoniostat")
    def export(self, outfile, level, name_='XSRotationalGoniostatSetting'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSRotationalGoniostatSetting'):
        XSDisplacementListSetting.exportChildren(self, outfile, level, name_)
        if self._baseaxissetting is not None:
            self.baseaxissetting.export(outfile, level, name_='baseaxissetting')
        else:
            warnEmptyAttribute("baseaxissetting", "XSDataAngle")
        for axissetting_ in self.getAxissetting():
            axissetting_.export(outfile, level, name_='axissetting')
        if self._XSRotationalGoniostat is not None:
            self.XSRotationalGoniostat.export(outfile, level, name_='XSRotationalGoniostat')
        else:
            warnEmptyAttribute("XSRotationalGoniostat", "XSRotationalGoniostat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'baseaxissetting':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setBaseaxissetting(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axissetting':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.axissetting.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSRotationalGoniostat':
            obj_ = XSRotationalGoniostat()
            obj_.build(child_)
            self.setXSRotationalGoniostat(obj_)
        XSDisplacementListSetting.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSRotationalGoniostatSetting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSRotationalGoniostatSetting' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSRotationalGoniostatSetting is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSRotationalGoniostatSetting.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSRotationalGoniostatSetting()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSRotationalGoniostatSetting" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSRotationalGoniostatSetting()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSRotationalGoniostatSetting


class XSDetectorRotationAxis(XSDetectorAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
        XSDetectorAxis.__init__(self, XSCalibratedDisplacementAxis, name)
    def export(self, outfile, level, name_='XSDetectorRotationAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorRotationAxis'):
        XSDetectorAxis.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDetectorAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorRotationAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorRotationAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorRotationAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorRotationAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorRotationAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorRotationAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorRotationAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorRotationAxis


class XSDetectorTranslationAxis(XSDetectorAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None):
        XSDetectorAxis.__init__(self, XSCalibratedDisplacementAxis, name)
    def export(self, outfile, level, name_='XSDetectorTranslationAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDetectorTranslationAxis'):
        XSDetectorAxis.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDetectorAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDetectorTranslationAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDetectorTranslationAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDetectorTranslationAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDetectorTranslationAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDetectorTranslationAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDetectorTranslationAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDetectorTranslationAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDetectorTranslationAxis


class XSGoniostatBaseAxis(XSGoniostatAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
        XSGoniostatAxis.__init__(self, XSCalibratedDisplacementAxis, name, isscannable)
    def export(self, outfile, level, name_='XSGoniostatBaseAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSGoniostatBaseAxis'):
        XSGoniostatAxis.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSGoniostatAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSGoniostatBaseAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSGoniostatBaseAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSGoniostatBaseAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSGoniostatBaseAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSGoniostatBaseAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSGoniostatBaseAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSGoniostatBaseAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSGoniostatBaseAxis


class XSGoniostatRotatableAxis(XSGoniostatAxis):
    def __init__(self, XSCalibratedDisplacementAxis=None, name=None, isscannable=None):
        XSGoniostatAxis.__init__(self, XSCalibratedDisplacementAxis, name, isscannable)
    def export(self, outfile, level, name_='XSGoniostatRotatableAxis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSGoniostatRotatableAxis'):
        XSGoniostatAxis.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSGoniostatAxis.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSGoniostatRotatableAxis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSGoniostatRotatableAxis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSGoniostatRotatableAxis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSGoniostatRotatableAxis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSGoniostatRotatableAxis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSGoniostatRotatableAxis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSGoniostatRotatableAxis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSGoniostatRotatableAxis



# End of data representation classes.


