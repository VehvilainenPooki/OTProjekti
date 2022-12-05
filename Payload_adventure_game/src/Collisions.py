import pygame
import math

from player import Player

class Collisions:

    def __init__(self, p):
        self.player = p
        self.p_radius = self.player.get_hitbox_r()
    
    def are_colliding(self, circle):
        d = math.dist(self.player.rect.center, circle.rect.center)
        r = circle.get_hitbox_r()
        if self.p_radius+r > d:
            return True
        return False