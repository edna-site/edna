#!/usr/bin/env python

#
# Generated Mon Sep 21 16:57:09 2009 by EDGenerateDS.py.
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

class XSDataDouble:
    subclass = None
    def __init__(self, value=0.0):
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
        pass
    def exportChildren(self, outfile, level, name_='XSDataDouble'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())

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
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
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
# end class XSDataDouble


class XSData:
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
        outfile.write(self.valueOf_)

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


class XSDataWavelength(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataWavelength.subclass:
            return XSDataWavelength.subclass(*args_, **kwargs_)
        else:
            return XSDataWavelength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataWavelength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataWavelength'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataWavelength')
    def exportChildren(self, outfile, level, name_='XSDataWavelength'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataWavelength


class XSDataMatrix(XSData):
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
        if XSDataMatrix.subclass:
            return XSDataMatrix.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrix(*args_, **kwargs_)
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
    def export(self, outfile, level, name_='XSDataMatrix'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrix'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMatrix')
    def exportChildren(self, outfile, level, name_='XSDataMatrix'):
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
# end class XSDataMatrix


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


class XSDataExecutionInfo(XSData):
    subclass = None
    def __init__(self, baseDirectory=None, configuration=None, executionTime=None, pluginName=None, startOfExecution=None, systemInfo=None, workingDirectory=None):
        XSData.__init__(self)
        self.baseDirectory = baseDirectory
        self.configuration = configuration
        self.executionTime = executionTime
        self.pluginName = pluginName
        self.startOfExecution = startOfExecution
        self.systemInfo = systemInfo
        self.workingDirectory = workingDirectory
    def factory(*args_, **kwargs_):
        if XSDataExecutionInfo.subclass:
            return XSDataExecutionInfo.subclass(*args_, **kwargs_)
        else:
            return XSDataExecutionInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBaseDirectory(self): return self.baseDirectory
    def setBaseDirectory(self, baseDirectory): self.baseDirectory = baseDirectory
    def getConfiguration(self): return self.configuration
    def setConfiguration(self, configuration): self.configuration = configuration
    def getExecutionTime(self): return self.executionTime
    def setExecutionTime(self, executionTime): self.executionTime = executionTime
    def getPluginName(self): return self.pluginName
    def setPluginName(self, pluginName): self.pluginName = pluginName
    def getStartOfExecution(self): return self.startOfExecution
    def setStartOfExecution(self, startOfExecution): self.startOfExecution = startOfExecution
    def getSystemInfo(self): return self.systemInfo
    def setSystemInfo(self, systemInfo): self.systemInfo = systemInfo
    def getWorkingDirectory(self): return self.workingDirectory
    def setWorkingDirectory(self, workingDirectory): self.workingDirectory = workingDirectory
    def export(self, outfile, level, name_='XSDataExecutionInfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataExecutionInfo'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataExecutionInfo')
    def exportChildren(self, outfile, level, name_='XSDataExecutionInfo'):
        if self.baseDirectory:
            self.baseDirectory.export(outfile, level, name_='baseDirectory')
        if self.configuration:
            self.configuration.export(outfile, level, name_='configuration')
        if self.executionTime:
            self.executionTime.export(outfile, level, name_='executionTime')
        if self.pluginName:
            self.pluginName.export(outfile, level, name_='pluginName')
        if self.startOfExecution:
            self.startOfExecution.export(outfile, level, name_='startOfExecution')
        if self.systemInfo:
            self.systemInfo.export(outfile, level, name_='systemInfo')
        if self.workingDirectory:
            self.workingDirectory.export(outfile, level, name_='workingDirectory')
        XSData.exportChildren(self, outfile, level, name_)

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
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.baseDirectory:
            showIndent(outfile, level)
            outfile.write('baseDirectory=XSDataFile(\n')
            self.baseDirectory.exportLiteral(outfile, level, name_='baseDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.configuration:
            showIndent(outfile, level)
            outfile.write('configuration=XSConfiguration(\n')
            self.configuration.exportLiteral(outfile, level, name_='configuration')
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
        if self.systemInfo:
            showIndent(outfile, level)
            outfile.write('systemInfo=XSDataSystemInfo(\n')
            self.systemInfo.exportLiteral(outfile, level, name_='systemInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.workingDirectory:
            showIndent(outfile, level)
            outfile.write('workingDirectory=XSDataFile(\n')
            self.workingDirectory.exportLiteral(outfile, level, name_='workingDirectory')
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
            nodeName_ == 'baseDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setBaseDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'configuration':
            obj_ = XSConfiguration.factory()
            obj_.build(child_)
            self.setConfiguration(obj_)
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
            nodeName_ == 'systemInfo':
            obj_ = XSDataSystemInfo.factory()
            obj_.build(child_)
            self.setSystemInfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'workingDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setWorkingDirectory(obj_)
# end class XSDataExecutionInfo


class XSDataDate(XSData):
    subclass = None
    def __init__(self, value=None):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataDate.subclass:
            return XSDataDate.subclass(*args_, **kwargs_)
        else:
            return XSDataDate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataDate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDate'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDate')
    def exportChildren(self, outfile, level, name_='XSDataDate'):
        if self.value:
            self.value.export(outfile, level, name_='value')
        XSData.exportChildren(self, outfile, level, name_)

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
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.value:
            showIndent(outfile, level)
            outfile.write('value=XSDataString(\n')
            self.value.exportLiteral(outfile, level, name_='value')
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
            nodeName_ == 'value':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setValue(obj_)
# end class XSDataDate


class XSDataMessage(XSData):
    subclass = None
    def __init__(self, debugInfo=None, level=None, text=None, typexx=None):
        XSData.__init__(self)
        self.debugInfo = debugInfo
        self.level = level
        self.text = text
        self.typexx = typexx
    def factory(*args_, **kwargs_):
        if XSDataMessage.subclass:
            return XSDataMessage.subclass(*args_, **kwargs_)
        else:
            return XSDataMessage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDebugInfo(self): return self.debugInfo
    def setDebugInfo(self, debugInfo): self.debugInfo = debugInfo
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
        if self.debugInfo:
            self.debugInfo.export(outfile, level, name_='debugInfo')
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
        if self.debugInfo:
            showIndent(outfile, level)
            outfile.write('debugInfo=XSDataString(\n')
            self.debugInfo.exportLiteral(outfile, level, name_='debugInfo')
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
            nodeName_ == 'debugInfo':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDebugInfo(obj_)
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


class XSDataMessageError(XSDataMessage):
    subclass = None
    def __init__(self, debugMessage=None, errorType=None, debugInfo=None, level=None, text=None, typexx=None):
        XSDataMessage.__init__(self, debugInfo, level, text, typexx)
        self.debugMessage = debugMessage
        self.errorType = errorType
    def factory(*args_, **kwargs_):
        if XSDataMessageError.subclass:
            return XSDataMessageError.subclass(*args_, **kwargs_)
        else:
            return XSDataMessageError(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDebugMessage(self): return self.debugMessage
    def setDebugMessage(self, debugMessage): self.debugMessage = debugMessage
    def getErrorType(self): return self.errorType
    def setErrorType(self, errorType): self.errorType = errorType
    def export(self, outfile, level, name_='XSDataMessageError'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMessageError'):
        XSDataMessage.exportAttributes(self, outfile, level, name_='XSDataMessageError')
    def exportChildren(self, outfile, level, name_='XSDataMessageError'):
        if self.debugMessage:
            self.debugMessage.export(outfile, level, name_='debugMessage')
        if self.errorType:
            self.errorType.export(outfile, level, name_='errorType')
        XSDataMessage.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMessageError' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMessageError.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMessageError.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMessageError" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMessageError'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataMessage.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.debugMessage:
            showIndent(outfile, level)
            outfile.write('debugMessage=XSDataString(\n')
            self.debugMessage.exportLiteral(outfile, level, name_='debugMessage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.errorType:
            showIndent(outfile, level)
            outfile.write('errorType=XSDataString(\n')
            self.errorType.exportLiteral(outfile, level, name_='errorType')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataMessage.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataMessage.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'debugMessage':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDebugMessage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'errorType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setErrorType(obj_)
        XSDataMessage.buildChildren(self, child_, nodeName_)
# end class XSDataMessageError


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
    def __init__(self, name='', XSOptionList=None, XSParamList=None):
        self.name = name
        self.XSOptionList = XSOptionList
        self.XSParamList = XSParamList
    def factory(*args_, **kwargs_):
        if XSPluginItem.subclass:
            return XSPluginItem.subclass(*args_, **kwargs_)
        else:
            return XSPluginItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getXSOptionList(self): return self.XSOptionList
    def setXSOptionList(self, XSOptionList): self.XSOptionList = XSOptionList
    def getXSParamList(self): return self.XSParamList
    def setXSParamList(self, XSParamList): self.XSParamList = XSParamList
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
        if self.XSOptionList:
            self.XSOptionList.export(outfile, level)
        if self.XSParamList:
            self.XSParamList.export(outfile, level)

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
        if self.XSOptionList:
            showIndent(outfile, level)
            outfile.write('XSOptionList=XSOptionList(\n')
            self.XSOptionList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XSParamList:
            showIndent(outfile, level)
            outfile.write('XSParamList=XSParamList(\n')
            self.XSParamList.exportLiteral(outfile, level)
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
            nodeName_ == 'XSOptionList':
            obj_ = XSOptionList.factory()
            obj_.build(child_)
            self.setXSOptionList(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSParamList':
            obj_ = XSParamList.factory()
            obj_.build(child_)
            self.setXSParamList(obj_)
# end class XSPluginItem


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


class XSDataStatus(XSData):
    subclass = None
    def __init__(self, executionInfo=None, executiveSummary=None, isSuccess=None, message=None):
        XSData.__init__(self)
        self.executionInfo = executionInfo
        self.executiveSummary = executiveSummary
        self.isSuccess = isSuccess
        if message is None:
            self.message = []
        else:
            self.message = message
    def factory(*args_, **kwargs_):
        if XSDataStatus.subclass:
            return XSDataStatus.subclass(*args_, **kwargs_)
        else:
            return XSDataStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExecutionInfo(self): return self.executionInfo
    def setExecutionInfo(self, executionInfo): self.executionInfo = executionInfo
    def getExecutiveSummary(self): return self.executiveSummary
    def setExecutiveSummary(self, executiveSummary): self.executiveSummary = executiveSummary
    def getIsSuccess(self): return self.isSuccess
    def setIsSuccess(self, isSuccess): self.isSuccess = isSuccess
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def addMessage(self, value): self.message.append(value)
    def insertMessage(self, index, value): self.message[index] = value
    def export(self, outfile, level, name_='XSDataStatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatus'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatus')
    def exportChildren(self, outfile, level, name_='XSDataStatus'):
        if self.executionInfo:
            self.executionInfo.export(outfile, level, name_='executionInfo')
        if self.executiveSummary:
            self.executiveSummary.export(outfile, level, name_='executiveSummary')
        if self.isSuccess:
            self.isSuccess.export(outfile, level, name_='isSuccess')
        for message_ in self.getMessage():
            message_.export(outfile, level, name_='message')
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
        if self.executionInfo:
            showIndent(outfile, level)
            outfile.write('executionInfo=XSDataExecutionInfo(\n')
            self.executionInfo.exportLiteral(outfile, level, name_='executionInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        showIndent(outfile, level)
        outfile.write('message=[\n')
        level += 1
        for message in self.message:
            showIndent(outfile, level)
            outfile.write('XSDataMessage(\n')
            message.exportLiteral(outfile, level, name_='message')
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
            nodeName_ == 'executionInfo':
            obj_ = XSDataExecutionInfo.factory()
            obj_.build(child_)
            self.setExecutionInfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
            nodeName_ == 'message':
            obj_ = XSDataMessage.factory()
            obj_.build(child_)
            self.message.append(obj_)
# end class XSDataStatus


class XSDataSystemInfo(XSData):
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
        if XSDataSystemInfo.subclass:
            return XSDataSystemInfo.subclass(*args_, **kwargs_)
        else:
            return XSDataSystemInfo(*args_, **kwargs_)
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
    def export(self, outfile, level, name_='XSDataSystemInfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSystemInfo'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSystemInfo')
    def exportChildren(self, outfile, level, name_='XSDataSystemInfo'):
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
        self.export( outfile, 0, name_='XSDataSystemInfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSystemInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSystemInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSystemInfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSystemInfo'):
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
# end class XSDataSystemInfo


class XSDataISPyBScreeningOutput(XSData):
    subclass = None
    def __init__(self, screeningOutputId=None, screeningId=None, statusDescription=None, rejectedReflections=None, resolutionObtained=None, spotDeviationR=None, spotDeviationTheta=None, beamShiftX=None, beamShiftY=None, numSpotsFound=None, numSpotsUsed=None, numSpotsRejected=None, mosaicity=None, iOverSigma=None, diffractionRings=None, screeningSuccess=None, mosaicityEstimated=None):
        XSData.__init__(self)
        self.screeningOutputId = screeningOutputId
        self.screeningId = screeningId
        self.statusDescription = statusDescription
        self.rejectedReflections = rejectedReflections
        self.resolutionObtained = resolutionObtained
        self.spotDeviationR = spotDeviationR
        self.spotDeviationTheta = spotDeviationTheta
        self.beamShiftX = beamShiftX
        self.beamShiftY = beamShiftY
        self.numSpotsFound = numSpotsFound
        self.numSpotsUsed = numSpotsUsed
        self.numSpotsRejected = numSpotsRejected
        self.mosaicity = mosaicity
        self.iOverSigma = iOverSigma
        self.diffractionRings = diffractionRings
        self.screeningSuccess = screeningSuccess
        self.mosaicityEstimated = mosaicityEstimated
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningOutput.subclass:
            return XSDataISPyBScreeningOutput.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningOutput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getStatusDescription(self): return self.statusDescription
    def setStatusDescription(self, statusDescription): self.statusDescription = statusDescription
    def getRejectedReflections(self): return self.rejectedReflections
    def setRejectedReflections(self, rejectedReflections): self.rejectedReflections = rejectedReflections
    def getResolutionObtained(self): return self.resolutionObtained
    def setResolutionObtained(self, resolutionObtained): self.resolutionObtained = resolutionObtained
    def getSpotDeviationR(self): return self.spotDeviationR
    def setSpotDeviationR(self, spotDeviationR): self.spotDeviationR = spotDeviationR
    def getSpotDeviationTheta(self): return self.spotDeviationTheta
    def setSpotDeviationTheta(self, spotDeviationTheta): self.spotDeviationTheta = spotDeviationTheta
    def getBeamShiftX(self): return self.beamShiftX
    def setBeamShiftX(self, beamShiftX): self.beamShiftX = beamShiftX
    def getBeamShiftY(self): return self.beamShiftY
    def setBeamShiftY(self, beamShiftY): self.beamShiftY = beamShiftY
    def getNumSpotsFound(self): return self.numSpotsFound
    def setNumSpotsFound(self, numSpotsFound): self.numSpotsFound = numSpotsFound
    def getNumSpotsUsed(self): return self.numSpotsUsed
    def setNumSpotsUsed(self, numSpotsUsed): self.numSpotsUsed = numSpotsUsed
    def getNumSpotsRejected(self): return self.numSpotsRejected
    def setNumSpotsRejected(self, numSpotsRejected): self.numSpotsRejected = numSpotsRejected
    def getMosaicity(self): return self.mosaicity
    def setMosaicity(self, mosaicity): self.mosaicity = mosaicity
    def getIOverSigma(self): return self.iOverSigma
    def setIOverSigma(self, iOverSigma): self.iOverSigma = iOverSigma
    def getDiffractionRings(self): return self.diffractionRings
    def setDiffractionRings(self, diffractionRings): self.diffractionRings = diffractionRings
    def getScreeningSuccess(self): return self.screeningSuccess
    def setScreeningSuccess(self, screeningSuccess): self.screeningSuccess = screeningSuccess
    def getMosaicityEstimated(self): return self.mosaicityEstimated
    def setMosaicityEstimated(self, mosaicityEstimated): self.mosaicityEstimated = mosaicityEstimated
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutput')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutput'):
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.statusDescription:
            self.statusDescription.export(outfile, level, name_='statusDescription')
        if self.rejectedReflections:
            self.rejectedReflections.export(outfile, level, name_='rejectedReflections')
        if self.resolutionObtained:
            self.resolutionObtained.export(outfile, level, name_='resolutionObtained')
        if self.spotDeviationR:
            self.spotDeviationR.export(outfile, level, name_='spotDeviationR')
        if self.spotDeviationTheta:
            self.spotDeviationTheta.export(outfile, level, name_='spotDeviationTheta')
        if self.beamShiftX:
            self.beamShiftX.export(outfile, level, name_='beamShiftX')
        if self.beamShiftY:
            self.beamShiftY.export(outfile, level, name_='beamShiftY')
        if self.numSpotsFound:
            self.numSpotsFound.export(outfile, level, name_='numSpotsFound')
        if self.numSpotsUsed:
            self.numSpotsUsed.export(outfile, level, name_='numSpotsUsed')
        if self.numSpotsRejected:
            self.numSpotsRejected.export(outfile, level, name_='numSpotsRejected')
        if self.mosaicity:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self.iOverSigma:
            self.iOverSigma.export(outfile, level, name_='iOverSigma')
        if self.diffractionRings:
            self.diffractionRings.export(outfile, level, name_='diffractionRings')
        if self.screeningSuccess:
            self.screeningSuccess.export(outfile, level, name_='screeningSuccess')
        if self.mosaicityEstimated:
            self.mosaicityEstimated.export(outfile, level, name_='mosaicityEstimated')
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
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statusDescription:
            showIndent(outfile, level)
            outfile.write('statusDescription=XSDataString(\n')
            self.statusDescription.exportLiteral(outfile, level, name_='statusDescription')
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
            outfile.write('resolutionObtained=XSDataFloat(\n')
            self.resolutionObtained.exportLiteral(outfile, level, name_='resolutionObtained')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationR:
            showIndent(outfile, level)
            outfile.write('spotDeviationR=XSDataFloat(\n')
            self.spotDeviationR.exportLiteral(outfile, level, name_='spotDeviationR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationTheta:
            showIndent(outfile, level)
            outfile.write('spotDeviationTheta=XSDataFloat(\n')
            self.spotDeviationTheta.exportLiteral(outfile, level, name_='spotDeviationTheta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamShiftX:
            showIndent(outfile, level)
            outfile.write('beamShiftX=XSDataFloat(\n')
            self.beamShiftX.exportLiteral(outfile, level, name_='beamShiftX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamShiftY:
            showIndent(outfile, level)
            outfile.write('beamShiftY=XSDataFloat(\n')
            self.beamShiftY.exportLiteral(outfile, level, name_='beamShiftY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsFound:
            showIndent(outfile, level)
            outfile.write('numSpotsFound=XSDataInteger(\n')
            self.numSpotsFound.exportLiteral(outfile, level, name_='numSpotsFound')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsUsed:
            showIndent(outfile, level)
            outfile.write('numSpotsUsed=XSDataInteger(\n')
            self.numSpotsUsed.exportLiteral(outfile, level, name_='numSpotsUsed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numSpotsRejected:
            showIndent(outfile, level)
            outfile.write('numSpotsRejected=XSDataInteger(\n')
            self.numSpotsRejected.exportLiteral(outfile, level, name_='numSpotsRejected')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mosaicity:
            showIndent(outfile, level)
            outfile.write('mosaicity=XSDataFloat(\n')
            self.mosaicity.exportLiteral(outfile, level, name_='mosaicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iOverSigma:
            showIndent(outfile, level)
            outfile.write('iOverSigma=XSDataFloat(\n')
            self.iOverSigma.exportLiteral(outfile, level, name_='iOverSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.diffractionRings:
            showIndent(outfile, level)
            outfile.write('diffractionRings=XSDataBoolean(\n')
            self.diffractionRings.exportLiteral(outfile, level, name_='diffractionRings')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningSuccess:
            showIndent(outfile, level)
            outfile.write('screeningSuccess=XSDataBoolean(\n')
            self.screeningSuccess.exportLiteral(outfile, level, name_='screeningSuccess')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mosaicityEstimated:
            showIndent(outfile, level)
            outfile.write('mosaicityEstimated=XSDataBoolean(\n')
            self.mosaicityEstimated.exportLiteral(outfile, level, name_='mosaicityEstimated')
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
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statusDescription':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setStatusDescription(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rejectedReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setRejectedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionObtained':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setResolutionObtained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setSpotDeviationR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationTheta':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setSpotDeviationTheta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShiftX':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamShiftX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShiftY':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamShiftY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsFound':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsFound(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsUsed':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numSpotsRejected':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumSpotsRejected(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iOverSigma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionRings':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setDiffractionRings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningSuccess':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setScreeningSuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityEstimated':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setMosaicityEstimated(obj_)
# end class XSDataISPyBScreeningOutput


class XSDataISPyBScreeningInput(XSData):
    subclass = None
    def __init__(self, screeningInputId=None, screeningId=None, beamX=None, beamY=None, rmsErrorLimits=None, minimumFractionIndexed=None, maximumFractionRejected=None, minimumSignalToNoise=None):
        XSData.__init__(self)
        self.screeningInputId = screeningInputId
        self.screeningId = screeningId
        self.beamX = beamX
        self.beamY = beamY
        self.rmsErrorLimits = rmsErrorLimits
        self.minimumFractionIndexed = minimumFractionIndexed
        self.maximumFractionRejected = maximumFractionRejected
        self.minimumSignalToNoise = minimumSignalToNoise
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningInput.subclass:
            return XSDataISPyBScreeningInput.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningInputId(self): return self.screeningInputId
    def setScreeningInputId(self, screeningInputId): self.screeningInputId = screeningInputId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getBeamX(self): return self.beamX
    def setBeamX(self, beamX): self.beamX = beamX
    def getBeamY(self): return self.beamY
    def setBeamY(self, beamY): self.beamY = beamY
    def getRmsErrorLimits(self): return self.rmsErrorLimits
    def setRmsErrorLimits(self, rmsErrorLimits): self.rmsErrorLimits = rmsErrorLimits
    def getMinimumFractionIndexed(self): return self.minimumFractionIndexed
    def setMinimumFractionIndexed(self, minimumFractionIndexed): self.minimumFractionIndexed = minimumFractionIndexed
    def getMaximumFractionRejected(self): return self.maximumFractionRejected
    def setMaximumFractionRejected(self, maximumFractionRejected): self.maximumFractionRejected = maximumFractionRejected
    def getMinimumSignalToNoise(self): return self.minimumSignalToNoise
    def setMinimumSignalToNoise(self, minimumSignalToNoise): self.minimumSignalToNoise = minimumSignalToNoise
    def export(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningInput')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningInput'):
        if self.screeningInputId:
            self.screeningInputId.export(outfile, level, name_='screeningInputId')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.beamX:
            self.beamX.export(outfile, level, name_='beamX')
        if self.beamY:
            self.beamY.export(outfile, level, name_='beamY')
        if self.rmsErrorLimits:
            self.rmsErrorLimits.export(outfile, level, name_='rmsErrorLimits')
        if self.minimumFractionIndexed:
            self.minimumFractionIndexed.export(outfile, level, name_='minimumFractionIndexed')
        if self.maximumFractionRejected:
            self.maximumFractionRejected.export(outfile, level, name_='maximumFractionRejected')
        if self.minimumSignalToNoise:
            self.minimumSignalToNoise.export(outfile, level, name_='minimumSignalToNoise')
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
        if self.screeningInputId:
            showIndent(outfile, level)
            outfile.write('screeningInputId=XSDataInteger(\n')
            self.screeningInputId.exportLiteral(outfile, level, name_='screeningInputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamX:
            showIndent(outfile, level)
            outfile.write('beamX=XSDataFloat(\n')
            self.beamX.exportLiteral(outfile, level, name_='beamX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamY:
            showIndent(outfile, level)
            outfile.write('beamY=XSDataFloat(\n')
            self.beamY.exportLiteral(outfile, level, name_='beamY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rmsErrorLimits:
            showIndent(outfile, level)
            outfile.write('rmsErrorLimits=XSDataFloat(\n')
            self.rmsErrorLimits.exportLiteral(outfile, level, name_='rmsErrorLimits')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minimumFractionIndexed:
            showIndent(outfile, level)
            outfile.write('minimumFractionIndexed=XSDataFloat(\n')
            self.minimumFractionIndexed.exportLiteral(outfile, level, name_='minimumFractionIndexed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.maximumFractionRejected:
            showIndent(outfile, level)
            outfile.write('maximumFractionRejected=XSDataFloat(\n')
            self.maximumFractionRejected.exportLiteral(outfile, level, name_='maximumFractionRejected')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minimumSignalToNoise:
            showIndent(outfile, level)
            outfile.write('minimumSignalToNoise=XSDataFloat(\n')
            self.minimumSignalToNoise.exportLiteral(outfile, level, name_='minimumSignalToNoise')
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
            nodeName_ == 'screeningInputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningInputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamX':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamY':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmsErrorLimits':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRmsErrorLimits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimumFractionIndexed':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMinimumFractionIndexed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maximumFractionRejected':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMaximumFractionRejected(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimumSignalToNoise':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMinimumSignalToNoise(obj_)
# end class XSDataISPyBScreeningInput


class XSDataISPyBDataCollection(XSData):
    subclass = None
    def __init__(self, dataCollectionId=None, blSampleId=None, sessionId=None, experimentType=None, dataCollectionNumber=None, imageDirectory=None, imagePrefix=None):
        XSData.__init__(self)
        self.dataCollectionId = dataCollectionId
        self.blSampleId = blSampleId
        self.sessionId = sessionId
        self.experimentType = experimentType
        self.dataCollectionNumber = dataCollectionNumber
        self.imageDirectory = imageDirectory
        self.imagePrefix = imagePrefix
    def factory(*args_, **kwargs_):
        if XSDataISPyBDataCollection.subclass:
            return XSDataISPyBDataCollection.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBDataCollection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getBlSampleId(self): return self.blSampleId
    def setBlSampleId(self, blSampleId): self.blSampleId = blSampleId
    def getSessionId(self): return self.sessionId
    def setSessionId(self, sessionId): self.sessionId = sessionId
    def getExperimentType(self): return self.experimentType
    def setExperimentType(self, experimentType): self.experimentType = experimentType
    def getDataCollectionNumber(self): return self.dataCollectionNumber
    def setDataCollectionNumber(self, dataCollectionNumber): self.dataCollectionNumber = dataCollectionNumber
    def getImageDirectory(self): return self.imageDirectory
    def setImageDirectory(self, imageDirectory): self.imageDirectory = imageDirectory
    def getImagePrefix(self): return self.imagePrefix
    def setImagePrefix(self, imagePrefix): self.imagePrefix = imagePrefix
    def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBDataCollection'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBDataCollection')
    def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
        if self.dataCollectionId:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self.blSampleId:
            self.blSampleId.export(outfile, level, name_='blSampleId')
        if self.sessionId:
            self.sessionId.export(outfile, level, name_='sessionId')
        if self.experimentType:
            self.experimentType.export(outfile, level, name_='experimentType')
        if self.dataCollectionNumber:
            self.dataCollectionNumber.export(outfile, level, name_='dataCollectionNumber')
        if self.imageDirectory:
            self.imageDirectory.export(outfile, level, name_='imageDirectory')
        if self.imagePrefix:
            self.imagePrefix.export(outfile, level, name_='imagePrefix')
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
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.blSampleId:
            showIndent(outfile, level)
            outfile.write('blSampleId=XSDataInteger(\n')
            self.blSampleId.exportLiteral(outfile, level, name_='blSampleId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sessionId:
            showIndent(outfile, level)
            outfile.write('sessionId=XSDataInteger(\n')
            self.sessionId.exportLiteral(outfile, level, name_='sessionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentType:
            showIndent(outfile, level)
            outfile.write('experimentType=XSDataString(\n')
            self.experimentType.exportLiteral(outfile, level, name_='experimentType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionNumber:
            showIndent(outfile, level)
            outfile.write('dataCollectionNumber=XSDataInteger(\n')
            self.dataCollectionNumber.exportLiteral(outfile, level, name_='dataCollectionNumber')
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
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blSampleId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setBlSampleId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSessionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setExperimentType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionNumber(obj_)
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
# end class XSDataISPyBDataCollection


class XSDataISPyBImage(XSData):
    subclass = None
    def __init__(self, imageId=None, imageNumber=None, fileName=None, fileLocation=None, measuredIntensity=None, jpegFileFullPath=None, jpegThumbnailFileFullPath=None, temperature=None, cumulativeIntensity=None, synchrotronCurrent=None, comments=None, machineMessage=None):
        XSData.__init__(self)
        self.imageId = imageId
        self.imageNumber = imageNumber
        self.fileName = fileName
        self.fileLocation = fileLocation
        self.measuredIntensity = measuredIntensity
        self.jpegFileFullPath = jpegFileFullPath
        self.jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
        self.temperature = temperature
        self.cumulativeIntensity = cumulativeIntensity
        self.synchrotronCurrent = synchrotronCurrent
        self.comments = comments
        self.machineMessage = machineMessage
    def factory(*args_, **kwargs_):
        if XSDataISPyBImage.subclass:
            return XSDataISPyBImage.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBImage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getImageId(self): return self.imageId
    def setImageId(self, imageId): self.imageId = imageId
    def getImageNumber(self): return self.imageNumber
    def setImageNumber(self, imageNumber): self.imageNumber = imageNumber
    def getFileName(self): return self.fileName
    def setFileName(self, fileName): self.fileName = fileName
    def getFileLocation(self): return self.fileLocation
    def setFileLocation(self, fileLocation): self.fileLocation = fileLocation
    def getMeasuredIntensity(self): return self.measuredIntensity
    def setMeasuredIntensity(self, measuredIntensity): self.measuredIntensity = measuredIntensity
    def getJpegFileFullPath(self): return self.jpegFileFullPath
    def setJpegFileFullPath(self, jpegFileFullPath): self.jpegFileFullPath = jpegFileFullPath
    def getJpegThumbnailFileFullPath(self): return self.jpegThumbnailFileFullPath
    def setJpegThumbnailFileFullPath(self, jpegThumbnailFileFullPath): self.jpegThumbnailFileFullPath = jpegThumbnailFileFullPath
    def getTemperature(self): return self.temperature
    def setTemperature(self, temperature): self.temperature = temperature
    def getCumulativeIntensity(self): return self.cumulativeIntensity
    def setCumulativeIntensity(self, cumulativeIntensity): self.cumulativeIntensity = cumulativeIntensity
    def getSynchrotronCurrent(self): return self.synchrotronCurrent
    def setSynchrotronCurrent(self, synchrotronCurrent): self.synchrotronCurrent = synchrotronCurrent
    def getComments(self): return self.comments
    def setComments(self, comments): self.comments = comments
    def getMachineMessage(self): return self.machineMessage
    def setMachineMessage(self, machineMessage): self.machineMessage = machineMessage
    def export(self, outfile, level, name_='XSDataISPyBImage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBImage'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBImage')
    def exportChildren(self, outfile, level, name_='XSDataISPyBImage'):
        if self.imageId:
            self.imageId.export(outfile, level, name_='imageId')
        if self.imageNumber:
            self.imageNumber.export(outfile, level, name_='imageNumber')
        if self.fileName:
            self.fileName.export(outfile, level, name_='fileName')
        if self.fileLocation:
            self.fileLocation.export(outfile, level, name_='fileLocation')
        if self.measuredIntensity:
            self.measuredIntensity.export(outfile, level, name_='measuredIntensity')
        if self.jpegFileFullPath:
            self.jpegFileFullPath.export(outfile, level, name_='jpegFileFullPath')
        if self.jpegThumbnailFileFullPath:
            self.jpegThumbnailFileFullPath.export(outfile, level, name_='jpegThumbnailFileFullPath')
        if self.temperature:
            self.temperature.export(outfile, level, name_='temperature')
        if self.cumulativeIntensity:
            self.cumulativeIntensity.export(outfile, level, name_='cumulativeIntensity')
        if self.synchrotronCurrent:
            self.synchrotronCurrent.export(outfile, level, name_='synchrotronCurrent')
        if self.comments:
            self.comments.export(outfile, level, name_='comments')
        if self.machineMessage:
            self.machineMessage.export(outfile, level, name_='machineMessage')
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
        if self.fileName:
            showIndent(outfile, level)
            outfile.write('fileName=XSDataString(\n')
            self.fileName.exportLiteral(outfile, level, name_='fileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fileLocation:
            showIndent(outfile, level)
            outfile.write('fileLocation=XSDataString(\n')
            self.fileLocation.exportLiteral(outfile, level, name_='fileLocation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.measuredIntensity:
            showIndent(outfile, level)
            outfile.write('measuredIntensity=XSDataFloat(\n')
            self.measuredIntensity.exportLiteral(outfile, level, name_='measuredIntensity')
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
        if self.temperature:
            showIndent(outfile, level)
            outfile.write('temperature=XSDataFloat(\n')
            self.temperature.exportLiteral(outfile, level, name_='temperature')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cumulativeIntensity:
            showIndent(outfile, level)
            outfile.write('cumulativeIntensity=XSDataFloat(\n')
            self.cumulativeIntensity.exportLiteral(outfile, level, name_='cumulativeIntensity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.synchrotronCurrent:
            showIndent(outfile, level)
            outfile.write('synchrotronCurrent=XSDataFloat(\n')
            self.synchrotronCurrent.exportLiteral(outfile, level, name_='synchrotronCurrent')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.comments:
            showIndent(outfile, level)
            outfile.write('comments=XSDataString(\n')
            self.comments.exportLiteral(outfile, level, name_='comments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.machineMessage:
            showIndent(outfile, level)
            outfile.write('machineMessage=XSDataString(\n')
            self.machineMessage.exportLiteral(outfile, level, name_='machineMessage')
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
            nodeName_ == 'fileName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileLocation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileLocation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'measuredIntensity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMeasuredIntensity(obj_)
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
            nodeName_ == 'temperature':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cumulativeIntensity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCumulativeIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'synchrotronCurrent':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setSynchrotronCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineMessage':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMachineMessage(obj_)
# end class XSDataISPyBImage


class XSDataISPyBScreeningRank(XSData):
    subclass = None
    def __init__(self, screeningRankId=None, screeningRankSetId=None, screeningId=None, rankValue=None, rankInformation=None):
        XSData.__init__(self)
        self.screeningRankId = screeningRankId
        self.screeningRankSetId = screeningRankSetId
        self.screeningId = screeningId
        self.rankValue = rankValue
        self.rankInformation = rankInformation
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningRank.subclass:
            return XSDataISPyBScreeningRank.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningRank(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningRankId(self): return self.screeningRankId
    def setScreeningRankId(self, screeningRankId): self.screeningRankId = screeningRankId
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getRankValue(self): return self.rankValue
    def setRankValue(self, rankValue): self.rankValue = rankValue
    def getRankInformation(self): return self.rankInformation
    def setRankInformation(self, rankInformation): self.rankInformation = rankInformation
    def export(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRank')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRank'):
        if self.screeningRankId:
            self.screeningRankId.export(outfile, level, name_='screeningRankId')
        if self.screeningRankSetId:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.rankValue:
            self.rankValue.export(outfile, level, name_='rankValue')
        if self.rankInformation:
            self.rankInformation.export(outfile, level, name_='rankInformation')
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
        if self.screeningId:
            showIndent(outfile, level)
            outfile.write('screeningId=XSDataInteger(\n')
            self.screeningId.exportLiteral(outfile, level, name_='screeningId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankValue:
            showIndent(outfile, level)
            outfile.write('rankValue=XSDataFloat(\n')
            self.rankValue.exportLiteral(outfile, level, name_='rankValue')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankInformation:
            showIndent(outfile, level)
            outfile.write('rankInformation=XSDataString(\n')
            self.rankInformation.exportLiteral(outfile, level, name_='rankInformation')
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
            nodeName_ == 'screeningRankId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankValue':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRankValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankInformation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRankInformation(obj_)
# end class XSDataISPyBScreeningRank


class XSDataResultISPyB(XSDataResult):
    subclass = None
    def __init__(self, screeningId=None, screeningInputId=None, screeningOutputId=None, screeningOutputLatticeId=None, screeningRankId=None, screeningRankSetId=None, screeningStrategyId=None, dataCollectionId=None, resultStatus=None, status=None):
        XSDataResult.__init__(self, status)
        self.screeningId = screeningId
        self.screeningInputId = screeningInputId
        self.screeningOutputId = screeningOutputId
        self.screeningOutputLatticeId = screeningOutputLatticeId
        self.screeningRankId = screeningRankId
        self.screeningRankSetId = screeningRankSetId
        self.screeningStrategyId = screeningStrategyId
        self.dataCollectionId = dataCollectionId
        if resultStatus is None:
            self.resultStatus = []
        else:
            self.resultStatus = resultStatus
    def factory(*args_, **kwargs_):
        if XSDataResultISPyB.subclass:
            return XSDataResultISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataResultISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getResultStatus(self): return self.resultStatus
    def setResultStatus(self, resultStatus): self.resultStatus = resultStatus
    def addResultStatus(self, value): self.resultStatus.append(value)
    def insertResultStatus(self, index, value): self.resultStatus[index] = value
    def export(self, outfile, level, name_='XSDataResultISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultISPyB'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultISPyB')
    def exportChildren(self, outfile, level, name_='XSDataResultISPyB'):
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.screeningInputId:
            self.screeningInputId.export(outfile, level, name_='screeningInputId')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.screeningOutputLatticeId:
            self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
        if self.screeningRankId:
            self.screeningRankId.export(outfile, level, name_='screeningRankId')
        if self.screeningRankSetId:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        if self.screeningStrategyId:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        if self.dataCollectionId:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        for resultStatus_ in self.getResultStatus():
            resultStatus_.export(outfile, level, name_='resultStatus')
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
        if self.screeningStrategyId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyId=XSDataInteger(\n')
            self.screeningStrategyId.exportLiteral(outfile, level, name_='screeningStrategyId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('resultStatus=[\n')
        level += 1
        for resultStatus in self.resultStatus:
            showIndent(outfile, level)
            outfile.write('XSDataResultStatus(\n')
            resultStatus.exportLiteral(outfile, level, name_='resultStatus')
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
            nodeName_ == 'screeningId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningInputId(obj_)
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
            nodeName_ == 'screeningRankId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultStatus':
            obj_ = XSDataResultStatus.factory()
            obj_.build(child_)
            self.resultStatus.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultISPyB


class XSDataISPyBScreeningStrategy(XSData):
    subclass = None
    def __init__(self, screeningStrategyId=None, screeningOutputId=None, phiStart=None, phiEnd=None, rotation=None, exposureTime=None, resolution=None, completeness=None, multiplicity=None, anomalous=None, program=None, rankingResolution=None):
        XSData.__init__(self)
        self.screeningStrategyId = screeningStrategyId
        self.screeningOutputId = screeningOutputId
        self.phiStart = phiStart
        self.phiEnd = phiEnd
        self.rotation = rotation
        self.exposureTime = exposureTime
        self.resolution = resolution
        self.completeness = completeness
        self.multiplicity = multiplicity
        self.anomalous = anomalous
        self.program = program
        self.rankingResolution = rankingResolution
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningStrategy.subclass:
            return XSDataISPyBScreeningStrategy.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningStrategy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningStrategyId(self): return self.screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId): self.screeningStrategyId = screeningStrategyId
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getPhiStart(self): return self.phiStart
    def setPhiStart(self, phiStart): self.phiStart = phiStart
    def getPhiEnd(self): return self.phiEnd
    def setPhiEnd(self, phiEnd): self.phiEnd = phiEnd
    def getRotation(self): return self.rotation
    def setRotation(self, rotation): self.rotation = rotation
    def getExposureTime(self): return self.exposureTime
    def setExposureTime(self, exposureTime): self.exposureTime = exposureTime
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getAnomalous(self): return self.anomalous
    def setAnomalous(self, anomalous): self.anomalous = anomalous
    def getProgram(self): return self.program
    def setProgram(self, program): self.program = program
    def getRankingResolution(self): return self.rankingResolution
    def setRankingResolution(self, rankingResolution): self.rankingResolution = rankingResolution
    def export(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningStrategy')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningStrategy'):
        if self.screeningStrategyId:
            self.screeningStrategyId.export(outfile, level, name_='screeningStrategyId')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.phiStart:
            self.phiStart.export(outfile, level, name_='phiStart')
        if self.phiEnd:
            self.phiEnd.export(outfile, level, name_='phiEnd')
        if self.rotation:
            self.rotation.export(outfile, level, name_='rotation')
        if self.exposureTime:
            self.exposureTime.export(outfile, level, name_='exposureTime')
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.multiplicity:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        if self.anomalous:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self.program:
            self.program.export(outfile, level, name_='program')
        if self.rankingResolution:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
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
        if self.screeningStrategyId:
            showIndent(outfile, level)
            outfile.write('screeningStrategyId=XSDataInteger(\n')
            self.screeningStrategyId.exportLiteral(outfile, level, name_='screeningStrategyId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.phiStart:
            showIndent(outfile, level)
            outfile.write('phiStart=XSDataFloat(\n')
            self.phiStart.exportLiteral(outfile, level, name_='phiStart')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.phiEnd:
            showIndent(outfile, level)
            outfile.write('phiEnd=XSDataFloat(\n')
            self.phiEnd.exportLiteral(outfile, level, name_='phiEnd')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotation:
            showIndent(outfile, level)
            outfile.write('rotation=XSDataFloat(\n')
            self.rotation.exportLiteral(outfile, level, name_='rotation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.exposureTime:
            showIndent(outfile, level)
            outfile.write('exposureTime=XSDataFloat(\n')
            self.exposureTime.exportLiteral(outfile, level, name_='exposureTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataFloat(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataFloat(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.multiplicity:
            showIndent(outfile, level)
            outfile.write('multiplicity=XSDataFloat(\n')
            self.multiplicity.exportLiteral(outfile, level, name_='multiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.anomalous:
            showIndent(outfile, level)
            outfile.write('anomalous=XSDataBoolean(\n')
            self.anomalous.exportLiteral(outfile, level, name_='anomalous')
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
            outfile.write('rankingResolution=XSDataFloat(\n')
            self.rankingResolution.exportLiteral(outfile, level, name_='rankingResolution')
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
            nodeName_ == 'screeningStrategyId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningStrategyId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPhiStart(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiEnd':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPhiEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotation':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRotation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'program':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setProgram(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRankingResolution(obj_)
# end class XSDataISPyBScreeningStrategy


class XSDataISPyBScreeningOutputLattice(XSData):
    subclass = None
    def __init__(self, screeningOutputLatticeId=None, screeningOutputId=None, spaceGroup=None, pointGroup=None, bravaisLattice=None, rawOrientationMatrix_a_x=None, rawOrientationMatrix_a_y=None, rawOrientationMatrix_a_z=None, rawOrientationMatrix_b_x=None, rawOrientationMatrix_b_y=None, rawOrientationMatrix_b_z=None, rawOrientationMatrix_c_x=None, rawOrientationMatrix_c_y=None, rawOrientationMatrix_c_z=None, unitCell_a=None, unitCell_b=None, unitCell_c=None, unitCell_alpha=None, unitCell_beta=None, unitCell_gamma=None, timeStamp=None):
        XSData.__init__(self)
        self.screeningOutputLatticeId = screeningOutputLatticeId
        self.screeningOutputId = screeningOutputId
        self.spaceGroup = spaceGroup
        self.pointGroup = pointGroup
        self.bravaisLattice = bravaisLattice
        self.rawOrientationMatrix_a_x = rawOrientationMatrix_a_x
        self.rawOrientationMatrix_a_y = rawOrientationMatrix_a_y
        self.rawOrientationMatrix_a_z = rawOrientationMatrix_a_z
        self.rawOrientationMatrix_b_x = rawOrientationMatrix_b_x
        self.rawOrientationMatrix_b_y = rawOrientationMatrix_b_y
        self.rawOrientationMatrix_b_z = rawOrientationMatrix_b_z
        self.rawOrientationMatrix_c_x = rawOrientationMatrix_c_x
        self.rawOrientationMatrix_c_y = rawOrientationMatrix_c_y
        self.rawOrientationMatrix_c_z = rawOrientationMatrix_c_z
        self.unitCell_a = unitCell_a
        self.unitCell_b = unitCell_b
        self.unitCell_c = unitCell_c
        self.unitCell_alpha = unitCell_alpha
        self.unitCell_beta = unitCell_beta
        self.unitCell_gamma = unitCell_gamma
        self.timeStamp = timeStamp
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningOutputLattice.subclass:
            return XSDataISPyBScreeningOutputLattice.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningOutputLattice(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningOutputLatticeId(self): return self.screeningOutputLatticeId
    def setScreeningOutputLatticeId(self, screeningOutputLatticeId): self.screeningOutputLatticeId = screeningOutputLatticeId
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getPointGroup(self): return self.pointGroup
    def setPointGroup(self, pointGroup): self.pointGroup = pointGroup
    def getBravaisLattice(self): return self.bravaisLattice
    def setBravaisLattice(self, bravaisLattice): self.bravaisLattice = bravaisLattice
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
    def getUnitCell_a(self): return self.unitCell_a
    def setUnitCell_a(self, unitCell_a): self.unitCell_a = unitCell_a
    def getUnitCell_b(self): return self.unitCell_b
    def setUnitCell_b(self, unitCell_b): self.unitCell_b = unitCell_b
    def getUnitCell_c(self): return self.unitCell_c
    def setUnitCell_c(self, unitCell_c): self.unitCell_c = unitCell_c
    def getUnitCell_alpha(self): return self.unitCell_alpha
    def setUnitCell_alpha(self, unitCell_alpha): self.unitCell_alpha = unitCell_alpha
    def getUnitCell_beta(self): return self.unitCell_beta
    def setUnitCell_beta(self, unitCell_beta): self.unitCell_beta = unitCell_beta
    def getUnitCell_gamma(self): return self.unitCell_gamma
    def setUnitCell_gamma(self, unitCell_gamma): self.unitCell_gamma = unitCell_gamma
    def getTimeStamp(self): return self.timeStamp
    def setTimeStamp(self, timeStamp): self.timeStamp = timeStamp
    def export(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningOutputLattice'):
        if self.screeningOutputLatticeId:
            self.screeningOutputLatticeId.export(outfile, level, name_='screeningOutputLatticeId')
        if self.screeningOutputId:
            self.screeningOutputId.export(outfile, level, name_='screeningOutputId')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.pointGroup:
            self.pointGroup.export(outfile, level, name_='pointGroup')
        if self.bravaisLattice:
            self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
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
        if self.unitCell_a:
            self.unitCell_a.export(outfile, level, name_='unitCell_a')
        if self.unitCell_b:
            self.unitCell_b.export(outfile, level, name_='unitCell_b')
        if self.unitCell_c:
            self.unitCell_c.export(outfile, level, name_='unitCell_c')
        if self.unitCell_alpha:
            self.unitCell_alpha.export(outfile, level, name_='unitCell_alpha')
        if self.unitCell_beta:
            self.unitCell_beta.export(outfile, level, name_='unitCell_beta')
        if self.unitCell_gamma:
            self.unitCell_gamma.export(outfile, level, name_='unitCell_gamma')
        if self.timeStamp:
            self.timeStamp.export(outfile, level, name_='timeStamp')
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
        if self.screeningOutputLatticeId:
            showIndent(outfile, level)
            outfile.write('screeningOutputLatticeId=XSDataInteger(\n')
            self.screeningOutputLatticeId.exportLiteral(outfile, level, name_='screeningOutputLatticeId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputId:
            showIndent(outfile, level)
            outfile.write('screeningOutputId=XSDataInteger(\n')
            self.screeningOutputId.exportLiteral(outfile, level, name_='screeningOutputId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=XSDataString(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pointGroup:
            showIndent(outfile, level)
            outfile.write('pointGroup=XSDataString(\n')
            self.pointGroup.exportLiteral(outfile, level, name_='pointGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.bravaisLattice:
            showIndent(outfile, level)
            outfile.write('bravaisLattice=XSDataString(\n')
            self.bravaisLattice.exportLiteral(outfile, level, name_='bravaisLattice')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_x=XSDataFloat(\n')
            self.rawOrientationMatrix_a_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_y=XSDataFloat(\n')
            self.rawOrientationMatrix_a_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_a_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_a_z=XSDataFloat(\n')
            self.rawOrientationMatrix_a_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_a_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_x=XSDataFloat(\n')
            self.rawOrientationMatrix_b_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_y=XSDataFloat(\n')
            self.rawOrientationMatrix_b_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_b_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_b_z=XSDataFloat(\n')
            self.rawOrientationMatrix_b_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_b_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_x:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_x=XSDataFloat(\n')
            self.rawOrientationMatrix_c_x.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_y:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_y=XSDataFloat(\n')
            self.rawOrientationMatrix_c_y.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rawOrientationMatrix_c_z:
            showIndent(outfile, level)
            outfile.write('rawOrientationMatrix_c_z=XSDataFloat(\n')
            self.rawOrientationMatrix_c_z.exportLiteral(outfile, level, name_='rawOrientationMatrix_c_z')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_a:
            showIndent(outfile, level)
            outfile.write('unitCell_a=XSDataFloat(\n')
            self.unitCell_a.exportLiteral(outfile, level, name_='unitCell_a')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_b:
            showIndent(outfile, level)
            outfile.write('unitCell_b=XSDataFloat(\n')
            self.unitCell_b.exportLiteral(outfile, level, name_='unitCell_b')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_c:
            showIndent(outfile, level)
            outfile.write('unitCell_c=XSDataFloat(\n')
            self.unitCell_c.exportLiteral(outfile, level, name_='unitCell_c')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_alpha:
            showIndent(outfile, level)
            outfile.write('unitCell_alpha=XSDataFloat(\n')
            self.unitCell_alpha.exportLiteral(outfile, level, name_='unitCell_alpha')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_beta:
            showIndent(outfile, level)
            outfile.write('unitCell_beta=XSDataFloat(\n')
            self.unitCell_beta.exportLiteral(outfile, level, name_='unitCell_beta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell_gamma:
            showIndent(outfile, level)
            outfile.write('unitCell_gamma=XSDataFloat(\n')
            self.unitCell_gamma.exportLiteral(outfile, level, name_='unitCell_gamma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeStamp:
            showIndent(outfile, level)
            outfile.write('timeStamp=XSDataFloat(\n')
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
            nodeName_ == 'screeningOutputLatticeId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputLatticeId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningOutputId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointGroup':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPointGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bravaisLattice':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBravaisLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_x':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_y':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_a_z':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_a_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_x':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_y':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_b_z':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_b_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_x':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_x(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_y':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_y(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawOrientationMatrix_c_z':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRawOrientationMatrix_c_z(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_a':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_b':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_c':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_alpha':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_beta':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell_gamma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setUnitCell_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeStamp':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTimeStamp(obj_)
# end class XSDataISPyBScreeningOutputLattice


class XSDataISPyBScreening(XSData):
    subclass = None
    def __init__(self, dataCollectionId=None, screeningId=None, timeStamp=None, programVersion=None):
        XSData.__init__(self)
        self.dataCollectionId = dataCollectionId
        self.screeningId = screeningId
        self.timeStamp = timeStamp
        self.programVersion = programVersion
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreening.subclass:
            return XSDataISPyBScreening.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreening(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getTimeStamp(self): return self.timeStamp
    def setTimeStamp(self, timeStamp): self.timeStamp = timeStamp
    def getProgramVersion(self): return self.programVersion
    def setProgramVersion(self, programVersion): self.programVersion = programVersion
    def export(self, outfile, level, name_='XSDataISPyBScreening'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreening'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreening')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreening'):
        if self.dataCollectionId:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self.screeningId:
            self.screeningId.export(outfile, level, name_='screeningId')
        if self.timeStamp:
            self.timeStamp.export(outfile, level, name_='timeStamp')
        if self.programVersion:
            self.programVersion.export(outfile, level, name_='programVersion')
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
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
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
        if self.programVersion:
            showIndent(outfile, level)
            outfile.write('programVersion=XSDataString(\n')
            self.programVersion.exportLiteral(outfile, level, name_='programVersion')
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
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'programVersion':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setProgramVersion(obj_)
# end class XSDataISPyBScreening


class XSDatadbstatus(XSData):
    subclass = None
    def __init__(self, screeningId=-1, screeningInputId=-1, screeningOutputId=-1, screeningOutputLatticeId=-1, screeningStrategyId=-1, screeningRankId=-1, screeningRankSetId=-1, dataCollectionId=-1, code='', message=''):
        XSData.__init__(self)
        self.screeningId = screeningId
        self.screeningInputId = screeningInputId
        self.screeningOutputId = screeningOutputId
        self.screeningOutputLatticeId = screeningOutputLatticeId
        self.screeningStrategyId = screeningStrategyId
        self.screeningRankId = screeningRankId
        self.screeningRankSetId = screeningRankSetId
        self.dataCollectionId = dataCollectionId
        self.code = code
        self.message = message
    def factory(*args_, **kwargs_):
        if XSDatadbstatus.subclass:
            return XSDatadbstatus.subclass(*args_, **kwargs_)
        else:
            return XSDatadbstatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningId(self): return self.screeningId
    def setScreeningId(self, screeningId): self.screeningId = screeningId
    def getScreeningInputId(self): return self.screeningInputId
    def setScreeningInputId(self, screeningInputId): self.screeningInputId = screeningInputId
    def getScreeningOutputId(self): return self.screeningOutputId
    def setScreeningOutputId(self, screeningOutputId): self.screeningOutputId = screeningOutputId
    def getScreeningOutputLatticeId(self): return self.screeningOutputLatticeId
    def setScreeningOutputLatticeId(self, screeningOutputLatticeId): self.screeningOutputLatticeId = screeningOutputLatticeId
    def getScreeningStrategyId(self): return self.screeningStrategyId
    def setScreeningStrategyId(self, screeningStrategyId): self.screeningStrategyId = screeningStrategyId
    def getScreeningRankId(self): return self.screeningRankId
    def setScreeningRankId(self, screeningRankId): self.screeningRankId = screeningRankId
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
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
        outfile.write('<screeningId>%d</screeningId>\n' % self.getScreeningId())
        showIndent(outfile, level)
        outfile.write('<screeningInputId>%d</screeningInputId>\n' % self.getScreeningInputId())
        showIndent(outfile, level)
        outfile.write('<screeningOutputId>%d</screeningOutputId>\n' % self.getScreeningOutputId())
        showIndent(outfile, level)
        outfile.write('<screeningOutputLatticeId>%d</screeningOutputLatticeId>\n' % self.getScreeningOutputLatticeId())
        showIndent(outfile, level)
        outfile.write('<screeningStrategyId>%d</screeningStrategyId>\n' % self.getScreeningStrategyId())
        showIndent(outfile, level)
        outfile.write('<screeningRankId>%d</screeningRankId>\n' % self.getScreeningRankId())
        showIndent(outfile, level)
        outfile.write('<screeningRankSetId>%d</screeningRankSetId>\n' % self.getScreeningRankSetId())
        showIndent(outfile, level)
        outfile.write('<dataCollectionId>%d</dataCollectionId>\n' % self.getDataCollectionId())
        showIndent(outfile, level)
        outfile.write('<code>%s</code>\n' % quote_xml(self.getCode()))
        showIndent(outfile, level)
        outfile.write('<message>%s</message>\n' % quote_xml(self.getMessage()))
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
        outfile.write('screeningId=%d,\n' % self.getScreeningId())
        showIndent(outfile, level)
        outfile.write('screeningInputId=%d,\n' % self.getScreeningInputId())
        showIndent(outfile, level)
        outfile.write('screeningOutputId=%d,\n' % self.getScreeningOutputId())
        showIndent(outfile, level)
        outfile.write('screeningOutputLatticeId=%d,\n' % self.getScreeningOutputLatticeId())
        showIndent(outfile, level)
        outfile.write('screeningStrategyId=%d,\n' % self.getScreeningStrategyId())
        showIndent(outfile, level)
        outfile.write('screeningRankId=%d,\n' % self.getScreeningRankId())
        showIndent(outfile, level)
        outfile.write('screeningRankSetId=%d,\n' % self.getScreeningRankSetId())
        showIndent(outfile, level)
        outfile.write('dataCollectionId=%d,\n' % self.getDataCollectionId())
        showIndent(outfile, level)
        outfile.write('code=%s,\n' % quote_python(self.getCode()))
        showIndent(outfile, level)
        outfile.write('message=%s,\n' % quote_python(self.getMessage()))
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
            nodeName_ == 'screeningStrategyId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.screeningStrategyId = ival_
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
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.dataCollectionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            code_ = ''
            for text__content_ in child_.childNodes:
                code_ += text__content_.nodeValue
            self.code = code_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            message_ = ''
            for text__content_ in child_.childNodes:
                message_ += text__content_.nodeValue
            self.message = message_
# end class XSDatadbstatus


class XSDataISPyBScreeningRankSet(XSData):
    subclass = None
    def __init__(self, screeningRankSetId=None, rankEngine=None, rankingProjectFileName=None, rankingSummaryFileName=None):
        XSData.__init__(self)
        self.screeningRankSetId = screeningRankSetId
        self.rankEngine = rankEngine
        self.rankingProjectFileName = rankingProjectFileName
        self.rankingSummaryFileName = rankingSummaryFileName
    def factory(*args_, **kwargs_):
        if XSDataISPyBScreeningRankSet.subclass:
            return XSDataISPyBScreeningRankSet.subclass(*args_, **kwargs_)
        else:
            return XSDataISPyBScreeningRankSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningRankSetId(self): return self.screeningRankSetId
    def setScreeningRankSetId(self, screeningRankSetId): self.screeningRankSetId = screeningRankSetId
    def getRankEngine(self): return self.rankEngine
    def setRankEngine(self, rankEngine): self.rankEngine = rankEngine
    def getRankingProjectFileName(self): return self.rankingProjectFileName
    def setRankingProjectFileName(self, rankingProjectFileName): self.rankingProjectFileName = rankingProjectFileName
    def getRankingSummaryFileName(self): return self.rankingSummaryFileName
    def setRankingSummaryFileName(self, rankingSummaryFileName): self.rankingSummaryFileName = rankingSummaryFileName
    def export(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataISPyBScreeningRankSet')
    def exportChildren(self, outfile, level, name_='XSDataISPyBScreeningRankSet'):
        if self.screeningRankSetId:
            self.screeningRankSetId.export(outfile, level, name_='screeningRankSetId')
        if self.rankEngine:
            self.rankEngine.export(outfile, level, name_='rankEngine')
        if self.rankingProjectFileName:
            self.rankingProjectFileName.export(outfile, level, name_='rankingProjectFileName')
        if self.rankingSummaryFileName:
            self.rankingSummaryFileName.export(outfile, level, name_='rankingSummaryFileName')
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
        if self.screeningRankSetId:
            showIndent(outfile, level)
            outfile.write('screeningRankSetId=XSDataInteger(\n')
            self.screeningRankSetId.exportLiteral(outfile, level, name_='screeningRankSetId')
            showIndent(outfile, level)
            outfile.write('),\n')
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
            nodeName_ == 'screeningRankSetId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setScreeningRankSetId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
# end class XSDataISPyBScreeningRankSet


class XSDataResultStatus(XSData):
    subclass = None
    def __init__(self, screeningObject=None, code=None, message=None):
        XSData.__init__(self)
        self.screeningObject = screeningObject
        self.code = code
        self.message = message
    def factory(*args_, **kwargs_):
        if XSDataResultStatus.subclass:
            return XSDataResultStatus.subclass(*args_, **kwargs_)
        else:
            return XSDataResultStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreeningObject(self): return self.screeningObject
    def setScreeningObject(self, screeningObject): self.screeningObject = screeningObject
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
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
        if self.screeningObject:
            self.screeningObject.export(outfile, level, name_='screeningObject')
        if self.code:
            self.code.export(outfile, level, name_='code')
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
        if self.screeningObject:
            showIndent(outfile, level)
            outfile.write('screeningObject=XSData(\n')
            self.screeningObject.exportLiteral(outfile, level, name_='screeningObject')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.code:
            showIndent(outfile, level)
            outfile.write('code=XSDataString(\n')
            self.code.exportLiteral(outfile, level, name_='code')
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
            nodeName_ == 'screeningObject':
            obj_ = XSData.factory()
            obj_.build(child_)
            self.setScreeningObject(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMessage(obj_)
# end class XSDataResultStatus


class XSDataInputISPyB(XSDataInput):
    subclass = None
    def __init__(self, screening=None, screeningInput=None, screeningOutput=None, screeningRank=None, screeningRankSet=None, screeningOutputLattice=None, screeningStrategy=None, image=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.screening = screening
        self.screeningInput = screeningInput
        self.screeningOutput = screeningOutput
        self.screeningRank = screeningRank
        self.screeningRankSet = screeningRankSet
        self.screeningOutputLattice = screeningOutputLattice
        self.screeningStrategy = screeningStrategy
        self.image = image
    def factory(*args_, **kwargs_):
        if XSDataInputISPyB.subclass:
            return XSDataInputISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataInputISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getScreening(self): return self.screening
    def setScreening(self, screening): self.screening = screening
    def getScreeningInput(self): return self.screeningInput
    def setScreeningInput(self, screeningInput): self.screeningInput = screeningInput
    def getScreeningOutput(self): return self.screeningOutput
    def setScreeningOutput(self, screeningOutput): self.screeningOutput = screeningOutput
    def getScreeningRank(self): return self.screeningRank
    def setScreeningRank(self, screeningRank): self.screeningRank = screeningRank
    def getScreeningRankSet(self): return self.screeningRankSet
    def setScreeningRankSet(self, screeningRankSet): self.screeningRankSet = screeningRankSet
    def getScreeningOutputLattice(self): return self.screeningOutputLattice
    def setScreeningOutputLattice(self, screeningOutputLattice): self.screeningOutputLattice = screeningOutputLattice
    def getScreeningStrategy(self): return self.screeningStrategy
    def setScreeningStrategy(self, screeningStrategy): self.screeningStrategy = screeningStrategy
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def export(self, outfile, level, name_='XSDataInputISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputISPyB'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputISPyB')
    def exportChildren(self, outfile, level, name_='XSDataInputISPyB'):
        if self.screening:
            self.screening.export(outfile, level, name_='screening')
        if self.screeningInput:
            self.screeningInput.export(outfile, level, name_='screeningInput')
        if self.screeningOutput:
            self.screeningOutput.export(outfile, level, name_='screeningOutput')
        if self.screeningRank:
            self.screeningRank.export(outfile, level, name_='screeningRank')
        if self.screeningRankSet:
            self.screeningRankSet.export(outfile, level, name_='screeningRankSet')
        if self.screeningOutputLattice:
            self.screeningOutputLattice.export(outfile, level, name_='screeningOutputLattice')
        if self.screeningStrategy:
            self.screeningStrategy.export(outfile, level, name_='screeningStrategy')
        if self.image:
            self.image.export(outfile, level, name_='image')
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
        if self.screening:
            showIndent(outfile, level)
            outfile.write('screening=XSDataISPyBScreening(\n')
            self.screening.exportLiteral(outfile, level, name_='screening')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningInput:
            showIndent(outfile, level)
            outfile.write('screeningInput=XSDataISPyBScreeningInput(\n')
            self.screeningInput.exportLiteral(outfile, level, name_='screeningInput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutput:
            showIndent(outfile, level)
            outfile.write('screeningOutput=XSDataISPyBScreeningOutput(\n')
            self.screeningOutput.exportLiteral(outfile, level, name_='screeningOutput')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningRank:
            showIndent(outfile, level)
            outfile.write('screeningRank=XSDataISPyBScreeningRank(\n')
            self.screeningRank.exportLiteral(outfile, level, name_='screeningRank')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningRankSet:
            showIndent(outfile, level)
            outfile.write('screeningRankSet=XSDataISPyBScreeningRankSet(\n')
            self.screeningRankSet.exportLiteral(outfile, level, name_='screeningRankSet')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningOutputLattice:
            showIndent(outfile, level)
            outfile.write('screeningOutputLattice=XSDataISPyBScreeningOutputLattice(\n')
            self.screeningOutputLattice.exportLiteral(outfile, level, name_='screeningOutputLattice')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.screeningStrategy:
            showIndent(outfile, level)
            outfile.write('screeningStrategy=XSDataISPyBScreeningStrategy(\n')
            self.screeningStrategy.exportLiteral(outfile, level, name_='screeningStrategy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.image:
            showIndent(outfile, level)
            outfile.write('image=XSDataISPyBImage(\n')
            self.image.exportLiteral(outfile, level, name_='image')
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
            nodeName_ == 'screening':
            obj_ = XSDataISPyBScreening.factory()
            obj_.build(child_)
            self.setScreening(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningInput':
            obj_ = XSDataISPyBScreeningInput.factory()
            obj_.build(child_)
            self.setScreeningInput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutput':
            obj_ = XSDataISPyBScreeningOutput.factory()
            obj_.build(child_)
            self.setScreeningOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRank':
            obj_ = XSDataISPyBScreeningRank.factory()
            obj_.build(child_)
            self.setScreeningRank(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningRankSet':
            obj_ = XSDataISPyBScreeningRankSet.factory()
            obj_.build(child_)
            self.setScreeningRankSet(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningOutputLattice':
            obj_ = XSDataISPyBScreeningOutputLattice.factory()
            obj_.build(child_)
            self.setScreeningOutputLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'screeningStrategy':
            obj_ = XSDataISPyBScreeningStrategy.factory()
            obj_.build(child_)
            self.setScreeningStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataISPyBImage.factory()
            obj_.build(child_)
            self.setImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputISPyB


class XSDataTime(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataTime.subclass:
            return XSDataTime.subclass(*args_, **kwargs_)
        else:
            return XSDataTime(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataTime'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataTime'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataTime')
    def exportChildren(self, outfile, level, name_='XSDataTime'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataTime


class XSDataAngle(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataAngle.subclass:
            return XSDataAngle.subclass(*args_, **kwargs_)
        else:
            return XSDataAngle(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataAngle'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngle'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAngle')
    def exportChildren(self, outfile, level, name_='XSDataAngle'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataAngle


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


class XSDataSpeed(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataSpeed.subclass:
            return XSDataSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSpeed'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSpeed')
    def exportChildren(self, outfile, level, name_='XSDataSpeed'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataSpeed


class XSDataFlux(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataFlux.subclass:
            return XSDataFlux.subclass(*args_, **kwargs_)
        else:
            return XSDataFlux(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataFlux'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFlux'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFlux')
    def exportChildren(self, outfile, level, name_='XSDataFlux'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataFlux


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


class XSDataLength(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataLength.subclass:
            return XSDataLength.subclass(*args_, **kwargs_)
        else:
            return XSDataLength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataLength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLength'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataLength')
    def exportChildren(self, outfile, level, name_='XSDataLength'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataLength


class XSDataAbsorbedDoseRate(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataAbsorbedDoseRate.subclass:
            return XSDataAbsorbedDoseRate.subclass(*args_, **kwargs_)
        else:
            return XSDataAbsorbedDoseRate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate')
    def exportChildren(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataAbsorbedDoseRate


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


class XSDataAngularSpeed(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataAngularSpeed.subclass:
            return XSDataAngularSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataAngularSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataAngularSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngularSpeed'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAngularSpeed')
    def exportChildren(self, outfile, level, name_='XSDataAngularSpeed'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataAngularSpeed


class XSDataImage(XSDataFile):
    subclass = None
    def __init__(self, date=None, number=None, path=None):
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
        if self.date:
            self.date.export(outfile, level, name_='date')
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


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxXSDataDoubleHandler(handler.ContentHandler):
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
        if name == 'XSDataDouble':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('XSDataDouble', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'value':
            stackObj = SaxStackElement('value', None)
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
        elif name == 'path':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('path', obj)
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
        elif name == 'configuration':
            obj = XSConfiguration.factory()
            stackObj = SaxStackElement('configuration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'status':
            obj = XSDataStatus.factory()
            stackObj = SaxStackElement('status', obj)
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
        elif name == 'systemInfo':
            obj = XSDataSystemInfo.factory()
            stackObj = SaxStackElement('systemInfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'workingDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('workingDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'debugInfo':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('debugInfo', obj)
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
        elif name == 'debugMessage':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('debugMessage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'errorType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('errorType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginList':
            obj = XSPluginList.factory()
            stackObj = SaxStackElement('XSPluginList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginItem':
            obj = XSPluginItem.factory()
            stackObj = SaxStackElement('XSPluginItem', obj)
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
        elif name == 'XSOptionList':
            obj = XSOptionList.factory()
            stackObj = SaxStackElement('XSOptionList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSParamList':
            obj = XSParamList.factory()
            stackObj = SaxStackElement('XSParamList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executionInfo':
            obj = XSDataExecutionInfo.factory()
            stackObj = SaxStackElement('executionInfo', obj)
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
        elif name == 'screeningOutputId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningOutputId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'statusDescription':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('statusDescription', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rejectedReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('rejectedReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolutionObtained':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('resolutionObtained', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationR':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('spotDeviationR', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationTheta':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('spotDeviationTheta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamShiftX':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamShiftX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamShiftY':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamShiftY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsFound':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsFound', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsUsed':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsUsed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numSpotsRejected':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numSpotsRejected', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('mosaicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iOverSigma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('iOverSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'diffractionRings':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('diffractionRings', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningSuccess':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('screeningSuccess', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicityEstimated':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('mosaicityEstimated', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningInputId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningInputId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamX':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamY':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rmsErrorLimits':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rmsErrorLimits', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimumFractionIndexed':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('minimumFractionIndexed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maximumFractionRejected':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('maximumFractionRejected', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimumSignalToNoise':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('minimumSignalToNoise', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollectionId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('dataCollectionId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'blSampleId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('blSampleId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sessionId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('sessionId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('experimentType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollectionNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('dataCollectionNumber', obj)
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
        elif name == 'fileName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fileLocation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileLocation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'measuredIntensity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('measuredIntensity', obj)
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
        elif name == 'temperature':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('temperature', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'cumulativeIntensity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('cumulativeIntensity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'synchrotronCurrent':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('synchrotronCurrent', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'comments':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('comments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'machineMessage':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('machineMessage', obj)
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
        elif name == 'rankValue':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rankValue', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankInformation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rankInformation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutputLatticeId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningOutputLatticeId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategyId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('screeningStrategyId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resultStatus':
            obj = XSDataResultStatus.factory()
            stackObj = SaxStackElement('resultStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phiStart':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('phiStart', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phiEnd':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('phiEnd', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotation':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rotation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'exposureTime':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('exposureTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('resolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'completeness':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('completeness', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'multiplicity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('multiplicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'anomalous':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('anomalous', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'program':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('program', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankingResolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rankingResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spaceGroup':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('spaceGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pointGroup':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('pointGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bravaisLattice':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bravaisLattice', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_x':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_y':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_a_z':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_a_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_x':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_y':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_b_z':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_b_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_x':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_y':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rawOrientationMatrix_c_z':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rawOrientationMatrix_c_z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_a':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_a', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_b':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_b', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_c':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_c', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_alpha':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_alpha', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_beta':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_beta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell_gamma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('unitCell_gamma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'timeStamp':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('timeStamp', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'programVersion':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('programVersion', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'code':
            stackObj = SaxStackElement('code', None)
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
        elif name == 'screeningObject':
            obj = XSData.factory()
            stackObj = SaxStackElement('screeningObject', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screening':
            obj = XSDataISPyBScreening.factory()
            stackObj = SaxStackElement('screening', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningInput':
            obj = XSDataISPyBScreeningInput.factory()
            stackObj = SaxStackElement('screeningInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningOutput':
            obj = XSDataISPyBScreeningOutput.factory()
            stackObj = SaxStackElement('screeningOutput', obj)
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
        elif name == 'screeningOutputLattice':
            obj = XSDataISPyBScreeningOutputLattice.factory()
            stackObj = SaxStackElement('screeningOutputLattice', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'screeningStrategy':
            obj = XSDataISPyBScreeningStrategy.factory()
            stackObj = SaxStackElement('screeningStrategy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'image':
            obj = XSDataISPyBImage.factory()
            stackObj = SaxStackElement('image', obj)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'XSDataDouble':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'value':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"value" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setValue(content)
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
        elif name == 'm11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"m11" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m12" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m13" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m21" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m22" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m23" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m31" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m32" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"m33" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM33(content)
                self.stack.pop()
                done = 1
        elif name == 'v1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"v1" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"v2" must be integer -- content: %s' % content)
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
                        content = int(content)
                    except:
                        self.reportError('"v3" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV3(content)
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
        elif name == 'path':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPath(self.stack[-1].obj)
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
        elif name == 'configuration':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setConfiguration(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'status':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatus(self.stack[-1].obj)
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
        elif name == 'systemInfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSystemInfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'workingDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setWorkingDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'debugInfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDebugInfo(self.stack[-1].obj)
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
        elif name == 'debugMessage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDebugMessage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'errorType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setErrorType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSPluginList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSPluginList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSPluginItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSPluginItem(self.stack[-1].obj)
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
        elif name == 'XSOptionList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSOptionList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSParamList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSParamList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executionInfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutionInfo(self.stack[-1].obj)
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
        elif name == 'message':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addMessage(self.stack[-1].obj)
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
        elif name == 'screeningOutputId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutputId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'statusDescription':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatusDescription(self.stack[-1].obj)
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
        elif name == 'numSpotsFound':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsFound(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numSpotsUsed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsUsed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numSpotsRejected':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumSpotsRejected(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iOverSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'diffractionRings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDiffractionRings(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningSuccess':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningSuccess(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicityEstimated':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicityEstimated(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningInputId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningInputId(self.stack[-1].obj)
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
        elif name == 'rmsErrorLimits':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRmsErrorLimits(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minimumFractionIndexed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinimumFractionIndexed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maximumFractionRejected':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaximumFractionRejected(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minimumSignalToNoise':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinimumSignalToNoise(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollectionId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollectionId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'blSampleId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBlSampleId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sessionId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSessionId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExperimentType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollectionNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollectionNumber(self.stack[-1].obj)
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
        elif name == 'fileName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fileLocation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileLocation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'measuredIntensity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMeasuredIntensity(self.stack[-1].obj)
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
        elif name == 'temperature':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTemperature(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'cumulativeIntensity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCumulativeIntensity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'synchrotronCurrent':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSynchrotronCurrent(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'comments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setComments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'machineMessage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMachineMessage(self.stack[-1].obj)
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
        elif name == 'rankValue':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankValue(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankInformation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankInformation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputLatticeId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutputLatticeId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategyId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategyId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resultStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addResultStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'phiStart':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPhiStart(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'phiEnd':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPhiEnd(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'exposureTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExposureTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'completeness':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCompleteness(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'multiplicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMultiplicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'anomalous':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAnomalous(self.stack[-1].obj)
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
        elif name == 'spaceGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpaceGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pointGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPointGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bravaisLattice':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBravaisLattice(self.stack[-1].obj)
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
        elif name == 'unitCell_a':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_a(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_b':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_b(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_c':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_c(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_alpha':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_alpha(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_beta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_beta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell_gamma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell_gamma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'timeStamp':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTimeStamp(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'programVersion':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setProgramVersion(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'code':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCode(content)
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
        elif name == 'screeningObject':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningObject(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screening':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreening(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningInput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRank':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRank(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningRankSet':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningRankSet(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningOutputLattice':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningOutputLattice(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'screeningStrategy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScreeningStrategy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'image':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImage(self.stack[-1].obj)
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
    documentHandler = SaxXSDataDoubleHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxXSDataDoubleHandler()
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
    rootObj = XSDataDouble.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSDataDouble")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = XSDataDouble.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSDataDouble")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = XSDataDouble.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from XSDataISPyBv10 import *\n\n')
    sys.stdout.write('rootObj = XSDataDouble(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSDataDouble")
    sys.stdout.write(')\n')
    return rootObj

class XSDataISPyBv10:
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

