from __future__ import division

__author__ = 'Alexander Otavka (zotavka@gmail.com)'
__copyright__ = 'Copyright (c) 2015 Alexander Otavka. All rights reserved.'


from math import sqrt, sin, cos, atan2, copysign


class Vector(object):
    '''A mutable two dimensional vector class.'''

    def __init__(self, vector=None):
        '''Initialize a vector.

        :Parameters:
            `vector` : object
                Iterable with numbers at indices 0 and 1, or an object with attributes `x` and `y`.
        '''
        if vector is None:
            self._x = 0
            self._y = 0
        else:
            try:
                self._x = vector.x
                self._y = vector.y
            except AttributeError:
                self._x = vector[0]
                self._y = vector[1]

    @classmethod
    def new(cls, x, y):
        '''Initialize a vector from cartesian coordinates.'''
        v = cls()
        v._x = x
        v._y = y
        return v

    @classmethod
    def new_polar(cls, m, d):
        v = cls()
        v._x = m * cos(d)
        v._y = m * sin(d)
        return v

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def components(self):
        return (self.x, self.y)

    @property
    def m(self):
        '''Magnitude of the vector.'''
        return sqrt(self.x ** 2 + self.y ** 2)

    @property
    def d(self):
        '''Direction of the vector.'''
        return atan2(self.y, self.x)

    def copysign(self, other):
        if other.x != 0:
            self.x = copysign(self.x, other.x)
        if other.y != 0:
            self.y = copysign(self.y, other.y)

    def __add__(self, other):
        return Vector.new(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector.new(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, scalar):
        return Vector.new(self.x * scalar, self.y * scalar)
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Vector.new(self.x / scalar, self.y / scalar)
    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self
    __rtruediv__ = __truediv__

    def __neg__(self):
        return Vector.new(-self.x, -self.y)

    def __nonzero__(self):
        return self.x != 0 or self.y != 0

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Vector.new({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)
