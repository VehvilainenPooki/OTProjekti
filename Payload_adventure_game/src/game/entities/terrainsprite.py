import os
import pygame

dirname = os.path.dirname(__file__)


class TerrainSprite(pygame.sprite.Sprite):
    """Stationary Sprite with a circle hitbox

    Args:
        pygame (Sprite): Pygame sprite super
    """

    def __init__(self, pos_x=0, pos_y=0, radius=20):
        """Classes constructor which creates an instance of a TerrainSprite

        Args:
            pos_x (int, optional): X coordinate of the sprite. Defaults to 0.
            pos_y (int, optional): Y coordinate of the sprite. Defaults to 0.
            radius (int, optional): Radius of the sprite. Defaults to 20.
        """
        self.posx = pos_x
        self.posy = pos_y
        self.hboxr = radius

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "trees", "tree1.png")
        )

        self.image = pygame.transform.scale(
            self.image, (self.hboxr*4, self.hboxr*4))
        self.rect = pygame.Rect((self.posx, self.posy),
                                (self.hboxr*4, self.hboxr*4))

    def get_hitbox_r(self):
        return self.hboxr
