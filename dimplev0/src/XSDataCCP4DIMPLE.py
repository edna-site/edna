#!/usr/bin/env python

#
# Generated Mon Nov 15 17:09:36 2010 by EDGenerateDS.py.
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


class CCP4UnitCell(XSData):
    subclass = None
    def __init__(self, a=None, b=None, c=None, alpha=None, beta=None, gamma=None):
        XSData.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
    def factory(*args_, **kwargs_):
        if CCP4UnitCell.subclass:
            return CCP4UnitCell.subclass(*args_, **kwargs_)
        else:
            return CCP4UnitCell(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def export(self, outfile, level, name_='CCP4UnitCell'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4UnitCell'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4UnitCell')
    def exportChildren(self, outfile, level, name_='CCP4UnitCell'):
        if self.a:
            self.a.export(outfile, level, name_='a')
        if self.b:
            self.b.export(outfile, level, name_='b')
        if self.c:
            self.c.export(outfile, level, name_='c')
        if self.alpha:
            self.alpha.export(outfile, level, name_='alpha')
        if self.beta:
            self.beta.export(outfile, level, name_='beta')
        if self.gamma:
            self.gamma.export(outfile, level, name_='gamma')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4UnitCell' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4UnitCell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4UnitCell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4UnitCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4UnitCell'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
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
# end class CCP4UnitCell


class CCP4MTZColLabels(XSData):
    subclass = None
    def __init__(self, F=None, SIGF=None, IMEAN=None, SIGIMEAN=None):
        XSData.__init__(self)
        self.F = F
        self.SIGF = SIGF
        self.IMEAN = IMEAN
        self.SIGIMEAN = SIGIMEAN
    def factory(*args_, **kwargs_):
        if CCP4MTZColLabels.subclass:
            return CCP4MTZColLabels.subclass(*args_, **kwargs_)
        else:
            return CCP4MTZColLabels(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getF(self): return self.F
    def setF(self, F): self.F = F
    def getSIGF(self): return self.SIGF
    def setSIGF(self, SIGF): self.SIGF = SIGF
    def getIMEAN(self): return self.IMEAN
    def setIMEAN(self, IMEAN): self.IMEAN = IMEAN
    def getSIGIMEAN(self): return self.SIGIMEAN
    def setSIGIMEAN(self, SIGIMEAN): self.SIGIMEAN = SIGIMEAN
    def export(self, outfile, level, name_='CCP4MTZColLabels'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4MTZColLabels'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4MTZColLabels')
    def exportChildren(self, outfile, level, name_='CCP4MTZColLabels'):
        if self.F:
            self.F.export(outfile, level, name_='F')
        if self.SIGF:
            self.SIGF.export(outfile, level, name_='SIGF')
        if self.IMEAN:
            self.IMEAN.export(outfile, level, name_='IMEAN')
        if self.SIGIMEAN:
            self.SIGIMEAN.export(outfile, level, name_='SIGIMEAN')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4MTZColLabels' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4MTZColLabels.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4MTZColLabels.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4MTZColLabels" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4MTZColLabels'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.F:
            showIndent(outfile, level)
            outfile.write('F=XSDataString(\n')
            self.F.exportLiteral(outfile, level, name_='F')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SIGF:
            showIndent(outfile, level)
            outfile.write('SIGF=XSDataString(\n')
            self.SIGF.exportLiteral(outfile, level, name_='SIGF')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.IMEAN:
            showIndent(outfile, level)
            outfile.write('IMEAN=XSDataString(\n')
            self.IMEAN.exportLiteral(outfile, level, name_='IMEAN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SIGIMEAN:
            showIndent(outfile, level)
            outfile.write('SIGIMEAN=XSDataString(\n')
            self.SIGIMEAN.exportLiteral(outfile, level, name_='SIGIMEAN')
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
            nodeName_ == 'F':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setF(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SIGF':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSIGF(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'IMEAN':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setIMEAN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SIGIMEAN':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSIGIMEAN(obj_)
# end class CCP4MTZColLabels


class CCP4SymmetryOperation(XSData):
    subclass = None
    def __init__(self, symmetryOperation=None, symmetryMatrix=None):
        XSData.__init__(self)
        self.symmetryOperation = symmetryOperation
        self.symmetryMatrix = symmetryMatrix
    def factory(*args_, **kwargs_):
        if CCP4SymmetryOperation.subclass:
            return CCP4SymmetryOperation.subclass(*args_, **kwargs_)
        else:
            return CCP4SymmetryOperation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSymmetryOperation(self): return self.symmetryOperation
    def setSymmetryOperation(self, symmetryOperation): self.symmetryOperation = symmetryOperation
    def getSymmetryMatrix(self): return self.symmetryMatrix
    def setSymmetryMatrix(self, symmetryMatrix): self.symmetryMatrix = symmetryMatrix
    def export(self, outfile, level, name_='CCP4SymmetryOperation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4SymmetryOperation'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4SymmetryOperation')
    def exportChildren(self, outfile, level, name_='CCP4SymmetryOperation'):
        if self.symmetryOperation:
            self.symmetryOperation.export(outfile, level, name_='symmetryOperation')
        if self.symmetryMatrix:
            self.symmetryMatrix.export(outfile, level, name_='symmetryMatrix')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4SymmetryOperation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4SymmetryOperation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4SymmetryOperation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4SymmetryOperation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4SymmetryOperation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.symmetryOperation:
            showIndent(outfile, level)
            outfile.write('symmetryOperation=XSDataString(\n')
            self.symmetryOperation.exportLiteral(outfile, level, name_='symmetryOperation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.symmetryMatrix:
            showIndent(outfile, level)
            outfile.write('symmetryMatrix=CCP4RTMatrix(\n')
            self.symmetryMatrix.exportLiteral(outfile, level, name_='symmetryMatrix')
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
            nodeName_ == 'symmetryOperation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymmetryOperation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetryMatrix':
            obj_ = CCP4RTMatrix.factory()
            obj_.build(child_)
            self.setSymmetryMatrix(obj_)
# end class CCP4SymmetryOperation


class CCP4RTMatrix(XSData):
    subclass = None
    def __init__(self, e11=None, e12=None, e13=None, e21=None, e22=None, e23=None, e31=None, e32=None, e33=None, e41=None, e42=None, e43=None):
        XSData.__init__(self)
        self.e11 = e11
        self.e12 = e12
        self.e13 = e13
        self.e21 = e21
        self.e22 = e22
        self.e23 = e23
        self.e31 = e31
        self.e32 = e32
        self.e33 = e33
        self.e41 = e41
        self.e42 = e42
        self.e43 = e43
    def factory(*args_, **kwargs_):
        if CCP4RTMatrix.subclass:
            return CCP4RTMatrix.subclass(*args_, **kwargs_)
        else:
            return CCP4RTMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getE11(self): return self.e11
    def setE11(self, e11): self.e11 = e11
    def getE12(self): return self.e12
    def setE12(self, e12): self.e12 = e12
    def getE13(self): return self.e13
    def setE13(self, e13): self.e13 = e13
    def getE21(self): return self.e21
    def setE21(self, e21): self.e21 = e21
    def getE22(self): return self.e22
    def setE22(self, e22): self.e22 = e22
    def getE23(self): return self.e23
    def setE23(self, e23): self.e23 = e23
    def getE31(self): return self.e31
    def setE31(self, e31): self.e31 = e31
    def getE32(self): return self.e32
    def setE32(self, e32): self.e32 = e32
    def getE33(self): return self.e33
    def setE33(self, e33): self.e33 = e33
    def getE41(self): return self.e41
    def setE41(self, e41): self.e41 = e41
    def getE42(self): return self.e42
    def setE42(self, e42): self.e42 = e42
    def getE43(self): return self.e43
    def setE43(self, e43): self.e43 = e43
    def export(self, outfile, level, name_='CCP4RTMatrix'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4RTMatrix'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4RTMatrix')
    def exportChildren(self, outfile, level, name_='CCP4RTMatrix'):
        if self.e11:
            self.e11.export(outfile, level, name_='e11')
        if self.e12:
            self.e12.export(outfile, level, name_='e12')
        if self.e13:
            self.e13.export(outfile, level, name_='e13')
        if self.e21:
            self.e21.export(outfile, level, name_='e21')
        if self.e22:
            self.e22.export(outfile, level, name_='e22')
        if self.e23:
            self.e23.export(outfile, level, name_='e23')
        if self.e31:
            self.e31.export(outfile, level, name_='e31')
        if self.e32:
            self.e32.export(outfile, level, name_='e32')
        if self.e33:
            self.e33.export(outfile, level, name_='e33')
        if self.e41:
            self.e41.export(outfile, level, name_='e41')
        if self.e42:
            self.e42.export(outfile, level, name_='e42')
        if self.e43:
            self.e43.export(outfile, level, name_='e43')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4RTMatrix' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4RTMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4RTMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4RTMatrix" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4RTMatrix'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.e11:
            showIndent(outfile, level)
            outfile.write('e11=XSDataFloat(\n')
            self.e11.exportLiteral(outfile, level, name_='e11')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e12:
            showIndent(outfile, level)
            outfile.write('e12=XSDataFloat(\n')
            self.e12.exportLiteral(outfile, level, name_='e12')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e13:
            showIndent(outfile, level)
            outfile.write('e13=XSDataFloat(\n')
            self.e13.exportLiteral(outfile, level, name_='e13')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e21:
            showIndent(outfile, level)
            outfile.write('e21=XSDataFloat(\n')
            self.e21.exportLiteral(outfile, level, name_='e21')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e22:
            showIndent(outfile, level)
            outfile.write('e22=XSDataFloat(\n')
            self.e22.exportLiteral(outfile, level, name_='e22')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e23:
            showIndent(outfile, level)
            outfile.write('e23=XSDataFloat(\n')
            self.e23.exportLiteral(outfile, level, name_='e23')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e31:
            showIndent(outfile, level)
            outfile.write('e31=XSDataFloat(\n')
            self.e31.exportLiteral(outfile, level, name_='e31')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e32:
            showIndent(outfile, level)
            outfile.write('e32=XSDataFloat(\n')
            self.e32.exportLiteral(outfile, level, name_='e32')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e33:
            showIndent(outfile, level)
            outfile.write('e33=XSDataFloat(\n')
            self.e33.exportLiteral(outfile, level, name_='e33')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e41:
            showIndent(outfile, level)
            outfile.write('e41=XSDataFloat(\n')
            self.e41.exportLiteral(outfile, level, name_='e41')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e42:
            showIndent(outfile, level)
            outfile.write('e42=XSDataFloat(\n')
            self.e42.exportLiteral(outfile, level, name_='e42')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.e43:
            showIndent(outfile, level)
            outfile.write('e43=XSDataFloat(\n')
            self.e43.exportLiteral(outfile, level, name_='e43')
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
            nodeName_ == 'e11':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE11(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e12':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE12(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e13':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE13(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e21':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE21(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e22':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE22(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e23':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE23(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e31':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE31(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e32':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE32(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e33':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE33(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e41':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE41(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e42':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE42(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e43':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setE43(obj_)
# end class CCP4RTMatrix


class CCP4SpaceGroup(XSData):
    subclass = None
    def __init__(self, name=None, number=None, symmetryOperations=None):
        XSData.__init__(self)
        self.name = name
        self.number = number
        if symmetryOperations is None:
            self.symmetryOperations = []
        else:
            self.symmetryOperations = symmetryOperations
    def factory(*args_, **kwargs_):
        if CCP4SpaceGroup.subclass:
            return CCP4SpaceGroup.subclass(*args_, **kwargs_)
        else:
            return CCP4SpaceGroup(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getNumber(self): return self.number
    def setNumber(self, number): self.number = number
    def getSymmetryOperations(self): return self.symmetryOperations
    def setSymmetryOperations(self, symmetryOperations): self.symmetryOperations = symmetryOperations
    def addSymmetryOperations(self, value): self.symmetryOperations.append(value)
    def insertSymmetryOperations(self, index, value): self.symmetryOperations[index] = value
    def export(self, outfile, level, name_='CCP4SpaceGroup'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4SpaceGroup'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4SpaceGroup')
    def exportChildren(self, outfile, level, name_='CCP4SpaceGroup'):
        if self.name:
            self.name.export(outfile, level, name_='name')
        if self.number:
            self.number.export(outfile, level, name_='number')
        for symmetryOperations_ in self.getSymmetryOperations():
            symmetryOperations_.export(outfile, level, name_='symmetryOperations')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4SpaceGroup' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4SpaceGroup.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4SpaceGroup.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4SpaceGroup" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4SpaceGroup'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.name:
            showIndent(outfile, level)
            outfile.write('name=XSDataString(\n')
            self.name.exportLiteral(outfile, level, name_='name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.number:
            showIndent(outfile, level)
            outfile.write('number=XSDataInteger(\n')
            self.number.exportLiteral(outfile, level, name_='number')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('symmetryOperations=[\n')
        level += 1
        for symmetryOperations in self.symmetryOperations:
            showIndent(outfile, level)
            outfile.write('CCP4SymmetryOperation(\n')
            symmetryOperations.exportLiteral(outfile, level, name_='symmetryOperations')
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
            nodeName_ == 'name':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetryOperations':
            obj_ = CCP4SymmetryOperation.factory()
            obj_.build(child_)
            self.symmetryOperations.append(obj_)
# end class CCP4SpaceGroup


class CCP4ResolutionLimit(XSData):
    subclass = None
    def __init__(self, resolution=None):
        XSData.__init__(self)
        self.resolution = resolution
    def factory(*args_, **kwargs_):
        if CCP4ResolutionLimit.subclass:
            return CCP4ResolutionLimit.subclass(*args_, **kwargs_)
        else:
            return CCP4ResolutionLimit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def export(self, outfile, level, name_='CCP4ResolutionLimit'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4ResolutionLimit'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4ResolutionLimit')
    def exportChildren(self, outfile, level, name_='CCP4ResolutionLimit'):
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4ResolutionLimit' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4ResolutionLimit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4ResolutionLimit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4ResolutionLimit" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4ResolutionLimit'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataFloat(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
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
            nodeName_ == 'resolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setResolution(obj_)
# end class CCP4ResolutionLimit


class HKL(XSData):
    subclass = None
    def __init__(self, path=None):
        XSData.__init__(self)
        self.path = path
    def factory(*args_, **kwargs_):
        if HKL.subclass:
            return HKL.subclass(*args_, **kwargs_)
        else:
            return HKL(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPath(self): return self.path
    def setPath(self, path): self.path = path
    def export(self, outfile, level, name_='HKL'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='HKL'):
        XSData.exportAttributes(self, outfile, level, name_='HKL')
    def exportChildren(self, outfile, level, name_='HKL'):
        if self.path:
            self.path.export(outfile, level, name_='path')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='HKL' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = HKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = HKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="HKL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='HKL'):
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
# end class HKL


class XYZ(XSData):
    subclass = None
    def __init__(self, path=None):
        XSData.__init__(self)
        self.path = path
    def factory(*args_, **kwargs_):
        if XYZ.subclass:
            return XYZ.subclass(*args_, **kwargs_)
        else:
            return XYZ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPath(self): return self.path
    def setPath(self, path): self.path = path
    def export(self, outfile, level, name_='XYZ'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XYZ'):
        XSData.exportAttributes(self, outfile, level, name_='XYZ')
    def exportChildren(self, outfile, level, name_='XYZ'):
        if self.path:
            self.path.export(outfile, level, name_='path')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XYZ' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XYZ" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XYZ'):
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
# end class XYZ


class CCP4Sequence(XSData):
    subclass = None
    def __init__(self, oneLetterCode=None, numberOfResidues=None, molecularMass=None):
        XSData.__init__(self)
        self.oneLetterCode = oneLetterCode
        self.numberOfResidues = numberOfResidues
        self.molecularMass = molecularMass
    def factory(*args_, **kwargs_):
        if CCP4Sequence.subclass:
            return CCP4Sequence.subclass(*args_, **kwargs_)
        else:
            return CCP4Sequence(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOneLetterCode(self): return self.oneLetterCode
    def setOneLetterCode(self, oneLetterCode): self.oneLetterCode = oneLetterCode
    def getNumberOfResidues(self): return self.numberOfResidues
    def setNumberOfResidues(self, numberOfResidues): self.numberOfResidues = numberOfResidues
    def getMolecularMass(self): return self.molecularMass
    def setMolecularMass(self, molecularMass): self.molecularMass = molecularMass
    def export(self, outfile, level, name_='CCP4Sequence'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4Sequence'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4Sequence')
    def exportChildren(self, outfile, level, name_='CCP4Sequence'):
        if self.oneLetterCode:
            self.oneLetterCode.export(outfile, level, name_='oneLetterCode')
        if self.numberOfResidues:
            self.numberOfResidues.export(outfile, level, name_='numberOfResidues')
        if self.molecularMass:
            self.molecularMass.export(outfile, level, name_='molecularMass')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4Sequence' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4Sequence.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4Sequence.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4Sequence" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4Sequence'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.oneLetterCode:
            showIndent(outfile, level)
            outfile.write('oneLetterCode=XSDataString(\n')
            self.oneLetterCode.exportLiteral(outfile, level, name_='oneLetterCode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfResidues:
            showIndent(outfile, level)
            outfile.write('numberOfResidues=XSDataInteger(\n')
            self.numberOfResidues.exportLiteral(outfile, level, name_='numberOfResidues')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.molecularMass:
            showIndent(outfile, level)
            outfile.write('molecularMass=XSDataFloat(\n')
            self.molecularMass.exportLiteral(outfile, level, name_='molecularMass')
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
            nodeName_ == 'oneLetterCode':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOneLetterCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfResidues':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfResidues(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'molecularMass':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMolecularMass(obj_)
# end class CCP4Sequence


class CCP4ReindexingOperation(XSData):
    subclass = None
    def __init__(self, ReindexingOperation=None, ReindexingMatrix=None):
        XSData.__init__(self)
        self.ReindexingOperation = ReindexingOperation
        self.ReindexingMatrix = ReindexingMatrix
    def factory(*args_, **kwargs_):
        if CCP4ReindexingOperation.subclass:
            return CCP4ReindexingOperation.subclass(*args_, **kwargs_)
        else:
            return CCP4ReindexingOperation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getReindexingOperation(self): return self.ReindexingOperation
    def setReindexingOperation(self, ReindexingOperation): self.ReindexingOperation = ReindexingOperation
    def getReindexingMatrix(self): return self.ReindexingMatrix
    def setReindexingMatrix(self, ReindexingMatrix): self.ReindexingMatrix = ReindexingMatrix
    def export(self, outfile, level, name_='CCP4ReindexingOperation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4ReindexingOperation'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4ReindexingOperation')
    def exportChildren(self, outfile, level, name_='CCP4ReindexingOperation'):
        if self.ReindexingOperation:
            self.ReindexingOperation.export(outfile, level, name_='ReindexingOperation')
        if self.ReindexingMatrix:
            self.ReindexingMatrix.export(outfile, level, name_='ReindexingMatrix')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4ReindexingOperation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4ReindexingOperation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4ReindexingOperation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4ReindexingOperation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4ReindexingOperation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ReindexingOperation:
            showIndent(outfile, level)
            outfile.write('ReindexingOperation=XSDataString(\n')
            self.ReindexingOperation.exportLiteral(outfile, level, name_='ReindexingOperation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ReindexingMatrix:
            showIndent(outfile, level)
            outfile.write('ReindexingMatrix=CCP4RTMatrix(\n')
            self.ReindexingMatrix.exportLiteral(outfile, level, name_='ReindexingMatrix')
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
            nodeName_ == 'ReindexingOperation':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setReindexingOperation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ReindexingMatrix':
            obj_ = CCP4RTMatrix.factory()
            obj_.build(child_)
            self.setReindexingMatrix(obj_)
# end class CCP4ReindexingOperation


class CCP4ReturnStatus(XSData):
    subclass = None
    def __init__(self, code=None, message=None):
        XSData.__init__(self)
        self.code = code
        self.message = message
    def factory(*args_, **kwargs_):
        if CCP4ReturnStatus.subclass:
            return CCP4ReturnStatus.subclass(*args_, **kwargs_)
        else:
            return CCP4ReturnStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def export(self, outfile, level, name_='CCP4ReturnStatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4ReturnStatus'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4ReturnStatus')
    def exportChildren(self, outfile, level, name_='CCP4ReturnStatus'):
        if self.code:
            self.code.export(outfile, level, name_='code')
        if self.message:
            self.message.export(outfile, level, name_='message')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4ReturnStatus' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4ReturnStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4ReturnStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4ReturnStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4ReturnStatus'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.code:
            showIndent(outfile, level)
            outfile.write('code=XSDataInteger(\n')
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
            nodeName_ == 'code':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMessage(obj_)
# end class CCP4ReturnStatus


class CCP4LogFile(XSData):
    subclass = None
    def __init__(self, path=None):
        XSData.__init__(self)
        self.path = path
    def factory(*args_, **kwargs_):
        if CCP4LogFile.subclass:
            return CCP4LogFile.subclass(*args_, **kwargs_)
        else:
            return CCP4LogFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPath(self): return self.path
    def setPath(self, path): self.path = path
    def export(self, outfile, level, name_='CCP4LogFile'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4LogFile'):
        XSData.exportAttributes(self, outfile, level, name_='CCP4LogFile')
    def exportChildren(self, outfile, level, name_='CCP4LogFile'):
        if self.path:
            self.path.export(outfile, level, name_='path')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4LogFile' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4LogFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4LogFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4LogFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4LogFile'):
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
# end class CCP4LogFile


class CCP4DataInputMTZDUMP(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputMTZDUMP.subclass:
            return CCP4DataInputMTZDUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputMTZDUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputMTZDUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputMTZDUMP'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputMTZDUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataInputMTZDUMP'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputMTZDUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputMTZDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputMTZDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputMTZDUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputMTZDUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputMTZDUMP


class CCP4DataResultMTZDUMP(XSDataResult):
    subclass = None
    def __init__(self, spaceGroup=None, unitCell=None, upperResolutionLimit=None, lowerResolutionLimit=None, listOfColumns=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.spaceGroup = spaceGroup
        self.unitCell = unitCell
        self.upperResolutionLimit = upperResolutionLimit
        self.lowerResolutionLimit = lowerResolutionLimit
        if listOfColumns is None:
            self.listOfColumns = []
        else:
            self.listOfColumns = listOfColumns
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultMTZDUMP.subclass:
            return CCP4DataResultMTZDUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultMTZDUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getUnitCell(self): return self.unitCell
    def setUnitCell(self, unitCell): self.unitCell = unitCell
    def getUpperResolutionLimit(self): return self.upperResolutionLimit
    def setUpperResolutionLimit(self, upperResolutionLimit): self.upperResolutionLimit = upperResolutionLimit
    def getLowerResolutionLimit(self): return self.lowerResolutionLimit
    def setLowerResolutionLimit(self, lowerResolutionLimit): self.lowerResolutionLimit = lowerResolutionLimit
    def getListOfColumns(self): return self.listOfColumns
    def setListOfColumns(self, listOfColumns): self.listOfColumns = listOfColumns
    def addListOfColumns(self, value): self.listOfColumns.append(value)
    def insertListOfColumns(self, index, value): self.listOfColumns[index] = value
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultMTZDUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultMTZDUMP'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultMTZDUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataResultMTZDUMP'):
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.unitCell:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self.upperResolutionLimit:
            self.upperResolutionLimit.export(outfile, level, name_='upperResolutionLimit')
        if self.lowerResolutionLimit:
            self.lowerResolutionLimit.export(outfile, level, name_='lowerResolutionLimit')
        for listOfColumns_ in self.getListOfColumns():
            listOfColumns_.export(outfile, level, name_='listOfColumns')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultMTZDUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultMTZDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultMTZDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultMTZDUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultMTZDUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=CCP4SpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell:
            showIndent(outfile, level)
            outfile.write('unitCell=CCP4UnitCell(\n')
            self.unitCell.exportLiteral(outfile, level, name_='unitCell')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.upperResolutionLimit:
            showIndent(outfile, level)
            outfile.write('upperResolutionLimit=CCP4ResolutionLimit(\n')
            self.upperResolutionLimit.exportLiteral(outfile, level, name_='upperResolutionLimit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lowerResolutionLimit:
            showIndent(outfile, level)
            outfile.write('lowerResolutionLimit=CCP4ResolutionLimit(\n')
            self.lowerResolutionLimit.exportLiteral(outfile, level, name_='lowerResolutionLimit')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('listOfColumns=[\n')
        level += 1
        for listOfColumns in self.listOfColumns:
            showIndent(outfile, level)
            outfile.write('XSParamList(\n')
            listOfColumns.exportLiteral(outfile, level, name_='listOfColumns')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'spaceGroup':
            obj_ = CCP4SpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = CCP4UnitCell.factory()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'upperResolutionLimit':
            obj_ = CCP4ResolutionLimit.factory()
            obj_.build(child_)
            self.setUpperResolutionLimit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lowerResolutionLimit':
            obj_ = CCP4ResolutionLimit.factory()
            obj_.build(child_)
            self.setLowerResolutionLimit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'listOfColumns':
            obj_ = XSParamList.factory()
            obj_.build(child_)
            self.listOfColumns.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultMTZDUMP


class CCP4DataInputPDBDUMP(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputPDBDUMP.subclass:
            return CCP4DataInputPDBDUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputPDBDUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputPDBDUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputPDBDUMP'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputPDBDUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataInputPDBDUMP'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputPDBDUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputPDBDUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputPDBDUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputPDBDUMP


class CCP4DataResultPDBDUMP(XSDataResult):
    subclass = None
    def __init__(self, spaceGroup=None, unitCell=None, sequence=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.spaceGroup = spaceGroup
        self.unitCell = unitCell
        self.sequence = sequence
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultPDBDUMP.subclass:
            return CCP4DataResultPDBDUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultPDBDUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getUnitCell(self): return self.unitCell
    def setUnitCell(self, unitCell): self.unitCell = unitCell
    def getSequence(self): return self.sequence
    def setSequence(self, sequence): self.sequence = sequence
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultPDBDUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultPDBDUMP'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultPDBDUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataResultPDBDUMP'):
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.unitCell:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self.sequence:
            self.sequence.export(outfile, level, name_='sequence')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultPDBDUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBDUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultPDBDUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultPDBDUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=CCP4SpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell:
            showIndent(outfile, level)
            outfile.write('unitCell=CCP4UnitCell(\n')
            self.unitCell.exportLiteral(outfile, level, name_='unitCell')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sequence:
            showIndent(outfile, level)
            outfile.write('sequence=CCP4Sequence(\n')
            self.sequence.exportLiteral(outfile, level, name_='sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'spaceGroup':
            obj_ = CCP4SpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = CCP4UnitCell.factory()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sequence':
            obj_ = CCP4Sequence.factory()
            obj_.build(child_)
            self.setSequence(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultPDBDUMP


class CCP4DataInputPDBSET(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, XYZOUT=None, unitCell=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.XYZOUT = XYZOUT
        self.unitCell = unitCell
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputPDBSET.subclass:
            return CCP4DataInputPDBSET.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputPDBSET(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getUnitCell(self): return self.unitCell
    def setUnitCell(self, unitCell): self.unitCell = unitCell
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputPDBSET'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputPDBSET'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputPDBSET')
    def exportChildren(self, outfile, level, name_='CCP4DataInputPDBSET'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.unitCell:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputPDBSET' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBSET.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBSET.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputPDBSET" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputPDBSET'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell:
            showIndent(outfile, level)
            outfile.write('unitCell=CCP4UnitCell(\n')
            self.unitCell.exportLiteral(outfile, level, name_='unitCell')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = CCP4UnitCell.factory()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputPDBSET


class CCP4DataResultPDBSET(XSDataResult):
    subclass = None
    def __init__(self, XYZOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.XYZOUT = XYZOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultPDBSET.subclass:
            return CCP4DataResultPDBSET.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultPDBSET(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultPDBSET'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultPDBSET'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultPDBSET')
    def exportChildren(self, outfile, level, name_='CCP4DataResultPDBSET'):
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultPDBSET' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBSET.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBSET.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultPDBSET" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultPDBSET'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultPDBSET


class CCP4DataInputTRUNCATE(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, sequence=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.sequence = sequence
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputTRUNCATE.subclass:
            return CCP4DataInputTRUNCATE.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputTRUNCATE(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getSequence(self): return self.sequence
    def setSequence(self, sequence): self.sequence = sequence
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputTRUNCATE'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputTRUNCATE'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputTRUNCATE')
    def exportChildren(self, outfile, level, name_='CCP4DataInputTRUNCATE'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.sequence:
            self.sequence.export(outfile, level, name_='sequence')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputTRUNCATE' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputTRUNCATE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputTRUNCATE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputTRUNCATE" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputTRUNCATE'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sequence:
            showIndent(outfile, level)
            outfile.write('sequence=CCP4Sequence(\n')
            self.sequence.exportLiteral(outfile, level, name_='sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sequence':
            obj_ = CCP4Sequence.factory()
            obj_.build(child_)
            self.setSequence(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputTRUNCATE


class CCP4DataResultTRUNCATE(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, ColLabels=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.ColLabels = ColLabels
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultTRUNCATE.subclass:
            return CCP4DataResultTRUNCATE.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultTRUNCATE(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultTRUNCATE'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultTRUNCATE'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultTRUNCATE')
    def exportChildren(self, outfile, level, name_='CCP4DataResultTRUNCATE'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultTRUNCATE' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultTRUNCATE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultTRUNCATE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultTRUNCATE" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultTRUNCATE'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultTRUNCATE


class CCP4DataInputREINDEX(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, spaceGroup=None, reindexingOperation=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.spaceGroup = spaceGroup
        self.reindexingOperation = reindexingOperation
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputREINDEX.subclass:
            return CCP4DataInputREINDEX.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputREINDEX(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getReindexingOperation(self): return self.reindexingOperation
    def setReindexingOperation(self, reindexingOperation): self.reindexingOperation = reindexingOperation
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputREINDEX'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputREINDEX'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputREINDEX')
    def exportChildren(self, outfile, level, name_='CCP4DataInputREINDEX'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.reindexingOperation:
            self.reindexingOperation.export(outfile, level, name_='reindexingOperation')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputREINDEX' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREINDEX.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREINDEX.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputREINDEX" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputREINDEX'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=CCP4SpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.reindexingOperation:
            showIndent(outfile, level)
            outfile.write('reindexingOperation=CCP4SymmetryOperation(\n')
            self.reindexingOperation.exportLiteral(outfile, level, name_='reindexingOperation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = CCP4SpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reindexingOperation':
            obj_ = CCP4SymmetryOperation.factory()
            obj_.build(child_)
            self.setReindexingOperation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputREINDEX


class CCP4DataResultREINDEX(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultREINDEX.subclass:
            return CCP4DataResultREINDEX.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultREINDEX(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultREINDEX'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultREINDEX'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultREINDEX')
    def exportChildren(self, outfile, level, name_='CCP4DataResultREINDEX'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultREINDEX' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREINDEX.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREINDEX.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultREINDEX" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultREINDEX'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultREINDEX


class CCP4DataInputUNIQUE(XSDataInput):
    subclass = None
    def __init__(self, HKLOUT=None, spaceGroup=None, unitCell=None, resolutionLimit=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLOUT = HKLOUT
        self.spaceGroup = spaceGroup
        self.unitCell = unitCell
        self.resolutionLimit = resolutionLimit
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputUNIQUE.subclass:
            return CCP4DataInputUNIQUE.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputUNIQUE(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getUnitCell(self): return self.unitCell
    def setUnitCell(self, unitCell): self.unitCell = unitCell
    def getResolutionLimit(self): return self.resolutionLimit
    def setResolutionLimit(self, resolutionLimit): self.resolutionLimit = resolutionLimit
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputUNIQUE'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputUNIQUE'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputUNIQUE')
    def exportChildren(self, outfile, level, name_='CCP4DataInputUNIQUE'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.unitCell:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self.resolutionLimit:
            self.resolutionLimit.export(outfile, level, name_='resolutionLimit')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputUNIQUE' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputUNIQUE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputUNIQUE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputUNIQUE" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputUNIQUE'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=CCP4SpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.unitCell:
            showIndent(outfile, level)
            outfile.write('unitCell=CCP4UnitCell(\n')
            self.unitCell.exportLiteral(outfile, level, name_='unitCell')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolutionLimit:
            showIndent(outfile, level)
            outfile.write('resolutionLimit=CCP4ResolutionLimit(\n')
            self.resolutionLimit.exportLiteral(outfile, level, name_='resolutionLimit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = CCP4SpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = CCP4UnitCell.factory()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionLimit':
            obj_ = CCP4ResolutionLimit.factory()
            obj_.build(child_)
            self.setResolutionLimit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputUNIQUE


class CCP4DataResultUNIQUE(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultUNIQUE.subclass:
            return CCP4DataResultUNIQUE.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultUNIQUE(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultUNIQUE'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultUNIQUE'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultUNIQUE')
    def exportChildren(self, outfile, level, name_='CCP4DataResultUNIQUE'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultUNIQUE' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultUNIQUE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultUNIQUE.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultUNIQUE" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultUNIQUE'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultUNIQUE


class CCP4DataInputFREERFLAG(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputFREERFLAG.subclass:
            return CCP4DataInputFREERFLAG.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputFREERFLAG(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputFREERFLAG'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputFREERFLAG'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputFREERFLAG')
    def exportChildren(self, outfile, level, name_='CCP4DataInputFREERFLAG'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputFREERFLAG' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputFREERFLAG.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputFREERFLAG.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputFREERFLAG" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputFREERFLAG'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputFREERFLAG


class CCP4DataResultFREERFLAG(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultFREERFLAG.subclass:
            return CCP4DataResultFREERFLAG.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultFREERFLAG(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultFREERFLAG'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultFREERFLAG'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultFREERFLAG')
    def exportChildren(self, outfile, level, name_='CCP4DataResultFREERFLAG'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultFREERFLAG' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultFREERFLAG.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultFREERFLAG.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultFREERFLAG" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultFREERFLAG'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultFREERFLAG


class CCP4DataInputREFMACRigidBody(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, XYZOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.XYZOUT = XYZOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputREFMACRigidBody.subclass:
            return CCP4DataInputREFMACRigidBody.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputREFMACRigidBody(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputREFMACRigidBody'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputREFMACRigidBody'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputREFMACRigidBody')
    def exportChildren(self, outfile, level, name_='CCP4DataInputREFMACRigidBody'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputREFMACRigidBody' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREFMACRigidBody.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREFMACRigidBody.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputREFMACRigidBody" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputREFMACRigidBody'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputREFMACRigidBody


class CCP4DataResultREFMACRigidBody(XSDataResult):
    subclass = None
    def __init__(self, XYZOUT=None, initialR=None, initialRFree=None, finalR=None, finalRFree=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.XYZOUT = XYZOUT
        self.initialR = initialR
        self.initialRFree = initialRFree
        self.finalR = finalR
        self.finalRFree = finalRFree
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultREFMACRigidBody.subclass:
            return CCP4DataResultREFMACRigidBody.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultREFMACRigidBody(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getInitialR(self): return self.initialR
    def setInitialR(self, initialR): self.initialR = initialR
    def getInitialRFree(self): return self.initialRFree
    def setInitialRFree(self, initialRFree): self.initialRFree = initialRFree
    def getFinalR(self): return self.finalR
    def setFinalR(self, finalR): self.finalR = finalR
    def getFinalRFree(self): return self.finalRFree
    def setFinalRFree(self, finalRFree): self.finalRFree = finalRFree
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultREFMACRigidBody'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultREFMACRigidBody'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultREFMACRigidBody')
    def exportChildren(self, outfile, level, name_='CCP4DataResultREFMACRigidBody'):
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.initialR:
            self.initialR.export(outfile, level, name_='initialR')
        if self.initialRFree:
            self.initialRFree.export(outfile, level, name_='initialRFree')
        if self.finalR:
            self.finalR.export(outfile, level, name_='finalR')
        if self.finalRFree:
            self.finalRFree.export(outfile, level, name_='finalRFree')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultREFMACRigidBody' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREFMACRigidBody.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREFMACRigidBody.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultREFMACRigidBody" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultREFMACRigidBody'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialR:
            showIndent(outfile, level)
            outfile.write('initialR=XSDataFloat(\n')
            self.initialR.exportLiteral(outfile, level, name_='initialR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialRFree:
            showIndent(outfile, level)
            outfile.write('initialRFree=XSDataFloat(\n')
            self.initialRFree.exportLiteral(outfile, level, name_='initialRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalR:
            showIndent(outfile, level)
            outfile.write('finalR=XSDataFloat(\n')
            self.finalR.exportLiteral(outfile, level, name_='finalR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalRFree:
            showIndent(outfile, level)
            outfile.write('finalRFree=XSDataFloat(\n')
            self.finalRFree.exportLiteral(outfile, level, name_='finalRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultREFMACRigidBody


class CCP4DataInputREFMACRestrainedRefinement(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, HKLOUT=None, XYZOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputREFMACRestrainedRefinement.subclass:
            return CCP4DataInputREFMACRestrainedRefinement.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputREFMACRestrainedRefinement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputREFMACRestrainedRefinement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputREFMACRestrainedRefinement'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputREFMACRestrainedRefinement')
    def exportChildren(self, outfile, level, name_='CCP4DataInputREFMACRestrainedRefinement'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputREFMACRestrainedRefinement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREFMACRestrainedRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputREFMACRestrainedRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputREFMACRestrainedRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputREFMACRestrainedRefinement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputREFMACRestrainedRefinement


class CCP4DataResultREFMACRestrainedRefinement(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, initialR=None, initialRFree=None, finalR=None, finalRFree=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.initialR = initialR
        self.initialRFree = initialRFree
        self.finalR = finalR
        self.finalRFree = finalRFree
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultREFMACRestrainedRefinement.subclass:
            return CCP4DataResultREFMACRestrainedRefinement.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultREFMACRestrainedRefinement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getInitialR(self): return self.initialR
    def setInitialR(self, initialR): self.initialR = initialR
    def getInitialRFree(self): return self.initialRFree
    def setInitialRFree(self, initialRFree): self.initialRFree = initialRFree
    def getFinalR(self): return self.finalR
    def setFinalR(self, finalR): self.finalR = finalR
    def getFinalRFree(self): return self.finalRFree
    def setFinalRFree(self, finalRFree): self.finalRFree = finalRFree
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultREFMACRestrainedRefinement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultREFMACRestrainedRefinement'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultREFMACRestrainedRefinement')
    def exportChildren(self, outfile, level, name_='CCP4DataResultREFMACRestrainedRefinement'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.initialR:
            self.initialR.export(outfile, level, name_='initialR')
        if self.initialRFree:
            self.initialRFree.export(outfile, level, name_='initialRFree')
        if self.finalR:
            self.finalR.export(outfile, level, name_='finalR')
        if self.finalRFree:
            self.finalRFree.export(outfile, level, name_='finalRFree')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultREFMACRestrainedRefinement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREFMACRestrainedRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultREFMACRestrainedRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultREFMACRestrainedRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultREFMACRestrainedRefinement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialR:
            showIndent(outfile, level)
            outfile.write('initialR=XSDataFloat(\n')
            self.initialR.exportLiteral(outfile, level, name_='initialR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialRFree:
            showIndent(outfile, level)
            outfile.write('initialRFree=XSDataFloat(\n')
            self.initialRFree.exportLiteral(outfile, level, name_='initialRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalR:
            showIndent(outfile, level)
            outfile.write('finalR=XSDataFloat(\n')
            self.finalR.exportLiteral(outfile, level, name_='finalR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalRFree:
            showIndent(outfile, level)
            outfile.write('finalRFree=XSDataFloat(\n')
            self.finalRFree.exportLiteral(outfile, level, name_='finalRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultREFMACRestrainedRefinement


class CCP4DataInputCAD(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, columnLabels=None, HKLOUT=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        if HKLIN is None:
            self.HKLIN = []
        else:
            self.HKLIN = HKLIN
        if columnLabels is None:
            self.columnLabels = []
        else:
            self.columnLabels = columnLabels
        self.HKLOUT = HKLOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputCAD.subclass:
            return CCP4DataInputCAD.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputCAD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def addHKLIN(self, value): self.HKLIN.append(value)
    def insertHKLIN(self, index, value): self.HKLIN[index] = value
    def getColumnLabels(self): return self.columnLabels
    def setColumnLabels(self, columnLabels): self.columnLabels = columnLabels
    def addColumnLabels(self, value): self.columnLabels.append(value)
    def insertColumnLabels(self, index, value): self.columnLabels[index] = value
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputCAD'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputCAD'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputCAD')
    def exportChildren(self, outfile, level, name_='CCP4DataInputCAD'):
        for HKLIN_ in self.getHKLIN():
            HKLIN_.export(outfile, level, name_='HKLIN')
        for columnLabels_ in self.getColumnLabels():
            columnLabels_.export(outfile, level, name_='columnLabels')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputCAD' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCAD.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCAD.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputCAD" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputCAD'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('HKLIN=[\n')
        level += 1
        for HKLIN in self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKL(\n')
            HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('columnLabels=[\n')
        level += 1
        for columnLabels in self.columnLabels:
            showIndent(outfile, level)
            outfile.write('XSDataListOfStrings(\n')
            columnLabels.exportLiteral(outfile, level, name_='columnLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.HKLIN.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'columnLabels':
            obj_ = XSDataListOfStrings.factory()
            obj_.build(child_)
            self.columnLabels.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputCAD


class CCP4DataResultCAD(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultCAD.subclass:
            return CCP4DataResultCAD.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultCAD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultCAD'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultCAD'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultCAD')
    def exportChildren(self, outfile, level, name_='CCP4DataResultCAD'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultCAD' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCAD.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCAD.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultCAD" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultCAD'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultCAD


class CCP4DataInputControlCopyUnitCellMTZtoPDB(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, XYZOUT=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.XYZOUT = XYZOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlCopyUnitCellMTZtoPDB.subclass:
            return CCP4DataInputControlCopyUnitCellMTZtoPDB.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlCopyUnitCellMTZtoPDB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlCopyUnitCellMTZtoPDB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlCopyUnitCellMTZtoPDB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlCopyUnitCellMTZtoPDB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlCopyUnitCellMTZtoPDB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlCopyUnitCellMTZtoPDB


class CCP4DataResultControlCopyUnitCellMTZtoPDB(XSDataResult):
    subclass = None
    def __init__(self, XYZOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.XYZOUT = XYZOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlCopyUnitCellMTZtoPDB.subclass:
            return CCP4DataResultControlCopyUnitCellMTZtoPDB.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlCopyUnitCellMTZtoPDB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB'):
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlCopyUnitCellMTZtoPDB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlCopyUnitCellMTZtoPDB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlCopyUnitCellMTZtoPDB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlCopyUnitCellMTZtoPDB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlCopyUnitCellMTZtoPDB


class CCP4DataInputControlCopySpaceGroupPDBtoMTZ(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, XYZIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlCopySpaceGroupPDBtoMTZ.subclass:
            return CCP4DataInputControlCopySpaceGroupPDBtoMTZ.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlCopySpaceGroupPDBtoMTZ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlCopySpaceGroupPDBtoMTZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlCopySpaceGroupPDBtoMTZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlCopySpaceGroupPDBtoMTZ" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlCopySpaceGroupPDBtoMTZ'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlCopySpaceGroupPDBtoMTZ


class CCP4DataResultControlCopySpaceGroupPDBtoMTZ(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlCopySpaceGroupPDBtoMTZ.subclass:
            return CCP4DataResultControlCopySpaceGroupPDBtoMTZ.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlCopySpaceGroupPDBtoMTZ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlCopySpaceGroupPDBtoMTZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlCopySpaceGroupPDBtoMTZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlCopySpaceGroupPDBtoMTZ" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlCopySpaceGroupPDBtoMTZ'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlCopySpaceGroupPDBtoMTZ


class CCP4DataInputControlPrepareMTZFileForRefinement(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, HKLIN=None, HKLOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlPrepareMTZFileForRefinement.subclass:
            return CCP4DataInputControlPrepareMTZFileForRefinement.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlPrepareMTZFileForRefinement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlPrepareMTZFileForRefinement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlPrepareMTZFileForRefinement'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlPrepareMTZFileForRefinement')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlPrepareMTZFileForRefinement'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlPrepareMTZFileForRefinement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlPrepareMTZFileForRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlPrepareMTZFileForRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlPrepareMTZFileForRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlPrepareMTZFileForRefinement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlPrepareMTZFileForRefinement


class CCP4DataResultControlPrepareMTZFileForRefinement(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, ColLabels=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.ColLabels = ColLabels
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlPrepareMTZFileForRefinement.subclass:
            return CCP4DataResultControlPrepareMTZFileForRefinement.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlPrepareMTZFileForRefinement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlPrepareMTZFileForRefinement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlPrepareMTZFileForRefinement'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlPrepareMTZFileForRefinement')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlPrepareMTZFileForRefinement'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlPrepareMTZFileForRefinement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlPrepareMTZFileForRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlPrepareMTZFileForRefinement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlPrepareMTZFileForRefinement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlPrepareMTZFileForRefinement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlPrepareMTZFileForRefinement


class CCP4DataInputControlPipelineCalcDiffMap(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, XYZIN=None, XYZOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        self.XYZIN = XYZIN
        self.XYZOUT = XYZOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlPipelineCalcDiffMap.subclass:
            return CCP4DataInputControlPipelineCalcDiffMap.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlPipelineCalcDiffMap(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlPipelineCalcDiffMap'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlPipelineCalcDiffMap'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlPipelineCalcDiffMap')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlPipelineCalcDiffMap'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlPipelineCalcDiffMap' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlPipelineCalcDiffMap.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlPipelineCalcDiffMap.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlPipelineCalcDiffMap" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlPipelineCalcDiffMap'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlPipelineCalcDiffMap


class CCP4DataResultControlPipelineCalcDiffMap(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, initialR=None, initialRFree=None, finalR=None, finalRFree=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.initialR = initialR
        self.initialRFree = initialRFree
        self.finalR = finalR
        self.finalRFree = finalRFree
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlPipelineCalcDiffMap.subclass:
            return CCP4DataResultControlPipelineCalcDiffMap.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlPipelineCalcDiffMap(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getInitialR(self): return self.initialR
    def setInitialR(self, initialR): self.initialR = initialR
    def getInitialRFree(self): return self.initialRFree
    def setInitialRFree(self, initialRFree): self.initialRFree = initialRFree
    def getFinalR(self): return self.finalR
    def setFinalR(self, finalR): self.finalR = finalR
    def getFinalRFree(self): return self.finalRFree
    def setFinalRFree(self, finalRFree): self.finalRFree = finalRFree
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlPipelineCalcDiffMap'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlPipelineCalcDiffMap'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlPipelineCalcDiffMap')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlPipelineCalcDiffMap'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.initialR:
            self.initialR.export(outfile, level, name_='initialR')
        if self.initialRFree:
            self.initialRFree.export(outfile, level, name_='initialRFree')
        if self.finalR:
            self.finalR.export(outfile, level, name_='finalR')
        if self.finalRFree:
            self.finalRFree.export(outfile, level, name_='finalRFree')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlPipelineCalcDiffMap' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlPipelineCalcDiffMap.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlPipelineCalcDiffMap.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlPipelineCalcDiffMap" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlPipelineCalcDiffMap'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialR:
            showIndent(outfile, level)
            outfile.write('initialR=XSDataFloat(\n')
            self.initialR.exportLiteral(outfile, level, name_='initialR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.initialRFree:
            showIndent(outfile, level)
            outfile.write('initialRFree=XSDataFloat(\n')
            self.initialRFree.exportLiteral(outfile, level, name_='initialRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalR:
            showIndent(outfile, level)
            outfile.write('finalR=XSDataFloat(\n')
            self.finalR.exportLiteral(outfile, level, name_='finalR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.finalRFree:
            showIndent(outfile, level)
            outfile.write('finalRFree=XSDataFloat(\n')
            self.finalRFree.exportLiteral(outfile, level, name_='finalRFree')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setInitialRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalR':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalRFree':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFinalRFree(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlPipelineCalcDiffMap


class XSDataListOfStrings(XSData):
    subclass = None
    def __init__(self, values=None):
        XSData.__init__(self)
        if values is None:
            self.values = []
        else:
            self.values = values
    def factory(*args_, **kwargs_):
        if XSDataListOfStrings.subclass:
            return XSDataListOfStrings.subclass(*args_, **kwargs_)
        else:
            return XSDataListOfStrings(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValues(self): return self.values
    def setValues(self, values): self.values = values
    def addValues(self, value): self.values.append(value)
    def insertValues(self, index, value): self.values[index] = value
    def export(self, outfile, level, name_='XSDataListOfStrings'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataListOfStrings'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataListOfStrings')
    def exportChildren(self, outfile, level, name_='XSDataListOfStrings'):
        for values_ in self.getValues():
            values_.export(outfile, level, name_='values')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataListOfStrings' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataListOfStrings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataListOfStrings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataListOfStrings" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataListOfStrings'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('values=[\n')
        level += 1
        for values in self.values:
            showIndent(outfile, level)
            outfile.write('XSDataString(\n')
            values.exportLiteral(outfile, level, name_='values')
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
            nodeName_ == 'values':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.values.append(obj_)
# end class XSDataListOfStrings


class XSDataListOfIntegers(XSData):
    subclass = None
    def __init__(self, values=None):
        XSData.__init__(self)
        if values is None:
            self.values = []
        else:
            self.values = values
    def factory(*args_, **kwargs_):
        if XSDataListOfIntegers.subclass:
            return XSDataListOfIntegers.subclass(*args_, **kwargs_)
        else:
            return XSDataListOfIntegers(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValues(self): return self.values
    def setValues(self, values): self.values = values
    def addValues(self, value): self.values.append(value)
    def insertValues(self, index, value): self.values[index] = value
    def export(self, outfile, level, name_='XSDataListOfIntegers'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataListOfIntegers'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataListOfIntegers')
    def exportChildren(self, outfile, level, name_='XSDataListOfIntegers'):
        for values_ in self.getValues():
            values_.export(outfile, level, name_='values')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataListOfIntegers' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataListOfIntegers.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataListOfIntegers.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataListOfIntegers" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataListOfIntegers'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('values=[\n')
        level += 1
        for values in self.values:
            showIndent(outfile, level)
            outfile.write('XSDataInteger(\n')
            values.exportLiteral(outfile, level, name_='values')
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
            nodeName_ == 'values':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.values.append(obj_)
# end class XSDataListOfIntegers


class XSDataListOfFloats(XSData):
    subclass = None
    def __init__(self, values=None):
        XSData.__init__(self)
        if values is None:
            self.values = []
        else:
            self.values = values
    def factory(*args_, **kwargs_):
        if XSDataListOfFloats.subclass:
            return XSDataListOfFloats.subclass(*args_, **kwargs_)
        else:
            return XSDataListOfFloats(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValues(self): return self.values
    def setValues(self, values): self.values = values
    def addValues(self, value): self.values.append(value)
    def insertValues(self, index, value): self.values[index] = value
    def export(self, outfile, level, name_='XSDataListOfFloats'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataListOfFloats'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataListOfFloats')
    def exportChildren(self, outfile, level, name_='XSDataListOfFloats'):
        for values_ in self.getValues():
            values_.export(outfile, level, name_='values')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataListOfFloats' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataListOfFloats.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataListOfFloats.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataListOfFloats" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataListOfFloats'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('values=[\n')
        level += 1
        for values in self.values:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            values.exportLiteral(outfile, level, name_='values')
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
            nodeName_ == 'values':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.values.append(obj_)
# end class XSDataListOfFloats


class CCP4DataInputPhaser(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, HKLOUT=None, XYZOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputPhaser.subclass:
            return CCP4DataInputPhaser.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputPhaser(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputPhaser'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputPhaser'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputPhaser')
    def exportChildren(self, outfile, level, name_='CCP4DataInputPhaser'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputPhaser' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputPhaser" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputPhaser'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputPhaser


class CCP4DataResultPhaser(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultPhaser.subclass:
            return CCP4DataResultPhaser.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultPhaser(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultPhaser'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultPhaser'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultPhaser')
    def exportChildren(self, outfile, level, name_='CCP4DataResultPhaser'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultPhaser' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultPhaser" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultPhaser'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultPhaser


class CCP4DataInputMRBUMP(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, sequence=None, prepdir=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.sequence = sequence
        self.prepdir = prepdir
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputMRBUMP.subclass:
            return CCP4DataInputMRBUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputMRBUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getSequence(self): return self.sequence
    def setSequence(self, sequence): self.sequence = sequence
    def getPrepdir(self): return self.prepdir
    def setPrepdir(self, prepdir): self.prepdir = prepdir
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputMRBUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputMRBUMP'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputMRBUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataInputMRBUMP'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.sequence:
            self.sequence.export(outfile, level, name_='sequence')
        if self.prepdir:
            self.prepdir.export(outfile, level, name_='prepdir')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputMRBUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputMRBUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputMRBUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputMRBUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputMRBUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sequence:
            showIndent(outfile, level)
            outfile.write('sequence=CCP4Sequence(\n')
            self.sequence.exportLiteral(outfile, level, name_='sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.prepdir:
            showIndent(outfile, level)
            outfile.write('prepdir=XSDataString(\n')
            self.prepdir.exportLiteral(outfile, level, name_='prepdir')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sequence':
            obj_ = CCP4Sequence.factory()
            obj_.build(child_)
            self.setSequence(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'prepdir':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPrepdir(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputMRBUMP


class CCP4DataResultMRBUMP(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, outpuLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.outpuLogFile = outpuLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultMRBUMP.subclass:
            return CCP4DataResultMRBUMP.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultMRBUMP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getOutpuLogFile(self): return self.outpuLogFile
    def setOutpuLogFile(self, outpuLogFile): self.outpuLogFile = outpuLogFile
    def export(self, outfile, level, name_='CCP4DataResultMRBUMP'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultMRBUMP'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultMRBUMP')
    def exportChildren(self, outfile, level, name_='CCP4DataResultMRBUMP'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.outpuLogFile:
            self.outpuLogFile.export(outfile, level, name_='outpuLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultMRBUMP' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultMRBUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultMRBUMP.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultMRBUMP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultMRBUMP'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outpuLogFile:
            showIndent(outfile, level)
            outfile.write('outpuLogFile=CCP4LogFile(\n')
            self.outpuLogFile.exportLiteral(outfile, level, name_='outpuLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outpuLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutpuLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultMRBUMP


class CCP4DataInputBUCCANEER(XSDataInput):
    subclass = None
    def __init__(self, XYZINREF=None, HKLINREF=None, HKLIN=None, XYZIN=None, sequence=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZINREF = XYZINREF
        self.HKLINREF = HKLINREF
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.sequence = sequence
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputBUCCANEER.subclass:
            return CCP4DataInputBUCCANEER.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputBUCCANEER(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZINREF(self): return self.XYZINREF
    def setXYZINREF(self, XYZINREF): self.XYZINREF = XYZINREF
    def getHKLINREF(self): return self.HKLINREF
    def setHKLINREF(self, HKLINREF): self.HKLINREF = HKLINREF
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getSequence(self): return self.sequence
    def setSequence(self, sequence): self.sequence = sequence
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputBUCCANEER'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputBUCCANEER'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputBUCCANEER')
    def exportChildren(self, outfile, level, name_='CCP4DataInputBUCCANEER'):
        if self.XYZINREF:
            self.XYZINREF.export(outfile, level, name_='XYZINREF')
        if self.HKLINREF:
            self.HKLINREF.export(outfile, level, name_='HKLINREF')
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.sequence:
            self.sequence.export(outfile, level, name_='sequence')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputBUCCANEER' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputBUCCANEER.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputBUCCANEER.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputBUCCANEER" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputBUCCANEER'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZINREF:
            showIndent(outfile, level)
            outfile.write('XYZINREF=XYZ(\n')
            self.XYZINREF.exportLiteral(outfile, level, name_='XYZINREF')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLINREF:
            showIndent(outfile, level)
            outfile.write('HKLINREF=HKL(\n')
            self.HKLINREF.exportLiteral(outfile, level, name_='HKLINREF')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sequence:
            showIndent(outfile, level)
            outfile.write('sequence=CCP4Sequence(\n')
            self.sequence.exportLiteral(outfile, level, name_='sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZINREF':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZINREF(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLINREF':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLINREF(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sequence':
            obj_ = CCP4Sequence.factory()
            obj_.build(child_)
            self.setSequence(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputBUCCANEER


class CCP4DataResultBUCCANEER(XSDataResult):
    subclass = None
    def __init__(self, XYZOUT=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.XYZOUT = XYZOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultBUCCANEER.subclass:
            return CCP4DataResultBUCCANEER.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultBUCCANEER(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultBUCCANEER'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultBUCCANEER'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultBUCCANEER')
    def exportChildren(self, outfile, level, name_='CCP4DataResultBUCCANEER'):
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultBUCCANEER' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultBUCCANEER.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultBUCCANEER.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultBUCCANEER" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultBUCCANEER'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultBUCCANEER


class XSDataListOfLists(XSData):
    subclass = None
    def __init__(self, valueOf_=''):
        XSData.__init__(self)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataListOfLists.subclass:
            return XSDataListOfLists.subclass(*args_, **kwargs_)
        else:
            return XSDataListOfLists(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataListOfLists'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataListOfLists'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataListOfLists')
    def exportChildren(self, outfile, level, name_='XSDataListOfLists'):
        XSData.exportChildren(self, outfile, level, name_)
        outfile.write(self.valueOf_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataListOfLists' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataListOfLists.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataListOfLists.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataListOfLists" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataListOfLists'):
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
# end class XSDataListOfLists


class CCP4DataInputPointlessOrigin(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, outputLogFile=None, HKLOUT=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
        self.HKLOUT = HKLOUT
    def factory(*args_, **kwargs_):
        if CCP4DataInputPointlessOrigin.subclass:
            return CCP4DataInputPointlessOrigin.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputPointlessOrigin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def export(self, outfile, level, name_='CCP4DataInputPointlessOrigin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputPointlessOrigin'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputPointlessOrigin')
    def exportChildren(self, outfile, level, name_='CCP4DataInputPointlessOrigin'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputPointlessOrigin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPointlessOrigin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPointlessOrigin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputPointlessOrigin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputPointlessOrigin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputPointlessOrigin


class CCP4DataResultPointlessOrigin(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, outputLogFile=None, returnStatus=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.outputLogFile = outputLogFile
        self.returnStatus = returnStatus
    def factory(*args_, **kwargs_):
        if CCP4DataResultPointlessOrigin.subclass:
            return CCP4DataResultPointlessOrigin.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultPointlessOrigin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def export(self, outfile, level, name_='CCP4DataResultPointlessOrigin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultPointlessOrigin'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultPointlessOrigin')
    def exportChildren(self, outfile, level, name_='CCP4DataResultPointlessOrigin'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultPointlessOrigin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPointlessOrigin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPointlessOrigin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultPointlessOrigin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultPointlessOrigin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultPointlessOrigin


class CCP4DataInputRefmacMonomerCheck(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputRefmacMonomerCheck.subclass:
            return CCP4DataInputRefmacMonomerCheck.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputRefmacMonomerCheck(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputRefmacMonomerCheck'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputRefmacMonomerCheck'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputRefmacMonomerCheck')
    def exportChildren(self, outfile, level, name_='CCP4DataInputRefmacMonomerCheck'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputRefmacMonomerCheck' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputRefmacMonomerCheck.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputRefmacMonomerCheck.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputRefmacMonomerCheck" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputRefmacMonomerCheck'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputRefmacMonomerCheck


class CCP4DataResultRefmacMonomerCheck(XSDataResult):
    subclass = None
    def __init__(self, fileStatus=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.fileStatus = fileStatus
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultRefmacMonomerCheck.subclass:
            return CCP4DataResultRefmacMonomerCheck.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultRefmacMonomerCheck(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFileStatus(self): return self.fileStatus
    def setFileStatus(self, fileStatus): self.fileStatus = fileStatus
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultRefmacMonomerCheck'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultRefmacMonomerCheck'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultRefmacMonomerCheck')
    def exportChildren(self, outfile, level, name_='CCP4DataResultRefmacMonomerCheck'):
        if self.fileStatus:
            self.fileStatus.export(outfile, level, name_='fileStatus')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultRefmacMonomerCheck' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultRefmacMonomerCheck.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultRefmacMonomerCheck.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultRefmacMonomerCheck" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultRefmacMonomerCheck'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.fileStatus:
            showIndent(outfile, level)
            outfile.write('fileStatus=XSDataString(\n')
            self.fileStatus.exportLiteral(outfile, level, name_='fileStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'fileStatus':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setFileStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultRefmacMonomerCheck


class CCP4DataInputCheckValidHKL(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputCheckValidHKL.subclass:
            return CCP4DataInputCheckValidHKL.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputCheckValidHKL(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputCheckValidHKL'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputCheckValidHKL'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputCheckValidHKL')
    def exportChildren(self, outfile, level, name_='CCP4DataInputCheckValidHKL'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputCheckValidHKL' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCheckValidHKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCheckValidHKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputCheckValidHKL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputCheckValidHKL'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputCheckValidHKL


class CCP4DataResultCheckValidHKL(XSDataResult):
    subclass = None
    def __init__(self, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultCheckValidHKL.subclass:
            return CCP4DataResultCheckValidHKL.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultCheckValidHKL(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultCheckValidHKL'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultCheckValidHKL'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultCheckValidHKL')
    def exportChildren(self, outfile, level, name_='CCP4DataResultCheckValidHKL'):
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultCheckValidHKL' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCheckValidHKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCheckValidHKL.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultCheckValidHKL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultCheckValidHKL'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultCheckValidHKL


class CCP4DataInputCheckValidXYZ(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputCheckValidXYZ.subclass:
            return CCP4DataInputCheckValidXYZ.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputCheckValidXYZ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputCheckValidXYZ'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputCheckValidXYZ'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputCheckValidXYZ')
    def exportChildren(self, outfile, level, name_='CCP4DataInputCheckValidXYZ'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputCheckValidXYZ' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCheckValidXYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputCheckValidXYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputCheckValidXYZ" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputCheckValidXYZ'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputCheckValidXYZ


class CCP4DataResultCheckValidXYZ(XSDataResult):
    subclass = None
    def __init__(self, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultCheckValidXYZ.subclass:
            return CCP4DataResultCheckValidXYZ.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultCheckValidXYZ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultCheckValidXYZ'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultCheckValidXYZ'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultCheckValidXYZ')
    def exportChildren(self, outfile, level, name_='CCP4DataResultCheckValidXYZ'):
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultCheckValidXYZ' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCheckValidXYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultCheckValidXYZ.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultCheckValidXYZ" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultCheckValidXYZ'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultCheckValidXYZ


class CCP4DataInputControlRefmacRigidBodyPhaser(XSDataInput):
    subclass = None
    def __init__(self, XYZIN=None, HKLIN=None, XYZOUT=None, ColLabels=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.XYZIN = XYZIN
        self.HKLIN = HKLIN
        self.XYZOUT = XYZOUT
        self.ColLabels = ColLabels
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlRefmacRigidBodyPhaser.subclass:
            return CCP4DataInputControlRefmacRigidBodyPhaser.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlRefmacRigidBodyPhaser(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getColLabels(self): return self.ColLabels
    def setColLabels(self, ColLabels): self.ColLabels = ColLabels
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlRefmacRigidBodyPhaser'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlRefmacRigidBodyPhaser'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlRefmacRigidBodyPhaser')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlRefmacRigidBodyPhaser'):
        if self.XYZIN:
            self.XYZIN.export(outfile, level, name_='XYZIN')
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.ColLabels:
            self.ColLabels.export(outfile, level, name_='ColLabels')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlRefmacRigidBodyPhaser' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlRefmacRigidBodyPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlRefmacRigidBodyPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlRefmacRigidBodyPhaser" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlRefmacRigidBodyPhaser'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZIN=XYZ(\n')
            self.XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ColLabels:
            showIndent(outfile, level)
            outfile.write('ColLabels=CCP4MTZColLabels(\n')
            self.ColLabels.exportLiteral(outfile, level, name_='ColLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ColLabels':
            obj_ = CCP4MTZColLabels.factory()
            obj_.build(child_)
            self.setColLabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlRefmacRigidBodyPhaser


class CCP4DataResultControlRefmacRigidBodyPhaser(XSDataResult):
    subclass = None
    def __init__(self, XYZOUT=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.XYZOUT = XYZOUT
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlRefmacRigidBodyPhaser.subclass:
            return CCP4DataResultControlRefmacRigidBodyPhaser.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlRefmacRigidBodyPhaser(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlRefmacRigidBodyPhaser'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlRefmacRigidBodyPhaser'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlRefmacRigidBodyPhaser')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlRefmacRigidBodyPhaser'):
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlRefmacRigidBodyPhaser' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlRefmacRigidBodyPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlRefmacRigidBodyPhaser.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlRefmacRigidBodyPhaser" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlRefmacRigidBodyPhaser'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlRefmacRigidBodyPhaser


class CCP4DataInputPDBList(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, XYZIN=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        if XYZIN is None:
            self.XYZIN = []
        else:
            self.XYZIN = XYZIN
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputPDBList.subclass:
            return CCP4DataInputPDBList.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputPDBList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def addXYZIN(self, value): self.XYZIN.append(value)
    def insertXYZIN(self, index, value): self.XYZIN[index] = value
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputPDBList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputPDBList'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputPDBList')
    def exportChildren(self, outfile, level, name_='CCP4DataInputPDBList'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        for XYZIN_ in self.getXYZIN():
            XYZIN_.export(outfile, level, name_='XYZIN')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputPDBList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputPDBList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputPDBList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputPDBList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('XYZIN=[\n')
        level += 1
        for XYZIN in self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZ(\n')
            XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.XYZIN.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputPDBList


class CCP4DataResultPDBList(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, spaceGroup=None, returnStatus=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.spaceGroup = spaceGroup
        self.returnStatus = returnStatus
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultPDBList.subclass:
            return CCP4DataResultPDBList.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultPDBList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getReturnStatus(self): return self.returnStatus
    def setReturnStatus(self, returnStatus): self.returnStatus = returnStatus
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultPDBList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultPDBList'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultPDBList')
    def exportChildren(self, outfile, level, name_='CCP4DataResultPDBList'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.returnStatus:
            self.returnStatus.export(outfile, level, name_='returnStatus')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultPDBList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultPDBList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultPDBList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultPDBList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=CCP4SpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.returnStatus:
            showIndent(outfile, level)
            outfile.write('returnStatus=CCP4ReturnStatus(\n')
            self.returnStatus.exportLiteral(outfile, level, name_='returnStatus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = CCP4SpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'returnStatus':
            obj_ = CCP4ReturnStatus.factory()
            obj_.build(child_)
            self.setReturnStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultPDBList


class CCP4DataInputControlDIMPLES(XSDataInput):
    subclass = None
    def __init__(self, HKLIN=None, HKLOUT=None, XYZIN=None, XYZOUT=None, outputLogFile=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.HKLIN = HKLIN
        self.HKLOUT = HKLOUT
        if XYZIN is None:
            self.XYZIN = []
        else:
            self.XYZIN = XYZIN
        self.XYZOUT = XYZOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataInputControlDIMPLES.subclass:
            return CCP4DataInputControlDIMPLES.subclass(*args_, **kwargs_)
        else:
            return CCP4DataInputControlDIMPLES(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLIN(self): return self.HKLIN
    def setHKLIN(self, HKLIN): self.HKLIN = HKLIN
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZIN(self): return self.XYZIN
    def setXYZIN(self, XYZIN): self.XYZIN = XYZIN
    def addXYZIN(self, value): self.XYZIN.append(value)
    def insertXYZIN(self, index, value): self.XYZIN[index] = value
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataInputControlDIMPLES'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataInputControlDIMPLES'):
        XSDataInput.exportAttributes(self, outfile, level, name_='CCP4DataInputControlDIMPLES')
    def exportChildren(self, outfile, level, name_='CCP4DataInputControlDIMPLES'):
        if self.HKLIN:
            self.HKLIN.export(outfile, level, name_='HKLIN')
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        for XYZIN_ in self.getXYZIN():
            XYZIN_.export(outfile, level, name_='XYZIN')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataInputControlDIMPLES' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlDIMPLES.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataInputControlDIMPLES.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataInputControlDIMPLES" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataInputControlDIMPLES'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLIN:
            showIndent(outfile, level)
            outfile.write('HKLIN=HKL(\n')
            self.HKLIN.exportLiteral(outfile, level, name_='HKLIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('XYZIN=[\n')
        level += 1
        for XYZIN in self.XYZIN:
            showIndent(outfile, level)
            outfile.write('XYZ(\n')
            XYZIN.exportLiteral(outfile, level, name_='XYZIN')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLIN':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLIN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZIN':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.XYZIN.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class CCP4DataInputControlDIMPLES


class CCP4DataResultControlDIMPLES(XSDataResult):
    subclass = None
    def __init__(self, HKLOUT=None, XYZOUT=None, outputLogFile=None, status=None):
        XSDataResult.__init__(self, status)
        self.HKLOUT = HKLOUT
        self.XYZOUT = XYZOUT
        self.outputLogFile = outputLogFile
    def factory(*args_, **kwargs_):
        if CCP4DataResultControlDIMPLES.subclass:
            return CCP4DataResultControlDIMPLES.subclass(*args_, **kwargs_)
        else:
            return CCP4DataResultControlDIMPLES(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHKLOUT(self): return self.HKLOUT
    def setHKLOUT(self, HKLOUT): self.HKLOUT = HKLOUT
    def getXYZOUT(self): return self.XYZOUT
    def setXYZOUT(self, XYZOUT): self.XYZOUT = XYZOUT
    def getOutputLogFile(self): return self.outputLogFile
    def setOutputLogFile(self, outputLogFile): self.outputLogFile = outputLogFile
    def export(self, outfile, level, name_='CCP4DataResultControlDIMPLES'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='CCP4DataResultControlDIMPLES'):
        XSDataResult.exportAttributes(self, outfile, level, name_='CCP4DataResultControlDIMPLES')
    def exportChildren(self, outfile, level, name_='CCP4DataResultControlDIMPLES'):
        if self.HKLOUT:
            self.HKLOUT.export(outfile, level, name_='HKLOUT')
        if self.XYZOUT:
            self.XYZOUT.export(outfile, level, name_='XYZOUT')
        if self.outputLogFile:
            self.outputLogFile.export(outfile, level, name_='outputLogFile')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='CCP4DataResultControlDIMPLES' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlDIMPLES.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = CCP4DataResultControlDIMPLES.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="CCP4DataResultControlDIMPLES" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='CCP4DataResultControlDIMPLES'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.HKLOUT:
            showIndent(outfile, level)
            outfile.write('HKLOUT=HKL(\n')
            self.HKLOUT.exportLiteral(outfile, level, name_='HKLOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XYZOUT:
            showIndent(outfile, level)
            outfile.write('XYZOUT=XYZ(\n')
            self.XYZOUT.exportLiteral(outfile, level, name_='XYZOUT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.outputLogFile:
            showIndent(outfile, level)
            outfile.write('outputLogFile=CCP4LogFile(\n')
            self.outputLogFile.exportLiteral(outfile, level, name_='outputLogFile')
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
            nodeName_ == 'HKLOUT':
            obj_ = HKL.factory()
            obj_.build(child_)
            self.setHKLOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XYZOUT':
            obj_ = XYZ.factory()
            obj_.build(child_)
            self.setXYZOUT(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputLogFile':
            obj_ = CCP4LogFile.factory()
            obj_.build(child_)
            self.setOutputLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class CCP4DataResultControlDIMPLES


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


class XSDataDisplacement(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataDisplacement.subclass:
            return XSDataDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDisplacement'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDisplacement')
    def exportChildren(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

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
# end class XSDataDisplacement


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


class XSDataLinearDisplacement(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, valueOf_=''):
        XSDataDisplacement.__init__(self, value)
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


class XSDataDictionary(XSData):
    subclass = None
    def __init__(self, keyValuePair=None):
        XSData.__init__(self)
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
        XSData.exportAttributes(self, outfile, level, name_='XSDataDictionary')
    def exportChildren(self, outfile, level, name_='XSDataDictionary'):
        for keyValuePair_ in self.getKeyValuePair():
            keyValuePair_.export(outfile, level, name_='keyValuePair')
        XSData.exportChildren(self, outfile, level, name_)

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
        XSData.exportLiteralAttributes(self, outfile, level, name_)
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
            nodeName_ == 'keyValuePair':
            obj_ = XSDataKeyValuePair.factory()
            obj_.build(child_)
            self.keyValuePair.append(obj_)
# end class XSDataDictionary


class XSDataKeyValuePair(XSData):
    subclass = None
    def __init__(self, key=None, value=None):
        XSData.__init__(self)
        self.key = key
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataKeyValuePair.subclass:
            return XSDataKeyValuePair.subclass(*args_, **kwargs_)
        else:
            return XSDataKeyValuePair(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getKey(self): return self.key
    def setKey(self, key): self.key = key
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataKeyValuePair'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataKeyValuePair'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataKeyValuePair')
    def exportChildren(self, outfile, level, name_='XSDataKeyValuePair'):
        if self.key:
            self.key.export(outfile, level, name_='key')
        if self.value:
            self.value.export(outfile, level, name_='value')
        XSData.exportChildren(self, outfile, level, name_)

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
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.key:
            showIndent(outfile, level)
            outfile.write('key=XSDataString(\n')
            self.key.exportLiteral(outfile, level, name_='key')
            showIndent(outfile, level)
            outfile.write('),\n')
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
            nodeName_ == 'key':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKey(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setValue(obj_)
# end class XSDataKeyValuePair


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


class XSDataAngle(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, valueOf_=''):
        XSDataDisplacement.__init__(self, value)
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
        elif name == 'key':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('key', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'keyValuePair':
            obj = XSDataKeyValuePair.factory()
            stackObj = SaxStackElement('keyValuePair', obj)
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
        elif name == 'F':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('F', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SIGF':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('SIGF', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'IMEAN':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('IMEAN', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SIGIMEAN':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('SIGIMEAN', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symmetryOperation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('symmetryOperation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symmetryMatrix':
            obj = CCP4RTMatrix.factory()
            stackObj = SaxStackElement('symmetryMatrix', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e11':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e11', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e12':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e12', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e13':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e13', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e21':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e21', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e22':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e22', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e23':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e23', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e31':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e31', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e32':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e32', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e33':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e33', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e41':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e41', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e42':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e42', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e43':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('e43', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symmetryOperations':
            obj = CCP4SymmetryOperation.factory()
            stackObj = SaxStackElement('symmetryOperations', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('resolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'oneLetterCode':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('oneLetterCode', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfResidues':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfResidues', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'molecularMass':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('molecularMass', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ReindexingOperation':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('ReindexingOperation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ReindexingMatrix':
            obj = CCP4RTMatrix.factory()
            stackObj = SaxStackElement('ReindexingMatrix', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'code':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('code', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'HKLIN':
            obj = HKL.factory()
            stackObj = SaxStackElement('HKLIN', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'outputLogFile':
            obj = CCP4LogFile.factory()
            stackObj = SaxStackElement('outputLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spaceGroup':
            obj = CCP4SpaceGroup.factory()
            stackObj = SaxStackElement('spaceGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unitCell':
            obj = CCP4UnitCell.factory()
            stackObj = SaxStackElement('unitCell', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'upperResolutionLimit':
            obj = CCP4ResolutionLimit.factory()
            stackObj = SaxStackElement('upperResolutionLimit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lowerResolutionLimit':
            obj = CCP4ResolutionLimit.factory()
            stackObj = SaxStackElement('lowerResolutionLimit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'listOfColumns':
            obj = XSParamList.factory()
            stackObj = SaxStackElement('listOfColumns', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XYZIN':
            obj = XYZ.factory()
            stackObj = SaxStackElement('XYZIN', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sequence':
            obj = CCP4Sequence.factory()
            stackObj = SaxStackElement('sequence', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XYZOUT':
            obj = XYZ.factory()
            stackObj = SaxStackElement('XYZOUT', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'returnStatus':
            obj = CCP4ReturnStatus.factory()
            stackObj = SaxStackElement('returnStatus', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'HKLOUT':
            obj = HKL.factory()
            stackObj = SaxStackElement('HKLOUT', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ColLabels':
            obj = CCP4MTZColLabels.factory()
            stackObj = SaxStackElement('ColLabels', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'reindexingOperation':
            obj = CCP4SymmetryOperation.factory()
            stackObj = SaxStackElement('reindexingOperation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolutionLimit':
            obj = CCP4ResolutionLimit.factory()
            stackObj = SaxStackElement('resolutionLimit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'initialR':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('initialR', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'initialRFree':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('initialRFree', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'finalR':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('finalR', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'finalRFree':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('finalRFree', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'columnLabels':
            obj = XSDataListOfStrings.factory()
            stackObj = SaxStackElement('columnLabels', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'values':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('values', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'prepdir':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('prepdir', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'outpuLogFile':
            obj = CCP4LogFile.factory()
            stackObj = SaxStackElement('outpuLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XYZINREF':
            obj = XYZ.factory()
            stackObj = SaxStackElement('XYZINREF', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'HKLINREF':
            obj = HKL.factory()
            stackObj = SaxStackElement('HKLINREF', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fileStatus':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('fileStatus', obj)
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
                    except Exception:
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
        elif name == 'path':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'key':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKey(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'keyValuePair':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addKeyValuePair(self.stack[-1].obj)
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
        elif name == 'F':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setF(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'SIGF':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSIGF(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'IMEAN':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIMEAN(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'SIGIMEAN':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSIGIMEAN(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symmetryOperation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSymmetryOperation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symmetryMatrix':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSymmetryMatrix(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e11':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE11(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e12':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE12(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e13':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE13(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e21':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE21(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e22':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE22(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e23':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE23(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e31':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE31(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e32':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE32(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e33':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE33(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e41':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE41(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e42':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE42(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e43':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setE43(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symmetryOperations':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSymmetryOperations(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'oneLetterCode':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOneLetterCode(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfResidues':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfResidues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'molecularMass':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMolecularMass(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ReindexingOperation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReindexingOperation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ReindexingMatrix':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReindexingMatrix(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'code':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCode(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'HKLIN':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHKLIN(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'outputLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutputLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spaceGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpaceGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unitCell':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnitCell(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'upperResolutionLimit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUpperResolutionLimit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'lowerResolutionLimit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLowerResolutionLimit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'listOfColumns':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addListOfColumns(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XYZIN':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXYZIN(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sequence':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSequence(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XYZOUT':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXYZOUT(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'returnStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReturnStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'HKLOUT':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHKLOUT(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ColLabels':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setColLabels(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'reindexingOperation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReindexingOperation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolutionLimit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolutionLimit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'initialR':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInitialR(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'initialRFree':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInitialRFree(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'finalR':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFinalR(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'finalRFree':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFinalRFree(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'columnLabels':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addColumnLabels(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'values':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addValues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'prepdir':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPrepdir(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'outpuLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOutpuLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XYZINREF':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXYZINREF(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'HKLINREF':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHKLINREF(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fileStatus':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFileStatus(self.stack[-1].obj)
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
    sys.stdout.write('from XSDataCCP4DIMPLE import *\n\n')
    sys.stdout.write('rootObj = XSDataDouble(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSDataDouble")
    sys.stdout.write(')\n')
    return rootObj

class XSDataCCP4DIMPLE:
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

