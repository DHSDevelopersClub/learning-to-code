'''Tools for checking and handling collisions.'''

from __future__ import division

__author__ = 'Alexander Otavka (zotavka@gmail.com)'
__copyright__ = 'Copyright (c) 2015 Alexander Otavka. All rights reserved.'

from rect import Rect


def get_collision_direction(o1, o2):
    return Rect(o1).get_collision_direction(Rect(o2))

def is_colliding(o1, o2):
    return Rect(o1).collides_with(Rect(o2))
