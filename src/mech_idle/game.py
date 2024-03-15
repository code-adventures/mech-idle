
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

from random import randrange

from . import definitions
from .update import StatefulObject
from .player import Player
from .enemy import Enemy

class WaveController(StatefulObject):
    def __init__(self, enemy_list):
        super(WaveController, self).__init__()
        self.enemy_list = enemy_list

    def update(self, time):
        if len(self.enemy_list) == 0:
            for x in range(randrange(1, 5)):
                self.enemy_list.append(Enemy(definitions.ACTION_AREA.x + randrange(definitions.ACTION_AREA.x / 16) + 20, randrange(definitions.ACTION_AREA.y), randrange(2,10), 10, time, self.enemy_list))

class Game:
    def __init__(self):
        self.enemies = []
        self.player = Player(self.enemies)
        self.wave_controller = WaveController(self.enemies)
