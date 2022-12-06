import unittest

from logic.player import Player
from logic.collisions import Collisions
from logic.movement import Movement
from logic.terrainsprite import TerrainSprite

class TestCollision(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.collisions = Collisions(self.player)
        self.movement = Movement(self.player)
        self.circle = TerrainSprite(200 ,200 , 50)
    
    def test_no_collision(self):
        self.assertEqual(self.collisions.are_colliding(self.circle), False)
    
    def test_collision(self):
        self.player.set_pos(290, 290)
        self.assertEqual(self.collisions.are_colliding(self.circle), True)
    
    def test_collision_push_works(self):
        self.player.set_pos(280, 280)
        self.movement.remove_collision(self.circle)
        self.assertEqual(self.collisions.are_colliding(self.circle), False)
    
    def test_remove_collision_push_works_in_the_middle(self):
        self.player.set_pos(290, 290)
        self.movement.remove_collision(self.circle)
        self.movement.remove_collision(self.circle)
        self.assertEqual(self.collisions.are_colliding(self.circle), False)