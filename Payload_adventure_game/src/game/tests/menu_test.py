import unittest

import pygame

from game.gameloop.menu import Menu

class StubClock():
    def __init__(self) -> None:
        pass

class StubScreen():
    def __init__(self) -> None:
        pass



class TestMenu(unittest.TestCase):
    def test_menu_init(self):
        pygame.font.init()
        self.menu = Menu(StubClock, StubScreen, 10, (1920,1080))

    def test_menu_scaling(self):
        pygame.font.init()
        self.menu = Menu(StubClock, StubScreen, 10, (1920,1080))
        self.menu._use_current_scaling((1920,1080), 10)


