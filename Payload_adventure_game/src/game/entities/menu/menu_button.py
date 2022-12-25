import os

import pygame


dirname = os.path.dirname(__file__)


class MenuButton(pygame.sprite.Sprite):
    """Menu buttons base class

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self, path, action, pos_x, pos_y, scale):
        """Classes constructor which makes a menu button

        Args:
            path (path): The path to the buttons texture.
            action (str): Action that the button does.
            pos_x (int): Player starting position X.
            pos_y (int): Player starting position Y.
            scale (int): Scale of the sprite compared to the image.
        """
        super() .__init__()
        self.scale = scale
        self.action = action

        self.original_image = pygame.image.load(path)
        width, height = self.original_image.get_size()
        width = width*scale
        height = height*scale
        self.size = (width, height)
        self.image = pygame.transform.scale(
            self.original_image, self.size)
        self.rect = pygame.Rect((pos_x, pos_y), self.size)

    def change_pos_scale(self, pos_x, pos_y, scale):
        """Changes button position and scale.

        Args:
            pos_x (int): Buttons new positions x.
            pos_y (int): Buttons new positions y.
            scale (int): The scaling value. 10 is normal for 1080p
        """
        width, height = self.original_image.get_size()
        width = width*scale
        height = height*scale
        self.size = (width, height)
        self.image = pygame.transform.scale(
            self.original_image, self.size)
        self.rect = pygame.Rect((pos_x, pos_y), self.size)

    def button_action(self):
        """Returns the action that the button has.

        Returns:
            str: The action that the button has.
        """
        return self.action

    def pointer_is_on(self):
        """Method that is called when the mouse pointer hovers on the button
        highlighting the button.
        """
        self._add_button_brightness()

    def pointer_is_off(self):
        """Method that is called when the mouse pointer doesn't
        hover the button anymore. Restores the button brightness.
        """
        self._restore_button_brightness()

    def _add_button_brightness(self):
        """Method to increase brightness of the button.
        """
        width, height = self.image.get_size()
        for posx in range(width):
            for posy in range(height):
                pixel = self.image.get_at((posx, posy))
                if pixel[3] > 0:
                    self.image.set_at((posx, posy), pygame.Color(
                        self._change_color_value(pixel[0], 50), self._change_color_value(pixel[1], 50), self._change_color_value(pixel[2], 50), pixel[3]))

    def _restore_button_brightness(self):
        """method to restore the button brightness.
        """
        self.image = pygame.transform.scale(
            self.original_image, self.size)

    def _change_color_value(self, color, change):
        """Method that increases all the R,G,B values of color by change.
        This method checks that the values stay within 0-255.

        Args:
            color (tuple): RGB color value.
            change (int): How much the color will be changed.

        Returns:
            tuple: The changed RGB color value.
        """
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
