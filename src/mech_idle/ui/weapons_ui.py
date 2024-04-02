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
from . import fonts

def draw(weapon):
    fonts.header_text(f"{weapon.name}")
    imgui.text(f"Damage: {weapon.damage}")
    imgui.text(f"Shield damage: {weapon.shield_damage}")
    imgui.text(f"Armor damage: {weapon.armor_damage}")
    imgui.text(f"Frequency: {weapon.frequency}")
    imgui.text(f"Range: {weapon.range}")
