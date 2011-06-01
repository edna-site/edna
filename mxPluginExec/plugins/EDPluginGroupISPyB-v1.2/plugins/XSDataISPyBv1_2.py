#!/usr/bin/env python

#
# Generated Tue Mar 22 15:52:03 2011 by EDGenerateDS.py.
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


class XSDataISPyBDataCollection(XSData):
    subclass = None
    def __init__(self, blSampleId=None, dataCollectionId=None, dataCollectionNumber=None, experimentType=None, imageDirectory=None, imagePrefix=None, sessionId=None):
        XSData.__init__(self)
        self.blSampleId = blSampleId
        self.dataCollectionId = dataCollectionId
        self.dataCollectionNumber = dataCollectionNumber
        self.experimentType = experimentType
        self.imageDirectory = imageDirectory
        self.imagePrefix = imagePrefix
        self.sessionId = sessionId
    def factory(*args_, **kwargs_):
        if XSDataISPyBDataCollection.subclass:
            return XSDataISPyBDataCollection.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBDataCollection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBlSampleId(self): return self.blSampleId
    def setBlSampleId(self, blSampleId): self.blSampleId = blSampleId
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getDataCollectionNumber(self): return self.dataCollectionNumber
    def setDataCollectionNumber(self, dataCollectionNumber): self.dataCollectionNumber = dataCollectionNumber
    def getExperimentType(self): return self.experimentType
    def setExperimentType(self, experimentType): self.experimentType = experimentType
    def getImageDirectory(self): return self.imageDirectory
    def setImageDirectory(self, imageDirectory): self.imageDirectory = imageDirectory
    def getImagePrefix(self): return self.imagePrefix
    def setImagePrefix(self, imagePrefix): self.imagePrefix = imagePrefix
    def getSessionId(self): return self.sessionId
    def setSessionId(self, sessionId): self.sessionId = sessionId
    def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBDataCollection'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBDataCollection')
    def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
        if self.blSampleId:
            self.blSampleId.export(outfile, level, name_='blSampleId')
        if self.dataCollectionId:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self.dataCollectionNumber:
            self.dataCollectionNumber.export(outfile, level, name_='dataCollectionNumber')
        if self.experimentType:
            self.experimentType.export(outfile, level, name_='experimentType')
        if self.imageDirectory:
            self.imageDirectory.export(outfile, level, name_='imageDirectory')
        if self.imagePrefix:
            self.imagePrefix.export(outfile, level, name_='imagePrefix')
        if self.sessionId:
            self.sessionId.export(outfile, level, name_='sessionId')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBDataCollection' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBDataCollection'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.blSampleId:
            showIndent(outfile, level)
            outfile.write('blSampleId=XSDataInteger(\n')
            self.blSampleId.exportLiteral(outfile, level, name_='blSampleId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionNumber:
            showIndent(outfile, level)
            outfile.write('dataCollectionNumber=XSDataInteger(\n')
            self.dataCollectionNumber.exportLiteral(outfile, level, name_='dataCollectionNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentType:
            showIndent(outfile, level)
            outfile.write('experimentType=XSDataString(\n')
            self.experimentType.exportLiteral(outfile, level, name_='experimentType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageDirectory:
            showIndent(outfile, level)
            outfile.write('imageDirectory=XSDataString(\n')
            self.imageDirectory.exportLiteral(outfile, level, name_='imageDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imagePrefix:
            showIndent(outfile, level)
            outfile.write('imagePrefix=XSDataString(\n')
            self.imagePrefix.exportLiteral(outfile, level, name_='imagePrefix')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sessionId:
            showIndent(outfile, level)
            outfile.write('sessionId=XSDataInteger(\n')
            self.sessionId.exportLiteral(outfile, level, name_='sessionId')
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
            nodeName_ == 'blSampleId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setBlSampleId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setExperimentType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageDirectory':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setImageDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePrefix':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setImagePrefix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSessionId(obj_)
# end class XSDataISPyBDataCollection


class XSDataISPyBImage(XSData):
    subclass = None
    def __init__(self, comments=None, cumulativeIntensity=None, fileLocation=None, fileName=None, imageId=None, imageNumber=None, jpegFileFullPath=None, jpegThumbnailFileFullPath=None, machineMessage=None, measuredIntensity=None, synchrotronCurrent=None, temperature=None):
        XSData.__init__(self)
        self.comments = comments
        self.cumulativeIntensity = cumulativeIntensity
        self.fileLocation = fileLocation
        self.fileName = fileName
        self.imageId = imageId
        self.imageNumber = imageNumber
        self.jpegFileFullPath = jpegFileFullPath
        self.jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
        self.machineMessage = machineMessage
        self.measuredIntensity = measuredIntensity
        self.synchrotronCurrent = synchrotronCurrent
        self.temperature = temperature
    def factory(*args_, **kwargs_):
        if XSDataISPyBImage.subclass:
            return XSDataISPyBImage.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBImage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getComments(self): return self.comments
    def setComments(self, comments): self.comments = comments
    def getCumulativeIntensity(self): return self.cumulativeIntensity
    def setCumulativeIntensity(self, cumulativeIntensity): self.cumulativeIntensity = cumulativeIntensity
    def getFileLocation(self): return self.fileLocation
    def setFileLocation(self, fileLocation): self.fileLocation = fileLocation
    def getFileName(self): return self.fileName
    def setFileName(self, fileName): self.fileName = fileName
    def getImageId(self): return self.imageId
    def setImageId(self, imageId): self.imageId = imageId
    def getImageNumber(self): return self.imageNumber
    def setImageNumber(self, imageNumber): self.imageNumber = imageNumber
    def getJpegFileFullPath(self): return self.jpegFileFullPath
    def setJpegFileFullPath(self, jpegFileFullPath): self.jpegFileFullPath = jpegFileFullPath
    def getJpegThumbnailFileFullPath(self): return self.jpegThumbnailFileFullPath
    def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath): self.jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
    def getMachineMessage(self): return self.machineMessage
    def setMachineMessage(self, machineMessage): self.machineMessage = machineMessage
    def getMeasuredIntensity(self): return self.measuredIntensity
    def setMeasuredIntensity(self, measuredIntensity): self.measuredIntensity = measuredIntensity
    def getSynchrotronCurrent(self): return self.synchrotronCurrent
    def setSynchrotronCurrent(self, synchrotronCurrent): self.synchrotronCurrent = synchrotronCurrent
    def getTemperature(self): return self.temperature
    def setTemperature(self, temperature): self.temperature = temperature
    def export(self, outfile, level, name_='XSDataISPyBImage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBImage'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBImage')
    def exportChildren(self, outfile, level, name_='XSDataISPyBImage'):
        if self.comments:
            self.comments.export(outfile, level, name_='comments')
        if self.cumulativeIntensity:
            self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
        if self.fileLocation:
            self.fileLocation.export(outfile, level, name_='fileLocation')
        if self.fileName:
            self.fileName.export(outfile, level, name_='fileName')
        if self.imageId:
            self.imageId.export(outfile, level, name_='imageId')
        if self.imageNumber:
            self.imageNumber.export(outfile, level, name_='imageNumber')
        if self.jpegFileFullPath:
            self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
        if self.jpegThumbnailFileFullPath:
            self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
        if self.machineMessage:
            self.machineMessage.export(outfile, level, name_='machineMessage')
        if self.measuredIntensity:
            self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
        if self.synchrotronCurrent:
            self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
        if self.temperature:
            self.temperature.export(outfile, level, name_='temperature')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBImage' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBImage'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.comments:
            showIndent(outfile, level)
            outfile.write('comments=XSDataString(\n')
            self.comments.exportLiteral(outfile, level, name_='comments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cumulativeIntensity:
            showIndent(outfile, level)
            outfile.write('cumulativeIntensity=XSDataDouble(\n')
            self.cumulativeIntensity.exportLiteral(outfile, level, name_='cumulativeIntensity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fileLocation:
            showIndent(outfile, level)
            outfile.write('fileLocation=XSDataString(\n')
            self.fileLocation.exportLiteral(outfile, level, name_='fileLocation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fileName:
            showIndent(outfile, level)
            outfile.write('fileName=XSDataString(\n')
            self.fileName.exportLiteral(outfile, level, name_='fileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageId:
            showIndent(outfile, level)
            outfile.write('imageId=XSDataInteger(\n')
            self.imageId.exportLiteral(outfile, level, name_='imageId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageNumber:
            showIndent(outfile, level)
            outfile.write('imageNumber=XSDataInteger(\n')
            self.imageNumber.exportLiteral(outfile, level, name_='imageNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.jpegFileFullPath:
            showIndent(outfile, level)
            outfile.write('jpegFileFullPath=XSDataString(\n')
            self.jpegFileFullPath.exportLiteral(outfile, level, name_='jpegFileFullPath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.jpegThumbnailFileFullPath:
            showIndent(outfile, level)
            outfile.write('jpegThumbnailFileFullPath=XSDataString(\n')
            self.jpegThumbnailFileFullPath.exportLiteral(outfile, level, name_='jpegThumbnailFileFullPath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.machineMessage:
            showIndent(outfile, level)
            outfile.write('machineMessage=XSDataString(\n')
            self.machineMessage.exportLiteral(outfile, level, name_='machineMessage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.measuredIntensity:
            showIndent(outfile, level)
            outfile.write('measuredIntensity=XSDataDouble(\n')
            self.measuredIntensity.exportLiteral(outfile, level, name_='measuredIntensity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.synchrotronCurrent:
            showIndent(outfile, level)
            outfile.write('synchrotronCurrent=XSDataDouble(\n')
            self.synchrotronCurrent.exportLiteral(outfile, level, name_='synchrotronCurrent')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.temperature:
            showIndent(outfile, level)
            outfile.write('temperature=XSDataDouble(\n')
            self.temperature.exportLiteral(outfile, level, name_='temperature')
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
            nodeName_ == 'comments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cumulativeIntensity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setCumulativeIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileLocation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileLocation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setImageId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jpegFileFullPath':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setJpegFileFullPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jpegThumbnailFileFullPath':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setJpegThumbnailFileFullPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineMessage':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMachineMessage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'measuredIntensity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMeasuredIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'synchrotronCurrent':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setSynchrotronCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'temperature':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setTemperature(obj_)
# end class XSDataISPyBImage


class XSDataISPyBScreening(XSData):
    subclass = None
    def __init__(self, comments=None, dataCollectionId=None, programVersion=None, screeningId=None, shortComments=None, timeStamp=None):
        XSData.__init__(self)
        self.comments = comments
        self.dataCollectionId = dataCollectionId
        self.programVersion = programVersion
        self.screeningId = screeningId
        self.shortComments = shortComments
        self.timeStamp = timeStamp
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreening.subclass:
            return XSDataISPyBScreening.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreening(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getComments(self): return self.comments
    def setComments(self, comments): self.comments = comments
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getProgramVersion(self): return self.programVersion
    def setProgramVersion(self, programVersion): self.programVersion = programVersion
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getShortComments(self): return self.shortComments
    def setShortComments(self, shortComments): self.shortComments = shortComments
    def getTimeStamp(self): return self.timeStamp
    def setTimeStamp(self, timeStamp): self.timeStamp = timeStamp
    def export(self, outfile, level, name_='XSDataISPyBScreening'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreening'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreening')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreening'):
        if self.comments:
            self.comments.export(outfile, level, name_='comments')
        if self.dataCollectionId:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self.programVersion:
            self.programVersion.export(outfile, level, name_='programVersion')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.shortComments:
            self.shortComments.export(outfile, level, name_='shortComments')
        if self.timeStamp:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreening' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreening.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreening.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreening" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreening'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.comments:
            showIndent(outfile, level)
            outfile.write('comments=XSDataString(\n')
            self.comments.exportLiteral(outfile, level, name_='comments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.programVersion:
            showIndent(outfile, level)
            outfile.write('programVersion=XSDataString(\n')
            self.programVersion.exportLiteral(outfile, level, name_='programVersion')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shortComments:
            showIndent(outfile, level)
            outfile.write('shortComments=XSDataString(\n')
            self.shortComments.exportLiteral(outfile, level, name_='shortComments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeStamp:
            showIndent(outfile, level)
            outfile.write('timeStamp=XSDataString(\n')
            self.timeStamp.exportLiteral(outfile, level, name_='timeStamp')
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
            nodeName_ == 'comments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'programVersion':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setProgramVersion(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shortComments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setShortComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTimeStamp(obj_)
# end class XSDataISPyBScreening


class XSDataISPyBScreeningFile(XSData):
    subclass = None
    def __init__(self, description=None, fileName=None, filePath=None, fileType=None, screeningFileId=None, screeningId=None, timeStamp=None):
        XSData.__init__(self)
        self.description = description
        self.fileName = fileName
        self.filePath = filePath
        self.fileType = fileType
        self.screeningFileId = screeningFileId
        self.screeningId = screeningId
        self.timeStamp = timeStamp
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningFile.subclass:
            return XSDataISPyBScreeningFile.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDescription(self): return self.description
    def setDescription(self, description): self.description = description
    def getFileName(self): return self.fileName
    def setFileName(self, fileName): self.fileName = fileName
    def getFilePath(self): return self.filePath
    def setFilePath(self, filePath): self.filePath = filePath
    def getFileType(self): return self.fileType
    def setFileType(self, fileType): self.fileType = fileType
    def getScreeningFileId(self): return self.screeningFileId
    def setScreeningFileId(self, screeningFileId): self.screeningFileId = screeningFileId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getTimeStamp(self): return self.timeStamp
    def setTimeStamp(self, timeStamp): self.timeStamp = timeStamp
    def export(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningFile')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        if self.description:
            self.description.export(outfile, level, name_='description')
        if self.fileName:
            self.fileName.export(outfile, level, name_='fileName')
        if self.filePath:
            self.filePath.export(outfile, level, name_='filePath')
        if self.fileType:
            self.fileType.export(outfile, level, name_='fileType')
        if self.screeningFileId:
            self.screeningFileId.export(outfile, level, name_='screeningFileId')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.timeStamp:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningFile' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningFile'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.description:
            showIndent(outfile, level)
            outfile.write('description=XSDataString(\n')
            self.description.exportLiteral(outfile, level, name_='description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fileName:
            showIndent(outfile, level)
            outfile.write('fileName=XSDataString(\n')
            self.fileName.exportLiteral(outfile, level, name_='fileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.filePath:
            showIndent(outfile, level)
            outfile.write('filePath=XSDataString(\n')
            self.filePath.exportLiteral(outfile, level, name_='filePath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fileType:
            showIndent(outfile, level)
            outfile.write('fileType=XSDataString(\n')
            self.fileType.exportLiteral(outfile, level, name_='fileType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningFileId:
            showIndent(outfile, level)
            outfile.write('screeningFileId=XSDataInteger(\n')
            self.screeningFileId.exportLiteral(outfile, level, name_='screeningFileId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeStamp:
            showIndent(outfile, level)
            outfile.write('timeStamp=XSDataString(\n')
            self.timeStamp.exportLiteral(outfile, level, name_='timeStamp')
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
            nodeName_ == 'description':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDescription(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePath':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningFileId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningFileId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTimeStamp(obj_)
# end class XSDataISPyBScreeningFile


class XSDataISPyBScreeningInput(XSData):
    subclass = None
    def __init__(self, beamX=None, beamY=None, maximumFractionRejected=None, minimumFractionIndexed=None, minimumSignalToNoise=None, rmsErrorLimits=None, screeningId=None, screeningInputId=None):
        XSData.__init__(self)
        self.beamX = beamX
        self.beamY = beamY
        self.maximumFractionRejected = maximumFractionRejected
        self.minimumFractionIndexed = minimumFractionIndexed
        self.minimumSignalToNoise = minimumSignalToNoise
        self.rmsErrorLimits = rmsErrorLimits
        self.screeningId = screeningId
        self.screeningInputId = screeningInputId
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningInput.subclass:
            return XSDataISPyBScreeningInput.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBeamX(self): return self.beamX
    def setBeamX(self, beamX): self.beamX = beamX
    def getBeamY(self): return self.beamY
    def setBeamY(self, beamY): self.beamY = beamY
    def getMaximumFractionRejected(self): return self.maximumFractionRejected
    def setMaximumFractionRejected(self, maximumFractionRejected): self.maximumFractionRejected = maximumFractionRejected
    def getMinimumFractionIndexed(self): return self.minimumFractionIndexed
    def setMinimumFractionIndexed(self, minimumFractionIndexed): self.minimumFractionIndexed = minimumFractionIndexed
    def getMinimumSignalToNoise(self): return self.minimumSignalToNoise
    def setMinimumSignalToNoise(self, minimumSignalToNoise): self.minimumSignalToNoise = minimumSignalToNoise
    def getRmsErrorLimits(self): return self.rmsErrorLimits
    def setRmsErrorLimits(self, rmsErrorLimits): self.rmsErrorLimits = rmsErrorLimits
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getScreeningInputId(self): return self.screeningInputId
    def setScreeningInputId(self, screeningInputId): self.screeningInputId = screeningInputId
    def export(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInput')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        if self.beamX:
            self.beamX.export(outfile, level, name_='beamX')
        if self.beamY:
            self.beamY.export(outfile, level, name_='beamY')
        if self.maximumFractionRejected:
            self.maximumFractionRejected.export(outfile, level, name_='maximumFractionRejected')
        if self.minimumFractionIndexed:
            self.minimumFractionIndexed.export(outfile, level, name_='minimumFractionIndexed')
        if self.minimumSignalToNoise:
            self.minimumSignalToNoise.export(outfile, level, name_='minimumSignalToNoise')
        if self.rmsErrorLimits:
            self.rmsErrorLimits.export(outfile, level, name_='rmsErrorLimits')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.screeningInputId:
            self.screeningInputId.export(outfile, level, name_='screeningInputId')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.beamX:
            showIndent(outfile, level)
            outfile.write('beamX=XSDataDouble(\n')
            self.beamX.exportLiteral(outfile, level, name_='beamX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamY:
            showIndent(outfile, level)
            outfile.write('beamY=XSDataDouble(\n')
            self.beamY.exportLiteral(outfile, level, name_='beamY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.maximumFractionRejected:
            showIndent(outfile, level)
            outfile.write('maximumFractionRejected=XSDataDouble(\n')
            self.maximumFractionRejected.exportLiteral(outfile, level, name_='maximumFractionRejected')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minimumFractionIndexed:
            showIndent(outfile, level)
            outfile.write('minimumFractionIndexed=XSDataDouble(\n')
            self.minimumFractionIndexed.exportLiteral(outfile, level, name_='minimumFractionIndexed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minimumSignalToNoise:
            showIndent(outfile, level)
            outfile.write('minimumSignalToNoise=XSDataDouble(\n')
            self.minimumSignalToNoise.exportLiteral(outfile, level, name_='minimumSignalToNoise')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmsErrorLimits:
            showIndent(outfile, level)
            outfile.write('rmsErrorLimits=XSDataDouble(\n')
            self.rmsErrorLimits.exportLiteral(outfile, level, name_='rmsErrorLimits')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningInputId:
            showIndent(outfile, level)
            outfile.write('screeningInputId=XSDataInteger(\n')
            self.screeningInputId.exportLiteral(outfile, level, name_='screeningInputId')
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
            nodeName_ == 'beamX':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBeamX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamY':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBeamY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maximumFractionRejected':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMaximumFractionRejected(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimumFractionIndexed':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMinimumFractionIndexed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimumSignalToNoise':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMinimumSignalToNoise(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmsErrorLimits':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRmsErrorLimits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningInputId(obj_)
# end class XSDataISPyBScreeningInput


class XSDataISPyBScreeningInputContainer(XSData):
    subclass = None
    def __init__(self, screeningInput=None):
        XSData.__init__(self)
        self.screeningInput = screeningInput
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningInputContainer.subclass:
            return XSDataISPyBScreeningInputContainer.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningInputContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningInput(self): return self.screeningInput
    def setScreeningInput(self, screeningInput): self.screeningInput = screeningInput
    def export(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInputContainer')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
        if self.screeningInput:
            self.screeningInput.export(outfile, level, name_='screeningInput')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningInputContainer' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningInputContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningInputContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningInputContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningInputContainer'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.screeningInput:
            showIndent(outfile, level)
            outfile.write('screeningInput=XSDataISPyBScreeningInput(\n')
            self.screeningInput.exportLiteral(outfile, level, name_='screeningInput')
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
            nodeName_ == 'screeningInput':
            obj_ = XSDataISPyBScreeningInput.factory()
            obj_.build(child_)
            self.setScreeningInput(obj_)
# end class XSDataISPyBScreeningInputContainer


class XSDataISPyBScreeningOutput(XSData):
    subclass = None
    def __init__(self, beamShiftX=None, beamShiftY=None, diffractionRings=None, iOverSigma=None, mosaicity=None, mosaicityEstimated=None, numSpotsFound=None, numSpotsRejected=None, numSpotsUsed=None, rejectedReflections=None, resolutionObtained=None, screeningId=None, screeningOutputId=None, screeningSuccess=None, spotDeviationR=None, spotDeviationTheta=None, statusDescription=None):
        XSData.__init__(self)
        self.beamShiftX = beamShiftX
        self.beamShiftY = beamShiftY
        self.diffractionRings = diffractionRings
        self.iOverSigma = iOverSigma
        self.mosaicity = mosaicity
        self.mosaicityEstimated = mosaicityEstimated
        self.numSpotsFound = numSpotsFound
        self.numSpotsRejected = numSpotsRejected
        self.numSpotsUsed = numSpotsUsed
        self.rejectedReflections = rejectedReflections
        self.resolutionObtained = resolutionObtained
        self.screeningId = screeningId
        self.screeningOutputId = screeningOutputId
        self.screeningSuccess = screeningSuccess
        self.spotDeviationR = spotDeviationR
        self.spotDeviationTheta = spotDeviationTheta
        self.statusDescription = statusDescription
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningOutput.subclass:
            return XSDataISPyBScreeningOutput.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningOutput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBeamShiftX(self): return self.beamShiftX
    def setBeamShiftX(self, beamShiftX): self.beamShiftX = beamShiftX
    def getBeamShiftY(self): return self.beamShiftY
    def setBeamShiftY(self, beamShiftY): self.beamShiftY = beamShiftY
    def getDiffractionRings(self): return self.diffractionRings
    def setDiffractionRings(self, diffractionRings): self.diffractionRings = diffractionRings
    def getIOverSigma(self): return self.iOverSigma
    def setIOverSigma(self, iOverSigma): self.iOverSigma = iOverSigma
    def getMosaicity(self): return self.mosaicity
    def setMosaicity(self, mosaicity): self.mosaicity = mosaicity
    def getMosaicityEstimated(self): return self.mosaicityEstimated
    def setMosaicityEstimated(self, mosaicityEstimated): self.mosaicityEstimated = mosaicityEstimated
    def getNumSpotsFound(self): return self.numSpotsFound
    def setNumSpotsFound(self, numSpotsFound): self.numSpotsFound = numSpotsFound
    def getNumSpotsRejected(self): return self.numSpotsRejected
    def setNumSpotsRejected(self, numSpotsRejected): self.numSpotsRejected = numSpotsRejected
    def getNumSpotsUsed(self): return self.numSpotsUsed
    def setNumSpotsUsed(self, numSpotsUsed): self.numSpotsUsed = numSpotsUsed
    def getRejectedReflections(self): return self.rejectedReflections
    def setRejectedReflections(self, rejectedReflections): self.rejectedReflections = rejectedReflections
    def getResolutionObtained(self): return self.resolutionObtained
    def setResolutionObtained(self, resolutionObtained): self.resolutionObtained = resolutionObtained
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningSuccess(self): return self.screeningSuccess
    def setScreeningSuccess(self, screeningSuccess): self.screeningSuccess = screeningSuccess
    def getSpotDeviationR(self): return self.spotDeviationR
    def setSpotDeviationR(self, spotDeviationR): self.spotDeviationR = spotDeviationR
    def getSpotDeviationTheta(self): return self.spotDeviationTheta
    def setSpotDeviationTheta(self, spotDeviationTheta): self.spotDeviationTheta = spotDeviationTheta
    def getStatusDescription(self): return self.statusDescription
    def setStatusDescription(self, statusDescription): self.statusDescription = statusDescription
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutput')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        if self.beamShiftX:
            self.beamShiftX.export(outfile, level, name_='beamShiftX')
        if self.beamShiftY:
            self.beamShiftY.export(outfile, level, name_='beamShiftY')
        if self.diffractionRings:
            self.diffractionRings.export(outfile, level, name_='diffractionRings')
        if self.iOverSigma:
            self.iOverSigma.export(outfile, level, name_='iOverSigma')
        if self.mosaicity:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self.mosaicityEstimated:
            self.mosaicityEstimated.export(outfile, level, name_='mosaicityEstimated')
        if self.numSpotsFound:
            self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
        if self.numSpotsRejected:
            self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
        if self.numSpotsUsed:
            self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
        if self.rejectedReflections:
            self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
        if self.resolutionObtained:
            self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.screeningSuccess:
            self.screeningSuccess.export(outfile, level, name_='screeningSuccess')
        if self.spotDeviationR:
            self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
        if self.spotDeviationTheta:
            self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
        if self.statusDescription:
            self.statusDescription.export(outfile, level, name_='statusDescription')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.beamShiftX:
            showIndent(outfile, level)
            outfile.write('beamShiftX=XSDataDouble(\n')
            self.beamShiftX.exportLiteral(outfile, level, name_='beamShiftX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamShiftY:
            showIndent(outfile, level)
            outfile.write('beamShiftY=XSDataDouble(\n')
            self.beamShiftY.exportLiteral(outfile, level, name_='beamShiftY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.diffractionRings:
            showIndent(outfile, level)
            outfile.write('diffractionRings=XSDataBoolean(\n')
            self.diffractionRings.exportLiteral(outfile, level, name_='diffractionRings')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iOverSigma:
            showIndent(outfile, level)
            outfile.write('iOverSigma=XSDataDouble(\n')
            self.iOverSigma.exportLiteral(outfile, level, name_='iOverSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mosaicity:
            showIndent(outfile, level)
            outfile.write('mosaicity=XSDataDouble(\n')
            self.mosaicity.exportLiteral(outfile, level, name_='mosaicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mosaicityEstimated:
            showIndent(outfile, level)
            outfile.write('mosaicityEstimated=XSDataBoolean(\n')
            self.mosaicityEstimated.exportLiteral(outfile, level, name_='mosaicityEstimated')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsFound:
            showIndent(outfile, level)
            outfile.write('numSpotsFound=XSDataInteger(\n')
            self.numSpotsFound.exportLiteral(outfile, level, name_='numSpotsFound')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsRejected:
            showIndent(outfile, level)
            outfile.write('numSpotsRejected=XSDataInteger(\n')
            self.numSpotsRejected.exportLiteral(outfile, level, name_='numSpotsRejected')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsUsed:
            showIndent(outfile, level)
            outfile.write('numSpotsUsed=XSDataInteger(\n')
            self.numSpotsUsed.exportLiteral(outfile, level, name_='numSpotsUsed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rejectedReflections:
            showIndent(outfile, level)
            outfile.write('rejectedReflections=XSDataInteger(\n')
            self.rejectedReflections.exportLiteral(outfile, level, name_='rejectedReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolutionObtained:
            showIndent(outfile, level)
            outfile.write('resolutionObtained=XSDataDouble(\n')
            self.resolutionObtained.exportLiteral(outfile, level, name_='resolutionObtained')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningSuccess:
            showIndent(outfile, level)
            outfile.write('screeningSuccess=XSDataBoolean(\n')
            self.screeningSuccess.exportLiteral(outfile, level, name_='screeningSuccess')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationR:
            showIndent(outfile, level)
            outfile.write('spotDeviationR=XSDataDouble(\n')
            self.spotDeviationR.exportLiteral(outfile, level, name_='spotDeviationR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationTheta:
            showIndent(outfile, level)
            outfile.write('spotDeviationTheta=XSDataDouble(\n')
            self.spotDeviationTheta.exportLiteral(outfile, level, name_='spotDeviationTheta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statusDescription:
            showIndent(outfile, level)
            outfile.write('statusDescription=XSDataString(\n')
            self.statusDescription.exportLiteral(outfile, level, name_='statusDescription')
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
            nodeName_ == 'beamShiftX':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBeamShiftX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShiftY':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBeamShiftY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionRings':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setDiffractionRings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iOverSigma':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityEstimated':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setMosaicityEstimated(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsFound':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsFound(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsRejected':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsRejected(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsUsed':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rejectedReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setRejectedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionObtained':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setResolutionObtained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningSuccess':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setScreeningSuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationR':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setSpotDeviationR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationTheta':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setSpotDeviationTheta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statusDescription':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setStatusDescription(obj_)
# end class XSDataISPyBScreeningOutput


class XSDataISPyBScreeningOutputContainer(XSData):
    subclass = None
    def __init__(self, screeningOutput=None, screeningOutputLattice=None, screeningStrategyContainer=None):
        XSData.__init__(self)
        self.screeningOutput = screeningOutput
        if screeningOutputLattice is None:
            self.screeningOutputLattice = []
        else:
            self.screeningOutputLattice = screeningOutputLattice
        if screeningStrategyContainer is None:
            self.screeningStrategyContainer = []
        else:
            self.screeningStrategyContainer = screeningStrategyContainer
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningOutputContainer.subclass:
            return XSDataISPyBScreeningOutputContainer.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningOutputContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningOutput(self): return self.screeningOutput
    def setScreeningOutput(self, screeningOutput): self.screeningOutput = screeningOutput
    def getScreeningOutputLattice(self): return self.screeningOutputLattice
    def setScreeningOutputLattice(self, screeningOutputLattice): self.screeningOutputLattice = screeningOutputLattice
    def addScreeningOutputLattice(self, value): self.screeningOutputLattice.append(value)
    def insertScreeningOutputLattice(self, index, value): self.screeningOutputLattice[index] = value
    def getScreeningStrategyContainer(self): return self.screeningStrategyContainer
    def setScreeningStrategyContainer(self, screeningStrategyContainer): self.screeningStrategyContainer = screeningStrategyContainer
    def addScreeningStrategyContainer(self, value): self.screeningStrategyContainer.append(value)
    def insertScreeningStrategyContainer(self, index, value): self.screeningStrategyContainer[index] = value
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        if self.screeningOutput:
            self.screeningOutput.export(outfile, level, name_='screeningOutput')
        for screeningOutputLattice_ in self.getScreeningOutputLattice():
            screeningOutputLattice_.export(outfile, level, name_='screeningOutputLattice')
        for screeningStrategyContainer_ in self.getScreeningStrategyContainer():
            screeningStrategyContainer_.export(outfile, level, name_='screeningStrategyContainer')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutputContainer' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningOutputContainer'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.screeningOutput:
            showIndent(outfile, level)
            outfile.write('screeningOutput=XSDataISPyBScreeningOutput(\n')
            self.screeningOutput.exportLiteral(outfile, level, name_='screeningOutput')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningOutputLattice=[\n')
        level += 1
        for screeningOutputLattice in self.screeningOutputLattice:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningOutputLattice(\n')
            screeningOutputLattice.exportLiteral(outfile, level, name_='screeningOutputLattice')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningStrategyContainer=[\n')
        level += 1
        for screeningStrategyContainer in self.screeningStrategyContainer:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningStrategyContainer(\n')
            screeningStrategyContainer.exportLiteral(outfile, level, name_='screeningStrategyContainer')
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
            nodeName_ == 'screeningOutput':
            obj_ = XSDataISPyBScreeningOutput.factory()
            obj_.build(child_)
            self.setScreeningOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLattice':
            obj_ = XSDataISPyBScreeningOutputLattice.factory()
            obj_.build(child_)
            self.screeningOutputLattice.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyContainer':
            obj_ = XSDataISPyBScreeningStrategyContainer.factory()
            obj_.build(child_)
            self.screeningStrategyContainer.append(obj_)
# end class XSDataISPyBScreeningOutputContainer


class XSDataISPyBScreeningOutputLattice(XSData):
    subclass = None
    def __init__(self, bravaisLattice=None, pointGroup=None, rawOrientationMatrix_a_x=None, rawOrientationMatrix_a_y=None, rawOrientationMatrix_a_z=None, rawOrientationMatrix_b_x=None, rawOrientationMatrix_b_y=None, rawOrientationMatrix_b_z=None, rawOrientationMatrix_c_x=None, rawOrientationMatrix_c_y=None, rawOrientationMatrix_c_z=None, screeningOutputId=None, screeningOutputLatticeId=None, spaceGroup=None, timeStamp=None, unitCell_a=None, unitCell_alpha=None, unitCell_b=None, unitCell_beta=None, unitCell_c=None, unitCell_gamma=None):
        XSData.__init__(self)
        self.bravaisLattice = bravaisLattice
        self.pointGroup = pointGroup
        self.rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
        self.rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
        self.rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
        self.rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
        self.rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
        self.rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
        self.rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
        self.rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
        self.rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
        self.screeningOutputId = screeningOutputId
        self.screeningOutputLatticeId = screeningOutputLatticeId
        self.spaceGroup = spaceGroup
        self.timeStamp = timeStamp
        self.unitCell_a = unitCell_a
        self.unitCell_alpha = unitCell_alpha
        self.unitCell_b = unitCell_b
        self.unitCell_beta = unitCell_beta
        self.unitCell_c = unitCell_c
        self.unitCell_gamma = unitCell_gamma
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningOutputLattice.subclass:
            return XSDataISPyBScreeningOutputLattice.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningOutputLattice(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBravaisLattice(self): return self.bravaisLattice
    def setBravaisLattice(self, bravaisLattice): self.bravaisLattice = bravaisLattice
    def getPointGroup(self): return self.pointGroup
    def setPointGroup(self, pointGroup): self.pointGroup = pointGroup
    def getRawOrientationMatrix_a_x(self): return self.rawOrientationMatrix_a_x
    def setRawOrientationMatrix_a_x(self, rawOrientationMatrix_a_x): self.rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
    def getRawOrientationMatrix_a_y(self): return self.rawOrientationMatrix_a_y
    def setRawOrientationMatrix_a_y(self, rawOrientationMatrix_a_y): self.rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
    def getRawOrientationMatrix_a_z(self): return self.rawOrientationMatrix_a_z
    def setRawOrientationMatrix_a_z(self, rawOrientationMatrix_a_z): self.rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
    def getRawOrientationMatrix_b_x(self): return self.rawOrientationMatrix_b_x
    def setRawOrientationMatrix_b_x(self, rawOrientationMatrix_b_x): self.rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
    def getRawOrientationMatrix_b_y(self): return self.rawOrientationMatrix_b_y
    def setRawOrientationMatrix_b_y(self, rawOrientationMatrix_b_y): self.rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
    def getRawOrientationMatrix_b_z(self): return self.rawOrientationMatrix_b_z
    def setRawOrientationMatrix_b_z(self, rawOrientationMatrix_b_z): self.rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
    def getRawOrientationMatrix_c_x(self): return self.rawOrientationMatrix_c_x
    def setRawOrientationMatrix_c_x(self, rawOrientationMatrix_c_x): self.rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
    def getRawOrientationMatrix_c_y(self): return self.rawOrientationMatrix_c_y
    def setRawOrientationMatrix_c_y(self, rawOrientationMatrix_c_y): self.rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
    def getRawOrientationMatrix_c_z(self): return self.rawOrientationMatrix_c_z
    def setRawOrientationMatrix_c_z(self, rawOrientationMatrix_c_z): self.rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningOutputLatticeId(self): return self.screeningOutputLatticeId
    def setScreeningOutputLatticeId(self, screeningOutputLatticeId): self.screeningOutputLatticeId = screeningOutputLatticeId
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getTimeStamp(self): return self.timeStamp
    def setTimeStamp(self, timeStamp): self.timeStamp = timeStamp
    def getUnitCell_a(self): return self.unitCell_a
    def setUnitCell_a(self, unitCell_a): self.unitCell_a = unitCell_a
    def getUnitCell_alpha(self): return self.unitCell_alpha
    def setUnitCell_alpha(self, unitCell_alpha): self.unitCell_alpha = unitCell_alpha
    def getUnitCell_b(self): return self.unitCell_b
    def setUnitCell_b(self, unitCell_b): self.unitCell_b = unitCell_b
    def getUnitCell_beta(self): return self.unitCell_beta
    def setUnitCell_beta(self, unitCell_beta): self.unitCell_beta = unitCell_beta
    def getUnitCell_c(self): return self.unitCell_c
    def setUnitCell_c(self, unitCell_c): self.unitCell_c = unitCell_c
    def getUnitCell_gamma(self): return self.unitCell_gamma
    def setUnitCell_gamma(self, unitCell_gamma): self.unitCell_gamma = unitCell_gamma
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        if self.bravaisLattice:
            self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
        if self.pointGroup:
            self.pointGroup.export(outfile, level, name_='pointGroup')
        if self.rawOrientationMatrix_a_x:
            self.rawOrientationMatrix_a_x.export(outfile, level, name_='rawOrientationMatrix_a_x')
        if self.rawOrientationMatrix_a_y:
            self.rawOrientationMatrix_a_y.export(outfile, level, name_='rawOrientationMatrix_a_y')
        if self.rawOrientationMatrix_a_z:
            self.rawOrientationMatrix_a_z.export(outfile, level, name_='rawOrientationMatrix_a_z')
        if self.rawOrientationMatrix_b_x:
            self.rawOrientationMatrix_b_x.export(outfile, level, name_='rawOrientationMatrix_b_x')
        if self.rawOrientationMatrix_b_y:
            self.rawOrientationMatrix_b_y.export(outfile, level, name_='rawOrientationMatrix_b_y')
        if self.rawOrientationMatrix_b_z:
            self.rawOrientationMatrix_b_z.export(outfile, level, name_='rawOrientationMatrix_b_z')
        if self.rawOrientationMatrix_c_x:
            self.rawOrientationMatrix_c_x.export(outfile, level, name_='rawOrientationMatrix_c_x')
        if self.rawOrientationMatrix_c_y:
            self.rawOrientationMatrix_c_y.export(outfile, level, name_='rawOrientationMatrix_c_y')
        if self.rawOrientationMatrix_c_z:
            self.rawOrientationMatrix_c_z.export(outfile, level, name_='rawOrientationMatrix_c_z')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.screeningOutputLatticeId:
            self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.timeStamp:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        if self.unitCell_a:
            self.unitCell_a.export(outfile, level, name_='unitCell_a')
        if self.unitCell_alpha:
            self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
        if self.unitCell_b:
            self.unitCell_b.export(outfile, level, name_='unitCell_b')
        if self.unitCell_beta:
            self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
        if self.unitCell_c:
            self.unitCell_c.export(outfile, level, name_='unitCell_c')
        if self.unitCell_gamma:
            self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningOutputLattice' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputLattice.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningOutputLattice.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningOutputLattice" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bravaisLattice:
            showIndent(outfile, level)
            outfile.write('bravaisLattice=XSDataString(\n')
            self.bravaisLattice.exportLiteral(outfile, level, name_='bravaisLattice')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pointGroup:
            showIndent(outfile, level)
            outfile.write('pointGroup=XSDataString(\n')
            self.pointGroup.exportLiteral(outfile, level, name_='pointGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_x=XSDataDouble(\n')
            self.rawOrientationMatrix_a_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_y=XSDataDouble(\n')
            self.rawOrientationMatrix_a_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_z=XSDataDouble(\n')
            self.rawOrientationMatrix_a_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_x=XSDataDouble(\n')
            self.rawOrientationMatrix_b_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_y=XSDataDouble(\n')
            self.rawOrientationMatrix_b_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_z=XSDataDouble(\n')
            self.rawOrientationMatrix_b_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_x=XSDataDouble(\n')
            self.rawOrientationMatrix_c_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_y=XSDataDouble(\n')
            self.rawOrientationMatrix_c_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_z=XSDataDouble(\n')
            self.rawOrientationMatrix_c_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputLatticeId:
            showIndent(outfile, level)
            outfile.write('screeningOutputLatticeId=XSDataInteger(\n')
            self.screeningOutputLatticeId.exportLiteral(outfile, level, name_='screeningOutputLatticeId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=XSDataString(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeStamp:
            showIndent(outfile, level)
            outfile.write('timeStamp=XSDataString(\n')
            self.timeStamp.exportLiteral(outfile, level, name_='timeStamp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_a:
            showIndent(outfile, level)
            outfile.write('unitCell_a=XSDataDouble(\n')
            self.unitCell_a.exportLiteral(outfile, level, name_='unitCell_a')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_alpha:
            showIndent(outfile, level)
            outfile.write('unitCell_alpha=XSDataDouble(\n')
            self.unitCell_alpha.exportLiteral(outfile, level, name_='unitCell_alpha')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_b:
            showIndent(outfile, level)
            outfile.write('unitCell_b=XSDataDouble(\n')
            self.unitCell_b.exportLiteral(outfile, level, name_='unitCell_b')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_beta:
            showIndent(outfile, level)
            outfile.write('unitCell_beta=XSDataDouble(\n')
            self.unitCell_beta.exportLiteral(outfile, level, name_='unitCell_beta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_c:
            showIndent(outfile, level)
            outfile.write('unitCell_c=XSDataDouble(\n')
            self.unitCell_c.exportLiteral(outfile, level, name_='unitCell_c')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_gamma:
            showIndent(outfile, level)
            outfile.write('unitCell_gamma=XSDataDouble(\n')
            self.unitCell_gamma.exportLiteral(outfile, level, name_='unitCell_gamma')
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
            nodeName_ == 'bravaisLattice':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBravaisLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointGroup':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPointGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_x':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_y':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_z':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_x':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_y':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_z':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_x':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_y':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_z':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLatticeId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputLatticeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setTimeStamp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_a':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_alpha':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_b':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_beta':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_c':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_gamma':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setUnitCell_gamma(obj_)
# end class XSDataISPyBScreeningOutputLattice


class XSDataISPyBScreeningRank(XSData):
    subclass = None
    def __init__(self, rankInformation=None, rankValue=None, screeningId=None, screeningRankId=None, screeningRankSetId=None):
        XSData.__init__(self)
        self.rankInformation = rankInformation
        self.rankValue = rankValue
        self.screeningId = screeningId
        self.screeningRankId = screeningRankId
        self.screeningRankSetId = screeningRankSetId
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningRank.subclass:
            return XSDataISPyBScreeningRank.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningRank(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getRankInformation(self): return self.rankInformation
    def setRankInformation(self, rankInformation): self.rankInformation = rankInformation
    def getRankValue(self): return self.rankValue
    def setRankValue(self, rankValue): self.rankValue = rankValue
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getScreeningRankId(self): return self.screeningRankId
    def setScreeningRankId(self, screeningRankId): self.screeningRankId = screeningRankId
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def export(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRank')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        if self.rankInformation:
            self.rankInformation.export(outfile, level, name_='rankInformation')
        if self.rankValue:
            self.rankValue.export(outfile, level, name_='rankValue')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.screeningRankId:
            self.screeningRankId.export(outfile, level, name_='screeningRankId')
        if self.screeningRankSetId:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningRank' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRank.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRank.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningRank" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.rankInformation:
            showIndent(outfile, level)
            outfile.write('rankInformation=XSDataString(\n')
            self.rankInformation.exportLiteral(outfile, level, name_='rankInformation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankValue:
            showIndent(outfile, level)
            outfile.write('rankValue=XSDataDouble(\n')
            self.rankValue.exportLiteral(outfile, level, name_='rankValue')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningRankId:
            showIndent(outfile, level)
            outfile.write('screeningRankId=XSDataInteger(\n')
            self.screeningRankId.exportLiteral(outfile, level, name_='screeningRankId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningRankSetId:
            showIndent(outfile, level)
            outfile.write('screeningRankSetId=XSDataInteger(\n')
            self.screeningRankSetId.exportLiteral(outfile, level, name_='screeningRankSetId')
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
            nodeName_ == 'rankInformation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRankInformation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankValue':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRankValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
# end class XSDataISPyBScreeningRank


class XSDataISPyBScreeningRankSet(XSData):
    subclass = None
    def __init__(self, rankEngine=None, rankingProjectFileName=None, rankingSummaryFileName=None, screeningRankSetId=None):
        XSData.__init__(self)
        self.rankEngine = rankEngine
        self.rankingProjectFileName = rankingProjectFileName
        self.rankingSummaryFileName = rankingSummaryFileName
        self.screeningRankSetId = screeningRankSetId
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningRankSet.subclass:
            return XSDataISPyBScreeningRankSet.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningRankSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getRankEngine(self): return self.rankEngine
    def setRankEngine(self, rankEngine): self.rankEngine = rankEngine
    def getRankingProjectFileName(self): return self.rankingProjectFileName
    def setRankingProjectFileName(self, rankingProjectFileName): self.rankingProjectFileName = rankingProjectFileName
    def getRankingSummaryFileName(self): return self.rankingSummaryFileName
    def setRankingSummaryFileName(self, rankingSummaryFileName): self.rankingSummaryFileName = rankingSummaryFileName
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def export(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRankSet')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        if self.rankEngine:
            self.rankEngine.export(outfile, level, name_='rankEngine')
        if self.rankingProjectFileName:
            self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
        if self.rankingSummaryFileName:
            self.rankingSummaryFileName.export(outfile, level, name_='rankingSummaryFileName')
        if self.screeningRankSetId:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningRankSet' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRankSet.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningRankSet.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningRankSet" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.rankEngine:
            showIndent(outfile, level)
            outfile.write('rankEngine=XSDataString(\n')
            self.rankEngine.exportLiteral(outfile, level, name_='rankEngine')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankingProjectFileName:
            showIndent(outfile, level)
            outfile.write('rankingProjectFileName=XSDataString(\n')
            self.rankingProjectFileName.exportLiteral(outfile, level, name_='rankingProjectFileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankingSummaryFileName:
            showIndent(outfile, level)
            outfile.write('rankingSummaryFileName=XSDataString(\n')
            self.rankingSummaryFileName.exportLiteral(outfile, level, name_='rankingSummaryFileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningRankSetId:
            showIndent(outfile, level)
            outfile.write('screeningRankSetId=XSDataInteger(\n')
            self.screeningRankSetId.exportLiteral(outfile, level, name_='screeningRankSetId')
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
            nodeName_ == 'rankEngine':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRankEngine(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingProjectFileName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRankingProjectFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingSummaryFileName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRankingSummaryFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
# end class XSDataISPyBScreeningRankSet


class XSDataISPyBScreeningStrategy(XSData):
    subclass = None
    def __init__(self, anomalous=None, completeness=None, exposureTime=None, multiplicity=None, phiEnd=None, phiStart=None, program=None, rankingResolution=None, resolution=None, rotation=None, screeningOutputId=None, screeningStrategyId=None, transmission=None):
        XSData.__init__(self)
        self.anomalous = anomalous
        self.completeness = completeness
        self.exposureTime = exposureTime
        self.multiplicity = multiplicity
        self.phiEnd = phiEnd
        self.phiStart = phiStart
        self.program = program
        self.rankingResolution = rankingResolution
        self.resolution = resolution
        self.rotation = rotation
        self.screeningOutputId = screeningOutputId
        self.screeningStrategyId = screeningStrategyId
        self.transmission = transmission
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategy.subclass:
            return XSDataISPyBScreeningStrategy.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAnomalous(self): return self.anomalous
    def setAnomalous(self, anomalous): self.anomalous = anomalous
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getExposureTime(self): return self.exposureTime
    def setExposureTime(self, exposureTime): self.exposureTime = exposureTime
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getPhiEnd(self): return self.phiEnd
    def setPhiEnd(self, phiEnd): self.phiEnd = phiEnd
    def getPhiStart(self): return self.phiStart
    def setPhiStart(self, phiStart): self.phiStart = phiStart
    def getProgram(self): return self.program
    def setProgram(self, program): self.program = program
    def getRankingResolution(self): return self.rankingResolution
    def setRankingResolution(self, rankingResolution): self.rankingResolution = rankingResolution
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getRotation(self): return self.rotation
    def setRotation(self, rotation): self.rotation = rotation
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningStrategyId(self): return self.screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId): self.screeningStrategyId = screeningStrategyId
    def getTransmission(self): return self.transmission
    def setTransmission(self, transmission): self.transmission = transmission
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategy')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        if self.anomalous:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.exposureTime:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self.multiplicity:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self.phiEnd:
            self.phiEnd.export(outfile, level, name_='phiEnd')
        if self.phiStart:
            self.phiStart.export(outfile, level, name_='phiStart')
        if self.program:
            self.program.export(outfile, level, name_='program')
        if self.rankingResolution:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        if self.rotation:
            self.rotation.export(outfile, level, name_='rotation')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.screeningStrategyId:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        if self.transmission:
            self.transmission.export(outfile, level, name_='transmission')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategy' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.anomalous:
            showIndent(outfile, level)
            outfile.write('anomalous=XSDataBoolean(\n')
            self.anomalous.exportLiteral(outfile, level, name_='anomalous')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataDouble(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.exposureTime:
            showIndent(outfile, level)
            outfile.write('exposureTime=XSDataDouble(\n')
            self.exposureTime.exportLiteral(outfile, level, name_='exposureTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.multiplicity:
            showIndent(outfile, level)
            outfile.write('multiplicity=XSDataDouble(\n')
            self.multiplicity.exportLiteral(outfile, level, name_='multiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.phiEnd:
            showIndent(outfile, level)
            outfile.write('phiEnd=XSDataDouble(\n')
            self.phiEnd.exportLiteral(outfile, level, name_='phiEnd')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.phiStart:
            showIndent(outfile, level)
            outfile.write('phiStart=XSDataDouble(\n')
            self.phiStart.exportLiteral(outfile, level, name_='phiStart')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.program:
            showIndent(outfile, level)
            outfile.write('program=XSDataString(\n')
            self.program.exportLiteral(outfile, level, name_='program')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankingResolution:
            showIndent(outfile, level)
            outfile.write('rankingResolution=XSDataDouble(\n')
            self.rankingResolution.exportLiteral(outfile, level, name_='rankingResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataDouble(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotation:
            showIndent(outfile, level)
            outfile.write('rotation=XSDataDouble(\n')
            self.rotation.exportLiteral(outfile, level, name_='rotation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategyId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyId=XSDataInteger(\n')
            self.screeningStrategyId.exportLiteral(outfile, level, name_='screeningStrategyId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.transmission:
            showIndent(outfile, level)
            outfile.write('transmission=XSDataDouble(\n')
            self.transmission.exportLiteral(outfile, level, name_='transmission')
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
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiEnd':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setPhiEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setPhiStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'program':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setProgram(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRankingResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotation':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRotation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setTransmission(obj_)
# end class XSDataISPyBScreeningStrategy


class XSDataISPyBScreeningStrategyContainer(XSData):
    subclass = None
    def __init__(self, screeningStrategy=None, screeningStrategyWedgeContainer=None):
        XSData.__init__(self)
        self.screeningStrategy = screeningStrategy
        if screeningStrategyWedgeContainer is None:
            self.screeningStrategyWedgeContainer = []
        else:
            self.screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategyContainer.subclass:
            return XSDataISPyBScreeningStrategyContainer.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategyContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningStrategy(self): return self.screeningStrategy
    def setScreeningStrategy(self, screeningStrategy): self.screeningStrategy = screeningStrategy
    def getScreeningStrategyWedgeContainer(self): return self.screeningStrategyWedgeContainer
    def setScreeningStrategyWedgeContainer(self, screeningStrategyWedgeContainer): self.screeningStrategyWedgeContainer = screeningStrategyWedgeContainer
    def addScreeningStrategyWedgeContainer(self, value): self.screeningStrategyWedgeContainer.append(value)
    def insertScreeningStrategyWedgeContainer(self, index, value): self.screeningStrategyWedgeContainer[index] = value
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        if self.screeningStrategy:
            self.screeningStrategy.export(outfile, level, name_='screeningStrategy')
        for screeningStrategyWedgeContainer_ in self.getScreeningStrategyWedgeContainer():
            screeningStrategyWedgeContainer_.export(outfile, level, name_='screeningStrategyWedgeContainer')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyContainer' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningStrategyContainer'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.screeningStrategy:
            showIndent(outfile, level)
            outfile.write('screeningStrategy=XSDataISPyBScreeningStrategy(\n')
            self.screeningStrategy.exportLiteral(outfile, level, name_='screeningStrategy')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningStrategyWedgeContainer=[\n')
        level += 1
        for screeningStrategyWedgeContainer in self.screeningStrategyWedgeContainer:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningStrategyWedgeContainer(\n')
            screeningStrategyWedgeContainer.exportLiteral(outfile, level, name_='screeningStrategyWedgeContainer')
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
            nodeName_ == 'screeningStrategy':
            obj_ = XSDataISPyBScreeningStrategy.factory()
            obj_.build(child_)
            self.setScreeningStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeContainer':
            obj_ = XSDataISPyBScreeningStrategyWedgeContainer.factory()
            obj_.build(child_)
            self.screeningStrategyWedgeContainer.append(obj_)
# end class XSDataISPyBScreeningStrategyContainer


class XSDataISPyBScreeningStrategySubWedge(XSData):
    subclass = None
    def __init__(self, axisEnd=None, axisStart=None, completeness=None, doseTotal=None, exposureTime=None, multiplicity=None, numberOfImages=None, oscillationRange=None, resolution=None, rotationAxis=None, screeningStrategySubWedgeId=None, screeningStrategyWedgeId=None, subWedgeNumber=None, transmission=None):
        XSData.__init__(self)
        self.axisEnd = axisEnd
        self.axisStart = axisStart
        self.completeness = completeness
        self.doseTotal = doseTotal
        self.exposureTime = exposureTime
        self.multiplicity = multiplicity
        self.numberOfImages = numberOfImages
        self.oscillationRange = oscillationRange
        self.resolution = resolution
        self.rotationAxis = rotationAxis
        self.screeningStrategySubWedgeId = screeningStrategySubWedgeId
        self.screeningStrategyWedgeId = screeningStrategyWedgeId
        self.subWedgeNumber = subWedgeNumber
        self.transmission = transmission
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategySubWedge.subclass:
            return XSDataISPyBScreeningStrategySubWedge.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategySubWedge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAxisEnd(self): return self.axisEnd
    def setAxisEnd(self, axisEnd): self.axisEnd = axisEnd
    def getAxisStart(self): return self.axisStart
    def setAxisStart(self, axisStart): self.axisStart = axisStart
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getDoseTotal(self): return self.doseTotal
    def setDoseTotal(self, doseTotal): self.doseTotal = doseTotal
    def getExposureTime(self): return self.exposureTime
    def setExposureTime(self, exposureTime): self.exposureTime = exposureTime
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getNumberOfImages(self): return self.numberOfImages
    def setNumberOfImages(self, numberOfImages): self.numberOfImages = numberOfImages
    def getOscillationRange(self): return self.oscillationRange
    def setOscillationRange(self, oscillationRange): self.oscillationRange = oscillationRange
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getRotationAxis(self): return self.rotationAxis
    def setRotationAxis(self, rotationAxis): self.rotationAxis = rotationAxis
    def getScreeningStrategySubWedgeId(self): return self.screeningStrategySubWedgeId
    def setScreeningStrategySubWedgeId(self, screeningStrategySubWedgeId): self.screeningStrategySubWedgeId = screeningStrategySubWedgeId
    def getScreeningStrategyWedgeId(self): return self.screeningStrategyWedgeId
    def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId): self.screeningStrategyWedgeId = screeningStrategyWedgeId
    def getSubWedgeNumber(self): return self.subWedgeNumber
    def setSubWedgeNumber(self, subWedgeNumber): self.subWedgeNumber = subWedgeNumber
    def getTransmission(self): return self.transmission
    def setTransmission(self, transmission): self.transmission = transmission
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        if self.axisEnd:
            self.axisEnd.export(outfile, level, name_='axisEnd')
        if self.axisStart:
            self.axisStart.export(outfile, level, name_='axisStart')
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.doseTotal:
            self.doseTotal.export(outfile, level, name_='doseTotal')
        if self.exposureTime:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self.multiplicity:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self.numberOfImages:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        if self.oscillationRange:
            self.oscillationRange.export(outfile, level, name_='oscillationRange')
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        if self.rotationAxis:
            self.rotationAxis.export(outfile, level, name_='rotationAxis')
        if self.screeningStrategySubWedgeId:
            self.screeningStrategySubWedgeId.export(outfile, level, name_='screeningStrategySubWedgeId')
        if self.screeningStrategyWedgeId:
            self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
        if self.subWedgeNumber:
            self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
        if self.transmission:
            self.transmission.export(outfile, level, name_='transmission')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategySubWedge' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategySubWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategySubWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategySubWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningStrategySubWedge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.axisEnd:
            showIndent(outfile, level)
            outfile.write('axisEnd=XSDataDouble(\n')
            self.axisEnd.exportLiteral(outfile, level, name_='axisEnd')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.axisStart:
            showIndent(outfile, level)
            outfile.write('axisStart=XSDataDouble(\n')
            self.axisStart.exportLiteral(outfile, level, name_='axisStart')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataDouble(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.doseTotal:
            showIndent(outfile, level)
            outfile.write('doseTotal=XSDataDouble(\n')
            self.doseTotal.exportLiteral(outfile, level, name_='doseTotal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.exposureTime:
            showIndent(outfile, level)
            outfile.write('exposureTime=XSDataDouble(\n')
            self.exposureTime.exportLiteral(outfile, level, name_='exposureTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.multiplicity:
            showIndent(outfile, level)
            outfile.write('multiplicity=XSDataDouble(\n')
            self.multiplicity.exportLiteral(outfile, level, name_='multiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfImages:
            showIndent(outfile, level)
            outfile.write('numberOfImages=XSDataInteger(\n')
            self.numberOfImages.exportLiteral(outfile, level, name_='numberOfImages')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.oscillationRange:
            showIndent(outfile, level)
            outfile.write('oscillationRange=XSDataDouble(\n')
            self.oscillationRange.exportLiteral(outfile, level, name_='oscillationRange')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataDouble(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotationAxis:
            showIndent(outfile, level)
            outfile.write('rotationAxis=XSDataString(\n')
            self.rotationAxis.exportLiteral(outfile, level, name_='rotationAxis')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategySubWedgeId:
            showIndent(outfile, level)
            outfile.write('screeningStrategySubWedgeId=XSDataInteger(\n')
            self.screeningStrategySubWedgeId.exportLiteral(outfile, level, name_='screeningStrategySubWedgeId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategyWedgeId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyWedgeId=XSDataInteger(\n')
            self.screeningStrategyWedgeId.exportLiteral(outfile, level, name_='screeningStrategyWedgeId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.subWedgeNumber:
            showIndent(outfile, level)
            outfile.write('subWedgeNumber=XSDataInteger(\n')
            self.subWedgeNumber.exportLiteral(outfile, level, name_='subWedgeNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.transmission:
            showIndent(outfile, level)
            outfile.write('transmission=XSDataDouble(\n')
            self.transmission.exportLiteral(outfile, level, name_='transmission')
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
            nodeName_ == 'axisEnd':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAxisEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisStart':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAxisStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseTotal':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setDoseTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationRange':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setOscillationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxis':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRotationAxis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategySubWedgeId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategySubWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedgeNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSubWedgeNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setTransmission(obj_)
# end class XSDataISPyBScreeningStrategySubWedge


class XSDataISPyBScreeningStrategyWedge(XSData):
    subclass = None
    def __init__(self, completeness=None, doseTotal=None, kappa=None, multiplicity=None, numberOfImages=None, phi=None, resolution=None, screeningStrategyId=None, screeningStrategyWedgeId=None, wedgeNumber=None):
        XSData.__init__(self)
        self.completeness = completeness
        self.doseTotal = doseTotal
        self.kappa = kappa
        self.multiplicity = multiplicity
        self.numberOfImages = numberOfImages
        self.phi = phi
        self.resolution = resolution
        self.screeningStrategyId = screeningStrategyId
        self.screeningStrategyWedgeId = screeningStrategyWedgeId
        self.wedgeNumber = wedgeNumber
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategyWedge.subclass:
            return XSDataISPyBScreeningStrategyWedge.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategyWedge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getDoseTotal(self): return self.doseTotal
    def setDoseTotal(self, doseTotal): self.doseTotal = doseTotal
    def getKappa(self): return self.kappa
    def setKappa(self, kappa): self.kappa = kappa
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getNumberOfImages(self): return self.numberOfImages
    def setNumberOfImages(self, numberOfImages): self.numberOfImages = numberOfImages
    def getPhi(self): return self.phi
    def setPhi(self, phi): self.phi = phi
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getScreeningStrategyId(self): return self.screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId): self.screeningStrategyId = screeningStrategyId
    def getScreeningStrategyWedgeId(self): return self.screeningStrategyWedgeId
    def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId): self.screeningStrategyWedgeId = screeningStrategyWedgeId
    def getWedgeNumber(self): return self.wedgeNumber
    def setWedgeNumber(self, wedgeNumber): self.wedgeNumber = wedgeNumber
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.doseTotal:
            self.doseTotal.export(outfile, level, name_='doseTotal')
        if self.kappa:
            self.kappa.export(outfile, level, name_='kappa')
        if self.multiplicity:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self.numberOfImages:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        if self.phi:
            self.phi.export(outfile, level, name_='phi')
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        if self.screeningStrategyId:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        if self.screeningStrategyWedgeId:
            self.screeningStrategyWedgeId.export(outfile, level, name_='screeningStrategyWedgeId')
        if self.wedgeNumber:
            self.wedgeNumber.export(outfile, level, name_='wedgeNumber')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedge' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataDouble(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.doseTotal:
            showIndent(outfile, level)
            outfile.write('doseTotal=XSDataDouble(\n')
            self.doseTotal.exportLiteral(outfile, level, name_='doseTotal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.kappa:
            showIndent(outfile, level)
            outfile.write('kappa=XSDataDouble(\n')
            self.kappa.exportLiteral(outfile, level, name_='kappa')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.multiplicity:
            showIndent(outfile, level)
            outfile.write('multiplicity=XSDataDouble(\n')
            self.multiplicity.exportLiteral(outfile, level, name_='multiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfImages:
            showIndent(outfile, level)
            outfile.write('numberOfImages=XSDataInteger(\n')
            self.numberOfImages.exportLiteral(outfile, level, name_='numberOfImages')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.phi:
            showIndent(outfile, level)
            outfile.write('phi=XSDataDouble(\n')
            self.phi.exportLiteral(outfile, level, name_='phi')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataDouble(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategyId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyId=XSDataInteger(\n')
            self.screeningStrategyId.exportLiteral(outfile, level, name_='screeningStrategyId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategyWedgeId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyWedgeId=XSDataInteger(\n')
            self.screeningStrategyWedgeId.exportLiteral(outfile, level, name_='screeningStrategyWedgeId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.wedgeNumber:
            showIndent(outfile, level)
            outfile.write('wedgeNumber=XSDataInteger(\n')
            self.wedgeNumber.exportLiteral(outfile, level, name_='wedgeNumber')
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
            nodeName_ == 'completeness':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseTotal':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setDoseTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setPhi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyWedgeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wedgeNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setWedgeNumber(obj_)
# end class XSDataISPyBScreeningStrategyWedge


class XSDataISPyBScreeningStrategyWedgeContainer(XSData):
    subclass = None
    def __init__(self, screeningStrategySubWedge=None, screeningStrategyWedge=None):
        XSData.__init__(self)
        if screeningStrategySubWedge is None:
            self.screeningStrategySubWedge = []
        else:
            self.screeningStrategySubWedge = screeningStrategySubWedge
        self.screeningStrategyWedge = screeningStrategyWedge
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategyWedgeContainer.subclass:
            return XSDataISPyBScreeningStrategyWedgeContainer.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategyWedgeContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningStrategySubWedge(self): return self.screeningStrategySubWedge
    def setScreeningStrategySubWedge(self, screeningStrategySubWedge): self.screeningStrategySubWedge = screeningStrategySubWedge
    def addScreeningStrategySubWedge(self, value): self.screeningStrategySubWedge.append(value)
    def insertScreeningStrategySubWedge(self, index, value): self.screeningStrategySubWedge[index] = value
    def getScreeningStrategyWedge(self): return self.screeningStrategyWedge
    def setScreeningStrategyWedge(self, screeningStrategyWedge): self.screeningStrategyWedge = screeningStrategyWedge
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        for screeningStrategySubWedge_ in self.getScreeningStrategySubWedge():
            screeningStrategySubWedge_.export(outfile, level, name_='screeningStrategySubWedge')
        if self.screeningStrategyWedge:
            self.screeningStrategyWedge.export(outfile, level, name_='screeningStrategyWedge')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataISPyBScreeningStrategyWedgeContainer' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedgeContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBScreeningStrategyWedgeContainer.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataISPyBScreeningStrategyWedgeContainer" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataISPyBScreeningStrategyWedgeContainer'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('screeningStrategySubWedge=[\n')
        level += 1
        for screeningStrategySubWedge in self.screeningStrategySubWedge:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningStrategySubWedge(\n')
            screeningStrategySubWedge.exportLiteral(outfile, level, name_='screeningStrategySubWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.screeningStrategyWedge:
            showIndent(outfile, level)
            outfile.write('screeningStrategyWedge=XSDataISPyBScreeningStrategyWedge(\n')
            self.screeningStrategyWedge.exportLiteral(outfile, level, name_='screeningStrategyWedge')
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
            nodeName_ == 'screeningStrategySubWedge':
            obj_ = XSDataISPyBScreeningStrategySubWedge.factory()
            obj_.build(child_)
            self.screeningStrategySubWedge.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedge':
            obj_ = XSDataISPyBScreeningStrategyWedge.factory()
            obj_.build(child_)
            self.setScreeningStrategyWedge(obj_)
# end class XSDataISPyBScreeningStrategyWedgeContainer


class XSDataInputISPyB(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, file=None, image=None, screening=None, screeningInput=None, screeningOutputContainer=None, screeningRank=None, screeningRankSet=None):
        XSDataInput.__init__(self, configuration)
        if file is None:
            self.file = []
        else:
            self.file = file
        self.image = image
        self.screening = screening
        if screeningInput is None:
            self.screeningInput = []
        else:
            self.screeningInput = screeningInput
        if screeningOutputContainer is None:
            self.screeningOutputContainer = []
        else:
            self.screeningOutputContainer = screeningOutputContainer
        if screeningRank is None:
            self.screeningRank = []
        else:
            self.screeningRank = screeningRank
        self.screeningRankSet = screeningRankSet
    def factory(*args_, **kwargs_):
        if XSDataInputISPyB.subclass:
            return XSDataInputISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataInputISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFile(self): return self.file
    def setFile(self, file): self.file = file
    def addFile(self, value): self.file.append(value)
    def insertFile(self, index, value): self.file[index] = value
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def getScreening(self): return self.screening
    def setScreening(self, screening): self.screening = screening
    def getScreeningInput(self): return self.screeningInput
    def setScreeningInput(self, screeningInput): self.screeningInput = screeningInput
    def addScreeningInput(self, value): self.screeningInput.append(value)
    def insertScreeningInput(self, index, value): self.screeningInput[index] = value
    def getScreeningOutputContainer(self): return self.screeningOutputContainer
    def setScreeningOutputContainer(self, screeningOutputContainer): self.screeningOutputContainer = screeningOutputContainer
    def addScreeningOutputContainer(self, value): self.screeningOutputContainer.append(value)
    def insertScreeningOutputContainer(self, index, value): self.screeningOutputContainer[index] = value
    def getScreeningRank(self): return self.screeningRank
    def setScreeningRank(self, screeningRank): self.screeningRank = screeningRank
    def addScreeningRank(self, value): self.screeningRank.append(value)
    def insertScreeningRank(self, index, value): self.screeningRank[index] = value
    def getScreeningRankSet(self): return self.screeningRankSet
    def setScreeningRankSet(self, screeningRankSet): self.screeningRankSet = screeningRankSet
    def export(self, outfile, level, name_='XSDataInputISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputISPyB'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputISPyB')
    def exportChildren(self, outfile, level, name_='XSDataInputISPyB'):
        for file_ in self.getFile():
            file_.export(outfile, level, name_='file')
        if self.getImage() != None :
            if self.image:
                self.image.export(outfile, level, name_='image')
        if self.getScreening() != None :
            if self.screening:
                self.screening.export(outfile, level, name_='screening')
        for screeningInput_ in self.getScreeningInput():
            screeningInput_.export(outfile, level, name_='screeningInput')
        for screeningOutputContainer_ in self.getScreeningOutputContainer():
            screeningOutputContainer_.export(outfile, level, name_='screeningOutputContainer')
        for screeningRank_ in self.getScreeningRank():
            screeningRank_.export(outfile, level, name_='screeningRank')
        if self.getScreeningRankSet() != None :
            if self.screeningRankSet:
                self.screeningRankSet.export(outfile, level, name_='screeningRankSet')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputISPyB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputISPyB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputISPyB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('file=[\n')
        level += 1
        for file in self.file:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningFile(\n')
            file.exportLiteral(outfile, level, name_='file')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.image:
            showIndent(outfile, level)
            outfile.write('image=XSDataISPyBImage(\n')
            self.image.exportLiteral(outfile, level, name_='image')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screening:
            showIndent(outfile, level)
            outfile.write('screening=XSDataISPyBScreening(\n')
            self.screening.exportLiteral(outfile, level, name_='screening')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningInput=[\n')
        level += 1
        for screeningInput in self.screeningInput:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningInput(\n')
            screeningInput.exportLiteral(outfile, level, name_='screeningInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningOutputContainer=[\n')
        level += 1
        for screeningOutputContainer in self.screeningOutputContainer:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningOutputContainer(\n')
            screeningOutputContainer.exportLiteral(outfile, level, name_='screeningOutputContainer')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningRank=[\n')
        level += 1
        for screeningRank in self.screeningRank:
            showIndent(outfile, level)
            outfile.write('XSDataISPyBScreeningRank(\n')
            screeningRank.exportLiteral(outfile, level, name_='screeningRank')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.screeningRankSet:
            showIndent(outfile, level)
            outfile.write('screeningRankSet=XSDataISPyBScreeningRankSet(\n')
            self.screeningRankSet.exportLiteral(outfile, level, name_='screeningRankSet')
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
            nodeName_ == 'file':
            obj_ = XSDataISPyBScreeningFile.factory()
            obj_.build(child_)
            self.file.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataISPyBImage.factory()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screening':
            obj_ = XSDataISPyBScreening.factory()
            obj_.build(child_)
            self.setScreening(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInput':
            obj_ = XSDataISPyBScreeningInput.factory()
            obj_.build(child_)
            self.screeningInput.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputContainer':
            obj_ = XSDataISPyBScreeningOutputContainer.factory()
            obj_.build(child_)
            self.screeningOutputContainer.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRank':
            obj_ = XSDataISPyBScreeningRank.factory()
            obj_.build(child_)
            self.screeningRank.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSet':
            obj_ = XSDataISPyBScreeningRankSet.factory()
            obj_.build(child_)
            self.setScreeningRankSet(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputISPyB


class XSDataResultISPyB(XSDataResult):
    subclass = None
    def __init__(self, status=None, dataCollectionId=None, screeningFileStatus=None, screeningInputStatus=None, screeningOutputLatticeStatus=None, screeningOutputStatus=None, screeningRankSetStatus=None, screeningRankStatus=None, screeningStatus=None, screeningStrategyStatus=None, screeningStrategySubWedgeStatus=None, screeningStrategyWedgeStatus=None):
        XSDataResult.__init__(self, status)
        self.dataCollectionId = dataCollectionId
        if screeningFileStatus is None:
            self.screeningFileStatus = []
        else:
            self.screeningFileStatus = screeningFileStatus
        if screeningInputStatus is None:
            self.screeningInputStatus = []
        else:
            self.screeningInputStatus = screeningInputStatus
        if screeningOutputLatticeStatus is None:
            self.screeningOutputLatticeStatus = []
        else:
            self.screeningOutputLatticeStatus = screeningOutputLatticeStatus
        if screeningOutputStatus is None:
            self.screeningOutputStatus = []
        else:
            self.screeningOutputStatus = screeningOutputStatus
        self.screeningRankSetStatus = screeningRankSetStatus
        if screeningRankStatus is None:
            self.screeningRankStatus = []
        else:
            self.screeningRankStatus = screeningRankStatus
        self.screeningStatus = screeningStatus
        if screeningStrategyStatus is None:
            self.screeningStrategyStatus = []
        else:
            self.screeningStrategyStatus = screeningStrategyStatus
        if screeningStrategySubWedgeStatus is None:
            self.screeningStrategySubWedgeStatus = []
        else:
            self.screeningStrategySubWedgeStatus = screeningStrategySubWedgeStatus
        if screeningStrategyWedgeStatus is None:
            self.screeningStrategyWedgeStatus = []
        else:
            self.screeningStrategyWedgeStatus = screeningStrategyWedgeStatus
    def factory(*args_, **kwargs_):
        if XSDataResultISPyB.subclass:
            return XSDataResultISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataResultISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getScreeningFileStatus(self): return self.screeningFileStatus
    def setScreeningFileStatus(self, screeningFileStatus): self.screeningFileStatus = screeningFileStatus
    def addScreeningFileStatus(self, value): self.screeningFileStatus.append(value)
    def insertScreeningFileStatus(self, index, value): self.screeningFileStatus[index] = value
    def getScreeningInputStatus(self): return self.screeningInputStatus
    def setScreeningInputStatus(self, screeningInputStatus): self.screeningInputStatus = screeningInputStatus
    def addScreeningInputStatus(self, value): self.screeningInputStatus.append(value)
    def insertScreeningInputStatus(self, index, value): self.screeningInputStatus[index] = value
    def getScreeningOutputLatticeStatus(self): return self.screeningOutputLatticeStatus
    def setScreeningOutputLatticeStatus(self, screeningOutputLatticeStatus): self.screeningOutputLatticeStatus = screeningOutputLatticeStatus
    def addScreeningOutputLatticeStatus(self, value): self.screeningOutputLatticeStatus.append(value)
    def insertScreeningOutputLatticeStatus(self, index, value): self.screeningOutputLatticeStatus[index] = value
    def getScreeningOutputStatus(self): return self.screeningOutputStatus
    def setScreeningOutputStatus(self, screeningOutputStatus): self.screeningOutputStatus = screeningOutputStatus
    def addScreeningOutputStatus(self, value): self.screeningOutputStatus.append(value)
    def insertScreeningOutputStatus(self, index, value): self.screeningOutputStatus[index] = value
    def getScreeningRankSetStatus(self): return self.screeningRankSetStatus
    def setScreeningRankSetStatus(self, screeningRankSetStatus): self.screeningRankSetStatus = screeningRankSetStatus
    def getScreeningRankStatus(self): return self.screeningRankStatus
    def setScreeningRankStatus(self, screeningRankStatus): self.screeningRankStatus = screeningRankStatus
    def addScreeningRankStatus(self, value): self.screeningRankStatus.append(value)
    def insertScreeningRankStatus(self, index, value): self.screeningRankStatus[index] = value
    def getScreeningStatus(self): return self.screeningStatus
    def setScreeningStatus(self, screeningStatus): self.screeningStatus = screeningStatus
    def getScreeningStrategyStatus(self): return self.screeningStrategyStatus
    def setScreeningStrategyStatus(self, screeningStrategyStatus): self.screeningStrategyStatus = screeningStrategyStatus
    def addScreeningStrategyStatus(self, value): self.screeningStrategyStatus.append(value)
    def insertScreeningStrategyStatus(self, index, value): self.screeningStrategyStatus[index] = value
    def getScreeningStrategySubWedgeStatus(self): return self.screeningStrategySubWedgeStatus
    def setScreeningStrategySubWedgeStatus(self, screeningStrategySubWedgeStatus): self.screeningStrategySubWedgeStatus = screeningStrategySubWedgeStatus
    def addScreeningStrategySubWedgeStatus(self, value): self.screeningStrategySubWedgeStatus.append(value)
    def insertScreeningStrategySubWedgeStatus(self, index, value): self.screeningStrategySubWedgeStatus[index] = value
    def getScreeningStrategyWedgeStatus(self): return self.screeningStrategyWedgeStatus
    def setScreeningStrategyWedgeStatus(self, screeningStrategyWedgeStatus): self.screeningStrategyWedgeStatus = screeningStrategyWedgeStatus
    def addScreeningStrategyWedgeStatus(self, value): self.screeningStrategyWedgeStatus.append(value)
    def insertScreeningStrategyWedgeStatus(self, index, value): self.screeningStrategyWedgeStatus[index] = value
    def export(self, outfile, level, name_='XSDataResultISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultISPyB'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultISPyB')
    def exportChildren(self, outfile, level, name_='XSDataResultISPyB'):
        if self.getDataCollectionId() != None :
            if self.dataCollectionId:
                self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        for screeningFileStatus_ in self.getScreeningFileStatus():
            screeningFileStatus_.export(outfile, level, name_='screeningFileStatus')
        for screeningInputStatus_ in self.getScreeningInputStatus():
            screeningInputStatus_.export(outfile, level, name_='screeningInputStatus')
        for screeningOutputLatticeStatus_ in self.getScreeningOutputLatticeStatus():
            screeningOutputLatticeStatus_.export(outfile, level, name_='screeningOutputLatticeStatus')
        for screeningOutputStatus_ in self.getScreeningOutputStatus():
            screeningOutputStatus_.export(outfile, level, name_='screeningOutputStatus')
        if self.getScreeningRankSetStatus() != None :
            if self.screeningRankSetStatus:
                self.screeningRankSetStatus.export(outfile, level, name_='screeningRankSetStatus')
        for screeningRankStatus_ in self.getScreeningRankStatus():
            screeningRankStatus_.export(outfile, level, name_='screeningRankStatus')
        if self.getScreeningStatus() != None :
            if self.screeningStatus:
                self.screeningStatus.export(outfile, level, name_='screeningStatus')
        for screeningStrategyStatus_ in self.getScreeningStrategyStatus():
            screeningStrategyStatus_.export(outfile, level, name_='screeningStrategyStatus')
        for screeningStrategySubWedgeStatus_ in self.getScreeningStrategySubWedgeStatus():
            screeningStrategySubWedgeStatus_.export(outfile, level, name_='screeningStrategySubWedgeStatus')
        for screeningStrategyWedgeStatus_ in self.getScreeningStrategyWedgeStatus():
            screeningStrategyWedgeStatus_.export(outfile, level, name_='screeningStrategyWedgeStatus')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultISPyB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultISPyB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultISPyB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningFileStatus=[\n')
        level += 1
        for screeningFileStatus in self.screeningFileStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningFileStatus.exportLiteral(outfile, level, name_='screeningFileStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningInputStatus=[\n')
        level += 1
        for screeningInputStatus in self.screeningInputStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningInputStatus.exportLiteral(outfile, level, name_='screeningInputStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningOutputLatticeStatus=[\n')
        level += 1
        for screeningOutputLatticeStatus in self.screeningOutputLatticeStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningOutputLatticeStatus.exportLiteral(outfile, level, name_='screeningOutputLatticeStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningOutputStatus=[\n')
        level += 1
        for screeningOutputStatus in self.screeningOutputStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningOutputStatus.exportLiteral(outfile, level, name_='screeningOutputStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.screeningRankSetStatus:
            showIndent(outfile, level)
            outfile.write('screeningRankSetStatus=XSDataResultStatus(\n')
            self.screeningRankSetStatus.exportLiteral(outfile, level, name_='screeningRankSetStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningRankStatus=[\n')
        level += 1
        for screeningRankStatus in self.screeningRankStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningRankStatus.exportLiteral(outfile, level, name_='screeningRankStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.screeningStatus:
            showIndent(outfile, level)
            outfile.write('screeningStatus=XSDataResultStatus(\n')
            self.screeningStatus.exportLiteral(outfile, level, name_='screeningStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('screeningStrategyStatus=[\n')
        level += 1
        for screeningStrategyStatus in self.screeningStrategyStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningStrategyStatus.exportLiteral(outfile, level, name_='screeningStrategyStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningStrategySubWedgeStatus=[\n')
        level += 1
        for screeningStrategySubWedgeStatus in self.screeningStrategySubWedgeStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningStrategySubWedgeStatus.exportLiteral(outfile, level, name_='screeningStrategySubWedgeStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('screeningStrategyWedgeStatus=[\n')
        level += 1
        for screeningStrategyWedgeStatus in self.screeningStrategyWedgeStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            screeningStrategyWedgeStatus.exportLiteral(outfile, level, name_='screeningStrategyWedgeStatus')
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
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningFileStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningFileStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInputStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningInputStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLatticeStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningOutputLatticeStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningOutputStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.setScreeningRankSetStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningRankStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.setScreeningStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningStrategyStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategySubWedgeStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningStrategySubWedgeStatus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.screeningStrategyWedgeStatus.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultISPyB


class XSDataResultStatus(XSData):
    subclass = None
    def __init__(self, code=None, id=None, message=None):
        XSData.__init__(self)
        self.code = code
        self.id = id
        self.message = message
    def factory(*args_, **kwargs_):
        if XSDataResultStatus.subclass:
            return XSDataResultStatus.subclass(*args_, **kwargs_)
        else:
            return XSDataResultStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def getId(self): return self.id
    def setId(self, id): self.id = id
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def export(self, outfile, level, name_='XSDataResultStatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultStatus'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataResultStatus')
    def exportChildren(self, outfile, level, name_='XSDataResultStatus'):
        if self.code:
            self.code.export(outfile, level, name_='code')
        if self.id:
            self.id.export(outfile, level, name_='id')
        if self.message:
            self.message.export(outfile, level, name_='message')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultStatus' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultStatus'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.code:
            showIndent(outfile, level)
            outfile.write('code=XSDataString(\n')
            self.code.exportLiteral(outfile, level, name_='code')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.id:
            showIndent(outfile, level)
            outfile.write('id=XSDataInteger(\n')
            self.id.exportLiteral(outfile, level, name_='id')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.message:
            showIndent(outfile, level)
            outfile.write('message=XSDataString(\n')
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
            nodeName_ == 'code':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'id':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMessage(obj_)
# end class XSDataResultStatus


class XSDatadbstatus(XSData):
    subclass = None
    def __init__(self, code='', dataCollectionId=-1, message='', screeningFileId=-1, screeningId=-1, screeningInputId=-1, screeningOutputId=-1, screeningOutputLatticeId=-1, screeningRankId=-1, screeningRankSetId=-1, screeningStrategyId=-1, screeningStrategySubWedgeId=-1, screeningStrategyWedgeId=-1):
        XSData.__init__(self)
        self.code = code
        self.dataCollectionId = dataCollectionId
        self.message = message
        self.screeningFileId = screeningFileId
        self.screeningId = screeningId
        self.screeningInputId = screeningInputId
        self.screeningOutputId = screeningOutputId
        self.screeningOutputLatticeId = screeningOutputLatticeId
        self.screeningRankId = screeningRankId
        self.screeningRankSetId = screeningRankSetId
        self.screeningStrategyId = screeningStrategyId
        self.screeningStrategySubWedgeId = screeningStrategySubWedgeId
        self.screeningStrategyWedgeId = screeningStrategyWedgeId
    def factory(*args_, **kwargs_):
        if XSDatadbstatus.subclass:
            return XSDatadbstatus.subclass(*args_, **kwargs_)
        else:
            return XSDatadbstatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def getScreeningFileId(self): return self.screeningFileId
    def setScreeningFileId(self, screeningFileId): self.screeningFileId = screeningFileId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getScreeningInputId(self): return self.screeningInputId
    def setScreeningInputId(self, screeningInputId): self.screeningInputId = screeningInputId
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningOutputLatticeId(self): return self.screeningOutputLatticeId
    def setScreeningOutputLatticeId(self, screeningOutputLatticeId): self.screeningOutputLatticeId = screeningOutputLatticeId
    def getScreeningRankId(self): return self.screeningRankId
    def setScreeningRankId(self, screeningRankId): self.screeningRankId = screeningRankId
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def getScreeningStrategyId(self): return self.screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId): self.screeningStrategyId = screeningStrategyId
    def getScreeningStrategySubWedgeId(self): return self.screeningStrategySubWedgeId
    def setScreeningStrategySubWedgeId(self, screeningStrategySubWedgeId): self.screeningStrategySubWedgeId = screeningStrategySubWedgeId
    def getScreeningStrategyWedgeId(self): return self.screeningStrategyWedgeId
    def setScreeningStrategyWedgeId(self, screeningStrategyWedgeId): self.screeningStrategyWedgeId = screeningStrategyWedgeId
    def export(self, outfile, level, name_='XSDatadbstatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDatadbstatus'):
        XSData.exportAttributes(self, outfile, level, name_='XSDatadbstatus')
    def exportChildren(self, outfile, level, name_='XSDatadbstatus'):
        showIndent(outfile, level)
        outfile.write('<code>%s</code>\n' % quote_xml(self.getCode()))
        showIndent(outfile, level)
        outfile.write('<dataCollectionId>%d</dataCollectionId>\n' % self.getDataCollectionId())
        showIndent(outfile, level)
        outfile.write('<message>%s</message>\n' % quote_xml(self.getMessage()))
        showIndent(outfile, level)
        outfile.write('<screeningFileId>%d</screeningFileId>\n' % self.getScreeningFileId())
        showIndent(outfile, level)
        outfile.write('<screeningId>%d</screeningId>\n' % self.getScreeningId())
        showIndent(outfile, level)
        outfile.write('<screeningInputId>%d</screeningInputId>\n' % self.getScreeningInputId())
        showIndent(outfile, level)
        outfile.write('<screeningOutputId>%d</screeningOutputId>\n' % self.getScreeningOutputId())
        showIndent(outfile, level)
        outfile.write('<screeningOutputLatticeId>%d</screeningOutputLatticeId>\n' % self.getScreeningOutputLatticeId())
        showIndent(outfile, level)
        outfile.write('<screeningRankId>%d</screeningRankId>\n' % self.getScreeningRankId())
        showIndent(outfile, level)
        outfile.write('<screeningRankSetId>%d</screeningRankSetId>\n' % self.getScreeningRankSetId())
        showIndent(outfile, level)
        outfile.write('<screeningStrategyId>%d</screeningStrategyId>\n' % self.getScreeningStrategyId())
        showIndent(outfile, level)
        outfile.write('<screeningStrategySubWedgeId>%d</screeningStrategySubWedgeId>\n' % self.getScreeningStrategySubWedgeId())
        showIndent(outfile, level)
        outfile.write('<screeningStrategyWedgeId>%d</screeningStrategyWedgeId>\n' % self.getScreeningStrategyWedgeId())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDatadbstatus' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDatadbstatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDatadbstatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDatadbstatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDatadbstatus'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('code=%s,\n' % quote_python(self.getCode()))
        showIndent(outfile, level)
        outfile.write('dataCollectionId=%d,\n' % self.getDataCollectionId())
        showIndent(outfile, level)
        outfile.write('message=%s,\n' % quote_python(self.getMessage()))
        showIndent(outfile, level)
        outfile.write('screeningFileId=%d,\n' % self.getScreeningFileId())
        showIndent(outfile, level)
        outfile.write('screeningId=%d,\n' % self.getScreeningId())
        showIndent(outfile, level)
        outfile.write('screeningInputId=%d,\n' % self.getScreeningInputId())
        showIndent(outfile, level)
        outfile.write('screeningOutputId=%d,\n' % self.getScreeningOutputId())
        showIndent(outfile, level)
        outfile.write('screeningOutputLatticeId=%d,\n' % self.getScreeningOutputLatticeId())
        showIndent(outfile, level)
        outfile.write('screeningRankId=%d,\n' % self.getScreeningRankId())
        showIndent(outfile, level)
        outfile.write('screeningRankSetId=%d,\n' % self.getScreeningRankSetId())
        showIndent(outfile, level)
        outfile.write('screeningStrategyId=%d,\n' % self.getScreeningStrategyId())
        showIndent(outfile, level)
        outfile.write('screeningStrategySubWedgeId=%d,\n' % self.getScreeningStrategySubWedgeId())
        showIndent(outfile, level)
        outfile.write('screeningStrategyWedgeId=%d,\n' % self.getScreeningStrategyWedgeId())
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
            nodeName_ == 'code':
            code_ = ''
            for text__content_ in child_.childNodes:
                code_ += text__content_.nodeValue
            self.code = code_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.dataCollectionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            message_ = ''
            for text__content_ in child_.childNodes:
                message_ += text__content_.nodeValue
            self.message = message_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningFileId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningFileId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInputId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningInputId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningOutputId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLatticeId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningOutputLatticeId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningRankId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningRankSetId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningStrategyId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategySubWedgeId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningStrategySubWedgeId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyWedgeId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningStrategyWedgeId = ival_
# end class XSDatadbstatus


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


class XSDataDisplacement(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataDisplacement.subclass:
            return XSDataDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDisplacement'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataDisplacement')
    def exportChildren(self, outfile, level, name_='XSDataDisplacement'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

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
# end class XSDataDisplacement


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
# end class XSDataLinearDisplacement


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
        elif name == 'blSampleId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('blSampleId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollectionId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('dataCollectionId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollectionNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('dataCollectionNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('experimentType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageDirectory':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('imageDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imagePrefix':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('imagePrefix', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sessionId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('sessionId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'comments':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('comments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'cumulativeIntensity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('cumulativeIntensity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fileLocation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileLocation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fileName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('imageId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('imageNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'jpegFileFullPath':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('jpegFileFullPath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'jpegThumbnailFileFullPath':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('jpegThumbnailFileFullPath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'machineMessage':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('machineMessage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'measuredIntensity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('measuredIntensity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'synchrotronCurrent':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('synchrotronCurrent', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'temperature':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('temperature', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'programVersion':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('programVersion', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shortComments':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('shortComments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'timeStamp':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('timeStamp', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'description':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('description', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'filePath':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('filePath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fileType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningFileId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningFileId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamX':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('beamX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamY':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('beamY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maximumFractionRejected':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('maximumFractionRejected', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimumFractionIndexed':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('minimumFractionIndexed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimumSignalToNoise':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('minimumSignalToNoise', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmsErrorLimits':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rmsErrorLimits', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningInputId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningInputId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningInput':
            obj = XSDataISPyBScreeningInput.factory()
            stackObj = SaxStackElement('screeningInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamShiftX':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('beamShiftX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamShiftY':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('beamShiftY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'diffractionRings':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('diffractionRings', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iOverSigma':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('iOverSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('mosaicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicityEstimated':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('mosaicityEstimated', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsFound':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsFound', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsRejected':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsRejected', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsUsed':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsUsed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rejectedReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('rejectedReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolutionObtained':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('resolutionObtained', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningOutputId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningSuccess':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('screeningSuccess', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationR':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('spotDeviationR', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationTheta':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('spotDeviationTheta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'statusDescription':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('statusDescription', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutput':
            obj = XSDataISPyBScreeningOutput.factory()
            stackObj = SaxStackElement('screeningOutput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputLattice':
            obj = XSDataISPyBScreeningOutputLattice.factory()
            stackObj = SaxStackElement('screeningOutputLattice', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyContainer':
            obj = XSDataISPyBScreeningStrategyContainer.factory()
            stackObj = SaxStackElement('screeningStrategyContainer', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bravaisLattice':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bravaisLattice', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pointGroup':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('pointGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_x':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_y':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_z':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_x':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_y':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_z':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_x':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_y':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_z':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputLatticeId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningOutputLatticeId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spaceGroup':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('spaceGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_a':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_a', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_alpha':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_alpha', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_b':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_b', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_beta':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_beta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_c':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_c', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_gamma':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('unitCell_gamma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankInformation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rankInformation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankValue':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rankValue', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRankId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningRankId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRankSetId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningRankSetId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankEngine':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rankEngine', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankingProjectFileName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rankingProjectFileName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankingSummaryFileName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rankingSummaryFileName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'anomalous':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('anomalous', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'completeness':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('completeness', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'exposureTime':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('exposureTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'multiplicity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('multiplicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phiEnd':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('phiEnd', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phiStart':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('phiStart', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'program':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('program', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankingResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rankingResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('resolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotation':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('rotation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningStrategyId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'transmission':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('transmission', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategy':
            obj = XSDataISPyBScreeningStrategy.factory()
            stackObj = SaxStackElement('screeningStrategy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyWedgeContainer':
            obj = XSDataISPyBScreeningStrategyWedgeContainer.factory()
            stackObj = SaxStackElement('screeningStrategyWedgeContainer', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'axisEnd':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('axisEnd', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'axisStart':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('axisStart', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'doseTotal':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('doseTotal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfImages':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfImages', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'oscillationRange':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('oscillationRange', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotationAxis':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rotationAxis', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategySubWedgeId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningStrategySubWedgeId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyWedgeId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningStrategyWedgeId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'subWedgeNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('subWedgeNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kappa':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('kappa', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phi':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('phi', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'wedgeNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('wedgeNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategySubWedge':
            obj = XSDataISPyBScreeningStrategySubWedge.factory()
            stackObj = SaxStackElement('screeningStrategySubWedge', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyWedge':
            obj = XSDataISPyBScreeningStrategyWedge.factory()
            stackObj = SaxStackElement('screeningStrategyWedge', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'file':
            obj = XSDataISPyBScreeningFile.factory()
            stackObj = SaxStackElement('file', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'image':
            obj = XSDataISPyBImage.factory()
            stackObj = SaxStackElement('image', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screening':
            obj = XSDataISPyBScreening.factory()
            stackObj = SaxStackElement('screening', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputContainer':
            obj = XSDataISPyBScreeningOutputContainer.factory()
            stackObj = SaxStackElement('screeningOutputContainer', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRank':
            obj = XSDataISPyBScreeningRank.factory()
            stackObj = SaxStackElement('screeningRank', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRankSet':
            obj = XSDataISPyBScreeningRankSet.factory()
            stackObj = SaxStackElement('screeningRankSet', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningFileStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningFileStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningInputStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningInputStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputLatticeStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningOutputLatticeStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningOutputStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRankSetStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningRankSetStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningRankStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningRankStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningStrategyStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategySubWedgeStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningStrategySubWedgeStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyWedgeStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('screeningStrategyWedgeStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'code':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('code', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'id':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('id', obj)
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
        elif name == 'blSampleId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBlSampleId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollectionId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollectionId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollectionNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollectionNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExperimentType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imagePrefix':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImagePrefix(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sessionId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSessionId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'comments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setComments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'cumulativeIntensity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCumulativeIntensity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fileLocation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileLocation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fileName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'jpegFileFullPath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setJpegFileFullPath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'jpegThumbnailFileFullPath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setJpegThumbnailFileFullPath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'machineMessage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMachineMessage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'measuredIntensity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMeasuredIntensity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'synchrotronCurrent':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSynchrotronCurrent(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'temperature':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTemperature(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'programVersion':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setProgramVersion(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shortComments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setShortComments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'timeStamp':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTimeStamp(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'description':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDescription(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'filePath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFilePath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fileType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningFileId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningFileId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maximumFractionRejected':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaximumFractionRejected(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minimumFractionIndexed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinimumFractionIndexed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minimumSignalToNoise':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinimumSignalToNoise(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rmsErrorLimits':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmsErrorLimits(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningInputId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningInputId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningInput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamShiftX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamShiftX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamShiftY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamShiftY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'diffractionRings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDiffractionRings(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iOverSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicityEstimated':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicityEstimated(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numSpotsFound':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsFound(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numSpotsRejected':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsRejected(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numSpotsUsed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsUsed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rejectedReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRejectedReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolutionObtained':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolutionObtained(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutputId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningSuccess':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningSuccess(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotDeviationR':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotDeviationR(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotDeviationTheta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotDeviationTheta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'statusDescription':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatusDescription(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputLattice':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningOutputLattice(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyContainer':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategyContainer(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bravaisLattice':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBravaisLattice(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pointGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPointGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_a_x':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_a_x(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_a_y':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_a_y(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_a_z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_a_z(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_b_x':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_b_x(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_b_y':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_b_y(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_b_z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_b_z(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_c_x':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_c_x(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_c_y':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_c_y(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rawOrientationMatrix_c_z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRawOrientationMatrix_c_z(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputLatticeId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutputLatticeId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spaceGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpaceGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_a':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_a(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_alpha':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_alpha(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_b':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_b(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_beta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_beta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_c':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_c(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_gamma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_gamma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankInformation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankInformation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankValue':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankValue(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRankId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankSetId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRankSetId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankEngine':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankEngine(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankingProjectFileName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankingProjectFileName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankingSummaryFileName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankingSummaryFileName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'anomalous':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAnomalous(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'completeness':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCompleteness(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'exposureTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExposureTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'multiplicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMultiplicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'phiEnd':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPhiEnd(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'phiStart':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPhiStart(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'program':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setProgram(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankingResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankingResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategyId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'transmission':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTransmission(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyWedgeContainer':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategyWedgeContainer(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'axisEnd':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAxisEnd(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'axisStart':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAxisStart(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'doseTotal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDoseTotal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfImages':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfImages(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'oscillationRange':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOscillationRange(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotationAxis':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotationAxis(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategySubWedgeId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategySubWedgeId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyWedgeId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategyWedgeId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'subWedgeNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSubWedgeNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'kappa':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKappa(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'phi':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPhi(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'wedgeNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setWedgeNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategySubWedge':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategySubWedge(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyWedge':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategyWedge(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'file':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'image':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screening':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreening(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputContainer':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningOutputContainer(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRank':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningRank(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankSet':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRankSet(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningFileStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningFileStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningInputStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningInputStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputLatticeStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningOutputLatticeStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningOutputStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankSetStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRankSetStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningRankStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategyStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategySubWedgeStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategySubWedgeStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyWedgeStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addScreeningStrategyWedgeStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'code':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCode(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'id':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setId(self.stack[-1].obj)
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
    sys.stdout.write('from XSDataISPyBv1_2 import *\n\n')
    sys.stdout.write('rootObj = XSConfiguration(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSConfiguration")
    sys.stdout.write(')\n')
    return rootObj

class XSDataISPyBv1_2:
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

