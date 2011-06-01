#
#    Copyright 2009 Peter Keller and Wlodek Paciorek, Global Phasing, UK
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

import math

class GPLABase(list):
    """Common supertype for vector and matrix types, holding
    methods that are the same for both"""
    
    # Default tolerance for comparison of floating point values
    __default_epsilon = 1e-10
    epsilon = __default_epsilon

    @classmethod
    def set_tolerance(this, epsilon=None):
        """Set tolerance for various built-in checks involving subtypes (e.g. magnitude of
        GPUnitVector or GPRotation == 1.0, GPFloatMatrix is symmetric and positive definite,
        comparison for equality/non-equality of float types, etc.
        
        This method can be called on any subtype of GPLABase, e.g.:
        
           GPFloatVector.set_tolerance(1e-8)
           
        which will make the tolerance apply to instances of that subtype and its subtypes
        only.
        
        Calling with None (or no arguments) will restore the default tolerance
        """
        if epsilon is None:
            if this == GPLABase:
                # Revert to default epsilon if we are at the top of the inheritance hierarchy
                this.epsilon = this.__default_epsilon
            elif "epsilon" in vars(this).keys():
                del(this.epsilon)
        else:
            this.epsilon = float(epsilon)
   
    def __init__(self, l):
        super(GPLABase, self).__init__(l)

    # N.B. type checking and assignment of return_type must be done in subclasses

    def __add__(self, other, return_type):
        return return_type( [ e1 + e2 for (e1, e2) in zip(self, other) ] )

    def __sub__(self, other, return_type):
        return return_type( [ e1 - e2 for (e1, e2) in zip(self, other) ] )

    def __div__(self, other, return_type):
        return return_type( [ e / other for e in self ] )

    # The reason for using 'self[:] = result[:]' in these in-place operations
    # rather than 'self = result' is so that we don't blindly copy anything
    # other than the list contents if we are dealing with a subclass that
    # has other attributes
    # In the case of a matrix type, we _will_ carry across any other attributes from the
    # matrix components, if they exist.
    # Subclasses that define additional instance attributes that should not be
    # lost during in-place operations will need to override
    # these methods (possibly calling super(<class>,self).__iadd__(other) etc.),
    # and handle those attributes correctly.
    
    def __iadd__(self, other):
        result = self + other
        self[:] = result[:]
        return self

    def __isub__(self, other):
        result = self - other
        self[:] = result[:]
        return self

    def __imul__(self, other):
        result = self * other
        self[:] = result[:]
        return self

    def __idiv__(self, other):
        result = self / other
        self[:] = result[:]
        return self

    def __pow__(self, other, modulo=None):
        
        if modulo is not None:
            raise TypeError, "Power operator on %s type does not support modulo argument" % type(self)
        elif not isinstance(other, int):
            raise TypeError, "Power operator on %s type only supported for integer powers" %type(self)
        elif other < 1:
            raise TypeError, "GPlinearAlgebra.GPLABase.__pow__ should not be called with power < 1"
        else:
            # Copy-assign self as starting point for return value
            retval = type(self)(self)
            for i in range(other - 1):
                retval *= self
                
        return retval

    def __delitem__(self):
        raise TypeError, "Number of elements in vector/matrix types is fixed: cannot insert or delete elements"


class GPNormalisable(object):
    """Class containing methods that are common to GPUnitVector and GPRotation, and relate to
    their magnitude/norm property"""
    # Need __setitem__
    # _normalise will probably be specific to implementing classes, but we give a
    # default method here
    
    def __abs__(self):
        """Override built-in abs(...) function to return magnitude of vector/quaternion"""
        return math.sqrt( sum( [ v*v for v in self ] ) )
        
    def _abs_check(self, tolerance):
        "Check that we satisfy the unit length condition for a unit vector/rotation quaternion"
        
        if tolerance is None:
            # In spite of the warning that Eclipse gives here, there is nothing wrong
            # with the next line. self.__class__ will never be GPNormalisable
            tolerance = self.__class__.epsilon
        return abs( abs(self) - 1 ) < tolerance

    def _normalise(self):
        """Default normalisation method: may be overridden by more specialised methods"""
        magnitude = abs(self)
        newvals = [ v/magnitude for v in self ]
        self[:] = newvals


