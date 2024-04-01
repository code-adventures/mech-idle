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
from dataclasses import dataclass
from .weapon_effects import WeaponEffects, create_effect

@dataclass
class Weapon:
    name: str
    damage: int
    shield_damage: float
    armor_damage: float
    frequency: float
    range: int
    effect: WeaponEffects
    last_shot = 0

    def shoot(self, owner, mount_point, time, enemy_list):
        if self.last_shot + 1000/self.frequency <= time and len(enemy_list) > 0:
            prepared_list = [(e, e.dist_to_mech()) for e in enemy_list]
            enemy = self.find_enemy(prepared_list)
            if enemy is not None:
                create_effect(self.effect, owner, mount_point, enemy, time, 2500)
                self.last_shot = time

    def find_enemy(self, prepared_list):
        possible_enemies = [e[0] for e in prepared_list if e[1] < self.range]
        return possible_enemies[0] if len(possible_enemies) > 0 else None

class AutoCannon(Weapon):
    def __init__(self):
        super(AutoCannon, self).__init__("AutoCannon", 1, 0.2, 0.8, 8.0, 1400, WeaponEffects.BULLET)

class BeamLaser(Weapon):
    def __init__(self):
        super(BeamLaser, self).__init__("BeamLaser", 3, 0.8, 0.2, 0.3, 800, WeaponEffects.BEAM)
    
