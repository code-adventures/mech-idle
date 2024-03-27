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

import unittest
from src.mech_idle.vec import Vec2
from src.mech_idle import weapons
from src.mech_idle import weapon_effects

class source_target_mock():
    def get_pos(self):
        return Vec2(0, 0)

    def get_pos_at(self, time):
        return Vec2(0, 0)



class weapons_test(unittest.TestCase):
    def test_create_effect(self):
        source = source_target_mock()
        target = source_target_mock()
        time = 0
        duration = 100
        effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.ROCKET, source, target, time, duration)
        self.assertIsInstance(effect, weapon_effects.Rocket)

        effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.BEAM, source, target, time, duration)
        self.assertIsInstance(effect, weapon_effects.Beam)

        effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.BULLET, source, target, time, duration)
        self.assertIsInstance(effect, weapon_effects.Bullet)


if __name__ == '__main__':
    unittest.main()
        