class GPVector(GPLABase, GPNormalisable):

    def __init__(self, v, vtype):

        # Should not invoke this method directly - only via subclasses
        # This class should be considered abstract
        assert type(self) != GPVector

        if ( isinstance(v, list) or isinstance(v, tuple) ) and len(v) == 3:
            super(GPVector, self).__init__( [ vtype(e) for e in v ] )
        elif isinstance(v, int) or isinstance(v, float):
            super(GPVector, self).__init__( [ vtype(v) ] * 3)
        else:
            raise TypeError, "Vector constructor requires one numeric argument, or a list argument of length 3"

    def __mul__(self, other, return_type):

        if isinstance(other, GPVector):
            return return_type( [ self[1]*other[2] - self[2]*other[1],
                                  self[2]*other[0] - self[0]*other[2],
                                  self[0]*other[1] - self[1]*other[0] ] )
        
        elif isinstance(other, GPMatrix):
            # Handle premultiplication by vector: v * m == m(T) * v, where v is a row
            # on the LHS and a column on the RHS
            return other.transpose() * self

        elif isinstance(other, GPRotation):
            # Treat v * r similarly to v * m, i.e.:
            #   v * r = r(T) * v (where r(T) is transpose of r, considering r to be a matrix,
            #                     and v is a row vector on the LHS, and a column vector on the RHS)
            # But, for rotations, r(T) == r.inverse(), which is equivalent to r.conjugate() of
            # the quaternion form, so we can simply do:
            return other.conjugate() * self
        
        else:
            return return_type( [ e * other for e in self ] )

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            # Multiplication of a vector by a number is commutative, so this is OK:
            return self * other
        else:
            # ... otherwise, multiplication is not commutative, so if we end up
            # here we have attempted an unimplemented operation.
            raise NotImplementedError, "Multiplication not yet implememented for %s * %s" % (type(other), type(self))

    def __mod__(self, other):
        """Override Python's '%' operator to do a dot/scalar product"""
        return sum( [ e1 * e2 for (e1, e2) in zip(self, other) ] )

    # Python's 'list' type defines the (now deprecated) __setslice__ method,
    # which allows an assignment to a simple slice like this to alter the length of a list:
    #
    #   l = [1,2,3]
    #   l[0:2] = [99]   # l is now [99,3]
    #
    # Vectors are fixed in length, so we don't want to inherit this implementation
    # of __setslice__ from list. Instead, we construct a an extended slice from the start and
    # end values of the simple slice and call __setitem__ instead.
    #
    # list.__setitem__ will raise ValueError if the length of sequence is different
    # from the length of the slice that is being assigned.
    #
    # See the following sections of the Python documentation:
    #
    #    3.4.5 Emulating container types
    #    3.4.6 Additional methods for emulation of sequence types

    def __setslice__(self, i, j, sequence):
        # Fixme! Need additional checks that elements of sequence are acceptable types. 
        # These checks will be different for matrices and vectors, so this method
        # does not belong in GPLABase
        self.__setitem__( slice(i,j,1), sequence )


    def unitVector(self):
        """Return a unit vector parallel to this one"""
        return GPUnitVector( self/abs(self) )



class GPIntVector(GPVector):

    def __init__(self, v):
        super(GPIntVector, self).__init__(v, int)

    def _normalise(self):
        raise TypeError, "Not allowed to normalise a GPIntVector (did you mean to call unitVector() method?)"
 
    def __add__(self, other):

        if isinstance(other, GPIntVector):
            return super(GPIntVector, self).__add__(other, type(self))

        elif isinstance(other, GPFloatVector):
            return GPFloatVector(self) + other

        else:
            raise TypeError, "Incompatible types for vector addition"

    def __sub__(self, other):
        
        if isinstance(other, GPIntVector):
            return super(GPIntVector, self).__sub__(other, type(self))

        elif isinstance(other, GPFloatVector):
            return GPFloatVector(self) - other

        else:
            raise TypeError, "Incompatible types for vector subtraction"

    def __mul__(self, other):

        if isinstance(other, int) \
                or isinstance(other, GPIntVector) \
                or isinstance(other, GPIntMatrix):
            return super(GPIntVector, self).__mul__(other, GPIntVector)

        elif isinstance(other, GPFloatVector) \
                or isinstance(other, float) \
                or isinstance(other, GPFloatMatrix) \
                or isinstance(other, GPRotation):
            return GPFloatVector(self) * other

        else:
            # Try __rmul__ on other
            return NotImplemented

    def __div__(self, other):

        if isinstance(other, int):
            return super(GPIntVector, self).__div__(other, type(self))

        elif isinstance(other, float):
            return GPFloatVector(self) / other

        else:
            raise TypeError, "Incompatible types for division of a vector"

