from GPLinearAlgebra import GPIntVector   as IV
from GPLinearAlgebra import GPFloatVector as FV
from GPLinearAlgebra import GPUnitVector  as UV
from GPLinearAlgebra import GPIntMatrix   as IM
from GPLinearAlgebra import GPFloatMatrix as FM
from GPLinearAlgebra import GPRotation    as R

# A couple of simple instantiations (integer vector and integer matrix)
iv = IV((2,4,6))
im = IM(((1,2,3),(4,5,6),(7,8,10)))

print "Integer vector iv: ", iv
print "Integer matrix im: ", im
print "im * iv: ", im * iv
print "iv * im: ", iv * im
print "im.determinant(), im.inverse(): ", im.determinant(), im.inverse()
print "im ** 2", im ** 2
print

m1 = FM( ( (7,0,0), (2,4,0), (3,5,6) ) )
m2 = m1 * m1.transpose()

print "Matrix m1: ", m1
print "Matrix m2 (m1 * m1.transpose()): ", m2
print "m2.cholesky(): ", m2.cholesky( tolerance=1e-8 )
print "m2.trace(): ", m2.trace()
print "m2.determinant(): ", m2.determinant()
print "m2.inverse(): ", m2.inverse( tolerance=1e-8 )
print "m2.cofactor(): ", m2.cofactor()
print "m2.adjugate(): ", m2.adjugate()

print
print "im * m2: ", im * m2
print
# Various ways of instantiating a rotation
# Matrix (row-wise)
r1 = R( ( (0.88860013132023608, -0.2849955979858817, 0.35939854722345349), 
         (0.33641092199191092, 0.93756710656407338, -0.088292764446605942), 
         (-0.31179720682233775, 0.19936255871587605, 0.92899788589643584) ),
    )

print "Rotation instantiated as row-wise tuple of tuples (r1): "
print r1

# List of float vectors (column-wise). These values are truncated
# slightly with respect to those of r1
# Could also instantiate these as UnitVectors instead of FloatVectors
v1 = FV( (0.8886001313202, 0.336410921992, -0.311797206822) )
v2 = FV( (-0.28499559799, 0.937567106564, 0.199362558716) )
v3 = FV( (0.359398547224, -0.0882927644466,0.928997885896 ) )
r2 = R( (v1, v2, v3), "col")

print "Rotation instantiated as column-wise tuple of float vectors (r2): " 
print r2

# Axis + unit vector form
r3 = R(0.5, UV((0.3,0.7,0.648074069841)) )
print "Rotation instantiated as axis + angle (r3): ", r3


# Comparison of r1 and r2
print "Equality tests of r1 and r2"
if r1 == r2:
    print "r1 == r2 at default tolerance"
else:
    print "r1 != r2 at default tolerance"

# First form: using '==' operator and setting internal tolerance for class
print
print "Checks using '==' operator"
for e in range(-8, -15, -1):
    R.set_tolerance( 10.0 ** e )
    if r1 == r2:
        print "r1 == r2 at tolerance %e" % 10.0 ** e
    else:
        print "r1 != r2 at tolerance %e" % 10.0 ** e

# Restore default tolerance
R.set_tolerance()
   
# Second form: using method underlying '==' operator and using a one-time
# tolerance for that comparison only
print
print "Checks using __eq__ method"
for e in range(-8, -15, -1):
    if r1.__eq__(r2, 10.0 ** e):
        print "r1 == r2 at tolerance %e" % 10.0 ** e
    else:
        print "r1 != r2 at tolerance %e" % 10.0 ** e

print
print "External views of the Rotation class: matrix"
print "r2 as a matrix: ", r2.matrix()
print "First column of r2 and return type: ", r2.getColumn(0), type(r2.getColumn(0))
print "Second row of r2 and return type: ", r2.getRow(1), type(r2.getRow(1))


print
print "External views of the Rotation class: angle + axis"

print "Rotation r2 (angle[radians] + unit vector)", r2.angleAxis()
(angle, axis) = r2.angleAxis()
print "Types of angleAxis: ", type(angle), type(axis)
print

v1 = UV((0.4, -0.9, 0.173205080757))
v2 = FV((1.0, 2.0, 3.0))

#for (v, typename) in ( (v1, "unit"), (v2, "float"), (iv, "integer") ):
for x in ( v1, v2, iv, im, m2 ):
    print "Operating on a %s x: " % type(x),                            x
    print "Apply rotation to x as r3 * x: ",                            r3 * x
    print "Type of ( r3 * x ): ",                                       type(r3 * x)
    print "Apply inverse rotation as x * r3: ",                         x * r3
    print "Apply inverse rotation as r3 ** -1 * x: ",                   r3 ** -1 * x
    print "Apply inverse rotation as r3.conjugate() * x: ",             r3.conjugate() * x
    print "Check that inverse rotation is correct r3 * r3 ** -1 * x: ", r3 * r3 ** -1 * x
    print


# Should fail: determinant is +1, but fails condition that m * m.transpose() == identity matrix
# Example is from Wikipedia article "Rotation_matrix"
try:
    r2 = R(((3, -4, 1), (5,3,-7), (-9,2,6)))
    raise AssertionError, "No exception raised: expected ValueError"
except ValueError:
    print "ValueError caught successfully"
    

