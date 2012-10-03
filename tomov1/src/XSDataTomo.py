#!/usr/bin/env python

#
# Generated Thu Mar 11 16:49:48 2010 by EDGenerateDS.py.
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


class XSDataInputSinogramGeneration(XSDataInput):
    subclass = None
    def __init__(self, imageDirectory=None, imageWidth=None, numberOfImages=None, numberOfSegments=None, segmentHeight=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.imageDirectory = imageDirectory
        self.imageWidth = imageWidth
        self.numberOfImages = numberOfImages
        self.numberOfSegments = numberOfSegments
        self.segmentHeight = segmentHeight
    def factory(*args_, **kwargs_):
        if XSDataInputSinogramGeneration.subclass:
            return XSDataInputSinogramGeneration.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSinogramGeneration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getImageDirectory(self): return self.imageDirectory
    def setImageDirectory(self, imageDirectory): self.imageDirectory = imageDirectory
    def getImageWidth(self): return self.imageWidth
    def setImageWidth(self, imageWidth): self.imageWidth = imageWidth
    def getNumberOfImages(self): return self.numberOfImages
    def setNumberOfImages(self, numberOfImages): self.numberOfImages = numberOfImages
    def getNumberOfSegments(self): return self.numberOfSegments
    def setNumberOfSegments(self, numberOfSegments): self.numberOfSegments = numberOfSegments
    def getSegmentHeight(self): return self.segmentHeight
    def setSegmentHeight(self, segmentHeight): self.segmentHeight = segmentHeight
    def export(self, outfile, level, name_='XSDataInputSinogramGeneration'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSinogramGeneration'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSinogramGeneration')
    def exportChildren(self, outfile, level, name_='XSDataInputSinogramGeneration'):
        if self.imageDirectory:
            self.imageDirectory.export(outfile, level, name_='imageDirectory')
        if self.imageWidth:
            self.imageWidth.export(outfile, level, name_='imageWidth')
        if self.numberOfImages:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        if self.numberOfSegments:
            self.numberOfSegments.export(outfile, level, name_='numberOfSegments')
        if self.segmentHeight:
            self.segmentHeight.export(outfile, level, name_='segmentHeight')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSinogramGeneration' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSinogramGeneration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSinogramGeneration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSinogramGeneration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSinogramGeneration'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.imageDirectory:
            showIndent(outfile, level)
            outfile.write('imageDirectory=XSDataFile(\n')
            self.imageDirectory.exportLiteral(outfile, level, name_='imageDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageWidth:
            showIndent(outfile, level)
            outfile.write('imageWidth=XSDataInteger(\n')
            self.imageWidth.exportLiteral(outfile, level, name_='imageWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfImages:
            showIndent(outfile, level)
            outfile.write('numberOfImages=XSDataInteger(\n')
            self.numberOfImages.exportLiteral(outfile, level, name_='numberOfImages')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfSegments:
            showIndent(outfile, level)
            outfile.write('numberOfSegments=XSDataInteger(\n')
            self.numberOfSegments.exportLiteral(outfile, level, name_='numberOfSegments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.segmentHeight:
            showIndent(outfile, level)
            outfile.write('segmentHeight=XSDataInteger(\n')
            self.segmentHeight.exportLiteral(outfile, level, name_='segmentHeight')
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
            nodeName_ == 'imageDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setImageDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageWidth':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setImageWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfSegments':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfSegments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'segmentHeight':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSegmentHeight(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSinogramGeneration


class XSDataInputReconstruction(XSDataInput):
    subclass = None
    def __init__(self, reconstructionCenter=None, sinogramDirectory=None, sinogramLength=None, sinogramWidth=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.reconstructionCenter = reconstructionCenter
        self.sinogramDirectory = sinogramDirectory
        self.sinogramLength = sinogramLength
        self.sinogramWidth = sinogramWidth
    def factory(*args_, **kwargs_):
        if XSDataInputReconstruction.subclass:
            return XSDataInputReconstruction.subclass(*args_, **kwargs_)
        else:
            return XSDataInputReconstruction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getReconstructionCenter(self): return self.reconstructionCenter
    def setReconstructionCenter(self, reconstructionCenter): self.reconstructionCenter = reconstructionCenter
    def getSinogramDirectory(self): return self.sinogramDirectory
    def setSinogramDirectory(self, sinogramDirectory): self.sinogramDirectory = sinogramDirectory
    def getSinogramLength(self): return self.sinogramLength
    def setSinogramLength(self, sinogramLength): self.sinogramLength = sinogramLength
    def getSinogramWidth(self): return self.sinogramWidth
    def setSinogramWidth(self, sinogramWidth): self.sinogramWidth = sinogramWidth
    def export(self, outfile, level, name_='XSDataInputReconstruction'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputReconstruction'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputReconstruction')
    def exportChildren(self, outfile, level, name_='XSDataInputReconstruction'):
        if self.reconstructionCenter:
            self.reconstructionCenter.export(outfile, level, name_='reconstructionCenter')
        if self.sinogramDirectory:
            self.sinogramDirectory.export(outfile, level, name_='sinogramDirectory')
        if self.sinogramLength:
            self.sinogramLength.export(outfile, level, name_='sinogramLength')
        if self.sinogramWidth:
            self.sinogramWidth.export(outfile, level, name_='sinogramWidth')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputReconstruction' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputReconstruction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputReconstruction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputReconstruction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputReconstruction'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.reconstructionCenter:
            showIndent(outfile, level)
            outfile.write('reconstructionCenter=XSDataFloat(\n')
            self.reconstructionCenter.exportLiteral(outfile, level, name_='reconstructionCenter')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sinogramDirectory:
            showIndent(outfile, level)
            outfile.write('sinogramDirectory=XSDataFile(\n')
            self.sinogramDirectory.exportLiteral(outfile, level, name_='sinogramDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sinogramLength:
            showIndent(outfile, level)
            outfile.write('sinogramLength=XSDataInteger(\n')
            self.sinogramLength.exportLiteral(outfile, level, name_='sinogramLength')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sinogramWidth:
            showIndent(outfile, level)
            outfile.write('sinogramWidth=XSDataInteger(\n')
            self.sinogramWidth.exportLiteral(outfile, level, name_='sinogramWidth')
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
            nodeName_ == 'reconstructionCenter':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setReconstructionCenter(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSinogramDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramLength':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSinogramLength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramWidth':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSinogramWidth(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputReconstruction


class XSDataTomoParameters(XSData):
    subclass = None
    def __init__(self, name=None, values=None):
        XSData.__init__(self)
        self.name = name
        if values is None:
            self.values = []
        else:
            self.values = values
    def factory(*args_, **kwargs_):
        if XSDataTomoParameters.subclass:
            return XSDataTomoParameters.subclass(*args_, **kwargs_)
        else:
            return XSDataTomoParameters(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getValues(self): return self.values
    def setValues(self, values): self.values = values
    def addValues(self, value): self.values.append(value)
    def insertValues(self, index, value): self.values[index] = value
    def export(self, outfile, level, name_='XSDataTomoParameters'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataTomoParameters'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataTomoParameters')
    def exportChildren(self, outfile, level, name_='XSDataTomoParameters'):
        if self.name:
            self.name.export(outfile, level, name_='name')
        for values_ in self.getValues():
            values_.export(outfile, level, name_='values')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataTomoParameters' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataTomoParameters.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataTomoParameters.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataTomoParameters" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataTomoParameters'):
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
            nodeName_ == 'name':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'values':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.values.append(obj_)
# end class XSDataTomoParameters


class XSDataResultSinogramGeneration(XSDataResult):
    subclass = None
    def __init__(self, sinogramDirectory=None, sinogramLength=None, sinogramWidth=None, status=None):
        XSDataResult.__init__(self, status)
        self.sinogramDirectory = sinogramDirectory
        self.sinogramLength = sinogramLength
        self.sinogramWidth = sinogramWidth
    def factory(*args_, **kwargs_):
        if XSDataResultSinogramGeneration.subclass:
            return XSDataResultSinogramGeneration.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSinogramGeneration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSinogramDirectory(self): return self.sinogramDirectory
    def setSinogramDirectory(self, sinogramDirectory): self.sinogramDirectory = sinogramDirectory
    def getSinogramLength(self): return self.sinogramLength
    def setSinogramLength(self, sinogramLength): self.sinogramLength = sinogramLength
    def getSinogramWidth(self): return self.sinogramWidth
    def setSinogramWidth(self, sinogramWidth): self.sinogramWidth = sinogramWidth
    def export(self, outfile, level, name_='XSDataResultSinogramGeneration'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSinogramGeneration'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSinogramGeneration')
    def exportChildren(self, outfile, level, name_='XSDataResultSinogramGeneration'):
        if self.sinogramDirectory:
            self.sinogramDirectory.export(outfile, level, name_='sinogramDirectory')
        if self.sinogramLength:
            self.sinogramLength.export(outfile, level, name_='sinogramLength')
        if self.sinogramWidth:
            self.sinogramWidth.export(outfile, level, name_='sinogramWidth')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSinogramGeneration' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSinogramGeneration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSinogramGeneration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSinogramGeneration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSinogramGeneration'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.sinogramDirectory:
            showIndent(outfile, level)
            outfile.write('sinogramDirectory=XSDataFile(\n')
            self.sinogramDirectory.exportLiteral(outfile, level, name_='sinogramDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sinogramLength:
            showIndent(outfile, level)
            outfile.write('sinogramLength=XSDataInteger(\n')
            self.sinogramLength.exportLiteral(outfile, level, name_='sinogramLength')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sinogramWidth:
            showIndent(outfile, level)
            outfile.write('sinogramWidth=XSDataInteger(\n')
            self.sinogramWidth.exportLiteral(outfile, level, name_='sinogramWidth')
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
            nodeName_ == 'sinogramDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSinogramDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramLength':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSinogramLength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramWidth':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSinogramWidth(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultSinogramGeneration


class XSDataResultReconstruction(XSDataResult):
    subclass = None
    def __init__(self, numberOfSlices=None, sliceDirectory=None, status=None):
        XSDataResult.__init__(self, status)
        self.numberOfSlices = numberOfSlices
        self.sliceDirectory = sliceDirectory
    def factory(*args_, **kwargs_):
        if XSDataResultReconstruction.subclass:
            return XSDataResultReconstruction.subclass(*args_, **kwargs_)
        else:
            return XSDataResultReconstruction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberOfSlices(self): return self.numberOfSlices
    def setNumberOfSlices(self, numberOfSlices): self.numberOfSlices = numberOfSlices
    def getSliceDirectory(self): return self.sliceDirectory
    def setSliceDirectory(self, sliceDirectory): self.sliceDirectory = sliceDirectory
    def export(self, outfile, level, name_='XSDataResultReconstruction'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultReconstruction'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultReconstruction')
    def exportChildren(self, outfile, level, name_='XSDataResultReconstruction'):
        if self.numberOfSlices:
            self.numberOfSlices.export(outfile, level, name_='numberOfSlices')
        if self.sliceDirectory:
            self.sliceDirectory.export(outfile, level, name_='sliceDirectory')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultReconstruction' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultReconstruction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultReconstruction.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultReconstruction" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultReconstruction'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.numberOfSlices:
            showIndent(outfile, level)
            outfile.write('numberOfSlices=XSDataInteger(\n')
            self.numberOfSlices.exportLiteral(outfile, level, name_='numberOfSlices')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sliceDirectory:
            showIndent(outfile, level)
            outfile.write('sliceDirectory=XSDataFile(\n')
            self.sliceDirectory.exportLiteral(outfile, level, name_='sliceDirectory')
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
            nodeName_ == 'numberOfSlices':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfSlices(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sliceDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSliceDirectory(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultReconstruction


class XSDataInputTomography(XSDataInput):
    subclass = None
    def __init__(self, byteDepthOfImage=None, chunkHeight=None, imageDirectory=None, imageWidth=None, jobName=None, numberOfChunks=None, numberOfProjectionsPerSegment=None, numberOfSegments=None, settingsFileName=None, timeoutLength=None, timeoutPollingInterval=None, uniqueName=None, configuration=None):
        XSDataInput.__init__(self, configuration)
        self.byteDepthOfImage = byteDepthOfImage
        self.chunkHeight = chunkHeight
        self.imageDirectory = imageDirectory
        self.imageWidth = imageWidth
        self.jobName = jobName
        self.numberOfChunks = numberOfChunks
        self.numberOfProjectionsPerSegment = numberOfProjectionsPerSegment
        self.numberOfSegments = numberOfSegments
        self.settingsFileName = settingsFileName
        self.timeoutLength = timeoutLength
        self.timeoutPollingInterval = timeoutPollingInterval
        self.uniqueName = uniqueName
    def factory(*args_, **kwargs_):
        if XSDataInputTomography.subclass:
            return XSDataInputTomography.subclass(*args_, **kwargs_)
        else:
            return XSDataInputTomography(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getByteDepthOfImage(self): return self.byteDepthOfImage
    def setByteDepthOfImage(self, byteDepthOfImage): self.byteDepthOfImage = byteDepthOfImage
    def getChunkHeight(self): return self.chunkHeight
    def setChunkHeight(self, chunkHeight): self.chunkHeight = chunkHeight
    def getImageDirectory(self): return self.imageDirectory
    def setImageDirectory(self, imageDirectory): self.imageDirectory = imageDirectory
    def getImageWidth(self): return self.imageWidth
    def setImageWidth(self, imageWidth): self.imageWidth = imageWidth
    def getJobName(self): return self.jobName
    def setJobName(self, jobName): self.jobName = jobName
    def getNumberOfChunks(self): return self.numberOfChunks
    def setNumberOfChunks(self, numberOfChunks): self.numberOfChunks = numberOfChunks
    def getNumberOfProjectionsPerSegment(self): return self.numberOfProjectionsPerSegment
    def setNumberOfProjectionsPerSegment(self, numberOfProjectionsPerSegment): self.numberOfProjectionsPerSegment = numberOfProjectionsPerSegment
    def getNumberOfSegments(self): return self.numberOfSegments
    def setNumberOfSegments(self, numberOfSegments): self.numberOfSegments = numberOfSegments
    def getSettingsFileName(self): return self.settingsFileName
    def setSettingsFileName(self, settingsFileName): self.settingsFileName = settingsFileName
    def getTimeoutLength(self): return self.timeoutLength
    def setTimeoutLength(self, timeoutLength): self.timeoutLength = timeoutLength
    def getTimeoutPollingInterval(self): return self.timeoutPollingInterval
    def setTimeoutPollingInterval(self, timeoutPollingInterval): self.timeoutPollingInterval = timeoutPollingInterval
    def getUniqueName(self): return self.uniqueName
    def setUniqueName(self, uniqueName): self.uniqueName = uniqueName
    def export(self, outfile, level, name_='XSDataInputTomography'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputTomography'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputTomography')
    def exportChildren(self, outfile, level, name_='XSDataInputTomography'):
        if self.byteDepthOfImage:
            self.byteDepthOfImage.export(outfile, level, name_='byteDepthOfImage')
        if self.chunkHeight:
            self.chunkHeight.export(outfile, level, name_='chunkHeight')
        if self.imageDirectory:
            self.imageDirectory.export(outfile, level, name_='imageDirectory')
        if self.imageWidth:
            self.imageWidth.export(outfile, level, name_='imageWidth')
        if self.jobName:
            self.jobName.export(outfile, level, name_='jobName')
        if self.numberOfChunks:
            self.numberOfChunks.export(outfile, level, name_='numberOfChunks')
        if self.numberOfProjectionsPerSegment:
            self.numberOfProjectionsPerSegment.export(outfile, level, name_='numberOfProjectionsPerSegment')
        if self.numberOfSegments:
            self.numberOfSegments.export(outfile, level, name_='numberOfSegments')
        if self.settingsFileName:
            self.settingsFileName.export(outfile, level, name_='settingsFileName')
        if self.timeoutLength:
            self.timeoutLength.export(outfile, level, name_='timeoutLength')
        if self.timeoutPollingInterval:
            self.timeoutPollingInterval.export(outfile, level, name_='timeoutPollingInterval')
        if self.uniqueName:
            self.uniqueName.export(outfile, level, name_='uniqueName')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputTomography' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputTomography.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputTomography.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputTomography" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputTomography'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.byteDepthOfImage:
            showIndent(outfile, level)
            outfile.write('byteDepthOfImage=XSDataInteger(\n')
            self.byteDepthOfImage.exportLiteral(outfile, level, name_='byteDepthOfImage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.chunkHeight:
            showIndent(outfile, level)
            outfile.write('chunkHeight=XSDataInteger(\n')
            self.chunkHeight.exportLiteral(outfile, level, name_='chunkHeight')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageDirectory:
            showIndent(outfile, level)
            outfile.write('imageDirectory=XSDataFile(\n')
            self.imageDirectory.exportLiteral(outfile, level, name_='imageDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageWidth:
            showIndent(outfile, level)
            outfile.write('imageWidth=XSDataInteger(\n')
            self.imageWidth.exportLiteral(outfile, level, name_='imageWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.jobName:
            showIndent(outfile, level)
            outfile.write('jobName=XSDataString(\n')
            self.jobName.exportLiteral(outfile, level, name_='jobName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfChunks:
            showIndent(outfile, level)
            outfile.write('numberOfChunks=XSDataInteger(\n')
            self.numberOfChunks.exportLiteral(outfile, level, name_='numberOfChunks')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfProjectionsPerSegment:
            showIndent(outfile, level)
            outfile.write('numberOfProjectionsPerSegment=XSDataInteger(\n')
            self.numberOfProjectionsPerSegment.exportLiteral(outfile, level, name_='numberOfProjectionsPerSegment')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfSegments:
            showIndent(outfile, level)
            outfile.write('numberOfSegments=XSDataInteger(\n')
            self.numberOfSegments.exportLiteral(outfile, level, name_='numberOfSegments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.settingsFileName:
            showIndent(outfile, level)
            outfile.write('settingsFileName=XSDataFile(\n')
            self.settingsFileName.exportLiteral(outfile, level, name_='settingsFileName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeoutLength:
            showIndent(outfile, level)
            outfile.write('timeoutLength=XSDataFloat(\n')
            self.timeoutLength.exportLiteral(outfile, level, name_='timeoutLength')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timeoutPollingInterval:
            showIndent(outfile, level)
            outfile.write('timeoutPollingInterval=XSDataFloat(\n')
            self.timeoutPollingInterval.exportLiteral(outfile, level, name_='timeoutPollingInterval')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.uniqueName:
            showIndent(outfile, level)
            outfile.write('uniqueName=XSDataString(\n')
            self.uniqueName.exportLiteral(outfile, level, name_='uniqueName')
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
            nodeName_ == 'byteDepthOfImage':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setByteDepthOfImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chunkHeight':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setChunkHeight(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setImageDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageWidth':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setImageWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jobName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setJobName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfChunks':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfChunks(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfProjectionsPerSegment':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfProjectionsPerSegment(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfSegments':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfSegments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'settingsFileName':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSettingsFileName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeoutLength':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTimeoutLength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeoutPollingInterval':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setTimeoutPollingInterval(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'uniqueName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUniqueName(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputTomography


class XSDataResultTomography(XSDataResult):
    subclass = None
    def __init__(self, numberOfSlices=None, overallTimeForReconstruction=None, reconstructionImageHeight=None, reconstructionImageWidth=None, reconstructionTimePerChunk=None, sinogramCreationTimePerChunk=None, sliceDirectory=None, voxelDepthScale=None, voxelHeightScale=None, voxelWidthScale=None, status=None):
        XSDataResult.__init__(self, status)
        self.numberOfSlices = numberOfSlices
        self.overallTimeForReconstruction = overallTimeForReconstruction
        self.reconstructionImageHeight = reconstructionImageHeight
        self.reconstructionImageWidth = reconstructionImageWidth
        if reconstructionTimePerChunk is None:
            self.reconstructionTimePerChunk = []
        else:
            self.reconstructionTimePerChunk = reconstructionTimePerChunk
        if sinogramCreationTimePerChunk is None:
            self.sinogramCreationTimePerChunk = []
        else:
            self.sinogramCreationTimePerChunk = sinogramCreationTimePerChunk
        self.sliceDirectory = sliceDirectory
        self.voxelDepthScale = voxelDepthScale
        self.voxelHeightScale = voxelHeightScale
        self.voxelWidthScale = voxelWidthScale
    def factory(*args_, **kwargs_):
        if XSDataResultTomography.subclass:
            return XSDataResultTomography.subclass(*args_, **kwargs_)
        else:
            return XSDataResultTomography(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberOfSlices(self): return self.numberOfSlices
    def setNumberOfSlices(self, numberOfSlices): self.numberOfSlices = numberOfSlices
    def getOverallTimeForReconstruction(self): return self.overallTimeForReconstruction
    def setOverallTimeForReconstruction(self, overallTimeForReconstruction): self.overallTimeForReconstruction = overallTimeForReconstruction
    def getReconstructionImageHeight(self): return self.reconstructionImageHeight
    def setReconstructionImageHeight(self, reconstructionImageHeight): self.reconstructionImageHeight = reconstructionImageHeight
    def getReconstructionImageWidth(self): return self.reconstructionImageWidth
    def setReconstructionImageWidth(self, reconstructionImageWidth): self.reconstructionImageWidth = reconstructionImageWidth
    def getReconstructionTimePerChunk(self): return self.reconstructionTimePerChunk
    def setReconstructionTimePerChunk(self, reconstructionTimePerChunk): self.reconstructionTimePerChunk = reconstructionTimePerChunk
    def addReconstructionTimePerChunk(self, value): self.reconstructionTimePerChunk.append(value)
    def insertReconstructionTimePerChunk(self, index, value): self.reconstructionTimePerChunk[index] = value
    def getSinogramCreationTimePerChunk(self): return self.sinogramCreationTimePerChunk
    def setSinogramCreationTimePerChunk(self, sinogramCreationTimePerChunk): self.sinogramCreationTimePerChunk = sinogramCreationTimePerChunk
    def addSinogramCreationTimePerChunk(self, value): self.sinogramCreationTimePerChunk.append(value)
    def insertSinogramCreationTimePerChunk(self, index, value): self.sinogramCreationTimePerChunk[index] = value
    def getSliceDirectory(self): return self.sliceDirectory
    def setSliceDirectory(self, sliceDirectory): self.sliceDirectory = sliceDirectory
    def getVoxelDepthScale(self): return self.voxelDepthScale
    def setVoxelDepthScale(self, voxelDepthScale): self.voxelDepthScale = voxelDepthScale
    def getVoxelHeightScale(self): return self.voxelHeightScale
    def setVoxelHeightScale(self, voxelHeightScale): self.voxelHeightScale = voxelHeightScale
    def getVoxelWidthScale(self): return self.voxelWidthScale
    def setVoxelWidthScale(self, voxelWidthScale): self.voxelWidthScale = voxelWidthScale
    def export(self, outfile, level, name_='XSDataResultTomography'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultTomography'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultTomography')
    def exportChildren(self, outfile, level, name_='XSDataResultTomography'):
        if self.numberOfSlices:
            self.numberOfSlices.export(outfile, level, name_='numberOfSlices')
        if self.overallTimeForReconstruction:
            self.overallTimeForReconstruction.export(outfile, level, name_='overallTimeForReconstruction')
        if self.reconstructionImageHeight:
            self.reconstructionImageHeight.export(outfile, level, name_='reconstructionImageHeight')
        if self.reconstructionImageWidth:
            self.reconstructionImageWidth.export(outfile, level, name_='reconstructionImageWidth')
        for reconstructionTimePerChunk_ in self.getReconstructionTimePerChunk():
            reconstructionTimePerChunk_.export(outfile, level, name_='reconstructionTimePerChunk')
        for sinogramCreationTimePerChunk_ in self.getSinogramCreationTimePerChunk():
            sinogramCreationTimePerChunk_.export(outfile, level, name_='sinogramCreationTimePerChunk')
        if self.sliceDirectory:
            self.sliceDirectory.export(outfile, level, name_='sliceDirectory')
        if self.voxelDepthScale:
            self.voxelDepthScale.export(outfile, level, name_='voxelDepthScale')
        if self.voxelHeightScale:
            self.voxelHeightScale.export(outfile, level, name_='voxelHeightScale')
        if self.voxelWidthScale:
            self.voxelWidthScale.export(outfile, level, name_='voxelWidthScale')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultTomography' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultTomography.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultTomography.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultTomography" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultTomography'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.numberOfSlices:
            showIndent(outfile, level)
            outfile.write('numberOfSlices=XSDataInteger(\n')
            self.numberOfSlices.exportLiteral(outfile, level, name_='numberOfSlices')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.overallTimeForReconstruction:
            showIndent(outfile, level)
            outfile.write('overallTimeForReconstruction=XSDataFloat(\n')
            self.overallTimeForReconstruction.exportLiteral(outfile, level, name_='overallTimeForReconstruction')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.reconstructionImageHeight:
            showIndent(outfile, level)
            outfile.write('reconstructionImageHeight=XSDataInteger(\n')
            self.reconstructionImageHeight.exportLiteral(outfile, level, name_='reconstructionImageHeight')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.reconstructionImageWidth:
            showIndent(outfile, level)
            outfile.write('reconstructionImageWidth=XSDataInteger(\n')
            self.reconstructionImageWidth.exportLiteral(outfile, level, name_='reconstructionImageWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('reconstructionTimePerChunk=[\n')
        level += 1
        for reconstructionTimePerChunk in self.reconstructionTimePerChunk:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            reconstructionTimePerChunk.exportLiteral(outfile, level, name_='reconstructionTimePerChunk')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('sinogramCreationTimePerChunk=[\n')
        level += 1
        for sinogramCreationTimePerChunk in self.sinogramCreationTimePerChunk:
            showIndent(outfile, level)
            outfile.write('XSDataFloat(\n')
            sinogramCreationTimePerChunk.exportLiteral(outfile, level, name_='sinogramCreationTimePerChunk')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.sliceDirectory:
            showIndent(outfile, level)
            outfile.write('sliceDirectory=XSDataFile(\n')
            self.sliceDirectory.exportLiteral(outfile, level, name_='sliceDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.voxelDepthScale:
            showIndent(outfile, level)
            outfile.write('voxelDepthScale=XSDataFloat(\n')
            self.voxelDepthScale.exportLiteral(outfile, level, name_='voxelDepthScale')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.voxelHeightScale:
            showIndent(outfile, level)
            outfile.write('voxelHeightScale=XSDataFloat(\n')
            self.voxelHeightScale.exportLiteral(outfile, level, name_='voxelHeightScale')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.voxelWidthScale:
            showIndent(outfile, level)
            outfile.write('voxelWidthScale=XSDataFloat(\n')
            self.voxelWidthScale.exportLiteral(outfile, level, name_='voxelWidthScale')
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
            nodeName_ == 'numberOfSlices':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfSlices(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallTimeForReconstruction':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setOverallTimeForReconstruction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reconstructionImageHeight':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setReconstructionImageHeight(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reconstructionImageWidth':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setReconstructionImageWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reconstructionTimePerChunk':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.reconstructionTimePerChunk.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sinogramCreationTimePerChunk':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.sinogramCreationTimePerChunk.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sliceDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setSliceDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'voxelDepthScale':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setVoxelDepthScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'voxelHeightScale':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setVoxelHeightScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'voxelWidthScale':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setVoxelWidthScale(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
# end class XSDataResultTomography


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
        elif name == 'imageDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('imageDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageWidth':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('imageWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfImages':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfImages', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfSegments':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfSegments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'segmentHeight':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('segmentHeight', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'reconstructionCenter':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('reconstructionCenter', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sinogramDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('sinogramDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sinogramLength':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('sinogramLength', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sinogramWidth':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('sinogramWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'values':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('values', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfSlices':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfSlices', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sliceDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('sliceDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'byteDepthOfImage':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('byteDepthOfImage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chunkHeight':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('chunkHeight', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'jobName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('jobName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfChunks':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfChunks', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfProjectionsPerSegment':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfProjectionsPerSegment', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'settingsFileName':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('settingsFileName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'timeoutLength':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('timeoutLength', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'timeoutPollingInterval':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('timeoutPollingInterval', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'uniqueName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('uniqueName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'overallTimeForReconstruction':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('overallTimeForReconstruction', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'reconstructionImageHeight':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('reconstructionImageHeight', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'reconstructionImageWidth':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('reconstructionImageWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'reconstructionTimePerChunk':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('reconstructionTimePerChunk', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sinogramCreationTimePerChunk':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('sinogramCreationTimePerChunk', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'voxelDepthScale':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('voxelDepthScale', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'voxelHeightScale':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('voxelHeightScale', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'voxelWidthScale':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('voxelWidthScale', obj)
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
        elif name == 'imageDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfImages':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfImages(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfSegments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfSegments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'segmentHeight':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSegmentHeight(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'reconstructionCenter':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReconstructionCenter(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sinogramDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSinogramDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sinogramLength':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSinogramLength(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sinogramWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSinogramWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'values':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addValues(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfSlices':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfSlices(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sliceDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSliceDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'byteDepthOfImage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setByteDepthOfImage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chunkHeight':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setChunkHeight(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'jobName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setJobName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfChunks':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfChunks(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfProjectionsPerSegment':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfProjectionsPerSegment(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'settingsFileName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSettingsFileName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'timeoutLength':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTimeoutLength(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'timeoutPollingInterval':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTimeoutPollingInterval(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'uniqueName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUniqueName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'overallTimeForReconstruction':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOverallTimeForReconstruction(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'reconstructionImageHeight':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReconstructionImageHeight(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'reconstructionImageWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setReconstructionImageWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'reconstructionTimePerChunk':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addReconstructionTimePerChunk(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sinogramCreationTimePerChunk':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSinogramCreationTimePerChunk(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'voxelDepthScale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVoxelDepthScale(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'voxelHeightScale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVoxelHeightScale(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'voxelWidthScale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVoxelWidthScale(self.stack[-1].obj)
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
    sys.stdout.write('from XSDataTomo import *\n\n')
    sys.stdout.write('rootObj = XSDataDouble(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSDataDouble")
    sys.stdout.write(')\n')
    return rootObj

class XSDataTomo:
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

