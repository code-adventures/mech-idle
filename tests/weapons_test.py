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
from src.mech_idle import weapons as weapons
from src.mech_idle import weapon_effects


class weapons_test(unittest.TestCase):
    def test_auto_cannon(self):
        ac = weapons.AutoCannon()
        self.assertEqual(ac.name, "AutoCannon")
        self.assertEqual(ac.damage, 1)
        self.assertEqual(ac.shield_damage, 0.2)
        self.assertEqual(ac.armor_damage, 0.8)
        self.assertEqual(ac.frequency, 1.0)
        self.assertEqual(ac.range, 400)
        self.assertEqual(ac.effect, weapon_effects.WeaponEffects.ROCKET)

    def test_beam_laser(self):
        bl = weapons.BeamLaser()
        self.assertEqual(bl.name, "BeamLaser")
        self.assertEqual(bl.damage, 3)
        self.assertEqual(bl.shield_damage, 0.8)
        self.assertEqual(bl.armor_damage, 0.2)
        self.assertEqual(bl.frequency, 0.3)
        self.assertEqual(bl.range, 800)
        self.assertEqual(bl.effect, weapon_effects.WeaponEffects.BEAM)

    def test_create_effect(self):
        source = object()
        target = object()
        time = 0
        duration = 100
        effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.ROCKET, source, target, time, duration)
        self.assertIsInstance(effect, weapon_effects.Rocket)

        effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.BEAM, source, target, time, duration)
        self.assertIsInstance(effect, weapon_effects.Beam)


if __name__ == '__main__':
    unittest.main()
        
