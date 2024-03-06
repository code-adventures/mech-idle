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

import sys
from pathlib import Path
import os

import pygame
import OpenGL.GL as gl
import imgui
from imgui.integrations.pygame import PygameRenderer

import mech
import hull
import action
import drawing
import update


def show_mech_information():
    pass

def show_skills():
    pass

def show_components():
    pass

def show_content_area(action_height):
    imgui.set_next_window_position(0, 0)
    imgui.set_next_window_size(imgui.get_io().display_size.x, imgui.get_io().display_size.y - action_height)
    with imgui.begin("Content", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        with imgui.begin_tab_bar("MyTabBar") as tab_bar:
            if tab_bar.opened:
                with imgui.begin_tab_item("Mech information") as item1:
                    if item1.selected:
                        show_mech_information()
                with imgui.begin_tab_item("Skills") as item2:
                    if item2.selected:
                        show_skills()
                with imgui.begin_tab_item("Components") as item3:
                    if item3.selected:
                        show_components()
                with imgui.begin_tab_item("Available hulls") as item4:
                    if item4.selected:
                        hull.show_available_hulls()
        pass

def show_action_area():
    dim = action.dimensions()
    height = imgui.get_io().display_size.x / (dim.x/dim.y)
    imgui.set_next_window_position(0, imgui.get_io().display_size.y - height)
    imgui.set_next_window_size(imgui.get_io().display_size.x, height)
    with imgui.begin("Action", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        drawing.draw()
    return height

    
size = 1280, 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)

# imgui setup
imgui.create_context()
imgui.get_io().display_size = size

impl = PygameRenderer()

clock = pygame.time.Clock()
running = True

# fonts
font_dir = Path(__file__).parent.parent.parent / "res"
fonts = imgui.get_io().fonts
fontfile = os.path.join(font_dir, "SpaceMono-Regular.ttf")
font = fonts.add_font_from_file_ttf(fontfile, 20)
impl.refresh_font_texture()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        impl.process_event(event)
    impl.process_inputs()

    clock.tick(60)  # limits FPS to 60
    time = pygame.time.get_ticks()

    update.update(time)

    imgui.new_frame()

    with imgui.font(font):
        height = show_action_area()
        show_content_area(height)

    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    impl.render(imgui.get_draw_data())

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