class GPFloatVector(GPVector):

    def __init__(self, v):
        super(GPFloatVector, self).__init__(v, float)

        
    def __add__(self, other):

        if isinstance(other, GPFloatVector):
            return super(GPFloatVector, self).__add__(other, type(self))

        elif isinstance(other, GPIntVector):
            return super(GPFloatVector, self).__add__(GPFloatVector(other), GPFloatVector)

        else:
            raise TypeError, "Incompatible types for vector addition"

    def __sub__(self, other):

        if isinstance(other, GPFloatVector):
            return super(GPFloatVector, self).__sub__(other, type(self))

        elif isinstance(other, GPIntVector):
            return super(GPFloatVector, self).__sub__(GPFloatVector(other), type(self))

        else:
            raise TypeError, "Incompatible types for vector subtraction"


    def __mul__(self, other):

        if isinstance(other, float) \
                or isinstance(other, GPFloatVector) \
                or isinstance(other, GPFloatMatrix) \
                or isinstance(other, GPRotation):
            return super(GPFloatVector, self).__mul__(other, type(self))

        elif isinstance(other, int):
            return super(GPFloatVector, self).__mul__(float(other), type(self))

        elif isinstance(other, GPIntVector):
            return super(GPFloatVector, self).__mul__(GPFloatVector(other), type(self))

        else:
            # Try __rmul__
            return NotImplemented

        
    def __div__(self, other):

        if isinstance(other, float):
            return super(GPFloatVector, self).__div__(other, type(self))

        elif isinstance(other, int):
            return super(GPFloatVector, self).__div__(float(other), GPIntVector)

        else:
            raise TypeError, "Incompatible types for division of a vector"

    # Need to take account of epsilon when comparing real types for equality

    def __eq__(self, other, tolerance=None):
        if not isinstance(other, GPVector):
            return NotImplemented
        
        if tolerance is None:
            tolerance = self.__class__.epsilon
        for i in range(len(self)):
            if abs(self[i] - other[i]) > tolerance:
                return False
            
        return True
            
    def __ne__(self, other, tolerance=None):
        if not isinstance(other, GPVector):
            return NotImplemented
        
        if tolerance is None:
            tolerance = self.__class__.epsilon
        for i in range(len(self)):
            if abs(self[i] - other[i]) > tolerance:
                return True
            
        return False

class GPUnitVector(GPFloatVector):
    
    def __init__(self, v, tolerance=None):
        super(GPUnitVector, self).__init__(v)
        if tolerance is None:
            tolerance = self.__class__.epsilon
        if not self._abs_check(tolerance=tolerance):
            self = []
            raise ValueError, "Unit vector cannot be instantiated with magnitude other than 1"
        # Normalise as accurately as possible
        self._normalise()

    def _normalise (self, tolerance=None):
        """Normalise unit vector as accurately as possible, not allowing small zon-zero components"""
        # Operate on a FloatVector-typed copy of self, so that we don't
        # trigger failures part-way through the normalisation process
        # on unit vectors that are close to the tolerance threshold
        tmpVector = GPFloatVector(self)

        if tolerance is None:
             tolerance = self.__class__.epsilon

        for i in (0,1,2):
            if abs(tmpVector[i]) < tolerance:
                tmpVector[i] = 0.0
        
        # Don't do tmpVector.unitVector(): that causes infinite recursion
        tmpVector /= abs(tmpVector)
        self[:] = tmpVector[:]


    def __setitem__(self, key, value, tolerance=None):
        # Check that magnitude isn't changed if someone assigns individual elements
        # Easier to just get the new value and check it than try to work out ahead
        # of time what the result would be

        # Save current elements, so that they can be restored before raising exception
        oldvals = tuple(self)

        # Make sure all elements are floats, or very strange things may happen
        # later on, after a successful call to this method!
        if isinstance(value, list) or isinstance(value, tuple):
            super(GPUnitVector, self).__setitem__( key, [ float(v) for v in value ] )
        else:
            super(GPUnitVector, self).__setitem__( key, float(value) )
            
        if not self._abs_check(tolerance):
            self[:] = oldvals
            raise ValueError, "Attempt to change values of a %s such that magnitude is not 1" % self.__class__.__name__
        

    # All these methods will not return a unit vector in most cases.
    # Operate instead on float vector type instead
    def __add__(self, other):
        return GPFloatVector(self) + other
    
    def __sub__(self, other):
        return GPFloatVector(self) - other
    
    def __mul__(self, other):
        # Exception to the above rule: UnitVector * Rotation -> UnitVector
        if isinstance(other, GPRotation):
            return super(GPUnitVector, self).__mul__(other)
        
        return GPFloatVector(self) * other
 
    def __div__(self, other):
        return GPFloatVector(self) / other

class GPMatrix(GPLABase):

    # mtype should be one of GPIntVector, GPFloatVector, GPUnitVector
    def __init__(self, m, mtype, sense="row"):

        assert type(self) != GPMatrix

        if ( isinstance(m, list) or isinstance(m, tuple) ) and len(m) == 3:

            if sense[0].lower() == "r":
                super(GPMatrix, self).__init__( [ mtype(e) for e in m ] )
            elif sense[0].lower() == "c":
                super(GPMatrix, self).__init__( [ mtype( [ e[i] for e in m ] ) for i in (0,1,2) ] )
            else:
                raise TypeError, "Matrix constructor requires sense argument to be one of (R/r)ow, (C/c)olumn"

        elif isinstance(m, int) or isinstance(m, float):
            super(GPMatrix, self).__init__( ( mtype( (m, 0, 0) ),
                                              mtype( (0, m, 0) ),
                                              mtype( (0, 0, m) ) ) )
        else:
            raise TypeError, "Matrix constructor requires one numeric argument, or a list of 3 lists"


    def __mul__(self, other, return_type):

        if isinstance(other, GPMatrix):
            ot = other.transpose()
            return return_type( [ [ self[i] % ot[j] for j in (0, 1, 2) ] for i in (0, 1, 2) ] )

        elif isinstance(other, GPVector):
            # Here, return_type should be a subclass of GPVector
            return return_type( [ self[i] % other for i in (0,1,2) ] )
        
        elif isinstance(other, GPRotation):
            return self * other.matrix()

        else:
            return return_type( [ e * other for e in self ] )

    def __pow__(self, other, modulo=None):
        
        # Special case for zero power of matrix (return identity matrix)
        if other == 0:
            return type(self)(1)
        else:
            retval = super(GPMatrix, self).__pow__( abs(other), modulo )
            if other < 0:
                return retval.inverse()
            else:
                return retval
            
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            # Multiplication by a number is commutative, so we are OK here.
            return self * other

        else:
            # If we end up here we have attempted an unimplemented operation.
            raise NotImplementedError, "Multiplication not yet implememented for %s * %s" % (type(other), type(self))

    def __setslice__(self, i, j, sequence):
        # Fixme! Need additional checks that elements of sequence are acceptable types.
        # These checks will be different for matrices and vectors, so this method
        # does not belong in GPLABase
        self.__setitem__( slice(i, j, 1), sequence )

    def trace(self):
        "Return trace (sum of diagonal elements) of matrix"
        return sum( [ self[i][i] for i in range(0, len(self)) ] )

    def transpose(self):
        "Return transpose of matrix"
        return type(self)( [ [ e[i] for e in self ] for i in (0,1,2) ] )

    def determinant(self):
        "Return determinant of matrix"
        return self[0] % ( self[1] * self[2] )

    def inverse(self, tolerance=None):
        "Return inverse of matrix"
        
        if tolerance is None:
            tolerance = self.__class__.epsilon

        det = self.determinant()
        if abs(det) < tolerance:
            raise ZeroDivisionError, "Cannot invert matrix with zero determinant"
        return self.adjugate()/float(det)
        
    def cofactor(self):
        "Calculate cofactor matrix"
        # Any row of the cofactor matrix is the cross product of the next row and the next
        # row but one of the original matrix, ordered cyclically
        return type(self)( [ self[ (i+1) % 3 ] * self[ (i+2) % 3 ] for i in (0,1,2) ] )
            
    def adjugate(self):
        "Calculate adjugate matrix (aka adjoint matrix)"
        return self.cofactor().transpose()

    def cholesky(self, tolerance=None):
        """Calculate Cholesky decomposition. Matrix must be symmetric and positive definite"""
        
        if tolerance is None:
            tolerance = self.__class__.epsilon
        
        # Diagonal elements must not be negative
        for i in (0,1,2):
            if self[i][i] < 0.0:
                raise ValueError, "Diagonal elements must be positive for Cholesky decomposition"
            
        # Check off-diagonal elements (matrix must be symmetric)
        for (i,j) in ( (0,1), (0,2), (1,2) ):
            if ( abs(self[i][j] - self[j][i] ) > tolerance ):
                raise ValueError, "Matrix must be symmetric for Cholesky decomposition"
            
        # Calculate using Maple-generated analytic expression taken from
        # http://www.mapleprimes.com/forum/maplectranslationsolvingsquarerootmatrix
        sqrta = math.sqrt(self[0][0])
        sqrteab2 = self[1][1]*self[0][0] - self[0][1]**2.0
        if sqrteab2 <= 0.0:
            raise ValueError, "Determinant of upper left hand 2x2 submatrix must be positive for Cholesky decomposition"
        sqrteab2 = math.sqrt(sqrteab2)
        
        # Calculate numerator of complicated bottom right-hand term
        element22 = self[2][2]*self[1][1]*self[0][0] - self[2][2]*self[1][0]**2.0 - \
             self[1][1]*self[0][2]**2.0 - self[0][0]*self[1][2]**2.0  + \
              2.0 * self[1][2]*self[0][1]*self[0][2]
        
        if element22 < 0.0:
            raise ValueError, "Unsatisfied condition for Cholesky decomposition"
        
        return GPFloatMatrix( ( ( sqrta, 0.0, 0.0 ),
                                ( self[0][1]/sqrta, sqrteab2/sqrta, 0.0),
                                ( self[0][2]/sqrta, 
                                  (self[2][1]*self[0][0] - self[1][0]*self[2][0])/sqrta/sqrteab2,
                                  math.sqrt(element22)/sqrteab2
                                )
                              )
                            )
        

class GPIntMatrix(GPMatrix):

    def __init__(self, m, sense="row"):
        if isinstance(m, list) or isinstance(m, tuple):
            super(GPIntMatrix, self).__init__( [ GPIntVector(e) for e in m ], GPIntVector, sense )
        else:
            super(GPIntMatrix, self).__init__( m, GPIntVector, sense )


    def __add__(self, other):

        if isinstance(other, GPIntMatrix):
            return super(GPIntMatrix, self).__add__(other, type(self))

        elif isinstance(other, GPFloatMatrix):
            return type(other)(self) + other

        else:
            raise TypeError, "Incompatible types for matrix addition"

    def __sub__(self, other):

        if isinstance(other, GPIntMatrix):
            return super(GPIntMatrix, self).__sub__(other, type(self))

        elif isinstance(other, GPFloatMatrix):
            return type(other)(self) - other

        else:
            raise TypeError, "Incompatible types for matrix subtraction"

    def __mul__(self, other):

        if isinstance(other, int) or isinstance(other, GPIntMatrix):
            return super(GPIntMatrix, self).__mul__(other, type(self))

        elif isinstance(other, GPIntVector):
            return super(GPIntMatrix, self).__mul__(other, type(other))

        elif isinstance(other, float) or isinstance(other, GPFloatVector) \
                or isinstance(other, GPFloatMatrix):
            return GPFloatMatrix(self) * other

        elif isinstance(other, GPRotation):
            return self * other.matrix()

        else:
            raise TypeError, "Incompatible types for matrix multiplication"


    def __div__(self, other):

        if isinstance (other, int):
            return super(GPIntMatrix, self).__div__(other, type(self))

        elif isinstance (other, float):
            return GPFloatMatrix(self) / other

        else:
            raise TypeError, "Incompatible types for matrix division"

