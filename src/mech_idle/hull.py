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

from dataclasses import dataclass
from functools import reduce
from enum import IntEnum
import imgui

class MountPoints(IntEnum):
    HEAD = 0
    TORSO = 1
    LEFT_ARM = 2
    RIGHT_ARM = 3
    LEFT_SHOULDER = 4
    RIGHT_SHOULDER = 5
    LEFT_LEG = 6
    RIGHT_LEG = 7

@dataclass
class Hull:
    id: int
    name: str
    speed: int
    mountpoints: dict[MountPoints, tuple[int, int]] = None

    @staticmethod
    def create_mountpoints(**mountpoints):
        return { MountPoints.HEAD: mountpoints.get('head', (0,0)),
                 MountPoints.TORSO: mountpoints.get('torso', (0,0)),
                 MountPoints.LEFT_ARM: mountpoints.get('left_arm', (0,0)),
                 MountPoints.RIGHT_ARM: mountpoints.get('right_arm', (0,0)),
                 MountPoints.LEFT_SHOULDER: mountpoints.get('left_shoulder', (0,0)),
                 MountPoints.RIGHT_SHOULDER: mountpoints.get('right_shoulder', (0,0)),
                 MountPoints.LEFT_LEG: mountpoints.get('left_leg', (0,0)),
                 MountPoints.RIGHT_LEG: mountpoints.get('right_leg', (0,0)) }

    def get_speed(self, skills):
        return self.speed


hulls : list[Hull] =  [Hull(0, "Toshido Hellcat", 5, Hull.create_mountpoints(head=(2,1), left_arm=(1,0), right_arm=(1,0))),
                       Hull(1, 'KPB "Panzer" XE-R4a', 2, Hull.create_mountpoints(left_arm=(1,0), right_arm=(1,0),torso=(0,2), left_leg=(0,1), right_leg=(0,1))),
                       Hull(2, "Yatoshi Dragon", 1, Hull.create_mountpoints(left_arm=(1,0), right_arm=(1,0), torso=(0,2)))]
