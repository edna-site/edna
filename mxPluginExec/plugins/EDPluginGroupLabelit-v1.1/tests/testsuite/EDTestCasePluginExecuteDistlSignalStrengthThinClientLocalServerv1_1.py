#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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


import os, time, shlex

from EDTestCasePluginExecute import EDTestCasePluginExecute
from EDConfiguration import EDConfiguration
from EDUtilsPlatform import EDUtilsPlatform

from EDPluginDistlSignalStrengthThinClientv1_1 import EDPluginDistlSignalStrengthThinClientv1_1
from EDTestCasePluginExecuteDistlSignalStrengthThinClientv1_1 import EDTestCasePluginExecuteDistlSignalStrengthThinClientv1_1


class EDTestCasePluginExecuteDistlSignalStrengthThinClientLocalServerv1_1(EDTestCasePluginExecuteDistlSignalStrengthThinClientv1_1):

    def preProcess(self):
        EDTestCasePluginExecuteDistlSignalStrengthThinClientv1_1.preProcess(self)
        # Load the configuration file
        xsPluginItem = self.getPluginConfiguration()
        if xsPluginItem is not None:
            strServerPort = EDConfiguration.getStringParamValue(xsPluginItem, \
                EDPluginDistlSignalStrengthThinClientv1_1.CONF_DISTL_SIGNAL_STRENGTH_SERVER_PORT)
            if strServerPort is None:
                iServerPort = EDPluginDistlSignalStrengthThinClientv1_1.DEFAULT_SERVER_PORT
            else:
                iServerPort = int(strServerPort)
            strPathToServer = EDConfiguration.getStringParamValue(xsPluginItem, \
                EDPluginDistlSignalStrengthThinClientv1_1.CONF_PATH_TO_DISTL_SIGNAL_STRENGTH_SERVER)
            if(strPathToServer == None):
                strErrorMessage = "EDPluginLabelitv1_1.configure : Configuration parameter missing: " + \
                                    "distl.mp_spotfinder_server_read_file"
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            # Start the server using random port
            self.subprocess = EDUtilsPlatform.Popen(shlex.split(str(EDUtilsPlatform.escape(strPathToServer + " distl.port=%d" % iServerPort))),
                                                       cwd=os.getcwd())
            self.iPID = self.subprocess.pid
            # Give the server some time to start up
            time.sleep(8)
        
        


    def testExecute(self):
        self.run()
        # Kill the server
        EDUtilsPlatform.kill(self.iPID)




if __name__ == '__main__':

    edTestCasePluginExecuteDistlSignalStrengthThinClientLocalServerv1_1 = EDTestCasePluginExecuteDistlSignalStrengthThinClientLocalServerv1_1("EDTestCasePluginExecuteDistlSignalStrengthThinClientLocalServerv1_1")
    edTestCasePluginExecuteDistlSignalStrengthThinClientLocalServerv1_1.execute()
