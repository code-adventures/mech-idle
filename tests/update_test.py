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
from src.mech_idle import update as update


class ATestStatefulObject(update.StatefulObject):
    def __init__(self):
        super(ATestStatefulObject, self).__init__()
        self.update_calls = 0
        self.update_call_time = 0
        
    def update(self, time):
        self.update_calls += 1
        self.update_call_time = time
        

class update_test(unittest.TestCase):
    def test_stateful_object(self):
        o = ATestStatefulObject()
        self.assertEqual(o.update_calls, 0)
        self.assertEqual(o.update_call_time, 0)
        update.update(113)
        self.assertEqual(o.update_calls, 1)
        self.assertEqual(o.update_call_time, 113)

    def test_two_stateful_objects(self):
        o1 = ATestStatefulObject()
        self.assertEqual(o1.update_calls, 0)
        self.assertEqual(o1.update_call_time, 0)
        o2 = ATestStatefulObject()
        self.assertEqual(o2.update_calls, 0)
        self.assertEqual(o2.update_call_time, 0)
        update.update(113)
        self.assertEqual(o1.update_calls, 1)
        self.assertEqual(o1.update_call_time, 113)
        self.assertEqual(o2.update_calls, 1)
        self.assertEqual(o2.update_call_time, 113)

if __name__ == '__main__':
    unittest.main()
        
