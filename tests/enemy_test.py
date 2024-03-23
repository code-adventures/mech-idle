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
from src.mech_idle import enemy
from src.mech_idle.vec import Vec2
from src.mech_idle import definitions

class enemy_test(unittest.TestCase):
    def test_create_enemy(self):
        e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
        self.assertEqual(e.get_pos(), Vec2(definitions.MECH.x + 1000, definitions.MECH.y))
        self.assertEqual(e.dist_to_mech(), 1000)

    def test_hit(self):
        e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
        dead = e.hit(10)
        self.assertEqual(e.health, 90)
        self.assertFalse(dead)

    def test_update(self):
        e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
        e.update(10)
        self.assertEqual(e.dist_to_mech(), 1000 - 10)

    def test_dead(self):
        enemy_list = []
        e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, enemy_list)
        dead = e.hit(200)
        self.assertTrue(dead)
        e.update(10)
        self.assertEqual(len(enemy_list), 0)

    def test_approach_mech(self):
        e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
        for i in range(1000):
            e.update(10 * i)
        self.assertEqual(e.dist_to_mech() < 200, False)
        
if __name__ == '__main__':
    unittest.main()
        
