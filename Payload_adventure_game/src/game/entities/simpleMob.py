import os

import pygame


dirname = os.path.dirname(__file__)


class Simplemob(pygame.sprite.Sprite):
    """Class that defines a simple mob

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self, starting_x=0, starting_y=0, mob_size=10, health=20, vision_radius=100):
        """Classes constructor which creates the player

        Args:
            starting_x (int, optional): mob starting position X. Defaults to 0.
            starting_y (int, optional): mob starting position Y. Defaults to 0.
            mob_size (int, optional): mob hitbox size. Defaults to 10.
            mob_health (int, optional): mob health. Defaults to 5.
            vision_radius (int, optional): How far the mob can see the player. Defaults to 100.
        """
        super() .__init__()

        self.hitbox_radius = mob_size
        self.max_health = health
        self.current_health = health
        self.vision_radius = vision_radius

        self.original_image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "mobs", "mob1.png")
        )

        self.image = pygame.transform.scale(
            self.original_image, (self.hitbox_radius*2, self.hitbox_radius*2))

        self.rect = pygame.Rect((starting_x, starting_y),
                                (self.hitbox_radius*2, self.hitbox_radius*2))

    def get_pos(self):
        return (self.rect.x, self.rect.y)
    
    def get_rendering_pos(self):
        i_size = self.image.get_rect().center
        pos = (self.rect[0]-i_size[0]+self.hitbox_radius,self.rect[1]-i_size[1]+self.hitbox_radius)
        return pos

    def set_pos(self, new_x, new_y):

        self.rect.x = new_x
        self.rect.y = new_y

    def add_pos(self, addto_x, addto_y):
        self.rect.x += addto_x
        self.rect.y += addto_y

    def get_hitbox_r(self):
        return self.hitbox_radius

    def get_original_image(self):
        return self.original_image
