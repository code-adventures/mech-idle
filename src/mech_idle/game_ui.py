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

from .game import Game

def draw(game: Game):
    imgui.text(f"XP: {int(game.player.xp)}")
    imgui.text(f"Wave: {game.wave_controller.wave}")
    imgui.text(f"Enemies: {len(game.enemies)}")
    for e in game.enemies:
        imgui.text(f" {e.health} => {int(e.dist_to_mech())}")
