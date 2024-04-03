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

from src.mech_idle import vec

def test_create_Vec2():
    v = vec.Vec2(1, 2)
    assert v.x == 1
    assert v.y == 2

def test_copy_Vec2():
    v = vec.Vec2(1, 2)
    v2 = v.copy()
    assert v2.x == 1
    assert v2.y == 2
    assert v is not v2

def test_offset_Vec2():
    v = vec.Vec2(1, 2)
    v2 = v.offset(3, 4)
    assert v2.x == 4
    assert v2.y == 6

    v = vec.Vec2(1, 2)
    v2 = v.offset(-3, -4)
    assert v2.x == -2
    assert v2.y == -2
