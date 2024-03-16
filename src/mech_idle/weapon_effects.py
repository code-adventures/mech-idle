#
#    Mech Idle - an idle mech game
#    Copyright (C) 2024 Code Adventures
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import imgui
import math

from random import randrange
from enum import IntEnum

from . import definitions
from .vec import Vec2
from .drawing import Drawable
from .update import StatefulObject

class WeaponEffects(IntEnum):
    BEAM = 0
    ROCKET = 1

def create_effect(effect, source, target, time, duration):
    if effect == WeaponEffects.BEAM:
        return Beam(source, target, time, duration)
    elif effect == WeaponEffects.ROCKET:
        return Rocket(source, target, time, duration)
    else:
        return None

class Beam(Drawable, StatefulObject):
    def __init__(self, source, target, time, duration):
        super(Beam, self).__init__()
        self.source = source
        self.target = target
        self.start = time
        self.duration = duration

    def draw(self, transform, draw_list):
        target_pos = self.target.get_pos()
        MY = self.source.get_pos().y + (definitions.MECH_RADIUS * (-1 if target_pos.y < self.source.get_pos().y else 1))
        draw_list.add_line(transform.x(self.source.get_pos().x), transform.y(MY),
                           transform.x(target_pos.x), transform.y(target_pos.y),
                           imgui.get_color_u32_rgba(0,0,1,1), 2)

    def update(self, time):
        done = self.start + self.duration <= time
        if done:
            super().remove_drawable()
            super().remove_stateful_object()
            if self.target.hit(1):
                self.source.xp += 1 
        return done


def bezier(p1, p2, p3, ratio):
    p11 = Vec2(p1.x + (p2.x - p1.x)*ratio, p1.y + (p2.y - p1.y)* ratio)
    p21 = Vec2(p2.x + (p3.x - p2.x)*ratio, p2.y + (p3.y - p2.y)* ratio)

    return Vec2(p11.x + (p21.x - p11.x)*ratio, p11.y + (p21.y -p11.y)* ratio)

class Rocket(Drawable, StatefulObject):
    def __init__(self, source, target, time, duration):
        super(Rocket, self).__init__()
        self.source = source
        self.target = target
        self.start = time
        self.duration = duration
        self.now = self.start

    def draw(self, transform, draw_list):
        target_pos = self.target.get_pos()

        MY = self.source.get_pos().y + (definitions.MECH_RADIUS * (-1 if target_pos.y < self.source.get_pos().y else 1))
        Y = 0 if target_pos.y < self.source.get_pos().y else definitions.ACTION_AREA.y
        pos = bezier(Vec2(self.source.get_pos().x, MY), Vec2(self.source.get_pos().x, Y), target_pos, (self.now - self.start)/self.duration)
        draw_list.add_circle(transform.x(pos.x), transform.y(pos.y), transform.scale(1), imgui.get_color_u32_rgba(0,1,0,1), thickness=transform.scale(1))

    def update(self, time):
        done = self.start + self.duration <= time
        self.now = time
        if done:
            super().remove_drawable()
            super().remove_stateful_object()
            if self.target.hit(1):
                self.source.xp += 1
        return done
