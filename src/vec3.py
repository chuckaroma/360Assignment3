__author__ = 'sean'

""" A three-dimensional vector class for Python 3.
Most operations will as expected, v+w, v*2, 2*v, v/2, v[0], etc.
The dot product is called with v.dot(w), not the * operator.
"""

from math import sqrt


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        """
        :return: The norm/length/magnitude of the vector
        """
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalize(self):
        """
        :return: A new vector in the same direction, but unit length.
        """
        norm = sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

        if norm == 0:
            return Vec3(0, 0, 0)

        return Vec3(self.x/norm, self.y/norm, self.z/norm)

    def dot(self, other):
        """
        :param other: The Vec3 to dot product with this vector (the dot product is commutative)
        :return: The dot product or inner product of the two vectors.
        """
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __mul__(self, other):
        """
        Scalar Multiplication can be achieved by using the * operator.  If v = Vec3(1, 2, 3):
        v*2 returns a new Vec3 with values <2, 4, 6>

        :param other: A scalar (use dot() for a dot/inner product)
        :return: A new vector in the same direction as self, but scaled by other
        """
        if isinstance(other, Vec3):
            return Vec3(self.x*other.x, self.y*other.y,  self.z*other.z)
        else:
            return Vec3(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError()

        return Vec3(self.x/other, self.y/other,  self.z/other)

    def __add__(self, other):
        """
        Can be called simply like v + w, if v and w are Vec3's.

        :param other:  Another Vec3 to be added to self.
        :return: The sum of the two vectors.
        """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            return self.z

    def __repr__(self):
        return "<{0}, {1}, {2}>".format(self.x, self.y, self.z)

    def __len__(self):
        return 3
