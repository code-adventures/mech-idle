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
from src.mech_idle import vec as vec
from src.mech_idle.ui import drawing as drawing

class ATestDrawable(drawing.Drawable):
    def __init__(self):
        super(ATestDrawable, self).__init__()
        self.draw_calls = 0
        
    def draw(self, transform, draw_list):
        super(ATestDrawable, self).draw(transform, draw_list)
        self.draw_calls += 1
        

class drawing_test(unittest.TestCase):
    def test_transform_identity(self):
        t = drawing.Transform(vec.Vec2(0,0), 1)
        self.assertEqual(t.x(1), 1)
        self.assertEqual(t.x(10), 10)
        self.assertEqual(t.y(1), 1)
        self.assertEqual(t.y(10), 10)
        self.assertEqual(t.scale(1), 1)
        self.assertEqual(t.scale(10), 10)

    def test_transform(self):
        t = drawing.Transform(vec.Vec2(10,10), 1.5)
        self.assertEqual(t.x(1), 11.5)
        self.assertEqual(t.x(10), 25)
        self.assertEqual(t.y(1), 11.5)
        self.assertEqual(t.y(10), 25)
        self.assertEqual(t.scale(1), 1.5)
        self.assertEqual(t.scale(10), 15)

    def test_drawable(self):
        d = ATestDrawable()
        self.assertEqual(d.draw_calls, 0)
        t = drawing.Transform(vec.Vec2(0,0), 1)
        draw_list = []
        drawing.draw(t, draw_list)
        self.assertEqual(d.draw_calls, 1)
        d.remove_drawable()
        drawing.draw(t, draw_list)
        self.assertEqual(d.draw_calls, 1)

    def test_two_drawables(self):
        t = drawing.Transform(vec.Vec2(0,0), 1)
        draw_list = []

        d1 = ATestDrawable()
        self.assertEqual(d1.draw_calls, 0)
        drawing.draw(t, draw_list)
        self.assertEqual(d1.draw_calls, 1)  
        d2 = ATestDrawable()
        self.assertEqual(d2.draw_calls, 0)
        drawing.draw(t, draw_list)
        self.assertEqual(d1.draw_calls, 2)
        self.assertEqual(d2.draw_calls, 1)
        d1.remove_drawable()
        drawing.draw(t, draw_list)
        self.assertEqual(d1.draw_calls, 2)
        self.assertEqual(d2.draw_calls, 2)
        d2.remove_drawable()
        drawing.draw(t, draw_list)
        self.assertEqual(d1.draw_calls, 2)
        self.assertEqual(d2.draw_calls, 2)

if __name__ == '__main__':
    unittest.main()
        
