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
import math
import imgui

from . import definitions
from .vec import Vec2
from .drawing import Drawable
from .update import StatefulObject

class Enemy(Drawable, StatefulObject):
    def __init__(self, x, y, speed, health, created, enemy_list):
        super(Enemy, self).__init__()
        self.start = Vec2(x, y)
        self.pos = Vec2(x, y)
        self.health = health
        self.created = created
        alpha = math.atan((y - definitions.MECH.y) / (x - definitions.MECH.x))
        dist = ((x - definitions.MECH.x) / math.cos(alpha)) - 250
        self.delta_x = dist * math.cos(alpha) / (dist / speed)
        self.delta_y = dist * math.sin(alpha) / (dist / speed)
        self.enemy_list = enemy_list

    def update(self, time):
        if self.health <= 0:
            if self in self.enemy_list: self.enemy_list.remove(self)
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
        dead = self.health <= 0
        h = self.health
        self.health -= dmg
        more_dead = self.health <= 0
        died = dead != more_dead
        print (f'{dead},{h} -> {more_dead},{self.health} -> {died}')
        return died
