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
from src.mech_idle import hull as hull

class hull_test(unittest.TestCase):
    def test_create_mountpoints_default(self):
        mp = hull.Hull.create_mountpoints()
        self.assertEqual(mp[hull.MountPoints.HEAD], (0,0))
        self.assertEqual(mp[hull.MountPoints.TORSO], (0,0))
        self.assertEqual(mp[hull.MountPoints.LEFT_ARM], (0,0))
        self.assertEqual(mp[hull.MountPoints.RIGHT_ARM], (0,0))
        self.assertEqual(mp[hull.MountPoints.LEFT_SHOULDER], (0,0))
        self.assertEqual(mp[hull.MountPoints.RIGHT_SHOULDER], (0,0))
        self.assertEqual(mp[hull.MountPoints.LEFT_LEG], (0,0))
        self.assertEqual(mp[hull.MountPoints.RIGHT_LEG], (0,0))

    def test_create_mountpoints(self):
        mp = hull.Hull.create_mountpoints(head=(1,1), torso=(2,2), left_arm=(3,3), right_arm=(4,4), left_shoulder=(5,5), right_shoulder=(6,6), left_leg=(7,7), right_leg=(8,8))
        self.assertEqual(mp[hull.MountPoints.HEAD], (1,1))
        self.assertEqual(mp[hull.MountPoints.TORSO], (2,2))
        self.assertEqual(mp[hull.MountPoints.LEFT_ARM], (3,3))
        self.assertEqual(mp[hull.MountPoints.RIGHT_ARM], (4,4))
        self.assertEqual(mp[hull.MountPoints.LEFT_SHOULDER], (5,5))
        self.assertEqual(mp[hull.MountPoints.RIGHT_SHOULDER], (6,6))
        self.assertEqual(mp[hull.MountPoints.LEFT_LEG], (7,7))
        self.assertEqual(mp[hull.MountPoints.RIGHT_LEG], (8,8))

    def test_create_mountpoints_mixed(self):
        mp = hull.Hull.create_mountpoints(head=(1,1), left_arm=(3,3), right_shoulder=(6,6))
        self.assertEqual(mp[hull.MountPoints.HEAD], (1,1))
        self.assertEqual(mp[hull.MountPoints.TORSO], (0,0))
        self.assertEqual(mp[hull.MountPoints.LEFT_ARM], (3,3))
        self.assertEqual(mp[hull.MountPoints.RIGHT_ARM], (0,0))
        self.assertEqual(mp[hull.MountPoints.LEFT_SHOULDER], (0,0))
        self.assertEqual(mp[hull.MountPoints.RIGHT_SHOULDER], (6,6))
        self.assertEqual(mp[hull.MountPoints.LEFT_LEG], (0,0))
        self.assertEqual(mp[hull.MountPoints.RIGHT_LEG], (0,0))


if __name__ == '__main__':
    unittest.main()
        
