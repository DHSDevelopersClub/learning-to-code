'''Unit tests for physics package.

Call run() to execute all unit tests, or specify a subclass of PhysicsUnitTest to run only tests
defined in it's subclass tree.
'''

from __future__ import division

__author__ = 'Alexander Otavka (zotavka@gmail.com)'
__copyright__ = 'Copyright (c) 2015 Alexander Otavka. All rights reserved.'

import unittest
from math import sqrt, atan2, sin, cos, pi

from collision import *
from vector import *
from rect import *


class PhysicsUnitTest(unittest.TestCase):

    @classmethod
    def _load_test_suite(cls):
        return unittest.TestLoader().loadTestsFromTestCase(cls)

    @classmethod
    def _get_subclasses(cls):
        subclasses = cls.__subclasses__()
        if len(subclasses) == 0:
            return [cls]
        else:
            leaves = []
            for subclass in subclasses:
                leaves += subclass._get_subclasses()
            return leaves

    @classmethod
    def get_suite(cls):
        return unittest.TestSuite([test._load_test_suite() for test in cls._get_subclasses()])


class VectorTest(PhysicsUnitTest):

    def make_blank_vector(self):
        self.v1 = Vector()

    def make_xy_vector(self):
        self.v2x = 3
        self.v2y = 4.6
        self.v2m = sqrt(self.v2x ** 2 + self.v2y ** 2)
        self.v2d = atan2(self.v2y, self.v2x)
        self.v2 = Vector.new(self.v2x, self.v2y)
        self.nv2 = -self.v2

    def make_polar_vector(self):
        self.v3m = 7
        self.v3d = 3
        self.v3x = self.v3m * cos(self.v3d)
        self.v3y = self.v3m * sin(self.v3d)
        self.v3 = Vector.new_polar(self.v3m, self.v3d)

class BlankVectorTest(VectorTest):

    def setUp(self):
        self.make_blank_vector()

    def test_xy(self):
        self.assertEqual(self.v1.x, 0)
        self.assertEqual(self.v1.y, 0)

    def test_polar(self):
        self.assertEqual(self.v1.d, 0)
        self.assertEqual(self.v1.m, 0)

    def test_neg(self):
        self.assertEqual(-self.v1, self.v1)

class XYVectorTest(VectorTest):

    def setUp(self):
        self.make_xy_vector()

    def test_xy(self):
        self.assertEqual(self.v2.x, self.v2x)
        self.assertEqual(self.v2.y, self.v2y)

    def test_polar(self):
        self.assertEqual(self.v2.d, self.v2d)
        self.assertEqual(self.v2.m, self.v2m)

    def test_neg_xy(self):
        self.assertEqual(self.nv2.x, -self.v2x)
        self.assertEqual(self.nv2.y, -self.v2y)

    def test_neg_polar(self):
        self.assertEqual(self.nv2.d, atan2(-self.v2y, -self.v2x))
        self.assertEqual(self.nv2.m, self.v2m)

class BlankVectorMathTest(VectorTest):

    def setUp(self):
        self.make_blank_vector()
        self.make_xy_vector()

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, self.v2)

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, self.nv2)

    def test_iadd(self):
        self.v2 += self.v1
        self.assertEqual(self.v2.x, self.v2x)
        self.assertEqual(self.v2.y, self.v2y)

    def test_isub(self):
        self.v2 -= self.v1
        self.assertEqual(self.v2.x, self.v2x)
        self.assertEqual(self.v2.y, self.v2y)

class PolarVectorTest(VectorTest):

    def setUp(self):
        self.make_polar_vector()

    def test_xy(self):
        self.assertEqual(self.v3.x, self.v3x)
        self.assertEqual(self.v3.y, self.v3y)

    def test_polar(self):
        self.assertEqual(self.v3.m, self.v3m)
        self.assertEqual(self.v3.d, self.v3d)

class VectorMathTest(VectorTest):

    def setUp(self):
        self.make_xy_vector()
        self.make_polar_vector()
        self.v4 = self.v2 + self.v3
        self.v5 = self.v2 - self.v3

    def test_add(self):
        self.assertEqual(self.v4.x, self.v2x + self.v3x)
        self.assertEqual(self.v4.y, self.v2y + self.v3y)

    def test_sub(self):
        self.assertEqual(self.v5.x, self.v2x - self.v3x)
        self.assertEqual(self.v5.y, self.v2y - self.v3y)

class VectorCompareTest(VectorTest):

    def setUp(self):
        self.make_xy_vector()
        self.make_polar_vector()
        self.v2copy = Vector(self.v2)

    def test_copy(self):
        self.assertEqual(self.v2.x, self.v2copy.x)
        self.assertEqual(self.v2.y, self.v2copy.y)
        self.assertFalse(self.v2 is self.v2copy)

    def test_eq(self):
        self.assertTrue(self.v2 == self.v2copy)
        self.assertFalse(self.v2 == self.v3)

    def test_ne(self):
        self.assertTrue(self.v2 != self.v3)
        self.assertFalse(self.v2 != self.v2copy)


class CollisionTest(PhysicsUnitTest):

    class Collidable(object):
        def __init__(self):
            self.x = 0
            self.y = 0
            self.width = 10
            self.height = 10

    def setUp(self):
        self.o1 = CollisionTest.Collidable()
        self.o2 = CollisionTest.Collidable()

    def test_full(self):
        self.assertEqual(get_collision_direction(self.o1, self.o2), Vector.new(0, 1))

    def test_corner(self):
        self.o1.x = self.o1.y = 5
        self.assertEqual(get_collision_direction(self.o1, self.o2), Vector.new(0, -1))

    def test_vertical(self):
        self.o1.y = 5
        self.assertEqual(get_collision_direction(self.o1, self.o2), Vector.new(0, -1))

    def test_horizontal(self):
        self.o1.x = 5
        self.assertEqual(get_collision_direction(self.o1, self.o2), Vector.new(-1, 0))

    def test_contain(self):
        self.o1.x = self.o1.y = 5
        self.o2.width = self.o2.height = 20
        self.assertTrue(is_colliding(self.o1, self.o2))

    def test_no_collision(self):
        self.o1.x = 20
        self.assertFalse(is_colliding(self.o1, self.o2))
        self.o1.y = 20
        self.assertFalse(is_colliding(self.o1, self.o2))


def run(scope=None):
    '''Run unit tests.

    :Parameters:
        `scope` : `type`
            A subclass of `PhysicsUnitTest`, only run tests in it's subclass tree.
    '''
    if scope is None:
        scope = PhysicsUnitTest
    suite = scope.get_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run()
