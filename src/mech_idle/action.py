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

from dataclasses import dataclass
from random import randrange

from . import definitions
from .vec import Vec2
from .drawing import Drawable
from .update import StatefulObject
from . import weapon_effects

enemies = []

class Enemy(Drawable, StatefulObject):
    def __init__(self, x, y, speed, health, created):
        super(Enemy, self).__init__()
        self.start = Vec2(x, y)
        self.pos = Vec2(x, y)
        self.health = health
        self.created = created
        alpha = math.atan((y - definitions.MECH.y) / (x - definitions.MECH.x))
        dist = ((x - definitions.MECH.x) / math.cos(alpha)) - 250
        self.delta_x = dist * math.cos(alpha) / (dist / speed)
        self.delta_y = dist * math.sin(alpha) / (dist / speed)

    def update(self, time):
        if self.health <= 0:
            if self in enemies: enemies.remove(self)
            super().remove_drawable()
            super().remove_stateful_object()
            return True
        if self.pos.x > definitions.MECH.x + 250:
            steps = (time - self.created) / 100 
            self.pos.x = self.start.x - self.delta_x * steps
            self.pos.y = self.start.y - self.delta_y * steps
        return False

    def get_pos(self):
        return self.pos

    def draw(self, transform, draw_list):
        draw_list.add_circle(transform.x(self.pos.x), transform.y(self.pos.y), transform.scale(definitions.ENEMY_RADIUS),
                             imgui.get_color_u32_rgba(1,0,0,1), thickness=transform.scale(2))

    def hit(self, dmg):
        self.health -= dmg;
        

class Mech(Drawable, StatefulObject):
    def __init__(self):
        super(Mech, self).__init__()
        self.last_shot = 0

    def shoot(self, time):
        if self.last_shot + 500 <= time and len(enemies) > 0:
            if randrange(2) < 1:
                weapon_effects.Rocket(self, enemies[randrange(len(enemies))], time, 2000)
            else:
                weapon_effects.Beam(self, enemies[randrange(len(enemies))], time, 500)
            self.last_shot = time

    def update(self, time):
        self.shoot(time)
        return False

    def get_pos(self):
        return Vec2(definitions.MECH.x, definitions.MECH.y)

    def draw(self, transform, draw_list):
        draw_list.add_circle(transform.x(self.get_pos().x), transform.y(self.get_pos().y), transform.scale(definitions.MECH_RADIUS),
                             imgui.get_color_u32_rgba(0,0,1,1), thickness=transform.scale(4))

class WaveController(StatefulObject):
    def __init__(self):
        super(WaveController, self).__init__()

    def update(self, time):
        if len(enemies) == 0:
            for x in range(randrange(1, 5)):
                enemies.append(Enemy(definitions.ACTION_AREA.x + randrange(definitions.ACTION_AREA.x / 16) + 20, randrange(definitions.ACTION_AREA.y), randrange(2,10), 10, time))

def dimensions():
    return Vec2(definitions.ACTION_AREA.x / 100, definitions.ACTION_AREA.y / 100)

Mech()
WaveController()
