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

        self.original_image = self.font.render(text, True, (255, 255, 255))
        width, height = self.original_image.get_size()
        self.image = pygame.transform.scale(
            self.original_image, (width*scale, height*scale))
        self.rect = pygame.Rect((pos_x, pos_y), (width*scale, height*scale))

    def change_pos_scale(self, pos_x, pos_y, scale):
        """Method to change the position and scale of the text sprite

        Args:
            pos_x (int): The new x position
            pos_y (int): The new y position
            scale (int): the new scale
        """
        self.posx = pos_x
        self.posy = pos_y
        self.scale = scale
        width, height = self.original_image.get_size()
        size = (width*scale, height*scale)
        self.image = pygame.transform.scale(
            self.original_image, size)
        self.rect = pygame.Rect((pos_x, pos_y), size)

    def change_text(self, new_text):
        """method to update the text.

        Args:
            new_text (str): The new text.
        """
        self.original_image = self.font.render(new_text, True, (255, 255, 255))
        width, height = self.original_image.get_size()
        self.image = pygame.transform.scale(
            self.original_image, (width*self.scale, height*self.scale))
        self.rect = pygame.Rect((self.posx, self.posy),
                                (width*self.scale, height*self.scale))

    def button_action(self):
        """Returns the action that the button has.

        Returns:
            str: The action that the button has.
        """
        return None

    def pointer_is_on(self):
        """Method that is called when the mouse pointer hovers on the button.
        Text_sprite doesn't do anything.
        """

    def pointer_is_off(self):
        """Method that is called when the mouse pointer doesn't
        hover the button anymore.Text_sprite doesn't do anything.
        """

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect
