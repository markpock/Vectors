"""
Defines some binary operations for mathematical objects in R3, vectors in particular.
"""

from R3Inheritance import R3Vector, R3Point
import math


"""
The three basis vectors.
"""
I, J, K  = R3Vector(R3Point(1, 0, 0)), R3Vector(R3Point(0, 1, 0)), R3Vector(R3Point(0, 0, 1))


def sum(A: R3Vector, B: R3Vector) -> R3Vector:
    """
    Returns a vector representing the sum of A and B.
    """
    return R3Vector(R3Point(getattr(A, '_R3Point_x') + getattr(B, '_R3Point_x'),
            getattr(A, '_R3Point_y') + getattr(B, '_R3Point_y'), 
            getattr(A, '_R3Point_z') + getattr(B, '_R3Point_z')))


def difference(A: R3Vector, B: R3Vector) -> R3Vector:
    """
    Returns a vector representing the difference of B from A.
    """
    return R3Vector(R3Point(getattr(A, '_R3Point_x') - getattr(B, '_R3Point_x'),
            getattr(A, '_R3Point_y') - getattr(B, '_R3Point_y'), 
            getattr(A, '_R3Point_z') - getattr(B, '_R3Point_z')))


def cross_product(A: R3Vector, B: R3Vector) -> R3Vector:
    """
    Returns the cross product of two vectors. Since cross products are anticommutative,
    it is useful to note that this vector is A and the other vector is B where a
    cross product is A x B.
    """
    x = (getattr(A, '_R3Point_y') * getattr(B, '_R3Point_z')
            - getattr(A, '_R3Point_z') * getattr(B, '_R3Point_y'))
    y = (getattr(A, '_R3Point_z') * getattr(B, '_R3Point_x')
            - getattr(A, '_R3Point_x') * getattr(B, '_R3Point_z'))
    z = (getattr(A, '_R3Point_x') * getattr(B, '_R3Point_y')
            - getattr(A, '_R3Point_y') * getattr(B, '_R3Point_x'))
    return R3Vector(R3Point(x, y, z))


def dot_product(A: R3Vector, B: R3Vector) -> float:
    """
    Takes the dot product of two vectors.
    """
    dp = (getattr(A, '_R3Point_x') * getattr(B, '_R3Point_x') +
          getattr(A, '_R3Point_y') * getattr(B, '_R3Point_y') +
          getattr(A, '_R3Point_z') * getattr(B, '_R3Point_z'))
    if dp // 1 == dp:
        return int(dp)
    else:
        return dp


def are_parallel(A: R3Vector, B: R3Vector) -> bool:
    """
    Tests for whether or not vectors A and B are parallel.
    """
    test = A.scalar_mult(getattr(A, '_R3Point_x') / getattr(B, '_R3Point_x'))
    return (getattr(test, '_R3Point_x') == getattr(B, '_R3Point_x') and
            getattr(test, '_R3Point_y') == getattr(B, '_R3Point_y') and
            getattr(test, '_R3Point_z') == getattr(B, '_R3Point_z'))


def are_orthogonal(A: R3Vector, B: R3Vector) -> bool:
    """
    Tests for whether or not vectors A and B are orthogonal.
    """
    return dot_product(A, B) == 0


def scalar_projection(A: R3Vector, B: R3Vector) -> float:
    """
    Returns comp_A{B}, the scalar projection of B onto A, as a real number.
    """
    return dot_product(A, B) / A.magnitude()


def vector_projection(A: R3Vector, B: R3Vector) -> R3Vector:
    """
    Returns the vector projection of B onto A.
    """
    return A.direction_vector().scalar_mult(scalar_projection(A, B))


def angle(A: R3Vector, B: R3Vector) -> float:
    """
    Returns the angle in degrees formed by two vectors A and B.
    """
    return (math.acos(dot_product(A, B) / (A.magnitude() * B.magnitude()))) * (180/math.pi)