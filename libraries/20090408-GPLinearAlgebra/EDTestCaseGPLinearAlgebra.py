#
#    Copyright 2009 Peter Keller and Wlodek Paciorek, Global Phasing, UK
#
#    Contributing author: Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#

from EDVerbose       import EDVerbose
from EDTestCase      import EDTestCase
from EDUtilsSymmetry import EDUtilsSymmetry
from EDAssert        import EDAssert

from GPLinearAlgebra import GPIntVector   as IV
from GPLinearAlgebra import GPFloatVector as FV
from GPLinearAlgebra import GPUnitVector  as UV
from GPLinearAlgebra import GPIntMatrix   as IM
from GPLinearAlgebra import GPFloatMatrix as FM
from GPLinearAlgebra import GPRotation    as R


class EDTestCaseGPLinearAlgebra(EDTestCase):


    def testVectorMatrixMultiplication(self):
        iv = IV((2, 4, 6))
        im = IM(((1, 2, 3), (4, 5, 6), (7, 8, 10)))
        productIvIm = iv * im
        productIvImReference = [60, 72, 90]
        EDAssert.equal(productIvImReference, productIvIm)
        productImIv = im * iv
        productImIvReference = [28, 64, 106]
        EDAssert.equal(productImIvReference, productImIv)


    def testMatrixDeterminant(self):
        im = IM(((1, 2, 3), (4, 5, 6), (7, 8, 10)))
        determinantIm = im.determinant()
        determinantImReference = -3
        EDAssert.equal(determinantImReference, determinantIm)


    def testMatrixInverse(self):
        im = IM(((1, 2, 3), (4, 5, 6), (7, 8, 10)))
        inverseIm = im.inverse()
        inverseImReference = [[-0.66666666666666663, -1.3333333333333333, 1.0], [-0.66666666666666663, 3.6666666666666665, -2.0], [1.0, -2.0, 1.0]]
        EDAssert.equal(inverseImReference, inverseIm)


    def testMatrixSquare(self):
        im = IM(((1, 2, 3), (4, 5, 6), (7, 8, 10)))
        squareIm = im ** 2
        squareImReference = [[30, 36, 45], [66, 81, 102], [109, 134, 169]]
        EDAssert.equal(squareImReference, squareIm)


    def process(self):
        self.addTestMethod(self.testVectorMatrixMultiplication)
        self.addTestMethod(self.testMatrixDeterminant)
        self.addTestMethod(self.testMatrixInverse)
        self.addTestMethod(self.testMatrixSquare)



if __name__ == '__main__':
    EDTestCaseGPLinearAlgebra = EDTestCaseGPLinearAlgebra("EDTestCaseGPLinearAlgebra")
    EDTestCaseGPLinearAlgebra.execute()
