import os

import pygame


dirname = os.path.dirname(__file__)

class TextSprite(pygame.sprite.Sprite):
    """Class that makes text sprites.

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self, text="Hello world!", font=None, pos_x=0, pos_y=0, scale=1):
        """Classes constructor which makes a text sprite

        Args:
            text (str, optional): The sprites text. Defaults to "Hello world!"
            font (str, optional): The font of the text. Defaults to None
            pos_x (int, optional): Player starting position X. Defaults to 0.
            pos_y (int, optional): Player starting position Y. Defaults to 0.
            scale (int, optional): Scale of the sprite compared to the image. Defaults to 1.
        """
        super() .__init__()
        self.scale = scale

        self.posx = pos_x
        self.posy = pos_y

        self.font = pygame.font.SysFont(font, 20)


        self.original_image = self.font.render(text, True, (255,255,255))
        w,h = self.original_image.get_size()
        self.image = pygame.transform.scale(
            self.original_image, (w*scale,h*scale))
        self.rect = pygame.Rect((pos_x, pos_y), (w*scale,h*scale))

    def change_pos_scale(self, pos_x, pos_y, scale):
        self.posx = pos_x
        self.posy = pos_y
        self.scale = scale
        w,h = self.original_image.get_size()
        size = (w*scale, h*scale)
        self.image = pygame.transform.scale(
            self.original_image, size)
        self.rect = pygame.Rect((pos_x, pos_y), size)

    def change_text(self, new_text):
        self.original_image = self.font.render(new_text, True, (255,255,255))
        w,h = self.original_image.get_size()
        self.image = pygame.transform.scale(
            self.original_image, (w*self.scale,h*self.scale))
        self.rect = pygame.Rect((self.posx, self.posy), (w*self.scale,h*self.scale))


    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect
