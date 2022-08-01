"""
Defines some mathematical objects in three-dimensional Euclidean space - R3 -
namely, the point and vector. Unary operations of the vector and point are
native to the classes.
"""

class R3Point:
    """
    Defines a point in Euclidean 3-space.
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Initialises a point with the given coords, defaults to origin. Coordinates
        must either be given in full as a str (x, y, z) or as separate arguments.
        If x alone is given, y and z default to 0, but x must be specified as 0 if
        y is to be given as a nonzero coordinate.
        """
        self._x, self._y, self._z = x, y, z

    def __str__(self) -> str:
        return "(" + str(self._x) + ", " + str(self._y) + ", " + str(self._z) + ")"

    def overwrite(self, x = 0, y = 0, z = 0):
        """
        Overwrites the current coordinates, defaulting to zero.
        """
        self._x, self._y, self._z = x, y, z


class R3Vector(R3Point):
    """
    Defines a vector in Euclidean 3-space, with some scalar and unary operations.
    """

    def __init__(self, point1: R3Point = R3Point(0, 0, 0), point2 = R3Point(0, 0, 0)):
        """
        Defines a new vector between point1 and point2. If point2 is not specified,
        gives the origin vector.
        """
        super().__init__(getattr(point1, '_x') - getattr(point2, '_x'), 
            getattr(point1, '_y') - getattr(point2, '_y'),
            getattr(point1, '_z') - getattr(point2, '_z'))

    def __str__(self) -> str:
        if (int(self._x) == self._x and int(self._y) == self._y and int(self._z) == self._z):
            self._x, self._y, self._z = int(self._x), int(self._y), int(self._z)
        return "<" + super().__str__()[1: -1] + ">"

    def magnitude(self) -> float:
        """
        Returns the magnitude of the vector.
        """
        return ((self._x) ** 2 + (self._y) ** 2 + (self._z ** 2)) ** 0.5

    def direction_vector(self):
        """
        Returns a unit vector in the direction of the original vector.
        """
        return self * (self.magnitude()**(-1))

    def reverse(self):
        """
        Returns the vector whose direction is opposite to this vector.
        """
        return self * -1

    def __add__(self, B):
        return R3Vector(R3Point(self._x + B._x, self._y + B._y, self._z + B._z))

    
    def __mul__(self, B: float):
        return R3Vector(R3Point(self._x * B, self._y * B, self._z * B))

    
    def __sub__(self, B):
        return R3Vector(R3Point(self._x - B._x, self._y - B._y, self._z - B._z))

    
    def __rmul__(self, B):
        return self * B

    
    def __eq__(self, B):
        return str(self) == str(B) and type(self) == type(B)

    
    def __ne__(self, B):
        return not self == B