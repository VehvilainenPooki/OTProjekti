import os

import pygame


dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """Class that gives the primary information about the player

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self, starting_x=0, starting_y=0, player_radius=10, player_health=20):
        """Classes constructor which creates the player

        Args:
            starting_x (int, optional): Player starting position X. Defaults to 0.
            starting_y (int, optional): Player starting position Y. Defaults to 0.
            player_radius (int, optional): Player hitbox radius. Defaults to 10.
            player_health (int, optional): Player max health. Defaults to 20.
        """
        super() .__init__()

        self.posx = starting_x
        self.posy = starting_y
        self.hitbox_radius = player_radius
        self.max_health = player_health

        self.original_image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player", "player.png")
        )

        self.image = pygame.transform.scale(
            self.get_original_image(), (self.hitbox_radius*2, self.hitbox_radius*2))

        self.rect = pygame.Rect((self.posx, self.posy),
                                (self.hitbox_radius*2, self.hitbox_radius*2))

    def get_pos(self):
        return (self.rect.x, self.rect.y)

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

    def get_original_image(self):
        return self.original_image
