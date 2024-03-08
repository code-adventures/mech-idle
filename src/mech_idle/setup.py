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

from . import hull

class Setup:
    def __init__(self):
        self.hull = None
        self.modules = dict()

    def setup(self, hull, modules):
        self.hull = hull
        self.modules = modules
        self.check_setup()

    def check_setup(self):
        if self.hull is None and bool(self.modules): # bool(self.modules) is True when not empty
            self.modules = dict()
        if self.hull is not None:
            for k,v in self.modules.items():
                c = self.hull.hardpoints[k]
                v[0] = v[0][:c[0]]    # drop every module after the available number of hardpoints
                v[1] = v[1][:c[1]]


