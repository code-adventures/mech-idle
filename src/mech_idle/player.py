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
from random import randrange
import math
import imgui

from . import definitions
from .vec import Vec2
from .update import StatefulObject
from .drawing import Drawable
from . import weapon_effects

class Skill:
    def __init__(self, name):
        self.name = name
        self.level = 0

    def get_cost(self):
        return math.pow(2,self.level)

class Player(Drawable, StatefulObject):
    def __init__(self, enemy_list):
        super(Player, self).__init__()
        self.last_shot = 0
        self.xp = 0
        self.skills = [Skill("Rocket launch frequency"), Skill("Beam frequency")]
        self.enemy_list = enemy_list

    def shoot(self, time):
        if self.last_shot + 500 <= time and len(self.enemy_list) > 0:
            if randrange(2) < 1:
                weapon_effects.Rocket(self, self.enemy_list[randrange(len(self.enemy_list))], time, 2000)
            else:
                weapon_effects.Beam(self, self.enemy_list[randrange(len(self.enemy_list))], time, 500)
            self.last_shot = time

    def update(self, time):
        self.shoot(time)
        return False

    def get_pos(self):
        return Vec2(definitions.MECH.x, definitions.MECH.y)

    def draw(self, transform, draw_list):
        draw_list.add_circle(transform.x(self.get_pos().x), transform.y(self.get_pos().y), transform.scale(definitions.MECH_RADIUS),
                             imgui.get_color_u32_rgba(0,0,1,1), thickness=transform.scale(4))
