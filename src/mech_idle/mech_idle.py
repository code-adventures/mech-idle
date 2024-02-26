import pygame
import imgui
from imgui.integrations.pygame import PygameRenderer
import sys
import OpenGL.GL as gl

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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        impl.process_event(event)
    impl.process_inputs()

    imgui.new_frame()

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item(
                "Quit", "Cmd+Q", False, True
            )
            if clicked_quit:
                sys.exit(0)

            imgui.end_menu()
        imgui.end_main_menu_bar()

        imgui.set_next_window_size(300, 300)
        with imgui.begin("Mech stats", False, flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE):
            imgui.text("Hardpoints")
            imgui.text("Speed")

    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    impl.render(imgui.get_draw_data())

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
