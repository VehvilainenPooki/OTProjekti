import os

import pygame

from .menu import Menu
from .adventure import Adventure

dirname = os.path.dirname(__file__)

class GameloopHandler():
    def __init__(self):
        # Initialising window
        self.resolution = (1920, 1080)
        #resolution = (720, 576)
        self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME)
        pygame.display.set_caption("Playload_adventure_game")
        self.clock = pygame.time.Clock()


        background = pygame.Surface(self.resolution)
        background.fill((100,100,100))

        self.adventure = Adventure()
        self.menu = Menu(self.clock, self.screen)

        pygame.init()

    def start_menu(self):
        running = True
        while running:
            pygame.mouse.set_visible(True)
            action = self.menu.mainmenu_screen()
            if action == "Start":
                self.adventure.gameloop(self.clock, self.screen, self.resolution)
            elif action == "Settings":
                self.menu.settingsmenu_screen()
            elif action == "Quit":
                running = False
        pygame.quit()
