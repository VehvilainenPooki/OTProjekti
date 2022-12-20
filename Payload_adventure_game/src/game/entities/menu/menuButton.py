import os

import pygame


dirname = os.path.dirname(__file__)

class MenuButton(pygame.sprite.Sprite):
    """Menu buttons base class

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self, path, pos_x=0, pos_y=0, scale=1):
        """Classes constructor which makes a menu button

        Args:
            image (path): the path to the buttons texture.
            pos_x (int, optional): Player starting position X. Defaults to 0.
            pos_y (int, optional): Player starting position Y. Defaults to 0.
            scale (int, optional): Scale of the sprite compared to the image. Defaults to 1.
        """
        super() .__init__()
        self.scale = scale

        self.original_image = pygame.image.load(path)
        w,h = self.original_image.get_size()
        width = w*scale
        height = h*scale
        self.size = (width, height)
        self.image = pygame.transform.scale(
            self.original_image, self.size)
        self.rect = pygame.Rect((pos_x, pos_y), self.size)

    def pointer_is_on(self):
        self._add_button_brightness()

    def pointer_is_off(self):
        self._restore_button_brightness()

    def _add_button_brightness(self):
        w, h = self.image.get_size()
        for x in range(w):
            for y in range(h):
                pixel = self.image.get_at((x,y))
                if pixel[3] > 0:
                    self.image.set_at((x,y),pygame.Color(self._change_color_value(pixel[0], 50),self._change_color_value(pixel[1], 50),self._change_color_value(pixel[2], 50),pixel[3]))

    def _restore_button_brightness(self):
        self.image = pygame.transform.scale(
            self.original_image, self.size)

    def _change_color_value(self, color, change):
        new = color + change
        if new > 255:
            new = 255
        elif new < 0:
            new = 0
        return new

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect
