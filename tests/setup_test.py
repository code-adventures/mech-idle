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
from src.mech_idle import setup as setup
from src.mech_idle import hull as hull


class setup_test(unittest.TestCase):
    def test_default_setup(self):
        my_setup = setup.Setup()
        self.assertEqual(my_setup.hull, None)
        self.assertEqual(my_setup.modules, dict())

    def test_empty_setup(self):
        my_hull = hull.Hull(0, "Test", 1, hull.Hull.create_mountpoints(head=(1,1)))
        my_setup = setup.Setup()
        my_setup.setup(my_hull, dict())
        self.assertEqual(my_setup.hull, my_hull)
        self.assertEqual(my_setup.modules, dict())

    def test_too_long_setup(self):
        my_hull = hull.Hull(0, "Test", 1, hull.Hull.create_mountpoints(head=(1,1)))
        my_setup = setup.Setup()
        my_setup.setup(my_hull, {hull.MountPoints.HEAD: [[1,2,3],[1,2,3]]})
        self.assertEqual(my_setup.hull, my_hull)
        self.assertEqual(my_setup.modules, {hull.MountPoints.HEAD: [[1],[1]]})

if __name__ == '__main__':
    unittest.main()
        