class GPFloatMatrix(GPMatrix):

    def __init__(self, m, sense="row"):

        # GPRotation is a subtype of list, so we want to pick it up first
        # and convert it to a matrix so that a constructor like this works correctly:
        #
        #   r = GPRotation(....)
        #   ....
        #   GPFloatMatrix(r)
        if isinstance(m, GPRotation):
            super(GPFloatMatrix, self).__init__ (m.matrix(), GPFloatVector, sense="row")

        # Now we pick up lists/tuples and assume that we have a 3 lists of 3 numbers
        elif isinstance(m, list) or isinstance(m, tuple):
            super(GPFloatMatrix, self).__init__( [ GPFloatVector(e) for e in m ] , GPFloatVector, sense )
        else:
            super(GPFloatMatrix, self).__init__( m, GPFloatVector, sense )


    def __add__(self, other):

        if isinstance(other, GPFloatMatrix):
            return super(GPFloatMatrix, self).__add__(other, type(self))

        elif isinstance(other, GPIntMatrix):
            return super(GPFloatMatrix, self).__add__(GPFloatMatrix(other), type(self))

        else:
            raise TypeError, "Incompatible types for matrix addition"


    def __sub__(self, other):

        if isinstance(other, GPFloatMatrix):
            return super(GPFloatMatrix, self).__sub__(other, type(self))

        elif isinstance(other, GPIntMatrix):
            return super(GPFloatMatrix, self).__sub__(GPFloatMatrix(other), type(self))

        else:
            raise TypeError, "Incompatible types for matrix subtraction"

    def __mul__(self, other):

        if isinstance(other, float) or isinstance(other, GPFloatMatrix):
            return super(GPFloatMatrix, self).__mul__(other, type(self))

        elif isinstance(other, int):
            return super(GPFloatMatrix, self).__mul__(float(other), type(self))

        elif isinstance(other, GPIntMatrix):
            return super(GPFloatMatrix, self).__mul__(type(self)(other), type(self))

        # This branch takes care of the Matrix * UnitVector -> FloatVector case,
        # since UnitVector is a subtype of FloatVector
        elif isinstance(other, GPFloatVector):
            return super(GPFloatMatrix, self).__mul__(other, GPFloatVector)

        elif isinstance(other, GPIntVector):
            return super(GPFloatMatrix, self).__mul__(GPFloatVector(other), type(self[0]))

        elif isinstance(other, GPRotation):
            return self * other.matrix()

    def __div__(self, other):

        if isinstance (other, float):
            return super(GPFloatMatrix, self).__div__(other, type(self))

        elif isinstance (other, int):
            return super(GPFloatMatrix, self).__div__(float(other), type(self))

        else:
            raise TypeError, "Incompatible types for matrix division"

    # Need to propagate tolerance upwards to float vector comparison
    def __eq__(self, other, tolerance=None):
        if not isinstance(other, GPMatrix):
            return NotImplemented
        
        for i in (0, 1, 2):
            if self[i].__ne__(other[i], tolerance):
                return False
            
        return True
            
    def __ne__(self, other, tolerance=None):
        if not isinstance(other, GPMatrix):
            return NotImplemented
        
        for i in (0, 1, 2):
            if self[i].__ne__(other[i], tolerance):
                return True
            
        return False
        

