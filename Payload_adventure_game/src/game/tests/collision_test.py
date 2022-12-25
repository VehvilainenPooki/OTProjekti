import unittest

from ..entities.player import Player
from ..logic.collisions import Collisions
from ..entities.terrain_sprite import TerrainSprite


class TestCollision(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.collisions = Collisions(self.player)
        self.circle = TerrainSprite(200, 200, 50, 200, 1)

    def test_no_collision(self):
        self.assertEqual(self.collisions.are_colliding(self.circle), False)

    def test_remove_collision_without_collision(self):
        self.collisions.remove_collision(self.circle)
        self.assertEqual(self.player.rect == (0, 0, 20, 20), True)

    def test_collision(self):
        self.player.set_pos(290, 290)
        self.assertEqual(self.collisions.are_colliding(self.circle), True)

    def test_collision_push_works(self):
        self.player.set_pos(280, 280)
        self.collisions.remove_collision(self.circle)
        print(self.player.get_pos())
        self.assertEqual(self.collisions.are_colliding(self.circle), False)

    def test_remove_collision_push_works_in_the_middle(self):
        self.player.set_pos(290, 290)
        self.collisions.remove_collision(self.circle)
        self.collisions.remove_collision(self.circle)
        print(self.player.get_pos())
        self.assertEqual(self.collisions.are_colliding(self.circle), False)
