#!/usr/bin/env python

#
# Generated Mon Jun 20 15:57:10 2011 by EDGenerateDS.py.
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
        if self.getConfiguration() != None :
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
    def __init__(self, status=None):
        XSData.__init__(self)
        self.status = status
    def factory(*args_, **kwargs_):
        if XSDataResult.subclass:
            return XSDataResult.subclass(*args_, **kwargs_)
        else:
            return XSDataResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatus(self): return self.status
    def setStatus(self, status): self.status = status
    def export(self, outfile, level, name_='XSDataResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResult'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataResult')
    def exportChildren(self, outfile, level, name_='XSDataResult'):
        if self.getStatus() != None :
            if self.status:
                self.status.export(outfile, level, name_='status')
        XSData.exportChildren(self, outfile, level, name_)

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
        if self.status:
            showIndent(outfile, level)
            outfile.write('status=XSDataStatus(\n')
            self.status.exportLiteral(outfile, level, name_='status')
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
            nodeName_ == 'status':
            obj_ = XSDataStatus.factory()
            obj_.build(child_)
            self.setStatus(obj_)
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
    def __init__(self, executiveSummary=None, isSuccess=None, executionInfo=None, message=None):
        XSData.__init__(self)
        self.executiveSummary = executiveSummary
        self.isSuccess = isSuccess
        self.executionInfo = executionInfo
        self.message = message
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
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
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
        if self.getMessage() != None :
            if self.message:
                self.message.export(outfile, level, name_='message')
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
        if self.message:
            showIndent(outfile, level)
            outfile.write('message=XSDataMessage(\n')
            self.message.exportLiteral(outfile, level, name_='message')
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            obj_ = XSDataMessage.factory()
            obj_.build(child_)
            self.setMessage(obj_)
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


class XSDataInputGnom(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, experimentalDataQ=None, experimentalDataValues=None, experimentalDataStdDev=None, rMax=None, angularScale=None, mode=None):
        XSDataInput.__init__(self, configuration)
        if experimentalDataQ is None:
            self.experimentalDataQ = []
        else:
            self.experimentalDataQ = experimentalDataQ
        if experimentalDataValues is None:
            self.experimentalDataValues = []
        else:
            self.experimentalDataValues = experimentalDataValues
        if experimentalDataStdDev is None:
            self.experimentalDataStdDev = []
        else:
            self.experimentalDataStdDev = experimentalDataStdDev
        self.rMax = rMax
        self.angularScale = angularScale
        self.mode = mode
    def factory(*args_, **kwargs_):
        if XSDataInputGnom.subclass:
            return XSDataInputGnom.subclass(*args_, **kwargs_)
        else:
            return XSDataInputGnom(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExperimentalDataQ(self): return self.experimentalDataQ
    def setExperimentalDataQ(self, experimentalDataQ): self.experimentalDataQ = experimentalDataQ
    def addExperimentalDataQ(self, value): self.experimentalDataQ.append(value)
    def insertExperimentalDataQ(self, index, value): self.experimentalDataQ[index] = value
    def getExperimentalDataValues(self): return self.experimentalDataValues
    def setExperimentalDataValues(self, experimentalDataValues): self.experimentalDataValues = experimentalDataValues
    def addExperimentalDataValues(self, value): self.experimentalDataValues.append(value)
    def insertExperimentalDataValues(self, index, value): self.experimentalDataValues[index] = value
    def getExperimentalDataStdDev(self): return self.experimentalDataStdDev
    def setExperimentalDataStdDev(self, experimentalDataStdDev): self.experimentalDataStdDev = experimentalDataStdDev
    def addExperimentalDataStdDev(self, value): self.experimentalDataStdDev.append(value)
    def insertExperimentalDataStdDev(self, index, value): self.experimentalDataStdDev[index] = value
    def getRMax(self): return self.rMax
    def setRMax(self, rMax): self.rMax = rMax
    def getAngularScale(self): return self.angularScale
    def setAngularScale(self, angularScale): self.angularScale = angularScale
    def getMode(self): return self.mode
    def setMode(self, mode): self.mode = mode
    def export(self, outfile, level, name_='XSDataInputGnom'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputGnom'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputGnom')
    def exportChildren(self, outfile, level, name_='XSDataInputGnom'):
        for experimentalDataQ_ in self.getExperimentalDataQ():
            experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
        for experimentalDataValues_ in self.getExperimentalDataValues():
            experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
        for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
            experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
        if self.rMax:
            self.rMax.export(outfile, level, name_='rMax')
        if self.getAngularScale() != None :
            if self.angularScale:
                self.angularScale.export(outfile, level, name_='angularScale')
        if self.getMode() != None :
            if self.mode:
                self.mode.export(outfile, level, name_='mode')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputGnom' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputGnom'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('experimentalDataQ=[\n')
        level += 1
        for experimentalDataQ in self.experimentalDataQ:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataQ.exportLiteral(outfile, level, name_='experimentalDataQ')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataValues=[\n')
        level += 1
        for experimentalDataValues in self.experimentalDataValues:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataValues.exportLiteral(outfile, level, name_='experimentalDataValues')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataStdDev=[\n')
        level += 1
        for experimentalDataStdDev in self.experimentalDataStdDev:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataStdDev.exportLiteral(outfile, level, name_='experimentalDataStdDev')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.rMax:
            showIndent(outfile, level)
            outfile.write('rMax=XSDataFloat(\n')
            self.rMax.exportLiteral(outfile, level, name_='rMax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.angularScale:
            showIndent(outfile, level)
            outfile.write('angularScale=XSDataInteger(\n')
            self.angularScale.exportLiteral(outfile, level, name_='angularScale')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mode:
            showIndent(outfile, level)
            outfile.write('mode=XSDataString(\n')
            self.mode.exportLiteral(outfile, level, name_='mode')
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
            nodeName_ == 'experimentalDataQ':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataValues':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdDev':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataStdDev.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angularScale':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setAngularScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputGnom


class XSDataResultGnom(XSDataResult):
    subclass = None
    def __init__(self, status=None, fitQuality=None, output=None, scatteringFitQ=None, scatteringFitValues=None, distributionR=None, distributionPr=None, distributionErr=None, radiusOfCrossSection=None, radiusOfGyration=None):
        XSDataResult.__init__(self, status)
        self.fitQuality = fitQuality
        self.output = output
        if scatteringFitQ is None:
            self.scatteringFitQ = []
        else:
            self.scatteringFitQ = scatteringFitQ
        if scatteringFitValues is None:
            self.scatteringFitValues = []
        else:
            self.scatteringFitValues = scatteringFitValues
        if distributionR is None:
            self.distributionR = []
        else:
            self.distributionR = distributionR
        if distributionPr is None:
            self.distributionPr = []
        else:
            self.distributionPr = distributionPr
        if distributionErr is None:
            self.distributionErr = []
        else:
            self.distributionErr = distributionErr
        self.radiusOfCrossSection = radiusOfCrossSection
        self.radiusOfGyration = radiusOfGyration
    def factory(*args_, **kwargs_):
        if XSDataResultGnom.subclass:
            return XSDataResultGnom.subclass(*args_, **kwargs_)
        else:
            return XSDataResultGnom(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFitQuality(self): return self.fitQuality
    def setFitQuality(self, fitQuality): self.fitQuality = fitQuality
    def getOutput(self): return self.output
    def setOutput(self, output): self.output = output
    def getScatteringFitQ(self): return self.scatteringFitQ
    def setScatteringFitQ(self, scatteringFitQ): self.scatteringFitQ = scatteringFitQ
    def addScatteringFitQ(self, value): self.scatteringFitQ.append(value)
    def insertScatteringFitQ(self, index, value): self.scatteringFitQ[index] = value
    def getScatteringFitValues(self): return self.scatteringFitValues
    def setScatteringFitValues(self, scatteringFitValues): self.scatteringFitValues = scatteringFitValues
    def addScatteringFitValues(self, value): self.scatteringFitValues.append(value)
    def insertScatteringFitValues(self, index, value): self.scatteringFitValues[index] = value
    def getDistributionR(self): return self.distributionR
    def setDistributionR(self, distributionR): self.distributionR = distributionR
    def addDistributionR(self, value): self.distributionR.append(value)
    def insertDistributionR(self, index, value): self.distributionR[index] = value
    def getDistributionPr(self): return self.distributionPr
    def setDistributionPr(self, distributionPr): self.distributionPr = distributionPr
    def addDistributionPr(self, value): self.distributionPr.append(value)
    def insertDistributionPr(self, index, value): self.distributionPr[index] = value
    def getDistributionErr(self): return self.distributionErr
    def setDistributionErr(self, distributionErr): self.distributionErr = distributionErr
    def addDistributionErr(self, value): self.distributionErr.append(value)
    def insertDistributionErr(self, index, value): self.distributionErr[index] = value
    def getRadiusOfCrossSection(self): return self.radiusOfCrossSection
    def setRadiusOfCrossSection(self, radiusOfCrossSection): self.radiusOfCrossSection = radiusOfCrossSection
    def getRadiusOfGyration(self): return self.radiusOfGyration
    def setRadiusOfGyration(self, radiusOfGyration): self.radiusOfGyration = radiusOfGyration
    def export(self, outfile, level, name_='XSDataResultGnom'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultGnom'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultGnom')
    def exportChildren(self, outfile, level, name_='XSDataResultGnom'):
        if self.fitQuality:
            self.fitQuality.export(outfile, level, name_='fitQuality')
        if self.output:
            self.output.export(outfile, level, name_='output')
        for scatteringFitQ_ in self.getScatteringFitQ():
            scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
        for scatteringFitValues_ in self.getScatteringFitValues():
            scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
        for distributionR_ in self.getDistributionR():
            distributionR_.export(outfile, level, name_='distributionR')
        for distributionPr_ in self.getDistributionPr():
            distributionPr_.export(outfile, level, name_='distributionPr')
        for distributionErr_ in self.getDistributionErr():
            distributionErr_.export(outfile, level, name_='distributionErr')
        if self.radiusOfCrossSection:
            self.radiusOfCrossSection.export(outfile, level, name_='radiusOfCrossSection')
        if self.radiusOfGyration:
            self.radiusOfGyration.export(outfile, level, name_='radiusOfGyration')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultGnom' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultGnom'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.fitQuality:
            showIndent(outfile, level)
            outfile.write('fitQuality=XSDataFloat(\n')
            self.fitQuality.exportLiteral(outfile, level, name_='fitQuality')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.output:
            showIndent(outfile, level)
            outfile.write('output=XSDataFile(\n')
            self.output.exportLiteral(outfile, level, name_='output')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('scatteringFitQ=[\n')
        level += 1
        for scatteringFitQ in self.scatteringFitQ:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            scatteringFitQ.exportLiteral(outfile, level, name_='scatteringFitQ')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('scatteringFitValues=[\n')
        level += 1
        for scatteringFitValues in self.scatteringFitValues:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            scatteringFitValues.exportLiteral(outfile, level, name_='scatteringFitValues')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('distributionR=[\n')
        level += 1
        for distributionR in self.distributionR:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            distributionR.exportLiteral(outfile, level, name_='distributionR')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('distributionPr=[\n')
        level += 1
        for distributionPr in self.distributionPr:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            distributionPr.exportLiteral(outfile, level, name_='distributionPr')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('distributionErr=[\n')
        level += 1
        for distributionErr in self.distributionErr:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            distributionErr.exportLiteral(outfile, level, name_='distributionErr')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.radiusOfCrossSection:
            showIndent(outfile, level)
            outfile.write('radiusOfCrossSection=XSDataFloat(\n')
            self.radiusOfCrossSection.exportLiteral(outfile, level, name_='radiusOfCrossSection')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.radiusOfGyration:
            showIndent(outfile, level)
            outfile.write('radiusOfGyration=XSDataFloat(\n')
            self.radiusOfGyration.exportLiteral(outfile, level, name_='radiusOfGyration')
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
            nodeName_ == 'fitQuality':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFitQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQ':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.scatteringFitQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitValues':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.scatteringFitValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.distributionR.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionPr':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.distributionPr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionErr':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.distributionErr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfCrossSection':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRadiusOfCrossSection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfGyration':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRadiusOfGyration(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultGnom


class XSDataInputDammin(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, expectedParticleShape=None, gnomOutputFile=None, initialDummyAtomModel=None, pdbInputFile=None, symmetry=None, mode=None):
        XSDataInput.__init__(self, configuration)
        self.expectedParticleShape = expectedParticleShape
        self.gnomOutputFile = gnomOutputFile
        self.initialDummyAtomModel = initialDummyAtomModel
        self.pdbInputFile = pdbInputFile
        self.symmetry = symmetry
        self.mode = mode
    def factory(*args_, **kwargs_):
        if XSDataInputDammin.subclass:
            return XSDataInputDammin.subclass(*args_, **kwargs_)
        else:
            return XSDataInputDammin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExpectedParticleShape(self): return self.expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape): self.expectedParticleShape = expectedParticleShape
    def getGnomOutputFile(self): return self.gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile): self.gnomOutputFile = gnomOutputFile
    def getInitialDummyAtomModel(self): return self.initialDummyAtomModel
    def setInitialDummyAtomModel(self, initialDummyAtomModel): self.initialDummyAtomModel = initialDummyAtomModel
    def getPdbInputFile(self): return self.pdbInputFile
    def setPdbInputFile(self, pdbInputFile): self.pdbInputFile = pdbInputFile
    def getSymmetry(self): return self.symmetry
    def setSymmetry(self, symmetry): self.symmetry = symmetry
    def getMode(self): return self.mode
    def setMode(self, mode): self.mode = mode
    def export(self, outfile, level, name_='XSDataInputDammin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputDammin'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputDammin')
    def exportChildren(self, outfile, level, name_='XSDataInputDammin'):
        if self.expectedParticleShape:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        if self.gnomOutputFile:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        if self.initialDummyAtomModel:
            self.initialDummyAtomModel.export(outfile, level, name_='initialDummyAtomModel')
        if self.pdbInputFile:
            self.pdbInputFile.export(outfile, level, name_='pdbInputFile')
        if self.symmetry:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self.getMode() != None :
            if self.mode:
                self.mode.export(outfile, level, name_='mode')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputDammin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputDammin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.expectedParticleShape:
            showIndent(outfile, level)
            outfile.write('expectedParticleShape=XSDataInteger(\n')
            self.expectedParticleShape.exportLiteral(outfile, level, name_='expectedParticleShape')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.gnomOutputFile:
            showIndent(outfile, level)
            outfile.write('gnomOutputFile=XSDataFile(\n')
            self.gnomOutputFile.exportLiteral(outfile, level, name_='gnomOutputFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialDummyAtomModel:
            showIndent(outfile, level)
            outfile.write('initialDummyAtomModel=XSDataInteger(\n')
            self.initialDummyAtomModel.exportLiteral(outfile, level, name_='initialDummyAtomModel')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbInputFile:
            showIndent(outfile, level)
            outfile.write('pdbInputFile=XSDataFile(\n')
            self.pdbInputFile.exportLiteral(outfile, level, name_='pdbInputFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.symmetry:
            showIndent(outfile, level)
            outfile.write('symmetry=XSDataString(\n')
            self.symmetry.exportLiteral(outfile, level, name_='symmetry')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mode:
            showIndent(outfile, level)
            outfile.write('mode=XSDataString(\n')
            self.mode.exportLiteral(outfile, level, name_='mode')
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
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialDummyAtomModel':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setInitialDummyAtomModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbInputFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbInputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputDammin


class XSDataResultDammin(XSDataResult):
    subclass = None
    def __init__(self, status=None, fitFile=None, logFile=None, pdbMoleculeFile=None, pdbSolventFile=None, rfactor=None, chiSqrt=None):
        XSDataResult.__init__(self, status)
        self.fitFile = fitFile
        self.logFile = logFile
        self.pdbMoleculeFile = pdbMoleculeFile
        self.pdbSolventFile = pdbSolventFile
        self.rfactor = rfactor
        self.chiSqrt = chiSqrt
    def factory(*args_, **kwargs_):
        if XSDataResultDammin.subclass:
            return XSDataResultDammin.subclass(*args_, **kwargs_)
        else:
            return XSDataResultDammin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFitFile(self): return self.fitFile
    def setFitFile(self, fitFile): self.fitFile = fitFile
    def getLogFile(self): return self.logFile
    def setLogFile(self, logFile): self.logFile = logFile
    def getPdbMoleculeFile(self): return self.pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile): self.pdbMoleculeFile = pdbMoleculeFile
    def getPdbSolventFile(self): return self.pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile): self.pdbSolventFile = pdbSolventFile
    def getRfactor(self): return self.rfactor
    def setRfactor(self, rfactor): self.rfactor = rfactor
    def getChiSqrt(self): return self.chiSqrt
    def setChiSqrt(self, chiSqrt): self.chiSqrt = chiSqrt
    def export(self, outfile, level, name_='XSDataResultDammin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultDammin'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultDammin')
    def exportChildren(self, outfile, level, name_='XSDataResultDammin'):
        if self.fitFile:
            self.fitFile.export(outfile, level, name_='fitFile')
        if self.logFile:
            self.logFile.export(outfile, level, name_='logFile')
        if self.pdbMoleculeFile:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        if self.pdbSolventFile:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        if self.getRfactor() != None :
            if self.rfactor:
                self.rfactor.export(outfile, level, name_='rfactor')
        if self.getChiSqrt() != None :
            if self.chiSqrt:
                self.chiSqrt.export(outfile, level, name_='chiSqrt')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultDammin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultDammin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.fitFile:
            showIndent(outfile, level)
            outfile.write('fitFile=XSDataFile(\n')
            self.fitFile.exportLiteral(outfile, level, name_='fitFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.logFile:
            showIndent(outfile, level)
            outfile.write('logFile=XSDataFile(\n')
            self.logFile.exportLiteral(outfile, level, name_='logFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbMoleculeFile:
            showIndent(outfile, level)
            outfile.write('pdbMoleculeFile=XSDataFile(\n')
            self.pdbMoleculeFile.exportLiteral(outfile, level, name_='pdbMoleculeFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbSolventFile:
            showIndent(outfile, level)
            outfile.write('pdbSolventFile=XSDataFile(\n')
            self.pdbSolventFile.exportLiteral(outfile, level, name_='pdbSolventFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rfactor:
            showIndent(outfile, level)
            outfile.write('rfactor=XSDataFloat(\n')
            self.rfactor.exportLiteral(outfile, level, name_='rfactor')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.chiSqrt:
            showIndent(outfile, level)
            outfile.write('chiSqrt=XSDataFloat(\n')
            self.chiSqrt.exportLiteral(outfile, level, name_='chiSqrt')
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
            nodeName_ == 'fitFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultDammin


class XSDataInputDammif(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, expectedParticleShape=None, gnomOutputFile=None, unit=None, symmetry=None, mode=None, chained=None, constant=None):
        XSDataInput.__init__(self, configuration)
        self.expectedParticleShape = expectedParticleShape
        self.gnomOutputFile = gnomOutputFile
        self.unit = unit
        self.symmetry = symmetry
        self.mode = mode
        self.chained = chained
        self.constant = constant
    def factory(*args_, **kwargs_):
        if XSDataInputDammif.subclass:
            return XSDataInputDammif.subclass(*args_, **kwargs_)
        else:
            return XSDataInputDammif(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExpectedParticleShape(self): return self.expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape): self.expectedParticleShape = expectedParticleShape
    def getGnomOutputFile(self): return self.gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile): self.gnomOutputFile = gnomOutputFile
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getSymmetry(self): return self.symmetry
    def setSymmetry(self, symmetry): self.symmetry = symmetry
    def getMode(self): return self.mode
    def setMode(self, mode): self.mode = mode
    def getChained(self): return self.chained
    def setChained(self, chained): self.chained = chained
    def getConstant(self): return self.constant
    def setConstant(self, constant): self.constant = constant
    def export(self, outfile, level, name_='XSDataInputDammif'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputDammif'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputDammif')
    def exportChildren(self, outfile, level, name_='XSDataInputDammif'):
        if self.expectedParticleShape:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        if self.gnomOutputFile:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.symmetry:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self.getMode() != None :
            if self.mode:
                self.mode.export(outfile, level, name_='mode')
        if self.getChained() != None :
            if self.chained:
                self.chained.export(outfile, level, name_='chained')
        if self.getConstant() != None :
            if self.constant:
                self.constant.export(outfile, level, name_='constant')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputDammif' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputDammif'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.expectedParticleShape:
            showIndent(outfile, level)
            outfile.write('expectedParticleShape=XSDataInteger(\n')
            self.expectedParticleShape.exportLiteral(outfile, level, name_='expectedParticleShape')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.gnomOutputFile:
            showIndent(outfile, level)
            outfile.write('gnomOutputFile=XSDataFile(\n')
            self.gnomOutputFile.exportLiteral(outfile, level, name_='gnomOutputFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataString(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.symmetry:
            showIndent(outfile, level)
            outfile.write('symmetry=XSDataString(\n')
            self.symmetry.exportLiteral(outfile, level, name_='symmetry')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mode:
            showIndent(outfile, level)
            outfile.write('mode=XSDataString(\n')
            self.mode.exportLiteral(outfile, level, name_='mode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.chained:
            showIndent(outfile, level)
            outfile.write('chained=XSDataBoolean(\n')
            self.chained.exportLiteral(outfile, level, name_='chained')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.constant:
            showIndent(outfile, level)
            outfile.write('constant=XSDataFloat(\n')
            self.constant.exportLiteral(outfile, level, name_='constant')
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
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chained':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setChained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'constant':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setConstant(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputDammif


class XSDataResultDammif(XSDataResult):
    subclass = None
    def __init__(self, status=None, fitFile=None, logFile=None, pdbMoleculeFile=None, pdbSolventFile=None, rfactor=None, chiSqrt=None):
        XSDataResult.__init__(self, status)
        self.fitFile = fitFile
        self.logFile = logFile
        self.pdbMoleculeFile = pdbMoleculeFile
        self.pdbSolventFile = pdbSolventFile
        self.rfactor = rfactor
        self.chiSqrt = chiSqrt
    def factory(*args_, **kwargs_):
        if XSDataResultDammif.subclass:
            return XSDataResultDammif.subclass(*args_, **kwargs_)
        else:
            return XSDataResultDammif(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFitFile(self): return self.fitFile
    def setFitFile(self, fitFile): self.fitFile = fitFile
    def getLogFile(self): return self.logFile
    def setLogFile(self, logFile): self.logFile = logFile
    def getPdbMoleculeFile(self): return self.pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile): self.pdbMoleculeFile = pdbMoleculeFile
    def getPdbSolventFile(self): return self.pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile): self.pdbSolventFile = pdbSolventFile
    def getRfactor(self): return self.rfactor
    def setRfactor(self, rfactor): self.rfactor = rfactor
    def getChiSqrt(self): return self.chiSqrt
    def setChiSqrt(self, chiSqrt): self.chiSqrt = chiSqrt
    def export(self, outfile, level, name_='XSDataResultDammif'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultDammif'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultDammif')
    def exportChildren(self, outfile, level, name_='XSDataResultDammif'):
        if self.fitFile:
            self.fitFile.export(outfile, level, name_='fitFile')
        if self.logFile:
            self.logFile.export(outfile, level, name_='logFile')
        if self.pdbMoleculeFile:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        if self.pdbSolventFile:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        if self.getRfactor() != None :
            if self.rfactor:
                self.rfactor.export(outfile, level, name_='rfactor')
        if self.getChiSqrt() != None :
            if self.chiSqrt:
                self.chiSqrt.export(outfile, level, name_='chiSqrt')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultDammif' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultDammif'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.fitFile:
            showIndent(outfile, level)
            outfile.write('fitFile=XSDataFile(\n')
            self.fitFile.exportLiteral(outfile, level, name_='fitFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.logFile:
            showIndent(outfile, level)
            outfile.write('logFile=XSDataFile(\n')
            self.logFile.exportLiteral(outfile, level, name_='logFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbMoleculeFile:
            showIndent(outfile, level)
            outfile.write('pdbMoleculeFile=XSDataFile(\n')
            self.pdbMoleculeFile.exportLiteral(outfile, level, name_='pdbMoleculeFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbSolventFile:
            showIndent(outfile, level)
            outfile.write('pdbSolventFile=XSDataFile(\n')
            self.pdbSolventFile.exportLiteral(outfile, level, name_='pdbSolventFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rfactor:
            showIndent(outfile, level)
            outfile.write('rfactor=XSDataFloat(\n')
            self.rfactor.exportLiteral(outfile, level, name_='rfactor')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.chiSqrt:
            showIndent(outfile, level)
            outfile.write('chiSqrt=XSDataFloat(\n')
            self.chiSqrt.exportLiteral(outfile, level, name_='chiSqrt')
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
            nodeName_ == 'fitFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultDammif


class XSDataInputSolutionScattering(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, title=None, experimentalDataQ=None, experimentalDataValues=None, experimentalDataStdDev=None, rMaxSearchSettings=None, angularUnits=None, symmetry=None, mode=None, iNbThreads=None, onlyGnom=None, plotFit=None):
        XSDataInput.__init__(self, configuration)
        self.title = title
        if experimentalDataQ is None:
            self.experimentalDataQ = []
        else:
            self.experimentalDataQ = experimentalDataQ
        if experimentalDataValues is None:
            self.experimentalDataValues = []
        else:
            self.experimentalDataValues = experimentalDataValues
        if experimentalDataStdDev is None:
            self.experimentalDataStdDev = []
        else:
            self.experimentalDataStdDev = experimentalDataStdDev
        self.rMaxSearchSettings = rMaxSearchSettings
        self.angularUnits = angularUnits
        self.symmetry = symmetry
        self.mode = mode
        self.iNbThreads = iNbThreads
        self.onlyGnom = onlyGnom
        self.plotFit = plotFit
    def factory(*args_, **kwargs_):
        if XSDataInputSolutionScattering.subclass:
            return XSDataInputSolutionScattering.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSolutionScattering(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getTitle(self): return self.title
    def setTitle(self, title): self.title = title
    def getExperimentalDataQ(self): return self.experimentalDataQ
    def setExperimentalDataQ(self, experimentalDataQ): self.experimentalDataQ = experimentalDataQ
    def addExperimentalDataQ(self, value): self.experimentalDataQ.append(value)
    def insertExperimentalDataQ(self, index, value): self.experimentalDataQ[index] = value
    def getExperimentalDataValues(self): return self.experimentalDataValues
    def setExperimentalDataValues(self, experimentalDataValues): self.experimentalDataValues = experimentalDataValues
    def addExperimentalDataValues(self, value): self.experimentalDataValues.append(value)
    def insertExperimentalDataValues(self, index, value): self.experimentalDataValues[index] = value
    def getExperimentalDataStdDev(self): return self.experimentalDataStdDev
    def setExperimentalDataStdDev(self, experimentalDataStdDev): self.experimentalDataStdDev = experimentalDataStdDev
    def addExperimentalDataStdDev(self, value): self.experimentalDataStdDev.append(value)
    def insertExperimentalDataStdDev(self, index, value): self.experimentalDataStdDev[index] = value
    def getRMaxSearchSettings(self): return self.rMaxSearchSettings
    def setRMaxSearchSettings(self, rMaxSearchSettings): self.rMaxSearchSettings = rMaxSearchSettings
    def getAngularUnits(self): return self.angularUnits
    def setAngularUnits(self, angularUnits): self.angularUnits = angularUnits
    def getSymmetry(self): return self.symmetry
    def setSymmetry(self, symmetry): self.symmetry = symmetry
    def getMode(self): return self.mode
    def setMode(self, mode): self.mode = mode
    def getINbThreads(self): return self.iNbThreads
    def setINbThreads(self, iNbThreads): self.iNbThreads = iNbThreads
    def getOnlyGnom(self): return self.onlyGnom
    def setOnlyGnom(self, onlyGnom): self.onlyGnom = onlyGnom
    def getPlotFit(self): return self.plotFit
    def setPlotFit(self, plotFit): self.plotFit = plotFit
    def export(self, outfile, level, name_='XSDataInputSolutionScattering'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSolutionScattering'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSolutionScattering')
    def exportChildren(self, outfile, level, name_='XSDataInputSolutionScattering'):
        if self.getTitle() != None :
            if self.title:
                self.title.export(outfile, level, name_='title')
        for experimentalDataQ_ in self.getExperimentalDataQ():
            experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
        for experimentalDataValues_ in self.getExperimentalDataValues():
            experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
        for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
            experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
        if self.getRMaxSearchSettings() != None :
            if self.rMaxSearchSettings:
                self.rMaxSearchSettings.export(outfile, level, name_='rMaxSearchSettings')
        if self.getAngularUnits() != None :
            if self.angularUnits:
                self.angularUnits.export(outfile, level, name_='angularUnits')
        if self.getSymmetry() != None :
            if self.symmetry:
                self.symmetry.export(outfile, level, name_='symmetry')
        if self.getMode() != None :
            if self.mode:
                self.mode.export(outfile, level, name_='mode')
        if self.getINbThreads() != None :
            if self.iNbThreads:
                self.iNbThreads.export(outfile, level, name_='iNbThreads')
        if self.getOnlyGnom() != None :
            if self.onlyGnom:
                self.onlyGnom.export(outfile, level, name_='onlyGnom')
        if self.getPlotFit() != None :
            if self.plotFit:
                self.plotFit.export(outfile, level, name_='plotFit')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSolutionScattering' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSolutionScattering.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSolutionScattering.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSolutionScattering" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSolutionScattering'):
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
        showIndent(outfile, level)
        outfile.write('experimentalDataQ=[\n')
        level += 1
        for experimentalDataQ in self.experimentalDataQ:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataQ.exportLiteral(outfile, level, name_='experimentalDataQ')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataValues=[\n')
        level += 1
        for experimentalDataValues in self.experimentalDataValues:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataValues.exportLiteral(outfile, level, name_='experimentalDataValues')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('experimentalDataStdDev=[\n')
        level += 1
        for experimentalDataStdDev in self.experimentalDataStdDev:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            experimentalDataStdDev.exportLiteral(outfile, level, name_='experimentalDataStdDev')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.rMaxSearchSettings:
            showIndent(outfile, level)
            outfile.write('rMaxSearchSettings=XSDataSolutionScatteringSettings(\n')
            self.rMaxSearchSettings.exportLiteral(outfile, level, name_='rMaxSearchSettings')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.angularUnits:
            showIndent(outfile, level)
            outfile.write('angularUnits=XSDataInteger(\n')
            self.angularUnits.exportLiteral(outfile, level, name_='angularUnits')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.symmetry:
            showIndent(outfile, level)
            outfile.write('symmetry=XSDataString(\n')
            self.symmetry.exportLiteral(outfile, level, name_='symmetry')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mode:
            showIndent(outfile, level)
            outfile.write('mode=XSDataString(\n')
            self.mode.exportLiteral(outfile, level, name_='mode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iNbThreads:
            showIndent(outfile, level)
            outfile.write('iNbThreads=XSDataInteger(\n')
            self.iNbThreads.exportLiteral(outfile, level, name_='iNbThreads')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.onlyGnom:
            showIndent(outfile, level)
            outfile.write('onlyGnom=XSDataBoolean(\n')
            self.onlyGnom.exportLiteral(outfile, level, name_='onlyGnom')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.plotFit:
            showIndent(outfile, level)
            outfile.write('plotFit=XSDataBoolean(\n')
            self.plotFit.exportLiteral(outfile, level, name_='plotFit')
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
            nodeName_ == 'experimentalDataQ':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataValues':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdDev':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.experimentalDataStdDev.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMaxSearchSettings':
            obj_ = XSDataSolutionScatteringSettings.factory()
            obj_.build(child_)
            self.setRMaxSearchSettings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angularUnits':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setAngularUnits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iNbThreads':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setINbThreads(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'onlyGnom':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setOnlyGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plotFit':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setPlotFit(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSolutionScattering


class XSDataResultSolutionScattering(XSDataResult):
    subclass = None
    def __init__(self, status=None, corelationFitValues=None, fitFile=None, lineProfileFitQuality=None, logFile=None, pdbMoleculeFile=None, pdbSolventFile=None, scatteringFitQ=None, scatteringFitValues=None, meanNSD=None, variationNSD=None):
        XSDataResult.__init__(self, status)
        if corelationFitValues is None:
            self.corelationFitValues = []
        else:
            self.corelationFitValues = corelationFitValues
        self.fitFile = fitFile
        self.lineProfileFitQuality = lineProfileFitQuality
        self.logFile = logFile
        self.pdbMoleculeFile = pdbMoleculeFile
        self.pdbSolventFile = pdbSolventFile
        if scatteringFitQ is None:
            self.scatteringFitQ = []
        else:
            self.scatteringFitQ = scatteringFitQ
        if scatteringFitValues is None:
            self.scatteringFitValues = []
        else:
            self.scatteringFitValues = scatteringFitValues
        self.meanNSD = meanNSD
        self.variationNSD = variationNSD
    def factory(*args_, **kwargs_):
        if XSDataResultSolutionScattering.subclass:
            return XSDataResultSolutionScattering.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSolutionScattering(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCorelationFitValues(self): return self.corelationFitValues
    def setCorelationFitValues(self, corelationFitValues): self.corelationFitValues = corelationFitValues
    def addCorelationFitValues(self, value): self.corelationFitValues.append(value)
    def insertCorelationFitValues(self, index, value): self.corelationFitValues[index] = value
    def getFitFile(self): return self.fitFile
    def setFitFile(self, fitFile): self.fitFile = fitFile
    def getLineProfileFitQuality(self): return self.lineProfileFitQuality
    def setLineProfileFitQuality(self, lineProfileFitQuality): self.lineProfileFitQuality = lineProfileFitQuality
    def getLogFile(self): return self.logFile
    def setLogFile(self, logFile): self.logFile = logFile
    def getPdbMoleculeFile(self): return self.pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile): self.pdbMoleculeFile = pdbMoleculeFile
    def getPdbSolventFile(self): return self.pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile): self.pdbSolventFile = pdbSolventFile
    def getScatteringFitQ(self): return self.scatteringFitQ
    def setScatteringFitQ(self, scatteringFitQ): self.scatteringFitQ = scatteringFitQ
    def addScatteringFitQ(self, value): self.scatteringFitQ.append(value)
    def insertScatteringFitQ(self, index, value): self.scatteringFitQ[index] = value
    def getScatteringFitValues(self): return self.scatteringFitValues
    def setScatteringFitValues(self, scatteringFitValues): self.scatteringFitValues = scatteringFitValues
    def addScatteringFitValues(self, value): self.scatteringFitValues.append(value)
    def insertScatteringFitValues(self, index, value): self.scatteringFitValues[index] = value
    def getMeanNSD(self): return self.meanNSD
    def setMeanNSD(self, meanNSD): self.meanNSD = meanNSD
    def getVariationNSD(self): return self.variationNSD
    def setVariationNSD(self, variationNSD): self.variationNSD = variationNSD
    def export(self, outfile, level, name_='XSDataResultSolutionScattering'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSolutionScattering'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSolutionScattering')
    def exportChildren(self, outfile, level, name_='XSDataResultSolutionScattering'):
        for corelationFitValues_ in self.getCorelationFitValues():
            corelationFitValues_.export(outfile, level, name_='corelationFitValues')
        if self.fitFile:
            self.fitFile.export(outfile, level, name_='fitFile')
        if self.lineProfileFitQuality:
            self.lineProfileFitQuality.export(outfile, level, name_='lineProfileFitQuality')
        if self.logFile:
            self.logFile.export(outfile, level, name_='logFile')
        if self.pdbMoleculeFile:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        if self.pdbSolventFile:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        for scatteringFitQ_ in self.getScatteringFitQ():
            scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
        for scatteringFitValues_ in self.getScatteringFitValues():
            scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
        if self.getMeanNSD() != None :
            if self.meanNSD:
                self.meanNSD.export(outfile, level, name_='meanNSD')
        if self.getVariationNSD() != None :
            if self.variationNSD:
                self.variationNSD.export(outfile, level, name_='variationNSD')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSolutionScattering' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSolutionScattering.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSolutionScattering.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSolutionScattering" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSolutionScattering'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('corelationFitValues=[\n')
        level += 1
        for corelationFitValues in self.corelationFitValues:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            corelationFitValues.exportLiteral(outfile, level, name_='corelationFitValues')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.fitFile:
            showIndent(outfile, level)
            outfile.write('fitFile=XSDataFile(\n')
            self.fitFile.exportLiteral(outfile, level, name_='fitFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineProfileFitQuality:
            showIndent(outfile, level)
            outfile.write('lineProfileFitQuality=XSDataFloat(\n')
            self.lineProfileFitQuality.exportLiteral(outfile, level, name_='lineProfileFitQuality')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.logFile:
            showIndent(outfile, level)
            outfile.write('logFile=XSDataFile(\n')
            self.logFile.exportLiteral(outfile, level, name_='logFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbMoleculeFile:
            showIndent(outfile, level)
            outfile.write('pdbMoleculeFile=XSDataFile(\n')
            self.pdbMoleculeFile.exportLiteral(outfile, level, name_='pdbMoleculeFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pdbSolventFile:
            showIndent(outfile, level)
            outfile.write('pdbSolventFile=XSDataFile(\n')
            self.pdbSolventFile.exportLiteral(outfile, level, name_='pdbSolventFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('scatteringFitQ=[\n')
        level += 1
        for scatteringFitQ in self.scatteringFitQ:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            scatteringFitQ.exportLiteral(outfile, level, name_='scatteringFitQ')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('scatteringFitValues=[\n')
        level += 1
        for scatteringFitValues in self.scatteringFitValues:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            scatteringFitValues.exportLiteral(outfile, level, name_='scatteringFitValues')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.meanNSD:
            showIndent(outfile, level)
            outfile.write('meanNSD=XSDataFloat(\n')
            self.meanNSD.exportLiteral(outfile, level, name_='meanNSD')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.variationNSD:
            showIndent(outfile, level)
            outfile.write('variationNSD=XSDataFloat(\n')
            self.variationNSD.exportLiteral(outfile, level, name_='variationNSD')
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
            nodeName_ == 'corelationFitValues':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.corelationFitValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lineProfileFitQuality':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setLineProfileFitQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQ':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.scatteringFitQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitValues':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.scatteringFitValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'meanNSD':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMeanNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'variationNSD':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setVariationNSD(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultSolutionScattering


class XSDataConfigGnom(XSData):
    subclass = None
    def __init__(self, printer=None, forfac=None, expert=None, input1=None, input2=None, nskip1=None, nskip2=None, output=None, iscale=None, plonp=None, plores=None, evaerr=None, ploerr=None, lkern=None, jobtyp=None, rmin=None, rmax=None, lzrmin=None, lzrmax=None, kernel=None, deviat=None, idet=None, fwhm1=None, fwhm2=None, ah1=None, lh1=None, aw1=None, lw1=None, ah2=None, lh2=None, aw2=None, lw2=None, spot1=None, spot2=None, alpha=None, nreal=None, coef=None, rad56=None, nextjob=None):
        XSData.__init__(self)
        if printer is None:
            self.printer = []
        else:
            self.printer = printer
        self.forfac = forfac
        self.expert = expert
        self.input1 = input1
        self.input2 = input2
        self.nskip1 = nskip1
        self.nskip2 = nskip2
        self.output = output
        self.iscale = iscale
        self.plonp = plonp
        self.plores = plores
        self.evaerr = evaerr
        self.ploerr = ploerr
        self.lkern = lkern
        self.jobtyp = jobtyp
        self.rmin = rmin
        self.rmax = rmax
        self.lzrmin = lzrmin
        self.lzrmax = lzrmax
        self.kernel = kernel
        self.deviat = deviat
        self.idet = idet
        self.fwhm1 = fwhm1
        self.fwhm2 = fwhm2
        self.ah1 = ah1
        self.lh1 = lh1
        self.aw1 = aw1
        self.lw1 = lw1
        self.ah2 = ah2
        self.lh2 = lh2
        self.aw2 = aw2
        self.lw2 = lw2
        self.spot1 = spot1
        self.spot2 = spot2
        self.alpha = alpha
        self.nreal = nreal
        self.coef = coef
        self.rad56 = rad56
        self.nextjob = nextjob
    def factory(*args_, **kwargs_):
        if XSDataConfigGnom.subclass:
            return XSDataConfigGnom.subclass(*args_, **kwargs_)
        else:
            return XSDataConfigGnom(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPrinter(self): return self.printer
    def setPrinter(self, printer): self.printer = printer
    def addPrinter(self, value): self.printer.append(value)
    def insertPrinter(self, index, value): self.printer[index] = value
    def getForfac(self): return self.forfac
    def setForfac(self, forfac): self.forfac = forfac
    def getExpert(self): return self.expert
    def setExpert(self, expert): self.expert = expert
    def getInput1(self): return self.input1
    def setInput1(self, input1): self.input1 = input1
    def getInput2(self): return self.input2
    def setInput2(self, input2): self.input2 = input2
    def getNskip1(self): return self.nskip1
    def setNskip1(self, nskip1): self.nskip1 = nskip1
    def getNskip2(self): return self.nskip2
    def setNskip2(self, nskip2): self.nskip2 = nskip2
    def getOutput(self): return self.output
    def setOutput(self, output): self.output = output
    def getIscale(self): return self.iscale
    def setIscale(self, iscale): self.iscale = iscale
    def getPlonp(self): return self.plonp
    def setPlonp(self, plonp): self.plonp = plonp
    def getPlores(self): return self.plores
    def setPlores(self, plores): self.plores = plores
    def getEvaerr(self): return self.evaerr
    def setEvaerr(self, evaerr): self.evaerr = evaerr
    def getPloerr(self): return self.ploerr
    def setPloerr(self, ploerr): self.ploerr = ploerr
    def getLkern(self): return self.lkern
    def setLkern(self, lkern): self.lkern = lkern
    def getJobtyp(self): return self.jobtyp
    def setJobtyp(self, jobtyp): self.jobtyp = jobtyp
    def getRmin(self): return self.rmin
    def setRmin(self, rmin): self.rmin = rmin
    def getRmax(self): return self.rmax
    def setRmax(self, rmax): self.rmax = rmax
    def getLzrmin(self): return self.lzrmin
    def setLzrmin(self, lzrmin): self.lzrmin = lzrmin
    def getLzrmax(self): return self.lzrmax
    def setLzrmax(self, lzrmax): self.lzrmax = lzrmax
    def getKernel(self): return self.kernel
    def setKernel(self, kernel): self.kernel = kernel
    def getDeviat(self): return self.deviat
    def setDeviat(self, deviat): self.deviat = deviat
    def getIdet(self): return self.idet
    def setIdet(self, idet): self.idet = idet
    def getFwhm1(self): return self.fwhm1
    def setFwhm1(self, fwhm1): self.fwhm1 = fwhm1
    def getFwhm2(self): return self.fwhm2
    def setFwhm2(self, fwhm2): self.fwhm2 = fwhm2
    def getAh1(self): return self.ah1
    def setAh1(self, ah1): self.ah1 = ah1
    def getLh1(self): return self.lh1
    def setLh1(self, lh1): self.lh1 = lh1
    def getAw1(self): return self.aw1
    def setAw1(self, aw1): self.aw1 = aw1
    def getLw1(self): return self.lw1
    def setLw1(self, lw1): self.lw1 = lw1
    def getAh2(self): return self.ah2
    def setAh2(self, ah2): self.ah2 = ah2
    def getLh2(self): return self.lh2
    def setLh2(self, lh2): self.lh2 = lh2
    def getAw2(self): return self.aw2
    def setAw2(self, aw2): self.aw2 = aw2
    def getLw2(self): return self.lw2
    def setLw2(self, lw2): self.lw2 = lw2
    def getSpot1(self): return self.spot1
    def setSpot1(self, spot1): self.spot1 = spot1
    def getSpot2(self): return self.spot2
    def setSpot2(self, spot2): self.spot2 = spot2
    def getAlpha(self): return self.alpha
    def setAlpha(self, alpha): self.alpha = alpha
    def getNreal(self): return self.nreal
    def setNreal(self, nreal): self.nreal = nreal
    def getCoef(self): return self.coef
    def setCoef(self, coef): self.coef = coef
    def getRad56(self): return self.rad56
    def setRad56(self, rad56): self.rad56 = rad56
    def getNextjob(self): return self.nextjob
    def setNextjob(self, nextjob): self.nextjob = nextjob
    def export(self, outfile, level, name_='XSDataConfigGnom'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataConfigGnom'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataConfigGnom')
    def exportChildren(self, outfile, level, name_='XSDataConfigGnom'):
        for printer_ in self.getPrinter():
            printer_.export(outfile, level, name_='printer')
        if self.getForfac() != None :
            if self.forfac:
                self.forfac.export(outfile, level, name_='forfac')
        if self.getExpert() != None :
            if self.expert:
                self.expert.export(outfile, level, name_='expert')
        if self.input1:
            self.input1.export(outfile, level, name_='input1')
        if self.getInput2() != None :
            if self.input2:
                self.input2.export(outfile, level, name_='input2')
        if self.getNskip1() != None :
            if self.nskip1:
                self.nskip1.export(outfile, level, name_='nskip1')
        if self.getNskip2() != None :
            if self.nskip2:
                self.nskip2.export(outfile, level, name_='nskip2')
        if self.getOutput() != None :
            if self.output:
                self.output.export(outfile, level, name_='output')
        if self.getIscale() != None :
            if self.iscale:
                self.iscale.export(outfile, level, name_='iscale')
        if self.plonp:
            self.plonp.export(outfile, level, name_='plonp')
        if self.plores:
            self.plores.export(outfile, level, name_='plores')
        if self.getEvaerr() != None :
            if self.evaerr:
                self.evaerr.export(outfile, level, name_='evaerr')
        if self.ploerr:
            self.ploerr.export(outfile, level, name_='ploerr')
        if self.getLkern() != None :
            if self.lkern:
                self.lkern.export(outfile, level, name_='lkern')
        if self.getJobtyp() != None :
            if self.jobtyp:
                self.jobtyp.export(outfile, level, name_='jobtyp')
        if self.getRmin() != None :
            if self.rmin:
                self.rmin.export(outfile, level, name_='rmin')
        if self.getRmax() != None :
            if self.rmax:
                self.rmax.export(outfile, level, name_='rmax')
        if self.getLzrmin() != None :
            if self.lzrmin:
                self.lzrmin.export(outfile, level, name_='lzrmin')
        if self.getLzrmax() != None :
            if self.lzrmax:
                self.lzrmax.export(outfile, level, name_='lzrmax')
        if self.getKernel() != None :
            if self.kernel:
                self.kernel.export(outfile, level, name_='kernel')
        if self.deviat:
            self.deviat.export(outfile, level, name_='deviat')
        if self.getIdet() != None :
            if self.idet:
                self.idet.export(outfile, level, name_='idet')
        if self.getFwhm1() != None :
            if self.fwhm1:
                self.fwhm1.export(outfile, level, name_='fwhm1')
        if self.getFwhm2() != None :
            if self.fwhm2:
                self.fwhm2.export(outfile, level, name_='fwhm2')
        if self.getAh1() != None :
            if self.ah1:
                self.ah1.export(outfile, level, name_='ah1')
        if self.getLh1() != None :
            if self.lh1:
                self.lh1.export(outfile, level, name_='lh1')
        if self.getAw1() != None :
            if self.aw1:
                self.aw1.export(outfile, level, name_='aw1')
        if self.getLw1() != None :
            if self.lw1:
                self.lw1.export(outfile, level, name_='lw1')
        if self.getAh2() != None :
            if self.ah2:
                self.ah2.export(outfile, level, name_='ah2')
        if self.getLh2() != None :
            if self.lh2:
                self.lh2.export(outfile, level, name_='lh2')
        if self.getAw2() != None :
            if self.aw2:
                self.aw2.export(outfile, level, name_='aw2')
        if self.getLw2() != None :
            if self.lw2:
                self.lw2.export(outfile, level, name_='lw2')
        if self.getSpot1() != None :
            if self.spot1:
                self.spot1.export(outfile, level, name_='spot1')
        if self.getSpot2() != None :
            if self.spot2:
                self.spot2.export(outfile, level, name_='spot2')
        if self.alpha:
            self.alpha.export(outfile, level, name_='alpha')
        if self.nreal:
            self.nreal.export(outfile, level, name_='nreal')
        if self.getCoef() != None :
            if self.coef:
                self.coef.export(outfile, level, name_='coef')
        if self.getRad56() != None :
            if self.rad56:
                self.rad56.export(outfile, level, name_='rad56')
        if self.getNextjob() != None :
            if self.nextjob:
                self.nextjob.export(outfile, level, name_='nextjob')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataConfigGnom' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataConfigGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataConfigGnom'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('printer=[\n')
        level += 1
        for printer in self.printer:
            showIndent(outfile, level)
            outfile.write('XSDataString(\n')
            printer.exportLiteral(outfile, level, name_='printer')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.forfac:
            showIndent(outfile, level)
            outfile.write('forfac=XSDataFile(\n')
            self.forfac.exportLiteral(outfile, level, name_='forfac')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.expert:
            showIndent(outfile, level)
            outfile.write('expert=XSDataFile(\n')
            self.expert.exportLiteral(outfile, level, name_='expert')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.input1:
            showIndent(outfile, level)
            outfile.write('input1=XSDataFile(\n')
            self.input1.exportLiteral(outfile, level, name_='input1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.input2:
            showIndent(outfile, level)
            outfile.write('input2=XSDataFile(\n')
            self.input2.exportLiteral(outfile, level, name_='input2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nskip1:
            showIndent(outfile, level)
            outfile.write('nskip1=XSDataInteger(\n')
            self.nskip1.exportLiteral(outfile, level, name_='nskip1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nskip2:
            showIndent(outfile, level)
            outfile.write('nskip2=XSDataInteger(\n')
            self.nskip2.exportLiteral(outfile, level, name_='nskip2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.output:
            showIndent(outfile, level)
            outfile.write('output=XSDataFile(\n')
            self.output.exportLiteral(outfile, level, name_='output')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iscale:
            showIndent(outfile, level)
            outfile.write('iscale=XSDataInteger(\n')
            self.iscale.exportLiteral(outfile, level, name_='iscale')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.plonp:
            showIndent(outfile, level)
            outfile.write('plonp=XSDataBoolean(\n')
            self.plonp.exportLiteral(outfile, level, name_='plonp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.plores:
            showIndent(outfile, level)
            outfile.write('plores=XSDataBoolean(\n')
            self.plores.exportLiteral(outfile, level, name_='plores')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.evaerr:
            showIndent(outfile, level)
            outfile.write('evaerr=XSDataBoolean(\n')
            self.evaerr.exportLiteral(outfile, level, name_='evaerr')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ploerr:
            showIndent(outfile, level)
            outfile.write('ploerr=XSDataBoolean(\n')
            self.ploerr.exportLiteral(outfile, level, name_='ploerr')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lkern:
            showIndent(outfile, level)
            outfile.write('lkern=XSDataBoolean(\n')
            self.lkern.exportLiteral(outfile, level, name_='lkern')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.jobtyp:
            showIndent(outfile, level)
            outfile.write('jobtyp=XSDataInteger(\n')
            self.jobtyp.exportLiteral(outfile, level, name_='jobtyp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmin:
            showIndent(outfile, level)
            outfile.write('rmin=XSDataFloat(\n')
            self.rmin.exportLiteral(outfile, level, name_='rmin')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmax:
            showIndent(outfile, level)
            outfile.write('rmax=XSDataFloat(\n')
            self.rmax.exportLiteral(outfile, level, name_='rmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lzrmin:
            showIndent(outfile, level)
            outfile.write('lzrmin=XSDataBoolean(\n')
            self.lzrmin.exportLiteral(outfile, level, name_='lzrmin')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lzrmax:
            showIndent(outfile, level)
            outfile.write('lzrmax=XSDataBoolean(\n')
            self.lzrmax.exportLiteral(outfile, level, name_='lzrmax')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kernel:
            showIndent(outfile, level)
            outfile.write('kernel=XSDataFile(\n')
            self.kernel.exportLiteral(outfile, level, name_='kernel')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.deviat:
            showIndent(outfile, level)
            outfile.write('deviat=XSDataFloat(\n')
            self.deviat.exportLiteral(outfile, level, name_='deviat')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.idet:
            showIndent(outfile, level)
            outfile.write('idet=XSDataInteger(\n')
            self.idet.exportLiteral(outfile, level, name_='idet')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fwhm1:
            showIndent(outfile, level)
            outfile.write('fwhm1=XSDataFloat(\n')
            self.fwhm1.exportLiteral(outfile, level, name_='fwhm1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fwhm2:
            showIndent(outfile, level)
            outfile.write('fwhm2=XSDataFloat(\n')
            self.fwhm2.exportLiteral(outfile, level, name_='fwhm2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ah1:
            showIndent(outfile, level)
            outfile.write('ah1=XSDataFloat(\n')
            self.ah1.exportLiteral(outfile, level, name_='ah1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lh1:
            showIndent(outfile, level)
            outfile.write('lh1=XSDataFloat(\n')
            self.lh1.exportLiteral(outfile, level, name_='lh1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aw1:
            showIndent(outfile, level)
            outfile.write('aw1=XSDataFloat(\n')
            self.aw1.exportLiteral(outfile, level, name_='aw1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lw1:
            showIndent(outfile, level)
            outfile.write('lw1=XSDataFloat(\n')
            self.lw1.exportLiteral(outfile, level, name_='lw1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ah2:
            showIndent(outfile, level)
            outfile.write('ah2=XSDataFloat(\n')
            self.ah2.exportLiteral(outfile, level, name_='ah2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lh2:
            showIndent(outfile, level)
            outfile.write('lh2=XSDataFloat(\n')
            self.lh2.exportLiteral(outfile, level, name_='lh2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aw2:
            showIndent(outfile, level)
            outfile.write('aw2=XSDataFloat(\n')
            self.aw2.exportLiteral(outfile, level, name_='aw2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lw2:
            showIndent(outfile, level)
            outfile.write('lw2=XSDataFloat(\n')
            self.lw2.exportLiteral(outfile, level, name_='lw2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spot1:
            showIndent(outfile, level)
            outfile.write('spot1=XSDataFile(\n')
            self.spot1.exportLiteral(outfile, level, name_='spot1')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spot2:
            showIndent(outfile, level)
            outfile.write('spot2=XSDataFile(\n')
            self.spot2.exportLiteral(outfile, level, name_='spot2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.alpha:
            showIndent(outfile, level)
            outfile.write('alpha=XSDataFloat(\n')
            self.alpha.exportLiteral(outfile, level, name_='alpha')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nreal:
            showIndent(outfile, level)
            outfile.write('nreal=XSDataInteger(\n')
            self.nreal.exportLiteral(outfile, level, name_='nreal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.coef:
            showIndent(outfile, level)
            outfile.write('coef=XSDataFloat(\n')
            self.coef.exportLiteral(outfile, level, name_='coef')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rad56:
            showIndent(outfile, level)
            outfile.write('rad56=XSDataFloat(\n')
            self.rad56.exportLiteral(outfile, level, name_='rad56')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.nextjob:
            showIndent(outfile, level)
            outfile.write('nextjob=XSDataBoolean(\n')
            self.nextjob.exportLiteral(outfile, level, name_='nextjob')
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
            nodeName_ == 'printer':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.printer.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forfac':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setForfac(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expert':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setExpert(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input1':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setInput1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input2':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setInput2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip1':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNskip1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip2':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNskip2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iscale':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIscale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plonp':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setPlonp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plores':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setPlores(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'evaerr':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setEvaerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ploerr':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setPloerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lkern':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setLkern(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jobtyp':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setJobtyp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmin':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmax':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmin':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setLzrmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmax':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setLzrmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kernel':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setKernel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deviat':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setDeviat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'idet':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIdet(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFwhm1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFwhm2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setLh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw1':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setLw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setLh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setLw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot1':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSpot1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot2':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSpot2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'alpha':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAlpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nreal':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNreal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coef':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCoef(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rad56':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRad56(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nextjob':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setNextjob(obj_)
# end class XSDataConfigGnom


class XSDataSolutionScatteringSettings(XSData):
    subclass = None
    def __init__(self, rMaxStart=None, rMaxStop=None, rMaxIntervals=None, rMaxAbsTol=None):
        XSData.__init__(self)
        self.rMaxStart = rMaxStart
        self.rMaxStop = rMaxStop
        self.rMaxIntervals = rMaxIntervals
        self.rMaxAbsTol = rMaxAbsTol
    def factory(*args_, **kwargs_):
        if XSDataSolutionScatteringSettings.subclass:
            return XSDataSolutionScatteringSettings.subclass(*args_, **kwargs_)
        else:
            return XSDataSolutionScatteringSettings(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getRMaxStart(self): return self.rMaxStart
    def setRMaxStart(self, rMaxStart): self.rMaxStart = rMaxStart
    def getRMaxStop(self): return self.rMaxStop
    def setRMaxStop(self, rMaxStop): self.rMaxStop = rMaxStop
    def getRMaxIntervals(self): return self.rMaxIntervals
    def setRMaxIntervals(self, rMaxIntervals): self.rMaxIntervals = rMaxIntervals
    def getRMaxAbsTol(self): return self.rMaxAbsTol
    def setRMaxAbsTol(self, rMaxAbsTol): self.rMaxAbsTol = rMaxAbsTol
    def export(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSolutionScatteringSettings')
    def exportChildren(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
        if self.rMaxStart:
            self.rMaxStart.export(outfile, level, name_='rMaxStart')
        if self.rMaxStop:
            self.rMaxStop.export(outfile, level, name_='rMaxStop')
        if self.rMaxIntervals:
            self.rMaxIntervals.export(outfile, level, name_='rMaxIntervals')
        if self.rMaxAbsTol:
            self.rMaxAbsTol.export(outfile, level, name_='rMaxAbsTol')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSolutionScatteringSettings' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSolutionScatteringSettings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSolutionScatteringSettings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSolutionScatteringSettings" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSolutionScatteringSettings'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.rMaxStart:
            showIndent(outfile, level)
            outfile.write('rMaxStart=XSDataFloat(\n')
            self.rMaxStart.exportLiteral(outfile, level, name_='rMaxStart')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rMaxStop:
            showIndent(outfile, level)
            outfile.write('rMaxStop=XSDataFloat(\n')
            self.rMaxStop.exportLiteral(outfile, level, name_='rMaxStop')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rMaxIntervals:
            showIndent(outfile, level)
            outfile.write('rMaxIntervals=XSDataInteger(\n')
            self.rMaxIntervals.exportLiteral(outfile, level, name_='rMaxIntervals')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rMaxAbsTol:
            showIndent(outfile, level)
            outfile.write('rMaxAbsTol=XSDataFloat(\n')
            self.rMaxAbsTol.exportLiteral(outfile, level, name_='rMaxAbsTol')
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
            nodeName_ == 'rMaxStart':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRMaxStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMaxStop':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRMaxStop(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMaxIntervals':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setRMaxIntervals(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMaxAbsTol':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRMaxAbsTol(obj_)
# end class XSDataSolutionScatteringSettings


class XSDataInputDamaver(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, pdbInputFiles=None, symmetry=None, automatic=None):
        XSDataInput.__init__(self, configuration)
        if pdbInputFiles is None:
            self.pdbInputFiles = []
        else:
            self.pdbInputFiles = pdbInputFiles
        self.symmetry = symmetry
        self.automatic = automatic
    def factory(*args_, **kwargs_):
        if XSDataInputDamaver.subclass:
            return XSDataInputDamaver.subclass(*args_, **kwargs_)
        else:
            return XSDataInputDamaver(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPdbInputFiles(self): return self.pdbInputFiles
    def setPdbInputFiles(self, pdbInputFiles): self.pdbInputFiles = pdbInputFiles
    def addPdbInputFiles(self, value): self.pdbInputFiles.append(value)
    def insertPdbInputFiles(self, index, value): self.pdbInputFiles[index] = value
    def getSymmetry(self): return self.symmetry
    def setSymmetry(self, symmetry): self.symmetry = symmetry
    def getAutomatic(self): return self.automatic
    def setAutomatic(self, automatic): self.automatic = automatic
    def export(self, outfile, level, name_='XSDataInputDamaver'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputDamaver'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputDamaver')
    def exportChildren(self, outfile, level, name_='XSDataInputDamaver'):
        for pdbInputFiles_ in self.getPdbInputFiles():
            pdbInputFiles_.export(outfile, level, name_='pdbInputFiles')
        if self.getSymmetry() != None :
            if self.symmetry:
                self.symmetry.export(outfile, level, name_='symmetry')
        if self.getAutomatic() != None :
            if self.automatic:
                self.automatic.export(outfile, level, name_='automatic')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputDamaver' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputDamaver'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('pdbInputFiles=[\n')
        level += 1
        for pdbInputFiles in self.pdbInputFiles:
            showIndent(outfile, level)
            outfile.write('XSDataFile(\n')
            pdbInputFiles.exportLiteral(outfile, level, name_='pdbInputFiles')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.symmetry:
            showIndent(outfile, level)
            outfile.write('symmetry=XSDataString(\n')
            self.symmetry.exportLiteral(outfile, level, name_='symmetry')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.automatic:
            showIndent(outfile, level)
            outfile.write('automatic=XSDataBoolean(\n')
            self.automatic.exportLiteral(outfile, level, name_='automatic')
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
            nodeName_ == 'pdbInputFiles':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.pdbInputFiles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'automatic':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setAutomatic(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputDamaver


class XSDataResultDamaver(XSDataResult):
    subclass = None
    def __init__(self, status=None, meanNSD=None, variationNSD=None, damaverPdbFile=None, damfilterPdbFile=None, damstartPdbFile=None):
        XSDataResult.__init__(self, status)
        self.meanNSD = meanNSD
        self.variationNSD = variationNSD
        self.damaverPdbFile = damaverPdbFile
        self.damfilterPdbFile = damfilterPdbFile
        self.damstartPdbFile = damstartPdbFile
    def factory(*args_, **kwargs_):
        if XSDataResultDamaver.subclass:
            return XSDataResultDamaver.subclass(*args_, **kwargs_)
        else:
            return XSDataResultDamaver(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMeanNSD(self): return self.meanNSD
    def setMeanNSD(self, meanNSD): self.meanNSD = meanNSD
    def getVariationNSD(self): return self.variationNSD
    def setVariationNSD(self, variationNSD): self.variationNSD = variationNSD
    def getDamaverPdbFile(self): return self.damaverPdbFile
    def setDamaverPdbFile(self, damaverPdbFile): self.damaverPdbFile = damaverPdbFile
    def getDamfilterPdbFile(self): return self.damfilterPdbFile
    def setDamfilterPdbFile(self, damfilterPdbFile): self.damfilterPdbFile = damfilterPdbFile
    def getDamstartPdbFile(self): return self.damstartPdbFile
    def setDamstartPdbFile(self, damstartPdbFile): self.damstartPdbFile = damstartPdbFile
    def export(self, outfile, level, name_='XSDataResultDamaver'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultDamaver'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultDamaver')
    def exportChildren(self, outfile, level, name_='XSDataResultDamaver'):
        if self.getMeanNSD() != None :
            if self.meanNSD:
                self.meanNSD.export(outfile, level, name_='meanNSD')
        if self.getVariationNSD() != None :
            if self.variationNSD:
                self.variationNSD.export(outfile, level, name_='variationNSD')
        if self.getDamaverPdbFile() != None :
            if self.damaverPdbFile:
                self.damaverPdbFile.export(outfile, level, name_='damaverPdbFile')
        if self.getDamfilterPdbFile() != None :
            if self.damfilterPdbFile:
                self.damfilterPdbFile.export(outfile, level, name_='damfilterPdbFile')
        if self.getDamstartPdbFile() != None :
            if self.damstartPdbFile:
                self.damstartPdbFile.export(outfile, level, name_='damstartPdbFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultDamaver' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultDamaver'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.meanNSD:
            showIndent(outfile, level)
            outfile.write('meanNSD=XSDataFloat(\n')
            self.meanNSD.exportLiteral(outfile, level, name_='meanNSD')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.variationNSD:
            showIndent(outfile, level)
            outfile.write('variationNSD=XSDataFloat(\n')
            self.variationNSD.exportLiteral(outfile, level, name_='variationNSD')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.damaverPdbFile:
            showIndent(outfile, level)
            outfile.write('damaverPdbFile=XSDataFile(\n')
            self.damaverPdbFile.exportLiteral(outfile, level, name_='damaverPdbFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.damfilterPdbFile:
            showIndent(outfile, level)
            outfile.write('damfilterPdbFile=XSDataFile(\n')
            self.damfilterPdbFile.exportLiteral(outfile, level, name_='damfilterPdbFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.damstartPdbFile:
            showIndent(outfile, level)
            outfile.write('damstartPdbFile=XSDataFile(\n')
            self.damstartPdbFile.exportLiteral(outfile, level, name_='damstartPdbFile')
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
            nodeName_ == 'meanNSD':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMeanNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'variationNSD':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setVariationNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damaverPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setDamaverPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfilterPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setDamfilterPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setDamstartPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultDamaver


class XSDataInputDamfilt(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
        self.inputPdbFile = inputPdbFile
    def factory(*args_, **kwargs_):
        if XSDataInputDamfilt.subclass:
            return XSDataInputDamfilt.subclass(*args_, **kwargs_)
        else:
            return XSDataInputDamfilt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getInputPdbFile(self): return self.inputPdbFile
    def setInputPdbFile(self, inputPdbFile): self.inputPdbFile = inputPdbFile
    def export(self, outfile, level, name_='XSDataInputDamfilt'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputDamfilt'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputDamfilt')
    def exportChildren(self, outfile, level, name_='XSDataInputDamfilt'):
        if self.inputPdbFile:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputDamfilt' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputDamfilt'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.inputPdbFile:
            showIndent(outfile, level)
            outfile.write('inputPdbFile=XSDataFile(\n')
            self.inputPdbFile.exportLiteral(outfile, level, name_='inputPdbFile')
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
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputDamfilt


class XSDataResultDamfilt(XSDataResult):
    subclass = None
    def __init__(self, status=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
        self.outputPdbFile = outputPdbFile
    def factory(*args_, **kwargs_):
        if XSDataResultDamfilt.subclass:
            return XSDataResultDamfilt.subclass(*args_, **kwargs_)
        else:
            return XSDataResultDamfilt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOutputPdbFile(self): return self.outputPdbFile
    def setOutputPdbFile(self, outputPdbFile): self.outputPdbFile = outputPdbFile
    def export(self, outfile, level, name_='XSDataResultDamfilt'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultDamfilt'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultDamfilt')
    def exportChildren(self, outfile, level, name_='XSDataResultDamfilt'):
        if self.getOutputPdbFile() != None :
            if self.outputPdbFile:
                self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultDamfilt' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultDamfilt'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.outputPdbFile:
            showIndent(outfile, level)
            outfile.write('outputPdbFile=XSDataFile(\n')
            self.outputPdbFile.exportLiteral(outfile, level, name_='outputPdbFile')
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
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultDamfilt


class XSDataInputDamstart(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
        self.inputPdbFile = inputPdbFile
    def factory(*args_, **kwargs_):
        if XSDataInputDamstart.subclass:
            return XSDataInputDamstart.subclass(*args_, **kwargs_)
        else:
            return XSDataInputDamstart(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getInputPdbFile(self): return self.inputPdbFile
    def setInputPdbFile(self, inputPdbFile): self.inputPdbFile = inputPdbFile
    def export(self, outfile, level, name_='XSDataInputDamstart'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputDamstart'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputDamstart')
    def exportChildren(self, outfile, level, name_='XSDataInputDamstart'):
        if self.inputPdbFile:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputDamstart' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputDamstart'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.inputPdbFile:
            showIndent(outfile, level)
            outfile.write('inputPdbFile=XSDataFile(\n')
            self.inputPdbFile.exportLiteral(outfile, level, name_='inputPdbFile')
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
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputDamstart


class XSDataResultDamstart(XSDataResult):
    subclass = None
    def __init__(self, status=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
        self.outputPdbFile = outputPdbFile
    def factory(*args_, **kwargs_):
        if XSDataResultDamstart.subclass:
            return XSDataResultDamstart.subclass(*args_, **kwargs_)
        else:
            return XSDataResultDamstart(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOutputPdbFile(self): return self.outputPdbFile
    def setOutputPdbFile(self, outputPdbFile): self.outputPdbFile = outputPdbFile
    def export(self, outfile, level, name_='XSDataResultDamstart'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultDamstart'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultDamstart')
    def exportChildren(self, outfile, level, name_='XSDataResultDamstart'):
        if self.getOutputPdbFile() != None :
            if self.outputPdbFile:
                self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultDamstart' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultDamstart'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.outputPdbFile:
            showIndent(outfile, level)
            outfile.write('outputPdbFile=XSDataFile(\n')
            self.outputPdbFile.exportLiteral(outfile, level, name_='outputPdbFile')
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
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultDamstart


class XSDataInputSupcomb(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, templateFile=None, superimposeFile=None, enantiomorphs=None, backbone=None):
        XSDataInput.__init__(self, configuration)
        self.templateFile = templateFile
        self.superimposeFile = superimposeFile
        self.enantiomorphs = enantiomorphs
        self.backbone = backbone
    def factory(*args_, **kwargs_):
        if XSDataInputSupcomb.subclass:
            return XSDataInputSupcomb.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSupcomb(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getTemplateFile(self): return self.templateFile
    def setTemplateFile(self, templateFile): self.templateFile = templateFile
    def getSuperimposeFile(self): return self.superimposeFile
    def setSuperimposeFile(self, superimposeFile): self.superimposeFile = superimposeFile
    def getEnantiomorphs(self): return self.enantiomorphs
    def setEnantiomorphs(self, enantiomorphs): self.enantiomorphs = enantiomorphs
    def getBackbone(self): return self.backbone
    def setBackbone(self, backbone): self.backbone = backbone
    def export(self, outfile, level, name_='XSDataInputSupcomb'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSupcomb'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSupcomb')
    def exportChildren(self, outfile, level, name_='XSDataInputSupcomb'):
        if self.templateFile:
            self.templateFile.export(outfile, level, name_='templateFile')
        if self.superimposeFile:
            self.superimposeFile.export(outfile, level, name_='superimposeFile')
        if self.getEnantiomorphs() != None :
            if self.enantiomorphs:
                self.enantiomorphs.export(outfile, level, name_='enantiomorphs')
        if self.getBackbone() != None :
            if self.backbone:
                self.backbone.export(outfile, level, name_='backbone')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSupcomb' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSupcomb'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.templateFile:
            showIndent(outfile, level)
            outfile.write('templateFile=XSDataFile(\n')
            self.templateFile.exportLiteral(outfile, level, name_='templateFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.superimposeFile:
            showIndent(outfile, level)
            outfile.write('superimposeFile=XSDataFile(\n')
            self.superimposeFile.exportLiteral(outfile, level, name_='superimposeFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.enantiomorphs:
            showIndent(outfile, level)
            outfile.write('enantiomorphs=XSDataBoolean(\n')
            self.enantiomorphs.exportLiteral(outfile, level, name_='enantiomorphs')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.backbone:
            showIndent(outfile, level)
            outfile.write('backbone=XSDataBoolean(\n')
            self.backbone.exportLiteral(outfile, level, name_='backbone')
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
            nodeName_ == 'templateFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setTemplateFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'superimposeFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSuperimposeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enantiomorphs':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setEnantiomorphs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'backbone':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setBackbone(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSupcomb


class XSDataResultSupcomb(XSDataResult):
    subclass = None
    def __init__(self, status=None, outputFile=None, rot=None, trns=None, NSD=None):
        XSDataResult.__init__(self, status)
        self.outputFile = outputFile
        self.rot = rot
        self.trns = trns
        self.NSD = NSD
    def factory(*args_, **kwargs_):
        if XSDataResultSupcomb.subclass:
            return XSDataResultSupcomb.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSupcomb(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOutputFile(self): return self.outputFile
    def setOutputFile(self, outputFile): self.outputFile = outputFile
    def getRot(self): return self.rot
    def setRot(self, rot): self.rot = rot
    def getTrns(self): return self.trns
    def setTrns(self, trns): self.trns = trns
    def getNSD(self): return self.NSD
    def setNSD(self, NSD): self.NSD = NSD
    def export(self, outfile, level, name_='XSDataResultSupcomb'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSupcomb'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSupcomb')
    def exportChildren(self, outfile, level, name_='XSDataResultSupcomb'):
        if self.outputFile:
            self.outputFile.export(outfile, level, name_='outputFile')
        if self.rot:
            self.rot.export(outfile, level, name_='rot')
        if self.trns:
            self.trns.export(outfile, level, name_='trns')
        if self.NSD:
            self.NSD.export(outfile, level, name_='NSD')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSupcomb' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSupcomb'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.outputFile:
            showIndent(outfile, level)
            outfile.write('outputFile=XSDataFile(\n')
            self.outputFile.exportLiteral(outfile, level, name_='outputFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rot:
            showIndent(outfile, level)
            outfile.write('rot=XSDataRotation(\n')
            self.rot.exportLiteral(outfile, level, name_='rot')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.trns:
            showIndent(outfile, level)
            outfile.write('trns=XSDataVectorDouble(\n')
            self.trns.exportLiteral(outfile, level, name_='trns')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.NSD:
            showIndent(outfile, level)
            outfile.write('NSD=XSDataFloat(\n')
            self.NSD.exportLiteral(outfile, level, name_='NSD')
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
            nodeName_ == 'outputFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rot':
            obj_ = XSDataRotation.factory()
            obj_.build(child_)
            self.setRot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trns':
            obj_ = XSDataVectorDouble.factory()
            obj_.build(child_)
            self.setTrns(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NSD':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNSD(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultSupcomb


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
        elif name == 'status':
            obj = XSDataStatus.factory()
            stackObj = SaxStackElement('status', obj)
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
        elif name == 'message':
            obj = XSDataMessage.factory()
            stackObj = SaxStackElement('message', obj)
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
        elif name == 'experimentalDataQ':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataQ', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataValues':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataValues', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalDataStdDev':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('experimentalDataStdDev', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMax':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rMax', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'angularScale':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('angularScale', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mode':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('mode', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fitQuality':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('fitQuality', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'output':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('output', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'scatteringFitQ':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('scatteringFitQ', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'scatteringFitValues':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('scatteringFitValues', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distributionR':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('distributionR', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distributionPr':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('distributionPr', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distributionErr':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('distributionErr', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'radiusOfCrossSection':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('radiusOfCrossSection', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'radiusOfGyration':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('radiusOfGyration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'expectedParticleShape':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('expectedParticleShape', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'gnomOutputFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('gnomOutputFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'initialDummyAtomModel':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('initialDummyAtomModel', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pdbInputFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('pdbInputFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symmetry':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('symmetry', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fitFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('fitFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'logFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('logFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pdbMoleculeFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('pdbMoleculeFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pdbSolventFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('pdbSolventFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rfactor':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rfactor', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chiSqrt':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('chiSqrt', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chained':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('chained', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'constant':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('constant', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'title':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('title', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMaxSearchSettings':
            obj = XSDataSolutionScatteringSettings.factory()
            stackObj = SaxStackElement('rMaxSearchSettings', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'angularUnits':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('angularUnits', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iNbThreads':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('iNbThreads', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'onlyGnom':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('onlyGnom', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'plotFit':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('plotFit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'corelationFitValues':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('corelationFitValues', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lineProfileFitQuality':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('lineProfileFitQuality', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'meanNSD':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('meanNSD', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'variationNSD':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('variationNSD', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'printer':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('printer', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'forfac':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('forfac', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'expert':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('expert', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'input1':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('input1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'input2':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('input2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nskip1':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('nskip1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nskip2':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('nskip2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iscale':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('iscale', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'plonp':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('plonp', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'plores':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('plores', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'evaerr':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('evaerr', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ploerr':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('ploerr', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lkern':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('lkern', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'jobtyp':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('jobtyp', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmin':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rmin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmax':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rmax', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lzrmin':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('lzrmin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lzrmax':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('lzrmax', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kernel':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('kernel', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'deviat':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('deviat', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'idet':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('idet', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fwhm1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('fwhm1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fwhm2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('fwhm2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ah1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('ah1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lh1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('lh1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aw1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('aw1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lw1':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('lw1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ah2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('ah2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lh2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('lh2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aw2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('aw2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lw2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('lw2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spot1':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('spot1', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spot2':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('spot2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'alpha':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('alpha', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nreal':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('nreal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'coef':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('coef', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rad56':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rad56', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'nextjob':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('nextjob', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMaxStart':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rMaxStart', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMaxStop':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rMaxStop', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMaxIntervals':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('rMaxIntervals', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rMaxAbsTol':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rMaxAbsTol', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pdbInputFiles':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('pdbInputFiles', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'automatic':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('automatic', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'damaverPdbFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('damaverPdbFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'damfilterPdbFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('damfilterPdbFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'damstartPdbFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('damstartPdbFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'inputPdbFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('inputPdbFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'outputPdbFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('outputPdbFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'templateFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('templateFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'superimposeFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('superimposeFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'enantiomorphs':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('enantiomorphs', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'backbone':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('backbone', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'outputFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('outputFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rot':
            obj = XSDataRotation.factory()
            stackObj = SaxStackElement('rot', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'trns':
            obj = XSDataVectorDouble.factory()
            stackObj = SaxStackElement('trns', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NSD':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('NSD', obj)
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
                    except:
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
        elif name == 'status':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'q0':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
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
                    except:
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
                    except:
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
                    except:
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
        elif name == 'message':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMessage(self.stack[-1].obj)
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
                    except:
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
                    except:
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
                    except:
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
        elif name == 'experimentalDataQ':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataQ(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataValues':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataValues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalDataStdDev':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addExperimentalDataStdDev(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMax':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMax(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'angularScale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAngularScale(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mode':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMode(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fitQuality':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFitQuality(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'output':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'scatteringFitQ':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScatteringFitQ(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'scatteringFitValues':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScatteringFitValues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'distributionR':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addDistributionR(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'distributionPr':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addDistributionPr(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'distributionErr':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addDistributionErr(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'radiusOfCrossSection':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRadiusOfCrossSection(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'radiusOfGyration':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRadiusOfGyration(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'expectedParticleShape':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExpectedParticleShape(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'gnomOutputFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGnomOutputFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'initialDummyAtomModel':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInitialDummyAtomModel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pdbInputFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPdbInputFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symmetry':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSymmetry(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fitFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFitFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'logFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pdbMoleculeFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPdbMoleculeFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pdbSolventFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPdbSolventFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rfactor':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRfactor(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chiSqrt':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setChiSqrt(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chained':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setChained(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'constant':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setConstant(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'title':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTitle(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMaxSearchSettings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMaxSearchSettings(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'angularUnits':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAngularUnits(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iNbThreads':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setINbThreads(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'onlyGnom':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOnlyGnom(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'plotFit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPlotFit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'corelationFitValues':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addCorelationFitValues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lineProfileFitQuality':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLineProfileFitQuality(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'meanNSD':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMeanNSD(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'variationNSD':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVariationNSD(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'printer':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addPrinter(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'forfac':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setForfac(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'expert':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExpert(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'input1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInput1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'input2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInput2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nskip1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNskip1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nskip2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNskip2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iscale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIscale(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'plonp':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPlonp(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'plores':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPlores(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'evaerr':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEvaerr(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ploerr':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPloerr(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lkern':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLkern(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'jobtyp':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setJobtyp(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rmin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rmax':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmax(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lzrmin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLzrmin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lzrmax':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLzrmax(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kernel':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKernel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'deviat':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDeviat(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'idet':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIdet(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fwhm1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFwhm1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fwhm2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFwhm2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ah1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAh1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lh1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLh1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aw1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAw1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lw1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLw1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ah2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAh2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lh2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLh2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aw2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAw2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lw2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLw2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spot1':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpot1(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spot2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpot2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'alpha':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAlpha(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nreal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNreal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'coef':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCoef(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rad56':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRad56(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'nextjob':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNextjob(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMaxStart':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMaxStart(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMaxStop':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMaxStop(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMaxIntervals':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMaxIntervals(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rMaxAbsTol':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMaxAbsTol(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pdbInputFiles':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addPdbInputFiles(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'automatic':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAutomatic(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'damaverPdbFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDamaverPdbFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'damfilterPdbFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDamfilterPdbFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'damstartPdbFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDamstartPdbFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'inputPdbFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInputPdbFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'outputPdbFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutputPdbFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'templateFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTemplateFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'superimposeFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSuperimposeFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'enantiomorphs':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEnantiomorphs(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'backbone':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBackbone(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'outputFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutputFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rot':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRot(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'trns':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTrns(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'NSD':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNSD(self.stack[-1].obj)
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
    sys.stdout.write('from XSDataSAS import *\n\n')
    sys.stdout.write('rootObj = XSConfiguration(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSConfiguration")
    sys.stdout.write(')\n')
    return rootObj

class XSDataSAS:
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

