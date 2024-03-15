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
import math
import imgui

def draw(player):
    imgui.text("XP: " + str(player.xp))
    
    for s in player.skills:
        imgui.progress_bar(min(1, player.xp / s.get_cost()), (200, 0), f'{min(s.get_cost(), player.xp)}/{s.get_cost()}')
        imgui.same_line()
        imgui.text(s.name)
        if imgui.button(f'Level {s.level+1}'):
            player.xp -= s.get_cost()
            s.level += 1

