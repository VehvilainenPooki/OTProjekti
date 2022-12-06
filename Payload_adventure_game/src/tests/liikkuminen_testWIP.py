import sys
import unittest

import pygame

from logic.player import Player
from logic.movement import Movement

class TestLiikkuminen(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.player = Player()
        self.movement = Movement(self.player)
        self.keyboard = Controller()

    def test_walk_up(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        self.keyboard.press("w")
        self.movement.move()
        self.keyboard.release("w")
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[0] == end_pos[0], True)
        self.assertEqual(start_pos[1]-end_pos[1] == 5, True)

    def test_walk_down(self):
        start_pos = self.player.get_pos()
        self.keyboard.press("s")
        self.movement.move()
        self.keyboard.release("s")
        end_pos = self.player.get_pos()
        self.assertEqual(start_pos[0] == end_pos[0], True)
        self.assertEqual(start_pos[1]-end_pos[1] == -5, True)

    def test_walk_left(self):
        start_pos = self.player.get_pos()
        self.keyboard.press("a")
        self.movement.move()
        self.keyboard.release("a")
        end_pos = self.player.get_pos()
        self.assertEqual(start_pos[1] == end_pos[1], True)
        self.assertEqual(start_pos[0]-end_pos[0] == 5, True)

    def test_walk_right(self):
        start_pos = self.player.get_pos()
        self.keyboard.press("d")
        self.movement.move()
        self.keyboard.release("d")
        end_pos = self.player.get_pos()
        self.assertEqual(start_pos[1] == end_pos[1], True)
        self.assertEqual(start_pos[0]-end_pos[0] == -5, True)

class main:
    pygame.init()
    player = Player()
    movement = Movement(player)
    keyboard = Controller()
    screen = pygame.display.set_mode((100,100))
    pygame.display.set_caption("Playload_adventure_game")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()
        screen.blit(pygame.Surface((100,100)), (0,0))
        print(str(pygame.key.get_pressed()[pygame.K_w]) + "\n")
        keyboard.press("w")
        print(str(pygame.key.get_pressed()[pygame.K_w]) + "\n")
        keyboard.release("w")
        print(str(pygame.key.get_pressed()[pygame.K_w]))
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    main()
