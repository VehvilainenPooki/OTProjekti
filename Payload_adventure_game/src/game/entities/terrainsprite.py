import os
import pygame

dirname = os.path.dirname(__file__)


class TerrainSprite(pygame.sprite.Sprite):
    """Stationary Sprite with a circle hitbox

    Args:
        pygame (Sprite): Pygame sprite super
    """

    def __init__(self, pos_x, pos_y, hitbox_radius, sprite_size, sprite_image_index):
        """Classes constructor which creates an instance of a TerrainSprite

        Args:
            pos_x (int, optional): X coordinate of the sprite.
            pos_y (int, optional): Y coordinate of the sprite.
            radius (int, optional): Radius of the sprite.
        """
        self.posx = pos_x
        self.posy = pos_y
        self.hitbox_radius = hitbox_radius
        self.sprite_size = sprite_size
        self.image_index = int(sprite_image_index)

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "trees", "tree" + str(self.image_index)+ ".png")
        )

        self.image = pygame.transform.scale(
            self.image, (self.sprite_size, self.sprite_size))
        self.rect = pygame.Rect((self.posx, self.posy),
                                (self.sprite_size, self.sprite_size))

    def get_hitbox_r(self):
        return self.hitbox_radius

    def get_rendering_pos(self):
        return (self.posx, self.posy)
