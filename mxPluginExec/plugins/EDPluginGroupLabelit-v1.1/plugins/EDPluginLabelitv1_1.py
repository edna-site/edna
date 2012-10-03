#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
#
#    Contributing author:    Karl Levik (karl.levik@diamond.ac.uk)
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"


from EDConfiguration           import EDConfiguration
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataCommon import XSPluginItem
from XSDataCommon import XSDataImage

class EDPluginLabelitv1_1(EDPluginExecProcessScript):
    """
    This is an abstract class to be subclassed by all Labelit plugins.
    It takes care of common configuration parameters.
    """

    CONF_PATH_TO_LABELIT_SETPATH_SCRIPT = "pathToLabelitSetpathScript"

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.__strPathToLabelitSetpathScript = None
        self.setXSDataInputClass(XSDataImage, "referenceImage")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginLabelitv1_1.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            self.warning("EDPluginLabelitv1_1.configure: No Labelit plugin item defined.")
            xsPluginItem = XSPluginItem()
        strPathToLabelitSetpathScript = EDConfiguration.getStringParamValue(xsPluginItem, \
                                                                            EDPluginLabelitv1_1.CONF_PATH_TO_LABELIT_SETPATH_SCRIPT)
        if(strPathToLabelitSetpathScript == None):
            strErrorMessage = "EDPluginLabelitv1_1.configure : Configuration parameter missing: " + \
                                EDPluginLabelitv1_1.CONF_PATH_TO_LABELIT_SETPATH_SCRIPT
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            self.setPathToLabelitSetpathScript(strPathToLabelitSetpathScript)


    def setPathToLabelitSetpathScript(self, _strPathToLabelitSetpathScript):
        self.__strPathToLabelitSetpathScript = _strPathToLabelitSetpathScript


    def getPathToLabelitSetpathScript(self):
        return self.__strPathToLabelitSetpathScript


    def initaliseLabelitCommandLine(self):
        """
        Initialises the Labelit command line
        """
        self.DEBUG("EDPluginLabelitv1_1.initaliseLabelitCommandLine")
        strCommandLabelit = "--index_only"
        xsDataImageList = self.getDataInput("referenceImage")
        for xsDataImage in xsDataImageList:
            strCommandLabelit = strCommandLabelit + " " + xsDataImage.getPath().getValue()
        self.setScriptCommandline(strCommandLabelit)
