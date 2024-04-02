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
from pathlib import Path
import os

normal = None
header = None

def header_text(text):
    with imgui.font(header):
        imgui.text(text)
        imgui.separator()

def load_fonts(impl):
    global normal
    global header

    font_dir = Path(__file__).parent.parent.parent.parent / "res"
    fontfile = os.path.join(font_dir, "SpaceMono-Regular.ttf")
    normal = imgui.get_io().fonts.add_font_from_file_ttf(fontfile, 20)
    header = imgui.get_io().fonts.add_font_from_file_ttf(fontfile, 30)
    impl.refresh_font_texture()
