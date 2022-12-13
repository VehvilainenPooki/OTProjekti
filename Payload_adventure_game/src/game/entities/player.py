import os

import pygame


dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, starting_x = 0, starting_y = 0, player_radius = 10, player_health = 20):

        super() .__init__()

        self.posx = starting_x
        self.posy = starting_y
        self.hitbox_radius = player_radius
        self.health = player_health

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player", "player.png")
        )

        self.image = pygame.transform.scale(self.image, (self.hitbox_radius*2,self.hitbox_radius*2))

        self.rect = pygame.Rect((self.posx, self.posy),(self.hitbox_radius*2,self.hitbox_radius*2))

    def get_pos(self):
        return (self.posx, self.posy)

    def set_pos(self, new_x, new_y):
        self.posx = new_x
        self.posy = new_y
        self.rect.x = new_x
        self.rect.y = new_y

    def add_pos(self, addto_x, addto_y):
        self.posx += addto_x
        self.posy += addto_y
        self.rect.x = self.posx
        self.rect.y = self.posy

    def get_hitbox_r(self):
        return self.hitbox_radius
