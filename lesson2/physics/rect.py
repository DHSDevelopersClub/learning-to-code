from __future__ import division

__author__ = 'Alexander Otavka (zotavka@gmail.com)'
__copyright__ = 'Copyright (c) 2015 Alexander Otavka. All rights reserved.'

from math import copysign

from vector import Vector


class Rect(object):
    '''A rectangle class for dealing with collisions.'''

    def __init__(self, rect=None):
        '''Initialize a rect from an object with position and size.

        Parameters:
            rect (object): An object with properties `x`, `y`, `width`, `height`.
        '''
        if rect is None:
            self._pos = Vector()
            self._size = Vector()
        else:
            self._pos = Vector.new(rect.x, rect.y)
            self._size = Vector.new(rect.width, rect.height)

    @classmethod
    def new(cls, x, y, width, height):
        r = cls()
        r._pos = Vector.new(x, y)
        r._size = Vector.new(width, height)
        return r

    @property
    def x(self):
        return self._pos.x
    @x.setter
    def x(self, new):
        self._pos.x = new

    @property
    def y(self):
        return self._pos.y
    @y.setter
    def y(self, new):
        self._pos.y = new

    @property
    def width(self):
        return self._size.x
    @width.setter
    def width(self, new):
        self._size.x = new

    @property
    def height(self):
        return self._size.y
    @height.setter
    def height(self, new):
        self._size.y = new

    @property
    def topleft(self):
        return self._pos + Vector.new(0, self.height)
    @property
    def topright(self):
        return self._pos + self._size
    @property
    def bottomleft(self):
        return Vector(self._pos)
    @property
    def bottomright(self):
        return self._pos + Vector.new(self.width, 0)
    @property
    def center(self):
        return self._pos + self._size / 2

    def _get_collision_dist_array(self, other):
        xdist1 = other.topright.x - self.bottomleft.x
        xdist2 = other.bottomleft.x - self.topright.x
        ydist1 = other.topright.y - self.bottomleft.y
        ydist2 = other.bottomleft.y - self.topright.y
        return xdist1, xdist2, ydist1, ydist2

    def _check_collision_from_dist_array(self, dist_array):
        xdist1, xdist2, ydist1, ydist2 = dist_array
        if (copysign(1, xdist1) != copysign(1, xdist2) and
            copysign(1, ydist1) != copysign(1, ydist2)):
            return True
        return False

    def collides_with(self, other):
        return self._check_collision_from_dist_array(
            self._get_collision_dist_array(other))

    def get_collision_direction(self, other):
        dist_array = self._get_collision_dist_array(other)
        if not self._check_collision_from_dist_array(dist_array):
            return Vector()
        xdist1, xdist2, ydist1, ydist2 = dist_array
        xdist1 = abs(xdist1)
        xdist2 = abs(xdist2)
        ydist1 = abs(ydist1)
        ydist2 = abs(ydist2)
        if min(xdist1, xdist2) < min(ydist1, ydist2):
            return Vector.new(copysign(1, xdist1 - xdist2), 0)
        return Vector.new(0, copysign(1, ydist1 - ydist2))