class GPRotation(GPLABase, GPNormalisable):
    """Class representing a rotation (internally as a quaternion of unit length)
    
    All constructors have an optional 'tolerance' parameter that can be used to 
    control the stringency of the check on the input parameters being a true
    rotation. This parameter must be keyworded in almost all cases.
    
    Possible constructors:
    
       Angle (radians/float) + Axis (GPUnitVector):
       
          axis = GPUnitVector( (0.0, 0.70710678118655, 0.70710678118655), tolerance=1e-8 )
          GPRotation ( 90.0/math.pi/2.0, axis )
       
          (N.B. here, the tolerance applies to the axis via the constructor of
          the GPUnitVector, not the rotation)
    
       Same arguments as for a GPFloatMatrix constructor (e.g. a 3-element list of 3-element lists 
       with optional second argument specifying row or column wise):
       
          GPRotation ( [ [0.88860013132023608, -0.28499559798588164, 0.35939854722345344], 
                         [0.33641092199191086, 0.93756710656407338, -0.088292764446605942], 
                         [-0.31179720682233769, 0.19936255871587599, 0.92899788589643584] ],
                         "row", tolerance=1e-8 )
                         
         Other possibilities include any GPMatrix instance, or a list/tuple of three GPVectors.
         Also, can use GPRotation(1) to get "unit matrix", i.e. quaternion corresponding to
         a rotation of 0.
          
       List of 4 quaternion components (i, j, k, real):

          GPRotation ( (0.0, 0.0, 0.0, 1.0), tolerance=1e-8 )
    
    """
    def __init__(self, arg1, arg2="row", tolerance=None):

        if tolerance is None:
            tolerance = self.__class__.epsilon
        
        if ( isinstance(arg1, list) or isinstance(arg1, tuple) )and len(arg1) == 4:
            # Native quaternion representation. Note that we put real element at the
            # end of the list, i.e. [x,y,z,w], or [ q(u), q(v), q(w), q(0) ] depending
            # on which notation you are using. The quaternion is thus:
            #
            #   self[3] + i *self[0] + j * self[1] + k * self[2]
            #
            # The reason for doing it this way is that it makes it simpler and less error-prone
            # to deal with quaternion/matrix and quaternion/vector combinations, if we don't
            # have to be constantly adjusting subscripts by +1/-1
            super(GPRotation, self).__init__(arg1)
            if not self._abs_check(tolerance=tolerance):
                self[:] = []
                raise ValueError, "Magnitude of rotation quaternion must be 1.0"
            
        elif ( isinstance(arg1, float) or isinstance(arg1, int) ) and isinstance(arg2, GPUnitVector):
            # Angle/axis representation
            s = math.sin(arg1/2.0)
            super(GPRotation, self).__init__( [ x * s for x in arg2 ] + [ math.cos(arg1/2.0) ] )
            
        elif isinstance(arg2, str):
            # Matrix representation. Construct matrix object first, and check that
            # it is OK
            if isinstance(arg1, GPMatrix):
                m = arg1
            else:
                m = GPFloatMatrix(arg1, arg2)
                   
            if abs(m.determinant() - 1.0) > tolerance:
                raise ValueError, "Determinant of rotation matrix must be 1.0"
            if (m * m.transpose()).__ne__(GPFloatMatrix(1.0), tolerance=tolerance):
                raise ValueError, "Transpose of rotation matrix must be its inverse"

            # If trace of matrix is > -1, we can calculate quaternion quite simply.
            # The slightly roundabout treatment of the real term of the quaternion
            # can give better behaviour, avoiding the worst  aspects of dividing by
            # a small number, when the trace is close to -1.
            
            t = m.trace()
            if t > -1.0:
                s = 0.5 / math.sqrt( t + 1.0 )
                super(GPRotation, self).__init__( (  
                                                    ( m[2][1] - m[1][2]) * s,
                                                    ( m[0][2] - m[2][0]) * s,
                                                    ( m[1][0] - m[0][1]) * s,
                                                    0.25 / s
                                                    )
                )   
            else:
                # Find index of largest diagonal element
                u = max( range(len(m)), key=lambda k: m[k][k] )
                # Now use formalism described at
                # http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation#Quaternions_versus_other_representations_of_rotations
                # to calcuate terms of quaternion
                
                v = ( u + 1 ) % 3
                w = ( u + 2 ) % 3
                r = math.sqrt( 1.0 + m[u][u] - m[v][v] - m[w][w] )
                
                # Set up list to initialise quaternion.
                # We don't know in which order u, v and w are, so we first
                # initialise imaginary components with None, and then set
                # elements u, v and w
                q = [ None, None, None, (m[w][v] - m[v][w])/2.0/r ]
                q[u] = r/2.0
                q[v] = ( m[u][v] + m[v][u] )/2.0/r
                q[w] = ( m[w][u] + m[u][w] )/2.0/r
                
                super(GPRotation, self).__init__(q)

        self._normalise()
                
    def angleAxis(self):
        """ Return rotation as a list [ angle[radians], GPUnitVector ]""" 
        # Method taken from "Rotation Representations and Performance Issues"
        # section 3.2 "Quaternion to Axis-Angle", downloadable from
        # http://www.geometrictools.com/Documentation/Documentation.html
        if abs(self[3] - 1.0) < self.__class__.epsilon:
            # Special case when rotation is zero
            return (0.0, GPUnitVector((1.0, 0.0, 0.0)) )
        else:
            return [ 2.0 * math.acos(self[3]), 
                     GPUnitVector( GPFloatVector( self[:3] )/math.sqrt(1.0 - self[3]**2.0) )
                   ]

    
    def matrix(self):
        """Return rotation as a GPFloatMatrix"""
        # Set up list of lists to hold results
        m = [ [None] * 3, [None] * 3, [None] * 3 ]
        
        # General form for constructing this matrix deduced by inspection
        # from the standard expressions that can be found for the widely-quoted
        # matrix form, for example in section 3.3 "Quaternion to Matrix" of
        # "Rotation Representations and Performance Issues"
        for u in (0,1,2):
            # Cyclically next and next but one indices
            v = ( u + 1 ) % 3
            w = ( u + 2 ) % 3

            # Set diagonal element
            m[u][u] = 1.0 - 2.0 * ( self[v]**2.0 + self[w]**2.0 )
            
            # Set the two off-diagonal elements that contain q(0)*q(u)
            m[v][w] = 2.0 * ( self[v]*self[w] - self[3]*self[u] )
            m[w][v] = 2.0 * ( self[v]*self[w] + self[3]*self[u] )
            
        return GPFloatMatrix(m)
            
    def conjugate(self):
        """Return conjugate (inverse) of rotation.
        Can also call this method as 'r.inverse()'"""
        return type(self)( [ -e for e in self[:3] ] + [ self[3] ] )

    # Let people who think of this type as a 3x3 matrix call the inverse() and transpose()
    # methods if they are happier with them than "conjugate"
    inverse   = conjugate
    transpose = conjugate
         
    def getRow(self, row):
        """Return a GPUnitVector corresponding to the specified row of the rotation
        (considered to be a rotation matrix"""
        return GPUnitVector(self.matrix()[row])
         
    def getColumn(self, col):
        """Return a GPUnitVector corresponding to the specified column of the rotation
        (considered to be a rotation matrix"""
        return GPUnitVector(self.matrix().transpose()[col])
    
    def __abs__(self):
        """Override built-in abs(...) function to return magnitude of quaternion"""
        return math.sqrt( sum( [ v*v for v in self ] ) )

    def __mul__(self, other):

        if isinstance(other, GPRotation):
            # Calculate pure quaternion part of product, as vector
            vself  = GPFloatVector(self[:3])
            vother = GPFloatVector(other[:3])
            vretval = self[3] * vother + other[3] * vself + vself * vother
            
            # Now return whole result (type of vretval[:] is 'list', so '+' does
            # the Python list concatenation that we need
            return type(self)( vretval[:] + [ self[3] * other[3] - vself % vother ] )
        
        elif isinstance(other, GPVector):
            # Apply rotation to vector, and return transformed vector
            # Use equation 5.14 from "Quaternions and Rotation Sequences", Jack B.
            # Kuipers  (Princeton University Press, 1999), also noting the discussion
            # in section 5.15.3 that this is the correct way around for a rotation
            # of a vector in a fixed coordinate frame, not a rotation of a coordinate
            # frame around a vector.
            
            vself = GPFloatVector(self[:3])
            retval = ( self[3]**2.0 - abs(vself)**2.0 ) * other + \
                2.0 * ( ( vself % other ) * vself + self[3] * vself * other )
            
            # At this stage, retval is a GPFloatVector. If other was a GPUnitVector,
            # we need to return a GPUnitVector:
            if isinstance(other, GPUnitVector):
                return GPUnitVector(retval)
            else:
                return retval

        elif isinstance(other, GPMatrix):
            return self.matrix() * other
        
        else:
            return NotImplemented
            
    def __pow__(self, other, modulo=None):
        
        # Special case for zero power of rotation (return unit quaternion)
        if other == 0:
            return type(self)( (0, 0, 0, 1) )
        else:
            retval = super(GPRotation, self).__pow__( abs(other), modulo )
            if other < 0:
                return retval.conjugate()
            else:
                return retval
            
    # Need to take account of epsilon when comparing real types for equality

    def __eq__(self, other, tolerance=None):
        if tolerance is None:
            tolerance = self.__class__.epsilon
        for i in range(len(self)):
            if abs(self[i] - other[i]) > tolerance:
                return False
            
        return True
            
    def __ne__(self, other, tolerance=None):
        if tolerance is None:
            tolerance = self.__class__.epsilon
        for i in range(len(self)):
            if abs(self[i] - other[i]) > tolerance:
                return True
            
        return False

