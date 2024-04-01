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
from dataclasses import dataclass

@dataclass
class Skill:
    name: str
    label: str
    initial_level: int
    max_level: int
    base_cost: int
    exponent: float
    level: int

    def cost(self):
        return self.cost_to_level(self.level+1)

    def cost_to_level(self, target_level):
        return self.base_cost * target_level ** self.exponent


class Skills:
    def __init__(self):
        self.skills = {}
        self.add_skill(Skill("mech_control", "Mech Control", 0, 5, 100, 2.5, 0))

    def add_skill(self, skill):
        self.skills[skill.name] = skill

    def get_skill(self, name):
        return self.skills[name]

