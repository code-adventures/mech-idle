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
    imgui.text(f"Skills")
    with imgui.begin_table("Skills", 3, imgui.TABLE_SIZING_STRETCH_PROP) as table:
        imgui.table_setup_column("1", imgui.TABLE_COLUMN_WIDTH_STRETCH)
        imgui.table_setup_column("2", imgui.TABLE_COLUMN_WIDTH_FIXED)
        imgui.table_setup_column("3", imgui.TABLE_COLUMN_WIDTH_FIXED)
        for s in player.skills:
            imgui.table_next_row()
            imgui.table_next_column()
            imgui.progress_bar(min(1, player.xp / s.get_cost()), (-1, 0), f'{int(min(s.get_cost(), player.xp))}/{int(s.get_cost())}')
            imgui.table_next_column()
            imgui.text(s.name)
            imgui.table_next_column()
            if player.xp < s.get_cost():
                imgui.text(f'Upgrade to level {s.level+1}')
            else:
                imgui.push_id(s.name)
                if imgui.button(f'Upgrade to level {s.level+1}'):
                    player.xp -= s.get_cost()
                    s.level += 1
                imgui.pop_id()

