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

from ..hull import MountPoints
from ..mechs import ExoSkeleton
from ..ui.mechs import ExoSkeleton_ui

selected = None

def text(text, disabled):
    if disabled:
        imgui.text_disabled(text)
    else:
        imgui.text(text)

def add_modules(mountpoints, location, label):
    text(f"{label}", mountpoints[location][0] + mountpoints[location][1] == 0) 

    if mountpoints[location][0] + mountpoints[location][1] == 0:
        return

    global selected

    for i in range(mountpoints[location][0]):
        opened, sel = imgui.selectable(f"  Weapon {i}##{location}", selected == (location, 0, i))
        if opened:
            selected = (location, 0, i)
    for i in range(mountpoints[location][1]):
        opened, sel = imgui.selectable(f"  Aux {i}##{location}", selected == (location, 1, i))
        if opened:
            selected = (location, 1, i)

def draw(setup):
    if isinstance(setup.hull, ExoSkeleton.ExoSkeleton):
        ExoSkeleton_ui.draw(setup.hull)
    else:
        imgui.text("No drawing instructions for hull of type {type(hull)}")

    with imgui.begin_list_box("##modules", 200, 500) as modules:
        if modules.opened:
            add_modules(setup.hull.mountpoints, MountPoints.HEAD, "Head:")
            add_modules(setup.hull.mountpoints, MountPoints.TORSO, "Torso:")
            add_modules(setup.hull.mountpoints, MountPoints.LEFT_ARM, "Left arm:")
            add_modules(setup.hull.mountpoints, MountPoints.RIGHT_ARM, "Right arm:")
            add_modules(setup.hull.mountpoints, MountPoints.LEFT_SHOULDER, "Left shoulder:")
            add_modules(setup.hull.mountpoints, MountPoints.RIGHT_SHOULDER, "Right shoulder:")
            add_modules(setup.hull.mountpoints, MountPoints.LEFT_LEG, "Left leg:")
            add_modules(setup.hull.mountpoints, MountPoints.RIGHT_LEG, "Right leg:")
    imgui.same_line()
    with imgui.begin_group():
        if selected is not None:
            module = setup.modules[selected[0]][selected[1]][selected[2]]
            imgui.text(f"{module.name}")            
