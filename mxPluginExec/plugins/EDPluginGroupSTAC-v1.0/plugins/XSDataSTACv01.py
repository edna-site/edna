#!/usr/bin/env python

#
# Generated Wed May 13 00:33:28 2009 by EDGenerateDS.py.
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

class mosflm_commands:
    subclass = None
    def __init__(self, command=None):
        if command is None:
            self.command = []
        else:
            self.command = command
    def factory(*args_, **kwargs_):
        if mosflm_commands.subclass:
            return mosflm_commands.subclass(*args_, **kwargs_)
        else:
            return mosflm_commands(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCommand(self): return self.command
    def setCommand(self, command): self.command = command
    def addCommand(self, value): self.command.append(value)
    def insertCommand(self, index, value): self.command[index] = value
    def export(self, outfile, level, name_='mosflm_commands'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='mosflm_commands'):
        pass
    def exportChildren(self, outfile, level, name_='mosflm_commands'):
        for command_ in self.getCommand():
            showIndent(outfile, level)
            outfile.write('<command>%s</command>\n' % quote_xml(command_))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='mosflm_commands' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = mosflm_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = mosflm_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="mosflm_commands" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='mosflm_commands'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('command=[\n')
        level += 1
        for command in self.command:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(command))
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
            nodeName_ == 'command':
            command_ = ''
            for text__content_ in child_.childNodes:
                command_ += text__content_.nodeValue
            self.command.append(command_)
# end class mosflm_commands


class scala_commands:
    subclass = None
    def __init__(self, command=None):
        if command is None:
            self.command = []
        else:
            self.command = command
    def factory(*args_, **kwargs_):
        if scala_commands.subclass:
            return scala_commands.subclass(*args_, **kwargs_)
        else:
            return scala_commands(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCommand(self): return self.command
    def setCommand(self, command): self.command = command
    def addCommand(self, value): self.command.append(value)
    def insertCommand(self, index, value): self.command[index] = value
    def export(self, outfile, level, name_='scala_commands'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='scala_commands'):
        pass
    def exportChildren(self, outfile, level, name_='scala_commands'):
        for command_ in self.getCommand():
            showIndent(outfile, level)
            outfile.write('<command>%s</command>\n' % quote_xml(command_))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='scala_commands' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = scala_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = scala_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="scala_commands" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='scala_commands'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('command=[\n')
        level += 1
        for command in self.command:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(command))
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
            nodeName_ == 'command':
            command_ = ''
            for text__content_ in child_.childNodes:
                command_ += text__content_.nodeValue
            self.command.append(command_)
# end class scala_commands


class xds_commands:
    subclass = None
    def __init__(self, command=None):
        if command is None:
            self.command = []
        else:
            self.command = command
    def factory(*args_, **kwargs_):
        if xds_commands.subclass:
            return xds_commands.subclass(*args_, **kwargs_)
        else:
            return xds_commands(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCommand(self): return self.command
    def setCommand(self, command): self.command = command
    def addCommand(self, value): self.command.append(value)
    def insertCommand(self, index, value): self.command[index] = value
    def export(self, outfile, level, name_='xds_commands'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='xds_commands'):
        pass
    def exportChildren(self, outfile, level, name_='xds_commands'):
        for command_ in self.getCommand():
            showIndent(outfile, level)
            outfile.write('<command>%s</command>\n' % quote_xml(command_))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='xds_commands' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = xds_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = xds_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="xds_commands" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='xds_commands'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('command=[\n')
        level += 1
        for command in self.command:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(command))
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
            nodeName_ == 'command':
            command_ = ''
            for text__content_ in child_.childNodes:
                command_ += text__content_.nodeValue
            self.command.append(command_)
# end class xds_commands


