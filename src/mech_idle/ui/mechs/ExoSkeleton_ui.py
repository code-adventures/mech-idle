

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

# Exo-Skeleton
#   Skill:
#       - Basic Mech control
#   Bonus:
#       - Chance to be hit 10% reduced per level MC
#       - Speed increased by 10% per level MC
#
#   Configuration:
#       - 1x weapon slot per arm

import imgui
from .. import fonts


def draw(hull):
    fonts.header_text("Exo-Skeleton")
    imgui.text("Chance to be hit reduced by 10% per level of Mech Control")
    imgui.text("Speed increased by 10% per level of Mech Control")

