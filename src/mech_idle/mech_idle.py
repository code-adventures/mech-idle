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

import pygame
import OpenGL.GL as gl
import imgui
from imgui.integrations.pygame import PygameRenderer

from . import definitions
from . import update
from . import debug
from .game import Game
from .ui import definitions as ui_definitions
from .ui import drawing
from .ui import player_ui
from .ui import game_ui
from .ui import setup_ui
from .ui import fonts


def show_mech_information():
    pass

def show_skills():
    pass

def show_components():
    pass

def show_content_area(action_height, width):
    imgui.set_next_window_position(width, 0)
    imgui.set_next_window_size(imgui.get_io().display_size.x - width, imgui.get_io().display_size.y - action_height)
    with imgui.begin("Content", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        with imgui.begin_tab_bar("MyTabBar") as tab_bar:
            if tab_bar.opened:
                with imgui.begin_tab_item("Player") as item1:
                    if item1.selected:
                        player_ui.draw(game.player)
                with imgui.begin_tab_item("Mech information") as item1:
                    if item1.selected:
                        setup_ui.draw(game.player.setup)
#               with imgui.begin_tab_item("Skills") as item2:
#                   if item2.selected:
#                       show_skills()
#               with imgui.begin_tab_item("Components") as item3:
#                   if item3.selected:
#                       show_components()
#               with imgui.begin_tab_item("Available hulls") as item4:
#                   if item4.selected:
#                       hull.show_available_hulls()
        pass

#debugging window
    ch = imgui.get_io().display_size.y - action_height
    debug_win_height = 300
    imgui.set_next_window_position(width, ch - debug_win_height)
    imgui.set_next_window_size(imgui.get_io().display_size.x - width, debug_win_height)
    with imgui.begin("Debug", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        debug.print_msgs()

def show_info_area(action_height):
    width = 250
    imgui.set_next_window_position(0, 0)
    imgui.set_next_window_size(width, imgui.get_io().display_size.y - action_height)
    with imgui.begin("Game Info", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        game_ui.draw(game)
    return width

def show_action_area():
    dim = ui_definitions.action_window_dimensions()
    height = imgui.get_io().display_size.x / (dim.x/dim.y)
    imgui.set_next_window_position(0, imgui.get_io().display_size.y - height)
    imgui.set_next_window_size(imgui.get_io().display_size.x, height)
    with imgui.begin("Action", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE):
        ratio = imgui.get_window_content_region_width() / definitions.ACTION_AREA.x
        pos = imgui.get_window_position()
        transform = drawing.Transform(pos, ratio)
        draw_list = imgui.get_window_draw_list()
        drawing.draw(transform, draw_list)
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

fonts.load_fonts(impl)

game = Game()

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

    with imgui.font(fonts.normal):
        height = show_action_area()
        width = show_info_area(height)
        show_content_area(height, width)

    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    impl.render(imgui.get_draw_data())

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
