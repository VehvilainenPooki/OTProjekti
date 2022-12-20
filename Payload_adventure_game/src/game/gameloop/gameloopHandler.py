import os

import pygame

from .menu import Menu
from .adventure import Adventure

dirname = os.path.dirname(__file__)

class GameloopHandler():
    def __init__(self):
        # Initialising window
        resolution = (1920, 1080)
        #resolution = (720, 576)
        screen = pygame.display.set_mode(resolution, pygame.NOFRAME)
        pygame.display.set_caption("Playload_adventure_game")
        clock = pygame.time.Clock()


        background = pygame.Surface(resolution)
        background.fill((100,100,100))

        self.adventure = Adventure()
        self.menu = Menu(clock, screen)

        pygame.init()

    def start(self):
        action = self.menu.mainmenu_screen()
        if action == "Start":
            self.adventure.gameloop()
