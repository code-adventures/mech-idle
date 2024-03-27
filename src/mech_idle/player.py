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
from .ui.drawing import Drawable
from . import weapon_effects
from . import hull
from . import setup
from . import weapons

class Skill:
    def __init__(self, name):
        self.name = name
        self.level = 0

    def get_cost(self):
        return math.pow(2,self.level)

class Player(Drawable, StatefulObject):
    def __init__(self, enemy_list):
        super(Player, self).__init__()
        self.xp = 0
        self.skills = [Skill("Rocket launch frequency"), Skill("Beam frequency")]
        self.enemy_list = enemy_list
        self.setup = setup.Setup()
        self.setup.setup(hull.hulls[0], { hull.MountPoints.LEFT_ARM: [ [weapons.AutoCannon()],[] ], hull.MountPoints.RIGHT_ARM: [ [weapons.BeamLaser()],[] ] })

    def shoot(self, time):
        self.setup.shoot(self, time, self.enemy_list)

    def update(self, time):
        self.shoot(time)
        return False

    def get_pos(self):
        return Vec2(definitions.MECH.x, definitions.MECH.y)

    def draw(self, transform, draw_list):
        draw_list.add_circle(transform.x(self.get_pos().x), transform.y(self.get_pos().y), transform.scale(definitions.MECH_RADIUS),
                             imgui.get_color_u32_rgba(0,0,1,1), thickness=transform.scale(4))
