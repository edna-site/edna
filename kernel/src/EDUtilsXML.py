#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 Diamond Light Source
#                            Chilton, Didcot, UK
#
#    Principal author:       Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Karl Levik", "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "karl.levik@diamond.ac.uk"
__license__ = "LGPLv3+"
__copyright__ = "Diamond Light Source, Chilton, Didcot, UK"

import StringIO, re, xml.dom.minidom


class EDUtilsXML:

    @staticmethod
    def dnaMarshal(_xsDataObject=None):
        """
        Returns a DNA compatible XML representation of an object derived from XSData.
        DNA compatible XML has no whitespace or newlines etc. between elements and single-quotes must be escaped.
        In addition, booleans must be either "True" or "False". Anything but "True" is interpreted as "False".
        """
        stringIO = StringIO.StringIO()
        stringIO.write('<?xml version="1.0" encoding="ISO-8859-1"?>')

        regexp = re.compile('XSDataISPyB(.*)')
        matchObject = regexp.match(_xsDataObject.__class__.__name__)
        strDNAClassName = matchObject.group(1)

        _xsDataObject.export(stringIO, 0, name_=strDNAClassName)
        strXML = stringIO.getvalue()
        stringIO.close()

        # Remove whitespace and <value> & </value> taqs, escape single-quotes etc
        strParsed = xml.dom.minidom.parseString(strXML)
        regexpXMLHeader = re.compile('\<\?xml version="1.0" \?\>(.*)')

        regexpValueTags = re.compile('\<value\>(.*)\</value\>')
        regexpOtherTag = re.compile('\<(.*)\>')
        strXML = ''
        bIsBoolean = False

        for strLine in strParsed.toxml().splitlines():
            if strLine.startswith('<?xml version="1.0" ?>'):
                strXML += '<?xml version="1.0" ?>'
                strLine = strLine[22:].strip()
                if len(strLine) == 0:
                    continue
            if strLine.startswith('</%s>' % strDNAClassName):
                strXML += '</%s>' % strDNAClassName
                break
            if strLine.startswith('<%s>' % strDNAClassName):
                strXML += '<%s>' % strDNAClassName
                strLine = strLine[len(strDNAClassName) + 2:]
                if len(strLine) == 0:
                    continue

            m = regexpValueTags.match(strLine.strip())
            if m != None:
                strValue = m.group(1)
                strValue = strValue.replace('\'', '\\\'')
                if bIsBoolean:
                    strValue = strValue.replace('1', 'True')
                strXML += strValue
            else:
                strXML += strLine.strip()
                m2 = regexpOtherTag.match(strLine.strip())
                if m2 != None:
                    strValue = m2.group(1)
                    if not strValue.startswith("/"):
                        method = getattr(_xsDataObject, 'get%s' % EDUtilsXML.capitalizeFirstLetter(strValue))
                        o = method()
                        if o.__class__.__name__ == 'XSDataBoolean':
                            bIsBoolean = True
                        else:
                            bIsBoolean = False
        return strXML


    @staticmethod
    def capitalizeFirstLetter(_str):
        """
        Capitalizes the first letter of a string, leaving the rest untouched
        """
        return (_str[0].capitalize() + _str[1:])
