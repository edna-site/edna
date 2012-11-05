#!/usr/bin/env python

#
# Generated Mon Mar  7 15:28:17 2011 by EDGenerateDS.py.
#

import sys
import getopt
import StringIO
from xml.dom import minidom
from xml.dom import Node

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = inStr
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('"', '&quot;')
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
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
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class _MemberSpec(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type(self): return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container


#
# Data representation classes.
#

class XSConfiguration:
    subclass = None
    def __init__(self, XSPluginList=None):
        self.XSPluginList = XSPluginList
    def factory(*args_, **kwargs_):
        if XSConfiguration.subclass:
            return XSConfiguration.subclass(*args_, **kwargs_)
        else:
            return XSConfiguration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSPluginList(self): return self.XSPluginList
    def setXSPluginList(self, XSPluginList): self.XSPluginList = XSPluginList
    def export(self, outfile, level, name_='XSConfiguration'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSConfiguration'):
        pass
    def exportChildren(self, outfile, level, name_='XSConfiguration'):
        if self.getXSPluginList() != None :
            if self.XSPluginList:
                self.XSPluginList.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSConfiguration' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSConfiguration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSConfiguration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSConfiguration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSConfiguration'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XSPluginList:
            showIndent(outfile, level)
            outfile.write('XSPluginList=XSPluginList(\n')
            self.XSPluginList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSPluginList':
            obj_ = XSPluginList.factory()
            obj_.build(child_)
            self.setXSPluginList(obj_)
# end class XSConfiguration


class XSData(object):
    subclass = None
    def __init__(self, valueOf_=''):
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSData.subclass:
            return XSData.subclass(*args_, **kwargs_)
        else:
            return XSData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSData'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSData'):
        pass
    def exportChildren(self, outfile, level, name_='XSData'):
        pass
    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSData' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSData.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSData.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSData" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSData'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class XSData


class XSDataArray(XSData):
    subclass = None
    def __init__(self, shape=None, size=-1, dtype='', data='', coding=None, md5sum=None):
        XSData.__init__(self)
        if shape is None:
            self.shape = []
        else:
            self.shape = shape
        self.size = size
        self.dtype = dtype
        self.data = data
        self.coding = coding
        self.md5sum = md5sum
    def factory(*args_, **kwargs_):
        if XSDataArray.subclass:
            return XSDataArray.subclass(*args_, **kwargs_)
        else:
            return XSDataArray(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getShape(self): return self.shape
    def setShape(self, shape): self.shape = shape
    def addShape(self, value): self.shape.append(value)
    def insertShape(self, index, value): self.shape[index] = value
    def getSize(self): return self.size
    def setSize(self, size): self.size = size
    def getDtype(self): return self.dtype
    def setDtype(self, dtype): self.dtype = dtype
    def getData(self): return self.data
    def setData(self, data): self.data = data
    def getCoding(self): return self.coding
    def setCoding(self, coding): self.coding = coding
    def getMd5sum(self): return self.md5sum
    def setMd5sum(self, md5sum): self.md5sum = md5sum
    def export(self, outfile, level, name_='XSDataArray'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataArray'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataArray')
    def exportChildren(self, outfile, level, name_='XSDataArray'):
        for shape_ in self.getShape():
            showIndent(outfile, level)
            outfile.write('<shape>%d</shape>\n' % shape_)
        showIndent(outfile, level)
        outfile.write('<size>%d</size>\n' % self.getSize())
        showIndent(outfile, level)
        outfile.write('<dtype>%s</dtype>\n' % quote_xml(self.getDtype()))
        showIndent(outfile, level)
        outfile.write('<data>%s</data>\n' % quote_xml(self.getData()))
        if self.getCoding() != None :
            if self.coding:
                self.coding.export(outfile, level, name_='coding')
        if self.getMd5sum() != None :
            if self.md5sum:
                self.md5sum.export(outfile, level, name_='md5sum')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataArray' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataArray.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataArray.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataArray" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataArray'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('shape=[\n')
        level += 1
        for shape in self.shape:
            showIndent(outfile, level)
            outfile.write('%d,\n' % shape)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('size=%d,\n' % self.getSize())
        showIndent(outfile, level)
        outfile.write('dtype=%s,\n' % quote_python(self.getDtype()))
        showIndent(outfile, level)
        outfile.write('data=%s,\n' % quote_python(self.getData()))
        if self.coding:
            showIndent(outfile, level)
            outfile.write('coding=XSDataString(\n')
            self.coding.exportLiteral(outfile, level, name_='coding')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.md5sum:
            showIndent(outfile, level)
            outfile.write('md5sum=XSDataString(\n')
            self.md5sum.exportLiteral(outfile, level, name_='md5sum')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shape':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.shape.append(ival_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'size':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.size = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dtype':
            dtype_ = ''
            for text__content_ in child_.childNodes:
                dtype_ += text__content_.nodeValue
            self.dtype = dtype_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            data_ = ''
            for text__content_ in child_.childNodes:
                data_ += text__content_.nodeValue
            self.data = data_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coding':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCoding(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'md5sum':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMd5sum(obj_)
# end class XSDataArray


class XSDataBoolean(XSData):
    subclass = None
    def __init__(self, value=0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataBoolean.subclass:
            return XSDataBoolean.subclass(*args_, **kwargs_)
        else:
            return XSDataBoolean(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataBoolean'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataBoolean'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataBoolean')
    def exportChildren(self, outfile, level, name_='XSDataBoolean'):
        showIndent(outfile, level)
        outfile.write('<value>%d</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataBoolean' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBoolean.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBoolean.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataBoolean" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataBoolean'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%d,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('true', '1'):
                    ival_ = 1
                elif sval_ in ('false', '0'):
                    ival_ = 0
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self.value = ival_
# end class XSDataBoolean


class XSDataDictionary:
    subclass = None
    def __init__(self, keyValuePair=None):
        if keyValuePair is None:
            self.keyValuePair = []
        else:
            self.keyValuePair = keyValuePair
    def factory(*args_, **kwargs_):
        if XSDataDictionary.subclass:
            return XSDataDictionary.subclass(*args_, **kwargs_)
        else:
            return XSDataDictionary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getKeyValuePair(self): return self.keyValuePair
    def setKeyValuePair(self, keyValuePair): self.keyValuePair = keyValuePair
    def addKeyValuePair(self, value): self.keyValuePair.append(value)
    def insertKeyValuePair(self, index, value): self.keyValuePair[index] = value
    def export(self, outfile, level, name_='XSDataDictionary'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDictionary'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataDictionary'):
        for keyValuePair_ in self.getKeyValuePair():
            keyValuePair_.export(outfile, level, name_='keyValuePair')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDictionary' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDictionary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDictionary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDictionary" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDictionary'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('keyValuePair=[\n')
        level += 1
        for keyValuePair in self.keyValuePair:
            showIndent(outfile, level)
            outfile.write('XSDataKeyValuePair(\n')
            keyValuePair.exportLiteral(outfile, level, name_='keyValuePair')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'keyValuePair':
            obj_ = XSDataKeyValuePair.factory()
            obj_.build(child_)
            self.keyValuePair.append(obj_)
# end class XSDataDictionary


class XSDataDisplacement:
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None):
        self.value = value
        self.unit = unit
        self.error = error
    def factory(*args_, **kwargs_):
        if XSDataDisplacement.subclass:
            return XSDataDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getError(self): return self.error
    def setError(self, error): self.error = error
    def export(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDisplacement'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.getError() != None :
            if self.error:
                self.error.export(outfile, level, name_='error')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDisplacement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDisplacement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDisplacement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataString(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.error:
            showIndent(outfile, level)
            outfile.write('error=XSDataDouble(\n')
            self.error.exportLiteral(outfile, level, name_='error')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'error':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setError(obj_)
# end class XSDataDisplacement


class XSDataDouble(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataDouble.subclass:
            return XSDataDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDouble')
    def exportChildren(self, outfile, level, name_='XSDataDouble'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
# end class XSDataDouble


class XSDataDoubleWithUnit(XSDataDouble):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None):
        XSDataDouble.__init__(self, value)
        self.unit = unit
        self.error = error
    def factory(*args_, **kwargs_):
        if XSDataDoubleWithUnit.subclass:
            return XSDataDoubleWithUnit.subclass(*args_, **kwargs_)
        else:
            return XSDataDoubleWithUnit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getError(self): return self.error
    def setError(self, error): self.error = error
    def export(self, outfile, level, name_='XSDataDoubleWithUnit'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDoubleWithUnit'):
        XSDataDouble.exportAttributes(self, outfile, level, name_='XSDataDoubleWithUnit')
    def exportChildren(self, outfile, level, name_='XSDataDoubleWithUnit'):
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.getError() != None :
            if self.error:
                self.error.export(outfile, level, name_='error')
        XSDataDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDoubleWithUnit' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDoubleWithUnit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDoubleWithUnit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDoubleWithUnit" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDoubleWithUnit'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataString(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.error:
            showIndent(outfile, level)
            outfile.write('error=XSDataDouble(\n')
            self.error.exportLiteral(outfile, level, name_='error')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'error':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setError(obj_)
        XSDataDouble.buildChildren(self, child_, nodeName_)
# end class XSDataDoubleWithUnit


class XSDataExecutionInfo:
    subclass = None
    def __init__(self, baseDirectory=None, executionTime=None, pluginName=None, startOfExecution=None, systeminfo=None, workingDirectory=None, configuration=None):
        self.baseDirectory = baseDirectory
        self.executionTime = executionTime
        self.pluginName = pluginName
        self.startOfExecution = startOfExecution
        self.systeminfo = systeminfo
        self.workingDirectory = workingDirectory
        self.configuration = configuration
    def factory(*args_, **kwargs_):
        if XSDataExecutionInfo.subclass:
            return XSDataExecutionInfo.subclass(*args_, **kwargs_)
        else:
            return XSDataExecutionInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBaseDirectory(self): return self.baseDirectory
    def setBaseDirectory(self, baseDirectory): self.baseDirectory = baseDirectory
    def getExecutionTime(self): return self.executionTime
    def setExecutionTime(self, executionTime): self.executionTime = executionTime
    def getPluginName(self): return self.pluginName
    def setPluginName(self, pluginName): self.pluginName = pluginName
    def getStartOfExecution(self): return self.startOfExecution
    def setStartOfExecution(self, startOfExecution): self.startOfExecution = startOfExecution
    def getSysteminfo(self): return self.systeminfo
    def setSysteminfo(self, systeminfo): self.systeminfo = systeminfo
    def getWorkingDirectory(self): return self.workingDirectory
    def setWorkingDirectory(self, workingDirectory): self.workingDirectory = workingDirectory
    def getConfiguration(self): return self.configuration
    def setConfiguration(self, configuration): self.configuration = configuration
    def export(self, outfile, level, name_='XSDataExecutionInfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataExecutionInfo'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataExecutionInfo'):
        if self.baseDirectory:
            self.baseDirectory.export(outfile, level, name_='baseDirectory')
        if self.executionTime:
            self.executionTime.export(outfile, level, name_='executionTime')
        if self.pluginName:
            self.pluginName.export(outfile, level, name_='pluginName')
        if self.startOfExecution:
            self.startOfExecution.export(outfile, level, name_='startOfExecution')
        if self.systeminfo:
            self.systeminfo.export(outfile, level, name_='systeminfo')
        if self.workingDirectory:
            self.workingDirectory.export(outfile, level, name_='workingDirectory')
        if self.configuration:
            self.configuration.export(outfile, level, name_='configuration')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataExecutionInfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataExecutionInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataExecutionInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataExecutionInfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataExecutionInfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.baseDirectory:
            showIndent(outfile, level)
            outfile.write('baseDirectory=XSDataFile(\n')
            self.baseDirectory.exportLiteral(outfile, level, name_='baseDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.executionTime:
            showIndent(outfile, level)
            outfile.write('executionTime=XSDataTime(\n')
            self.executionTime.exportLiteral(outfile, level, name_='executionTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pluginName:
            showIndent(outfile, level)
            outfile.write('pluginName=XSDataString(\n')
            self.pluginName.exportLiteral(outfile, level, name_='pluginName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.startOfExecution:
            showIndent(outfile, level)
            outfile.write('startOfExecution=XSDataDate(\n')
            self.startOfExecution.exportLiteral(outfile, level, name_='startOfExecution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.systeminfo:
            showIndent(outfile, level)
            outfile.write('systeminfo=XSDataSysteminfo(\n')
            self.systeminfo.exportLiteral(outfile, level, name_='systeminfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.workingDirectory:
            showIndent(outfile, level)
            outfile.write('workingDirectory=XSDataFile(\n')
            self.workingDirectory.exportLiteral(outfile, level, name_='workingDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.configuration:
            showIndent(outfile, level)
            outfile.write('configuration=XSConfiguration(\n')
            self.configuration.exportLiteral(outfile, level, name_='configuration')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'baseDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setBaseDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executionTime':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setExecutionTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pluginName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPluginName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startOfExecution':
            obj_ = XSDataDate.factory()
            obj_.build(child_)
            self.setStartOfExecution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'systeminfo':
            obj_ = XSDataSysteminfo.factory()
            obj_.build(child_)
            self.setSysteminfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'workingDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setWorkingDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'configuration':
            obj_ = XSConfiguration.factory()
            obj_.build(child_)
            self.setConfiguration(obj_)
# end class XSDataExecutionInfo


class XSDataFile(XSData):
    subclass = None
    def __init__(self, path=None):
        XSData.__init__(self)
        self.path = path
    def factory(*args_, **kwargs_):
        if XSDataFile.subclass:
            return XSDataFile.subclass(*args_, **kwargs_)
        else:
            return XSDataFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPath(self): return self.path
    def setPath(self, path): self.path = path
    def export(self, outfile, level, name_='XSDataFile'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFile'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFile')
    def exportChildren(self, outfile, level, name_='XSDataFile'):
        if self.path:
            self.path.export(outfile, level, name_='path')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFile' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFile'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.path:
            showIndent(outfile, level)
            outfile.write('path=XSDataString(\n')
            self.path.exportLiteral(outfile, level, name_='path')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPath(obj_)
# end class XSDataFile


class XSDataFloat(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataFloat.subclass:
            return XSDataFloat.subclass(*args_, **kwargs_)
        else:
            return XSDataFloat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataFloat'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFloat'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFloat')
    def exportChildren(self, outfile, level, name_='XSDataFloat'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFloat' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFloat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFloat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFloat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFloat'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
# end class XSDataFloat


class XSDataFlux(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataFlux.subclass:
            return XSDataFlux.subclass(*args_, **kwargs_)
        else:
            return XSDataFlux(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataFlux'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFlux'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataFlux')
    def exportChildren(self, outfile, level, name_='XSDataFlux'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFlux' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFlux.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFlux.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFlux" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFlux'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataFlux


class XSDataImage(XSDataFile):
    subclass = None
    def __init__(self, path=None, date=None, number=None):
        XSDataFile.__init__(self, path)
        self.date = date
        self.number = number
    def factory(*args_, **kwargs_):
        if XSDataImage.subclass:
            return XSDataImage.subclass(*args_, **kwargs_)
        else:
            return XSDataImage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDate(self): return self.date
    def setDate(self, date): self.date = date
    def getNumber(self): return self.number
    def setNumber(self, number): self.number = number
    def export(self, outfile, level, name_='XSDataImage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataImage'):
        XSDataFile.exportAttributes(self, outfile, level, name_='XSDataImage')
    def exportChildren(self, outfile, level, name_='XSDataImage'):
        if self.getDate() != None :
            if self.date:
                self.date.export(outfile, level, name_='date')
        if self.getNumber() != None :
            if self.number:
                self.number.export(outfile, level, name_='number')
        XSDataFile.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataImage' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataImage'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataFile.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.date:
            showIndent(outfile, level)
            outfile.write('date=XSDataString(\n')
            self.date.exportLiteral(outfile, level, name_='date')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.number:
            showIndent(outfile, level)
            outfile.write('number=XSDataInteger(\n')
            self.number.exportLiteral(outfile, level, name_='number')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataFile.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataFile.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'date':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumber(obj_)
        XSDataFile.buildChildren(self, child_, nodeName_)
# end class XSDataImage


class XSDataInput(XSData):
    subclass = None
    def __init__(self, configuration=None):
        XSData.__init__(self)
        self.configuration = configuration
    def factory(*args_, **kwargs_):
        if XSDataInput.subclass:
            return XSDataInput.subclass(*args_, **kwargs_)
        else:
            return XSDataInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getConfiguration(self): return self.configuration
    def setConfiguration(self, configuration): self.configuration = configuration
    def export(self, outfile, level, name_='XSDataInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataInput')
    def exportChildren(self, outfile, level, name_='XSDataInput'):
        if self.configuration:
            self.configuration.export(outfile, level, name_='configuration')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.configuration:
            showIndent(outfile, level)
            outfile.write('configuration=XSConfiguration(\n')
            self.configuration.exportLiteral(outfile, level, name_='configuration')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'configuration':
            obj_ = XSConfiguration.factory()
            obj_.build(child_)
            self.setConfiguration(obj_)
# end class XSDataInput


class XSDataInteger(XSData):
    subclass = None
    def __init__(self, value=-1):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataInteger.subclass:
            return XSDataInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataInteger')
    def exportChildren(self, outfile, level, name_='XSDataInteger'):
        showIndent(outfile, level)
        outfile.write('<value>%d</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%d,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.value = ival_
# end class XSDataInteger


class XSDataKeyValuePair:
    subclass = None
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
    def factory(*args_, **kwargs_):
        if XSDataKeyValuePair.subclass:
            return XSDataKeyValuePair.subclass(*args_, **kwargs_)
        else:
            return XSDataKeyValuePair(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def getKey(self): return self.key
    def setKey(self, key): self.key = key
    def export(self, outfile, level, name_='XSDataKeyValuePair'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataKeyValuePair'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataKeyValuePair'):
        if self.value:
            self.value.export(outfile, level, name_='value')
        if self.key:
            self.key.export(outfile, level, name_='key')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataKeyValuePair' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataKeyValuePair.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataKeyValuePair.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataKeyValuePair" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataKeyValuePair'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.value:
            showIndent(outfile, level)
            outfile.write('value=XSDataString(\n')
            self.value.exportLiteral(outfile, level, name_='value')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.key:
            showIndent(outfile, level)
            outfile.write('key=XSDataString(\n')
            self.key.exportLiteral(outfile, level, name_='key')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'key':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKey(obj_)
# end class XSDataKeyValuePair


class XSDataLength(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataLength.subclass:
            return XSDataLength.subclass(*args_, **kwargs_)
        else:
            return XSDataLength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataLength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLength'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataLength')
    def exportChildren(self, outfile, level, name_='XSDataLength'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataLength' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataLength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataLength'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataLength


class XSDataLinearDisplacement(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDisplacement.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataLinearDisplacement.subclass:
            return XSDataLinearDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataLinearDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataLinearDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLinearDisplacement'):
        XSDataDisplacement.exportAttributes(self, outfile, level, name_='XSDataLinearDisplacement')
    def exportChildren(self, outfile, level, name_='XSDataLinearDisplacement'):
        XSDataDisplacement.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataLinearDisplacement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLinearDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLinearDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataLinearDisplacement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataLinearDisplacement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDisplacement.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDisplacement.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDisplacement.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDisplacement.buildChildren(self, child_, nodeName_)
# end class XSDataLinearDisplacement


class XSDataMatrixDouble(XSData):
    subclass = None
    def __init__(self, m11=0.0, m12=0.0, m13=0.0, m21=0.0, m22=0.0, m23=0.0, m31=0.0, m32=0.0, m33=0.0):
        XSData.__init__(self)
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33
    def factory(*args_, **kwargs_):
        if XSDataMatrixDouble.subclass:
            return XSDataMatrixDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrixDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getM11(self): return self.m11
    def setM11(self, m11): self.m11 = m11
    def getM12(self): return self.m12
    def setM12(self, m12): self.m12 = m12
    def getM13(self): return self.m13
    def setM13(self, m13): self.m13 = m13
    def getM21(self): return self.m21
    def setM21(self, m21): self.m21 = m21
    def getM22(self): return self.m22
    def setM22(self, m22): self.m22 = m22
    def getM23(self): return self.m23
    def setM23(self, m23): self.m23 = m23
    def getM31(self): return self.m31
    def setM31(self, m31): self.m31 = m31
    def getM32(self): return self.m32
    def setM32(self, m32): self.m32 = m32
    def getM33(self): return self.m33
    def setM33(self, m33): self.m33 = m33
    def export(self, outfile, level, name_='XSDataMatrixDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrixDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMatrixDouble')
    def exportChildren(self, outfile, level, name_='XSDataMatrixDouble'):
        showIndent(outfile, level)
        outfile.write('<m11>%e</m11>\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('<m12>%e</m12>\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('<m13>%e</m13>\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('<m21>%e</m21>\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('<m22>%e</m22>\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('<m23>%e</m23>\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('<m31>%e</m31>\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('<m32>%e</m32>\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('<m33>%e</m33>\n' % self.getM33())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrixDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrixDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrixDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('m11=%e,\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('m12=%e,\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('m13=%e,\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('m21=%e,\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('m22=%e,\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('m23=%e,\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('m31=%e,\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('m32=%e,\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('m33=%e,\n' % self.getM33())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm11':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m11 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm12':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m12 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm13':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m13 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm21':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m21 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm22':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m22 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm23':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m23 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm31':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m31 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm32':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m32 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm33':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m33 = fval_
# end class XSDataMatrixDouble


class XSDataMatrixInteger(XSData):
    subclass = None
    def __init__(self, m11=-1, m12=-1, m13=-1, m21=-1, m22=-1, m23=-1, m31=-1, m32=-1, m33=-1):
        XSData.__init__(self)
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33
    def factory(*args_, **kwargs_):
        if XSDataMatrixInteger.subclass:
            return XSDataMatrixInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrixInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getM11(self): return self.m11
    def setM11(self, m11): self.m11 = m11
    def getM12(self): return self.m12
    def setM12(self, m12): self.m12 = m12
    def getM13(self): return self.m13
    def setM13(self, m13): self.m13 = m13
    def getM21(self): return self.m21
    def setM21(self, m21): self.m21 = m21
    def getM22(self): return self.m22
    def setM22(self, m22): self.m22 = m22
    def getM23(self): return self.m23
    def setM23(self, m23): self.m23 = m23
    def getM31(self): return self.m31
    def setM31(self, m31): self.m31 = m31
    def getM32(self): return self.m32
    def setM32(self, m32): self.m32 = m32
    def getM33(self): return self.m33
    def setM33(self, m33): self.m33 = m33
    def export(self, outfile, level, name_='XSDataMatrixInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrixInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMatrixInteger')
    def exportChildren(self, outfile, level, name_='XSDataMatrixInteger'):
        showIndent(outfile, level)
        outfile.write('<m11>%d</m11>\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('<m12>%d</m12>\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('<m13>%d</m13>\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('<m21>%d</m21>\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('<m22>%d</m22>\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('<m23>%d</m23>\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('<m31>%d</m31>\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('<m32>%d</m32>\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('<m33>%d</m33>\n' % self.getM33())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrixInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrixInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrixInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('m11=%d,\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('m12=%d,\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('m13=%d,\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('m21=%d,\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('m22=%d,\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('m23=%d,\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('m31=%d,\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('m32=%d,\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('m33=%d,\n' % self.getM33())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm11':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m11 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm12':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m12 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm13':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m13 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm21':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m21 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm22':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m22 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm23':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m23 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm31':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m31 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm32':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m32 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm33':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m33 = ival_
# end class XSDataMatrixInteger


class XSDataMessage(XSData):
    subclass = None
    def __init__(self, debuginfo=None, level=None, text=None, typexx=None):
        XSData.__init__(self)
        self.debuginfo = debuginfo
        self.level = level
        self.text = text
        self.typexx = typexx
    def factory(*args_, **kwargs_):
        if XSDataMessage.subclass:
            return XSDataMessage.subclass(*args_, **kwargs_)
        else:
            return XSDataMessage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDebuginfo(self): return self.debuginfo
    def setDebuginfo(self, debuginfo): self.debuginfo = debuginfo
    def getLevel(self): return self.level
    def setLevel(self, level): self.level = level
    def getText(self): return self.text
    def setText(self, text): self.text = text
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def export(self, outfile, level, name_='XSDataMessage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMessage'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMessage')
    def exportChildren(self, outfile, level, name_='XSDataMessage'):
        if self.debuginfo:
            self.debuginfo.export(outfile, level, name_='debuginfo')
        if self.level:
            self.level.export(outfile, level, name_='level')
        if self.text:
            self.text.export(outfile, level, name_='text')
        if self.typexx:
            self.typexx.export(outfile, level, name_='type')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMessage' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMessage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMessage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMessage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMessage'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.debuginfo:
            showIndent(outfile, level)
            outfile.write('debuginfo=XSDataString(\n')
            self.debuginfo.exportLiteral(outfile, level, name_='debuginfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.level:
            showIndent(outfile, level)
            outfile.write('level=XSDataString(\n')
            self.level.exportLiteral(outfile, level, name_='level')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.text:
            showIndent(outfile, level)
            outfile.write('text=XSDataString(\n')
            self.text.exportLiteral(outfile, level, name_='text')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.typexx:
            showIndent(outfile, level)
            outfile.write('typexx=XSDataString(\n')
            self.typexx.exportLiteral(outfile, level, name_='type')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'debuginfo':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDebuginfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'level':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setLevel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'text':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setText(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setType(obj_)
# end class XSDataMessage


class XSDataResult(XSData):
    subclass = None
    def __init__(self, valueOf_=''):
        XSData.__init__(self)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataResult.subclass:
            return XSDataResult.subclass(*args_, **kwargs_)
        else:
            return XSDataResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataResult'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResult'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataResult')
    def exportChildren(self, outfile, level, name_='XSDataResult'):
        XSData.exportChildren(self, outfile, level, name_)
        outfile.write(self.valueOf_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class XSDataResult


class XSDataRotation(XSData):
    subclass = None
    def __init__(self, q0=0.0, q1=0.0, q2=0.0, q3=0.0):
        XSData.__init__(self)
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
    def factory(*args_, **kwargs_):
        if XSDataRotation.subclass:
            return XSDataRotation.subclass(*args_, **kwargs_)
        else:
            return XSDataRotation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getQ0(self): return self.q0
    def setQ0(self, q0): self.q0 = q0
    def getQ1(self): return self.q1
    def setQ1(self, q1): self.q1 = q1
    def getQ2(self): return self.q2
    def setQ2(self, q2): self.q2 = q2
    def getQ3(self): return self.q3
    def setQ3(self, q3): self.q3 = q3
    def export(self, outfile, level, name_='XSDataRotation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataRotation'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataRotation')
    def exportChildren(self, outfile, level, name_='XSDataRotation'):
        showIndent(outfile, level)
        outfile.write('<q0>%e</q0>\n' % self.getQ0())
        showIndent(outfile, level)
        outfile.write('<q1>%e</q1>\n' % self.getQ1())
        showIndent(outfile, level)
        outfile.write('<q2>%e</q2>\n' % self.getQ2())
        showIndent(outfile, level)
        outfile.write('<q3>%e</q3>\n' % self.getQ3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataRotation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRotation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRotation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataRotation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataRotation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('q0=%e,\n' % self.getQ0())
        showIndent(outfile, level)
        outfile.write('q1=%e,\n' % self.getQ1())
        showIndent(outfile, level)
        outfile.write('q2=%e,\n' % self.getQ2())
        showIndent(outfile, level)
        outfile.write('q3=%e,\n' % self.getQ3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q0':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q0 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q3 = fval_
# end class XSDataRotation


class XSDataSize(XSData):
    subclass = None
    def __init__(self, x=None, y=None, z=None):
        XSData.__init__(self)
        self.x = x
        self.y = y
        self.z = z
    def factory(*args_, **kwargs_):
        if XSDataSize.subclass:
            return XSDataSize.subclass(*args_, **kwargs_)
        else:
            return XSDataSize(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getX(self): return self.x
    def setX(self, x): self.x = x
    def getY(self): return self.y
    def setY(self, y): self.y = y
    def getZ(self): return self.z
    def setZ(self, z): self.z = z
    def export(self, outfile, level, name_='XSDataSize'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSize'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSize')
    def exportChildren(self, outfile, level, name_='XSDataSize'):
        if self.x:
            self.x.export(outfile, level, name_='x')
        if self.y:
            self.y.export(outfile, level, name_='y')
        if self.z:
            self.z.export(outfile, level, name_='z')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSize' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSize.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSize.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSize" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSize'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.x:
            showIndent(outfile, level)
            outfile.write('x=XSDataLength(\n')
            self.x.exportLiteral(outfile, level, name_='x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.y:
            showIndent(outfile, level)
            outfile.write('y=XSDataLength(\n')
            self.y.exportLiteral(outfile, level, name_='y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.z:
            showIndent(outfile, level)
            outfile.write('z=XSDataLength(\n')
            self.z.exportLiteral(outfile, level, name_='z')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'z':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setZ(obj_)
# end class XSDataSize


class XSDataSpeed(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataSpeed.subclass:
            return XSDataSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSpeed'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataSpeed')
    def exportChildren(self, outfile, level, name_='XSDataSpeed'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSpeed' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSpeed" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSpeed'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataSpeed


class XSDataStatus(XSData):
    subclass = None
    def __init__(self, executiveSummary=None, isSuccess=None, executionInfo=None):
        XSData.__init__(self)
        self.executiveSummary = executiveSummary
        self.isSuccess = isSuccess
        self.executionInfo = executionInfo
    def factory(*args_, **kwargs_):
        if XSDataStatus.subclass:
            return XSDataStatus.subclass(*args_, **kwargs_)
        else:
            return XSDataStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExecutiveSummary(self): return self.executiveSummary
    def setExecutiveSummary(self, executiveSummary): self.executiveSummary = executiveSummary
    def getIsSuccess(self): return self.isSuccess
    def setIsSuccess(self, isSuccess): self.isSuccess = isSuccess
    def getExecutionInfo(self): return self.executionInfo
    def setExecutionInfo(self, executionInfo): self.executionInfo = executionInfo
    def export(self, outfile, level, name_='XSDataStatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatus'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatus')
    def exportChildren(self, outfile, level, name_='XSDataStatus'):
        if self.getExecutiveSummary() != None :
            if self.executiveSummary:
                self.executiveSummary.export(outfile, level, name_='executiveSummary')
        if self.isSuccess:
            self.isSuccess.export(outfile, level, name_='isSuccess')
        if self.getExecutionInfo() != None :
            if self.executionInfo:
                self.executionInfo.export(outfile, level, name_='executionInfo')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatus' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatus'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.executiveSummary:
            showIndent(outfile, level)
            outfile.write('executiveSummary=XSDataString(\n')
            self.executiveSummary.exportLiteral(outfile, level, name_='executiveSummary')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.isSuccess:
            showIndent(outfile, level)
            outfile.write('isSuccess=XSDataBoolean(\n')
            self.isSuccess.exportLiteral(outfile, level, name_='isSuccess')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.executionInfo:
            showIndent(outfile, level)
            outfile.write('executionInfo=XSDataExecutionInfo(\n')
            self.executionInfo.exportLiteral(outfile, level, name_='executionInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executiveSummary':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setExecutiveSummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isSuccess':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setIsSuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executionInfo':
            obj_ = XSDataExecutionInfo.factory()
            obj_.build(child_)
            self.setExecutionInfo(obj_)
# end class XSDataStatus


class XSDataString(XSData):
    subclass = None
    def __init__(self, value=''):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataString.subclass:
            return XSDataString.subclass(*args_, **kwargs_)
        else:
            return XSDataString(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataString'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataString'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataString')
    def exportChildren(self, outfile, level, name_='XSDataString'):
        showIndent(outfile, level)
        outfile.write('<value>%s</value>\n' % quote_xml(self.getValue()))
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataString' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataString.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataString.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataString" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataString'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%s,\n' % quote_python(self.getValue()))
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            value_ = ''
            for text__content_ in child_.childNodes:
                value_ += text__content_.nodeValue
            self.value = value_
# end class XSDataString


class XSDataSysteminfo(XSData):
    subclass = None
    def __init__(self, compiler=None, hostIP=None, hostName=None, operatingSystem=None, operatingSystemType=None, userName=None, virtualMachine=None):
        XSData.__init__(self)
        self.compiler = compiler
        self.hostIP = hostIP
        self.hostName = hostName
        self.operatingSystem = operatingSystem
        self.operatingSystemType = operatingSystemType
        self.userName = userName
        self.virtualMachine = virtualMachine
    def factory(*args_, **kwargs_):
        if XSDataSysteminfo.subclass:
            return XSDataSysteminfo.subclass(*args_, **kwargs_)
        else:
            return XSDataSysteminfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCompiler(self): return self.compiler
    def setCompiler(self, compiler): self.compiler = compiler
    def getHostIP(self): return self.hostIP
    def setHostIP(self, hostIP): self.hostIP = hostIP
    def getHostName(self): return self.hostName
    def setHostName(self, hostName): self.hostName = hostName
    def getOperatingSystem(self): return self.operatingSystem
    def setOperatingSystem(self, operatingSystem): self.operatingSystem = operatingSystem
    def getOperatingSystemType(self): return self.operatingSystemType
    def setOperatingSystemType(self, operatingSystemType): self.operatingSystemType = operatingSystemType
    def getUserName(self): return self.userName
    def setUserName(self, userName): self.userName = userName
    def getVirtualMachine(self): return self.virtualMachine
    def setVirtualMachine(self, virtualMachine): self.virtualMachine = virtualMachine
    def export(self, outfile, level, name_='XSDataSysteminfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSysteminfo'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSysteminfo')
    def exportChildren(self, outfile, level, name_='XSDataSysteminfo'):
        if self.compiler:
            self.compiler.export(outfile, level, name_='compiler')
        if self.hostIP:
            self.hostIP.export(outfile, level, name_='hostIP')
        if self.hostName:
            self.hostName.export(outfile, level, name_='hostName')
        if self.operatingSystem:
            self.operatingSystem.export(outfile, level, name_='operatingSystem')
        if self.operatingSystemType:
            self.operatingSystemType.export(outfile, level, name_='operatingSystemType')
        if self.userName:
            self.userName.export(outfile, level, name_='userName')
        if self.virtualMachine:
            self.virtualMachine.export(outfile, level, name_='virtualMachine')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSysteminfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSysteminfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSysteminfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSysteminfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSysteminfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.compiler:
            showIndent(outfile, level)
            outfile.write('compiler=XSDataString(\n')
            self.compiler.exportLiteral(outfile, level, name_='compiler')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.hostIP:
            showIndent(outfile, level)
            outfile.write('hostIP=XSDataString(\n')
            self.hostIP.exportLiteral(outfile, level, name_='hostIP')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.hostName:
            showIndent(outfile, level)
            outfile.write('hostName=XSDataString(\n')
            self.hostName.exportLiteral(outfile, level, name_='hostName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.operatingSystem:
            showIndent(outfile, level)
            outfile.write('operatingSystem=XSDataString(\n')
            self.operatingSystem.exportLiteral(outfile, level, name_='operatingSystem')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.operatingSystemType:
            showIndent(outfile, level)
            outfile.write('operatingSystemType=XSDataString(\n')
            self.operatingSystemType.exportLiteral(outfile, level, name_='operatingSystemType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.userName:
            showIndent(outfile, level)
            outfile.write('userName=XSDataString(\n')
            self.userName.exportLiteral(outfile, level, name_='userName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.virtualMachine:
            showIndent(outfile, level)
            outfile.write('virtualMachine=XSDataString(\n')
            self.virtualMachine.exportLiteral(outfile, level, name_='virtualMachine')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'compiler':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCompiler(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hostIP':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setHostIP(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hostName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setHostName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operatingSystem':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOperatingSystem(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operatingSystemType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOperatingSystemType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'userName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUserName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'virtualMachine':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setVirtualMachine(obj_)
# end class XSDataSysteminfo


class XSDataTime(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataTime.subclass:
            return XSDataTime.subclass(*args_, **kwargs_)
        else:
            return XSDataTime(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataTime'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataTime'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataTime')
    def exportChildren(self, outfile, level, name_='XSDataTime'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataTime' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataTime.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataTime.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataTime" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataTime'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataTime


class XSDataVectorDouble(XSData):
    subclass = None
    def __init__(self, v1=0.0, v2=0.0, v3=0.0):
        XSData.__init__(self)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def factory(*args_, **kwargs_):
        if XSDataVectorDouble.subclass:
            return XSDataVectorDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataVectorDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getV3(self): return self.v3
    def setV3(self, v3): self.v3 = v3
    def export(self, outfile, level, name_='XSDataVectorDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataVectorDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataVectorDouble')
    def exportChildren(self, outfile, level, name_='XSDataVectorDouble'):
        showIndent(outfile, level)
        outfile.write('<v1>%e</v1>\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('<v2>%e</v2>\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('<v3>%e</v3>\n' % self.getV3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataVectorDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataVectorDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataVectorDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataVectorDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataVectorDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%e,\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('v2=%e,\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('v3=%e,\n' % self.getV3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v3 = fval_
# end class XSDataVectorDouble


class XSDataVectorInteger(XSData):
    subclass = None
    def __init__(self, v1=-1, v2=-1, v3=-1):
        XSData.__init__(self)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def factory(*args_, **kwargs_):
        if XSDataVectorInteger.subclass:
            return XSDataVectorInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataVectorInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getV3(self): return self.v3
    def setV3(self, v3): self.v3 = v3
    def export(self, outfile, level, name_='XSDataVectorInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataVectorInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataVectorInteger')
    def exportChildren(self, outfile, level, name_='XSDataVectorInteger'):
        showIndent(outfile, level)
        outfile.write('<v1>%d</v1>\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('<v2>%d</v2>\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('<v3>%d</v3>\n' % self.getV3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataVectorInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataVectorInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataVectorInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataVectorInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataVectorInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%d,\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('v2=%d,\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('v3=%d,\n' % self.getV3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v1 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v2 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v3 = ival_
# end class XSDataVectorInteger


class XSDataWavelength(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataWavelength.subclass:
            return XSDataWavelength.subclass(*args_, **kwargs_)
        else:
            return XSDataWavelength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataWavelength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataWavelength'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataWavelength')
    def exportChildren(self, outfile, level, name_='XSDataWavelength'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataWavelength' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataWavelength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataWavelength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataWavelength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataWavelength'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataWavelength


class XSOptionItem:
    subclass = None
    def __init__(self, enabled=0, name=''):
        self.enabled = enabled
        self.name = name
    def factory(*args_, **kwargs_):
        if XSOptionItem.subclass:
            return XSOptionItem.subclass(*args_, **kwargs_)
        else:
            return XSOptionItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getEnabled(self): return self.enabled
    def setEnabled(self, enabled): self.enabled = enabled
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def export(self, outfile, level, name_='XSOptionItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSOptionItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSOptionItem'):
        showIndent(outfile, level)
        outfile.write('<enabled>%d</enabled>\n' % self.getEnabled())
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSOptionItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSOptionItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSOptionItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSOptionItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSOptionItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('enabled=%d,\n' % self.getEnabled())
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enabled':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('true', '1'):
                    ival_ = 1
                elif sval_ in ('false', '0'):
                    ival_ = 0
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self.enabled = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
# end class XSOptionItem


class XSOptionList:
    subclass = None
    def __init__(self, XSOptionItem=None):
        if XSOptionItem is None:
            self.XSOptionItem = []
        else:
            self.XSOptionItem = XSOptionItem
    def factory(*args_, **kwargs_):
        if XSOptionList.subclass:
            return XSOptionList.subclass(*args_, **kwargs_)
        else:
            return XSOptionList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSOptionItem(self): return self.XSOptionItem
    def setXSOptionItem(self, XSOptionItem): self.XSOptionItem = XSOptionItem
    def addXSOptionItem(self, value): self.XSOptionItem.append(value)
    def insertXSOptionItem(self, index, value): self.XSOptionItem[index] = value
    def export(self, outfile, level, name_='XSOptionList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSOptionList'):
        pass
    def exportChildren(self, outfile, level, name_='XSOptionList'):
        for XSOptionItem_ in self.getXSOptionItem():
            XSOptionItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSOptionList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSOptionList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSOptionList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSOptionList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSOptionList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSOptionItem=[\n')
        level += 1
        for XSOptionItem in self.XSOptionItem:
            showIndent(outfile, level)
            outfile.write('XSOptionItem(\n')
            XSOptionItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSOptionItem':
            obj_ = XSOptionItem.factory()
            obj_.build(child_)
            self.XSOptionItem.append(obj_)
# end class XSOptionList


class XSParamItem:
    subclass = None
    def __init__(self, name='', value=''):
        self.name = name
        self.value = value
    def factory(*args_, **kwargs_):
        if XSParamItem.subclass:
            return XSParamItem.subclass(*args_, **kwargs_)
        else:
            return XSParamItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSParamItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSParamItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSParamItem'):
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))
        showIndent(outfile, level)
        outfile.write('<value>%s</value>\n' % quote_xml(self.getValue()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSParamItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSParamItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSParamItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSParamItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSParamItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
        showIndent(outfile, level)
        outfile.write('value=%s,\n' % quote_python(self.getValue()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            value_ = ''
            for text__content_ in child_.childNodes:
                value_ += text__content_.nodeValue
            self.value = value_
# end class XSParamItem


class XSParamList:
    subclass = None
    def __init__(self, XSParamItem=None):
        if XSParamItem is None:
            self.XSParamItem = []
        else:
            self.XSParamItem = XSParamItem
    def factory(*args_, **kwargs_):
        if XSParamList.subclass:
            return XSParamList.subclass(*args_, **kwargs_)
        else:
            return XSParamList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSParamItem(self): return self.XSParamItem
    def setXSParamItem(self, XSParamItem): self.XSParamItem = XSParamItem
    def addXSParamItem(self, value): self.XSParamItem.append(value)
    def insertXSParamItem(self, index, value): self.XSParamItem[index] = value
    def export(self, outfile, level, name_='XSParamList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSParamList'):
        pass
    def exportChildren(self, outfile, level, name_='XSParamList'):
        for XSParamItem_ in self.getXSParamItem():
            XSParamItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSParamList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSParamList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSParamList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSParamList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSParamList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSParamItem=[\n')
        level += 1
        for XSParamItem in self.XSParamItem:
            showIndent(outfile, level)
            outfile.write('XSParamItem(\n')
            XSParamItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSParamItem':
            obj_ = XSParamItem.factory()
            obj_.build(child_)
            self.XSParamItem.append(obj_)
# end class XSParamList


class XSPluginItem:
    subclass = None
    def __init__(self, name='', XSParamList=None, XSOptionList=None):
        self.name = name
        self.XSParamList = XSParamList
        self.XSOptionList = XSOptionList
    def factory(*args_, **kwargs_):
        if XSPluginItem.subclass:
            return XSPluginItem.subclass(*args_, **kwargs_)
        else:
            return XSPluginItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getXSParamList(self): return self.XSParamList
    def setXSParamList(self, XSParamList): self.XSParamList = XSParamList
    def getXSOptionList(self): return self.XSOptionList
    def setXSOptionList(self, XSOptionList): self.XSOptionList = XSOptionList
    def export(self, outfile, level, name_='XSPluginItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSPluginItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSPluginItem'):
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))
        if self.getXSParamList() != None :
            if self.XSParamList:
                self.XSParamList.export(outfile, level)
        if self.getXSOptionList() != None :
            if self.XSOptionList:
                self.XSOptionList.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSPluginItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSPluginItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSPluginItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSPluginItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSPluginItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
        if self.XSParamList:
            showIndent(outfile, level)
            outfile.write('XSParamList=XSParamList(\n')
            self.XSParamList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XSOptionList:
            showIndent(outfile, level)
            outfile.write('XSOptionList=XSOptionList(\n')
            self.XSOptionList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSParamList':
            obj_ = XSParamList.factory()
            obj_.build(child_)
            self.setXSParamList(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSOptionList':
            obj_ = XSOptionList.factory()
            obj_.build(child_)
            self.setXSOptionList(obj_)
# end class XSPluginItem


class XSPluginList:
    subclass = None
    def __init__(self, XSPluginItem=None):
        if XSPluginItem is None:
            self.XSPluginItem = []
        else:
            self.XSPluginItem = XSPluginItem
    def factory(*args_, **kwargs_):
        if XSPluginList.subclass:
            return XSPluginList.subclass(*args_, **kwargs_)
        else:
            return XSPluginList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSPluginItem(self): return self.XSPluginItem
    def setXSPluginItem(self, XSPluginItem): self.XSPluginItem = XSPluginItem
    def addXSPluginItem(self, value): self.XSPluginItem.append(value)
    def insertXSPluginItem(self, index, value): self.XSPluginItem[index] = value
    def export(self, outfile, level, name_='XSPluginList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSPluginList'):
        pass
    def exportChildren(self, outfile, level, name_='XSPluginList'):
        for XSPluginItem_ in self.getXSPluginItem():
            XSPluginItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSPluginList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSPluginList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSPluginList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSPluginList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSPluginList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSPluginItem=[\n')
        level += 1
        for XSPluginItem in self.XSPluginItem:
            showIndent(outfile, level)
            outfile.write('XSPluginItem(\n')
            XSPluginItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSPluginItem':
            obj_ = XSPluginItem.factory()
            obj_.build(child_)
            self.XSPluginItem.append(obj_)
# end class XSPluginList


class XSDataAbsorbedDoseRate(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAbsorbedDoseRate.subclass:
            return XSDataAbsorbedDoseRate.subclass(*args_, **kwargs_)
        else:
            return XSDataAbsorbedDoseRate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate')
    def exportChildren(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAbsorbedDoseRate' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAbsorbedDoseRate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAbsorbedDoseRate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAbsorbedDoseRate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataAbsorbedDoseRate


class XSDataAngle(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDisplacement.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAngle.subclass:
            return XSDataAngle.subclass(*args_, **kwargs_)
        else:
            return XSDataAngle(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAngle'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngle'):
        XSDataDisplacement.exportAttributes(self, outfile, level, name_='XSDataAngle')
    def exportChildren(self, outfile, level, name_='XSDataAngle'):
        XSDataDisplacement.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAngle' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAngle.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAngle.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAngle" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAngle'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDisplacement.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDisplacement.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDisplacement.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDisplacement.buildChildren(self, child_, nodeName_)
# end class XSDataAngle


class XSDataAngularSpeed(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAngularSpeed.subclass:
            return XSDataAngularSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataAngularSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAngularSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngularSpeed'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataAngularSpeed')
    def exportChildren(self, outfile, level, name_='XSDataAngularSpeed'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAngularSpeed' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAngularSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAngularSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAngularSpeed" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAngularSpeed'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataAngularSpeed


class XSDataDate(XSDataString):
    subclass = None
    def __init__(self, value='', valueOf_=''):
        XSDataString.__init__(self, value)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataDate.subclass:
            return XSDataDate.subclass(*args_, **kwargs_)
        else:
            return XSDataDate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataDate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDate'):
        XSDataString.exportAttributes(self, outfile, level, name_='XSDataDate')
    def exportChildren(self, outfile, level, name_='XSDataDate'):
        XSDataString.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDate' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDate'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataString.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataString.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataString.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataString.buildChildren(self, child_, nodeName_)
# end class XSDataDate


class XSDataMatrix(XSDataMatrixDouble):
    subclass = None
    def __init__(self, m11=0.0, m12=0.0, m13=0.0, m21=0.0, m22=0.0, m23=0.0, m31=0.0, m32=0.0, m33=0.0, valueOf_=''):
        XSDataMatrixDouble.__init__(self, m11, m12, m13, m21, m22, m23, m31, m32, m33)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataMatrix.subclass:
            return XSDataMatrix.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataMatrix'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrix'):
        XSDataMatrixDouble.exportAttributes(self, outfile, level, name_='XSDataMatrix')
    def exportChildren(self, outfile, level, name_='XSDataMatrix'):
        XSDataMatrixDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrix' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrix" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrix'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataMatrixDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataMatrixDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataMatrixDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataMatrixDouble.buildChildren(self, child_, nodeName_)
# end class XSDataMatrix


class XSDataUnitVector(XSDataVectorDouble):
    subclass = None
    def __init__(self, v1=0.0, v2=0.0, v3=0.0, valueOf_=''):
        XSDataVectorDouble.__init__(self, v1, v2, v3)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataUnitVector.subclass:
            return XSDataUnitVector.subclass(*args_, **kwargs_)
        else:
            return XSDataUnitVector(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataUnitVector'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataUnitVector'):
        XSDataVectorDouble.exportAttributes(self, outfile, level, name_='XSDataUnitVector')
    def exportChildren(self, outfile, level, name_='XSDataUnitVector'):
        XSDataVectorDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataUnitVector' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataUnitVector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataUnitVector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataUnitVector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataUnitVector'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataVectorDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataVectorDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataVectorDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataVectorDouble.buildChildren(self, child_, nodeName_)
# end class XSDataUnitVector


class XSDataAtomsShift(XSData):
    subclass = None
    def __init__(self, dx=None, dy=None, dz=None):
        XSData.__init__(self)
        self.dx = dx
        self.dy = dy
        self.dz = dz
    def factory(*args_, **kwargs_):
        if XSDataAtomsShift.subclass:
            return XSDataAtomsShift.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomsShift(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDx(self): return self.dx
    def setDx(self, dx): self.dx = dx
    def getDy(self): return self.dy
    def setDy(self, dy): self.dy = dy
    def getDz(self): return self.dz
    def setDz(self, dz): self.dz = dz
    def export(self, outfile, level, name_='XSDataAtomsShift'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomsShift'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomsShift')
    def exportChildren(self, outfile, level, name_='XSDataAtomsShift'):
        if self.dx:
            self.dx.export(outfile, level, name_='dx')
        if self.dy:
            self.dy.export(outfile, level, name_='dy')
        if self.dz:
            self.dz.export(outfile, level, name_='dz')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomsShift' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsShift.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsShift.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomsShift" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomsShift'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dx:
            showIndent(outfile, level)
            outfile.write('dx=XSDataFloat(\n')
            self.dx.exportLiteral(outfile, level, name_='dx')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dy:
            showIndent(outfile, level)
            outfile.write('dy=XSDataFloat(\n')
            self.dy.exportLiteral(outfile, level, name_='dy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dz:
            showIndent(outfile, level)
            outfile.write('dz=XSDataFloat(\n')
            self.dz.exportLiteral(outfile, level, name_='dz')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dx':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDx(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dy':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dz':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDz(obj_)
# end class XSDataAtomsShift


class XSDataAtomsSite(XSData):
    subclass = None
    def __init__(self, typexx=None, x=None, y=None, z=None, tag=None):
        XSData.__init__(self)
        self.typexx = typexx
        self.x = x
        self.y = y
        self.z = z
        self.tag = tag
    def factory(*args_, **kwargs_):
        if XSDataAtomsSite.subclass:
            return XSDataAtomsSite.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomsSite(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def getX(self): return self.x
    def setX(self, x): self.x = x
    def getY(self): return self.y
    def setY(self, y): self.y = y
    def getZ(self): return self.z
    def setZ(self, z): self.z = z
    def getTag(self): return self.tag
    def setTag(self, tag): self.tag = tag
    def export(self, outfile, level, name_='XSDataAtomsSite'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomsSite'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomsSite')
    def exportChildren(self, outfile, level, name_='XSDataAtomsSite'):
        if self.typexx:
            self.typexx.export(outfile, level, name_='type')
        if self.x:
            self.x.export(outfile, level, name_='x')
        if self.y:
            self.y.export(outfile, level, name_='y')
        if self.z:
            self.z.export(outfile, level, name_='z')
        if self.getTag() != None :
            if self.tag:
                self.tag.export(outfile, level, name_='tag')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomsSite' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsSite.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsSite.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomsSite" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomsSite'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.typexx:
            showIndent(outfile, level)
            outfile.write('typexx=XSDataString(\n')
            self.typexx.exportLiteral(outfile, level, name_='type')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.x:
            showIndent(outfile, level)
            outfile.write('x=XSDataFloat(\n')
            self.x.exportLiteral(outfile, level, name_='x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.y:
            showIndent(outfile, level)
            outfile.write('y=XSDataFloat(\n')
            self.y.exportLiteral(outfile, level, name_='y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.z:
            showIndent(outfile, level)
            outfile.write('z=XSDataFloat(\n')
            self.z.exportLiteral(outfile, level, name_='z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.tag:
            showIndent(outfile, level)
            outfile.write('tag=XSDataString(\n')
            self.tag.exportLiteral(outfile, level, name_='tag')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'z':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setZ(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'tag':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTag(obj_)
# end class XSDataAtomsSite


class XSDataAtomsCrystal(XSData):
    subclass = None
    def __init__(self, space=None, a=None, b=None, c=None, alpha=None, beta=None, gamma=None, shift=None):
        XSData.__init__(self)
        self.space = space
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.shift = shift
    def factory(*args_, **kwargs_):
        if XSDataAtomsCrystal.subclass:
            return XSDataAtomsCrystal.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomsCrystal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSpace(self): return self.space
    def setSpace(self, space): self.space = space
    def getA(self): return self.a
    def setA(self, a): self.a = a
    def getB(self): return self.b
    def setB(self, b): self.b = b
    def getC(self): return self.c
    def setC(self, c): self.c = c
    def getAlpha(self): return self.alpha
    def setAlpha(self, alpha): self.alpha = alpha
    def getBeta(self): return self.beta
    def setBeta(self, beta): self.beta = beta
    def getGamma(self): return self.gamma
    def setGamma(self, gamma): self.gamma = gamma
    def getShift(self): return self.shift
    def setShift(self, shift): self.shift = shift
    def export(self, outfile, level, name_='XSDataAtomsCrystal'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomsCrystal'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomsCrystal')
    def exportChildren(self, outfile, level, name_='XSDataAtomsCrystal'):
        if self.space:
            self.space.export(outfile, level, name_='space')
        if self.a:
            self.a.export(outfile, level, name_='a')
        if self.getB() != None :
            if self.b:
                self.b.export(outfile, level, name_='b')
        if self.getC() != None :
            if self.c:
                self.c.export(outfile, level, name_='c')
        if self.getAlpha() != None :
            if self.alpha:
                self.alpha.export(outfile, level, name_='alpha')
        if self.getBeta() != None :
            if self.beta:
                self.beta.export(outfile, level, name_='beta')
        if self.getGamma() != None :
            if self.gamma:
                self.gamma.export(outfile, level, name_='gamma')
        if self.getShift() != None :
            if self.shift:
                self.shift.export(outfile, level, name_='shift')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomsCrystal' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomsCrystal" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomsCrystal'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.space:
            showIndent(outfile, level)
            outfile.write('space=XSDataString(\n')
            self.space.exportLiteral(outfile, level, name_='space')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.a:
            showIndent(outfile, level)
            outfile.write('a=XSDataFloat(\n')
            self.a.exportLiteral(outfile, level, name_='a')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.b:
            showIndent(outfile, level)
            outfile.write('b=XSDataFloat(\n')
            self.b.exportLiteral(outfile, level, name_='b')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.c:
            showIndent(outfile, level)
            outfile.write('c=XSDataFloat(\n')
            self.c.exportLiteral(outfile, level, name_='c')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.alpha:
            showIndent(outfile, level)
            outfile.write('alpha=XSDataFloat(\n')
            self.alpha.exportLiteral(outfile, level, name_='alpha')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beta:
            showIndent(outfile, level)
            outfile.write('beta=XSDataFloat(\n')
            self.beta.exportLiteral(outfile, level, name_='beta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.gamma:
            showIndent(outfile, level)
            outfile.write('gamma=XSDataFloat(\n')
            self.gamma.exportLiteral(outfile, level, name_='gamma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shift:
            showIndent(outfile, level)
            outfile.write('shift=XSDataAtomsShift(\n')
            self.shift.exportLiteral(outfile, level, name_='shift')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'space':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSpace(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'a':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setA(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setB(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'c':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setC(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'alpha':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAlpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beta':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gamma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setGamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shift':
            obj_ = XSDataAtomsShift.factory()
            obj_.build(child_)
            self.setShift(obj_)
# end class XSDataAtomsCrystal


class XSDataAtomsSample(XSData):
    subclass = None
    def __init__(self, core=None, edge=None, rmax=None, nitrogen=None, argon=None, krypton=None):
        XSData.__init__(self)
        self.core = core
        self.edge = edge
        self.rmax = rmax
        self.nitrogen = nitrogen
        self.argon = argon
        self.krypton = krypton
    def factory(*args_, **kwargs_):
        if XSDataAtomsSample.subclass:
            return XSDataAtomsSample.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomsSample(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCore(self): return self.core
    def setCore(self, core): self.core = core
    def getEdge(self): return self.edge
    def setEdge(self, edge): self.edge = edge
    def getRmax(self): return self.rmax
    def setRmax(self, rmax): self.rmax = rmax
    def getNitrogen(self): return self.nitrogen
    def setNitrogen(self, nitrogen): self.nitrogen = nitrogen
    def getArgon(self): return self.argon
    def setArgon(self, argon): self.argon = argon
    def getKrypton(self): return self.krypton
    def setKrypton(self, krypton): self.krypton = krypton
    def export(self, outfile, level, name_='XSDataAtomsSample'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomsSample'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomsSample')
    def exportChildren(self, outfile, level, name_='XSDataAtomsSample'):
        if self.core:
            self.core.export(outfile, level, name_='core')
        if self.getEdge() != None :
            if self.edge:
                self.edge.export(outfile, level, name_='edge')
        if self.getRmax() != None :
            if self.rmax:
                self.rmax.export(outfile, level, name_='rmax')
        if self.getNitrogen() != None :
            if self.nitrogen:
                self.nitrogen.export(outfile, level, name_='nitrogen')
        if self.getArgon() != None :
            if self.argon:
                self.argon.export(outfile, level, name_='argon')
        if self.getKrypton() != None :
            if self.krypton:
                self.krypton.export(outfile, level, name_='krypton')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomsSample' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsSample.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsSample.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomsSample'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.core:
            showIndent(outfile, level)
            outfile.write('core=XSDataString(\n')
            self.core.exportLiteral(outfile, level, name_='core')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.edge:
            showIndent(outfile, level)
            outfile.write('edge=XSDataString(\n')
            self.edge.exportLiteral(outfile, level, name_='edge')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmax:
            showIndent(outfile, level)
            outfile.write('rmax=XSDataFloat(\n')
            self.rmax.exportLiteral(outfile, level, name_='rmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nitrogen:
            showIndent(outfile, level)
            outfile.write('nitrogen=XSDataFloat(\n')
            self.nitrogen.exportLiteral(outfile, level, name_='nitrogen')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.argon:
            showIndent(outfile, level)
            outfile.write('argon=XSDataFloat(\n')
            self.argon.exportLiteral(outfile, level, name_='argon')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.krypton:
            showIndent(outfile, level)
            outfile.write('krypton=XSDataFloat(\n')
            self.krypton.exportLiteral(outfile, level, name_='krypton')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'core':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCore(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'edge':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setEdge(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nitrogen':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNitrogen(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'argon':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setArgon(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'krypton':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKrypton(obj_)
# end class XSDataAtomsSample


class XSDataAtomsFlags(XSData):
    subclass = None
    def __init__(self, index=None, feff=None, feff8=None, corrections=None, geom=None, unit=None, p1=None):
        XSData.__init__(self)
        self.index = index
        self.feff = feff
        self.feff8 = feff8
        self.corrections = corrections
        self.geom = geom
        self.unit = unit
        self.p1 = p1
    def factory(*args_, **kwargs_):
        if XSDataAtomsFlags.subclass:
            return XSDataAtomsFlags.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomsFlags(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getIndex(self): return self.index
    def setIndex(self, index): self.index = index
    def getFeff(self): return self.feff
    def setFeff(self, feff): self.feff = feff
    def getFeff8(self): return self.feff8
    def setFeff8(self, feff8): self.feff8 = feff8
    def getCorrections(self): return self.corrections
    def setCorrections(self, corrections): self.corrections = corrections
    def getGeom(self): return self.geom
    def setGeom(self, geom): self.geom = geom
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getP1(self): return self.p1
    def setP1(self, p1): self.p1 = p1
    def export(self, outfile, level, name_='XSDataAtomsFlags'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomsFlags'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomsFlags')
    def exportChildren(self, outfile, level, name_='XSDataAtomsFlags'):
        if self.getIndex() != None :
            if self.index:
                self.index.export(outfile, level, name_='index')
        if self.getFeff() != None :
            if self.feff:
                self.feff.export(outfile, level, name_='feff')
        if self.getFeff8() != None :
            if self.feff8:
                self.feff8.export(outfile, level, name_='feff8')
        if self.getCorrections() != None :
            if self.corrections:
                self.corrections.export(outfile, level, name_='corrections')
        if self.getGeom() != None :
            if self.geom:
                self.geom.export(outfile, level, name_='geom')
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.getP1() != None :
            if self.p1:
                self.p1.export(outfile, level, name_='p1')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomsFlags' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsFlags.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomsFlags.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomsFlags" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomsFlags'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.index:
            showIndent(outfile, level)
            outfile.write('index=XSDataBoolean(\n')
            self.index.exportLiteral(outfile, level, name_='index')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.feff:
            showIndent(outfile, level)
            outfile.write('feff=XSDataBoolean(\n')
            self.feff.exportLiteral(outfile, level, name_='feff')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.feff8:
            showIndent(outfile, level)
            outfile.write('feff8=XSDataBoolean(\n')
            self.feff8.exportLiteral(outfile, level, name_='feff8')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.corrections:
            showIndent(outfile, level)
            outfile.write('corrections=XSDataBoolean(\n')
            self.corrections.exportLiteral(outfile, level, name_='corrections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.geom:
            showIndent(outfile, level)
            outfile.write('geom=XSDataBoolean(\n')
            self.geom.exportLiteral(outfile, level, name_='geom')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataBoolean(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.p1:
            showIndent(outfile, level)
            outfile.write('p1=XSDataBoolean(\n')
            self.p1.exportLiteral(outfile, level, name_='p1')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'index':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setIndex(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'feff':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setFeff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'feff8':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setFeff8(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'corrections':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setCorrections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'geom':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setGeom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'p1':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setP1(obj_)
# end class XSDataAtomsFlags


class XSDataFeffCardHole(XSData):
    subclass = None
    def __init__(self, ihole=None, s02=None):
        XSData.__init__(self)
        self.ihole = ihole
        self.s02 = s02
    def factory(*args_, **kwargs_):
        if XSDataFeffCardHole.subclass:
            return XSDataFeffCardHole.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardHole(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getIhole(self): return self.ihole
    def setIhole(self, ihole): self.ihole = ihole
    def getS02(self): return self.s02
    def setS02(self, s02): self.s02 = s02
    def export(self, outfile, level, name_='XSDataFeffCardHole'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardHole'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardHole')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardHole'):
        if self.ihole:
            self.ihole.export(outfile, level, name_='ihole')
        if self.s02:
            self.s02.export(outfile, level, name_='s02')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardHole' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardHole.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardHole.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardHole" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardHole'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ihole:
            showIndent(outfile, level)
            outfile.write('ihole=XSDataInteger(\n')
            self.ihole.exportLiteral(outfile, level, name_='ihole')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.s02:
            showIndent(outfile, level)
            outfile.write('s02=XSDataFloat(\n')
            self.s02.exportLiteral(outfile, level, name_='s02')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ihole':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIhole(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 's02':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setS02(obj_)
# end class XSDataFeffCardHole


class XSDataFeffCardCriteria(XSData):
    subclass = None
    def __init__(self, critcw=None, critpw=None):
        XSData.__init__(self)
        self.critcw = critcw
        self.critpw = critpw
    def factory(*args_, **kwargs_):
        if XSDataFeffCardCriteria.subclass:
            return XSDataFeffCardCriteria.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardCriteria(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCritcw(self): return self.critcw
    def setCritcw(self, critcw): self.critcw = critcw
    def getCritpw(self): return self.critpw
    def setCritpw(self, critpw): self.critpw = critpw
    def export(self, outfile, level, name_='XSDataFeffCardCriteria'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardCriteria'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardCriteria')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardCriteria'):
        if self.critcw:
            self.critcw.export(outfile, level, name_='critcw')
        if self.critpw:
            self.critpw.export(outfile, level, name_='critpw')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardCriteria' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardCriteria.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardCriteria.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardCriteria" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardCriteria'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.critcw:
            showIndent(outfile, level)
            outfile.write('critcw=XSDataFloat(\n')
            self.critcw.exportLiteral(outfile, level, name_='critcw')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.critpw:
            showIndent(outfile, level)
            outfile.write('critpw=XSDataFloat(\n')
            self.critpw.exportLiteral(outfile, level, name_='critpw')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'critcw':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCritcw(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'critpw':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCritpw(obj_)
# end class XSDataFeffCardCriteria


class XSDataFeffCardDebye(XSData):
    subclass = None
    def __init__(self, temp=None, tempDebye=None, idwopt=None):
        XSData.__init__(self)
        self.temp = temp
        self.tempDebye = tempDebye
        self.idwopt = idwopt
    def factory(*args_, **kwargs_):
        if XSDataFeffCardDebye.subclass:
            return XSDataFeffCardDebye.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardDebye(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getTemp(self): return self.temp
    def setTemp(self, temp): self.temp = temp
    def getTempDebye(self): return self.tempDebye
    def setTempDebye(self, tempDebye): self.tempDebye = tempDebye
    def getIdwopt(self): return self.idwopt
    def setIdwopt(self, idwopt): self.idwopt = idwopt
    def export(self, outfile, level, name_='XSDataFeffCardDebye'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardDebye'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardDebye')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardDebye'):
        if self.temp:
            self.temp.export(outfile, level, name_='temp')
        if self.tempDebye:
            self.tempDebye.export(outfile, level, name_='tempDebye')
        if self.idwopt:
            self.idwopt.export(outfile, level, name_='idwopt')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardDebye' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardDebye.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardDebye.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardDebye" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardDebye'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.temp:
            showIndent(outfile, level)
            outfile.write('temp=XSDataFloat(\n')
            self.temp.exportLiteral(outfile, level, name_='temp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.tempDebye:
            showIndent(outfile, level)
            outfile.write('tempDebye=XSDataFloat(\n')
            self.tempDebye.exportLiteral(outfile, level, name_='tempDebye')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.idwopt:
            showIndent(outfile, level)
            outfile.write('idwopt=XSDataInteger(\n')
            self.idwopt.exportLiteral(outfile, level, name_='idwopt')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'temp':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTemp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'tempDebye':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTempDebye(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'idwopt':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIdwopt(obj_)
# end class XSDataFeffCardDebye


class XSDataFeffCardControl(XSData):
    subclass = None
    def __init__(self, mphase=None, mpath=None, mfeff=None, mchi=None):
        XSData.__init__(self)
        self.mphase = mphase
        self.mpath = mpath
        self.mfeff = mfeff
        self.mchi = mchi
    def factory(*args_, **kwargs_):
        if XSDataFeffCardControl.subclass:
            return XSDataFeffCardControl.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardControl(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMphase(self): return self.mphase
    def setMphase(self, mphase): self.mphase = mphase
    def getMpath(self): return self.mpath
    def setMpath(self, mpath): self.mpath = mpath
    def getMfeff(self): return self.mfeff
    def setMfeff(self, mfeff): self.mfeff = mfeff
    def getMchi(self): return self.mchi
    def setMchi(self, mchi): self.mchi = mchi
    def export(self, outfile, level, name_='XSDataFeffCardControl'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardControl'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardControl')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardControl'):
        if self.mphase:
            self.mphase.export(outfile, level, name_='mphase')
        if self.mpath:
            self.mpath.export(outfile, level, name_='mpath')
        if self.mfeff:
            self.mfeff.export(outfile, level, name_='mfeff')
        if self.mchi:
            self.mchi.export(outfile, level, name_='mchi')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardControl' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardControl.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardControl.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardControl" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardControl'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.mphase:
            showIndent(outfile, level)
            outfile.write('mphase=XSDataInteger(\n')
            self.mphase.exportLiteral(outfile, level, name_='mphase')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mpath:
            showIndent(outfile, level)
            outfile.write('mpath=XSDataInteger(\n')
            self.mpath.exportLiteral(outfile, level, name_='mpath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mfeff:
            showIndent(outfile, level)
            outfile.write('mfeff=XSDataInteger(\n')
            self.mfeff.exportLiteral(outfile, level, name_='mfeff')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mchi:
            showIndent(outfile, level)
            outfile.write('mchi=XSDataInteger(\n')
            self.mchi.exportLiteral(outfile, level, name_='mchi')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mphase':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMphase(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mpath':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMpath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mfeff':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMfeff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mchi':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMchi(obj_)
# end class XSDataFeffCardControl


class XSDataFeffCardPrint(XSData):
    subclass = None
    def __init__(self, mphase=None, mpath=None, mfeff=None, mchi=None):
        XSData.__init__(self)
        self.mphase = mphase
        self.mpath = mpath
        self.mfeff = mfeff
        self.mchi = mchi
    def factory(*args_, **kwargs_):
        if XSDataFeffCardPrint.subclass:
            return XSDataFeffCardPrint.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardPrint(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMphase(self): return self.mphase
    def setMphase(self, mphase): self.mphase = mphase
    def getMpath(self): return self.mpath
    def setMpath(self, mpath): self.mpath = mpath
    def getMfeff(self): return self.mfeff
    def setMfeff(self, mfeff): self.mfeff = mfeff
    def getMchi(self): return self.mchi
    def setMchi(self, mchi): self.mchi = mchi
    def export(self, outfile, level, name_='XSDataFeffCardPrint'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardPrint'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardPrint')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardPrint'):
        if self.mphase:
            self.mphase.export(outfile, level, name_='mphase')
        if self.mpath:
            self.mpath.export(outfile, level, name_='mpath')
        if self.mfeff:
            self.mfeff.export(outfile, level, name_='mfeff')
        if self.mchi:
            self.mchi.export(outfile, level, name_='mchi')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardPrint' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardPrint.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardPrint.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardPrint" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardPrint'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.mphase:
            showIndent(outfile, level)
            outfile.write('mphase=XSDataInteger(\n')
            self.mphase.exportLiteral(outfile, level, name_='mphase')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mpath:
            showIndent(outfile, level)
            outfile.write('mpath=XSDataInteger(\n')
            self.mpath.exportLiteral(outfile, level, name_='mpath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mfeff:
            showIndent(outfile, level)
            outfile.write('mfeff=XSDataInteger(\n')
            self.mfeff.exportLiteral(outfile, level, name_='mfeff')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mchi:
            showIndent(outfile, level)
            outfile.write('mchi=XSDataInteger(\n')
            self.mchi.exportLiteral(outfile, level, name_='mchi')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mphase':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMphase(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mpath':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMpath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mfeff':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMfeff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mchi':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setMchi(obj_)
# end class XSDataFeffCardPrint


class XSDataFeffCardPotentials(XSData):
    subclass = None
    def __init__(self, ipot=None, Z=None, element=None):
        XSData.__init__(self)
        self.ipot = ipot
        self.Z = Z
        self.element = element
    def factory(*args_, **kwargs_):
        if XSDataFeffCardPotentials.subclass:
            return XSDataFeffCardPotentials.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardPotentials(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getIpot(self): return self.ipot
    def setIpot(self, ipot): self.ipot = ipot
    def getZ(self): return self.Z
    def setZ(self, Z): self.Z = Z
    def getElement(self): return self.element
    def setElement(self, element): self.element = element
    def export(self, outfile, level, name_='XSDataFeffCardPotentials'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardPotentials'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardPotentials')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardPotentials'):
        if self.ipot:
            self.ipot.export(outfile, level, name_='ipot')
        if self.Z:
            self.Z.export(outfile, level, name_='Z')
        if self.element:
            self.element.export(outfile, level, name_='element')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardPotentials' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardPotentials.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardPotentials.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardPotentials" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardPotentials'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ipot:
            showIndent(outfile, level)
            outfile.write('ipot=XSDataInteger(\n')
            self.ipot.exportLiteral(outfile, level, name_='ipot')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Z:
            showIndent(outfile, level)
            outfile.write('Z=XSDataInteger(\n')
            self.Z.exportLiteral(outfile, level, name_='Z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.element:
            showIndent(outfile, level)
            outfile.write('element=XSDataString(\n')
            self.element.exportLiteral(outfile, level, name_='element')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ipot':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIpot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Z':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setZ(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'element':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setElement(obj_)
# end class XSDataFeffCardPotentials


class XSDataFeffCardAtoms(XSData):
    subclass = None
    def __init__(self, x=None, y=None, z=None, ipot=None, tag=None, distance=None):
        XSData.__init__(self)
        self.x = x
        self.y = y
        self.z = z
        self.ipot = ipot
        self.tag = tag
        self.distance = distance
    def factory(*args_, **kwargs_):
        if XSDataFeffCardAtoms.subclass:
            return XSDataFeffCardAtoms.subclass(*args_, **kwargs_)
        else:
            return XSDataFeffCardAtoms(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getX(self): return self.x
    def setX(self, x): self.x = x
    def getY(self): return self.y
    def setY(self, y): self.y = y
    def getZ(self): return self.z
    def setZ(self, z): self.z = z
    def getIpot(self): return self.ipot
    def setIpot(self, ipot): self.ipot = ipot
    def getTag(self): return self.tag
    def setTag(self, tag): self.tag = tag
    def getDistance(self): return self.distance
    def setDistance(self, distance): self.distance = distance
    def export(self, outfile, level, name_='XSDataFeffCardAtoms'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFeffCardAtoms'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFeffCardAtoms')
    def exportChildren(self, outfile, level, name_='XSDataFeffCardAtoms'):
        if self.x:
            self.x.export(outfile, level, name_='x')
        if self.y:
            self.y.export(outfile, level, name_='y')
        if self.z:
            self.z.export(outfile, level, name_='z')
        if self.ipot:
            self.ipot.export(outfile, level, name_='ipot')
        if self.tag:
            self.tag.export(outfile, level, name_='tag')
        if self.distance:
            self.distance.export(outfile, level, name_='distance')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFeffCardAtoms' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFeffCardAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFeffCardAtoms" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFeffCardAtoms'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.x:
            showIndent(outfile, level)
            outfile.write('x=XSDataFloat(\n')
            self.x.exportLiteral(outfile, level, name_='x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.y:
            showIndent(outfile, level)
            outfile.write('y=XSDataFloat(\n')
            self.y.exportLiteral(outfile, level, name_='y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.z:
            showIndent(outfile, level)
            outfile.write('z=XSDataFloat(\n')
            self.z.exportLiteral(outfile, level, name_='z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ipot:
            showIndent(outfile, level)
            outfile.write('ipot=XSDataInteger(\n')
            self.ipot.exportLiteral(outfile, level, name_='ipot')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.tag:
            showIndent(outfile, level)
            outfile.write('tag=XSDataString(\n')
            self.tag.exportLiteral(outfile, level, name_='tag')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.distance:
            showIndent(outfile, level)
            outfile.write('distance=XSDataFloat(\n')
            self.distance.exportLiteral(outfile, level, name_='distance')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'z':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setZ(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ipot':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIpot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'tag':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTag(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDistance(obj_)
# end class XSDataFeffCardAtoms


class XSDataInputFeff(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, file=None, header=None, title=None, hole=None, control=None, printxx=None, rmax=None, nleg=None, potentials=None, atoms=None):
        XSDataInput.__init__(self, configuration)
        self.file = file
        if header is None:
            self.header = []
        else:
            self.header = header
        self.title = title
        self.hole = hole
        self.control = control
        self.printxx = printxx
        self.rmax = rmax
        self.nleg = nleg
        self.potentials = potentials
        if atoms is None:
            self.atoms = []
        else:
            self.atoms = atoms
    def factory(*args_, **kwargs_):
        if XSDataInputFeff.subclass:
            return XSDataInputFeff.subclass(*args_, **kwargs_)
        else:
            return XSDataInputFeff(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFile(self): return self.file
    def setFile(self, file): self.file = file
    def getHeader(self): return self.header
    def setHeader(self, header): self.header = header
    def addHeader(self, value): self.header.append(value)
    def insertHeader(self, index, value): self.header[index] = value
    def getTitle(self): return self.title
    def setTitle(self, title): self.title = title
    def getHole(self): return self.hole
    def setHole(self, hole): self.hole = hole
    def getControl(self): return self.control
    def setControl(self, control): self.control = control
    def getPrint(self): return self.printxx
    def setPrint(self, printxx): self.printxx = printxx
    def getRmax(self): return self.rmax
    def setRmax(self, rmax): self.rmax = rmax
    def getNleg(self): return self.nleg
    def setNleg(self, nleg): self.nleg = nleg
    def getPotentials(self): return self.potentials
    def setPotentials(self, potentials): self.potentials = potentials
    def getAtoms(self): return self.atoms
    def setAtoms(self, atoms): self.atoms = atoms
    def addAtoms(self, value): self.atoms.append(value)
    def insertAtoms(self, index, value): self.atoms[index] = value
    def export(self, outfile, level, name_='XSDataInputFeff'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputFeff'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputFeff')
    def exportChildren(self, outfile, level, name_='XSDataInputFeff'):
        if self.file:
            self.file.export(outfile, level, name_='file')
        for header_ in self.getHeader():
            header_.export(outfile, level, name_='header')
        if self.title:
            self.title.export(outfile, level, name_='title')
        if self.hole:
            self.hole.export(outfile, level, name_='hole')
        if self.control:
            self.control.export(outfile, level, name_='control')
        if self.printxx:
            self.printxx.export(outfile, level, name_='print')
        if self.rmax:
            self.rmax.export(outfile, level, name_='rmax')
        if self.nleg:
            self.nleg.export(outfile, level, name_='nleg')
        if self.potentials:
            self.potentials.export(outfile, level, name_='potentials')
        for atoms_ in self.getAtoms():
            atoms_.export(outfile, level, name_='atoms')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputFeff' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputFeff.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputFeff.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputFeff" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputFeff'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.file:
            showIndent(outfile, level)
            outfile.write('file=XSDataFile(\n')
            self.file.exportLiteral(outfile, level, name_='file')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('header=[\n')
        level += 1
        for header in self.header:
            showIndent(outfile, level)
            outfile.write('XSDataString(\n')
            header.exportLiteral(outfile, level, name_='header')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.title:
            showIndent(outfile, level)
            outfile.write('title=XSDataString(\n')
            self.title.exportLiteral(outfile, level, name_='title')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.hole:
            showIndent(outfile, level)
            outfile.write('hole=XSDataFeffCardHole(\n')
            self.hole.exportLiteral(outfile, level, name_='hole')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.control:
            showIndent(outfile, level)
            outfile.write('control=XSDataFeffCardControl(\n')
            self.control.exportLiteral(outfile, level, name_='control')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.printxx:
            showIndent(outfile, level)
            outfile.write('printxx=XSDataFeffCardPrint(\n')
            self.printxx.exportLiteral(outfile, level, name_='print')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmax:
            showIndent(outfile, level)
            outfile.write('rmax=XSDataFloat(\n')
            self.rmax.exportLiteral(outfile, level, name_='rmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nleg:
            showIndent(outfile, level)
            outfile.write('nleg=XSDataFloat(\n')
            self.nleg.exportLiteral(outfile, level, name_='nleg')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.potentials:
            showIndent(outfile, level)
            outfile.write('potentials=XSDataFeffCardPotentials(\n')
            self.potentials.exportLiteral(outfile, level, name_='potentials')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('atoms=[\n')
        level += 1
        for atoms in self.atoms:
            showIndent(outfile, level)
            outfile.write('XSDataFeffCardAtoms(\n')
            atoms.exportLiteral(outfile, level, name_='atoms')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'file':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'header':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.header.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'title':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTitle(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hole':
            obj_ = XSDataFeffCardHole.factory()
            obj_.build(child_)
            self.setHole(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'control':
            obj_ = XSDataFeffCardControl.factory()
            obj_.build(child_)
            self.setControl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'print':
            obj_ = XSDataFeffCardPrint.factory()
            obj_.build(child_)
            self.setPrint(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nleg':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNleg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'potentials':
            obj_ = XSDataFeffCardPotentials.factory()
            obj_.build(child_)
            self.setPotentials(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'atoms':
            obj_ = XSDataFeffCardAtoms.factory()
            obj_.build(child_)
            self.atoms.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputFeff


class XSDataInputIfeffit(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, scriptFile=None):
        XSDataInput.__init__(self, configuration)
        self.scriptFile = scriptFile
    def factory(*args_, **kwargs_):
        if XSDataInputIfeffit.subclass:
            return XSDataInputIfeffit.subclass(*args_, **kwargs_)
        else:
            return XSDataInputIfeffit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScriptFile(self): return self.scriptFile
    def setScriptFile(self, scriptFile): self.scriptFile = scriptFile
    def export(self, outfile, level, name_='XSDataInputIfeffit'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputIfeffit'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputIfeffit')
    def exportChildren(self, outfile, level, name_='XSDataInputIfeffit'):
        if self.scriptFile:
            self.scriptFile.export(outfile, level, name_='scriptFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputIfeffit' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputIfeffit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputIfeffit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputIfeffit" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputIfeffit'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.scriptFile:
            showIndent(outfile, level)
            outfile.write('scriptFile=XSDataFile(\n')
            self.scriptFile.exportLiteral(outfile, level, name_='scriptFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scriptFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setScriptFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputIfeffit


class XSDataResultIfeffit(XSDataResult):
    subclass = None
    def __init__(self, sessionFile=None):
        XSDataResult.__init__(self)
        self.sessionFile = sessionFile
    def factory(*args_, **kwargs_):
        if XSDataResultIfeffit.subclass:
            return XSDataResultIfeffit.subclass(*args_, **kwargs_)
        else:
            return XSDataResultIfeffit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSessionFile(self): return self.sessionFile
    def setSessionFile(self, sessionFile): self.sessionFile = sessionFile
    def export(self, outfile, level, name_='XSDataResultIfeffit'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultIfeffit'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultIfeffit')
    def exportChildren(self, outfile, level, name_='XSDataResultIfeffit'):
        if self.sessionFile:
            self.sessionFile.export(outfile, level, name_='sessionFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultIfeffit' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultIfeffit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultIfeffit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultIfeffit" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultIfeffit'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.sessionFile:
            showIndent(outfile, level)
            outfile.write('sessionFile=XSDataFile(\n')
            self.sessionFile.exportLiteral(outfile, level, name_='sessionFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSessionFile(obj_)
# end class XSDataResultIfeffit


class XSDataInputPreEdgeSubtraction(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, energy=None, xmu=None, group=None, pre1=None, pre2=None, norm1=None, norm2=None):
        XSDataInput.__init__(self, configuration)
        self.energy = energy
        self.xmu = xmu
        self.group = group
        self.pre1 = pre1
        self.pre2 = pre2
        self.norm1 = norm1
        self.norm2 = norm2
    def factory(*args_, **kwargs_):
        if XSDataInputPreEdgeSubtraction.subclass:
            return XSDataInputPreEdgeSubtraction.subclass(*args_, **kwargs_)
        else:
            return XSDataInputPreEdgeSubtraction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getEnergy(self): return self.energy
    def setEnergy(self, energy): self.energy = energy
    def getXmu(self): return self.xmu
    def setXmu(self, xmu): self.xmu = xmu
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getPre1(self): return self.pre1
    def setPre1(self, pre1): self.pre1 = pre1
    def getPre2(self): return self.pre2
    def setPre2(self, pre2): self.pre2 = pre2
    def getNorm1(self): return self.norm1
    def setNorm1(self, norm1): self.norm1 = norm1
    def getNorm2(self): return self.norm2
    def setNorm2(self, norm2): self.norm2 = norm2
    def export(self, outfile, level, name_='XSDataInputPreEdgeSubtraction'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputPreEdgeSubtraction'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputPreEdgeSubtraction')
    def exportChildren(self, outfile, level, name_='XSDataInputPreEdgeSubtraction'):
        if self.getEnergy() != None :
            if self.energy:
                self.energy.export(outfile, level, name_='energy')
        if self.getXmu() != None :
            if self.xmu:
                self.xmu.export(outfile, level, name_='xmu')
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getPre1() != None :
            if self.pre1:
                self.pre1.export(outfile, level, name_='pre1')
        if self.getPre2() != None :
            if self.pre2:
                self.pre2.export(outfile, level, name_='pre2')
        if self.getNorm1() != None :
            if self.norm1:
                self.norm1.export(outfile, level, name_='norm1')
        if self.getNorm2() != None :
            if self.norm2:
                self.norm2.export(outfile, level, name_='norm2')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputPreEdgeSubtraction' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputPreEdgeSubtraction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputPreEdgeSubtraction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputPreEdgeSubtraction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputPreEdgeSubtraction'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.energy:
            showIndent(outfile, level)
            outfile.write('energy=XSDataString(\n')
            self.energy.exportLiteral(outfile, level, name_='energy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.xmu:
            showIndent(outfile, level)
            outfile.write('xmu=XSDataString(\n')
            self.xmu.exportLiteral(outfile, level, name_='xmu')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pre1:
            showIndent(outfile, level)
            outfile.write('pre1=XSDataFloat(\n')
            self.pre1.exportLiteral(outfile, level, name_='pre1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pre2:
            showIndent(outfile, level)
            outfile.write('pre2=XSDataFloat(\n')
            self.pre2.exportLiteral(outfile, level, name_='pre2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.norm1:
            showIndent(outfile, level)
            outfile.write('norm1=XSDataFloat(\n')
            self.norm1.exportLiteral(outfile, level, name_='norm1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.norm2:
            showIndent(outfile, level)
            outfile.write('norm2=XSDataFloat(\n')
            self.norm2.exportLiteral(outfile, level, name_='norm2')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'energy':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setEnergy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmu':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setXmu(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pre1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPre1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pre2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPre2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'norm1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNorm1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'norm2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNorm2(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputPreEdgeSubtraction


class XSDataResultPreEdgeSubtraction(XSDataResult):
    subclass = None
    def __init__(self, group=None, e0=None, pre1=None, pre2=None, norm1=None, norm2=None, edgeStep=None, preSlope=None, preOffset=None, preEdgeData=None):
        XSDataResult.__init__(self)
        self.group = group
        self.e0 = e0
        self.pre1 = pre1
        self.pre2 = pre2
        self.norm1 = norm1
        self.norm2 = norm2
        self.edgeStep = edgeStep
        self.preSlope = preSlope
        self.preOffset = preOffset
        if preEdgeData is None:
            self.preEdgeData = []
        else:
            self.preEdgeData = preEdgeData
    def factory(*args_, **kwargs_):
        if XSDataResultPreEdgeSubtraction.subclass:
            return XSDataResultPreEdgeSubtraction.subclass(*args_, **kwargs_)
        else:
            return XSDataResultPreEdgeSubtraction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getE0(self): return self.e0
    def setE0(self, e0): self.e0 = e0
    def getPre1(self): return self.pre1
    def setPre1(self, pre1): self.pre1 = pre1
    def getPre2(self): return self.pre2
    def setPre2(self, pre2): self.pre2 = pre2
    def getNorm1(self): return self.norm1
    def setNorm1(self, norm1): self.norm1 = norm1
    def getNorm2(self): return self.norm2
    def setNorm2(self, norm2): self.norm2 = norm2
    def getEdgeStep(self): return self.edgeStep
    def setEdgeStep(self, edgeStep): self.edgeStep = edgeStep
    def getPreSlope(self): return self.preSlope
    def setPreSlope(self, preSlope): self.preSlope = preSlope
    def getPreOffset(self): return self.preOffset
    def setPreOffset(self, preOffset): self.preOffset = preOffset
    def getPreEdgeData(self): return self.preEdgeData
    def setPreEdgeData(self, preEdgeData): self.preEdgeData = preEdgeData
    def addPreEdgeData(self, value): self.preEdgeData.append(value)
    def insertPreEdgeData(self, index, value): self.preEdgeData[index] = value
    def export(self, outfile, level, name_='XSDataResultPreEdgeSubtraction'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultPreEdgeSubtraction'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultPreEdgeSubtraction')
    def exportChildren(self, outfile, level, name_='XSDataResultPreEdgeSubtraction'):
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getE0() != None :
            if self.e0:
                self.e0.export(outfile, level, name_='e0')
        if self.getPre1() != None :
            if self.pre1:
                self.pre1.export(outfile, level, name_='pre1')
        if self.getPre2() != None :
            if self.pre2:
                self.pre2.export(outfile, level, name_='pre2')
        if self.getNorm1() != None :
            if self.norm1:
                self.norm1.export(outfile, level, name_='norm1')
        if self.getNorm2() != None :
            if self.norm2:
                self.norm2.export(outfile, level, name_='norm2')
        if self.getEdgeStep() != None :
            if self.edgeStep:
                self.edgeStep.export(outfile, level, name_='edgeStep')
        if self.getPreSlope() != None :
            if self.preSlope:
                self.preSlope.export(outfile, level, name_='preSlope')
        if self.getPreOffset() != None :
            if self.preOffset:
                self.preOffset.export(outfile, level, name_='preOffset')
        for preEdgeData_ in self.getPreEdgeData():
            preEdgeData_.export(outfile, level, name_='preEdgeData')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultPreEdgeSubtraction' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultPreEdgeSubtraction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultPreEdgeSubtraction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultPreEdgeSubtraction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultPreEdgeSubtraction'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e0:
            showIndent(outfile, level)
            outfile.write('e0=XSDataFloat(\n')
            self.e0.exportLiteral(outfile, level, name_='e0')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pre1:
            showIndent(outfile, level)
            outfile.write('pre1=XSDataFloat(\n')
            self.pre1.exportLiteral(outfile, level, name_='pre1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pre2:
            showIndent(outfile, level)
            outfile.write('pre2=XSDataFloat(\n')
            self.pre2.exportLiteral(outfile, level, name_='pre2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.norm1:
            showIndent(outfile, level)
            outfile.write('norm1=XSDataFloat(\n')
            self.norm1.exportLiteral(outfile, level, name_='norm1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.norm2:
            showIndent(outfile, level)
            outfile.write('norm2=XSDataFloat(\n')
            self.norm2.exportLiteral(outfile, level, name_='norm2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.edgeStep:
            showIndent(outfile, level)
            outfile.write('edgeStep=XSDataFloat(\n')
            self.edgeStep.exportLiteral(outfile, level, name_='edgeStep')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.preSlope:
            showIndent(outfile, level)
            outfile.write('preSlope=XSDataFloat(\n')
            self.preSlope.exportLiteral(outfile, level, name_='preSlope')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.preOffset:
            showIndent(outfile, level)
            outfile.write('preOffset=XSDataFloat(\n')
            self.preOffset.exportLiteral(outfile, level, name_='preOffset')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('preEdgeData=[\n')
        level += 1
        for preEdgeData in self.preEdgeData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            preEdgeData.exportLiteral(outfile, level, name_='preEdgeData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pre1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPre1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pre2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPre2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'norm1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNorm1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'norm2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNorm2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'edgeStep':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setEdgeStep(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preSlope':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPreSlope(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preOffset':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPreOffset(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preEdgeData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.preEdgeData.append(obj_)
# end class XSDataResultPreEdgeSubtraction


class XSDataResultNormalization(XSDataResult):
    subclass = None
    def __init__(self, group=None, normC0=None, normC1=None, normC2=None, normData=None):
        XSDataResult.__init__(self)
        self.group = group
        self.normC0 = normC0
        self.normC1 = normC1
        self.normC2 = normC2
        if normData is None:
            self.normData = []
        else:
            self.normData = normData
    def factory(*args_, **kwargs_):
        if XSDataResultNormalization.subclass:
            return XSDataResultNormalization.subclass(*args_, **kwargs_)
        else:
            return XSDataResultNormalization(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getNormC0(self): return self.normC0
    def setNormC0(self, normC0): self.normC0 = normC0
    def getNormC1(self): return self.normC1
    def setNormC1(self, normC1): self.normC1 = normC1
    def getNormC2(self): return self.normC2
    def setNormC2(self, normC2): self.normC2 = normC2
    def getNormData(self): return self.normData
    def setNormData(self, normData): self.normData = normData
    def addNormData(self, value): self.normData.append(value)
    def insertNormData(self, index, value): self.normData[index] = value
    def export(self, outfile, level, name_='XSDataResultNormalization'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultNormalization'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultNormalization')
    def exportChildren(self, outfile, level, name_='XSDataResultNormalization'):
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getNormC0() != None :
            if self.normC0:
                self.normC0.export(outfile, level, name_='normC0')
        if self.getNormC1() != None :
            if self.normC1:
                self.normC1.export(outfile, level, name_='normC1')
        if self.getNormC2() != None :
            if self.normC2:
                self.normC2.export(outfile, level, name_='normC2')
        for normData_ in self.getNormData():
            normData_.export(outfile, level, name_='normData')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultNormalization' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultNormalization.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultNormalization.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultNormalization" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultNormalization'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.normC0:
            showIndent(outfile, level)
            outfile.write('normC0=XSDataFloat(\n')
            self.normC0.exportLiteral(outfile, level, name_='normC0')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.normC1:
            showIndent(outfile, level)
            outfile.write('normC1=XSDataFloat(\n')
            self.normC1.exportLiteral(outfile, level, name_='normC1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.normC2:
            showIndent(outfile, level)
            outfile.write('normC2=XSDataFloat(\n')
            self.normC2.exportLiteral(outfile, level, name_='normC2')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('normData=[\n')
        level += 1
        for normData in self.normData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            normData.exportLiteral(outfile, level, name_='normData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normC0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNormC0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normC1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNormC1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normC2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNormC2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.normData.append(obj_)
# end class XSDataResultNormalization


class XSDataInputSpline(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, energy=None, xmu=None, group=None, e0=None, rbkg=None, toler=None, nKnots=None, kminSpl=None, kmaxSpl=None, kweightSpl=None, dk1Spl=None, dk2Spl=None, kwindow=None):
        XSDataInput.__init__(self, configuration)
        self.energy = energy
        self.xmu = xmu
        self.group = group
        self.e0 = e0
        self.rbkg = rbkg
        self.toler = toler
        self.nKnots = nKnots
        self.kminSpl = kminSpl
        self.kmaxSpl = kmaxSpl
        self.kweightSpl = kweightSpl
        self.dk1Spl = dk1Spl
        self.dk2Spl = dk2Spl
        self.kwindow = kwindow
    def factory(*args_, **kwargs_):
        if XSDataInputSpline.subclass:
            return XSDataInputSpline.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSpline(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getEnergy(self): return self.energy
    def setEnergy(self, energy): self.energy = energy
    def getXmu(self): return self.xmu
    def setXmu(self, xmu): self.xmu = xmu
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getE0(self): return self.e0
    def setE0(self, e0): self.e0 = e0
    def getRbkg(self): return self.rbkg
    def setRbkg(self, rbkg): self.rbkg = rbkg
    def getToler(self): return self.toler
    def setToler(self, toler): self.toler = toler
    def getNKnots(self): return self.nKnots
    def setNKnots(self, nKnots): self.nKnots = nKnots
    def getKminSpl(self): return self.kminSpl
    def setKminSpl(self, kminSpl): self.kminSpl = kminSpl
    def getKmaxSpl(self): return self.kmaxSpl
    def setKmaxSpl(self, kmaxSpl): self.kmaxSpl = kmaxSpl
    def getKweightSpl(self): return self.kweightSpl
    def setKweightSpl(self, kweightSpl): self.kweightSpl = kweightSpl
    def getDk1Spl(self): return self.dk1Spl
    def setDk1Spl(self, dk1Spl): self.dk1Spl = dk1Spl
    def getDk2Spl(self): return self.dk2Spl
    def setDk2Spl(self, dk2Spl): self.dk2Spl = dk2Spl
    def getKwindow(self): return self.kwindow
    def setKwindow(self, kwindow): self.kwindow = kwindow
    def export(self, outfile, level, name_='XSDataInputSpline'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSpline'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSpline')
    def exportChildren(self, outfile, level, name_='XSDataInputSpline'):
        if self.getEnergy() != None :
            if self.energy:
                self.energy.export(outfile, level, name_='energy')
        if self.getXmu() != None :
            if self.xmu:
                self.xmu.export(outfile, level, name_='xmu')
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getE0() != None :
            if self.e0:
                self.e0.export(outfile, level, name_='e0')
        if self.getRbkg() != None :
            if self.rbkg:
                self.rbkg.export(outfile, level, name_='rbkg')
        if self.getToler() != None :
            if self.toler:
                self.toler.export(outfile, level, name_='toler')
        if self.getNKnots() != None :
            if self.nKnots:
                self.nKnots.export(outfile, level, name_='nKnots')
        if self.getKminSpl() != None :
            if self.kminSpl:
                self.kminSpl.export(outfile, level, name_='kminSpl')
        if self.getKmaxSpl() != None :
            if self.kmaxSpl:
                self.kmaxSpl.export(outfile, level, name_='kmaxSpl')
        if self.getKweightSpl() != None :
            if self.kweightSpl:
                self.kweightSpl.export(outfile, level, name_='kweightSpl')
        if self.getDk1Spl() != None :
            if self.dk1Spl:
                self.dk1Spl.export(outfile, level, name_='dk1Spl')
        if self.getDk2Spl() != None :
            if self.dk2Spl:
                self.dk2Spl.export(outfile, level, name_='dk2Spl')
        if self.getKwindow() != None :
            if self.kwindow:
                self.kwindow.export(outfile, level, name_='kwindow')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSpline' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSpline.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSpline.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSpline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSpline'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.energy:
            showIndent(outfile, level)
            outfile.write('energy=XSDataString(\n')
            self.energy.exportLiteral(outfile, level, name_='energy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.xmu:
            showIndent(outfile, level)
            outfile.write('xmu=XSDataString(\n')
            self.xmu.exportLiteral(outfile, level, name_='xmu')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e0:
            showIndent(outfile, level)
            outfile.write('e0=XSDataFloat(\n')
            self.e0.exportLiteral(outfile, level, name_='e0')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rbkg:
            showIndent(outfile, level)
            outfile.write('rbkg=XSDataFloat(\n')
            self.rbkg.exportLiteral(outfile, level, name_='rbkg')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.toler:
            showIndent(outfile, level)
            outfile.write('toler=XSDataFloat(\n')
            self.toler.exportLiteral(outfile, level, name_='toler')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nKnots:
            showIndent(outfile, level)
            outfile.write('nKnots=XSDataFloat(\n')
            self.nKnots.exportLiteral(outfile, level, name_='nKnots')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kminSpl:
            showIndent(outfile, level)
            outfile.write('kminSpl=XSDataFloat(\n')
            self.kminSpl.exportLiteral(outfile, level, name_='kminSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmaxSpl:
            showIndent(outfile, level)
            outfile.write('kmaxSpl=XSDataFloat(\n')
            self.kmaxSpl.exportLiteral(outfile, level, name_='kmaxSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kweightSpl:
            showIndent(outfile, level)
            outfile.write('kweightSpl=XSDataFloat(\n')
            self.kweightSpl.exportLiteral(outfile, level, name_='kweightSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk1Spl:
            showIndent(outfile, level)
            outfile.write('dk1Spl=XSDataFloat(\n')
            self.dk1Spl.exportLiteral(outfile, level, name_='dk1Spl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk2Spl:
            showIndent(outfile, level)
            outfile.write('dk2Spl=XSDataFloat(\n')
            self.dk2Spl.exportLiteral(outfile, level, name_='dk2Spl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kwindow:
            showIndent(outfile, level)
            outfile.write('kwindow=XSDataString(\n')
            self.kwindow.exportLiteral(outfile, level, name_='kwindow')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'energy':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setEnergy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xmu':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setXmu(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rbkg':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRbkg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'toler':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setToler(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nKnots':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNKnots(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kminSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKminSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmaxSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmaxSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kweightSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKweightSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk1Spl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk1Spl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk2Spl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk2Spl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kwindow':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKwindow(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSpline


class XSDataInputFFTF(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, real=None, imag=None, k=None, group=None, kmin=None, kmax=None, dk1=None, dk2=None, dk=None, kweight=None, kwindow=None):
        XSDataInput.__init__(self, configuration)
        self.real = real
        self.imag = imag
        self.k = k
        self.group = group
        self.kmin = kmin
        self.kmax = kmax
        self.dk1 = dk1
        self.dk2 = dk2
        self.dk = dk
        self.kweight = kweight
        self.kwindow = kwindow
    def factory(*args_, **kwargs_):
        if XSDataInputFFTF.subclass:
            return XSDataInputFFTF.subclass(*args_, **kwargs_)
        else:
            return XSDataInputFFTF(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getReal(self): return self.real
    def setReal(self, real): self.real = real
    def getImag(self): return self.imag
    def setImag(self, imag): self.imag = imag
    def getK(self): return self.k
    def setK(self, k): self.k = k
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getKmin(self): return self.kmin
    def setKmin(self, kmin): self.kmin = kmin
    def getKmax(self): return self.kmax
    def setKmax(self, kmax): self.kmax = kmax
    def getDk1(self): return self.dk1
    def setDk1(self, dk1): self.dk1 = dk1
    def getDk2(self): return self.dk2
    def setDk2(self, dk2): self.dk2 = dk2
    def getDk(self): return self.dk
    def setDk(self, dk): self.dk = dk
    def getKweight(self): return self.kweight
    def setKweight(self, kweight): self.kweight = kweight
    def getKwindow(self): return self.kwindow
    def setKwindow(self, kwindow): self.kwindow = kwindow
    def export(self, outfile, level, name_='XSDataInputFFTF'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputFFTF'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputFFTF')
    def exportChildren(self, outfile, level, name_='XSDataInputFFTF'):
        if self.getReal() != None :
            if self.real:
                self.real.export(outfile, level, name_='real')
        if self.getImag() != None :
            if self.imag:
                self.imag.export(outfile, level, name_='imag')
        if self.getK() != None :
            if self.k:
                self.k.export(outfile, level, name_='k')
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getKmin() != None :
            if self.kmin:
                self.kmin.export(outfile, level, name_='kmin')
        if self.getKmax() != None :
            if self.kmax:
                self.kmax.export(outfile, level, name_='kmax')
        if self.getDk1() != None :
            if self.dk1:
                self.dk1.export(outfile, level, name_='dk1')
        if self.getDk2() != None :
            if self.dk2:
                self.dk2.export(outfile, level, name_='dk2')
        if self.getDk() != None :
            if self.dk:
                self.dk.export(outfile, level, name_='dk')
        if self.getKweight() != None :
            if self.kweight:
                self.kweight.export(outfile, level, name_='kweight')
        if self.getKwindow() != None :
            if self.kwindow:
                self.kwindow.export(outfile, level, name_='kwindow')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputFFTF' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputFFTF.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputFFTF.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputFFTF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputFFTF'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.real:
            showIndent(outfile, level)
            outfile.write('real=XSDataString(\n')
            self.real.exportLiteral(outfile, level, name_='real')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imag:
            showIndent(outfile, level)
            outfile.write('imag=XSDataString(\n')
            self.imag.exportLiteral(outfile, level, name_='imag')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.k:
            showIndent(outfile, level)
            outfile.write('k=XSDataString(\n')
            self.k.exportLiteral(outfile, level, name_='k')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmin:
            showIndent(outfile, level)
            outfile.write('kmin=XSDataFloat(\n')
            self.kmin.exportLiteral(outfile, level, name_='kmin')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmax:
            showIndent(outfile, level)
            outfile.write('kmax=XSDataFloat(\n')
            self.kmax.exportLiteral(outfile, level, name_='kmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk1:
            showIndent(outfile, level)
            outfile.write('dk1=XSDataFloat(\n')
            self.dk1.exportLiteral(outfile, level, name_='dk1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk2:
            showIndent(outfile, level)
            outfile.write('dk2=XSDataFloat(\n')
            self.dk2.exportLiteral(outfile, level, name_='dk2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk:
            showIndent(outfile, level)
            outfile.write('dk=XSDataFloat(\n')
            self.dk.exportLiteral(outfile, level, name_='dk')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kweight:
            showIndent(outfile, level)
            outfile.write('kweight=XSDataFloat(\n')
            self.kweight.exportLiteral(outfile, level, name_='kweight')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kwindow:
            showIndent(outfile, level)
            outfile.write('kwindow=XSDataString(\n')
            self.kwindow.exportLiteral(outfile, level, name_='kwindow')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'real':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setReal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imag':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setImag(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'k':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setK(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmin':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kweight':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKweight(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kwindow':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKwindow(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputFFTF


class XSDataResultFFTF(XSDataResult):
    subclass = None
    def __init__(self, group=None, kmin=None, kmax=None, dk1=None, dk2=None, kweight=None, rmaxOut=None, winData=None, rData=None, chiRMagData=None, chiRReData=None, chiRImData=None):
        XSDataResult.__init__(self)
        self.group = group
        self.kmin = kmin
        self.kmax = kmax
        self.dk1 = dk1
        self.dk2 = dk2
        self.kweight = kweight
        self.rmaxOut = rmaxOut
        if winData is None:
            self.winData = []
        else:
            self.winData = winData
        if rData is None:
            self.rData = []
        else:
            self.rData = rData
        if chiRMagData is None:
            self.chiRMagData = []
        else:
            self.chiRMagData = chiRMagData
        if chiRReData is None:
            self.chiRReData = []
        else:
            self.chiRReData = chiRReData
        if chiRImData is None:
            self.chiRImData = []
        else:
            self.chiRImData = chiRImData
    def factory(*args_, **kwargs_):
        if XSDataResultFFTF.subclass:
            return XSDataResultFFTF.subclass(*args_, **kwargs_)
        else:
            return XSDataResultFFTF(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getKmin(self): return self.kmin
    def setKmin(self, kmin): self.kmin = kmin
    def getKmax(self): return self.kmax
    def setKmax(self, kmax): self.kmax = kmax
    def getDk1(self): return self.dk1
    def setDk1(self, dk1): self.dk1 = dk1
    def getDk2(self): return self.dk2
    def setDk2(self, dk2): self.dk2 = dk2
    def getKweight(self): return self.kweight
    def setKweight(self, kweight): self.kweight = kweight
    def getRmaxOut(self): return self.rmaxOut
    def setRmaxOut(self, rmaxOut): self.rmaxOut = rmaxOut
    def getWinData(self): return self.winData
    def setWinData(self, winData): self.winData = winData
    def addWinData(self, value): self.winData.append(value)
    def insertWinData(self, index, value): self.winData[index] = value
    def getRData(self): return self.rData
    def setRData(self, rData): self.rData = rData
    def addRData(self, value): self.rData.append(value)
    def insertRData(self, index, value): self.rData[index] = value
    def getChiRMagData(self): return self.chiRMagData
    def setChiRMagData(self, chiRMagData): self.chiRMagData = chiRMagData
    def addChiRMagData(self, value): self.chiRMagData.append(value)
    def insertChiRMagData(self, index, value): self.chiRMagData[index] = value
    def getChiRReData(self): return self.chiRReData
    def setChiRReData(self, chiRReData): self.chiRReData = chiRReData
    def addChiRReData(self, value): self.chiRReData.append(value)
    def insertChiRReData(self, index, value): self.chiRReData[index] = value
    def getChiRImData(self): return self.chiRImData
    def setChiRImData(self, chiRImData): self.chiRImData = chiRImData
    def addChiRImData(self, value): self.chiRImData.append(value)
    def insertChiRImData(self, index, value): self.chiRImData[index] = value
    def export(self, outfile, level, name_='XSDataResultFFTF'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultFFTF'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultFFTF')
    def exportChildren(self, outfile, level, name_='XSDataResultFFTF'):
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getKmin() != None :
            if self.kmin:
                self.kmin.export(outfile, level, name_='kmin')
        if self.getKmax() != None :
            if self.kmax:
                self.kmax.export(outfile, level, name_='kmax')
        if self.getDk1() != None :
            if self.dk1:
                self.dk1.export(outfile, level, name_='dk1')
        if self.getDk2() != None :
            if self.dk2:
                self.dk2.export(outfile, level, name_='dk2')
        if self.getKweight() != None :
            if self.kweight:
                self.kweight.export(outfile, level, name_='kweight')
        if self.getRmaxOut() != None :
            if self.rmaxOut:
                self.rmaxOut.export(outfile, level, name_='rmaxOut')
        for winData_ in self.getWinData():
            winData_.export(outfile, level, name_='winData')
        for rData_ in self.getRData():
            rData_.export(outfile, level, name_='rData')
        for chiRMagData_ in self.getChiRMagData():
            chiRMagData_.export(outfile, level, name_='chiRMagData')
        for chiRReData_ in self.getChiRReData():
            chiRReData_.export(outfile, level, name_='chiRReData')
        for chiRImData_ in self.getChiRImData():
            chiRImData_.export(outfile, level, name_='chiRImData')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultFFTF' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultFFTF.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultFFTF.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultFFTF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultFFTF'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmin:
            showIndent(outfile, level)
            outfile.write('kmin=XSDataFloat(\n')
            self.kmin.exportLiteral(outfile, level, name_='kmin')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmax:
            showIndent(outfile, level)
            outfile.write('kmax=XSDataFloat(\n')
            self.kmax.exportLiteral(outfile, level, name_='kmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk1:
            showIndent(outfile, level)
            outfile.write('dk1=XSDataFloat(\n')
            self.dk1.exportLiteral(outfile, level, name_='dk1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk2:
            showIndent(outfile, level)
            outfile.write('dk2=XSDataFloat(\n')
            self.dk2.exportLiteral(outfile, level, name_='dk2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kweight:
            showIndent(outfile, level)
            outfile.write('kweight=XSDataFloat(\n')
            self.kweight.exportLiteral(outfile, level, name_='kweight')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmaxOut:
            showIndent(outfile, level)
            outfile.write('rmaxOut=XSDataString(\n')
            self.rmaxOut.exportLiteral(outfile, level, name_='rmaxOut')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('winData=[\n')
        level += 1
        for winData in self.winData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            winData.exportLiteral(outfile, level, name_='winData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('rData=[\n')
        level += 1
        for rData in self.rData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            rData.exportLiteral(outfile, level, name_='rData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRMagData=[\n')
        level += 1
        for chiRMagData in self.chiRMagData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRMagData.exportLiteral(outfile, level, name_='chiRMagData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRReData=[\n')
        level += 1
        for chiRReData in self.chiRReData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRReData.exportLiteral(outfile, level, name_='chiRReData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRImData=[\n')
        level += 1
        for chiRImData in self.chiRImData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRImData.exportLiteral(outfile, level, name_='chiRImData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmin':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kweight':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKweight(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmaxOut':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRmaxOut(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'winData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.winData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.rData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRMagData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRMagData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRReData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRReData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRImData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRImData.append(obj_)
# end class XSDataResultFFTF


class XSDataResultSpline(XSDataResult):
    subclass = None
    def __init__(self, group=None, e0=None, rbkg=None, toler=None, nKnots=None, kminSpl=None, kmaxSpl=None, kweightSpl=None, dk1Spl=None, dk2Spl=None, kWindow=None):
        XSDataResult.__init__(self)
        self.group = group
        self.e0 = e0
        self.rbkg = rbkg
        self.toler = toler
        self.nKnots = nKnots
        self.kminSpl = kminSpl
        self.kmaxSpl = kmaxSpl
        self.kweightSpl = kweightSpl
        self.dk1Spl = dk1Spl
        self.dk2Spl = dk2Spl
        self.kWindow = kWindow
    def factory(*args_, **kwargs_):
        if XSDataResultSpline.subclass:
            return XSDataResultSpline.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSpline(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getGroup(self): return self.group
    def setGroup(self, group): self.group = group
    def getE0(self): return self.e0
    def setE0(self, e0): self.e0 = e0
    def getRbkg(self): return self.rbkg
    def setRbkg(self, rbkg): self.rbkg = rbkg
    def getToler(self): return self.toler
    def setToler(self, toler): self.toler = toler
    def getNKnots(self): return self.nKnots
    def setNKnots(self, nKnots): self.nKnots = nKnots
    def getKminSpl(self): return self.kminSpl
    def setKminSpl(self, kminSpl): self.kminSpl = kminSpl
    def getKmaxSpl(self): return self.kmaxSpl
    def setKmaxSpl(self, kmaxSpl): self.kmaxSpl = kmaxSpl
    def getKweightSpl(self): return self.kweightSpl
    def setKweightSpl(self, kweightSpl): self.kweightSpl = kweightSpl
    def getDk1Spl(self): return self.dk1Spl
    def setDk1Spl(self, dk1Spl): self.dk1Spl = dk1Spl
    def getDk2Spl(self): return self.dk2Spl
    def setDk2Spl(self, dk2Spl): self.dk2Spl = dk2Spl
    def getKWindow(self): return self.kWindow
    def setKWindow(self, kWindow): self.kWindow = kWindow
    def export(self, outfile, level, name_='XSDataResultSpline'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSpline'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSpline')
    def exportChildren(self, outfile, level, name_='XSDataResultSpline'):
        if self.getGroup() != None :
            if self.group:
                self.group.export(outfile, level, name_='group')
        if self.getE0() != None :
            if self.e0:
                self.e0.export(outfile, level, name_='e0')
        if self.getRbkg() != None :
            if self.rbkg:
                self.rbkg.export(outfile, level, name_='rbkg')
        if self.getToler() != None :
            if self.toler:
                self.toler.export(outfile, level, name_='toler')
        if self.getNKnots() != None :
            if self.nKnots:
                self.nKnots.export(outfile, level, name_='nKnots')
        if self.getKminSpl() != None :
            if self.kminSpl:
                self.kminSpl.export(outfile, level, name_='kminSpl')
        if self.getKmaxSpl() != None :
            if self.kmaxSpl:
                self.kmaxSpl.export(outfile, level, name_='kmaxSpl')
        if self.getKweightSpl() != None :
            if self.kweightSpl:
                self.kweightSpl.export(outfile, level, name_='kweightSpl')
        if self.getDk1Spl() != None :
            if self.dk1Spl:
                self.dk1Spl.export(outfile, level, name_='dk1Spl')
        if self.getDk2Spl() != None :
            if self.dk2Spl:
                self.dk2Spl.export(outfile, level, name_='dk2Spl')
        if self.getKWindow() != None :
            if self.kWindow:
                self.kWindow.export(outfile, level, name_='kWindow')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSpline' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSpline.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSpline.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSpline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSpline'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.group:
            showIndent(outfile, level)
            outfile.write('group=XSDataString(\n')
            self.group.exportLiteral(outfile, level, name_='group')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e0:
            showIndent(outfile, level)
            outfile.write('e0=XSDataFloat(\n')
            self.e0.exportLiteral(outfile, level, name_='e0')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rbkg:
            showIndent(outfile, level)
            outfile.write('rbkg=XSDataFloat(\n')
            self.rbkg.exportLiteral(outfile, level, name_='rbkg')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.toler:
            showIndent(outfile, level)
            outfile.write('toler=XSDataFloat(\n')
            self.toler.exportLiteral(outfile, level, name_='toler')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nKnots:
            showIndent(outfile, level)
            outfile.write('nKnots=XSDataFloat(\n')
            self.nKnots.exportLiteral(outfile, level, name_='nKnots')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kminSpl:
            showIndent(outfile, level)
            outfile.write('kminSpl=XSDataFloat(\n')
            self.kminSpl.exportLiteral(outfile, level, name_='kminSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kmaxSpl:
            showIndent(outfile, level)
            outfile.write('kmaxSpl=XSDataFloat(\n')
            self.kmaxSpl.exportLiteral(outfile, level, name_='kmaxSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kweightSpl:
            showIndent(outfile, level)
            outfile.write('kweightSpl=XSDataFloat(\n')
            self.kweightSpl.exportLiteral(outfile, level, name_='kweightSpl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk1Spl:
            showIndent(outfile, level)
            outfile.write('dk1Spl=XSDataFloat(\n')
            self.dk1Spl.exportLiteral(outfile, level, name_='dk1Spl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dk2Spl:
            showIndent(outfile, level)
            outfile.write('dk2Spl=XSDataFloat(\n')
            self.dk2Spl.exportLiteral(outfile, level, name_='dk2Spl')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kWindow:
            showIndent(outfile, level)
            outfile.write('kWindow=XSDataString(\n')
            self.kWindow.exportLiteral(outfile, level, name_='kWindow')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'group':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rbkg':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRbkg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'toler':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setToler(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nKnots':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNKnots(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kminSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKminSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kmaxSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKmaxSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kweightSpl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setKweightSpl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk1Spl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk1Spl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dk2Spl':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDk2Spl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kWindow':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKWindow(obj_)
# end class XSDataResultSpline


class XSDataXAFSExperiment(XSData):
    subclass = None
    def __init__(self, label=None, experimentalDataEnergy=None, experimentalDataI0=None, experimentalDataIref=None, experimentalDataIt=None, experimentalDataTime=None, experimentalDataLnI0Iref=None, experimentalDataLnI0It=None):
        XSData.__init__(self)
        self.label = label
        if experimentalDataEnergy is None:
            self.experimentalDataEnergy = []
        else:
            self.experimentalDataEnergy = experimentalDataEnergy
        if experimentalDataI0 is None:
            self.experimentalDataI0 = []
        else:
            self.experimentalDataI0 = experimentalDataI0
        if experimentalDataIref is None:
            self.experimentalDataIref = []
        else:
            self.experimentalDataIref = experimentalDataIref
        if experimentalDataIt is None:
            self.experimentalDataIt = []
        else:
            self.experimentalDataIt = experimentalDataIt
        if experimentalDataTime is None:
            self.experimentalDataTime = []
        else:
            self.experimentalDataTime = experimentalDataTime
        if experimentalDataLnI0Iref is None:
            self.experimentalDataLnI0Iref = []
        else:
            self.experimentalDataLnI0Iref = experimentalDataLnI0Iref
        if experimentalDataLnI0It is None:
            self.experimentalDataLnI0It = []
        else:
            self.experimentalDataLnI0It = experimentalDataLnI0It
    def factory(*args_, **kwargs_):
        if XSDataXAFSExperiment.subclass:
            return XSDataXAFSExperiment.subclass(*args_, **kwargs_)
        else:
            return XSDataXAFSExperiment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLabel(self): return self.label
    def setLabel(self, label): self.label = label
    def getExperimentalDataEnergy(self): return self.experimentalDataEnergy
    def setExperimentalDataEnergy(self, experimentalDataEnergy): self.experimentalDataEnergy = experimentalDataEnergy
    def addExperimentalDataEnergy(self, value): self.experimentalDataEnergy.append(value)
    def insertExperimentalDataEnergy(self, index, value): self.experimentalDataEnergy[index] = value
    def getExperimentalDataI0(self): return self.experimentalDataI0
    def setExperimentalDataI0(self, experimentalDataI0): self.experimentalDataI0 = experimentalDataI0
    def addExperimentalDataI0(self, value): self.experimentalDataI0.append(value)
    def insertExperimentalDataI0(self, index, value): self.experimentalDataI0[index] = value
    def getExperimentalDataIref(self): return self.experimentalDataIref
    def setExperimentalDataIref(self, experimentalDataIref): self.experimentalDataIref = experimentalDataIref
    def addExperimentalDataIref(self, value): self.experimentalDataIref.append(value)
    def insertExperimentalDataIref(self, index, value): self.experimentalDataIref[index] = value
    def getExperimentalDataIt(self): return self.experimentalDataIt
    def setExperimentalDataIt(self, experimentalDataIt): self.experimentalDataIt = experimentalDataIt
    def addExperimentalDataIt(self, value): self.experimentalDataIt.append(value)
    def insertExperimentalDataIt(self, index, value): self.experimentalDataIt[index] = value
    def getExperimentalDataTime(self): return self.experimentalDataTime
    def setExperimentalDataTime(self, experimentalDataTime): self.experimentalDataTime = experimentalDataTime
    def addExperimentalDataTime(self, value): self.experimentalDataTime.append(value)
    def insertExperimentalDataTime(self, index, value): self.experimentalDataTime[index] = value
    def getExperimentalDataLnI0Iref(self): return self.experimentalDataLnI0Iref
    def setExperimentalDataLnI0Iref(self, experimentalDataLnI0Iref): self.experimentalDataLnI0Iref = experimentalDataLnI0Iref
    def addExperimentalDataLnI0Iref(self, value): self.experimentalDataLnI0Iref.append(value)
    def insertExperimentalDataLnI0Iref(self, index, value): self.experimentalDataLnI0Iref[index] = value
    def getExperimentalDataLnI0It(self): return self.experimentalDataLnI0It
    def setExperimentalDataLnI0It(self, experimentalDataLnI0It): self.experimentalDataLnI0It = experimentalDataLnI0It
    def addExperimentalDataLnI0It(self, value): self.experimentalDataLnI0It.append(value)
    def insertExperimentalDataLnI0It(self, index, value): self.experimentalDataLnI0It[index] = value
    def export(self, outfile, level, name_='XSDataXAFSExperiment'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataXAFSExperiment'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataXAFSExperiment')
    def exportChildren(self, outfile, level, name_='XSDataXAFSExperiment'):
        if self.getLabel() != None :
            if self.label:
                self.label.export(outfile, level, name_='label')
        for experimentalDataEnergy_ in self.getExperimentalDataEnergy():
            experimentalDataEnergy_.export(outfile, level, name_='experimentalDataEnergy')
        for experimentalDataI0_ in self.getExperimentalDataI0():
            experimentalDataI0_.export(outfile, level, name_='experimentalDataI0')
        for experimentalDataIref_ in self.getExperimentalDataIref():
            experimentalDataIref_.export(outfile, level, name_='experimentalDataIref')
        for experimentalDataIt_ in self.getExperimentalDataIt():
            experimentalDataIt_.export(outfile, level, name_='experimentalDataIt')
        for experimentalDataTime_ in self.getExperimentalDataTime():
            experimentalDataTime_.export(outfile, level, name_='experimentalDataTime')
        for experimentalDataLnI0Iref_ in self.getExperimentalDataLnI0Iref():
            experimentalDataLnI0Iref_.export(outfile, level, name_='experimentalDataLnI0Iref')
        for experimentalDataLnI0It_ in self.getExperimentalDataLnI0It():
            experimentalDataLnI0It_.export(outfile, level, name_='experimentalDataLnI0It')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataXAFSExperiment' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXAFSExperiment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXAFSExperiment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataXAFSExperiment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataXAFSExperiment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.label:
            showIndent(outfile, level)
            outfile.write('label=XSDataString(\n')
            self.label.exportLiteral(outfile, level, name_='label')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataEnergy=[\n')
        level += 1
        for experimentalDataEnergy in self.experimentalDataEnergy:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataEnergy.exportLiteral(outfile, level, name_='experimentalDataEnergy')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataI0=[\n')
        level += 1
        for experimentalDataI0 in self.experimentalDataI0:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataI0.exportLiteral(outfile, level, name_='experimentalDataI0')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataIref=[\n')
        level += 1
        for experimentalDataIref in self.experimentalDataIref:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataIref.exportLiteral(outfile, level, name_='experimentalDataIref')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataIt=[\n')
        level += 1
        for experimentalDataIt in self.experimentalDataIt:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataIt.exportLiteral(outfile, level, name_='experimentalDataIt')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataTime=[\n')
        level += 1
        for experimentalDataTime in self.experimentalDataTime:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataTime.exportLiteral(outfile, level, name_='experimentalDataTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataLnI0Iref=[\n')
        level += 1
        for experimentalDataLnI0Iref in self.experimentalDataLnI0Iref:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataLnI0Iref.exportLiteral(outfile, level, name_='experimentalDataLnI0Iref')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataLnI0It=[\n')
        level += 1
        for experimentalDataLnI0It in self.experimentalDataLnI0It:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataLnI0It.exportLiteral(outfile, level, name_='experimentalDataLnI0It')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'label':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setLabel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataEnergy':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataEnergy.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataI0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataI0.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIref':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataIref.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIt':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataIt.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataTime':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataTime.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataLnI0Iref':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataLnI0Iref.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataLnI0It':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataLnI0It.append(obj_)
# end class XSDataXAFSExperiment


class XSDataInputXAFSDataBatchProcessing(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, xafsExperimentData=None, preEdgeDataInput=None, splineDataInput=None, fftfDataInput=None):
        XSDataInput.__init__(self, configuration)
        if xafsExperimentData is None:
            self.xafsExperimentData = []
        else:
            self.xafsExperimentData = xafsExperimentData
        self.preEdgeDataInput = preEdgeDataInput
        self.splineDataInput = splineDataInput
        self.fftfDataInput = fftfDataInput
    def factory(*args_, **kwargs_):
        if XSDataInputXAFSDataBatchProcessing.subclass:
            return XSDataInputXAFSDataBatchProcessing.subclass(*args_, **kwargs_)
        else:
            return XSDataInputXAFSDataBatchProcessing(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXafsExperimentData(self): return self.xafsExperimentData
    def setXafsExperimentData(self, xafsExperimentData): self.xafsExperimentData = xafsExperimentData
    def addXafsExperimentData(self, value): self.xafsExperimentData.append(value)
    def insertXafsExperimentData(self, index, value): self.xafsExperimentData[index] = value
    def getPreEdgeDataInput(self): return self.preEdgeDataInput
    def setPreEdgeDataInput(self, preEdgeDataInput): self.preEdgeDataInput = preEdgeDataInput
    def getSplineDataInput(self): return self.splineDataInput
    def setSplineDataInput(self, splineDataInput): self.splineDataInput = splineDataInput
    def getFftfDataInput(self): return self.fftfDataInput
    def setFftfDataInput(self, fftfDataInput): self.fftfDataInput = fftfDataInput
    def export(self, outfile, level, name_='XSDataInputXAFSDataBatchProcessing'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputXAFSDataBatchProcessing'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputXAFSDataBatchProcessing')
    def exportChildren(self, outfile, level, name_='XSDataInputXAFSDataBatchProcessing'):
        for xafsExperimentData_ in self.getXafsExperimentData():
            xafsExperimentData_.export(outfile, level, name_='xafsExperimentData')
        if self.getPreEdgeDataInput() != None :
            if self.preEdgeDataInput:
                self.preEdgeDataInput.export(outfile, level, name_='preEdgeDataInput')
        if self.getSplineDataInput() != None :
            if self.splineDataInput:
                self.splineDataInput.export(outfile, level, name_='splineDataInput')
        if self.getFftfDataInput() != None :
            if self.fftfDataInput:
                self.fftfDataInput.export(outfile, level, name_='fftfDataInput')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputXAFSDataBatchProcessing' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXAFSDataBatchProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXAFSDataBatchProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputXAFSDataBatchProcessing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputXAFSDataBatchProcessing'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('xafsExperimentData=[\n')
        level += 1
        for xafsExperimentData in self.xafsExperimentData:
            showIndent(outfile, level)
            outfile.write('XSDataXAFSExperiment(\n')
            xafsExperimentData.exportLiteral(outfile, level, name_='xafsExperimentData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.preEdgeDataInput:
            showIndent(outfile, level)
            outfile.write('preEdgeDataInput=XSDataInputPreEdgeSubtraction(\n')
            self.preEdgeDataInput.exportLiteral(outfile, level, name_='preEdgeDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.splineDataInput:
            showIndent(outfile, level)
            outfile.write('splineDataInput=XSDataInputSpline(\n')
            self.splineDataInput.exportLiteral(outfile, level, name_='splineDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fftfDataInput:
            showIndent(outfile, level)
            outfile.write('fftfDataInput=XSDataInputFFTF(\n')
            self.fftfDataInput.exportLiteral(outfile, level, name_='fftfDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xafsExperimentData':
            obj_ = XSDataXAFSExperiment.factory()
            obj_.build(child_)
            self.xafsExperimentData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preEdgeDataInput':
            obj_ = XSDataInputPreEdgeSubtraction.factory()
            obj_.build(child_)
            self.setPreEdgeDataInput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'splineDataInput':
            obj_ = XSDataInputSpline.factory()
            obj_.build(child_)
            self.setSplineDataInput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fftfDataInput':
            obj_ = XSDataInputFFTF.factory()
            obj_.build(child_)
            self.setFftfDataInput(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputXAFSDataBatchProcessing


class XSDataInputXAFSDataProcessing(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, experimentalDataEnergy=None, experimentalDataI0=None, experimentalDataIref=None, experimentalDataIt=None, experimentalDataTime=None, experimentalDataLnI0Iref=None, experimentalDataLnI0It=None, preEdgeDataInput=None, splineDataInput=None, fftfDataInput=None):
        XSDataInput.__init__(self, configuration)
        if experimentalDataEnergy is None:
            self.experimentalDataEnergy = []
        else:
            self.experimentalDataEnergy = experimentalDataEnergy
        if experimentalDataI0 is None:
            self.experimentalDataI0 = []
        else:
            self.experimentalDataI0 = experimentalDataI0
        if experimentalDataIref is None:
            self.experimentalDataIref = []
        else:
            self.experimentalDataIref = experimentalDataIref
        if experimentalDataIt is None:
            self.experimentalDataIt = []
        else:
            self.experimentalDataIt = experimentalDataIt
        if experimentalDataTime is None:
            self.experimentalDataTime = []
        else:
            self.experimentalDataTime = experimentalDataTime
        if experimentalDataLnI0Iref is None:
            self.experimentalDataLnI0Iref = []
        else:
            self.experimentalDataLnI0Iref = experimentalDataLnI0Iref
        if experimentalDataLnI0It is None:
            self.experimentalDataLnI0It = []
        else:
            self.experimentalDataLnI0It = experimentalDataLnI0It
        self.preEdgeDataInput = preEdgeDataInput
        self.splineDataInput = splineDataInput
        self.fftfDataInput = fftfDataInput
    def factory(*args_, **kwargs_):
        if XSDataInputXAFSDataProcessing.subclass:
            return XSDataInputXAFSDataProcessing.subclass(*args_, **kwargs_)
        else:
            return XSDataInputXAFSDataProcessing(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExperimentalDataEnergy(self): return self.experimentalDataEnergy
    def setExperimentalDataEnergy(self, experimentalDataEnergy): self.experimentalDataEnergy = experimentalDataEnergy
    def addExperimentalDataEnergy(self, value): self.experimentalDataEnergy.append(value)
    def insertExperimentalDataEnergy(self, index, value): self.experimentalDataEnergy[index] = value
    def getExperimentalDataI0(self): return self.experimentalDataI0
    def setExperimentalDataI0(self, experimentalDataI0): self.experimentalDataI0 = experimentalDataI0
    def addExperimentalDataI0(self, value): self.experimentalDataI0.append(value)
    def insertExperimentalDataI0(self, index, value): self.experimentalDataI0[index] = value
    def getExperimentalDataIref(self): return self.experimentalDataIref
    def setExperimentalDataIref(self, experimentalDataIref): self.experimentalDataIref = experimentalDataIref
    def addExperimentalDataIref(self, value): self.experimentalDataIref.append(value)
    def insertExperimentalDataIref(self, index, value): self.experimentalDataIref[index] = value
    def getExperimentalDataIt(self): return self.experimentalDataIt
    def setExperimentalDataIt(self, experimentalDataIt): self.experimentalDataIt = experimentalDataIt
    def addExperimentalDataIt(self, value): self.experimentalDataIt.append(value)
    def insertExperimentalDataIt(self, index, value): self.experimentalDataIt[index] = value
    def getExperimentalDataTime(self): return self.experimentalDataTime
    def setExperimentalDataTime(self, experimentalDataTime): self.experimentalDataTime = experimentalDataTime
    def addExperimentalDataTime(self, value): self.experimentalDataTime.append(value)
    def insertExperimentalDataTime(self, index, value): self.experimentalDataTime[index] = value
    def getExperimentalDataLnI0Iref(self): return self.experimentalDataLnI0Iref
    def setExperimentalDataLnI0Iref(self, experimentalDataLnI0Iref): self.experimentalDataLnI0Iref = experimentalDataLnI0Iref
    def addExperimentalDataLnI0Iref(self, value): self.experimentalDataLnI0Iref.append(value)
    def insertExperimentalDataLnI0Iref(self, index, value): self.experimentalDataLnI0Iref[index] = value
    def getExperimentalDataLnI0It(self): return self.experimentalDataLnI0It
    def setExperimentalDataLnI0It(self, experimentalDataLnI0It): self.experimentalDataLnI0It = experimentalDataLnI0It
    def addExperimentalDataLnI0It(self, value): self.experimentalDataLnI0It.append(value)
    def insertExperimentalDataLnI0It(self, index, value): self.experimentalDataLnI0It[index] = value
    def getPreEdgeDataInput(self): return self.preEdgeDataInput
    def setPreEdgeDataInput(self, preEdgeDataInput): self.preEdgeDataInput = preEdgeDataInput
    def getSplineDataInput(self): return self.splineDataInput
    def setSplineDataInput(self, splineDataInput): self.splineDataInput = splineDataInput
    def getFftfDataInput(self): return self.fftfDataInput
    def setFftfDataInput(self, fftfDataInput): self.fftfDataInput = fftfDataInput
    def export(self, outfile, level, name_='XSDataInputXAFSDataProcessing'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputXAFSDataProcessing'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputXAFSDataProcessing')
    def exportChildren(self, outfile, level, name_='XSDataInputXAFSDataProcessing'):
        for experimentalDataEnergy_ in self.getExperimentalDataEnergy():
            experimentalDataEnergy_.export(outfile, level, name_='experimentalDataEnergy')
        for experimentalDataI0_ in self.getExperimentalDataI0():
            experimentalDataI0_.export(outfile, level, name_='experimentalDataI0')
        for experimentalDataIref_ in self.getExperimentalDataIref():
            experimentalDataIref_.export(outfile, level, name_='experimentalDataIref')
        for experimentalDataIt_ in self.getExperimentalDataIt():
            experimentalDataIt_.export(outfile, level, name_='experimentalDataIt')
        for experimentalDataTime_ in self.getExperimentalDataTime():
            experimentalDataTime_.export(outfile, level, name_='experimentalDataTime')
        for experimentalDataLnI0Iref_ in self.getExperimentalDataLnI0Iref():
            experimentalDataLnI0Iref_.export(outfile, level, name_='experimentalDataLnI0Iref')
        for experimentalDataLnI0It_ in self.getExperimentalDataLnI0It():
            experimentalDataLnI0It_.export(outfile, level, name_='experimentalDataLnI0It')
        if self.getPreEdgeDataInput() != None :
            if self.preEdgeDataInput:
                self.preEdgeDataInput.export(outfile, level, name_='preEdgeDataInput')
        if self.getSplineDataInput() != None :
            if self.splineDataInput:
                self.splineDataInput.export(outfile, level, name_='splineDataInput')
        if self.getFftfDataInput() != None :
            if self.fftfDataInput:
                self.fftfDataInput.export(outfile, level, name_='fftfDataInput')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputXAFSDataProcessing' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXAFSDataProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXAFSDataProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputXAFSDataProcessing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputXAFSDataProcessing'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('experimentalDataEnergy=[\n')
        level += 1
        for experimentalDataEnergy in self.experimentalDataEnergy:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataEnergy.exportLiteral(outfile, level, name_='experimentalDataEnergy')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataI0=[\n')
        level += 1
        for experimentalDataI0 in self.experimentalDataI0:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataI0.exportLiteral(outfile, level, name_='experimentalDataI0')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataIref=[\n')
        level += 1
        for experimentalDataIref in self.experimentalDataIref:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataIref.exportLiteral(outfile, level, name_='experimentalDataIref')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataIt=[\n')
        level += 1
        for experimentalDataIt in self.experimentalDataIt:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataIt.exportLiteral(outfile, level, name_='experimentalDataIt')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataTime=[\n')
        level += 1
        for experimentalDataTime in self.experimentalDataTime:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataTime.exportLiteral(outfile, level, name_='experimentalDataTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataLnI0Iref=[\n')
        level += 1
        for experimentalDataLnI0Iref in self.experimentalDataLnI0Iref:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataLnI0Iref.exportLiteral(outfile, level, name_='experimentalDataLnI0Iref')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataLnI0It=[\n')
        level += 1
        for experimentalDataLnI0It in self.experimentalDataLnI0It:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataLnI0It.exportLiteral(outfile, level, name_='experimentalDataLnI0It')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.preEdgeDataInput:
            showIndent(outfile, level)
            outfile.write('preEdgeDataInput=XSDataInputPreEdgeSubtraction(\n')
            self.preEdgeDataInput.exportLiteral(outfile, level, name_='preEdgeDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.splineDataInput:
            showIndent(outfile, level)
            outfile.write('splineDataInput=XSDataInputSpline(\n')
            self.splineDataInput.exportLiteral(outfile, level, name_='splineDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fftfDataInput:
            showIndent(outfile, level)
            outfile.write('fftfDataInput=XSDataInputFFTF(\n')
            self.fftfDataInput.exportLiteral(outfile, level, name_='fftfDataInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataEnergy':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataEnergy.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataI0':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataI0.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIref':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataIref.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIt':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataIt.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataTime':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataTime.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataLnI0Iref':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataLnI0Iref.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataLnI0It':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataLnI0It.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preEdgeDataInput':
            obj_ = XSDataInputPreEdgeSubtraction.factory()
            obj_.build(child_)
            self.setPreEdgeDataInput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'splineDataInput':
            obj_ = XSDataInputSpline.factory()
            obj_.build(child_)
            self.setSplineDataInput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fftfDataInput':
            obj_ = XSDataInputFFTF.factory()
            obj_.build(child_)
            self.setFftfDataInput(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputXAFSDataProcessing


class XSDataResultXAFSDataProcessing(XSDataResult):
    subclass = None
    def __init__(self, label=None, preEdgeDataResult=None, normDataResult=None, splineDataResult=None, rDataResult=None, chiRMagData=None, chiRReData=None, chiRImData=None, sessionFile=None):
        XSDataResult.__init__(self)
        self.label = label
        self.preEdgeDataResult = preEdgeDataResult
        self.normDataResult = normDataResult
        self.splineDataResult = splineDataResult
        if rDataResult is None:
            self.rDataResult = []
        else:
            self.rDataResult = rDataResult
        if chiRMagData is None:
            self.chiRMagData = []
        else:
            self.chiRMagData = chiRMagData
        if chiRReData is None:
            self.chiRReData = []
        else:
            self.chiRReData = chiRReData
        if chiRImData is None:
            self.chiRImData = []
        else:
            self.chiRImData = chiRImData
        self.sessionFile = sessionFile
    def factory(*args_, **kwargs_):
        if XSDataResultXAFSDataProcessing.subclass:
            return XSDataResultXAFSDataProcessing.subclass(*args_, **kwargs_)
        else:
            return XSDataResultXAFSDataProcessing(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLabel(self): return self.label
    def setLabel(self, label): self.label = label
    def getPreEdgeDataResult(self): return self.preEdgeDataResult
    def setPreEdgeDataResult(self, preEdgeDataResult): self.preEdgeDataResult = preEdgeDataResult
    def getNormDataResult(self): return self.normDataResult
    def setNormDataResult(self, normDataResult): self.normDataResult = normDataResult
    def getSplineDataResult(self): return self.splineDataResult
    def setSplineDataResult(self, splineDataResult): self.splineDataResult = splineDataResult
    def getRDataResult(self): return self.rDataResult
    def setRDataResult(self, rDataResult): self.rDataResult = rDataResult
    def addRDataResult(self, value): self.rDataResult.append(value)
    def insertRDataResult(self, index, value): self.rDataResult[index] = value
    def getChiRMagData(self): return self.chiRMagData
    def setChiRMagData(self, chiRMagData): self.chiRMagData = chiRMagData
    def addChiRMagData(self, value): self.chiRMagData.append(value)
    def insertChiRMagData(self, index, value): self.chiRMagData[index] = value
    def getChiRReData(self): return self.chiRReData
    def setChiRReData(self, chiRReData): self.chiRReData = chiRReData
    def addChiRReData(self, value): self.chiRReData.append(value)
    def insertChiRReData(self, index, value): self.chiRReData[index] = value
    def getChiRImData(self): return self.chiRImData
    def setChiRImData(self, chiRImData): self.chiRImData = chiRImData
    def addChiRImData(self, value): self.chiRImData.append(value)
    def insertChiRImData(self, index, value): self.chiRImData[index] = value
    def getSessionFile(self): return self.sessionFile
    def setSessionFile(self, sessionFile): self.sessionFile = sessionFile
    def export(self, outfile, level, name_='XSDataResultXAFSDataProcessing'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultXAFSDataProcessing'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultXAFSDataProcessing')
    def exportChildren(self, outfile, level, name_='XSDataResultXAFSDataProcessing'):
        if self.getLabel() != None :
            if self.label:
                self.label.export(outfile, level, name_='label')
        if self.getPreEdgeDataResult() != None :
            if self.preEdgeDataResult:
                self.preEdgeDataResult.export(outfile, level, name_='preEdgeDataResult')
        if self.getNormDataResult() != None :
            if self.normDataResult:
                self.normDataResult.export(outfile, level, name_='normDataResult')
        if self.getSplineDataResult() != None :
            if self.splineDataResult:
                self.splineDataResult.export(outfile, level, name_='splineDataResult')
        for rDataResult_ in self.getRDataResult():
            rDataResult_.export(outfile, level, name_='rDataResult')
        for chiRMagData_ in self.getChiRMagData():
            chiRMagData_.export(outfile, level, name_='chiRMagData')
        for chiRReData_ in self.getChiRReData():
            chiRReData_.export(outfile, level, name_='chiRReData')
        for chiRImData_ in self.getChiRImData():
            chiRImData_.export(outfile, level, name_='chiRImData')
        if self.sessionFile:
            self.sessionFile.export(outfile, level, name_='sessionFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultXAFSDataProcessing' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXAFSDataProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXAFSDataProcessing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultXAFSDataProcessing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultXAFSDataProcessing'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.label:
            showIndent(outfile, level)
            outfile.write('label=XSDataString(\n')
            self.label.exportLiteral(outfile, level, name_='label')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.preEdgeDataResult:
            showIndent(outfile, level)
            outfile.write('preEdgeDataResult=XSDataResultPreEdgeSubtraction(\n')
            self.preEdgeDataResult.exportLiteral(outfile, level, name_='preEdgeDataResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.normDataResult:
            showIndent(outfile, level)
            outfile.write('normDataResult=XSDataResultNormalization(\n')
            self.normDataResult.exportLiteral(outfile, level, name_='normDataResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.splineDataResult:
            showIndent(outfile, level)
            outfile.write('splineDataResult=XSDataResultSpline(\n')
            self.splineDataResult.exportLiteral(outfile, level, name_='splineDataResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('rDataResult=[\n')
        level += 1
        for rDataResult in self.rDataResult:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            rDataResult.exportLiteral(outfile, level, name_='rDataResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRMagData=[\n')
        level += 1
        for chiRMagData in self.chiRMagData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRMagData.exportLiteral(outfile, level, name_='chiRMagData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRReData=[\n')
        level += 1
        for chiRReData in self.chiRReData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRReData.exportLiteral(outfile, level, name_='chiRReData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('chiRImData=[\n')
        level += 1
        for chiRImData in self.chiRImData:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            chiRImData.exportLiteral(outfile, level, name_='chiRImData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.sessionFile:
            showIndent(outfile, level)
            outfile.write('sessionFile=XSDataFile(\n')
            self.sessionFile.exportLiteral(outfile, level, name_='sessionFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'label':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setLabel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'preEdgeDataResult':
            obj_ = XSDataResultPreEdgeSubtraction.factory()
            obj_.build(child_)
            self.setPreEdgeDataResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normDataResult':
            obj_ = XSDataResultNormalization.factory()
            obj_.build(child_)
            self.setNormDataResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'splineDataResult':
            obj_ = XSDataResultSpline.factory()
            obj_.build(child_)
            self.setSplineDataResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rDataResult':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.rDataResult.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRMagData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRMagData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRReData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRReData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRImData':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.chiRImData.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSessionFile(obj_)
# end class XSDataResultXAFSDataProcessing


class XSDataInputAtoms(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, title=None, crystal=None, sample=None, flags=None, sites=None, outputFile=None):
        XSDataInput.__init__(self, configuration)
        self.title = title
        self.crystal = crystal
        self.sample = sample
        self.flags = flags
        if sites is None:
            self.sites = []
        else:
            self.sites = sites
        self.outputFile = outputFile
    def factory(*args_, **kwargs_):
        if XSDataInputAtoms.subclass:
            return XSDataInputAtoms.subclass(*args_, **kwargs_)
        else:
            return XSDataInputAtoms(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getTitle(self): return self.title
    def setTitle(self, title): self.title = title
    def getCrystal(self): return self.crystal
    def setCrystal(self, crystal): self.crystal = crystal
    def getSample(self): return self.sample
    def setSample(self, sample): self.sample = sample
    def getFlags(self): return self.flags
    def setFlags(self, flags): self.flags = flags
    def getSites(self): return self.sites
    def setSites(self, sites): self.sites = sites
    def addSites(self, value): self.sites.append(value)
    def insertSites(self, index, value): self.sites[index] = value
    def getOutputFile(self): return self.outputFile
    def setOutputFile(self, outputFile): self.outputFile = outputFile
    def export(self, outfile, level, name_='XSDataInputAtoms'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputAtoms'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputAtoms')
    def exportChildren(self, outfile, level, name_='XSDataInputAtoms'):
        if self.getTitle() != None :
            if self.title:
                self.title.export(outfile, level, name_='title')
        if self.crystal:
            self.crystal.export(outfile, level, name_='crystal')
        if self.sample:
            self.sample.export(outfile, level, name_='sample')
        if self.flags:
            self.flags.export(outfile, level, name_='flags')
        for sites_ in self.getSites():
            sites_.export(outfile, level, name_='sites')
        if self.outputFile:
            self.outputFile.export(outfile, level, name_='outputFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputAtoms' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputAtoms" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputAtoms'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.title:
            showIndent(outfile, level)
            outfile.write('title=XSDataString(\n')
            self.title.exportLiteral(outfile, level, name_='title')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.crystal:
            showIndent(outfile, level)
            outfile.write('crystal=XSDataAtomsCrystal(\n')
            self.crystal.exportLiteral(outfile, level, name_='crystal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sample:
            showIndent(outfile, level)
            outfile.write('sample=XSDataAtomsSample(\n')
            self.sample.exportLiteral(outfile, level, name_='sample')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.flags:
            showIndent(outfile, level)
            outfile.write('flags=XSDataAtomsFlags(\n')
            self.flags.exportLiteral(outfile, level, name_='flags')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('sites=[\n')
        level += 1
        for sites in self.sites:
            showIndent(outfile, level)
            outfile.write('XSDataAtomsSite(\n')
            sites.exportLiteral(outfile, level, name_='sites')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.outputFile:
            showIndent(outfile, level)
            outfile.write('outputFile=XSDataString(\n')
            self.outputFile.exportLiteral(outfile, level, name_='outputFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'title':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTitle(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataAtomsCrystal.factory()
            obj_.build(child_)
            self.setCrystal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataAtomsSample.factory()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flags':
            obj_ = XSDataAtomsFlags.factory()
            obj_.build(child_)
            self.setFlags(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sites':
            obj_ = XSDataAtomsSite.factory()
            obj_.build(child_)
            self.sites.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputFile':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOutputFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputAtoms


class XSDataResultAtoms(XSDataResult):
    subclass = None
    def __init__(self, inpFile=None, optionsFeff=None):
        XSDataResult.__init__(self)
        self.inpFile = inpFile
        self.optionsFeff = optionsFeff
    def factory(*args_, **kwargs_):
        if XSDataResultAtoms.subclass:
            return XSDataResultAtoms.subclass(*args_, **kwargs_)
        else:
            return XSDataResultAtoms(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getInpFile(self): return self.inpFile
    def setInpFile(self, inpFile): self.inpFile = inpFile
    def getOptionsFeff(self): return self.optionsFeff
    def setOptionsFeff(self, optionsFeff): self.optionsFeff = optionsFeff
    def export(self, outfile, level, name_='XSDataResultAtoms'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultAtoms'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultAtoms')
    def exportChildren(self, outfile, level, name_='XSDataResultAtoms'):
        if self.inpFile:
            self.inpFile.export(outfile, level, name_='inpFile')
        if self.optionsFeff:
            self.optionsFeff.export(outfile, level, name_='optionsFeff')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultAtoms' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAtoms.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultAtoms" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultAtoms'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.inpFile:
            showIndent(outfile, level)
            outfile.write('inpFile=XSDataFile(\n')
            self.inpFile.exportLiteral(outfile, level, name_='inpFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.optionsFeff:
            showIndent(outfile, level)
            outfile.write('optionsFeff=XSDataInputFeff(\n')
            self.optionsFeff.exportLiteral(outfile, level, name_='optionsFeff')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inpFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setInpFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'optionsFeff':
            obj_ = XSDataInputFeff.factory()
            obj_.build(child_)
            self.setOptionsFeff(obj_)
# end class XSDataResultAtoms


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxXSConfigurationHandler(handler.ContentHandler):
    def __init__(self):
        self.stack = []
        self.root = None

    def getRoot(self):
        return self.root

    def setDocumentLocator(self, locator):
        self.locator = locator
    
    def showError(self, msg):
        print '*** (showError):', msg
        sys.exit(-1)

    def startElement(self, name, attrs):
        done = 0
        if name == 'XSConfiguration':
            obj = XSConfiguration.factory()
            stackObj = SaxStackElement('XSConfiguration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginList':
            obj = XSPluginList.factory()
            stackObj = SaxStackElement('XSPluginList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shape':
            stackObj = SaxStackElement('shape', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'size':
            stackObj = SaxStackElement('size', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dtype':
            stackObj = SaxStackElement('dtype', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'data':
            stackObj = SaxStackElement('data', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'coding':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('coding', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'md5sum':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('md5sum', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'value':
            stackObj = SaxStackElement('value', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'keyValuePair':
            obj = XSDataKeyValuePair.factory()
            stackObj = SaxStackElement('keyValuePair', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unit':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('unit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'error':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('error', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'baseDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('baseDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executionTime':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('executionTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pluginName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('pluginName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'startOfExecution':
            obj = XSDataDate.factory()
            stackObj = SaxStackElement('startOfExecution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'systeminfo':
            obj = XSDataSysteminfo.factory()
            stackObj = SaxStackElement('systeminfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'workingDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('workingDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'configuration':
            obj = XSConfiguration.factory()
            stackObj = SaxStackElement('configuration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'path':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('path', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'date':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('date', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'number':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('number', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'key':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('key', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm11':
            stackObj = SaxStackElement('m11', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm12':
            stackObj = SaxStackElement('m12', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm13':
            stackObj = SaxStackElement('m13', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm21':
            stackObj = SaxStackElement('m21', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm22':
            stackObj = SaxStackElement('m22', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm23':
            stackObj = SaxStackElement('m23', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm31':
            stackObj = SaxStackElement('m31', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm32':
            stackObj = SaxStackElement('m32', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm33':
            stackObj = SaxStackElement('m33', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'debuginfo':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('debuginfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'level':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('level', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'text':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('text', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'type':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('typexx', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q0':
            stackObj = SaxStackElement('q0', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q1':
            stackObj = SaxStackElement('q1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q2':
            stackObj = SaxStackElement('q2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q3':
            stackObj = SaxStackElement('q3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'x':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'y':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'z':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executiveSummary':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('executiveSummary', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'isSuccess':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('isSuccess', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executionInfo':
            obj = XSDataExecutionInfo.factory()
            stackObj = SaxStackElement('executionInfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'compiler':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('compiler', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hostIP':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('hostIP', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hostName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('hostName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'operatingSystem':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('operatingSystem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'operatingSystemType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('operatingSystemType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'userName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('userName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'virtualMachine':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('virtualMachine', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v1':
            stackObj = SaxStackElement('v1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v2':
            stackObj = SaxStackElement('v2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v3':
            stackObj = SaxStackElement('v3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'enabled':
            stackObj = SaxStackElement('enabled', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'name':
            stackObj = SaxStackElement('name', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSOptionItem':
            obj = XSOptionItem.factory()
            stackObj = SaxStackElement('XSOptionItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSParamItem':
            obj = XSParamItem.factory()
            stackObj = SaxStackElement('XSParamItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSParamList':
            obj = XSParamList.factory()
            stackObj = SaxStackElement('XSParamList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSOptionList':
            obj = XSOptionList.factory()
            stackObj = SaxStackElement('XSOptionList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginItem':
            obj = XSPluginItem.factory()
            stackObj = SaxStackElement('XSPluginItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dx':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dx', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dy':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dz':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dz', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'tag':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('tag', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'space':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('space', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'a':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('a', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'b':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('b', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'c':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('c', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'alpha':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('alpha', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beta':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'gamma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('gamma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shift':
            obj = XSDataAtomsShift.factory()
            stackObj = SaxStackElement('shift', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'core':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('core', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'edge':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('edge', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmax':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rmax', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nitrogen':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('nitrogen', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'argon':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('argon', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'krypton':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('krypton', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'index':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('index', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'feff':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('feff', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'feff8':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('feff8', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'corrections':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('corrections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'geom':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('geom', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'p1':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('p1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ihole':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('ihole', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 's02':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('s02', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'critcw':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('critcw', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'critpw':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('critpw', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'temp':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('temp', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'tempDebye':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('tempDebye', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'idwopt':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('idwopt', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mphase':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('mphase', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mpath':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('mpath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mfeff':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('mfeff', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mchi':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('mchi', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ipot':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('ipot', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Z':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('Z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'element':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('element', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distance':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('distance', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'file':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('file', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'header':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('header', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'title':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('title', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hole':
            obj = XSDataFeffCardHole.factory()
            stackObj = SaxStackElement('hole', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'control':
            obj = XSDataFeffCardControl.factory()
            stackObj = SaxStackElement('control', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'print':
            obj = XSDataFeffCardPrint.factory()
            stackObj = SaxStackElement('printxx', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nleg':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('nleg', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'potentials':
            obj = XSDataFeffCardPotentials.factory()
            stackObj = SaxStackElement('potentials', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'atoms':
            obj = XSDataFeffCardAtoms.factory()
            stackObj = SaxStackElement('atoms', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'scriptFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('scriptFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sessionFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('sessionFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'energy':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('energy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'xmu':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('xmu', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'group':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('group', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pre1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('pre1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pre2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('pre2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'norm1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('norm1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'norm2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('norm2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e0':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e0', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'edgeStep':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('edgeStep', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'preSlope':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('preSlope', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'preOffset':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('preOffset', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'preEdgeData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('preEdgeData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'normC0':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('normC0', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'normC1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('normC1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'normC2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('normC2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'normData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('normData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rbkg':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rbkg', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'toler':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('toler', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nKnots':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('nKnots', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kminSpl':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kminSpl', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kmaxSpl':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kmaxSpl', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kweightSpl':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kweightSpl', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dk1Spl':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dk1Spl', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dk2Spl':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dk2Spl', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kwindow':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('kwindow', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'real':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('real', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imag':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('imag', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'k':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('k', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kmin':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kmin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kmax':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kmax', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dk1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dk1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dk2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dk2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dk':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('dk', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kweight':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('kweight', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmaxOut':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rmaxOut', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'winData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('winData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chiRMagData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('chiRMagData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chiRReData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('chiRReData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chiRImData':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('chiRImData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kWindow':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('kWindow', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'label':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('label', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataEnergy':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataEnergy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataI0':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataI0', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataIref':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataIref', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataIt':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataIt', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataTime':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataLnI0Iref':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataLnI0Iref', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataLnI0It':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataLnI0It', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'xafsExperimentData':
            obj = XSDataXAFSExperiment.factory()
            stackObj = SaxStackElement('xafsExperimentData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'preEdgeDataInput':
            obj = XSDataInputPreEdgeSubtraction.factory()
            stackObj = SaxStackElement('preEdgeDataInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'splineDataInput':
            obj = XSDataInputSpline.factory()
            stackObj = SaxStackElement('splineDataInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fftfDataInput':
            obj = XSDataInputFFTF.factory()
            stackObj = SaxStackElement('fftfDataInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'preEdgeDataResult':
            obj = XSDataResultPreEdgeSubtraction.factory()
            stackObj = SaxStackElement('preEdgeDataResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'normDataResult':
            obj = XSDataResultNormalization.factory()
            stackObj = SaxStackElement('normDataResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'splineDataResult':
            obj = XSDataResultSpline.factory()
            stackObj = SaxStackElement('splineDataResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rDataResult':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rDataResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'crystal':
            obj = XSDataAtomsCrystal.factory()
            stackObj = SaxStackElement('crystal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sample':
            obj = XSDataAtomsSample.factory()
            stackObj = SaxStackElement('sample', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'flags':
            obj = XSDataAtomsFlags.factory()
            stackObj = SaxStackElement('flags', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sites':
            obj = XSDataAtomsSite.factory()
            stackObj = SaxStackElement('sites', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'outputFile':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('outputFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'inpFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('inpFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'optionsFeff':
            obj = XSDataInputFeff.factory()
            stackObj = SaxStackElement('optionsFeff', obj)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'XSConfiguration':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'XSPluginList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSPluginList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shape':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except Exception:
                        self.reportError('"shape" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.addShape(content)
                self.stack.pop()
                done = 1
        elif name == 'size':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except Exception:
                        self.reportError('"size" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setSize(content)
                self.stack.pop()
                done = 1
        elif name == 'dtype':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setDtype(content)
                self.stack.pop()
                done = 1
        elif name == 'data':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setData(content)
                self.stack.pop()
                done = 1
        elif name == 'coding':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCoding(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'md5sum':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMd5sum(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'value':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content and content in ('true', '1'):
                    content = 1
                else:
                    content = 0
                self.stack[-2].obj.setValue(content)
                self.stack.pop()
                done = 1
        elif name == 'keyValuePair':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addKeyValuePair(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'error':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setError(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'baseDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBaseDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executionTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutionTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pluginName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPluginName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'startOfExecution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStartOfExecution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'systeminfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSysteminfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'workingDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setWorkingDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'configuration':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setConfiguration(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'path':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'date':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDate(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'number':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'key':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKey(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'm11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m11" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM11(content)
                self.stack.pop()
                done = 1
        elif name == 'm12':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m12" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM12(content)
                self.stack.pop()
                done = 1
        elif name == 'm13':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m13" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM13(content)
                self.stack.pop()
                done = 1
        elif name == 'm21':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m21" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM21(content)
                self.stack.pop()
                done = 1
        elif name == 'm22':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m22" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM22(content)
                self.stack.pop()
                done = 1
        elif name == 'm23':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m23" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM23(content)
                self.stack.pop()
                done = 1
        elif name == 'm31':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m31" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM31(content)
                self.stack.pop()
                done = 1
        elif name == 'm32':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m32" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM32(content)
                self.stack.pop()
                done = 1
        elif name == 'm33':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"m33" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM33(content)
                self.stack.pop()
                done = 1
        elif name == 'debuginfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDebuginfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'level':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLevel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'text':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setText(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'type':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'q0':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"q0" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ0(content)
                self.stack.pop()
                done = 1
        elif name == 'q1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"q1" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ1(content)
                self.stack.pop()
                done = 1
        elif name == 'q2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"q2" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ2(content)
                self.stack.pop()
                done = 1
        elif name == 'q3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"q3" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ3(content)
                self.stack.pop()
                done = 1
        elif name == 'x':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'y':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setZ(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executiveSummary':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutiveSummary(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'isSuccess':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIsSuccess(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executionInfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutionInfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'compiler':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCompiler(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hostIP':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHostIP(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hostName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHostName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'operatingSystem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOperatingSystem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'operatingSystemType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOperatingSystemType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'userName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUserName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'virtualMachine':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVirtualMachine(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'v1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"v1" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV1(content)
                self.stack.pop()
                done = 1
        elif name == 'v2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"v2" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV2(content)
                self.stack.pop()
                done = 1
        elif name == 'v3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except Exception:
                        self.reportError('"v3" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV3(content)
                self.stack.pop()
                done = 1
        elif name == 'enabled':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content and content in ('true', '1'):
                    content = 1
                else:
                    content = 0
                self.stack[-2].obj.setEnabled(content)
                self.stack.pop()
                done = 1
        elif name == 'name':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setName(content)
                self.stack.pop()
                done = 1
        elif name == 'XSOptionItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSOptionItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSParamItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSParamItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSParamList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSParamList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSOptionList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSOptionList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSPluginItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSPluginItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dx':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDx(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dz':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDz(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'tag':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTag(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'space':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpace(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'a':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setA(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'b':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setB(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'c':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setC(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'alpha':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAlpha(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'gamma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGamma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shift':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setShift(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'core':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCore(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'edge':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEdge(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rmax':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmax(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nitrogen':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNitrogen(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'argon':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setArgon(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'krypton':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKrypton(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'index':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIndex(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'feff':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFeff(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'feff8':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFeff8(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'corrections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCorrections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'geom':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGeom(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'p1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setP1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ihole':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIhole(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 's02':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setS02(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'critcw':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCritcw(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'critpw':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCritpw(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'temp':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTemp(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'tempDebye':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTempDebye(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'idwopt':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIdwopt(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mphase':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMphase(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mpath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMpath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mfeff':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMfeff(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mchi':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMchi(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ipot':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIpot(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setZ(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'element':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setElement(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'distance':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDistance(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'file':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'header':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addHeader(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'title':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTitle(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hole':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHole(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'control':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setControl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'print':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPrint(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nleg':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNleg(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'potentials':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPotentials(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'atoms':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addAtoms(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'scriptFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScriptFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sessionFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSessionFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'energy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEnergy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'xmu':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXmu(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'group':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pre1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPre1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pre2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPre2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'norm1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNorm1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'norm2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNorm2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e0':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE0(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'edgeStep':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEdgeStep(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'preSlope':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPreSlope(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'preOffset':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPreOffset(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'preEdgeData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addPreEdgeData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'normC0':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNormC0(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'normC1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNormC1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'normC2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNormC2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'normData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addNormData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rbkg':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRbkg(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'toler':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setToler(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nKnots':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNKnots(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kminSpl':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKminSpl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kmaxSpl':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKmaxSpl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kweightSpl':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKweightSpl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dk1Spl':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDk1Spl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dk2Spl':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDk2Spl(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kwindow':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKwindow(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'real':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imag':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImag(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'k':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setK(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kmin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKmin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kmax':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKmax(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dk1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDk1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dk2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDk2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dk':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDk(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kweight':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKweight(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rmaxOut':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmaxOut(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'winData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addWinData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addRData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chiRMagData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addChiRMagData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chiRReData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addChiRReData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chiRImData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addChiRImData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kWindow':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKWindow(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'label':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLabel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataEnergy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataEnergy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataI0':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataI0(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataIref':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataIref(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataIt':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataIt(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataLnI0Iref':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataLnI0Iref(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataLnI0It':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataLnI0It(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'xafsExperimentData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXafsExperimentData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'preEdgeDataInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPreEdgeDataInput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'splineDataInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSplineDataInput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fftfDataInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFftfDataInput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'preEdgeDataResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPreEdgeDataResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'normDataResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNormDataResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'splineDataResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSplineDataResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rDataResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addRDataResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'crystal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCrystal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sample':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSample(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'flags':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFlags(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sites':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSites(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'outputFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutputFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'inpFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInpFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'optionsFeff':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOptionsFeff(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def characters(self, chrs, start, end):
        if len(self.stack) > 0:
            self.stack[-1].content += chrs[start:end]

    def reportError(self, mesg):
        locator = self.locator
        sys.stderr.write('Doc: %s  Line: %d  Column: %d\n' % \
            (locator.getSystemId(), locator.getLineNumber(), 
            locator.getColumnNumber() + 1))
        sys.stderr.write(mesg)
        sys.stderr.write('\n')
        sys.exit(-1)
        #raise RuntimeError

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
Options:
    -s        Use the SAX parser, not the minidom parser.
"""

def usage():
    print USAGE_TEXT
    sys.exit(-1)


#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in globals():
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = globals()[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = SaxXSConfigurationHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxXSConfigurationHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSConfiguration")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSConfiguration")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from XSDataIfeffit import *\n\n')
    sys.stdout.write('rootObj = XSConfiguration(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSConfiguration")
    sys.stdout.write(')\n')
    return rootObj

class XSDataIfeffit:
    pass


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-s':
        saxParse(args[1])
    elif len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')

