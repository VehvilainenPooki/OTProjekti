import os

import pygame

from .menu import Menu
from .adventure import Adventure

dirname = os.path.dirname(__file__)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

class GameloopHandler():
    def __init__(self):
        # Initialising window
        self.resolution = None
        self.scale = None
        self._read_config()
        #resolution = (720, 576)
        self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME)
        pygame.display.set_caption("Playload_adventure_game")
        self.clock = pygame.time.Clock()

        self.adventure = Adventure(self.clock, self.screen, self.scale, self.resolution)
        pygame.font.init()
        self.menu = Menu(self.clock, self.screen, self.scale, self.resolution)

        pygame.init()

    def start_loop(self):
        running = True
        while running:
            pygame.mouse.set_visible(True)
            action = self.menu.mainmenu_screen(self.resolution,self.scale)
            if action == "Start":
                self.adventure.gameloop(self.clock, self.screen, self.scale, self.resolution)
            elif action == "Settings":
                settings_action = self.menu.settingsmenu_screen(self.resolution, self.scale)
                if settings_action[0] == "Apply":
                    self._change_scaling(settings_action[1])
            if action == "Quit":
                running = False
        pygame.quit()

    def _change_scaling(self, resolution):
        self.resolution = resolution
        config = open(os.path.join(dirname, "..","config.txt"), "w")
        config.seek(0)
        config.write("resolution " + str(resolution[0])+","+str(resolution[1]) + "\n")
        if resolution == (720,480):
            self.scale = 5
        elif resolution == (1920,1080):
            self.scale = 10
        elif resolution == (2560,1440):
            self.scale = 13
        elif resolution == (3840,2160):
            self.scale = 20
        config.write("scale " + str(self.scale))
        config.close()

        self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME)

    def _read_config(self):
        config = open(os.path.join(dirname, "..","config.txt"), "r")
        raw = config.readline().split(" ")[1].strip().split(",")
        self.resolution = (int(raw[0]), int(raw[1]))
        print(self.resolution)
        self.scale = int(config.readline().split(" ")[1])
        config.close

