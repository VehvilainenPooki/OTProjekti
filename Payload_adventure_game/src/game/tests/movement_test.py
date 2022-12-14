import sys
import unittest

import pygame

from ..entities.player import Player
from ..entities.pointer import Pointer
from ..logic.movement import Movement


class StubPointer():
    def __init__(self) -> None:
        self.pos = (0,0)

    def spin(self):
        self.pos = (self.pos[0]+100,self.pos[1])

    def get_pos(self):
        return self.pos

class TestMovement(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.player = Player()
        self.pointer = StubPointer()
        self.movement = Movement(self.player, self.pointer)

    def test_walk_up(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: True, pygame.K_s: False,
                pygame.K_a: False, pygame.K_d: False}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[0] == end_pos[0], True)
        self.assertEqual(start_pos[1]-end_pos[1] == 5, True)

    def test_walk_down(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: False, pygame.K_s: True,
                pygame.K_a: False, pygame.K_d: False}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[0] == end_pos[0], True)
        self.assertEqual(start_pos[1]-end_pos[1] == -5, True)

    def test_walk_left(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: False, pygame.K_s: False,
                pygame.K_a: True, pygame.K_d: False}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[1] == end_pos[1], True)
        self.assertEqual(start_pos[0]-end_pos[0] == 5, True)

    def test_walk_right(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: False, pygame.K_s: False,
                pygame.K_a: False, pygame.K_d: True}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[1] == end_pos[1], True)
        self.assertEqual(start_pos[0]-end_pos[0] == -5, True)

    def test_walk_right_down(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: False, pygame.K_s: True,
                pygame.K_a: False, pygame.K_d: True}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[1]-end_pos[1] == -5, True)
        self.assertEqual(start_pos[0]-end_pos[0] == -5, True)

    def test_walk_left_up(self):
        start_pos = self.player.get_pos()
        print(start_pos)
        keys = {pygame.K_w: True, pygame.K_s: False,
                pygame.K_a: True, pygame.K_d: False}
        self.movement._take_a_step(keys, 5)
        end_pos = self.player.get_pos()
        print(end_pos)
        self.assertEqual(start_pos[1] - end_pos[1] == 5, True)
        self.assertEqual(start_pos[0]-end_pos[0] == 5, True)

    def test_walking(self):
        keys = {pygame.K_LCTRL: False, pygame.K_LSHIFT: False}
        self.assertEqual(self.movement._movement_speed(keys) == 5, True)

    def test_crawling(self):
        keys = {pygame.K_LCTRL: True, pygame.K_LSHIFT: False}
        self.assertEqual(self.movement._movement_speed(keys) == 3, True)

    def test_running(self):
        keys = {pygame.K_LCTRL: False, pygame.K_LSHIFT: True}
        self.assertEqual(self.movement._movement_speed(keys) == 7, True)

    def test_dash_with_SPACE(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: False,
                pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (0, -10, 20, 20), True)

    def test_dash_with_SPACE_w(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: True,
                pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (0, -10, 20, 20), True)

    def test_dash_with_SPACE_s(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: False,
                pygame.K_s: True, pygame.K_a: False, pygame.K_d: False}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (0, 10, 20, 20), True)

    def test_dash_with_SPACE_a(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: False,
                pygame.K_s: False, pygame.K_a: True, pygame.K_d: False}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (-10, 0, 20, 20), True)

    def test_dash_with_SPACE_d(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: False,
                pygame.K_s: False, pygame.K_a: False, pygame.K_d: True}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (10, 0, 20, 20), True)

    def test_dash_with_SPACE_w_a(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: True,
                pygame.K_s: False, pygame.K_a: True, pygame.K_d: False}
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (-10, -10, 20, 20), True)

    def test_dash_with_SPACE_s_d(self):
        keys = {pygame.K_SPACE: True, pygame.K_w: False,
                pygame.K_s: True, pygame.K_a: False, pygame.K_d: True}
        self.movement._dash(keys)
        self.movement._dash(keys)
        print(self.player.rect)
        self.assertEqual(self.player.rect == (20, 20, 20, 20), True)

    def test_looking_at(self):
        self.movement._update_pointer_pos()
        self.movement._look_at_pointer((1920,1080))

    def test_pointer_moves(self):
        pointer = Pointer()
        pointer.spin()
        self.assertEqual((0,0) == pointer.get_pos(), True)