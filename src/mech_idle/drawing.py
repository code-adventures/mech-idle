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

import imgui
from . import definitions

drawables = []

class Drawable:
    def __init__(self):
        super(Drawable, self).__init__()
        drawables.append(self)

    def draw(self, transform, draw_list):
        pass

    def remove_drawable(self):
        if self in drawables: drawables.remove(self)

class Transform:
    def __init__(self, pos, ratio):
        self.pos = pos
        self.ratio = ratio

    def x(self, _x):
        return self.pos.x + _x*self.ratio

    def y(self, _y):
        return self.pos.y + _y*self.ratio

    def scale(self, v):
        return v*self.ratio;

def draw(transform, draw_list):

    for d in drawables:
        d.draw(transform, draw_list)

