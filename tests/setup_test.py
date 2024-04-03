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

from src.mech_idle import setup as setup
from src.mech_idle import hull as hull
from src.mech_idle import weapons

def test_default_setup():
    my_setup = setup.Setup()
    assert my_setup.hull == None
    assert my_setup.modules == dict()

def test_empty_hull_but_modules():
    my_setup = setup.Setup()
    my_setup.setup(None, {hull.MountPoints.HEAD: [[1,2,3],[1,2,3]]})
    assert my_setup.hull == None
    assert my_setup.modules == dict()

def test_empty_setup():
    my_hull = hull.Hull(0, "Test", 1, hull.Hull.create_mountpoints(head=(1,1)))
    my_setup = setup.Setup()
    my_setup.setup(my_hull, dict())
    assert my_setup.hull == my_hull
    assert my_setup.modules == dict()

def test_too_long_setup():
    my_hull = hull.Hull(0, "Test", 1, hull.Hull.create_mountpoints(head=(1,1)))
    my_setup = setup.Setup()
    my_setup.setup(my_hull, {hull.MountPoints.HEAD: [[1,2,3],[1,2,3]]})
    assert my_setup.hull == my_hull
    assert my_setup.modules == {hull.MountPoints.HEAD: [[1],[1]]}

class Enemy_Mock:
    pass

def test_shoot(mocker):
    my_hull = hull.Hull(0, "Test", 1, hull.Hull.create_mountpoints(head=(1,1)))
    my_setup = setup.Setup()
    my_setup.setup(my_hull, {hull.MountPoints.HEAD: [[weapons.AutoCannon()],[]]})
    m = mocker.patch('src.mech_idle.weapons.AutoCannon.shoot')
    e = Enemy_Mock()
    my_setup.shoot(None, 0, [e])
    m.assert_called_once()
    