class extra_commands:
    subclass = None
    def __init__(self, mosflm_commands=None, scala_commands=None, xds_commands=None):
        self.mosflm_commands = mosflm_commands
        self.scala_commands = scala_commands
        self.xds_commands = xds_commands
    def factory(*args_, **kwargs_):
        if extra_commands.subclass:
            return extra_commands.subclass(*args_, **kwargs_)
        else:
            return extra_commands(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMosflm_commands(self): return self.mosflm_commands
    def setMosflm_commands(self, mosflm_commands): self.mosflm_commands = mosflm_commands
    def getScala_commands(self): return self.scala_commands
    def setScala_commands(self, scala_commands): self.scala_commands = scala_commands
    def getXds_commands(self): return self.xds_commands
    def setXds_commands(self, xds_commands): self.xds_commands = xds_commands
    def export(self, outfile, level, name_='extra_commands'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='extra_commands'):
        pass
    def exportChildren(self, outfile, level, name_='extra_commands'):
        if self.getMosflm_commands() != None :
            if self.mosflm_commands:
                self.mosflm_commands.export(outfile, level)
        if self.getScala_commands() != None :
            if self.scala_commands:
                self.scala_commands.export(outfile, level)
        if self.getXds_commands() != None :
            if self.xds_commands:
                self.xds_commands.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='extra_commands' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = extra_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = extra_commands.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="extra_commands" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='extra_commands'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.mosflm_commands:
            showIndent(outfile, level)
            outfile.write('mosflm_commands=mosflm_commands(\n')
            self.mosflm_commands.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.scala_commands:
            showIndent(outfile, level)
            outfile.write('scala_commands=scala_commands(\n')
            self.scala_commands.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.xds_commands:
            showIndent(outfile, level)
            outfile.write('xds_commands=xds_commands(\n')
            self.xds_commands.exportLiteral(outfile, level)
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
            nodeName_ == 'mosflm_commands':
            obj_ = mosflm_commands.factory()
            obj_.build(child_)
            self.setMosflm_commands(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scala_commands':
            obj_ = scala_commands.factory()
            obj_.build(child_)
            self.setScala_commands(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_commands':
            obj_ = xds_commands.factory()
            obj_.build(child_)
            self.setXds_commands(obj_)
# end class extra_commands


class status:
    subclass = None
    def __init__(self, code='', message=''):
        self.code = code
        self.message = message
    def factory(*args_, **kwargs_):
        if status.subclass:
            return status.subclass(*args_, **kwargs_)
        else:
            return status(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def validate_status_code(self, value):
        # Validate type status_code, a restriction on xsd:string.
        pass
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def export(self, outfile, level, name_='status'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='status'):
        pass
    def exportChildren(self, outfile, level, name_='status'):
        showIndent(outfile, level)
        outfile.write('<code>%s</code>\n' % quote_xml(self.getCode()))
        if self.getMessage() != None :
            showIndent(outfile, level)
            outfile.write('<message>%s</message>\n' % quote_xml(self.getMessage()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='status' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = status.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = status.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="status" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='status'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('code=%s,\n' % quote_python(self.getCode()))
        showIndent(outfile, level)
        outfile.write('message=%s,\n' % quote_python(self.getMessage()))
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
            nodeName_ == 'code':
            code_ = ''
            for text__content_ in child_.childNodes:
                code_ += text__content_.nodeValue
            self.code = code_
            self.validate_status_code(self.code)    # validate type status_code
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            message_ = ''
            for text__content_ in child_.childNodes:
                message_ += text__content_.nodeValue
            self.message = message_
# end class status


class fileinfo:
    subclass = None
    def __init__(self, directory='', prefix='', suffix='', template='', run_number=''):
        self.directory = directory
        self.prefix = prefix
        self.suffix = suffix
        self.template = template
        self.run_number = run_number
    def factory(*args_, **kwargs_):
        if fileinfo.subclass:
            return fileinfo.subclass(*args_, **kwargs_)
        else:
            return fileinfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDirectory(self): return self.directory
    def setDirectory(self, directory): self.directory = directory
    def getPrefix(self): return self.prefix
    def setPrefix(self, prefix): self.prefix = prefix
    def getSuffix(self): return self.suffix
    def setSuffix(self, suffix): self.suffix = suffix
    def getTemplate(self): return self.template
    def setTemplate(self, template): self.template = template
    def getRun_number(self): return self.run_number
    def setRun_number(self, run_number): self.run_number = run_number
    def export(self, outfile, level, name_='fileinfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='fileinfo'):
        pass
    def exportChildren(self, outfile, level, name_='fileinfo'):
        showIndent(outfile, level)
        outfile.write('<directory>%s</directory>\n' % quote_xml(self.getDirectory()))
        if self.getPrefix() != None :
            showIndent(outfile, level)
            outfile.write('<prefix>%s</prefix>\n' % quote_xml(self.getPrefix()))
        if self.getSuffix() != None :
            showIndent(outfile, level)
            outfile.write('<suffix>%s</suffix>\n' % quote_xml(self.getSuffix()))
        if self.getTemplate() != None :
            showIndent(outfile, level)
            outfile.write('<template>%s</template>\n' % quote_xml(self.getTemplate()))
        if self.getRun_number() != None :
            showIndent(outfile, level)
            outfile.write('<run_number>%s</run_number>\n' % quote_xml(self.getRun_number()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='fileinfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = fileinfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = fileinfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="fileinfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='fileinfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('directory=%s,\n' % quote_python(self.getDirectory()))
        showIndent(outfile, level)
        outfile.write('prefix=%s,\n' % quote_python(self.getPrefix()))
        showIndent(outfile, level)
        outfile.write('suffix=%s,\n' % quote_python(self.getSuffix()))
        showIndent(outfile, level)
        outfile.write('template=%s,\n' % quote_python(self.getTemplate()))
        showIndent(outfile, level)
        outfile.write('run_number=%s,\n' % quote_python(self.getRun_number()))
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
            nodeName_ == 'directory':
            directory_ = ''
            for text__content_ in child_.childNodes:
                directory_ += text__content_.nodeValue
            self.directory = directory_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'prefix':
            prefix_ = ''
            for text__content_ in child_.childNodes:
                prefix_ += text__content_.nodeValue
            self.prefix = prefix_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'suffix':
            suffix_ = ''
            for text__content_ in child_.childNodes:
                suffix_ += text__content_.nodeValue
            self.suffix = suffix_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'template':
            template_ = ''
            for text__content_ in child_.childNodes:
                template_ += text__content_.nodeValue
            self.template = template_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'run_number':
            run_number_ = ''
            for text__content_ in child_.childNodes:
                run_number_ += text__content_.nodeValue
            self.run_number = run_number_
# end class fileinfo


class oscillation_sequence:
    subclass = None
    def __init__(self, start='', end='', range='', number_of_images='', overlap='', exposure_time='', start_image_number='', number_of_passes=''):
        self.start = start
        self.end = end
        self.range = range
        self.number_of_images = number_of_images
        self.overlap = overlap
        self.exposure_time = exposure_time
        self.start_image_number = start_image_number
        self.number_of_passes = number_of_passes
    def factory(*args_, **kwargs_):
        if oscillation_sequence.subclass:
            return oscillation_sequence.subclass(*args_, **kwargs_)
        else:
            return oscillation_sequence(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStart(self): return self.start
    def setStart(self, start): self.start = start
    def getEnd(self): return self.end
    def setEnd(self, end): self.end = end
    def getRange(self): return self.range
    def setRange(self, range): self.range = range
    def getNumber_of_images(self): return self.number_of_images
    def setNumber_of_images(self, number_of_images): self.number_of_images = number_of_images
    def getOverlap(self): return self.overlap
    def setOverlap(self, overlap): self.overlap = overlap
    def getExposure_time(self): return self.exposure_time
    def setExposure_time(self, exposure_time): self.exposure_time = exposure_time
    def getStart_image_number(self): return self.start_image_number
    def setStart_image_number(self, start_image_number): self.start_image_number = start_image_number
    def getNumber_of_passes(self): return self.number_of_passes
    def setNumber_of_passes(self, number_of_passes): self.number_of_passes = number_of_passes
    def export(self, outfile, level, name_='oscillation_sequence'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='oscillation_sequence'):
        pass
    def exportChildren(self, outfile, level, name_='oscillation_sequence'):
        if self.getStart() != None :
            showIndent(outfile, level)
            outfile.write('<start>%s</start>\n' % quote_xml(self.getStart()))
        if self.getEnd() != None :
            showIndent(outfile, level)
            outfile.write('<end>%s</end>\n' % quote_xml(self.getEnd()))
        if self.getRange() != None :
            showIndent(outfile, level)
            outfile.write('<range>%s</range>\n' % quote_xml(self.getRange()))
        if self.getNumber_of_images() != None :
            showIndent(outfile, level)
            outfile.write('<number_of_images>%s</number_of_images>\n' % quote_xml(self.getNumber_of_images()))
        if self.getOverlap() != None :
            showIndent(outfile, level)
            outfile.write('<overlap>%s</overlap>\n' % quote_xml(self.getOverlap()))
        if self.getExposure_time() != None :
            showIndent(outfile, level)
            outfile.write('<exposure_time>%s</exposure_time>\n' % quote_xml(self.getExposure_time()))
        if self.getStart_image_number() != None :
            showIndent(outfile, level)
            outfile.write('<start_image_number>%s</start_image_number>\n' % quote_xml(self.getStart_image_number()))
        if self.getNumber_of_passes() != None :
            showIndent(outfile, level)
            outfile.write('<number_of_passes>%s</number_of_passes>\n' % quote_xml(self.getNumber_of_passes()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='oscillation_sequence' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = oscillation_sequence.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = oscillation_sequence.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="oscillation_sequence" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='oscillation_sequence'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('start=%s,\n' % quote_python(self.getStart()))
        showIndent(outfile, level)
        outfile.write('end=%s,\n' % quote_python(self.getEnd()))
        showIndent(outfile, level)
        outfile.write('range=%s,\n' % quote_python(self.getRange()))
        showIndent(outfile, level)
        outfile.write('number_of_images=%s,\n' % quote_python(self.getNumber_of_images()))
        showIndent(outfile, level)
        outfile.write('overlap=%s,\n' % quote_python(self.getOverlap()))
        showIndent(outfile, level)
        outfile.write('exposure_time=%s,\n' % quote_python(self.getExposure_time()))
        showIndent(outfile, level)
        outfile.write('start_image_number=%s,\n' % quote_python(self.getStart_image_number()))
        showIndent(outfile, level)
        outfile.write('number_of_passes=%s,\n' % quote_python(self.getNumber_of_passes()))
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
            nodeName_ == 'start':
            start_ = ''
            for text__content_ in child_.childNodes:
                start_ += text__content_.nodeValue
            self.start = start_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end':
            end_ = ''
            for text__content_ in child_.childNodes:
                end_ += text__content_.nodeValue
            self.end = end_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'range':
            range_ = ''
            for text__content_ in child_.childNodes:
                range_ += text__content_.nodeValue
            self.range = range_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number_of_images':
            number_of_images_ = ''
            for text__content_ in child_.childNodes:
                number_of_images_ += text__content_.nodeValue
            self.number_of_images = number_of_images_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlap':
            overlap_ = ''
            for text__content_ in child_.childNodes:
                overlap_ += text__content_.nodeValue
            self.overlap = overlap_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposure_time':
            exposure_time_ = ''
            for text__content_ in child_.childNodes:
                exposure_time_ += text__content_.nodeValue
            self.exposure_time = exposure_time_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image_number':
            start_image_number_ = ''
            for text__content_ in child_.childNodes:
                start_image_number_ += text__content_.nodeValue
            self.start_image_number = start_image_number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number_of_passes':
            number_of_passes_ = ''
            for text__content_ in child_.childNodes:
                number_of_passes_ += text__content_.nodeValue
            self.number_of_passes = number_of_passes_
# end class oscillation_sequence


class detector:
    subclass = None
    def __init__(self, typexx='', suffix=''):
        self.typexx = typexx
        self.suffix = suffix
    def factory(*args_, **kwargs_):
        if detector.subclass:
            return detector.subclass(*args_, **kwargs_)
        else:
            return detector(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def getSuffix(self): return self.suffix
    def setSuffix(self, suffix): self.suffix = suffix
    def export(self, outfile, level, name_='detector'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='detector'):
        pass
    def exportChildren(self, outfile, level, name_='detector'):
        showIndent(outfile, level)
        outfile.write('<type>%s</type>\n' % quote_xml(self.getType()))
        if self.getSuffix() != None :
            showIndent(outfile, level)
            outfile.write('<suffix>%s</suffix>\n' % quote_xml(self.getSuffix()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='detector' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = detector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = detector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="detector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='detector'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('typexx=%s,\n' % quote_python(self.getType()))
        showIndent(outfile, level)
        outfile.write('suffix=%s,\n' % quote_python(self.getSuffix()))
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
            nodeName_ == 'type':
            type_ = ''
            for text__content_ in child_.childNodes:
                type_ += text__content_.nodeValue
            self.typexx = type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'suffix':
            suffix_ = ''
            for text__content_ in child_.childNodes:
                suffix_ += text__content_.nodeValue
            self.suffix = suffix_
# end class detector


class beam:
    subclass = None
    def __init__(self, x='', y=''):
        self.x = x
        self.y = y
    def factory(*args_, **kwargs_):
        if beam.subclass:
            return beam.subclass(*args_, **kwargs_)
        else:
            return beam(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getX(self): return self.x
    def setX(self, x): self.x = x
    def getY(self): return self.y
    def setY(self, y): self.y = y
    def export(self, outfile, level, name_='beam'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='beam'):
        pass
    def exportChildren(self, outfile, level, name_='beam'):
        showIndent(outfile, level)
        outfile.write('<x>%s</x>\n' % quote_xml(self.getX()))
        showIndent(outfile, level)
        outfile.write('<y>%s</y>\n' % quote_xml(self.getY()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='beam' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = beam.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = beam.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="beam" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='beam'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('x=%s,\n' % quote_python(self.getX()))
        showIndent(outfile, level)
        outfile.write('y=%s,\n' % quote_python(self.getY()))
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
            nodeName_ == 'x':
            x_ = ''
            for text__content_ in child_.childNodes:
                x_ += text__content_.nodeValue
            self.x = x_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            y_ = ''
            for text__content_ in child_.childNodes:
                y_ += text__content_.nodeValue
            self.y = y_
# end class beam


class cell:
    subclass = None
    def __init__(self, a='', b='', c='', alpha='', beta='', gamma=''):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
    def factory(*args_, **kwargs_):
        if cell.subclass:
            return cell.subclass(*args_, **kwargs_)
        else:
            return cell(*args_, **kwargs_)
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
    def export(self, outfile, level, name_='cell'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='cell'):
        pass
    def exportChildren(self, outfile, level, name_='cell'):
        showIndent(outfile, level)
        outfile.write('<a>%s</a>\n' % quote_xml(self.getA()))
        showIndent(outfile, level)
        outfile.write('<b>%s</b>\n' % quote_xml(self.getB()))
        showIndent(outfile, level)
        outfile.write('<c>%s</c>\n' % quote_xml(self.getC()))
        showIndent(outfile, level)
        outfile.write('<alpha>%s</alpha>\n' % quote_xml(self.getAlpha()))
        showIndent(outfile, level)
        outfile.write('<beta>%s</beta>\n' % quote_xml(self.getBeta()))
        showIndent(outfile, level)
        outfile.write('<gamma>%s</gamma>\n' % quote_xml(self.getGamma()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='cell' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = cell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = cell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="cell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='cell'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('a=%s,\n' % quote_python(self.getA()))
        showIndent(outfile, level)
        outfile.write('b=%s,\n' % quote_python(self.getB()))
        showIndent(outfile, level)
        outfile.write('c=%s,\n' % quote_python(self.getC()))
        showIndent(outfile, level)
        outfile.write('alpha=%s,\n' % quote_python(self.getAlpha()))
        showIndent(outfile, level)
        outfile.write('beta=%s,\n' % quote_python(self.getBeta()))
        showIndent(outfile, level)
        outfile.write('gamma=%s,\n' % quote_python(self.getGamma()))
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
            nodeName_ == 'a':
            a_ = ''
            for text__content_ in child_.childNodes:
                a_ += text__content_.nodeValue
            self.a = a_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'b':
            b_ = ''
            for text__content_ in child_.childNodes:
                b_ += text__content_.nodeValue
            self.b = b_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'c':
            c_ = ''
            for text__content_ in child_.childNodes:
                c_ += text__content_.nodeValue
            self.c = c_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'alpha':
            alpha_ = ''
            for text__content_ in child_.childNodes:
                alpha_ += text__content_.nodeValue
            self.alpha = alpha_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beta':
            beta_ = ''
            for text__content_ in child_.childNodes:
                beta_ += text__content_.nodeValue
            self.beta = beta_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gamma':
            gamma_ = ''
            for text__content_ in child_.childNodes:
                gamma_ += text__content_.nodeValue
            self.gamma = gamma_
# end class cell


class experiment:
    subclass = None
    def __init__(self, wavelength='', distance='', resolution=None):
        self.wavelength = wavelength
        self.distance = distance
        self.resolution = resolution
    def factory(*args_, **kwargs_):
        if experiment.subclass:
            return experiment.subclass(*args_, **kwargs_)
        else:
            return experiment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getWavelength(self): return self.wavelength
    def setWavelength(self, wavelength): self.wavelength = wavelength
    def getDistance(self): return self.distance
    def setDistance(self, distance): self.distance = distance
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def export(self, outfile, level, name_='experiment'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='experiment'):
        pass
    def exportChildren(self, outfile, level, name_='experiment'):
        showIndent(outfile, level)
        outfile.write('<wavelength>%s</wavelength>\n' % quote_xml(self.getWavelength()))
        showIndent(outfile, level)
        outfile.write('<distance>%s</distance>\n' % quote_xml(self.getDistance()))
        if self.getResolution() != None :
            if self.resolution:
                self.resolution.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='experiment' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = experiment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = experiment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="experiment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='experiment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('wavelength=%s,\n' % quote_python(self.getWavelength()))
        showIndent(outfile, level)
        outfile.write('distance=%s,\n' % quote_python(self.getDistance()))
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=resolution(\n')
            self.resolution.exportLiteral(outfile, level)
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
            nodeName_ == 'wavelength':
            wavelength_ = ''
            for text__content_ in child_.childNodes:
                wavelength_ += text__content_.nodeValue
            self.wavelength = wavelength_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            distance_ = ''
            for text__content_ in child_.childNodes:
                distance_ += text__content_.nodeValue
            self.distance = distance_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = resolution.factory()
            obj_.build(child_)
            self.setResolution(obj_)
# end class experiment


class matrix:
    subclass = None
    def __init__(self, e11='', e12='', e13='', e21='', e22='', e23='', e31='', e32='', e33=''):
        self.e11 = e11
        self.e12 = e12
        self.e13 = e13
        self.e21 = e21
        self.e22 = e22
        self.e23 = e23
        self.e31 = e31
        self.e32 = e32
        self.e33 = e33
    def factory(*args_, **kwargs_):
        if matrix.subclass:
            return matrix.subclass(*args_, **kwargs_)
        else:
            return matrix(*args_, **kwargs_)
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
    def export(self, outfile, level, name_='matrix'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='matrix'):
        pass
    def exportChildren(self, outfile, level, name_='matrix'):
        showIndent(outfile, level)
        outfile.write('<e11>%s</e11>\n' % quote_xml(self.getE11()))
        showIndent(outfile, level)
        outfile.write('<e12>%s</e12>\n' % quote_xml(self.getE12()))
        showIndent(outfile, level)
        outfile.write('<e13>%s</e13>\n' % quote_xml(self.getE13()))
        showIndent(outfile, level)
        outfile.write('<e21>%s</e21>\n' % quote_xml(self.getE21()))
        showIndent(outfile, level)
        outfile.write('<e22>%s</e22>\n' % quote_xml(self.getE22()))
        showIndent(outfile, level)
        outfile.write('<e23>%s</e23>\n' % quote_xml(self.getE23()))
        showIndent(outfile, level)
        outfile.write('<e31>%s</e31>\n' % quote_xml(self.getE31()))
        showIndent(outfile, level)
        outfile.write('<e32>%s</e32>\n' % quote_xml(self.getE32()))
        showIndent(outfile, level)
        outfile.write('<e33>%s</e33>\n' % quote_xml(self.getE33()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='matrix' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = matrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = matrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="matrix" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='matrix'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('e11=%s,\n' % quote_python(self.getE11()))
        showIndent(outfile, level)
        outfile.write('e12=%s,\n' % quote_python(self.getE12()))
        showIndent(outfile, level)
        outfile.write('e13=%s,\n' % quote_python(self.getE13()))
        showIndent(outfile, level)
        outfile.write('e21=%s,\n' % quote_python(self.getE21()))
        showIndent(outfile, level)
        outfile.write('e22=%s,\n' % quote_python(self.getE22()))
        showIndent(outfile, level)
        outfile.write('e23=%s,\n' % quote_python(self.getE23()))
        showIndent(outfile, level)
        outfile.write('e31=%s,\n' % quote_python(self.getE31()))
        showIndent(outfile, level)
        outfile.write('e32=%s,\n' % quote_python(self.getE32()))
        showIndent(outfile, level)
        outfile.write('e33=%s,\n' % quote_python(self.getE33()))
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
            nodeName_ == 'e11':
            e11_ = ''
            for text__content_ in child_.childNodes:
                e11_ += text__content_.nodeValue
            self.e11 = e11_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e12':
            e12_ = ''
            for text__content_ in child_.childNodes:
                e12_ += text__content_.nodeValue
            self.e12 = e12_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e13':
            e13_ = ''
            for text__content_ in child_.childNodes:
                e13_ += text__content_.nodeValue
            self.e13 = e13_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e21':
            e21_ = ''
            for text__content_ in child_.childNodes:
                e21_ += text__content_.nodeValue
            self.e21 = e21_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e22':
            e22_ = ''
            for text__content_ in child_.childNodes:
                e22_ += text__content_.nodeValue
            self.e22 = e22_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e23':
            e23_ = ''
            for text__content_ in child_.childNodes:
                e23_ += text__content_.nodeValue
            self.e23 = e23_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e31':
            e31_ = ''
            for text__content_ in child_.childNodes:
                e31_ += text__content_.nodeValue
            self.e31 = e31_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e32':
            e32_ = ''
            for text__content_ in child_.childNodes:
                e32_ += text__content_.nodeValue
            self.e32 = e32_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'e33':
            e33_ = ''
            for text__content_ in child_.childNodes:
                e33_ += text__content_.nodeValue
            self.e33 = e33_
# end class matrix


class dna_message:
    subclass = None
    def __init__(self, typexx='', content_type='', level='', message=''):
        self.typexx = typexx
        self.content_type = content_type
        self.level = level
        self.message = message
    def factory(*args_, **kwargs_):
        if dna_message.subclass:
            return dna_message.subclass(*args_, **kwargs_)
        else:
            return dna_message(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def getContent_type(self): return self.content_type
    def setContent_type(self, content_type): self.content_type = content_type
    def getLevel(self): return self.level
    def setLevel(self, level): self.level = level
    def getMessage(self): return self.message
    def setMessage(self, message): self.message = message
    def export(self, outfile, level, name_='dna_message'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='dna_message'):
        pass
    def exportChildren(self, outfile, level, name_='dna_message'):
        showIndent(outfile, level)
        outfile.write('<type>%s</type>\n' % quote_xml(self.getType()))
        if self.getContent_type() != None :
            showIndent(outfile, level)
            outfile.write('<content_type>%s</content_type>\n' % quote_xml(self.getContent_type()))
        if self.getLevel() != None :
            showIndent(outfile, level)
            outfile.write('<level>%s</level>\n' % quote_xml(self.getLevel()))
        showIndent(outfile, level)
        outfile.write('<message>%s</message>\n' % quote_xml(self.getMessage()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='dna_message' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = dna_message.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = dna_message.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="dna_message" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='dna_message'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('typexx=%s,\n' % quote_python(self.getType()))
        showIndent(outfile, level)
        outfile.write('content_type=%s,\n' % quote_python(self.getContent_type()))
        showIndent(outfile, level)
        outfile.write('level=%s,\n' % quote_python(self.getLevel()))
        showIndent(outfile, level)
        outfile.write('message=%s,\n' % quote_python(self.getMessage()))
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
            nodeName_ == 'type':
            type_ = ''
            for text__content_ in child_.childNodes:
                type_ += text__content_.nodeValue
            self.typexx = type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'content_type':
            content_type_ = ''
            for text__content_ in child_.childNodes:
                content_type_ += text__content_.nodeValue
            self.content_type = content_type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'level':
            level_ = ''
            for text__content_ in child_.childNodes:
                level_ += text__content_.nodeValue
            self.level = level_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'message':
            message_ = ''
            for text__content_ in child_.childNodes:
                message_ += text__content_.nodeValue
            self.message = message_
# end class dna_message


class input_reflections:
    subclass = None
    def __init__(self, hklin=None):
        if hklin is None:
            self.hklin = []
        else:
            self.hklin = hklin
    def factory(*args_, **kwargs_):
        if input_reflections.subclass:
            return input_reflections.subclass(*args_, **kwargs_)
        else:
            return input_reflections(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHklin(self): return self.hklin
    def setHklin(self, hklin): self.hklin = hklin
    def addHklin(self, value): self.hklin.append(value)
    def insertHklin(self, index, value): self.hklin[index] = value
    def export(self, outfile, level, name_='input_reflections'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='input_reflections'):
        pass
    def exportChildren(self, outfile, level, name_='input_reflections'):
        for hklin_ in self.getHklin():
            showIndent(outfile, level)
            outfile.write('<hklin>%s</hklin>\n' % quote_xml(hklin_))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='input_reflections' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = input_reflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = input_reflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="input_reflections" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='input_reflections'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('hklin=[\n')
        level += 1
        for hklin in self.hklin:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(hklin))
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
            nodeName_ == 'hklin':
            hklin_ = ''
            for text__content_ in child_.childNodes:
                hklin_ += text__content_.nodeValue
            self.hklin.append(hklin_)
# end class input_reflections


class output_reflections:
    subclass = None
    def __init__(self, hklout=''):
        self.hklout = hklout
    def factory(*args_, **kwargs_):
        if output_reflections.subclass:
            return output_reflections.subclass(*args_, **kwargs_)
        else:
            return output_reflections(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getHklout(self): return self.hklout
    def setHklout(self, hklout): self.hklout = hklout
    def export(self, outfile, level, name_='output_reflections'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='output_reflections'):
        pass
    def exportChildren(self, outfile, level, name_='output_reflections'):
        showIndent(outfile, level)
        outfile.write('<hklout>%s</hklout>\n' % quote_xml(self.getHklout()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='output_reflections' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = output_reflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = output_reflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="output_reflections" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='output_reflections'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('hklout=%s,\n' % quote_python(self.getHklout()))
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
            nodeName_ == 'hklout':
            hklout_ = ''
            for text__content_ in child_.childNodes:
                hklout_ += text__content_.nodeValue
            self.hklout = hklout_
# end class output_reflections


class resolution:
    subclass = None
    def __init__(self, lower='', upper=''):
        self.lower = lower
        self.upper = upper
    def factory(*args_, **kwargs_):
        if resolution.subclass:
            return resolution.subclass(*args_, **kwargs_)
        else:
            return resolution(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLower(self): return self.lower
    def setLower(self, lower): self.lower = lower
    def getUpper(self): return self.upper
    def setUpper(self, upper): self.upper = upper
    def export(self, outfile, level, name_='resolution'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='resolution'):
        pass
    def exportChildren(self, outfile, level, name_='resolution'):
        if self.getLower() != None :
            showIndent(outfile, level)
            outfile.write('<lower>%s</lower>\n' % quote_xml(self.getLower()))
        if self.getUpper() != None :
            showIndent(outfile, level)
            outfile.write('<upper>%s</upper>\n' % quote_xml(self.getUpper()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='resolution' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = resolution.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = resolution.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="resolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='resolution'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('lower=%s,\n' % quote_python(self.getLower()))
        showIndent(outfile, level)
        outfile.write('upper=%s,\n' % quote_python(self.getUpper()))
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
            nodeName_ == 'lower':
            lower_ = ''
            for text__content_ in child_.childNodes:
                lower_ += text__content_.nodeValue
            self.lower = lower_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'upper':
            upper_ = ''
            for text__content_ in child_.childNodes:
                upper_ += text__content_.nodeValue
            self.upper = upper_
# end class resolution


class abort_request:
    subclass = None
    def __init__(self, level=''):
        self.level = level
    def factory(*args_, **kwargs_):
        if abort_request.subclass:
            return abort_request.subclass(*args_, **kwargs_)
        else:
            return abort_request(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLevel(self): return self.level
    def setLevel(self, level): self.level = level
    def validate_abort_level(self, value):
        # Validate type abort_level, a restriction on xsd:string.
        pass
    def export(self, outfile, level, name_='abort_request'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='abort_request'):
        pass
    def exportChildren(self, outfile, level, name_='abort_request'):
        showIndent(outfile, level)
        outfile.write('<level>%s</level>\n' % quote_xml(self.getLevel()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='abort_request' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = abort_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = abort_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="abort_request" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='abort_request'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('level=%s,\n' % quote_python(self.getLevel()))
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
            nodeName_ == 'level':
            level_ = ''
            for text__content_ in child_.childNodes:
                level_ += text__content_.nodeValue
            self.level = level_
            self.validate_abort_level(self.level)    # validate type abort_level
# end class abort_request


class abort_response:
    subclass = None
    def __init__(self, status=None):
        self.status = status
    def factory(*args_, **kwargs_):
        if abort_response.subclass:
            return abort_response.subclass(*args_, **kwargs_)
        else:
            return abort_response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatus(self): return self.status
    def setStatus(self, status): self.status = status
    def export(self, outfile, level, name_='abort_response'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='abort_response'):
        pass
    def exportChildren(self, outfile, level, name_='abort_response'):
        if self.status:
            self.status.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='abort_response' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = abort_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = abort_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="abort_response" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='abort_response'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.status:
            showIndent(outfile, level)
            outfile.write('status=status(\n')
            self.status.exportLiteral(outfile, level)
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
            nodeName_ == 'status':
            obj_ = status.factory()
            obj_.build(child_)
            self.setStatus(obj_)
# end class abort_response


class sample_reference:
    subclass = None
    def __init__(self, code='', container_reference='', container_code='', sample_location='', blSampleId=''):
        self.code = code
        self.container_reference = container_reference
        self.container_code = container_code
        self.sample_location = sample_location
        self.blSampleId = blSampleId
    def factory(*args_, **kwargs_):
        if sample_reference.subclass:
            return sample_reference.subclass(*args_, **kwargs_)
        else:
            return sample_reference(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCode(self): return self.code
    def setCode(self, code): self.code = code
    def getContainer_reference(self): return self.container_reference
    def setContainer_reference(self, container_reference): self.container_reference = container_reference
    def getContainer_code(self): return self.container_code
    def setContainer_code(self, container_code): self.container_code = container_code
    def getSample_location(self): return self.sample_location
    def setSample_location(self, sample_location): self.sample_location = sample_location
    def getBlSampleId(self): return self.blSampleId
    def setBlSampleId(self, blSampleId): self.blSampleId = blSampleId
    def export(self, outfile, level, name_='sample_reference'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='sample_reference'):
        pass
    def exportChildren(self, outfile, level, name_='sample_reference'):
        if self.getCode() != None :
            showIndent(outfile, level)
            outfile.write('<code>%s</code>\n' % quote_xml(self.getCode()))
        if self.getContainer_reference() != None :
            showIndent(outfile, level)
            outfile.write('<container_reference>%s</container_reference>\n' % quote_xml(self.getContainer_reference()))
        if self.getContainer_code() != None :
            showIndent(outfile, level)
            outfile.write('<container_code>%s</container_code>\n' % quote_xml(self.getContainer_code()))
        if self.getSample_location() != None :
            showIndent(outfile, level)
            outfile.write('<sample_location>%s</sample_location>\n' % quote_xml(self.getSample_location()))
        if self.getBlSampleId() != None :
            showIndent(outfile, level)
            outfile.write('<blSampleId>%s</blSampleId>\n' % quote_xml(self.getBlSampleId()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='sample_reference' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = sample_reference.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = sample_reference.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="sample_reference" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='sample_reference'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('code=%s,\n' % quote_python(self.getCode()))
        showIndent(outfile, level)
        outfile.write('container_reference=%s,\n' % quote_python(self.getContainer_reference()))
        showIndent(outfile, level)
        outfile.write('container_code=%s,\n' % quote_python(self.getContainer_code()))
        showIndent(outfile, level)
        outfile.write('sample_location=%s,\n' % quote_python(self.getSample_location()))
        showIndent(outfile, level)
        outfile.write('blSampleId=%s,\n' % quote_python(self.getBlSampleId()))
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
            nodeName_ == 'code':
            code_ = ''
            for text__content_ in child_.childNodes:
                code_ += text__content_.nodeValue
            self.code = code_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'container_reference':
            container_reference_ = ''
            for text__content_ in child_.childNodes:
                container_reference_ += text__content_.nodeValue
            self.container_reference = container_reference_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'container_code':
            container_code_ = ''
            for text__content_ in child_.childNodes:
                container_code_ += text__content_.nodeValue
            self.container_code = container_code_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample_location':
            sample_location_ = ''
            for text__content_ in child_.childNodes:
                sample_location_ += text__content_.nodeValue
            self.sample_location = sample_location_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blSampleId':
            blSampleId_ = ''
            for text__content_ in child_.childNodes:
                blSampleId_ += text__content_.nodeValue
            self.blSampleId = blSampleId_
# end class sample_reference


class beamline_parameters:
    subclass = None
    def __init__(self, maximum_exposure='', minimum_exposure_time='', minimum_phi_speed='', maximum_phi_speed='', minimum_phi_oscillation=''):
        self.maximum_exposure = maximum_exposure
        self.minimum_exposure_time = minimum_exposure_time
        self.minimum_phi_speed = minimum_phi_speed
        self.maximum_phi_speed = maximum_phi_speed
        self.minimum_phi_oscillation = minimum_phi_oscillation
    def factory(*args_, **kwargs_):
        if beamline_parameters.subclass:
            return beamline_parameters.subclass(*args_, **kwargs_)
        else:
            return beamline_parameters(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMaximum_exposure(self): return self.maximum_exposure
    def setMaximum_exposure(self, maximum_exposure): self.maximum_exposure = maximum_exposure
    def getMinimum_exposure_time(self): return self.minimum_exposure_time
    def setMinimum_exposure_time(self, minimum_exposure_time): self.minimum_exposure_time = minimum_exposure_time
    def getMinimum_phi_speed(self): return self.minimum_phi_speed
    def setMinimum_phi_speed(self, minimum_phi_speed): self.minimum_phi_speed = minimum_phi_speed
    def getMaximum_phi_speed(self): return self.maximum_phi_speed
    def setMaximum_phi_speed(self, maximum_phi_speed): self.maximum_phi_speed = maximum_phi_speed
    def getMinimum_phi_oscillation(self): return self.minimum_phi_oscillation
    def setMinimum_phi_oscillation(self, minimum_phi_oscillation): self.minimum_phi_oscillation = minimum_phi_oscillation
    def export(self, outfile, level, name_='beamline_parameters'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='beamline_parameters'):
        pass
    def exportChildren(self, outfile, level, name_='beamline_parameters'):
        if self.getMaximum_exposure() != None :
            showIndent(outfile, level)
            outfile.write('<maximum_exposure>%s</maximum_exposure>\n' % quote_xml(self.getMaximum_exposure()))
        if self.getMinimum_exposure_time() != None :
            showIndent(outfile, level)
            outfile.write('<minimum_exposure_time>%s</minimum_exposure_time>\n' % quote_xml(self.getMinimum_exposure_time()))
        if self.getMinimum_phi_speed() != None :
            showIndent(outfile, level)
            outfile.write('<minimum_phi_speed>%s</minimum_phi_speed>\n' % quote_xml(self.getMinimum_phi_speed()))
        if self.getMaximum_phi_speed() != None :
            showIndent(outfile, level)
            outfile.write('<maximum_phi_speed>%s</maximum_phi_speed>\n' % quote_xml(self.getMaximum_phi_speed()))
        if self.getMinimum_phi_oscillation() != None :
            showIndent(outfile, level)
            outfile.write('<minimum_phi_oscillation>%s</minimum_phi_oscillation>\n' % quote_xml(self.getMinimum_phi_oscillation()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='beamline_parameters' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = beamline_parameters.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = beamline_parameters.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="beamline_parameters" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='beamline_parameters'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('maximum_exposure=%s,\n' % quote_python(self.getMaximum_exposure()))
        showIndent(outfile, level)
        outfile.write('minimum_exposure_time=%s,\n' % quote_python(self.getMinimum_exposure_time()))
        showIndent(outfile, level)
        outfile.write('minimum_phi_speed=%s,\n' % quote_python(self.getMinimum_phi_speed()))
        showIndent(outfile, level)
        outfile.write('maximum_phi_speed=%s,\n' % quote_python(self.getMaximum_phi_speed()))
        showIndent(outfile, level)
        outfile.write('minimum_phi_oscillation=%s,\n' % quote_python(self.getMinimum_phi_oscillation()))
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
            nodeName_ == 'maximum_exposure':
            maximum_exposure_ = ''
            for text__content_ in child_.childNodes:
                maximum_exposure_ += text__content_.nodeValue
            self.maximum_exposure = maximum_exposure_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimum_exposure_time':
            minimum_exposure_time_ = ''
            for text__content_ in child_.childNodes:
                minimum_exposure_time_ += text__content_.nodeValue
            self.minimum_exposure_time = minimum_exposure_time_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimum_phi_speed':
            minimum_phi_speed_ = ''
            for text__content_ in child_.childNodes:
                minimum_phi_speed_ += text__content_.nodeValue
            self.minimum_phi_speed = minimum_phi_speed_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maximum_phi_speed':
            maximum_phi_speed_ = ''
            for text__content_ in child_.childNodes:
                maximum_phi_speed_ += text__content_.nodeValue
            self.maximum_phi_speed = maximum_phi_speed_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimum_phi_oscillation':
            minimum_phi_oscillation_ = ''
            for text__content_ in child_.childNodes:
                minimum_phi_oscillation_ += text__content_.nodeValue
            self.minimum_phi_oscillation = minimum_phi_oscillation_
# end class beamline_parameters


class strategy_request:
    subclass = None
    def __init__(self, extra_commands=None, strategy_settings=None, symmetry=''):
        self.extra_commands = extra_commands
        self.strategy_settings = strategy_settings
        self.symmetry = symmetry
    def factory(*args_, **kwargs_):
        if strategy_request.subclass:
            return strategy_request.subclass(*args_, **kwargs_)
        else:
            return strategy_request(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExtra_commands(self): return self.extra_commands
    def setExtra_commands(self, extra_commands): self.extra_commands = extra_commands
    def getStrategy_settings(self): return self.strategy_settings
    def setStrategy_settings(self, strategy_settings): self.strategy_settings = strategy_settings
    def getSymmetry(self): return self.symmetry
    def setSymmetry(self, symmetry): self.symmetry = symmetry
    def validate_spacegroup(self, value):
        # Validate type spacegroup, a restriction on xsd:string.
        pass
    def export(self, outfile, level, name_='strategy_request'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_request'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_request'):
        if self.getExtra_commands() != None :
            if self.extra_commands:
                self.extra_commands.export(outfile, level)
        if self.getStrategy_settings() != None :
            if self.strategy_settings:
                self.strategy_settings.export(outfile, level)
        if self.getSymmetry() != None :
            showIndent(outfile, level)
            outfile.write('<symmetry>%s</symmetry>\n' % quote_xml(self.getSymmetry()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_request' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_request" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_request'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.extra_commands:
            showIndent(outfile, level)
            outfile.write('extra_commands=extra_commands(\n')
            self.extra_commands.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategy_settings:
            showIndent(outfile, level)
            outfile.write('strategy_settings=strategy_settings(\n')
            self.strategy_settings.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('symmetry=%s,\n' % quote_python(self.getSymmetry()))
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
            nodeName_ == 'extra_commands':
            obj_ = extra_commands.factory()
            obj_.build(child_)
            self.setExtra_commands(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategy_settings':
            obj_ = strategy_settings.factory()
            obj_.build(child_)
            self.setStrategy_settings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            symmetry_ = ''
            for text__content_ in child_.childNodes:
                symmetry_ += text__content_.nodeValue
            self.symmetry = symmetry_
            self.validate_spacegroup(self.symmetry)    # validate type spacegroup
# end class strategy_request


class strategy_settings:
    subclass = None
    def __init__(self, resolution=None, overlap_limit='', completeness='', multiplicity='', i_over_sigma='', anomalous='', beamline_parameters=None, user_desired_minimum_phi_oscillation=''):
        self.resolution = resolution
        self.overlap_limit = overlap_limit
        self.completeness = completeness
        self.multiplicity = multiplicity
        self.i_over_sigma = i_over_sigma
        self.anomalous = anomalous
        self.beamline_parameters = beamline_parameters
        self.user_desired_minimum_phi_oscillation = user_desired_minimum_phi_oscillation
    def factory(*args_, **kwargs_):
        if strategy_settings.subclass:
            return strategy_settings.subclass(*args_, **kwargs_)
        else:
            return strategy_settings(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getOverlap_limit(self): return self.overlap_limit
    def setOverlap_limit(self, overlap_limit): self.overlap_limit = overlap_limit
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getI_over_sigma(self): return self.i_over_sigma
    def setI_over_sigma(self, i_over_sigma): self.i_over_sigma = i_over_sigma
    def getAnomalous(self): return self.anomalous
    def setAnomalous(self, anomalous): self.anomalous = anomalous
    def getBeamline_parameters(self): return self.beamline_parameters
    def setBeamline_parameters(self, beamline_parameters): self.beamline_parameters = beamline_parameters
    def getUser_desired_minimum_phi_oscillation(self): return self.user_desired_minimum_phi_oscillation
    def setUser_desired_minimum_phi_oscillation(self, user_desired_minimum_phi_oscillation): self.user_desired_minimum_phi_oscillation = user_desired_minimum_phi_oscillation
    def export(self, outfile, level, name_='strategy_settings'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_settings'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_settings'):
        if self.getResolution() != None :
            if self.resolution:
                self.resolution.export(outfile, level)
        if self.getOverlap_limit() != None :
            showIndent(outfile, level)
            outfile.write('<overlap_limit>%s</overlap_limit>\n' % quote_xml(self.getOverlap_limit()))
        if self.getCompleteness() != None :
            showIndent(outfile, level)
            outfile.write('<completeness>%s</completeness>\n' % quote_xml(self.getCompleteness()))
        if self.getMultiplicity() != None :
            showIndent(outfile, level)
            outfile.write('<multiplicity>%s</multiplicity>\n' % quote_xml(self.getMultiplicity()))
        if self.getI_over_sigma() != None :
            showIndent(outfile, level)
            outfile.write('<i_over_sigma>%s</i_over_sigma>\n' % quote_xml(self.getI_over_sigma()))
        if self.getAnomalous() != None :
            showIndent(outfile, level)
            outfile.write('<anomalous>%s</anomalous>\n' % quote_xml(self.getAnomalous()))
        if self.getBeamline_parameters() != None :
            if self.beamline_parameters:
                self.beamline_parameters.export(outfile, level)
        if self.getUser_desired_minimum_phi_oscillation() != None :
            showIndent(outfile, level)
            outfile.write('<user_desired_minimum_phi_oscillation>%s</user_desired_minimum_phi_oscillation>\n' % quote_xml(self.getUser_desired_minimum_phi_oscillation()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_settings' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_settings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_settings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_settings" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_settings'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=resolution(\n')
            self.resolution.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('overlap_limit=%s,\n' % quote_python(self.getOverlap_limit()))
        showIndent(outfile, level)
        outfile.write('completeness=%s,\n' % quote_python(self.getCompleteness()))
        showIndent(outfile, level)
        outfile.write('multiplicity=%s,\n' % quote_python(self.getMultiplicity()))
        showIndent(outfile, level)
        outfile.write('i_over_sigma=%s,\n' % quote_python(self.getI_over_sigma()))
        showIndent(outfile, level)
        outfile.write('anomalous=%s,\n' % quote_python(self.getAnomalous()))
        if self.beamline_parameters:
            showIndent(outfile, level)
            outfile.write('beamline_parameters=beamline_parameters(\n')
            self.beamline_parameters.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('user_desired_minimum_phi_oscillation=%s,\n' % quote_python(self.getUser_desired_minimum_phi_oscillation()))
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
            nodeName_ == 'resolution':
            obj_ = resolution.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlap_limit':
            overlap_limit_ = ''
            for text__content_ in child_.childNodes:
                overlap_limit_ += text__content_.nodeValue
            self.overlap_limit = overlap_limit_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            completeness_ = ''
            for text__content_ in child_.childNodes:
                completeness_ += text__content_.nodeValue
            self.completeness = completeness_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            multiplicity_ = ''
            for text__content_ in child_.childNodes:
                multiplicity_ += text__content_.nodeValue
            self.multiplicity = multiplicity_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i_over_sigma':
            i_over_sigma_ = ''
            for text__content_ in child_.childNodes:
                i_over_sigma_ += text__content_.nodeValue
            self.i_over_sigma = i_over_sigma_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            anomalous_ = ''
            for text__content_ in child_.childNodes:
                anomalous_ += text__content_.nodeValue
            self.anomalous = anomalous_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamline_parameters':
            obj_ = beamline_parameters.factory()
            obj_.build(child_)
            self.setBeamline_parameters(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'user_desired_minimum_phi_oscillation':
            user_desired_minimum_phi_oscillation_ = ''
            for text__content_ in child_.childNodes:
                user_desired_minimum_phi_oscillation_ += text__content_.nodeValue
            self.user_desired_minimum_phi_oscillation = user_desired_minimum_phi_oscillation_
# end class strategy_settings


class completeness:
    subclass = None
    def __init__(self, standard=''):
        self.standard = standard
    def factory(*args_, **kwargs_):
        if completeness.subclass:
            return completeness.subclass(*args_, **kwargs_)
        else:
            return completeness(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStandard(self): return self.standard
    def setStandard(self, standard): self.standard = standard
    def export(self, outfile, level, name_='completeness'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='completeness'):
        pass
    def exportChildren(self, outfile, level, name_='completeness'):
        showIndent(outfile, level)
        outfile.write('<standard>%s</standard>\n' % quote_xml(self.getStandard()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='completeness' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = completeness.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = completeness.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="completeness" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='completeness'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('standard=%s,\n' % quote_python(self.getStandard()))
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
            nodeName_ == 'standard':
            standard_ = ''
            for text__content_ in child_.childNodes:
                standard_ += text__content_.nodeValue
            self.standard = standard_
# end class completeness


class predicted_spots:
    subclass = None
    def __init__(self, full='', overlap=''):
        self.full = full
        self.overlap = overlap
    def factory(*args_, **kwargs_):
        if predicted_spots.subclass:
            return predicted_spots.subclass(*args_, **kwargs_)
        else:
            return predicted_spots(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFull(self): return self.full
    def setFull(self, full): self.full = full
    def validate_percentage(self, value):
        # Validate type percentage, a restriction on xsd:double.
        pass
    def getOverlap(self): return self.overlap
    def setOverlap(self, overlap): self.overlap = overlap
    def validate_percentage(self, value):
        # Validate type percentage, a restriction on xsd:double.
        pass
    def export(self, outfile, level, name_='predicted_spots'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='predicted_spots'):
        pass
    def exportChildren(self, outfile, level, name_='predicted_spots'):
        showIndent(outfile, level)
        outfile.write('<full>%s</full>\n' % quote_xml(self.getFull()))
        showIndent(outfile, level)
        outfile.write('<overlap>%s</overlap>\n' % quote_xml(self.getOverlap()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='predicted_spots' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = predicted_spots.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = predicted_spots.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="predicted_spots" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='predicted_spots'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('full=%s,\n' % quote_python(self.getFull()))
        showIndent(outfile, level)
        outfile.write('overlap=%s,\n' % quote_python(self.getOverlap()))
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
            nodeName_ == 'full':
            full_ = ''
            for text__content_ in child_.childNodes:
                full_ += text__content_.nodeValue
            self.full = full_
            self.validate_percentage(self.full)    # validate type percentage
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlap':
            overlap_ = ''
            for text__content_ in child_.childNodes:
                overlap_ += text__content_.nodeValue
            self.overlap = overlap_
            self.validate_percentage(self.overlap)    # validate type percentage
# end class predicted_spots


class segment:
    subclass = None
    def __init__(self, oscillation_sequence=None, predicted_spots=None):
        self.oscillation_sequence = oscillation_sequence
        self.predicted_spots = predicted_spots
    def factory(*args_, **kwargs_):
        if segment.subclass:
            return segment.subclass(*args_, **kwargs_)
        else:
            return segment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOscillation_sequence(self): return self.oscillation_sequence
    def setOscillation_sequence(self, oscillation_sequence): self.oscillation_sequence = oscillation_sequence
    def getPredicted_spots(self): return self.predicted_spots
    def setPredicted_spots(self, predicted_spots): self.predicted_spots = predicted_spots
    def export(self, outfile, level, name_='segment'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='segment'):
        pass
    def exportChildren(self, outfile, level, name_='segment'):
        if self.oscillation_sequence:
            self.oscillation_sequence.export(outfile, level)
        if self.getPredicted_spots() != None :
            if self.predicted_spots:
                self.predicted_spots.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='segment' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = segment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = segment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="segment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='segment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.oscillation_sequence:
            showIndent(outfile, level)
            outfile.write('oscillation_sequence=oscillation_sequence(\n')
            self.oscillation_sequence.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.predicted_spots:
            showIndent(outfile, level)
            outfile.write('predicted_spots=predicted_spots(\n')
            self.predicted_spots.exportLiteral(outfile, level)
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
            nodeName_ == 'oscillation_sequence':
            obj_ = oscillation_sequence.factory()
            obj_.build(child_)
            self.setOscillation_sequence(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'predicted_spots':
            obj_ = predicted_spots.factory()
            obj_.build(child_)
            self.setPredicted_spots(obj_)
# end class segment


class strategy_summary:
    subclass = None
    def __init__(self, number_of_segments='', segment=None):
        self.number_of_segments = number_of_segments
        if segment is None:
            self.segment = []
        else:
            self.segment = segment
    def factory(*args_, **kwargs_):
        if strategy_summary.subclass:
            return strategy_summary.subclass(*args_, **kwargs_)
        else:
            return strategy_summary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber_of_segments(self): return self.number_of_segments
    def setNumber_of_segments(self, number_of_segments): self.number_of_segments = number_of_segments
    def getSegment(self): return self.segment
    def setSegment(self, segment): self.segment = segment
    def addSegment(self, value): self.segment.append(value)
    def insertSegment(self, index, value): self.segment[index] = value
    def export(self, outfile, level, name_='strategy_summary'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_summary'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_summary'):
        showIndent(outfile, level)
        outfile.write('<number_of_segments>%s</number_of_segments>\n' % quote_xml(self.getNumber_of_segments()))
        for segment_ in self.getSegment():
            segment_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_summary' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_summary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_summary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_summary" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_summary'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('number_of_segments=%s,\n' % quote_python(self.getNumber_of_segments()))
        showIndent(outfile, level)
        outfile.write('segment=[\n')
        level += 1
        for segment in self.segment:
            showIndent(outfile, level)
            outfile.write('segment(\n')
            segment.exportLiteral(outfile, level)
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
            nodeName_ == 'number_of_segments':
            number_of_segments_ = ''
            for text__content_ in child_.childNodes:
                number_of_segments_ += text__content_.nodeValue
            self.number_of_segments = number_of_segments_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'segment':
            obj_ = segment.factory()
            obj_.build(child_)
            self.segment.append(obj_)
# end class strategy_summary


class strategy_interpretation:
    subclass = None
    def __init__(self, oscillation_sequence=None):
        if oscillation_sequence is None:
            self.oscillation_sequence = []
        else:
            self.oscillation_sequence = oscillation_sequence
    def factory(*args_, **kwargs_):
        if strategy_interpretation.subclass:
            return strategy_interpretation.subclass(*args_, **kwargs_)
        else:
            return strategy_interpretation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOscillation_sequence(self): return self.oscillation_sequence
    def setOscillation_sequence(self, oscillation_sequence): self.oscillation_sequence = oscillation_sequence
    def addOscillation_sequence(self, value): self.oscillation_sequence.append(value)
    def insertOscillation_sequence(self, index, value): self.oscillation_sequence[index] = value
    def export(self, outfile, level, name_='strategy_interpretation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_interpretation'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_interpretation'):
        for oscillation_sequence_ in self.getOscillation_sequence():
            oscillation_sequence_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_interpretation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_interpretation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_interpretation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_interpretation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_interpretation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('oscillation_sequence=[\n')
        level += 1
        for oscillation_sequence in self.oscillation_sequence:
            showIndent(outfile, level)
            outfile.write('oscillation_sequence(\n')
            oscillation_sequence.exportLiteral(outfile, level)
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
            nodeName_ == 'oscillation_sequence':
            obj_ = oscillation_sequence.factory()
            obj_.build(child_)
            self.oscillation_sequence.append(obj_)
# end class strategy_interpretation


class strategy_response:
    subclass = None
    def __init__(self, status=None, completeness=None, strategy_summary=None, segment=None, strategy_interpretation=None, strategy_statistics=None):
        self.status = status
        self.completeness = completeness
        if strategy_summary is None:
            self.strategy_summary = []
        else:
            self.strategy_summary = strategy_summary
        if segment is None:
            self.segment = []
        else:
            self.segment = segment
        self.strategy_interpretation = strategy_interpretation
        self.strategy_statistics = strategy_statistics
    def factory(*args_, **kwargs_):
        if strategy_response.subclass:
            return strategy_response.subclass(*args_, **kwargs_)
        else:
            return strategy_response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatus(self): return self.status
    def setStatus(self, status): self.status = status
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getStrategy_summary(self): return self.strategy_summary
    def setStrategy_summary(self, strategy_summary): self.strategy_summary = strategy_summary
    def addStrategy_summary(self, value): self.strategy_summary.append(value)
    def insertStrategy_summary(self, index, value): self.strategy_summary[index] = value
    def getSegment(self): return self.segment
    def setSegment(self, segment): self.segment = segment
    def addSegment(self, value): self.segment.append(value)
    def insertSegment(self, index, value): self.segment[index] = value
    def getStrategy_interpretation(self): return self.strategy_interpretation
    def setStrategy_interpretation(self, strategy_interpretation): self.strategy_interpretation = strategy_interpretation
    def getStrategy_statistics(self): return self.strategy_statistics
    def setStrategy_statistics(self, strategy_statistics): self.strategy_statistics = strategy_statistics
    def export(self, outfile, level, name_='strategy_response'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_response'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_response'):
        if self.status:
            self.status.export(outfile, level)
        if self.getCompleteness() != None :
            if self.completeness:
                self.completeness.export(outfile, level)
        for strategy_summary_ in self.getStrategy_summary():
            strategy_summary_.export(outfile, level)
        for segment_ in self.getSegment():
            segment_.export(outfile, level)
        if self.getStrategy_interpretation() != None :
            if self.strategy_interpretation:
                self.strategy_interpretation.export(outfile, level)
        if self.getStrategy_statistics() != None :
            if self.strategy_statistics:
                self.strategy_statistics.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_response' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_response" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_response'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.status:
            showIndent(outfile, level)
            outfile.write('status=status(\n')
            self.status.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=completeness(\n')
            self.completeness.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('strategy_summary=[\n')
        level += 1
        for strategy_summary in self.strategy_summary:
            showIndent(outfile, level)
            outfile.write('strategy_summary(\n')
            strategy_summary.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('segment=[\n')
        level += 1
        for segment in self.segment:
            showIndent(outfile, level)
            outfile.write('segment(\n')
            segment.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.strategy_interpretation:
            showIndent(outfile, level)
            outfile.write('strategy_interpretation=strategy_interpretation(\n')
            self.strategy_interpretation.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategy_statistics:
            showIndent(outfile, level)
            outfile.write('strategy_statistics=strategy_statistics(\n')
            self.strategy_statistics.exportLiteral(outfile, level)
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
            nodeName_ == 'status':
            obj_ = status.factory()
            obj_.build(child_)
            self.setStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = completeness.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategy_summary':
            obj_ = strategy_summary.factory()
            obj_.build(child_)
            self.strategy_summary.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'segment':
            obj_ = segment.factory()
            obj_.build(child_)
            self.segment.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategy_interpretation':
            obj_ = strategy_interpretation.factory()
            obj_.build(child_)
            self.setStrategy_interpretation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategy_statistics':
            obj_ = strategy_statistics.factory()
            obj_.build(child_)
            self.setStrategy_statistics(obj_)
# end class strategy_response


class strategy_statistics:
    subclass = None
    def __init__(self, r_merge='', i_over_sigma='', overloads='', max_overloads='', multiplicity='', completeness='', resolution='', ranking_resolution='', maximum_exposure=''):
        self.r_merge = r_merge
        self.i_over_sigma = i_over_sigma
        self.overloads = overloads
        self.max_overloads = max_overloads
        self.multiplicity = multiplicity
        self.completeness = completeness
        self.resolution = resolution
        self.ranking_resolution = ranking_resolution
        self.maximum_exposure = maximum_exposure
    def factory(*args_, **kwargs_):
        if strategy_statistics.subclass:
            return strategy_statistics.subclass(*args_, **kwargs_)
        else:
            return strategy_statistics(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getR_merge(self): return self.r_merge
    def setR_merge(self, r_merge): self.r_merge = r_merge
    def getI_over_sigma(self): return self.i_over_sigma
    def setI_over_sigma(self, i_over_sigma): self.i_over_sigma = i_over_sigma
    def getOverloads(self): return self.overloads
    def setOverloads(self, overloads): self.overloads = overloads
    def getMax_overloads(self): return self.max_overloads
    def setMax_overloads(self, max_overloads): self.max_overloads = max_overloads
    def getMultiplicity(self): return self.multiplicity
    def setMultiplicity(self, multiplicity): self.multiplicity = multiplicity
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getRanking_resolution(self): return self.ranking_resolution
    def setRanking_resolution(self, ranking_resolution): self.ranking_resolution = ranking_resolution
    def getMaximum_exposure(self): return self.maximum_exposure
    def setMaximum_exposure(self, maximum_exposure): self.maximum_exposure = maximum_exposure
    def export(self, outfile, level, name_='strategy_statistics'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='strategy_statistics'):
        pass
    def exportChildren(self, outfile, level, name_='strategy_statistics'):
        showIndent(outfile, level)
        outfile.write('<r_merge>%s</r_merge>\n' % quote_xml(self.getR_merge()))
        showIndent(outfile, level)
        outfile.write('<i_over_sigma>%s</i_over_sigma>\n' % quote_xml(self.getI_over_sigma()))
        showIndent(outfile, level)
        outfile.write('<overloads>%s</overloads>\n' % quote_xml(self.getOverloads()))
        showIndent(outfile, level)
        outfile.write('<max_overloads>%s</max_overloads>\n' % quote_xml(self.getMax_overloads()))
        showIndent(outfile, level)
        outfile.write('<multiplicity>%s</multiplicity>\n' % quote_xml(self.getMultiplicity()))
        showIndent(outfile, level)
        outfile.write('<completeness>%s</completeness>\n' % quote_xml(self.getCompleteness()))
        showIndent(outfile, level)
        outfile.write('<resolution>%s</resolution>\n' % quote_xml(self.getResolution()))
        showIndent(outfile, level)
        outfile.write('<ranking_resolution>%s</ranking_resolution>\n' % quote_xml(self.getRanking_resolution()))
        showIndent(outfile, level)
        outfile.write('<maximum_exposure>%s</maximum_exposure>\n' % quote_xml(self.getMaximum_exposure()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='strategy_statistics' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = strategy_statistics.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = strategy_statistics.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="strategy_statistics" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='strategy_statistics'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('r_merge=%s,\n' % quote_python(self.getR_merge()))
        showIndent(outfile, level)
        outfile.write('i_over_sigma=%s,\n' % quote_python(self.getI_over_sigma()))
        showIndent(outfile, level)
        outfile.write('overloads=%s,\n' % quote_python(self.getOverloads()))
        showIndent(outfile, level)
        outfile.write('max_overloads=%s,\n' % quote_python(self.getMax_overloads()))
        showIndent(outfile, level)
        outfile.write('multiplicity=%s,\n' % quote_python(self.getMultiplicity()))
        showIndent(outfile, level)
        outfile.write('completeness=%s,\n' % quote_python(self.getCompleteness()))
        showIndent(outfile, level)
        outfile.write('resolution=%s,\n' % quote_python(self.getResolution()))
        showIndent(outfile, level)
        outfile.write('ranking_resolution=%s,\n' % quote_python(self.getRanking_resolution()))
        showIndent(outfile, level)
        outfile.write('maximum_exposure=%s,\n' % quote_python(self.getMaximum_exposure()))
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
            nodeName_ == 'r_merge':
            r_merge_ = ''
            for text__content_ in child_.childNodes:
                r_merge_ += text__content_.nodeValue
            self.r_merge = r_merge_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i_over_sigma':
            i_over_sigma_ = ''
            for text__content_ in child_.childNodes:
                i_over_sigma_ += text__content_.nodeValue
            self.i_over_sigma = i_over_sigma_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overloads':
            overloads_ = ''
            for text__content_ in child_.childNodes:
                overloads_ += text__content_.nodeValue
            self.overloads = overloads_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'max_overloads':
            max_overloads_ = ''
            for text__content_ in child_.childNodes:
                max_overloads_ += text__content_.nodeValue
            self.max_overloads = max_overloads_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            multiplicity_ = ''
            for text__content_ in child_.childNodes:
                multiplicity_ += text__content_.nodeValue
            self.multiplicity = multiplicity_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            completeness_ = ''
            for text__content_ in child_.childNodes:
                completeness_ += text__content_.nodeValue
            self.completeness = completeness_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            resolution_ = ''
            for text__content_ in child_.childNodes:
                resolution_ += text__content_.nodeValue
            self.resolution = resolution_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ranking_resolution':
            ranking_resolution_ = ''
            for text__content_ in child_.childNodes:
                ranking_resolution_ += text__content_.nodeValue
            self.ranking_resolution = ranking_resolution_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maximum_exposure':
            maximum_exposure_ = ''
            for text__content_ in child_.childNodes:
                maximum_exposure_ += text__content_.nodeValue
            self.maximum_exposure = maximum_exposure_
# end class strategy_statistics


class kappa_alignment:
    subclass = None
    def __init__(self, v1='', v2='', close='', comment=''):
        self.v1 = v1
        self.v2 = v2
        self.close = close
        self.comment = comment
    def factory(*args_, **kwargs_):
        if kappa_alignment.subclass:
            return kappa_alignment.subclass(*args_, **kwargs_)
        else:
            return kappa_alignment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getClose(self): return self.close
    def setClose(self, close): self.close = close
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def export(self, outfile, level, name_='kappa_alignment'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_alignment'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_alignment'):
        showIndent(outfile, level)
        outfile.write('<v1>%s</v1>\n' % quote_xml(self.getV1()))
        showIndent(outfile, level)
        outfile.write('<v2>%s</v2>\n' % quote_xml(self.getV2()))
        showIndent(outfile, level)
        outfile.write('<close>%s</close>\n' % quote_xml(self.getClose()))
        showIndent(outfile, level)
        outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_alignment' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_alignment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_alignment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_alignment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_alignment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%s,\n' % quote_python(self.getV1()))
        showIndent(outfile, level)
        outfile.write('v2=%s,\n' % quote_python(self.getV2()))
        showIndent(outfile, level)
        outfile.write('close=%s,\n' % quote_python(self.getClose()))
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
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
            nodeName_ == 'v1':
            v1_ = ''
            for text__content_ in child_.childNodes:
                v1_ += text__content_.nodeValue
            self.v1 = v1_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            v2_ = ''
            for text__content_ in child_.childNodes:
                v2_ += text__content_.nodeValue
            self.v2 = v2_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'close':
            close_ = ''
            for text__content_ in child_.childNodes:
                close_ += text__content_.nodeValue
            self.close = close_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
# end class kappa_alignment


class kappa_alignment_request:
    subclass = None
    def __init__(self, desired_orientation=None, comment=''):
        if desired_orientation is None:
            self.desired_orientation = []
        else:
            self.desired_orientation = desired_orientation
        self.comment = comment
    def factory(*args_, **kwargs_):
        if kappa_alignment_request.subclass:
            return kappa_alignment_request.subclass(*args_, **kwargs_)
        else:
            return kappa_alignment_request(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDesired_orientation(self): return self.desired_orientation
    def setDesired_orientation(self, desired_orientation): self.desired_orientation = desired_orientation
    def addDesired_orientation(self, value): self.desired_orientation.append(value)
    def insertDesired_orientation(self, index, value): self.desired_orientation[index] = value
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def export(self, outfile, level, name_='kappa_alignment_request'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_alignment_request'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_alignment_request'):
        for desired_orientation_ in self.getDesired_orientation():
            desired_orientation_.export(outfile, level, name_='desired_orientation')
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_alignment_request' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_alignment_request" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_alignment_request'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('desired_orientation=[\n')
        level += 1
        for desired_orientation in self.desired_orientation:
            showIndent(outfile, level)
            outfile.write('kappa_alignment(\n')
            desired_orientation.exportLiteral(outfile, level, name_='desired_orientation')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
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
            nodeName_ == 'desired_orientation':
            obj_ = kappa_alignment.factory()
            obj_.build(child_)
            self.desired_orientation.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
# end class kappa_alignment_request


class kappa_possible_alignment:
    subclass = None
    def __init__(self, v1='', v2='', omega='', kappa='', phi='', trans='', rank=''):
        self.v1 = v1
        self.v2 = v2
        self.omega = omega
        self.kappa = kappa
        self.phi = phi
        self.trans = trans
        self.rank = rank
    def factory(*args_, **kwargs_):
        if kappa_possible_alignment.subclass:
            return kappa_possible_alignment.subclass(*args_, **kwargs_)
        else:
            return kappa_possible_alignment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getOmega(self): return self.omega
    def setOmega(self, omega): self.omega = omega
    def getKappa(self): return self.kappa
    def setKappa(self, kappa): self.kappa = kappa
    def getPhi(self): return self.phi
    def setPhi(self, phi): self.phi = phi
    def getTrans(self): return self.trans
    def setTrans(self, trans): self.trans = trans
    def getRank(self): return self.rank
    def setRank(self, rank): self.rank = rank
    def export(self, outfile, level, name_='kappa_possible_alignment'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_possible_alignment'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_possible_alignment'):
        showIndent(outfile, level)
        outfile.write('<v1>%s</v1>\n' % quote_xml(self.getV1()))
        showIndent(outfile, level)
        outfile.write('<v2>%s</v2>\n' % quote_xml(self.getV2()))
        showIndent(outfile, level)
        outfile.write('<omega>%s</omega>\n' % quote_xml(self.getOmega()))
        showIndent(outfile, level)
        outfile.write('<kappa>%s</kappa>\n' % quote_xml(self.getKappa()))
        showIndent(outfile, level)
        outfile.write('<phi>%s</phi>\n' % quote_xml(self.getPhi()))
        showIndent(outfile, level)
        outfile.write('<trans>%s</trans>\n' % quote_xml(self.getTrans()))
        showIndent(outfile, level)
        outfile.write('<rank>%s</rank>\n' % quote_xml(self.getRank()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_possible_alignment' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_possible_alignment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_possible_alignment.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_possible_alignment" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_possible_alignment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%s,\n' % quote_python(self.getV1()))
        showIndent(outfile, level)
        outfile.write('v2=%s,\n' % quote_python(self.getV2()))
        showIndent(outfile, level)
        outfile.write('omega=%s,\n' % quote_python(self.getOmega()))
        showIndent(outfile, level)
        outfile.write('kappa=%s,\n' % quote_python(self.getKappa()))
        showIndent(outfile, level)
        outfile.write('phi=%s,\n' % quote_python(self.getPhi()))
        showIndent(outfile, level)
        outfile.write('trans=%s,\n' % quote_python(self.getTrans()))
        showIndent(outfile, level)
        outfile.write('rank=%s,\n' % quote_python(self.getRank()))
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
            nodeName_ == 'v1':
            v1_ = ''
            for text__content_ in child_.childNodes:
                v1_ += text__content_.nodeValue
            self.v1 = v1_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            v2_ = ''
            for text__content_ in child_.childNodes:
                v2_ += text__content_.nodeValue
            self.v2 = v2_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omega':
            omega_ = ''
            for text__content_ in child_.childNodes:
                omega_ += text__content_.nodeValue
            self.omega = omega_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            kappa_ = ''
            for text__content_ in child_.childNodes:
                kappa_ += text__content_.nodeValue
            self.kappa = kappa_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            phi_ = ''
            for text__content_ in child_.childNodes:
                phi_ += text__content_.nodeValue
            self.phi = phi_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trans':
            trans_ = ''
            for text__content_ in child_.childNodes:
                trans_ += text__content_.nodeValue
            self.trans = trans_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rank':
            rank_ = ''
            for text__content_ in child_.childNodes:
                rank_ += text__content_.nodeValue
            self.rank = rank_
# end class kappa_possible_alignment


class kappa_alignment_response:
    subclass = None
    def __init__(self, status=None, comment='', possible_orientation=None):
        self.status = status
        self.comment = comment
        if possible_orientation is None:
            self.possible_orientation = []
        else:
            self.possible_orientation = possible_orientation
    def factory(*args_, **kwargs_):
        if kappa_alignment_response.subclass:
            return kappa_alignment_response.subclass(*args_, **kwargs_)
        else:
            return kappa_alignment_response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatus(self): return self.status
    def setStatus(self, status): self.status = status
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def getPossible_orientation(self): return self.possible_orientation
    def setPossible_orientation(self, possible_orientation): self.possible_orientation = possible_orientation
    def addPossible_orientation(self, value): self.possible_orientation.append(value)
    def insertPossible_orientation(self, index, value): self.possible_orientation[index] = value
    def export(self, outfile, level, name_='kappa_alignment_response'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_alignment_response'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_alignment_response'):
        if self.status:
            self.status.export(outfile, level)
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))
        for possible_orientation_ in self.getPossible_orientation():
            possible_orientation_.export(outfile, level, name_='possible_orientation')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_alignment_response' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_alignment_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_alignment_response" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_alignment_response'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.status:
            showIndent(outfile, level)
            outfile.write('status=status(\n')
            self.status.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
        showIndent(outfile, level)
        outfile.write('possible_orientation=[\n')
        level += 1
        for possible_orientation in self.possible_orientation:
            showIndent(outfile, level)
            outfile.write('kappa_possible_alignment(\n')
            possible_orientation.exportLiteral(outfile, level, name_='possible_orientation')
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
            nodeName_ == 'status':
            obj_ = status.factory()
            obj_.build(child_)
            self.setStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possible_orientation':
            obj_ = kappa_possible_alignment.factory()
            obj_.build(child_)
            self.possible_orientation.append(obj_)
# end class kappa_alignment_response


class kappa_strategy_request:
    subclass = None
    def __init__(self, comment='', desired_datum=None, standard_request=None):
        self.comment = comment
        if desired_datum is None:
            self.desired_datum = []
        else:
            self.desired_datum = desired_datum
        self.standard_request = standard_request
    def factory(*args_, **kwargs_):
        if kappa_strategy_request.subclass:
            return kappa_strategy_request.subclass(*args_, **kwargs_)
        else:
            return kappa_strategy_request(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def getDesired_datum(self): return self.desired_datum
    def setDesired_datum(self, desired_datum): self.desired_datum = desired_datum
    def addDesired_datum(self, value): self.desired_datum.append(value)
    def insertDesired_datum(self, index, value): self.desired_datum[index] = value
    def getStandard_request(self): return self.standard_request
    def setStandard_request(self, standard_request): self.standard_request = standard_request
    def export(self, outfile, level, name_='kappa_strategy_request'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_strategy_request'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_strategy_request'):
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))
        for desired_datum_ in self.getDesired_datum():
            desired_datum_.export(outfile, level, name_='desired_datum')
        if self.standard_request:
            self.standard_request.export(outfile, level, name_='standard_request')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_strategy_request' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_request.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_strategy_request" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_strategy_request'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
        showIndent(outfile, level)
        outfile.write('desired_datum=[\n')
        level += 1
        for desired_datum in self.desired_datum:
            showIndent(outfile, level)
            outfile.write('kappa_possible_alignment(\n')
            desired_datum.exportLiteral(outfile, level, name_='desired_datum')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.standard_request:
            showIndent(outfile, level)
            outfile.write('standard_request=strategy_request(\n')
            self.standard_request.exportLiteral(outfile, level, name_='standard_request')
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
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'desired_datum':
            obj_ = kappa_possible_alignment.factory()
            obj_.build(child_)
            self.desired_datum.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'standard_request':
            obj_ = strategy_request.factory()
            obj_.build(child_)
            self.setStandard_request(obj_)
# end class kappa_strategy_request


class kappa_strategy_sweep:
    subclass = None
    def __init__(self, strategyID='', omegaStart='', omegaEnd='', kappa='', phi='', completeness='', rank=''):
        self.strategyID = strategyID
        self.omegaStart = omegaStart
        self.omegaEnd = omegaEnd
        self.kappa = kappa
        self.phi = phi
        self.completeness = completeness
        self.rank = rank
    def factory(*args_, **kwargs_):
        if kappa_strategy_sweep.subclass:
            return kappa_strategy_sweep.subclass(*args_, **kwargs_)
        else:
            return kappa_strategy_sweep(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStrategyID(self): return self.strategyID
    def setStrategyID(self, strategyID): self.strategyID = strategyID
    def getOmegaStart(self): return self.omegaStart
    def setOmegaStart(self, omegaStart): self.omegaStart = omegaStart
    def getOmegaEnd(self): return self.omegaEnd
    def setOmegaEnd(self, omegaEnd): self.omegaEnd = omegaEnd
    def getKappa(self): return self.kappa
    def setKappa(self, kappa): self.kappa = kappa
    def getPhi(self): return self.phi
    def setPhi(self, phi): self.phi = phi
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getRank(self): return self.rank
    def setRank(self, rank): self.rank = rank
    def export(self, outfile, level, name_='kappa_strategy_sweep'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_strategy_sweep'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_strategy_sweep'):
        showIndent(outfile, level)
        outfile.write('<strategyID>%s</strategyID>\n' % quote_xml(self.getStrategyID()))
        showIndent(outfile, level)
        outfile.write('<omegaStart>%s</omegaStart>\n' % quote_xml(self.getOmegaStart()))
        showIndent(outfile, level)
        outfile.write('<omegaEnd>%s</omegaEnd>\n' % quote_xml(self.getOmegaEnd()))
        showIndent(outfile, level)
        outfile.write('<kappa>%s</kappa>\n' % quote_xml(self.getKappa()))
        showIndent(outfile, level)
        outfile.write('<phi>%s</phi>\n' % quote_xml(self.getPhi()))
        showIndent(outfile, level)
        outfile.write('<completeness>%s</completeness>\n' % quote_xml(self.getCompleteness()))
        showIndent(outfile, level)
        outfile.write('<rank>%s</rank>\n' % quote_xml(self.getRank()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_strategy_sweep' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_sweep.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_sweep.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_strategy_sweep" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_strategy_sweep'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('strategyID=%s,\n' % quote_python(self.getStrategyID()))
        showIndent(outfile, level)
        outfile.write('omegaStart=%s,\n' % quote_python(self.getOmegaStart()))
        showIndent(outfile, level)
        outfile.write('omegaEnd=%s,\n' % quote_python(self.getOmegaEnd()))
        showIndent(outfile, level)
        outfile.write('kappa=%s,\n' % quote_python(self.getKappa()))
        showIndent(outfile, level)
        outfile.write('phi=%s,\n' % quote_python(self.getPhi()))
        showIndent(outfile, level)
        outfile.write('completeness=%s,\n' % quote_python(self.getCompleteness()))
        showIndent(outfile, level)
        outfile.write('rank=%s,\n' % quote_python(self.getRank()))
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
            nodeName_ == 'strategyID':
            strategyID_ = ''
            for text__content_ in child_.childNodes:
                strategyID_ += text__content_.nodeValue
            self.strategyID = strategyID_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omegaStart':
            omegaStart_ = ''
            for text__content_ in child_.childNodes:
                omegaStart_ += text__content_.nodeValue
            self.omegaStart = omegaStart_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omegaEnd':
            omegaEnd_ = ''
            for text__content_ in child_.childNodes:
                omegaEnd_ += text__content_.nodeValue
            self.omegaEnd = omegaEnd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            kappa_ = ''
            for text__content_ in child_.childNodes:
                kappa_ += text__content_.nodeValue
            self.kappa = kappa_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            phi_ = ''
            for text__content_ in child_.childNodes:
                phi_ += text__content_.nodeValue
            self.phi = phi_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            completeness_ = ''
            for text__content_ in child_.childNodes:
                completeness_ += text__content_.nodeValue
            self.completeness = completeness_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rank':
            rank_ = ''
            for text__content_ in child_.childNodes:
                rank_ += text__content_.nodeValue
            self.rank = rank_
# end class kappa_strategy_sweep


class kappa_strategy_response:
    subclass = None
    def __init__(self, status=None, comment='', generated_sweep=None, standard_response=None):
        self.status = status
        self.comment = comment
        if generated_sweep is None:
            self.generated_sweep = []
        else:
            self.generated_sweep = generated_sweep
        self.standard_response = standard_response
    def factory(*args_, **kwargs_):
        if kappa_strategy_response.subclass:
            return kappa_strategy_response.subclass(*args_, **kwargs_)
        else:
            return kappa_strategy_response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatus(self): return self.status
    def setStatus(self, status): self.status = status
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def getGenerated_sweep(self): return self.generated_sweep
    def setGenerated_sweep(self, generated_sweep): self.generated_sweep = generated_sweep
    def addGenerated_sweep(self, value): self.generated_sweep.append(value)
    def insertGenerated_sweep(self, index, value): self.generated_sweep[index] = value
    def getStandard_response(self): return self.standard_response
    def setStandard_response(self, standard_response): self.standard_response = standard_response
    def export(self, outfile, level, name_='kappa_strategy_response'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_strategy_response'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_strategy_response'):
        if self.status:
            self.status.export(outfile, level)
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))
        for generated_sweep_ in self.getGenerated_sweep():
            generated_sweep_.export(outfile, level, name_='generated_sweep')
        if self.getStandard_response() != None :
            if self.standard_response:
                self.standard_response.export(outfile, level, name_='standard_response')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_strategy_response' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_strategy_response.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_strategy_response" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_strategy_response'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.status:
            showIndent(outfile, level)
            outfile.write('status=status(\n')
            self.status.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
        showIndent(outfile, level)
        outfile.write('generated_sweep=[\n')
        level += 1
        for generated_sweep in self.generated_sweep:
            showIndent(outfile, level)
            outfile.write('kappa_strategy_sweep(\n')
            generated_sweep.exportLiteral(outfile, level, name_='generated_sweep')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.standard_response:
            showIndent(outfile, level)
            outfile.write('standard_response=strategy_response(\n')
            self.standard_response.exportLiteral(outfile, level, name_='standard_response')
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
            nodeName_ == 'status':
            obj_ = status.factory()
            obj_.build(child_)
            self.setStatus(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'generated_sweep':
            obj_ = kappa_strategy_sweep.factory()
            obj_.build(child_)
            self.generated_sweep.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'standard_response':
            obj_ = strategy_response.factory()
            obj_.build(child_)
            self.setStandard_response(obj_)
# end class kappa_strategy_response


class kappa_motor_setting:
    subclass = None
    def __init__(self, motorName='', motorValue='', comment=''):
        self.motorName = motorName
        self.motorValue = motorValue
        self.comment = comment
    def factory(*args_, **kwargs_):
        if kappa_motor_setting.subclass:
            return kappa_motor_setting.subclass(*args_, **kwargs_)
        else:
            return kappa_motor_setting(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMotorName(self): return self.motorName
    def setMotorName(self, motorName): self.motorName = motorName
    def getMotorValue(self): return self.motorValue
    def setMotorValue(self, motorValue): self.motorValue = motorValue
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def export(self, outfile, level, name_='kappa_motor_setting'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_motor_setting'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_motor_setting'):
        showIndent(outfile, level)
        outfile.write('<motorName>%s</motorName>\n' % quote_xml(self.getMotorName()))
        showIndent(outfile, level)
        outfile.write('<motorValue>%s</motorValue>\n' % quote_xml(self.getMotorValue()))
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_motor_setting' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_motor_setting.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_motor_setting.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_motor_setting" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_motor_setting'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('motorName=%s,\n' % quote_python(self.getMotorName()))
        showIndent(outfile, level)
        outfile.write('motorValue=%s,\n' % quote_python(self.getMotorValue()))
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
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
            nodeName_ == 'motorName':
            motorName_ = ''
            for text__content_ in child_.childNodes:
                motorName_ += text__content_.nodeValue
            self.motorName = motorName_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'motorValue':
            motorValue_ = ''
            for text__content_ in child_.childNodes:
                motorValue_ += text__content_.nodeValue
            self.motorValue = motorValue_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
# end class kappa_motor_setting


class kappa_collect_settings:
    subclass = None
    def __init__(self, motorSettings=None, comment=''):
        if motorSettings is None:
            self.motorSettings = []
        else:
            self.motorSettings = motorSettings
        self.comment = comment
    def factory(*args_, **kwargs_):
        if kappa_collect_settings.subclass:
            return kappa_collect_settings.subclass(*args_, **kwargs_)
        else:
            return kappa_collect_settings(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMotorSettings(self): return self.motorSettings
    def setMotorSettings(self, motorSettings): self.motorSettings = motorSettings
    def addMotorSettings(self, value): self.motorSettings.append(value)
    def insertMotorSettings(self, index, value): self.motorSettings[index] = value
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def export(self, outfile, level, name_='kappa_collect_settings'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='kappa_collect_settings'):
        pass
    def exportChildren(self, outfile, level, name_='kappa_collect_settings'):
        for motorSettings_ in self.getMotorSettings():
            motorSettings_.export(outfile, level, name_='motorSettings')
        if self.getComment() != None :
            showIndent(outfile, level)
            outfile.write('<comment>%s</comment>\n' % quote_xml(self.getComment()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='kappa_collect_settings' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = kappa_collect_settings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = kappa_collect_settings.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="kappa_collect_settings" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='kappa_collect_settings'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('motorSettings=[\n')
        level += 1
        for motorSettings in self.motorSettings:
            showIndent(outfile, level)
            outfile.write('kappa_motor_setting(\n')
            motorSettings.exportLiteral(outfile, level, name_='motorSettings')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('comment=%s,\n' % quote_python(self.getComment()))
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
            nodeName_ == 'motorSettings':
            obj_ = kappa_motor_setting.factory()
            obj_.build(child_)
            self.motorSettings.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            comment_ = ''
            for text__content_ in child_.childNodes:
                comment_ += text__content_.nodeValue
            self.comment = comment_
# end class kappa_collect_settings


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxMosflm_commandsHandler(handler.ContentHandler):
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
        if name == 'mosflm_commands':
            obj = mosflm_commands.factory()
            stackObj = SaxStackElement('mosflm_commands', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'command':
            stackObj = SaxStackElement('command', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosflm_commands':
            obj = mosflm_commands.factory()
            stackObj = SaxStackElement('mosflm_commands', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'scala_commands':
            obj = scala_commands.factory()
            stackObj = SaxStackElement('scala_commands', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'xds_commands':
            obj = xds_commands.factory()
            stackObj = SaxStackElement('xds_commands', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'code':
            stackObj = SaxStackElement('code', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'message':
            stackObj = SaxStackElement('message', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'directory':
            stackObj = SaxStackElement('directory', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'prefix':
            stackObj = SaxStackElement('prefix', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'suffix':
            stackObj = SaxStackElement('suffix', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'template':
            stackObj = SaxStackElement('template', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'run_number':
            stackObj = SaxStackElement('run_number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'start':
            stackObj = SaxStackElement('start', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'end':
            stackObj = SaxStackElement('end', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'range':
            stackObj = SaxStackElement('range', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'number_of_images':
            stackObj = SaxStackElement('number_of_images', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'overlap':
            stackObj = SaxStackElement('overlap', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'exposure_time':
            stackObj = SaxStackElement('exposure_time', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'start_image_number':
            stackObj = SaxStackElement('start_image_number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'number_of_passes':
            stackObj = SaxStackElement('number_of_passes', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'type':
            stackObj = SaxStackElement('typexx', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'x':
            stackObj = SaxStackElement('x', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'y':
            stackObj = SaxStackElement('y', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'a':
            stackObj = SaxStackElement('a', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'b':
            stackObj = SaxStackElement('b', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'c':
            stackObj = SaxStackElement('c', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'alpha':
            stackObj = SaxStackElement('alpha', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beta':
            stackObj = SaxStackElement('beta', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'gamma':
            stackObj = SaxStackElement('gamma', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'wavelength':
            stackObj = SaxStackElement('wavelength', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distance':
            stackObj = SaxStackElement('distance', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolution':
            obj = resolution.factory()
            stackObj = SaxStackElement('resolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e11':
            stackObj = SaxStackElement('e11', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e12':
            stackObj = SaxStackElement('e12', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e13':
            stackObj = SaxStackElement('e13', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e21':
            stackObj = SaxStackElement('e21', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e22':
            stackObj = SaxStackElement('e22', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e23':
            stackObj = SaxStackElement('e23', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e31':
            stackObj = SaxStackElement('e31', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e32':
            stackObj = SaxStackElement('e32', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'e33':
            stackObj = SaxStackElement('e33', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'content_type':
            stackObj = SaxStackElement('content_type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'level':
            stackObj = SaxStackElement('level', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hklin':
            stackObj = SaxStackElement('hklin', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hklout':
            stackObj = SaxStackElement('hklout', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'lower':
            stackObj = SaxStackElement('lower', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'upper':
            stackObj = SaxStackElement('upper', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'status':
            obj = status.factory()
            stackObj = SaxStackElement('status', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'container_reference':
            stackObj = SaxStackElement('container_reference', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'container_code':
            stackObj = SaxStackElement('container_code', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sample_location':
            stackObj = SaxStackElement('sample_location', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'blSampleId':
            stackObj = SaxStackElement('blSampleId', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maximum_exposure':
            stackObj = SaxStackElement('maximum_exposure', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimum_exposure_time':
            stackObj = SaxStackElement('minimum_exposure_time', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimum_phi_speed':
            stackObj = SaxStackElement('minimum_phi_speed', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maximum_phi_speed':
            stackObj = SaxStackElement('maximum_phi_speed', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minimum_phi_oscillation':
            stackObj = SaxStackElement('minimum_phi_oscillation', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'extra_commands':
            obj = extra_commands.factory()
            stackObj = SaxStackElement('extra_commands', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategy_settings':
            obj = strategy_settings.factory()
            stackObj = SaxStackElement('strategy_settings', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symmetry':
            stackObj = SaxStackElement('symmetry', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'overlap_limit':
            stackObj = SaxStackElement('overlap_limit', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'completeness':
            stackObj = SaxStackElement('completeness', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'multiplicity':
            stackObj = SaxStackElement('multiplicity', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'i_over_sigma':
            stackObj = SaxStackElement('i_over_sigma', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'anomalous':
            stackObj = SaxStackElement('anomalous', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamline_parameters':
            obj = beamline_parameters.factory()
            stackObj = SaxStackElement('beamline_parameters', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'user_desired_minimum_phi_oscillation':
            stackObj = SaxStackElement('user_desired_minimum_phi_oscillation', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'standard':
            stackObj = SaxStackElement('standard', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'full':
            stackObj = SaxStackElement('full', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'oscillation_sequence':
            obj = oscillation_sequence.factory()
            stackObj = SaxStackElement('oscillation_sequence', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'predicted_spots':
            obj = predicted_spots.factory()
            stackObj = SaxStackElement('predicted_spots', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'number_of_segments':
            stackObj = SaxStackElement('number_of_segments', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'segment':
            obj = segment.factory()
            stackObj = SaxStackElement('segment', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategy_summary':
            obj = strategy_summary.factory()
            stackObj = SaxStackElement('strategy_summary', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategy_interpretation':
            obj = strategy_interpretation.factory()
            stackObj = SaxStackElement('strategy_interpretation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategy_statistics':
            obj = strategy_statistics.factory()
            stackObj = SaxStackElement('strategy_statistics', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'r_merge':
            stackObj = SaxStackElement('r_merge', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'overloads':
            stackObj = SaxStackElement('overloads', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'max_overloads':
            stackObj = SaxStackElement('max_overloads', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ranking_resolution':
            stackObj = SaxStackElement('ranking_resolution', None)
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
        elif name == 'close':
            stackObj = SaxStackElement('close', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'comment':
            stackObj = SaxStackElement('comment', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'desired_orientation':
            obj = kappa_alignment.factory()
            stackObj = SaxStackElement('desired_orientation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'omega':
            stackObj = SaxStackElement('omega', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'kappa':
            stackObj = SaxStackElement('kappa', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'phi':
            stackObj = SaxStackElement('phi', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'trans':
            stackObj = SaxStackElement('trans', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rank':
            stackObj = SaxStackElement('rank', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'possible_orientation':
            obj = kappa_possible_alignment.factory()
            stackObj = SaxStackElement('possible_orientation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'desired_datum':
            obj = kappa_possible_alignment.factory()
            stackObj = SaxStackElement('desired_datum', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'standard_request':
            obj = strategy_request.factory()
            stackObj = SaxStackElement('standard_request', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategyID':
            stackObj = SaxStackElement('strategyID', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'omegaStart':
            stackObj = SaxStackElement('omegaStart', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'omegaEnd':
            stackObj = SaxStackElement('omegaEnd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'generated_sweep':
            obj = kappa_strategy_sweep.factory()
            stackObj = SaxStackElement('generated_sweep', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'standard_response':
            obj = strategy_response.factory()
            stackObj = SaxStackElement('standard_response', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'motorName':
            stackObj = SaxStackElement('motorName', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'motorValue':
            stackObj = SaxStackElement('motorValue', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'motorSettings':
            obj = kappa_motor_setting.factory()
            stackObj = SaxStackElement('motorSettings', obj)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'mosflm_commands':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'command':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.addCommand(content)
                self.stack.pop()
                done = 1
        elif name == 'mosflm_commands':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosflm_commands(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'scala_commands':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScala_commands(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'xds_commands':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXds_commands(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'code':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCode(content)
                self.stack.pop()
                done = 1
        elif name == 'message':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMessage(content)
                self.stack.pop()
                done = 1
        elif name == 'directory':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setDirectory(content)
                self.stack.pop()
                done = 1
        elif name == 'prefix':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrefix(content)
                self.stack.pop()
                done = 1
        elif name == 'suffix':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSuffix(content)
                self.stack.pop()
                done = 1
        elif name == 'template':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setTemplate(content)
                self.stack.pop()
                done = 1
        elif name == 'run_number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setRun_number(content)
                self.stack.pop()
                done = 1
        elif name == 'start':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setStart(content)
                self.stack.pop()
                done = 1
        elif name == 'end':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setEnd(content)
                self.stack.pop()
                done = 1
        elif name == 'range':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setRange(content)
                self.stack.pop()
                done = 1
        elif name == 'number_of_images':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber_of_images(content)
                self.stack.pop()
                done = 1
        elif name == 'overlap':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOverlap(content)
                self.stack.pop()
                done = 1
        elif name == 'exposure_time':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setExposure_time(content)
                self.stack.pop()
                done = 1
        elif name == 'start_image_number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setStart_image_number(content)
                self.stack.pop()
                done = 1
        elif name == 'number_of_passes':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber_of_passes(content)
                self.stack.pop()
                done = 1
        elif name == 'type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setType(content)
                self.stack.pop()
                done = 1
        elif name == 'x':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setX(content)
                self.stack.pop()
                done = 1
        elif name == 'y':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setY(content)
                self.stack.pop()
                done = 1
        elif name == 'a':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setA(content)
                self.stack.pop()
                done = 1
        elif name == 'b':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setB(content)
                self.stack.pop()
                done = 1
        elif name == 'c':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setC(content)
                self.stack.pop()
                done = 1
        elif name == 'alpha':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAlpha(content)
                self.stack.pop()
                done = 1
        elif name == 'beta':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBeta(content)
                self.stack.pop()
                done = 1
        elif name == 'gamma':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setGamma(content)
                self.stack.pop()
                done = 1
        elif name == 'wavelength':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setWavelength(content)
                self.stack.pop()
                done = 1
        elif name == 'distance':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setDistance(content)
                self.stack.pop()
                done = 1
        elif name == 'resolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'e11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE11(content)
                self.stack.pop()
                done = 1
        elif name == 'e12':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE12(content)
                self.stack.pop()
                done = 1
        elif name == 'e13':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE13(content)
                self.stack.pop()
                done = 1
        elif name == 'e21':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE21(content)
                self.stack.pop()
                done = 1
        elif name == 'e22':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE22(content)
                self.stack.pop()
                done = 1
        elif name == 'e23':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE23(content)
                self.stack.pop()
                done = 1
        elif name == 'e31':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE31(content)
                self.stack.pop()
                done = 1
        elif name == 'e32':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE32(content)
                self.stack.pop()
                done = 1
        elif name == 'e33':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setE33(content)
                self.stack.pop()
                done = 1
        elif name == 'content_type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setContent_type(content)
                self.stack.pop()
                done = 1
        elif name == 'level':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setLevel(content)
                self.stack.pop()
                done = 1
        elif name == 'hklin':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.addHklin(content)
                self.stack.pop()
                done = 1
        elif name == 'hklout':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setHklout(content)
                self.stack.pop()
                done = 1
        elif name == 'lower':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setLower(content)
                self.stack.pop()
                done = 1
        elif name == 'upper':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setUpper(content)
                self.stack.pop()
                done = 1
        elif name == 'status':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatus(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'container_reference':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setContainer_reference(content)
                self.stack.pop()
                done = 1
        elif name == 'container_code':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setContainer_code(content)
                self.stack.pop()
                done = 1
        elif name == 'sample_location':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSample_location(content)
                self.stack.pop()
                done = 1
        elif name == 'blSampleId':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBlSampleId(content)
                self.stack.pop()
                done = 1
        elif name == 'maximum_exposure':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMaximum_exposure(content)
                self.stack.pop()
                done = 1
        elif name == 'minimum_exposure_time':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMinimum_exposure_time(content)
                self.stack.pop()
                done = 1
        elif name == 'minimum_phi_speed':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMinimum_phi_speed(content)
                self.stack.pop()
                done = 1
        elif name == 'maximum_phi_speed':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMaximum_phi_speed(content)
                self.stack.pop()
                done = 1
        elif name == 'minimum_phi_oscillation':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMinimum_phi_oscillation(content)
                self.stack.pop()
                done = 1
        elif name == 'extra_commands':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExtra_commands(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategy_settings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategy_settings(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symmetry':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSymmetry(content)
                self.stack.pop()
                done = 1
        elif name == 'overlap_limit':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOverlap_limit(content)
                self.stack.pop()
                done = 1
        elif name == 'completeness':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCompleteness(content)
                self.stack.pop()
                done = 1
        elif name == 'multiplicity':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMultiplicity(content)
                self.stack.pop()
                done = 1
        elif name == 'i_over_sigma':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setI_over_sigma(content)
                self.stack.pop()
                done = 1
        elif name == 'anomalous':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAnomalous(content)
                self.stack.pop()
                done = 1
        elif name == 'beamline_parameters':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamline_parameters(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'user_desired_minimum_phi_oscillation':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setUser_desired_minimum_phi_oscillation(content)
                self.stack.pop()
                done = 1
        elif name == 'standard':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setStandard(content)
                self.stack.pop()
                done = 1
        elif name == 'full':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setFull(content)
                self.stack.pop()
                done = 1
        elif name == 'oscillation_sequence':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOscillation_sequence(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'predicted_spots':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPredicted_spots(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'number_of_segments':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber_of_segments(content)
                self.stack.pop()
                done = 1
        elif name == 'segment':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSegment(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategy_summary':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addStrategy_summary(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategy_interpretation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategy_interpretation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategy_statistics':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategy_statistics(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'r_merge':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setR_merge(content)
                self.stack.pop()
                done = 1
        elif name == 'overloads':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOverloads(content)
                self.stack.pop()
                done = 1
        elif name == 'max_overloads':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMax_overloads(content)
                self.stack.pop()
                done = 1
        elif name == 'ranking_resolution':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setRanking_resolution(content)
                self.stack.pop()
                done = 1
        elif name == 'v1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setV1(content)
                self.stack.pop()
                done = 1
        elif name == 'v2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setV2(content)
                self.stack.pop()
                done = 1
        elif name == 'close':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setClose(content)
                self.stack.pop()
                done = 1
        elif name == 'comment':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setComment(content)
                self.stack.pop()
                done = 1
        elif name == 'desired_orientation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addDesired_orientation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'omega':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOmega(content)
                self.stack.pop()
                done = 1
        elif name == 'kappa':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setKappa(content)
                self.stack.pop()
                done = 1
        elif name == 'phi':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPhi(content)
                self.stack.pop()
                done = 1
        elif name == 'trans':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setTrans(content)
                self.stack.pop()
                done = 1
        elif name == 'rank':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setRank(content)
                self.stack.pop()
                done = 1
        elif name == 'possible_orientation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addPossible_orientation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'desired_datum':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addDesired_datum(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'standard_request':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStandard_request(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategyID':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setStrategyID(content)
                self.stack.pop()
                done = 1
        elif name == 'omegaStart':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOmegaStart(content)
                self.stack.pop()
                done = 1
        elif name == 'omegaEnd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOmegaEnd(content)
                self.stack.pop()
                done = 1
        elif name == 'generated_sweep':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addGenerated_sweep(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'standard_response':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStandard_response(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'motorName':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMotorName(content)
                self.stack.pop()
                done = 1
        elif name == 'motorValue':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMotorValue(content)
                self.stack.pop()
                done = 1
        elif name == 'motorSettings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addMotorSettings(self.stack[-1].obj)
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
    documentHandler = SaxMosflm_commandsHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxMosflm_commandsHandler()
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
    rootObj = mosflm_commands.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="mosflm_commands")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = mosflm_commands.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="mosflm_commands")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = mosflm_commands.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from XSDataSTACv01 import *\n\n')
    sys.stdout.write('rootObj = mosflm_commands(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="mosflm_commands")
    sys.stdout.write(')\n')
    return rootObj

class XSDataSTACv01:
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

