#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF Grenoble
#
#    Principal author:       Jerome Kieffer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF Grenoble"

import os, time

from EDVerbose                      import EDVerbose
from EDTestCasePluginUnit           import EDTestCasePluginUnit
from EDFactoryPluginStatic          import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDPluginHDF5")
#from EDPluginHDF5                   import EDPluginHDF5
from EDAssert                       import EDAssert

class EDTestCasePluginUnitHDF5(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin HDF5StackImagesv10
    we test mainly the static methods f the class
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginHDF5")

    def preProcess(self,):
        self.edluginHDF5 = EDFactoryPluginStatic.loadPlugin("EDPluginHDF5")


    def testGetIsoTime(self):
        isotime = self.edluginHDF5.getIsoTime()
        EDVerbose.screen("testGetIsoTime: %s" % (isotime))
        #EDAssert.equal(len(isotime.split(("T", "+"))), 3, "Check of Iso Time")

    def testCreateStructure(self):
        if "LOGNAME" in os.environ:
            name = os.environ["LOGNAME"]
        else:
            name = str(os.getpid())

        testfile = "/tmp/edna-%s/test-empty.h5" % name
        struct = "/toto/titi/tata"
        h5grp = self.edluginHDF5.createStructure(testfile, struct, {struct:{"foo":"bar"}, "/toto/titi":{"spam":"eggs"}, "/toto":{"tintin":"milou"}})
        EDAssert.equal(h5grp.name, struct, "Check the internal HDF5 path")
        EDAssert.equal(h5grp.file.filename, testfile, "Check the name of the HDF5 File")
        self.edluginHDF5.flushFile(testfile)
        h5grp = self.edluginHDF5.getHDF5File(testfile)[struct]
        ds = h5grp.require_dataset("fake", (10, 10), "i")
        ds[2] = range(10)
        self.edluginHDF5.flushAll()
        EDAssert.equal(self.edluginHDF5.getDataChunk(testfile, struct + "/fake", "[2,6]"), 6, "Check the shape of the dataset written on the disk")
        hdf = self.edluginHDF5.getHDF5File(testfile)
        if "foo" in hdf[struct].attrs:
            EDAssert.equal(hdf[struct].attrs["foo"], "bar", "attributes are OK")
        else:
            raise RuntimeError("HDF5 attributes are not set correctly")
        self.edluginHDF5.close(testfile)
        self.edluginHDF5.closeAll()
        EDAssert.isFile(testfile, "Check the existance of the destination HDF5 file")

    def process(self):
        self.addTestMethod(self.testCreateStructure)
        self.addTestMethod(self.testGetIsoTime)

if __name__ == '__main__':

    edTestCasePluginUnitHDF5StackImagesv10 = EDTestCasePluginUnitHDF5StackImagesv10("EDTestCasePluginUnitHDF5StackImagesv10")
    edTestCasePluginUnitHDF5StackImagesv10.execute()
