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

from src.mech_idle import enemy
from src.mech_idle.vec import Vec2
from src.mech_idle import definitions

def test_create_enemy():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    assert e.get_pos() == Vec2(definitions.MECH.x + 1000, definitions.MECH.y)
    assert e.dist_to_mech() == 1000

def test_hit():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    dead = e.hit(10)
    assert e.health == 90
    assert dead == False

def test_update():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    e.update(10)
    assert e.dist_to_mech() == 1000 - 10

def test_dead():
    enemy_list = []
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, enemy_list)
    dead = e.hit(200)
    assert dead == True
    e.update(10)
    assert len(enemy_list) == 0

def test_approach_mech():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    for i in range(1000):
        e.update(10 * i)
    assert e.dist_to_mech() >= 200

def test_get_pos_at():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    assert e.get_pos_at(10) == Vec2(definitions.MECH.x + 1000 - 10, definitions.MECH.y)

def test_dist_to_mech_at():
    e = enemy.Enemy(Vec2(definitions.MECH.x + 1000, definitions.MECH.y), 100, 100, 0, [])
    assert e.dist_to_mech_at(10) == 1000 - 10
